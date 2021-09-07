import enum
import logging
import re
import xml.etree.ElementTree as ET
from abc import ABC
from dataclasses import dataclass, field
from distutils.util import strtobool
from itertools import chain
from pathlib import Path
from typing import Iterable, ClassVar, Literal

from freecad_stub_gen.generators.base import BaseGenerator, commentRemover
from freecad_stub_gen.generators.method.function_finder import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.names import getSimpleClassName

logger = logging.getLogger(__name__)


class PropertyType(enum.Flag):
    def __new__(cls, value, description):
        member = object.__new__(cls)
        member._value_ = value
        member.description = description
        return member

    Prop_None = 0, "No special property type"
    Prop_ReadOnly = 1, "Property is read-only in the editor"
    Prop_Transient = 2, "Property content won't be saved to file, " \
                        "but still saves name, type and status"
    Prop_Hidden = 4, "Property won't appear in the editor"
    Prop_Output = 8, "Modified property doesn't touch its parent container"
    Prop_NoRecompute = 16, "Modified property doesn't touch its container for recompute"
    Prop_NoPersist = 32, "Property won't be saved to file at all"


@dataclass
class PropertyMacro:
    defaultSet: ClassVar = set()
    name: str
    default: str
    group: str = ''
    _rawType: str = ''
    _docs: str = ''
    type: PropertyType = PropertyType.Prop_None

    body: str = field(default='', repr=False)
    content: str = field(default='', repr=False)
    _pythonType: str = 'Enum'

    def __post_init__(self):
        self._docs = self._convertRawText(self._docs, isSentence=True)
        self.group = self._convertRawText(self.group)
        self._convertTypes()

    REG_PATTERN_GROUP_CHAR = r'char\s*\*\s*{}\s*=\s*\"([^"]+)"'

    def _convertRawText(self, rawText: str, isSentence=False):
        match rawText:
            case 'nullptr' | '0' | '':
                newVal = ''
            case val if isinstance(val, str) and val.startswith('"') and val.endswith('"'):
                newVal = BaseGenerator.prepareDocs(val.removeprefix('"').removesuffix('"'))
                if isSentence and not newVal.endswith('.'):
                    newVal = newVal + '.'
            case val if 'group' in val:
                reg = self.REG_PATTERN_GROUP_CHAR.format(val)
                if match := re.search(reg, self.body):
                    newVal = match.group(1)
                else:
                    raise ValueError(f"Cannot find value for variable: {val}")
            case unexpectedVal:
                raise ValueError(unexpectedVal)
        return newVal

    def _convertTypes(self):
        newTypes = self._rawType \
            .replace('\n', '') \
            .replace(' ', '') \
            .replace('App::', '') \
            .replace('(', '') \
            .replace(')', '') \
            .removeprefix('PropertyType')

        for t in newTypes.split('|'):
            if t:
                self.type |= PropertyType[t]

    @property
    def docs(self):
        result = ''
        count = 0

        for p in PropertyType:
            if p & self.type:
                count += 1
                result += f'[{p.name}] {p.description}.\n'

        if self.group:
            count += 1
            result += f'Property group: {self.group}.\n'

        if self._docs:
            count += 1
            result += self._docs

        if count > 1:
            result = '\n' + result + '\n'

        return result

    @property
    def readOnly(self):
        return bool(self.type & PropertyType.Prop_ReadOnly)

    REG_PATTERN_ENUM_VAR_NAME = r'{}\.setEnums\(\s*(\w+)\s*\)'
    REG_PATTERN_ENUM_ARRAY = r'{}\s*\[\s*]\s*=\s*([^;]+)'

    @property
    def pythonType(self):
        if self._pythonType != 'Enum':
            return self._pythonType

        reg = self.REG_PATTERN_ENUM_VAR_NAME.format(self.name)
        if varNameMatch := re.search(reg, self.body):
            reg = self.REG_PATTERN_ENUM_ARRAY.format(varNameMatch.group(1))

            if match := re.search(reg, self.body):
                literalsRaw = match.group(1)
            elif match := re.search(reg, self.content):
                literalsRaw = match.group(1)
            else:
                raise ValueError("Cannot find enum variable")

            literalsStart = literalsRaw.find('{') + 1
            literalsArray = [exp.removeprefix('"').removesuffix('"')
                             for exp in generateExpressionUntilChar(
                    literalsRaw, literalsStart, ",", bracketL='{', bracketR='}')]
            literalsArray = literalsArray[:-1]  # remove NULL

            return f'typing.Literal{literalsArray}'
        return ''


