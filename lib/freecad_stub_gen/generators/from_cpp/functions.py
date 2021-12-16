import logging
import re
from collections.abc import Iterable

from more_itertools import islice_extended

from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.from_cpp.base import Method, PyMethodDef, \
    BaseGeneratorFromCpp

logger = logging.getLogger(__name__)


class FreecadStubGeneratorFromCppFunctions(BaseGeneratorFromCpp):
    """Generate functions from cpp code defined in array."""

    def _genStub(self, moduleName: str) -> Iterable[str]:
        it = self._findArrayGen()
        methods = self._genAllMethods(it, functionSpacing=2)
        yield from methods

    REG_METHOD_DEF = re.compile(r'PyMethodDef(?!\s*\*)')

    def _findArrayGen(self) -> Iterable[Method]:
        """Based on https://docs.python.org/3/c-api/structures.html#c.PyMethodDef"""
        for match in self.REG_METHOD_DEF.finditer(self.impContent):
            arrayStr = findFunctionCall(self.impContent, match.start())
            arrayStrStartPos = arrayStr.find('{') + 1

            # skip the last one element - it is sentinel to skip processing
            for arrayElemText in islice_extended(generateExpressionUntilChar(
                    arrayStr, arrayStrStartPos, ',', bracketL='{', bracketR='}'), -1):
                arrayElemStartPos = arrayElemText.find('{') + 1
                method = PyMethodDef(list(
                    generateExpressionUntilChar(arrayElemText, arrayElemStartPos, ',')))
                yield from self._genMethodWithArgs(method, argNumStart=0)
