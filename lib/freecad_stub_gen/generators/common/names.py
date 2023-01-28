import ast
import builtins
import logging
import xml.etree.ElementTree as ET

from freecad_stub_gen.importable_map import importableMap
from freecad_stub_gen.module_namespace import moduleNamespace
from freecad_stub_gen.util import OrderedSet

logger = logging.getLogger(__name__)


def getFatherClassWithModules(currentNode: ET.Element) -> str:
    fatherNamespace: str = currentNode.attrib['FatherNamespace']
    fatherName: str = currentNode.attrib['Father']

    if fatherName == 'PyObjectBase':
        return f'{moduleNamespace.convertNamespaceToModule(fatherNamespace)}.{fatherName}'

    return getClassWithModulesFromStem(fatherName, fatherNamespace)


def getClassWithModulesFromStem(stem: str, namespace: str):
    try:
        file = moduleNamespace.getFileForStem(stem, namespace)
    except ValueError:
        name = stem.removesuffix('Py')
        if not namespace:
            return name

        namespace = moduleNamespace.convertNamespaceToModule(namespace)
        return f'{namespace}.{name}'

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
        else:
            return name

    if fullName := importableMap.get(currentNode.attrib['Name']):
        if '.' in fullName:
            name = getClassName(fullName)

    if not name:
        name = currentNode.attrib.get('Name').removesuffix('Py')

    namespace = currentNode.attrib.get('Namespace')
    namespace = moduleNamespace.convertNamespaceToModule(namespace)
    name = CLASS_TO_ALIAS.get(name, name)
    return f'{namespace}.{name}'


def getClassNameFromNode(currentNode: ET.Element) -> str:
    return getClassName(getClassWithModulesFromNode(currentNode))


def getClassName(classWithModules: str):
    return classWithModules[classWithModules.rfind('.') + 1:]


def getModuleName(classWithModules: str):
    if (splitIndex := classWithModules.rfind('.')) != -1:
        return classWithModules[:splitIndex]


def useAliasedModule(classWithModules: str, requiredImports: OrderedSet = None) -> str:
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


def getClassWithModulesFromPointer(cTypePointer: str):
    cType = cTypePointer.removesuffix('::Type')
    namespace, cType = getNamespaceWithClass(cType)
    return getClassWithModulesFromStem(cType, namespace or '')


def validatePythonValue(value: str) -> str | None:
    if value in builtins.__dict__:
        return value

    if value in ('true', 'false'):
        return value.title()

    try:
        ast.literal_eval(value)
    except (SyntaxError, ValueError):
        pass
    except Exception as exc:
        logger.error(f'Cannot evaluate value: {exc}')
    else:
        return value

    if value and value[-1].lower() in ('f', 'l'):
        # maybe float literal (ex. 3.14f)
        return validatePythonValue(value[:-1])

    return None

def convertToPythonValue(value: str):
    if (safe := validatePythonValue(value)) is None:
        return False, None

    if value in builtins.__dict__:
        conv = builtins.__dict__[value]
    else:
        conv = ast.literal_eval(safe)

    return True, conv
