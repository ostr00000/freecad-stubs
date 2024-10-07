import logging
import typing
import xml.etree.ElementTree as ET

from freecad_stub_gen.generators.common.context import getCurrentNamespace
from freecad_stub_gen.generators.common.return_type_converter.str_wrapper import (
    StrWrapper,
)
from freecad_stub_gen.ordered_set import OrderedStrSet

logger = logging.getLogger(__name__)


def getFatherClassWithModules(currentNode: ET.Element) -> str:
    fatherNamespace: str = currentNode.attrib['FatherNamespace']
    fatherName: str = currentNode.attrib['Father']

    if fatherName == 'PyObjectBase':
        mod = convertNamespaceToModule(fatherNamespace)
        return f'{mod}.{fatherName}'

    from freecad_stub_gen.module_namespace import moduleNamespace

    return moduleNamespace.getPythonNameFromCpp(fatherNamespace, fatherName)


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
            namespace = convertNamespaceToModule(namespace)
            return f'{namespace}.{name}'

        return name
    from freecad_stub_gen.importable_map import importableMap

    fullName = importableMap.get(currentNode.attrib['Name'])
    if fullName and '.' in fullName:
        name = getClassName(fullName)

    if not name:
        name = currentNode.attrib['Name'].removesuffix('Py')

    namespace = currentNode.attrib['Namespace']
    namespace = convertNamespaceToModule(namespace)
    name = CLASS_TO_ALIAS.get(name, name)
    return f'{namespace}.{name}'


def getPythonClassNameFromNode(currentNode: ET.Element) -> str:
    return getClassName(getClassWithModulesFromNode(currentNode))


def getClassName(classWithModules: str) -> str:
    return classWithModules[classWithModules.rfind('.') + 1 :]


@typing.overload
def getModuleName(classWithModules: str, *, required: typing.Literal[True]) -> str:
    ...


@typing.overload
def getModuleName(
    classWithModules: str, *, required: typing.Literal[False] = False
) -> str | None:
    ...


def getModuleName(classWithModules: str, *, required=False) -> str | None:
    if (splitIndex := classWithModules.rfind('.')) != -1:
        return classWithModules[:splitIndex]

    if not required:
        return None

    msg = f'Cannot find module for `{classWithModules}`'
    raise ValueError(msg)


def useAliasedModule(
    classWithModules: str, requiredImports: OrderedStrSet | None = None
) -> str:
    mod = getModuleName(classWithModules)
    if mod is None:
        return classWithModules

    cls = getClassName(classWithModules)
    mod = convertNamespaceToModule(mod)
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
    cType = removeAffix(cTypePointer, suffixes=('::Type', '::type_object('))
    namespace, cType = getNamespaceWithClass(cType)

    from freecad_stub_gen.module_namespace import moduleNamespace

    return moduleNamespace.getPythonNameFromCpp(namespace, cType)


_NAMESPACE_TO_MODULE = {
    'Base': 'FreeCAD',
    'App': 'FreeCAD',
    'Gui': 'FreeCADGui',
    'Data': 'FreeCAD',
    'Attacher': 'Part',
    'Materials': 'Material',
}

# Some modules have class with the same name therefore we must use alias.
_MODULE_TO_ALIAS = {
    'Mesh': 'MeshModule',
    'Path': 'PathModule',
    'Points': 'PointsModule',
    'Part': 'PartModule',
}


def getModFromAlias(alias: str, default: str = '') -> str:
    for k, v in _MODULE_TO_ALIAS.items():
        if v == alias:
            return k
    return default


def convertNamespaceToModule(namespace: str) -> str:
    mod = _NAMESPACE_TO_MODULE.get(namespace, namespace)
    return _MODULE_TO_ALIAS.get(mod, mod)


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


def mergeModuleNames(mod: str, namespaceWithClass: str) -> str:
    """Merge namespace and name into a single string."""
    if '.' not in namespaceWithClass:
        return f'{mod}.{namespaceWithClass}'

    parts = namespaceWithClass.split('.')
    if convertNamespaceToModule(parts[0]) != mod:
        msg = (
            f"Found module {mod}, "
            f"but it is not consistent with name {namespaceWithClass}"
        )
        raise ValueError(msg)

    return f"{mod}.{'.'.join(parts[1:])}"
