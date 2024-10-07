import logging
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.file_functions import genCppIiFiles, genXmlFiles
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
                # self._addFromExtensions(cppNameToClassEntry)
                self._addFromPyTypeObject(cppNameToClassEntry)
                self._addFromInitType(cppNameToClassEntry)
                self._addFromClassTypeId(cppNameToClassEntry)

            # for file in genIiHFiles(sourcePath):
            #     initContext(file)
            #     self._addFromClassDeclaration(file, cppNameToClassEntry)

        # as usual in FreeCAD, there must be at least one exception
        # actually in runtime this shows __module__ == 'builtins'
        # TODO maybe: we should generate `__all__` in stubs for importable classes?
        cppNameToClassEntry['PyObjectBase'].add(
            ClassEntry('FreeCAD.PyObjectBase', 'FreeCAD', 'special')
        )

        for cppName, pythonName in importableMap.items():
            # it is visible from python, so we should prefer it over `tp_name`
            mod = getModuleName(pythonName)
            cppNameToClassEntry[cppName].add(
                ClassEntry(pythonName, mod, 'importableMap')
            )

        cppNameToClassEntrySeq = {k: list(v) for k, v in cppNameToClassEntry.items()}
        self.cppNameToClassEntry: CppNameToClassEntryList_t = defaultdict(
            list, sorted(cppNameToClassEntrySeq.items())
        )

    # REG_TEMPLATE = re.compile(r'Py::PythonExtension<(?P<klass>\w+)>')
    #
    # def _addFromExtensions(self, cppNameToClassEntry: CppNameToClassEntrySet_t):
    #     for match in self.REG_TEMPLATE.finditer(currentSource.get()):
    #         self._addClass(match, cppNameToClassEntry, 'PythonExtension')

    REG_PY_TYPE = re.compile(r'"(?P<klass>[.\w]+)"\s*,?\s*/\*tp_name\*/')

    def _addFromPyTypeObject(self, cppNameToClassEntry: CppNameToClassEntrySet_t):
        for match in self.REG_PY_TYPE.finditer(currentSource.get()):
            self._addClass(match, cppNameToClassEntry, 'tp_name')

    # TODO this is repeated in `FreecadStubGeneratorFromCppClass`
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

    # REG_CLASS_DECLARATION = re.compile(r'class\s+(?P<klass>\w+)\b')
    #
    # def _addFromClassDeclaration(self, hIiFile: Path, cppNameToClassEntry: cppNameToClassEntrySet_t):
    #     for match in self.REG_CLASS_DECLARATION.finditer(hIiFile.read_text()):
    #         self._addClass(match, cppNameToClassEntry)

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
            mod = getModuleName(moduleAndClass)
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
        root = ET.parse(file).getroot()
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
        classEntries = self.cppNameToClassEntry[cppName]
        pythonNames = [ce.name for ce in classEntries]
        match pythonNames:
            case []:
                match StrWrapper(cppName), deep:
                    case 'SplitView3DInventorPy', _:
                        return 'AbstractSplitViewPy'

                    case StrWrapper(end='Wrap' | 'Py'), 0:
                        fixedCppName = removeAffix(cppName, suffixes=('Py', 'Wrap'))

                    case _, 0:
                        fixedCppName = cppName + 'Py'

                    case _:
                        msg = f"Cannot find `{cppName}`"
                        raise KeyError(msg)

                return self.getPythonNameFromCpp(namespace, fixedCppName, deep=deep + 1)

            case [onlyOne]:
                return onlyOne

            case ['FreeCAD.TypeId' | 'FreeCAD.BaseType', *_]:
                # TODO this is strange - where is it defined, is there aliases?
                return 'FreeCAD.Base.TypeId'

        # prefer from `importableMap`
        fromImportableMap = set()
        for ce in classEntries:
            if 'importableMap' in ce.sourceTypes:
                fromImportableMap.add(ce.name)
        if len(fromImportableMap) == 1:
            return fromImportableMap.pop()

        # TODO [P5]: fix repeated code here

        # try match current namespace
        ns = getCurrentNamespace()
        currentMod = convertNamespaceToModule(ns)
        fromCurrentNamespace = set()
        for p in pythonNames:
            if p.startswith(currentMod):
                fromCurrentNamespace.add(p)
        if len(fromCurrentNamespace):
            return fromCurrentNamespace.pop()

        # try based on `Gui` in namespace
        isGui = isGuiInNamespace()
        possibleNames = set()
        for p in pythonNames:
            if (isGui and 'Gui' in p) or (not isGui and 'Gui' not in p):
                possibleNames.add(p)
        if len(possibleNames) == 1:
            return possibleNames.pop()

        # we already should have provided module, so use it
        nsMod = convertNamespaceToModule(namespace)
        possibleByNamespace = set()
        for p in pythonNames:
            if p.startswith(nsMod):
                possibleByNamespace.add(p)
        if len(possibleByNamespace) == 1:
            return possibleByNamespace.pop()

        # TODO P3: we should choose MeshObject over Mesh (MeshPy),
        #  because this is declared in PyTypeObject
        cpNameWithoutPy = cppName.removesuffix('Py')
        if any(cpNameWithoutPy == getClassName(pnOk := pn) for pn in pythonNames):
            return pnOk  # dirty hack for MeshPy

        msg = f"Cannot choose class from `{pythonNames}` using module: `{currentMod}`"
        ns = getCurrentNamespace()
        raise ValueError(msg)

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
