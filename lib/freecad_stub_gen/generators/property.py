import xml.etree.ElementTree as ET
from distutils.util import strtobool

from freecad_stub_gen.generators.base import BaseGenerator
from freecad_stub_gen.generators.names import getSimpleClassName


class PropertyGenerator(BaseGenerator):
    def getAttributes(self, node: ET.Element):
        name = node.attrib["Name"]
        pythonType = self.__findType(node)
        docs = self._getDocFromNode(node)
        readOnly = strtobool(node.attrib.get('ReadOnly', 'True'))

        pythonType = self.__getReturnTypeForSpecialCase(name, pythonType)
        return self.getProperty(name, pythonType, docs, readOnly)

    def getProperty(self, name: str, pythonType: str = '', docs: str = '', readOnly=True):
        if docs:
            docs = '\n' + self.indent(self._genDocFromStr(docs))
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

    def __getReturnTypeForSpecialCase(self, propertyName: str, pythonType: str):
        className = getSimpleClassName(self.currentNode)
        if className == 'DocumentObject' and propertyName == 'ViewObject':
            pythonType = 'typing.Optional[FreeCADGui.ViewProviderDocumentObject]'
            self.requiredImports.add('typing')

        elif className == 'DocumentObject' and pythonType == 'list':
            if propertyName == 'Parents':
                pythonType = 'list[tuple[FreeCAD.DocumentObject, str]]'
            else:
                pythonType = 'list[FreeCAD.DocumentObject]'

        elif className == 'ViewProviderDocumentObject':
            if propertyName == 'Document':
                pythonType = 'FreeCADGui.Document'
            elif propertyName == 'Object':
                pythonType = 'FreeCAD.DocumentObject'

        elif className == 'Placement':
            if propertyName == 'Base':
                pythonType = 'FreeCAD.Vector'

        if propertyName == 'Placement':
            pythonType = 'FreeCAD.Placement'
        elif propertyName == 'Matrix':
            pythonType = 'FreeCAD.Matrix'
        elif propertyName == 'Rotation':
            pythonType = 'FreeCAD.Rotation'

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
