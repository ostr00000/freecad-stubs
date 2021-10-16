import re
from dataclasses import dataclass, field
from functools import cached_property

from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar
from freecad_stub_gen.generators.common.gen_property.property_type import PropertyType
from freecad_stub_gen.generators.common.doc_string import prepareDocs


@dataclass
class PropertyMacroBase:
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

    REG_PATTERN_PROP_DECLARATION = r'([\w:]+)\s*{}\s*;'

    @cached_property
    def TypeId(self) -> str | None:
        # TODO P3 find declaration in parent
        reg = self.REG_PATTERN_PROP_DECLARATION.format(self.name)
        for classDecBody in self.classDeclarationBodies:
            if match := re.search(reg, classDecBody):
                return match.group(1)
