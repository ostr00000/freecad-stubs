import logging
import xml.etree.ElementTree as ET
from typing import Optional

from freecad_stub_gen.module_map import moduleNamespace

logger = logging.getLogger(__name__)


def getBaseClasses(currentNode: ET.Element) -> tuple[str, ...]:
    return getFatherClass(currentNode),


def getFatherClass(currentNode: ET.Element) -> str:
    fatherNamespace: str = currentNode.attrib['FatherNamespace']
    fatherName: str = currentNode.attrib['Father']

    if len(moduleNamespace.stemToPaths[fatherName]) == 1:
        return getTypeForStem(fatherName, fatherNamespace)
    else:
        fatherTwin = fatherName.removesuffix('Py')
        fatherModule = moduleNamespace.convertNamespaceToModule(fatherNamespace)
        name = f'{fatherModule}.{fatherTwin}'
        return name


def getTypeForStem(stem: str, namespace: str = None):
    if namespace is None:
        namespace = moduleNamespace.getNamespaceForStem(stem)

    pathType = moduleNamespace.stemToPaths[stem][0]
    root = ET.parse(pathType).getroot()
    exportElement = root.find('PythonExport')
    assert exportElement
    twin = getClassName(exportElement)

    if '.' in twin:
        return twin
    else:
        module = moduleNamespace.convertNamespaceToModule(namespace)
        return f'{module}.{twin}'


_renamedTypes = {
    # these types are renamed in code
    # https://github.com/FreeCAD/FreeCAD/blob/8ac722c1e89ef530564293efd30987db09017e12/src/Mod/Part/App/AppPart.cpp#L226
    # regex to find non matching names:
    # Base::Interpreter\(\).addType\(\&\w+::(\w+)Py\s*::Type,\s*\w+,"(?!\1")

    'TypePy': 'FreeCAD.TypeId',
    'MeshFeaturePy': 'Mesh.Feature',
    'TopoShapePy': 'Part.Shape',
    'TopoShapeVertexPy': 'Part.Vertex',
    'TopoShapeWirePy': 'Part.Wire',
    'TopoShapeEdgePy': 'Part.Edge',
    'TopoShapeSolidPy': 'Part.Solid',
    'TopoShapeFacePy': 'Part.Face',
    'TopoShapeCompoundPy': 'Part.Compound',
    'TopoShapeCompSolidPy': 'Part.CompSolid',
    'TopoShapeShellPy': 'Part.Shell',
    'PartFeaturePy': 'Part.Feature',
    'BRepOffsetAPI_MakePipeShellPy': 'Part.MakePipeShell',
    'BRepOffsetAPI_MakeFillingPy': 'Part.MakeFilling',
}


def getClassName(currentNode: ET.Element) -> str:
    """Based on
    https://github.com/FreeCAD/FreeCAD/blob/8ac722c1e89ef530564293efd30987db09017e12/src/Tools/generateTemplates/templateClassPyExport.py#L279
    """
    if name := currentNode.attrib.get('PythonName'):
        return name

    if name := _renamedTypes.get(currentNode.attrib['Name']):
        return name

    return currentNode.attrib['Twin']


def getSimpleClassName(currentNode: ET.Element) -> str:
    className = getClassName(currentNode)
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
