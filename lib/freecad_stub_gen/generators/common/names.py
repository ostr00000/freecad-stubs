import logging
import typing
import xml.etree.ElementTree as ET

from freecad_stub_gen.importable_map import importableMap
from freecad_stub_gen.module_namespace import moduleNamespace
from freecad_stub_gen.ordered_set import OrderedStrSet

logger = logging.getLogger(__name__)


def getFatherClassWithModules(currentNode: ET.Element) -> str:
    fatherNamespace: str = currentNode.attrib['FatherNamespace']
    fatherName: str = currentNode.attrib['Father']

    if fatherName == 'PyObjectBase':
        return f'{moduleNamespace.convertNamespaceToModule(fatherNamespace)}.{fatherName}'

    return getClassWithModulesFromStem(fatherName, fatherNamespace)


def getClassWithModulesFromStem(stem: str, namespace: str) -> str:
    try:
        file = moduleNamespace.getFileForStem(stem, namespace)
    except ValueError:
        # if there is no xml, use this `match`
        match namespace, stem:

            # Gui + without Py
            case '', 'SelectionFilterPy':
                stem = stem.removesuffix('Py')
                namespace = 'Gui'

            # Gui + with Py
            case _, ('MDIViewPy' | 'View3DInventorPy'
                     | 'View3DInventorViewerPy' | 'AbstractSplitViewPy'):
                namespace = 'Gui'

            # we must use a base class
            case _, 'SplitView3DInventor' | 'View3DInventor':
                return 'FreeCADGui.AbstractSplitViewPy'

            case '', _:
                return stem.removesuffix('Py')

            case _, _:
                stem = stem.removesuffix('Py')

        mod = moduleNamespace.convertNamespaceToModule(namespace)
        return f'{mod}.{stem}'

    root = ET.parse(file).getroot()
    assert (exportElement := root.find('PythonExport'))
    return getClassWithModulesFromNode(exportElement)


CLASS_TO_ALIAS = {
    'Workbench': 'WorkbenchC',
}


def getClassWithModulesFromNode(currentNode: ET.Element) -> str:
    """
    Return class name preceded by all modules, ex. `FreeCAD.Vector`.
    Some classes are renamed in c++ code - try them first, then extract based on
    https://github.com/FreeCAD/FreeCAD/blob/8ac722c1e89ef530564293efd30987db09017e12/src/Tools/generateTemplates/templateClassPyExport.py#L279
    """
    if name := currentNode.attrib.get('PythonName'):
        assert '.' in name
        if name.count('.') == 1:
            # we want to map only main module without submodules
            namespace, name = name.split('.', maxsplit=1)
            namespace = moduleNamespace.convertNamespaceToModule(namespace)
            return f'{namespace}.{name}'

        return name

    if fullName := importableMap.get(currentNode.attrib['Name']):
        if '.' in fullName:
            name = getClassName(fullName)

    if not name:
        name = currentNode.attrib['Name'].removesuffix('Py')

    namespace = currentNode.attrib['Namespace']
    namespace = moduleNamespace.convertNamespaceToModule(namespace)
    name = CLASS_TO_ALIAS.get(name, name)
    return f'{namespace}.{name}'


def getClassNameFromNode(currentNode: ET.Element) -> str:
    return getClassName(getClassWithModulesFromNode(currentNode))


def getClassName(classWithModules: str) -> str:
    return classWithModules[classWithModules.rfind('.') + 1:]


@typing.overload
def getModuleName(classWithModules: str, required: typing.Literal[True]) -> str: ...


@typing.overload
def getModuleName(classWithModules: str, required=False) -> str | None: ...


def getModuleName(classWithModules: str, required=False) -> str | None:
    if (splitIndex := classWithModules.rfind('.')) != -1:
        return classWithModules[:splitIndex]

    if not required:
        return None

    raise ValueError(f"Cannot find module for {classWithModules}")


def useAliasedModule(classWithModules: str, requiredImports: OrderedStrSet | None = None) -> str:
    mod = getModuleName(classWithModules)
    if mod is None:
        return classWithModules

    cls = getClassName(classWithModules)
    mod = moduleNamespace.convertNamespaceToModule(mod)
    if requiredImports is not None:
        requiredImports.add(mod)
    return f'{mod}.{cls}'


def getNamespaceWithClass(cTypeClass: str):
    cType = cTypeClass
    if '::' in cType:
        namespace, cType = cType.split('::')
    else:
        namespace = None
    return namespace, cType


def getClassWithModulesFromPointer(cTypePointer: str) -> str:
    cType = cTypePointer.removesuffix('::Type').removesuffix('::type_object(')
    namespace, cType = getNamespaceWithClass(cType)
    return getClassWithModulesFromStem(cType, namespace or '')
