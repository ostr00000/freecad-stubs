import xml.etree.ElementTree as ET
from pathlib import Path

from freecad_stub_gen.generators.method.method import MethodGenerator
from freecad_stub_gen.generators.property import PropertyGenerator


class FreecadStubGenerator(PropertyGenerator, MethodGenerator):
    def __init__(self, xmlPath: Path):
        super().__init__(xmlPath)
        self.currentNode = None

    def _prepareBaseClassesImport(self):
        for base in self._genBaseClasses():
            self.requiredImports.add(base)

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
        self._prepareBaseClassesImport()

        baseClasses = ', '.join(self._genBaseClasses())
        classStr = f"class {self._genClassName()}({baseClasses}):\n"
        if doc := self._genDoc(self.currentNode):
            classStr += self.indent(doc)
            classStr += '\n'
        classStr += self.indent(self.genInit())

        for methodNode in sorted(self.currentNode.findall('Methode'), key=self._nodeSort):
            classStr += self.indent(self.genMethod(methodNode))

        for attributeNode in sorted(self.currentNode.findall('Attribute'), key=self._nodeSort):
            classStr += self.indent(self.getAttributes(attributeNode))

        ret = f'{self.genImports()}\n{classStr}'.rstrip() + '\n'
        return ret

    @staticmethod
    def _nodeSort(node: ET.Element):
        return node.attrib['Name']

    def _genBaseClasses(self) -> tuple:
        bases = []
        if self._genClassName() == 'Workbench':
            self.requiredImports.add('FreeCADGui')
            bases.append('FreeCADGui.Workbench')

        bases.append(
            self._genName(self.currentNode.attrib['Father'],
                          self.currentNode.attrib['FatherNamespace']))

        return tuple(bases)

    def _genClassName(self):
        return self._genName(self.currentNode.attrib['Name'])
