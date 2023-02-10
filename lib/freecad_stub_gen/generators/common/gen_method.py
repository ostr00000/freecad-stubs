import logging
from abc import ABC
from typing import Sequence, Protocol

from freecad_stub_gen.generators.common.doc_string import formatDocstring
from freecad_stub_gen.generators.common.gen_python_api import PythonApiGenerator
from freecad_stub_gen.util import indent

logger = logging.getLogger(__name__)


class StringType(Protocol):
    def __str__(self):
        pass


class MethodGenerator(PythonApiGenerator, ABC):
    def convertMethodToStr(self, methodName: str,
                           strSignatures: Sequence[StringType | str],
                           docs: str = '',
                           isClassic=False,
                           isStatic=False,
                           functionSpacing=1) -> str:
        ret = ''
        if not strSignatures:
            return ret
        signatures = list(map(str, strSignatures))

        static = '@staticmethod\n' if isStatic else ''
        classic = '@classmethod\n' if isClassic else ''

        # only single signature should not have overload
        if len(signatures) > 1:
            self.requiredImports.add('typing')
            overload = '@typing.overload\n'
        else:
            overload = ''

        forcedType = self._getForcedReturnType(methodName)
        spacing = '\n' * functionSpacing
        pattern = (
            f'{static}'
            f'{classic}'
            f'{overload}'
            f'def {methodName}{{signature}}:'
            f'{{docs}}'
            f'{spacing}'
        )

        for sig in signatures[:-1]:
            sig = self._formatSignatureWithReturnType(sig, forcedType)
            ret += pattern.format(signature=sig, docs=' ...\n')

        # last signature should have docstring
        docs = f'\n{indent(doc)}' if (doc := formatDocstring(docs)) else ' ...\n'
        sig = self._formatSignatureWithReturnType(signatures[-1], forcedType)
        ret += pattern.format(signature=sig, docs=docs)
        return ret

    def _getForcedReturnType(self, methodName: str) -> str | None:
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

    @classmethod
    def _formatSignatureWithReturnType(cls, sig: str, forcedType: str | None):
        if forcedType:
            if ' ->' in sig:
                sig = sig.rsplit(' ->', maxsplit=1)[0]
            return f'{sig} -> {forcedType}'
        return sig
