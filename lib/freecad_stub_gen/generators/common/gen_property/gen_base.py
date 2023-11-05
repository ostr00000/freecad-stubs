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
        readOnly=True,
    ):
        """This method return string with generated property for specified arguments."""
        pythonGetType = self._extractTypeAlias(pythonGetType)
        self.requiredImports.update(self._genImportsFromType(pythonGetType))
        retType = f' -> {pythonGetType}' if pythonGetType else ''
        docs = f'\n{indent(doc)}' if (doc := formatDocstring(docs)) else ' ...\n'
        prop = f'@property\ndef {name}(self){retType}:{docs}\n'

        if not readOnly:
            pythonSetType = self._extractTypeAlias(pythonSetType)
            self.requiredImports.update(self._genImportsFromType(pythonSetType))
            valueType = f': {pythonSetType}' if pythonSetType else ''
            prop += f'@{name}.setter\ndef {name}(self, value{valueType}): ...\n\n'

        return prop

    def _extractTypeAlias(self, pythonType: str):
        if pythonType == '':
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
            if '.' in subType:
                subType = subType.replace(' ', '')
                if '...' == subType:
                    continue

                mod = getModuleName(subType, required=True)
                yield mod
