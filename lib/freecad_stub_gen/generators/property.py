import enum
import logging
import re
import xml.etree.ElementTree as ET
from abc import ABC
from dataclasses import dataclass, field
from distutils.util import strtobool
from functools import cached_property
from itertools import chain
from pathlib import Path
from typing import Iterable, Literal, Optional

from freecad_stub_gen.util import indent, prepareDocs, formatDocstring, getDocFromNode, readContent
from freecad_stub_gen.generators.base import BaseGenerator
from freecad_stub_gen.generators.method.function_finder import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.names import getClassNameFromNode

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
    name: str
    default: str
    group: str = ''
    _rawType: str = ''
    _docs: str = ''
    type: PropertyType = PropertyType.Prop_None

    constructorBody: str = field(default='', repr=False)
    cppContent: str = field(default='', repr=False)
    classDeclarationBodies: list[str] = field(default_factory=list, repr=False)

    def __post_init__(self):
        self._docs = self._convertRawText(self._docs, isSentence=True)
        self.group = self._convertRawText(self.group)
        self._convertPropertyTypes()

    REG_PATTERN_GROUP_CHAR = r'char\s*\*\s*{}\s*=\s*\"([^"]+)"'

    def _convertRawText(self, rawText: str, isSentence=False):
        match rawText:
            case 'nullptr' | '0' | '':
                newVal = ''
            case str(val) if val.startswith('"') and val.endswith('"'):
                newVal = prepareDocs(val.removeprefix('"').removesuffix('"'))
                if isSentence and not newVal.endswith('.'):
                    newVal = newVal + '.'
            case val if 'group' in val:
                reg = self.REG_PATTERN_GROUP_CHAR.format(val)
                if match := re.search(reg, self.constructorBody):
                    newVal = match.group(1)
                else:
                    raise ValueError(f"Cannot find value for variable: {val}")
            case unexpectedVal:
                raise ValueError(unexpectedVal)
        return newVal

    def _convertPropertyTypes(self):
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
        result = '\n'

        for p in PropertyType:
            if p & self.type:
                result += f'[{p.name}] {p.description}.\n'

        if self.group:
            result += f'Property group: {self.group}.\n'

        if self.TypeId:
            result += f'Property TypeId: {self.TypeId}.\n'

        if self._docs:
            result += self._docs + '\n'

        return result

    @property
    def readOnly(self):
        return bool(self.type & PropertyType.Prop_ReadOnly)

    @property
    def pythonSetType(self) -> str:
        if not (typeId := self.TypeId):
            return ''

        constraint = '{t} | tuple[{t}, {t}, {t}, {t}]'
        match typeId, typeId.lower():
            case _, listProp if 'list' in listProp:
                container = 'dict[int, {t}] | typing.Iterable[{t}] | typing.Sequence[{t}]'
            case _, listProp if 'set' in listProp:
                container = 'typing.Sequence[{t}] | {t}'
            case (_, constraintProp) if 'constraint' in constraintProp:
                container = constraint
            case ("App::PropertyPercent", _):
                container = constraint
            case _:
                container = '{t}'

        match typeId, typeId.lower():
            case 'App::PropertyEnumeration', _:
                return self._getEnumType()

            case (("App::PropertyQuantity" | "App::PropertyDistance" | "App::PropertyFrequency"
                   | "App::PropertySpeed" | "App::PropertyAcceleration"), _):
                innerType = 'str | float | FreeCAD.Quantity | FreeCAD.Unit'

            case (("App::PropertyQuantityConstraint" | "App::PropertyLength" | "App::PropertyArea"
                   | "App::PropertyVolume" | "App::PropertyAngle" | "App::PropertyPressure"
                   | "App::PropertyForce" | "App::PropertyVacuumPermittivity"), _):
                innerType = 'str | float | FreeCAD.Quantity'

            case "App::PropertyPercent", _:
                innerType = 'int'

            case ("App::PropertyFloatConstraint" | "App::PropertyPrecision"), _:
                innerType = 'float | tuple[float, float, float, float]'

            case "App::PropertyMap", _:
                return 'dict[str, str]'

            case "App::PropertyStringList", _:
                innerType = 'str | bytes'

            case ("App::PropertyPersistentObject" | "App::PropertyUUID" | "App::PropertyFont"
                  | "App::PropertyFile"), _:
                return 'str'

            case (("App::PropertyLink" | "App::PropertyLinkChild" | "App::PropertyLinkGlobal" |
                   "App::PropertyLinkHidden" | "App::PropertyLinkList" |
                   "App::PropertyPlacementLink"), _):
                innerType = 'FreeCAD.DocumentObject | None'

            case (("App::PropertyLinkSub" | "App::PropertyLinkSubChild"
                   | "App::PropertyLinkSubGlobal" | "App::PropertyLinkSubHidden"
                   | "App::PropertyLinkListChild" | "App::PropertyLinkListGlobal"
                   | "App::PropertyLinkListHidden" | "App::PropertyLinkSubList"
                   | "App::PropertyLinkSubListChild" | "App::PropertyLinkSubListGlobal"
                   | "App::PropertyLinkSubListHidden" | "App::PropertyXLink"
                   | "App::PropertyXLinkSub" | "App::PropertyXLinkSubList"
                   | "App::PropertyXLinkList" | "App::PropertyXLinkContainer"), _):
                partResult = '{t} | tuple[{t}, {s}] | list[{t} | {s}] | None'
                innerType = partResult.format(
                    t='FreeCAD.DocumentObject', s='str | typing.Sequence[str]')

            case "App::PropertyMatrix", _:
                partResult = 'FreeCAD.Matrix | tuple[{t}]'
                innerType = partResult.format(t=', '.join('float' for _ in range(16)))

            case ("App::PropertyVector" | "App::PropertyVectorDistance" | "App::PropertyPosition"
                  | "App::PropertyDirection" | "App::PropertyVectorList"), _:
                partResult = 'FreeCAD.Vector | tuple[{t}, {t}, {t}]'
                innerType = partResult.format(t='float | int')

            case "App::PropertyPlacement":
                innerType = 'FreeCAD.Matrix | FreeCAD.Placement'

            case ("App::PropertyColor" | "App::PropertyColorList"), _:
                partResult = 'tuple[{t}, {t}, {t}] | tuple[{t}, {t}, {t}, {t}] | int'
                innerType = partResult.format(t='float')

            case ("App::PropertyMaterial" | "App::PropertyMaterialList"), _:
                innerType = 'FreeCAD.Material'

            case "App::PropertyPath":
                innerType = 'Path.Path'  # TODO fix Path (ToolPath)

            case "App::PropertyFileIncluded":
                partResult = '{t} | tuple[{t} {t}]'
                innerType = partResult.format(t='str | bytes | io.IOBase')

            case "App::PropertyPythonObject":
                innerType = 'object'

            case _, low if 'bool' in low:
                innerType = 'int | bool'
            case _, low if 'float' in low:
                innerType = 'float | int'
            case _, low if 'int' in low:
                innerType = 'int'
            case _, low if 'string' in low:
                innerType = 'str'
            case _:
                return ''

        return container.format(t=innerType)

    REG_PATTERN_PROP_DECL = r'([\w:]+)\s*{}\s*;'

    @cached_property
    def TypeId(self) -> Optional[str]:
        # TODO P3 find declaration in parent
        reg = self.REG_PATTERN_PROP_DECL.format(self.name)
        for classDecBody in self.classDeclarationBodies:
            if match := re.search(reg, classDecBody):
                return match.group(1)

    REG_PATTERN_ENUM_VAR_NAME = r'{}\.setEnums\(\s*(\w+)\s*\)'
    REG_PATTERN_ENUM_ARRAY = r'{}\s*\[\s*]\s*=\s*([^;]+)'

    def _getEnumType(self) -> str:
        reg = self.REG_PATTERN_ENUM_VAR_NAME.format(self.name)
        if varNameMatch := re.search(reg, self.constructorBody):
            reg = self.REG_PATTERN_ENUM_ARRAY.format(varNameMatch.group(1))

            if match := re.search(reg, self.constructorBody):
                literalsRaw = match.group(1)
            elif match := re.search(reg, self.cppContent):
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
        docs = getDocFromNode(node)
        readOnly = strtobool(node.attrib.get('ReadOnly', 'True'))

        pythonType = self.__getReturnTypeForSpecialCase(name, pythonType)
        return self.getProperty(name, pythonType, pythonType, docs, readOnly)

    def __findType(self, node: ET.Element):
        pythonType = None
        if (parm := node.find('Parameter')) is not None:
            xmlType = parm.attrib.get('Type')
            pythonType = xmlTypeToPythonType[xmlType]
            if 'typing' in pythonType:
                self.requiredImports.add('typing')
        return pythonType

    def __getReturnTypeForSpecialCase(self, propertyName: str, pythonType: str):
        className = getClassNameFromNode(self.currentNode)

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

    @property
    def isGuiFile(self) -> bool:
        return 'Gui' in str(self.baseGenFilePath)

    def getProperty(self, name: str, pythonGetType: str = '', pythonSetType: str = '',
                    docs: str = '', readOnly=True):
        if docs and (formattedDocs := formatDocstring(docs)):
            docs = '\n' + indent(formattedDocs)
        else:
            docs = ' ...\n'

        retType = f' -> {pythonGetType}' if pythonGetType else ''
        prop = f'@property\ndef {name}(self){retType}:{docs}\n'

        if not readOnly:
            valueType = f': {pythonSetType}' if pythonSetType else ''
            prop += f'@{name}.setter\ndef {name}(self, value{valueType}): ...\n\n'

        for importName in ('typing', 'os', 'FreeCAD', 'FreeCADGui'):
            if importName in (pythonSetType.split('.') + pythonGetType.split('.')):
                self.requiredImports.add(importName)

        return prop

    REG_DYNAMIC_PROPERTY = re.compile(r'\bADD_PROPERTY\(')
    REG_DYNAMIC_PROPERTY_TYPE = re.compile(r'\bADD_PROPERTY_TYPE\(')
    REG_DYNAMIC_PROPERTY_EXP = re.compile(r'\bEXTENSION_ADD_PROPERTY\(')
    REG_DYNAMIC_PROPERTY_EXP_TYPE = re.compile(r'\bEXTENSION_ADD_PROPERTY_TYPE\(')

    REG_PATTERN_CLASS_DEC = r'class .* {}[^{{]*'

    def genDynamicProperties(self) -> Iterable[str]:
        twinName = self.currentNode.attrib.get('Twin')
        assert twinName is not None, f"'Twin' not found in {self.baseGenFilePath}"

        if not (cppIncludeContent := self.getIncludeContent('.cpp')):
            return

        # there may be few separated declarations (ex. DocumentObject)
        hIncludeContent = self.getIncludeContent('.h')
        reg = re.compile(self.REG_PATTERN_CLASS_DEC.format(twinName))
        classDeclarationBodies = [
            findFunctionCall(hIncludeContent, classMatch.start())
            for classMatch in re.finditer(reg, hIncludeContent)]

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

                pm = PropertyMacro(
                    *macroArgs, constructorBody=constructorBody,
                    cppContent=cppIncludeContent, classDeclarationBodies=classDeclarationBodies)
                # print(pm)
                yield self.getProperty(
                    pm.name, pythonSetType=pm.pythonSetType, pythonGetType=pm.pythonSetType,
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
                    return readContent(p.with_suffix(ext))
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
