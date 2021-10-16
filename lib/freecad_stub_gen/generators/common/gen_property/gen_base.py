from abc import ABC

from freecad_stub_gen.generators.common.doc_string import formatDocstring
from freecad_stub_gen.generators.common.gen_base import BaseGenerator
from freecad_stub_gen.util import indent


class BasePropertyGenerator(BaseGenerator, ABC):

    def getProperty(self, name: str, pythonGetType: str = '', pythonSetType: str = '',
                    docs: str = '', readOnly=True):
        """This method return string with generated property for specified arguments."""
        docs = f'\n{indent(doc)}' if (doc := formatDocstring(docs)) else ' ...\n'
        retType = f' -> {pythonGetType}' if pythonGetType else ''
        prop = f'@property\ndef {name}(self){retType}:{docs}\n'

        if not readOnly:
            valueType = f': {pythonSetType}' if pythonSetType else ''
            prop += f'@{name}.setter\ndef {name}(self, value{valueType}): ...\n\n'

        for importName in ('typing', 'os', 'FreeCAD', 'FreeCADGui'):
            if importName in (pythonSetType.split('.') + pythonGetType.split('.')):
                self.requiredImports.add(importName)

        return prop
