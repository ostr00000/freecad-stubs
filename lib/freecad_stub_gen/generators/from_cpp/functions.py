import logging
import re
from typing import Iterable

from more_itertools import islice_extended

from freecad_stub_gen.generators.from_cpp.base import Method, PyMethodDef, \
    FreecadStubGeneratorFromCpp
from freecad_stub_gen.generators.method.function_finder import findFunctionCall, \
    generateExpressionUntilChar

logger = logging.getLogger(__name__)


# TODO P2 find functions added directly to module
#  ex.    Module() : Py::ExtensionModule<Module>("DraftUtils")

class FreecadStubGeneratorFromCppFunctions(FreecadStubGeneratorFromCpp):

    def _genStub(self):
        it = self._findArrayGen()
        methods = self._genAllMethods(it, isStatic=False, functionSpacing=2)
        yield from methods

    REG_METHOD_DEF = re.compile(r'PyMethodDef(?!\s*\*)')

    def _findArrayGen(self) -> Iterable[Method]:
        """Based on https://docs.python.org/3/c-api/structures.html#c.PyMethodDef"""
        for match in self.REG_METHOD_DEF.finditer(self.impContent):
            start, end = match.span()
            arrayStr = findFunctionCall(self.impContent, start)
            arrayStrStartPos = arrayStr.find('{') + 1

            for arrayElemText in islice_extended(generateExpressionUntilChar(
                    arrayStr, arrayStrStartPos, ',', bracketL='{', bracketR='}'), -1):
                arrayElemStartPos = arrayElemText.find('{') + 1
                method = PyMethodDef(list(
                    generateExpressionUntilChar(arrayElemText, arrayElemStartPos, ',')))
                yield from self._genMethodWithArgs(method)
