import logging
import xml.etree.ElementTree as ET
from typing import Optional

from freecad_stub_gen.module_map import moduleNamespace

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


def getClassWithModulesFromNode(currentNode: ET.Element) -> str:
    """
    Return class name preceded by all modules, ex. `FreeCAD.Vector`.
    Some classes are renamed in c++ code - try them first, then extract based on
    https://github.com/FreeCAD/FreeCAD/blob/8ac722c1e89ef530564293efd30987db09017e12/src/Tools/generateTemplates/templateClassPyExport.py#L279
    """
    if name := _renamedTypes.get(currentNode.attrib['Name']):
        assert '.' in name
        return name

    if name := currentNode.attrib.get('PythonName'):
        assert '.' in name
        return name

    namespace = currentNode.attrib.get('Namespace')
    namespace = moduleNamespace.convertNamespaceToModule(namespace)
    twin = currentNode.attrib.get('Twin')
    return f'{namespace}.{twin}'


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
