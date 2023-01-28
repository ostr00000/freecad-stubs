import re
from dataclasses import dataclass, field
from functools import cached_property

from freecad_stub_gen.generators.common.doc_string import prepareDocs
from freecad_stub_gen.generators.common.gen_property.property_type import PropertyType


@dataclass
class PropertyMacroBase:
    name: str
    default: str
    group: str = ''
    _rawType: str = ''
    _docs: str = ''
    type: PropertyType = PropertyType.Prop_None

    constructorBody: str = field(default='', repr=False)
    namespace: str = ''
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
                newVal = val.removeprefix('"').removesuffix('"')
                if isSentence and newVal and not newVal.endswith('.'):
                    newVal = newVal + '.'
                newVal = prepareDocs(newVal)

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
            .removeprefix('PropertyType') \
            .removeprefix('::')

        for t in newTypes.split('|'):
            if t:
                self.type |= PropertyType[t]

    REG_PATTERN_PROP_DECLARATION = r'([\w: \t]+)\b{}\b\s*;'

    @cached_property
    def TypeId(self) -> str | None:
        reg = self.REG_PATTERN_PROP_DECLARATION.format(self.name)
        for classDecBody in self.classDeclarationBodies:
            if match := re.search(reg, classDecBody):
                typeId = match.group(1).replace(' ', '').replace('\t', '')
                if '::' not in typeId:
                    typeId = f'{self.namespace}::{typeId}'

                return typeId
