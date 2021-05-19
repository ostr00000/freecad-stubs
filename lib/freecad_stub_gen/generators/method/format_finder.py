import logging
import re
from re import Pattern

from freecad_stub_gen.generators.method.function_finder import FunctionFinder, findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.method.types_converter import TypesConverter

logger = logging.getLogger(__name__)


class FormatFinder(FunctionFinder):
    REG_TUP = re.compile(r'PyArg_ParseTuple(?!\w)\s*\(')
    REG_TUP_KW = re.compile(r'PyArg_ParseTupleAndKeywords\s*\(')

    def _generateArgFromCode(self, functionName, start=1):
        if not (funBody := self.findFunctionBody(functionName, self.parentXml)):
            return

        yield from self.__findParseTuple(funBody, start)
        yield from self.__findParseTupleAndKeywords(funBody, start)
        # TODO P5 PyArg_UnpackTuple
        # https://docs.python.org/3/c-api/arg.html#c.PyArg_UnpackTuple

    def __findParseTuple(self, functionBody: str, start: int):
        yield from self._baseParse(
            functionBody, pattern=self.REG_TUP,
            formatStrPosition=1, minSize=2, onlyPositional=True, start=start)

    def __findParseTupleAndKeywords(self, functionBody: str, start: int):
        yield from self._baseParse(
            functionBody, pattern=self.REG_TUP_KW,
            formatStrPosition=2, minSize=4, onlyPositional=False, start=start)

    def _baseParse(self, functionBody: str, pattern: Pattern,
                   formatStrPosition: int, minSize: int, onlyPositional: bool, start: int):
        for match in re.finditer(pattern, functionBody):
            funStart, _endOFFormat = match.span()
            funCall = findFunctionCall(functionBody, funStart, bracketL='(', bracketR=')')
            tc = TypesConverter(funCall, self.currentNode, self.requiredImports,
                                onlyPositional, formatStrPosition, start, self.xmlPath,
                                realStartArgNum=minSize)

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
