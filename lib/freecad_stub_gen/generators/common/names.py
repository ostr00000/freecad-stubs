import logging
import xml.etree.ElementTree as ET
from typing import Optional

from freecad_stub_gen.importable_map import importableMap
from freecad_stub_gen.module_namespace import moduleNamespace

logger = logging.getLogger(__name__)


def getFatherClassWithModules(currentNode: ET.Element) -> str:
    fatherNamespace: str = currentNode.attrib['FatherNamespace']
    fatherName: str = currentNode.attrib['Father']

    if fatherName == 'PyObjectBase':
        return f'{moduleNamespace.convertNamespaceToModule(fatherNamespace)}.{fatherName}'

    return getClassWithModulesFromStem(fatherName, fatherNamespace)


def getClassWithModulesFromStem(stem: str, namespace: str):
    file = moduleNamespace.getFileForStem(stem, namespace)
    root = ET.parse(file).getroot()
    assert (exportElement := root.find('PythonExport'))
    return getClassWithModulesFromNode(exportElement)


def getClassWithModulesFromNode(currentNode: ET.Element) -> str:
    """
    Return class name preceded by all modules, ex. `FreeCAD.Vector`.
    Some classes are renamed in c++ code - try them first, then extract based on
    https://github.com/FreeCAD/FreeCAD/blob/8ac722c1e89ef530564293efd30987db09017e12/src/Tools/generateTemplates/templateClassPyExport.py#L279
    """
    if name := currentNode.attrib.get('PythonName'):
        assert '.' in name
        return name

    if fullName := importableMap.get(currentNode.attrib['Name']):
        if '.' in fullName:
            name = getClassName(fullName)

    if not name:
        name = currentNode.attrib.get('Name').removesuffix('Py')

    namespace = currentNode.attrib.get('Namespace')
    namespace = moduleNamespace.convertNamespaceToModule(namespace)
    return f'{namespace}.{name}'


def getClassNameFromNode(currentNode: ET.Element) -> str:
    return getClassName(getClassWithModulesFromNode(currentNode))


def getClassName(classWithModules: str):
    return classWithModules[classWithModules.rfind('.') + 1:]


def getModuleName(classWithModules: str):
    return classWithModules[:classWithModules.rfind('.')]


def getClassWithModulesFromPointer(cTypePointer: str):
    cType = cTypePointer.removesuffix('::Type')
    if '::' in cType:
        namespace, cType = cType.split('::')
    else:
        namespace = None

    return getClassWithModulesFromStem(cType, namespace)


def validatePythonValue(value: str) -> Optional[str]:
    try:
        eval(value, {}, {})
    except NameError:
        if value in ('true', 'false'):
            return value.title()
        logger.debug(f'Invalid value for default argument {value=}')
    except SyntaxError:
        return None
    except Exception as exc:
        logger.debug(f'Cannot evaluate value: {exc}')
    else:
        return value
