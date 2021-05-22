import xml.etree.ElementTree as ET
from distutils.util import strtobool

from freecad_stub_gen.generators.base import BaseGenerator


class PropertyGenerator(BaseGenerator):
    def getAttributes(self, node: ET.Element):
        name = node.attrib["Name"]
        pythonType = self.__findType(node)

        if docs := self._getDocFromNode(node):
            docs = '\n' + self.indent(self._genDocFromStr(docs))
        else:
            docs = ' ...\n'

        retType = f' -> {pythonType}' if pythonType else ''
        prop = f'@property\ndef {name}(self){retType}:{docs}\n'

        if not strtobool(node.attrib.get('ReadOnly', 'True')):
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
