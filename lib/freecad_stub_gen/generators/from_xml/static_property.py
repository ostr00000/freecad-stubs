import logging
from abc import ABC
from functools import cached_property
from xml.etree import ElementTree as ET

from freecad_stub_gen.cpp_code.converters import toBool
from freecad_stub_gen.generators.common.annotation_parameter import SelfSignature
from freecad_stub_gen.generators.common.doc_string import getDocFromNode
from freecad_stub_gen.generators.common.gen_property.gen_base import (
    BasePropertyGenerator,
)
from freecad_stub_gen.generators.common.names import (
    getModuleName,
    getPythonClassNameFromNode,
)
from freecad_stub_gen.generators.common.return_type_converter.full import (
    ReturnTypeConverter,
)
from freecad_stub_gen.generators.from_xml.base import BaseXmlGenerator
from freecad_stub_gen.generators.from_xml.method import XmlMethodGenerator

logger = logging.getLogger(__name__)


class XmlPropertyGenerator(
    XmlMethodGenerator, BaseXmlGenerator, BasePropertyGenerator, ABC
):
    def createAttribute(self, node: ET.Element) -> str:
        """Generate property based on xml file."""
        name = node.attrib['Name']
        docs = getDocFromNode(node)
        readOnly = toBool(node.attrib.get('ReadOnly', True))

        pythonTypeFromXml = self._findTypeBasedOnXmlDeclaration(node)
        specialType = self._getReturnTypeForSpecialCase(name, pythonTypeFromXml)

        rt = self._getReturnTypeConverter(f'get{name}')
        sig = SelfSignature(exceptions=rt.getExceptionsFromCode())
        docsGet = docs + SelfSignature.getExceptionsDocs((sig,))
        extractedGetType = rt.getStrReturnType()

        patchedGetType = self._patchType(specialType, extractedGetType)
        ret = self.createProperty(name, patchedGetType, docsGet, getter=True)

        if not readOnly:
            rt = self._getReturnTypeConverter(f'set{name}')
            sig = SelfSignature(exceptions=rt.getExceptionsFromCode())
            if d := SelfSignature.getExceptionsDocs((sig,)):
                docsSet = docs + d
            else:
                # do not repeat if there is no additional info
                docsSet = ''

            # let's assume that setter value type is same as getter,
            # this is not true, maybe it could be implemented later
            ret += self.createProperty(name, patchedGetType, docsSet, setter=True)

        return ret

    def _findTypeBasedOnXmlDeclaration(self, node: ET.Element) -> str:
        if (param := node.find('Parameter')) is None:
            raise ValueError

        xmlType = param.attrib['Type']
        pythonType = xmlTypeToPythonType[xmlType]
        if mn := getModuleName(pythonType):
            self.requiredImports.add(mn)
        return pythonType

    def _getReturnTypeConverter(self, cFuncName: str) -> ReturnTypeConverter:
        cClassName = self.currentNode.attrib['Name']
        funcBody = self.findFunctionBody(cFuncName, cClassName)
        if funcBody is None:
            raise TypeError

        return ReturnTypeConverter(
            funcBody, self.requiredImports, self.classNameWithModules, cFuncName
        )

    def _patchType(self, baseType: str, extractedType: str) -> str:
        match baseType, extractedType:
            case ('object', _):
                return extractedType

            case _ if baseType == extractedType:
                return extractedType

            case (_, 'object'):
                return baseType

            case ('dict' | 'list' | 'tuple' | 'typing.Sequence', _):
                if extractedType.startswith(baseType) or extractedType.endswith('Dict'):
                    return extractedType

                logger.warning(
                    f"Type from code does not match type from xml"
                    f" (cannot extend): {baseType=}, {extractedType=}"
                )

            case _:
                logger.warning(
                    f"Type from code does not match type from xml:"
                    f"{baseType=}, {extractedType=}, {self._cFunctionName=}"
                )

        return baseType

    def _getReturnTypeForSpecialCase(self, propertyName: str, pythonType: str):
        className = getPythonClassNameFromNode(self.currentNode)

        match className, propertyName:
            case 'DocumentObject', 'ViewObject':
                pythonType = 'FreeCADGui.ViewProviderDocumentObject | None'
            case 'DocumentObject', 'Parents':
                pythonType = 'list[tuple[FreeCAD.DocumentObject, str]]'
            case 'DocumentObject', 'Document':
                pythonType = 'FreeCAD.Document'
            case 'DocumentObject', (
                'InList' | 'InListRecursive' | 'OutList' | 'OutListRecursive'
            ):
                pythonType = 'list[FreeCAD.DocumentObject]'
            case 'DocumentObject', 'State':
                pythonType = (
                    'list[typing.Literal["Touched", "Invalid", "Recompute", '
                    '"Recompute2", "Restore", "Expanded", "Partial", '
                    '"Importing", "Up-to-date"]]'
                )

            case 'Document', 'Document':  # here is reversed
                pythonType = (
                    'FreeCAD.Document' if self._isGuiFile else 'FreeCADGui.Document'
                )

            case _, 'Document':
                pythonType = (
                    'FreeCADGui.Document' if self._isGuiFile else 'FreeCAD.Document'
                )

            case 'Document', 'ActiveView':
                # we want to add more specified type: FreeCADGui.View3DInventor,
                # because this is very common a real type
                pythonType = 'FreeCADGui.MDIViewPy | FreeCADGui.View3DInventorPy | None'

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
    'Vector': 'FreeCAD.Vector',
}
