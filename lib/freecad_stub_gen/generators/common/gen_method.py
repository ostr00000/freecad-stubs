import logging
from abc import ABC
from typing import Protocol, Sequence

from freecad_stub_gen.generators.common.doc_string import formatDocstring
from freecad_stub_gen.generators.common.gen_python_api import PythonApiGenerator
from freecad_stub_gen.python_code import indent

logger = logging.getLogger(__name__)


class PythonSignatureProtocol(Protocol):
    def getPythonSignature(self) -> str:
        ...


class MethodGenerator(PythonApiGenerator, ABC):
    _NEW_LINE = '\n'  # future change (3.12) PEP 701 - inline

    def convertMethodToStr(
        self,
        methodName: str,
        strSignatures: Sequence[PythonSignatureProtocol | str],
        docs: str = '',
        isClassic=False,
        isStatic=False,
        functionSpacing=1,
    ) -> str:
        ret = ''
        if not strSignatures:
            return ret
        signatures = [
            ss if isinstance(ss, str) else ss.getPythonSignature()
            for ss in strSignatures
        ]

        # only single signature should not have overload
        if len(signatures) > 1:
            self.requiredImports.add('typing')
            overload = '@typing.overload\n'
        else:
            overload = ''

        forcedType = self._getForcedReturnType(methodName)
        pattern = (
            f'{"@staticmethod" + self._NEW_LINE if isStatic else ""}'
            f'{"@classmethod" + self._NEW_LINE if isClassic else ""}'
            f'{overload}'
            f'def {methodName}{{signature}}:'
            f'{{docs}}'
            f'{self._NEW_LINE * functionSpacing}'
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
                msg = f'Unexpected function type in file {self.baseGenFilePath}'
                logger.warning(msg)
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
