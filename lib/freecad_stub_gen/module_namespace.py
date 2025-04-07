import logging
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from functools import cached_property, partial
from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.file_functions import (
    genCppIiFiles,
    genXmlFiles,
    parseXml,
)
from freecad_stub_gen.generators.common.context import (
    currentPath,
    currentSource,
    getCurrentNamespace,
    initContext,
    isGuiInNamespace,
    isolatedContext,
)
from freecad_stub_gen.generators.common.cpp_function import findFunctionCall
from freecad_stub_gen.generators.common.names import (
    CLASS_TO_ALIAS,
    convertNamespaceToModule,
    getClassName,
    getModuleName,
    mergeModuleNames,
    removeAffix,
)
from freecad_stub_gen.generators.common.return_type_converter.str_wrapper import (
    StrWrapper,
)
from freecad_stub_gen.importable_map import importableMap

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ClassEntry:
    name: str
    module: str
    sourceType: str
    file: Path = field(default_factory=currentPath.get)

    @cached_property
    def sourceTypes(self):
        return self.sourceType.split(',')


type CppNameToClassEntrySet_t = defaultdict[str, set[ClassEntry]]
type CppNameToClassEntryList_t = defaultdict[str, list[ClassEntry]]


class DebugDefaultDict(defaultdict):
    def __getitem__(self, key):
        """Use this method to set breakpoint."""
        return super().__getitem__(key)


