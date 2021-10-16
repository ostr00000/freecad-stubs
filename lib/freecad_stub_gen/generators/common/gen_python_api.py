import logging
import re
from abc import ABC
from re import Pattern

from freecad_stub_gen.generators.common.gen_base import BaseGenerator
from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.common.types_converter import TypesConverter

logger = logging.getLogger(__name__)


class PythonApiGenerator(BaseGenerator, ABC):
    REG_TUP = re.compile(r'PyArg_ParseTuple(?!\w)\s*\(')
    REG_TUP_KW = re.compile(r'PyArg_ParseTupleAndKeywords\s*\(')

    def generateArgFromCode(self, functionName: str, className: str = '', *, argNumStart=1):
        """
        Generate arguments for `functionName` in `className`.
        There may be more than one possible signature.
        """
        if not (funBody := self.findFunctionBody(functionName, className)):
            return

        yield from self.__findParseTuple(funBody, argNumStart)
        yield from self.__findParseTupleAndKeywords(funBody, argNumStart)
        # TODO P5 PyArg_UnpackTuple
        # https://docs.python.org/3/c-api/arg.html#c.PyArg_UnpackTuple

    def findFunctionBody(self, funcName: str, className: str = '') -> str | None:
        if res := self._findFunction(funcName, className):
            return res

    def _findFunction(self, funcName: str, className: str = '') -> str | None:
        for searchRegex in (
                fr'{funcName}\s*\(\s*PyObject\s*\*.*?\)',
                fr'{className}::{funcName}\s*\([^)]*\)',
                fr'Py::Object {funcName}\s*\([^)]*\)',
        ):
            if match := re.search(searchRegex, self.impContent):
                return findFunctionCall(self.impContent, match.end())

    def __findParseTuple(self, functionBody: str, argNumStart: int):
        yield from self._baseParse(functionBody, pattern=self.REG_TUP, formatStrPosition=1,
                                   minSize=2, onlyPositional=True, argNumStart=argNumStart)

    def __findParseTupleAndKeywords(self, functionBody: str, argNumStart: int):
        yield from self._baseParse(functionBody, pattern=self.REG_TUP_KW, formatStrPosition=2,
                                   minSize=4, onlyPositional=False, argNumStart=argNumStart)

    def _baseParse(self, functionBody: str, pattern: Pattern,
                   formatStrPosition: int, minSize: int, onlyPositional: bool, argNumStart: int):
        for match in re.finditer(pattern, functionBody):
            funStart = match.start()
            funCall = findFunctionCall(functionBody, funStart, bracketL='(', bracketR=')')
            tc = TypesConverter(
                funCall, self.requiredImports, onlyPositional, formatStrPosition,
                argNumStart=argNumStart, realStartArgNum=minSize, xmlPath=self.baseGenFilePath)

            assert minSize <= len(tc.argumentStrings), "Invalid format - expected bigger size"

            kwargsList = []
            if not onlyPositional:
                kwargsArgumentName = tc.argumentStrings[formatStrPosition + 1]
                kwargsDeclaration = functionBody[:funStart]
                matches: list[str] = re.findall(
                    rf'{kwargsArgumentName}\s*\[\s*]\s*=\s*{{((?:.|\s)*?)}}', kwargsDeclaration)
                if matches:
                    # take the latest match and remove whitespaces
                    kwargsStr = ''.join(matches[-1].split())
                    kwargsList = [
                        kw[1:-1]
                        for kw in generateExpressionUntilChar(kwargsStr, 0, ',')
                        if kw.startswith('"') and kw.endswith('"')]

            args = list(tc.convertFormatToTypes(kwargsList))
            yield args

