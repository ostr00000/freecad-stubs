import inspect
import xml.etree.ElementTree as ET
from distutils.util import strtobool
from pathlib import Path
from typing import Optional

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.generators.method.method import MethodGenerator
from freecad_stub_gen.generators.names import getFatherClassWithModules, getModuleName, \
    getClassWithModulesFromNode, getClassName
from freecad_stub_gen.generators.property import PropertyGenerator
from freecad_stub_gen.importable_map import importableMap
from freecad_stub_gen.module_container import Module
from freecad_stub_gen.util import indent, formatDocstring, getDocFromNode


class FreecadStubGeneratorFromXML(PropertyGenerator, MethodGenerator):
    """Generate class defined in xml file.
    Argument types are extracted from code."""

    def __init__(self, filePath: Path, sourceDir: Path = SOURCE_DIR):
        super().__init__(filePath, sourceDir)
        self.currentNode: Optional[ET.Element] = None

    def getStub(self, mod: Module, moduleName, submodule=''):
        header = f'# {self.baseGenFilePath.name}\n'

        tree = ET.parse(self.baseGenFilePath)
        for child in tree.getroot():
            if child.tag == 'PythonExport':
                self.currentNode = child
                content, classNameWithModules = self._getClassContent()

                modName = getModuleName(classNameWithModules)
                if submodule:
                    modName = f'{modName}.{submodule}'

                curMod = mod[modName]
                curMod.update(Module(header + content + '\n', self.requiredImports))
                self.requiredImports.clear()

    def _getClassContent(self):
        baseClasses = ', '.join(self.genBaseClasses())
        classNameWithModules = getClassWithModulesFromNode(self.currentNode)
        className = getClassName(classNameWithModules)
        classStr = f"class {className}({baseClasses}):\n"

        doc = getDocFromNode(self.currentNode)
        if importableMap.isImportable(classNameWithModules):
            doc = "This class can be imported.\n" + (doc or '')
        if doc:
            classStr += indent(formatDocstring(doc))
            classStr += '\n'
        classStr += indent(self.genInit())

        if specialCaseCode := self.getCodeForSpecialCase(className):
            classStr += indent(specialCaseCode)

        for attributeNode in sorted(self.currentNode.findall('Attribute'), key=self._nodeSort):
            classStr += indent(self.getAttributes(attributeNode))
        for dynamicProperty in sorted(self.genDynamicProperties()):
            classStr += indent(dynamicProperty)

        for methodNode in sorted(self.currentNode.findall('Methode'), key=self._nodeSort):
            classStr += indent(self.genMethod(methodNode))

        if strtobool(self.currentNode.attrib.get('RichCompare', 'False')):
            classStr += indent(self.genRichCompare())
        if strtobool(self.currentNode.attrib.get('NumberProtocol', 'False')):
            classStr += indent(self.genNumberProtocol(className))

        return classStr, classNameWithModules

    @staticmethod
    def _nodeSort(node: ET.Element):
        return node.attrib['Name']

    def genBaseClasses(self):
        """Only one class is available in xml as a father."""
        fatherModuleAndClass = getFatherClassWithModules(self.currentNode)
        self.requiredImports.add(getModuleName(fatherModuleAndClass))
        yield fatherModuleAndClass

    def getCodeForSpecialCase(self, className: str) -> str:
        ret = ''
        if className == 'DocumentObject':
            ret += self.getProperty('Proxy', 'FreeCADTemplates.ProxyPython',
                                    'FreeCADTemplates.ProxyPython', readOnly=False)
            self.requiredImports.add('FreeCADTemplates')

        elif className == 'ViewProviderDocumentObject':
            ret += self.getProperty('Proxy', 'FreeCADTemplates.ViewProviderPython',
                                    'FreeCADTemplates.ViewProviderPython', readOnly=False)
            self.requiredImports.add('FreeCADTemplates')

        elif className == 'GroupExtension':
            ret += self.getProperty('Group', 'list[DocumentObject]',
                                    'list[DocumentObject]', readOnly=False)

        elif className == 'Workbench':
            ret += workbenchBody + '\n\n'

        return ret


workbenchBody = inspect.cleandoc("""
    MenuText = ""
    ToolTip = ""
    
    def Initialize(self):
        raise NotImplementedError
    
    def ContextMenu(self, recipient): ...
    
    def appendToolbar(self, name, cmds): ...
    
    def removeToolbar(self, name): ...
    
    def appendCommandbar(self, name, cmds): ...
    
    def removeCommandbar(self, name): ...
    
    def appendMenu(self, name, cmds): ...
    
    def removeMenu(self, name): ...
    
    def appendContextMenu(self, name, cmds): ...
    
    def removeContextMenu(self, name): ...
    
    def GetClassName(self): ...
""")