class _ModuleNamespace:
    def __init__(self, sourcePath: Path = SOURCE_DIR):
        self.sourcePath = sourcePath

        self.stemToPaths: defaultdict[str, list[Path]] = defaultdict(list)
        self.pathToXml: dict[Path, ET.Element] = {}

        cppNameToClassEntry: CppNameToClassEntrySet_t = DebugDefaultDict(set)
        for file in genXmlFiles(sourcePath):
            self.stemToPaths[file.stem].append(file)
            self._parseXml(file, cppNameToClassEntry)

        with isolatedContext():
            for file in genCppIiFiles(sourcePath):
                initContext(file)
                self._addFromPyTypeObject(cppNameToClassEntry)
                self._addFromInitType(cppNameToClassEntry)
                self._addFromClassTypeId(cppNameToClassEntry)

        # TODO @PO: maybe we should generate `__all__`
        #  in stubs for importable classes?
        #  or maybe use private module for not importable objects?
        cppNameToClassEntry['PyObjectBase'].add(
            ClassEntry('FreeCAD.PyObjectBase', 'FreeCAD', 'special')
        )

        for cppName, pythonName in importableMap.items():
            # it is visible from python, so we should prefer it over `tp_name`
            if (mod := getModuleName(pythonName)) is None:
                raise ValueError
            cppNameToClassEntry[cppName].add(
                ClassEntry(pythonName, mod, 'importableMap')
            )

        cppNameToClassEntrySeq = {k: list(v) for k, v in cppNameToClassEntry.items()}
        self.cppNameToClassEntry: CppNameToClassEntryList_t = defaultdict(
            list, sorted(cppNameToClassEntrySeq.items())
        )

    REG_PY_TYPE = re.compile(r'"(?P<klass>[.\w]+)"\s*,?\s*/\*tp_name\*/')

    def _addFromPyTypeObject(self, cppNameToClassEntry: CppNameToClassEntrySet_t):
        for match in self.REG_PY_TYPE.finditer(currentSource.get()):
            self._addClass(match, cppNameToClassEntry, 'tp_name')

    # TODO @PO: [P3] this is repeated in `FreecadStubGeneratorFromCppClass`
    REG_INIT_TYPE = re.compile(r'::init_type\([^{;]*{')
    REG_CLASS_NAME = re.compile(r'behaviors\(\)\.name\(\s*"(?P<klass>[\w.]+)"\s*\);')

    def _addFromInitType(self, cppNameToClassEntry: CppNameToClassEntrySet_t):
        for match in self.REG_INIT_TYPE.finditer(currentSource.get()):
            funcCall = findFunctionCall(currentSource.get(), match.start())
            if classMatch := self.REG_CLASS_NAME.search(funcCall):
                self._addClass(classMatch, cppNameToClassEntry, '::init_type')

    REG_TYPESYSTEM_SOURCE = re.compile(
        r'Base::Type (?P<mod>\w+)::(?P<klass>\w+)\s*::\s*getClassTypeId\(void\)'
    )

    def _addFromClassTypeId(self, cppNameToClassEntry: CppNameToClassEntrySet_t):
        for match in self.REG_TYPESYSTEM_SOURCE.finditer(currentSource.get()):
            self._addClass(match, cppNameToClassEntry, 'TYPESYSTEM_SOURCE')

    @classmethod
    def _addClass(
        cls,
        match: re.Match,
        cppNameToClassEntry: CppNameToClassEntrySet_t,
        sourceType: str,
    ):
        groups = match.groupdict()
        klass = groups['klass']
        if '.' in klass:
            moduleAndClass = klass
            klass = getClassName(moduleAndClass)
            if (mod := getModuleName(moduleAndClass)) is None:
                raise TypeError
            cppNameToClassEntry[klass].add(
                ClassEntry(moduleAndClass, mod, sourceType + ',dot')
            )
            return

        mod = groups.get('mod')
        if mod is None:
            ns = getCurrentNamespace()
            mod = convertNamespaceToModule(ns)

        cppNameToClassEntry[klass].add(ClassEntry(f'{mod}.{klass}', mod, sourceType))

    def _parseXml(self, file: Path, cppNameToClassEntry: CppNameToClassEntrySet_t):
        root = parseXml(file).getroot()
        if (exportElem := root.find('PythonExport')) is None:
            raise ValueError

        self.pathToXml[file] = root
        mod = self._getPythonModule(exportElem)

        cpp = self._getCppName(exportElem)
        py = self._getPythonName(exportElem)
        classWithModule = mergeModuleNames(mod, py)
        cppNameToClassEntry[cpp].add(ClassEntry(classWithModule, mod, 'xml_normal'))

        cppTwin = self._getCppTwinName(exportElem)
        pyTwin = self._getPythonName(exportElem)
        twinClassWithModule = mergeModuleNames(mod, pyTwin)
        cppNameToClassEntry[cppTwin].add(
            ClassEntry(twinClassWithModule, mod, 'xml_twin')
        )

    def _getCppName(self, elem: ET.Element) -> str:
        if name := elem.attrib.get('Name'):
            return name
        raise ValueError

    def _getCppTwinName(self, elem: ET.Element) -> str:
        if twinName := elem.attrib.get('Twin'):
            return twinName
        raise ValueError

    def _getPythonModule(self, elem: ET.Element) -> str:
        if namespace := elem.attrib.get('Namespace'):
            return convertNamespaceToModule(namespace)

        msg = "Cannot find namespace in xml"
        raise ValueError(msg)

    def _getPythonName(self, elem: ET.Element) -> str:
        for n in ('PythonName', 'Twin'):
            if (name := elem.attrib.get(n)) is not None:
                return CLASS_TO_ALIAS.get(name, name)

        msg = "Cannot find python name in xml"
        raise ValueError(msg)

    def getPythonNameFromCpp(self, namespace: str, cppName: str, *, deep=0) -> str:
        return self._getPythonNameFromCpp(namespace, cppName, deep=deep)

    def _getPythonNameFromCppSimple(
        self, namespace: str, cppName: str, pythonNames: list[str], *, deep: int
    ) -> str | None:
        match pythonNames:
            case []:
                match StrWrapper(cppName):
                    case 'SplitView3DInventorPy':
                        return 'AbstractSplitViewPy'

                    case 'StringIDRef':
                        fixedCppName = 'StringID'

                    case StrWrapper(end='Wrap' | 'Py') if deep == 0:
                        fixedCppName = removeAffix(cppName, suffixes=('Py', 'Wrap'))

                    case _ if deep == 0:
                        fixedCppName = cppName + 'Py'

                    case _:
                        msg = f"Cannot find `{cppName}`"
                        raise KeyError(msg)

                return self.getPythonNameFromCpp(namespace, fixedCppName, deep=deep + 1)

            case [onlyOne]:
                return onlyOne

            case ['FreeCAD.TypeId' | 'FreeCAD.BaseType', *_]:
                # TODO @PO: [P4] this is strange:
                #  - where is it defined, is there aliases?
                return 'FreeCAD.Base.TypeId'

            case _ if cppName == 'DocumentObject' and namespace == 'App':
                return 'FreeCADGui.DocumentObjectPy'

        return None

    def _filterPythonNames(
        self, pythonNames: list[str], predicate: Callable[[str], bool]
    ) -> str | None:
        fromCurrentNamespace = set()
        for p in pythonNames:
            if predicate(p):
                fromCurrentNamespace.add(p)

        if fromCurrentNamespace:
            return fromCurrentNamespace.pop()
        return None

    def _getPythonNameFromCpp(self, namespace: str, cppName: str, *, deep=0) -> str:
        classEntries = self.cppNameToClassEntry[cppName]
        pythonNames = [ce.name for ce in classEntries]

        pyName = self._getPythonNameFromCppSimple(
            namespace, cppName, pythonNames, deep=deep
        )
        if isinstance(pyName, str):
            return pyName

        # prefer from `importableMap`
        fromImportableMap = set()
        for ce in classEntries:
            if 'importableMap' in ce.sourceTypes:
                fromImportableMap.add(ce.name)
        if len(fromImportableMap) == 1:
            return fromImportableMap.pop()

        # try match current namespace
        ns = getCurrentNamespace()
        isCurNamespace = partial(self._isStartsWithNamespace, namespace=ns)
        if pyName := self._filterPythonNames(pythonNames, isCurNamespace):
            return pyName

        # try based on `Gui` in namespace
        if pyName := self._filterPythonNames(pythonNames, self._isGuiPackage):
            return pyName

        # we already should have provided module, so use it
        nsMod = convertNamespaceToModule(namespace)
        isCurModNamespace = partial(self._isStartsWithNamespace, namespace=nsMod)
        if pyName := self._filterPythonNames(pythonNames, isCurModNamespace):
            return pyName

        # TODO @PO: [P3] we should choose MeshObject over Mesh (MeshPy),
        #  because this is declared in PyTypeObject
        cpNameWithoutPy = cppName.removesuffix('Py')
        if any(cpNameWithoutPy == getClassName(onOk := on) for on in pythonNames):
            return onOk  # dirty hack for MeshPy

        currentMod = convertNamespaceToModule(ns)
        msg = f"Cannot choose class from `{pythonNames}` using module: `{currentMod}`"
        raise ValueError(msg)

    @classmethod
    def _isStartsWithNamespace(cls, packageName: str, namespace: str):
        return packageName.startswith(namespace)

    @classmethod
    def _isGuiPackage(cls, packageName: str) -> bool:
        if isGuiInNamespace():
            return 'Gui' in packageName
        return 'Gui' not in packageName

    def getFileForStem(self, stem: str, namespace: str = '') -> Path:
        match stem:  # if there is xml file, use this `match`
            case 'Geom2dCurvePy':
                stem = 'Curve2dPy'
            case 'GeomSurface':
                stem = 'GeometrySurface'

        match self.stemToPaths[stem]:
            case []:
                msg = f'There is no path for {stem=}'
                raise ValueError(msg)
            case [onlyOnePath]:
                return onlyOnePath
            case manyPaths if any(
                namespace in str(pathWithNamespace := p) for p in manyPaths
            ):
                # noinspection PyUnboundLocalVariable
                return pathWithNamespace
            case [anyPath, *_] as possiblePaths:
                paths = [p.relative_to(self.sourcePath) for p in possiblePaths]
                logger.warning(f'There is more than one possible {paths=}')
                return anyPath
            case _:
                raise NotImplementedError


__all__ = ['moduleNamespace']
moduleNamespace = _ModuleNamespace()
