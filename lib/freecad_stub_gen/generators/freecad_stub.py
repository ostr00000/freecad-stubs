import xml.etree.ElementTree as ET
from distutils.util import strtobool
from pathlib import Path

from freecad_stub_gen.generators.method.method import MethodGenerator
from freecad_stub_gen.generators.names import genBaseClasses, genClassName, getSimpleClassName
from freecad_stub_gen.generators.property import PropertyGenerator


class FreecadStubGenerator(PropertyGenerator, MethodGenerator):
    def __init__(self, xmlPath: Path):
        super().__init__(xmlPath)
        self.currentNode = None

    def parseFile(self) -> str:
        return '\n'.join(self._parseFile())

    def generateToFile(self, targetFile: Path):
        targetFile.parent.mkdir(exist_ok=True, parents=True)
        content = self.parseFile()
        with open(targetFile, 'w') as file:
            file.write(content)

    def _parseFile(self) -> str:
        tree = ET.parse(self.xmlPath)
        root = tree.getroot()

        for child in root:
            if child.tag == 'PythonExport':
                self.currentNode = child
                yield self.genClass()

    def genClass(self):
        baseClasses = ', '.join(self.genBaseClasses())
        classStr = f"class {getSimpleClassName(self.currentNode)}({baseClasses}):\n"
        if doc := self._genDoc(self.currentNode):
            classStr += self.indent(doc)
            classStr += '\n'
        classStr += self.indent(self.genInit())

        for attributeNode in sorted(self.currentNode.findall('Attribute'), key=self._nodeSort):
            classStr += self.indent(self.getAttributes(attributeNode))

        for methodNode in sorted(self.currentNode.findall('Methode'), key=self._nodeSort):
            classStr += self.indent(self.genMethod(methodNode))

        if strtobool(self.currentNode.attrib.get('RichCompare', 'False')):
            classStr += self.indent(self.genRichCompare())
        if strtobool(self.currentNode.attrib.get('NumberProtocol', 'False')):
            classStr += self.indent(self.genNumberProtocol())

        ret = f'{self.genImports()}\n{classStr}'.rstrip() + '\n'
        return ret

    @staticmethod
    def _nodeSort(node: ET.Element):
        return node.attrib['Name']

    def genBaseClasses(self):
        for base in genBaseClasses(self.currentNode):
            self.requiredImports.add(base[:base.rfind('.')])
            yield base
