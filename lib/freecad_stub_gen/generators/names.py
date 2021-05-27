import logging
import xml.etree.ElementTree as ET
from typing import Optional

from freecad_stub_gen.module_map import moduleNamespace

logger = logging.getLogger(__name__)


def genBaseClasses(currentNode: ET.Element) -> tuple[str, ...]:
    return genFatherClass(currentNode),


def genFatherClass(currentNode: ET.Element) -> str:
    fatherNamespace: str = currentNode.attrib['FatherNamespace']
    fatherName: str = currentNode.attrib['Father']

    if len(moduleNamespace.stemToPaths[fatherName]) == 1:
        return genTypeForStem(fatherName, fatherNamespace)
    else:
        fatherTwin = fatherName.removesuffix('Py')
        fatherModule = moduleNamespace.convertNamespaceToModule(fatherNamespace)
        name = f'{fatherModule}.{fatherTwin}'
        return name


def genTypeForStem(stem: str, namespace: str = None):
    if namespace is None:
        namespace = moduleNamespace.getNamespaceForStem(stem)

    pathType = moduleNamespace.stemToPaths[stem][0]
    root = ET.parse(pathType).getroot()
    exportElement = root.find('PythonExport')
    assert exportElement
    twin = genClassName(exportElement)

    if '.' in twin:
        return twin
    else:
        module = moduleNamespace.convertNamespaceToModule(namespace)
        return f'{module}.{twin}'


def genClassName(currentNode: ET.Element) -> str:
    """Based on
    https://github.com/FreeCAD/FreeCAD/blob/8ac722c1e89ef530564293efd30987db09017e12/src/Tools/generateTemplates/templateClassPyExport.py#L279
    """
    if not (name := currentNode.attrib.get('PythonName')):
        name = currentNode.attrib['Twin']

    return name


def getSimpleClassName(currentNode: ET.Element) -> str:
    className = genClassName(currentNode)
    return className[className.rfind('.') + 1:]


def getShortModuleFormat(fullTypeName: str) -> tuple[str, str]:
    """ Return main module and class:
    >>> assert getShortModuleFormat('foo.bar.baz') == ('foo', 'foo.baz')
    This is workaround, because submodules are not supported yet."""
    module = fullTypeName[:fullTypeName.find('.')]
    className = fullTypeName[fullTypeName.rfind('.') + 1:]
    return module, f'{module}.{className}'


assert getShortModuleFormat('foo.bar.baz') == ('foo', 'foo.baz')


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