class PropertyGenerator(BaseGenerator, ABC):
    def getAttributes(self, node: ET.Element):
        name = node.attrib["Name"]
        pythonType = self.__findType(node)
        docs = self._getDocFromNode(node)
        readOnly = strtobool(node.attrib.get('ReadOnly', 'True'))

        pythonType = self.__getReturnTypeForSpecialCase(name, pythonType)
        return self.getProperty(name, pythonType, docs, readOnly)

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

    @property
    def isGuiFile(self) -> bool:
        return 'Gui' in str(self.baseGenFilePath)

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

        if 'typing' in pythonType:
            self.requiredImports.add('typing')

        return prop

    REG_DYNAMIC_PROPERTY = re.compile(r'\bADD_PROPERTY\(')
    REG_DYNAMIC_PROPERTY_TYPE = re.compile(r'\bADD_PROPERTY_TYPE\(')
    REG_DYNAMIC_PROPERTY_EXP = re.compile(r'\bEXTENSION_ADD_PROPERTY\(')
    REG_DYNAMIC_PROPERTY_EXP_TYPE = re.compile(r'\bEXTENSION_ADD_PROPERTY_TYPE\(')

    def genDynamicProperties(self) -> Iterable[str]:
        twinName = self.currentNode.attrib.get('Twin')
        assert twinName is not None, f"'Twin' not found in {self.baseGenFilePath}"

        if not (cppIncludeContent := self.getIncludeContent('.cpp')):
            return

        for match in re.finditer(f'{twinName}::{twinName}', cppIncludeContent):
            constructorBody = findFunctionCall(cppIncludeContent, match.start())
            for propMatch in chain(
                    re.finditer(self.REG_DYNAMIC_PROPERTY, constructorBody),
                    re.finditer(self.REG_DYNAMIC_PROPERTY_TYPE, constructorBody),
                    re.finditer(self.REG_DYNAMIC_PROPERTY_EXP, constructorBody),
                    re.finditer(self.REG_DYNAMIC_PROPERTY_EXP_TYPE, constructorBody)
            ):
                macroBody = findFunctionCall(
                    constructorBody, propMatch.start(), bracketL='(', bracketR=')')
                macroCallStartPos = macroBody.find('(') + 1
                macroArgs = [exp.strip() for exp in generateExpressionUntilChar(
                    macroBody, expStart=macroCallStartPos, splitChar=',')]
                pm = PropertyMacro(*macroArgs, body=constructorBody, content=cppIncludeContent)
                print(pm)
                # TODO P2 support enums values as literals
                # TODO P2 support return types = get from .h file
                yield self.getProperty(
                    pm.name, pythonType=pm.pythonType,
                    docs=pm.docs, readOnly=pm.readOnly)

            # We assume that they may be more than one constructor,
            # but each constructor add the same properties.
            break

    def getIncludeContent(self, extension: Literal['.cpp', '.h']):
        inc = self.currentNode.get('Include')
        assert inc is not None, f"'Include' not found in {self.baseGenFilePath}"

        parts = self.baseGenFilePath.parts
        baseParts = parts[:parts.index('src') + 1] + (inc,)
        pathFromSrc = Path(*baseParts)
        pathFromLocal = self.baseGenFilePath.parent / inc

        for p in (pathFromSrc, pathFromLocal):
            for ext in (extension, Path(inc).suffix):
                try:
                    content = p.with_suffix(ext).read_text()
                    return commentRemover(content)
                except FileNotFoundError:
                    pass

        if inc.endswith('.hxx'):
            return  # probably these files are generated - just ignore them

        logger.warning(f"Could not find cpp file for {self.baseGenFilePath}")


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
