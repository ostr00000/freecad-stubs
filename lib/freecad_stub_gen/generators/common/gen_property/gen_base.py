import re
from abc import ABC

from freecad_stub_gen.generators.common.doc_string import formatDocstring
from freecad_stub_gen.generators.common.gen_base import BaseGenerator
from freecad_stub_gen.generators.common.names import getModuleName
from freecad_stub_gen.python_code import indent


class BasePropertyGenerator(BaseGenerator, ABC):
    def getProperty(
        self,
        name: str,
        pythonGetType: str = '',
        pythonSetType: str = '',
        docs: str = '',
        *,
        readOnly=True,
    ):
        """Generate property for specified arguments."""

    def createProperty(
        self, name: str, propValType: str, docs: str = '', *, getter=False, setter=False
    ) -> str:
        propValType = self._extractTypeAlias(propValType)
        self.requiredImports.update(self._genImportsFromType(propValType))
        docs = f'\n{indent(d)}' if (d := formatDocstring(docs)) else ' ...\n'
        ret = ''

        if getter:
            retType = f' -> {propValType}' if propValType else ''
            ret += f'@property\ndef {name}(self){retType}:{docs}\n'

        if setter:
            valueType = f': {propValType}' if propValType else ''
            ret += f'@{name}.setter\ndef {name}(self, value{valueType}):{docs}\n'

        return ret

    def _extractTypeAlias(self, pythonType: str):
        if not pythonType:
            return pythonType

        for typePart in pythonType.split('\n'):
            line = typePart.strip()
            if any(t in line for t in ('typing.TypeAlias', 'typing.TypeVar')):
                self.requiredImports.update(self._genImportsFromType(line))
                self.requiredImports.add(line)
            elif line:
                return line
        raise ValueError

    REG_TYPE_SPLIT_CHARS = re.compile(r'[\[\]|,:=]')

    @classmethod
    def _genImportsFromType(cls, pythonType: str):
        if '.' not in pythonType:
            return
        for subType in cls.REG_TYPE_SPLIT_CHARS.split(pythonType):
            if '.' not in subType:
                continue

            strippedSubType = subType.strip()
            if strippedSubType == '...':
                continue

            yield getModuleName(strippedSubType, required=True)
