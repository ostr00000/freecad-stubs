import xml.etree.ElementTree as ET
from abc import ABC
from distutils.util import strtobool

from freecad_stub_gen.generators.base import BaseGenerator
from freecad_stub_gen.generators.names import getSimpleClassName


class PropertyGenerator(BaseGenerator, ABC):
    def getAttributes(self, node: ET.Element):
        name = node.attrib["Name"]
        pythonType = self.__findType(node)
        docs = self._getDocFromNode(node)
        readOnly = strtobool(node.attrib.get('ReadOnly', 'True'))

        pythonType = self.__getReturnTypeForSpecialCase(name, pythonType)
        return self.getProperty(name, pythonType, docs, readOnly)

    def getProperty(self, name: str, pythonType: str = '', docs: str = '', readOnly=True):
        if docs:
            docs = '\n' + self.indent(self._getDocFromStr(docs))
        else:
            docs = ' ...\n'

        retType = f' -> {pythonType}' if pythonType else ''
        prop = f'@property\ndef {name}(self){retType}:{docs}\n'

        if not readOnly:
            valueType = f': {pythonType}' if pythonType else ''
            prop += f'@{name}.setter\ndef {name}(self, value{valueType}): ...\n\n'
        return prop

    def __findType(self, node: ET.Element):
        pythonType = None
        if (parm := node.find('Parameter')) is not None:
            xmlType = parm.attrib.get('Type')
            pythonType = xmlTypeToPythonType[xmlType]
            if 'typing' in pythonType:
                self.requiredImports.add('typing')
        return pythonType

    @property
    def isGuiFile(self) -> bool:
        return 'Gui' in str(self.baseGenFilePath)

    def __getReturnTypeForSpecialCase(self, propertyName: str, pythonType: str):
        className = getSimpleClassName(self.currentNode)

        match className, propertyName:
            case 'DocumentObject', 'ViewObject':
                pythonType = 'typing.Optional[FreeCADGui.ViewProviderDocumentObject]'
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

            case 'Document', 'ActiveObject':
                pythonType = 'typing.Optional[FreeCAD.DocumentObject]'
            case 'Document', 'ActiveView':
                pythonType = 'FreeCADGui.View3DInventorPy'
            case 'Document', 'Document':  # here is reversed
                pythonType = 'FreeCAD.Document' if self.isGuiFile else 'FreeCADGui.Document'

            case 'ViewProviderDocumentObject', 'Document':
                pythonType = 'FreeCADGui.Document'
            case 'ViewProviderDocumentObject', 'Object':
                pythonType = 'FreeCAD.DocumentObject'

            case 'Placement', 'Base':
                pythonType = 'FreeCAD.Vector'

            case _, 'Document':
                pythonType = 'FreeCADGui.Document' if self.isGuiFile else 'FreeCAD.Document'

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


xmlTypeToPythonType = {
    "Boolean": 'bool',
    "Dict": 'dict',
    "Float": 'float',
    "Int": 'int',
    "List": 'list',
    "Long": 'int',
    "Object": 'object',
    "Sequence": 'typing.Sequence',
    "String": 'str',
    "Tuple": 'tuple',
}
