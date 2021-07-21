import logging
import re
from abc import ABC
from pathlib import Path
from re import Pattern
from typing import Optional

from freecad_stub_gen.generators.method.function_finder import FunctionFinder, findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.method.types_converter import TypesConverter

logger = logging.getLogger(__name__)


class FormatFinder(FunctionFinder, ABC):
    REG_TUP = re.compile(r'PyArg_ParseTuple(?!\w)\s*\(')
    REG_TUP_KW = re.compile(r'PyArg_ParseTupleAndKeywords\s*\(')

    def generateArgFromCode(self, functionName: str, className: str = '', *, argNumStart=1):
        if not (funBody := self.findFunctionBody(functionName, className, self.parentXml)):
            return

        yield from self.__findParseTuple(funBody, argNumStart)
        yield from self.__findParseTupleAndKeywords(funBody, argNumStart)
        # TODO P5 PyArg_UnpackTuple
        # https://docs.python.org/3/c-api/arg.html#c.PyArg_UnpackTuple

    @property
    def parentXml(self) -> Optional[Path]:
        if self.currentNode is None:
            return

        fatherInclude = self.currentNode.attrib['FatherInclude'].replace('/', '.')
        parentFile = (self.sourceDir / fatherInclude).with_suffix('.xml')
        return parentFile

    def __findParseTuple(self, functionBody: str, argNumStart: int):
        yield from self._baseParse(functionBody, pattern=self.REG_TUP, formatStrPosition=1,
                                   minSize=2, onlyPositional=True, argNumStart=argNumStart)

    def __findParseTupleAndKeywords(self, functionBody: str, argNumStart: int):
        yield from self._baseParse(functionBody, pattern=self.REG_TUP_KW, formatStrPosition=2,
                                   minSize=4, onlyPositional=False, argNumStart=argNumStart)

    def _baseParse(self, functionBody: str, pattern: Pattern,
                   formatStrPosition: int, minSize: int, onlyPositional: bool, argNumStart: int):
        for match in re.finditer(pattern, functionBody):
            funStart, _endOFFormat = match.span()
            funCall = findFunctionCall(functionBody, funStart, bracketL='(', bracketR=')')
            tc = TypesConverter(funCall, self.currentNode, self.requiredImports,
                                onlyPositional, formatStrPosition, argNumStart,
                                self.baseGenFilePath, realStartArgNum=minSize)

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

    def convertMethodToStr(self, methodName: str, args: list, docsText: str = None,
                           isClassic=False, isStatic=False, functionSpacing=1) -> str:
        """Element of args must implement __str__ method."""
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
        doc = f'\n{self.indent(self._genDocFromStr(docsText))}' if docsText else ' ...\n'
        ret += pattern.format(args=args[-1], docs=doc)
        return ret

    def _getReturnType(self, methodName: str) -> Optional[str]:
        ret = None
        if methodName == 'activeDocument':
            if 'App' in self.baseGenFilePath.parts:
                ret = 'FreeCAD.Document'
            elif 'Gui' in self.baseGenFilePath.parts:
                ret = 'FreeCADGui.Document'
            else:
                logger.warning(f'Unexpected function type in file {self.baseGenFilePath}')
        return ret
