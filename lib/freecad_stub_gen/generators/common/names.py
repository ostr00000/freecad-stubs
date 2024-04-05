import logging
import typing
import xml.etree.ElementTree as ET

from freecad_stub_gen.generators.common.context import getCurrentNamespace
from freecad_stub_gen.generators.common.return_type_converter.str_wrapper import (
    StrWrapper,
)
from freecad_stub_gen.importable_map import importableMap
from freecad_stub_gen.module_namespace import moduleNamespace
from freecad_stub_gen.ordered_set import OrderedStrSet

logger = logging.getLogger(__name__)


def getFatherClassWithModules(currentNode: ET.Element) -> str:
    fatherNamespace: str = currentNode.attrib['FatherNamespace']
    fatherName: str = currentNode.attrib['Father']

    if fatherName == 'PyObjectBase':
        mod = moduleNamespace.convertNamespaceToModule(fatherNamespace)
        return f'{mod}.{fatherName}'

    return getClassWithModulesFromStem(fatherName, fatherNamespace)


def getClassWithModulesFromStem(stem: str, namespace: str) -> str:
    if stem.endswith('Py'):
        stems = [stem, stem.removesuffix('Py')]
    else:
        stems = [stem, stem + 'Py']

    # extract from xml
    for s in stems:
        try:
            file = moduleNamespace.getFileForStem(s, namespace)
        except ValueError:
            continue

        root = ET.parse(file).getroot()
        if (exportElement := root.find('PythonExport')) is None:
            raise ValueError

        return getClassWithModulesFromNode(exportElement)

    # something is wrong with `stem`
    if not stem[0].isupper():
        msg = "Cannot extract class name (first letter is not upper)."
        raise ValueError(msg)

    # extract from manual match
    for s in stems:
        if val := _getClassWithModulesFromMatch(s):
            return val

    # final fallback
    mod = moduleNamespace.convertNamespaceToModule(namespace)
    return f'{mod}.{stem}'


def _getClassWithModulesFromMatch(stem: str) -> str | None:
    ret = None
    match stem:
        case 'SplitView3DInventor' | 'View3DInventor':
            # we must use a base class
            ret = 'FreeCADGui.AbstractSplitViewPy'

        case 'ParameterGrpPy':
            ret = 'FreeCAD.ParameterGrp'

        case 'StringIDRef':
            ret = 'FreeCAD.StringID'

        case (
            'MDIViewPy'
            | 'View3DInventorPy'
            | 'View3DInventorViewerPy'
            | 'AbstractSplitViewPy'
        ):
            ret = f'FreeCADGui.{stem}'

        case 'MDIViewPyWrap':
            ret = 'FreeCADGui.MDIViewPy'

        case 'SelectionFilterPy':
            ret = 'FreeCADGui.SelectionFilter'

        case 'GeomCurve':
            ret = 'FreeCAD.Geom.Curve'

    return ret


CLASS_TO_ALIAS = {
    'Workbench': 'WorkbenchC',
}


def getClassWithModulesFromNode(currentNode: ET.Element) -> str:
    """Return class name preceded by all modules, ex. `FreeCAD.Vector`.

    Some classes are renamed in c++ code - try them first, then extract based on
    https://github.com/FreeCAD/FreeCAD/blob/8ac722c1e89ef530564293efd30987db09017e12/src/Tools/generateTemplates/templateClassPyExport.py#L279
    """
    if name := currentNode.attrib.get('PythonName'):
        if '.' not in name:
            raise ValueError

        if name.count('.') == 1:
            # we want to map only main module without submodules
            namespace, name = name.split('.', maxsplit=1)
            namespace = moduleNamespace.convertNamespaceToModule(namespace)
            return f'{namespace}.{name}'

        return name

    fullName = importableMap.get(currentNode.attrib['Name'])
    if fullName and '.' in fullName:
        name = getClassName(fullName)

    if not name:
        name = currentNode.attrib['Name'].removesuffix('Py')

    namespace = currentNode.attrib['Namespace']
    namespace = moduleNamespace.convertNamespaceToModule(namespace)
    name = CLASS_TO_ALIAS.get(name, name)
    return f'{namespace}.{name}'


def getPythonClassNameFromNode(currentNode: ET.Element) -> str:
    return getClassName(getClassWithModulesFromNode(currentNode))


def getClassName(classWithModules: str) -> str:
    return classWithModules[classWithModules.rfind('.') + 1 :]


@typing.overload
def getModuleName(classWithModules: str, *, required: typing.Literal[True]) -> str: ...


@typing.overload
def getModuleName(
    classWithModules: str, *, required: typing.Literal[False] = False
) -> str | None: ...


def getModuleName(classWithModules: str, *, required=False) -> str | None:
    if (splitIndex := classWithModules.rfind('.')) != -1:
        return classWithModules[:splitIndex]

    if not required:
        return None

    msg = f'Cannot find module for {classWithModules}'
    raise ValueError(msg)


def useAliasedModule(
    classWithModules: str, requiredImports: OrderedStrSet | None = None
) -> str:
    mod = getModuleName(classWithModules)
    if mod is None:
        return classWithModules

    cls = getClassName(classWithModules)
    mod = moduleNamespace.convertNamespaceToModule(mod)
    if requiredImports is not None:
        requiredImports.add(mod)
    return f'{mod}.{cls}'


def getNamespaceWithClass(cTypeClass: str) -> tuple[str, str]:
    match StrWrapper(cTypeClass):
        case StrWrapper(contain='::'):
            namespace, cType = cTypeClass.split('::')
        case StrWrapper(start='PyExc_'):
            namespace = '__python__'
            cType = cTypeClass
        case _:
            namespace = getCurrentNamespace()
            cType = cTypeClass

    return namespace, cType


def getClassWithModulesFromPointer(cTypePointer: str) -> str:
    cType = removeAffix(cTypePointer, suffixes=('::Type', '::type_object(', 'Py'))
    namespace, cType = getNamespaceWithClass(cType)
    return getClassWithModulesFromStem(cType, namespace)


def removeAffix(
    text: str,
    prefixes: typing.Iterable[str] | str = (),
    suffixes: typing.Iterable[str] | str = (),
) -> str:
    if isinstance(prefixes, str):
        prefixes = (prefixes,)
    if isinstance(suffixes, str):
        suffixes = (suffixes,)

    text = text.strip()
    for p in prefixes:
        text = text.removeprefix(p).strip()
    for s in suffixes:
        text = text.removesuffix(s).strip()
    return text
