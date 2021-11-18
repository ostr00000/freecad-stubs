import logging
from abc import ABC
from distutils.util import strtobool
from functools import cached_property
from xml.etree import ElementTree as ET

from freecad_stub_gen.generators.common.doc_string import getDocFromNode
from freecad_stub_gen.generators.common.gen_property.gen_base import BasePropertyGenerator
from freecad_stub_gen.generators.common.names import getClassNameFromNode
from freecad_stub_gen.generators.common.return_type_converter.full import ReturnTypeConverter
from freecad_stub_gen.generators.from_xml.base import BaseXmlGenerator
from freecad_stub_gen.generators.from_xml.method import XmlMethodGenerator

logger = logging.getLogger(__name__)


class XmlPropertyGenerator(XmlMethodGenerator, BaseXmlGenerator, BasePropertyGenerator, ABC):
    def getAttributes(self, node: ET.Element):
        """This function generate property based on xml file."""
        name = node.attrib['Name']
        docs = getDocFromNode(node)
        readOnly = strtobool(node.attrib.get('ReadOnly', 'True'))

        pythonType = self._findTypeBasedOnXmlDeclaration(node)
        pythonGetType = pythonSetType = self.__getReturnTypeForSpecialCase(name, pythonType)

        pythonGetType = self._getExtendedTypeFromCode(pythonGetType, f'get{name}')
        if not readOnly:
            pythonSetType = self._getExtendedTypeFromCode(pythonSetType, f'set{name}')
            if pythonSetType == 'object':
                pythonSetType = pythonGetType

        return self.getProperty(name, pythonGetType, pythonSetType, docs, readOnly)

    def _findTypeBasedOnXmlDeclaration(self, node: ET.Element):
        pythonType = None
        if (parm := node.find('Parameter')) is not None:
            xmlType = parm.attrib.get('Type')
            pythonType = xmlTypeToPythonType[xmlType]
            if 'typing' in pythonType:
                self.requiredImports.add('typing')
        return pythonType

    def _getExtendedTypeFromCode(self, pythonType: str, cFuncName: str) -> str:
        cClassName = self.currentNode.attrib['Name']
        funcBody = self.findFunctionBody(cFuncName, cClassName)
        assert funcBody is not None

        rt = ReturnTypeConverter(
            self.requiredImports, funcBody,
            self.classNameWithModules, cFuncName)
        extendedType = rt.getStrReturnType()

        match pythonType, extendedType:
            case ('object', _):
                return extendedType

            case _ if pythonType == extendedType:
                return extendedType

            case (_, 'object'):
                return pythonType

            case ('dict' | 'list' | 'tuple' | 'typing.Sequence', _):
                if extendedType.startswith(pythonType) or extendedType.endswith('Dict'):
                    return extendedType
                else:
                    logger.warning(f"Type from code does not match type from xml"
                                   f" (cannot extend): {pythonType=}, {extendedType=}")

            case _:
                logger.warning(f"Type from code does not match type from xml:"
                               f"{pythonType=}, {extendedType=}, {self._cFunctionName=}")

        return pythonType

    def __getReturnTypeForSpecialCase(self, propertyName: str, pythonType: str):
        className = getClassNameFromNode(self.currentNode)

        match className, propertyName:
            case 'DocumentObject', 'ViewObject':
                pythonType = 'FreeCADGui.ViewProviderDocumentObject | None'
            case 'DocumentObject', 'Parents':
                pythonType = 'list[tuple[FreeCAD.DocumentObject, str]]'
            case 'DocumentObject', 'Document':
                pythonType = 'FreeCAD.Document'
            case 'DocumentObject', ('InList' | 'InListRecursive' | 'OutList' | 'OutListRecursive'):
                pythonType = 'list[FreeCAD.DocumentObject]'
            case 'DocumentObject', 'State':
                pythonType = 'list[typing.Literal["Touched", "Invalid", "Recompute", ' \
                             '"Recompute2", "Restore", "Expanded", "Partial", ' \
                             '"Importing", "Up-to-date"]]'

            case 'Document', 'ActiveView':
                pythonType = 'FreeCADGui.View3DInventorPy'
            case 'Document', 'Document':  # here is reversed
                pythonType = 'FreeCAD.Document' if self._isGuiFile else 'FreeCADGui.Document'

            case 'ViewProviderDocumentObject', 'Document':
                pythonType = 'FreeCADGui.Document'
            case 'ViewProviderDocumentObject', 'Object':
                pythonType = 'FreeCAD.DocumentObject'

            case 'Placement', 'Base':
                pythonType = 'FreeCAD.Vector'

            case _, 'Document':
                pythonType = 'FreeCADGui.Document' if self._isGuiFile else 'FreeCAD.Document'

            case _, 'BoundBox':
                pythonType = 'FreeCAD.BoundBox'
            case _, 'Placement':
                pythonType = 'FreeCAD.Placement'
            case _, 'Matrix':
                pythonType = 'FreeCAD.Matrix'
            case _, 'Rotation':
                pythonType = 'FreeCAD.Rotation'
            case _, ('Axis' | 'RawAxis'):
                pythonType = 'FreeCAD.Vector'
            case _, 'Q':
                pythonType = 'tuple[float, float, float, float]'

        if 'typing' in pythonType:
            self.requiredImports.add('typing')
        return pythonType

    @cached_property
    def _isGuiFile(self) -> bool:
        return 'Gui' in str(self.baseGenFilePath)


xmlTypeToPythonType = {
    'Boolean': 'bool',
    'Dict': 'dict',
    'Float': 'float',
    'Int': 'int',
    'List': 'list',
    'Long': 'int',
    'Object': 'object',
    'Sequence': 'typing.Sequence',
    'String': 'str',
    'Tuple': 'tuple',
}
