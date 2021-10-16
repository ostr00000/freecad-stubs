import logging
from abc import ABC
from typing import Protocol

from freecad_stub_gen.generators.common.doc_string import formatDocstring
from freecad_stub_gen.generators.common.gen_python_api import PythonApiGenerator
from freecad_stub_gen.util import indent

logger = logging.getLogger(__name__)


class StringType(Protocol):
    def __str__(self):
        pass


class MethodGenerator(PythonApiGenerator, ABC):
    def convertMethodToStr(self, methodName: str, args: list[StringType], docs: str = '',
                           isClassic=False, isStatic=False, functionSpacing=1) -> str:
        ret = ''
        if not args:
            return ret

        static = '@staticmethod\n' if isStatic else ''
        classic = '@classmethod\n' if isClassic else ''

        # only single signature should not have overload
        if len(args) > 1:
            self.requiredImports.add('typing')
            overload = '@typing.overload\n'
        else:
            overload = ''

        spacing = '\n' * functionSpacing
        returnType = f' -> {rt}' if (rt := self._getReturnType(methodName)) else ''
        pattern = (
            f'{static}'
            f'{classic}'
            f'{overload}'
            f'def {methodName}({{args}}){returnType}:'
            f'{{docs}}'
            f'{spacing}'
        )

        for arg in args[:-1]:
            ret += pattern.format(args=arg, docs=' ...\n')

        # last signature should have docstring
        docs = f'\n{indent(doc)}' if (doc := formatDocstring(docs)) else ' ...\n'
        ret += pattern.format(args=args[-1], docs=docs)
        return ret

    def _getReturnType(self, methodName: str) -> str | None:
        ret = None
        if methodName == 'activeDocument':
            if 'App' in self.baseGenFilePath.parts:
                ret = 'FreeCAD.Document'
            elif 'Gui' in self.baseGenFilePath.parts:
                ret = 'FreeCADGui.Document'
            else:
                logger.warning(f'Unexpected function type in file {self.baseGenFilePath}')
        elif methodName == 'getParentGroup':
            ret = 'FreeCAD.DocumentObjectGroup | None'
        return ret
