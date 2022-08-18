import logging
import re
from abc import ABC
from itertools import chain
from pathlib import Path

import more_itertools

from freecad_stub_gen.generators.common.annotation_parameter import SelfSignature
from freecad_stub_gen.generators.common.arguments_converter import TypesConverter
from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.common.gen_base import BaseGenerator
from freecad_stub_gen.generators.common.return_type_converter.full import ReturnTypeConverter

logger = logging.getLogger(__name__)


class PythonApiGenerator(BaseGenerator, ABC):
    REG_TUP = re.compile(r'PyArg_ParseTuple(?!\w)\s*\(')
    REG_TUP_KW = re.compile(r'PyArg_ParseTupleAndKeywords\s*\(')

    def __init__(self, filePath: Path, sourceDir: Path):
        super().__init__(filePath, sourceDir)
        self.classNameWithModules = ''

        self._cFunctionName = ''
        self._functionBody = ''
        self._argNumStart = -1

    def generateSignaturesFromCode(self, cFunctionName: str, cClassName: str, *, argNumStart=1):
        """
        Generate arguments for `cFunctionName` in `cClassName`.
        There may be more than one possible signature.
        """
        self._functionBody = self.findFunctionBody(cFunctionName, cClassName)
        if not self._functionBody:
            return

        self._cFunctionName = cFunctionName
        self._argNumStart = argNumStart

        returnSig = self._getReturnSignature()
        signatures = chain(
            self.__findParseTuple(),
            self.__findParseTupleAndKeywords(),
            # TODO P5 PyArg_UnpackTuple
            # https://docs.python.org/3/c-api/arg.html#c.PyArg_UnpackTuple
        )
        hasAnySig, sigIter = more_itertools.spy(signatures)
        for sig in sigIter:
            yield returnSig.replace(parameters=sig.parameters, unknown_parameters=False)

        if not hasAnySig:
            yield returnSig

    def findFunctionBody(self, cFuncName: str, cClassName: str) -> str | None:
        if res := self._findFunction(cFuncName, cClassName):
            return res

    def _findFunction(self, cFuncName: str, cClassName: str = '') -> str | None:
        if cFuncName == 'PyMake':
            regs = [re.compile(fr'{cFuncName}\s*\(\s*struct\s*_typeobject\s*\*')]
        else:
            regs = [
                re.compile(fr'{cFuncName}\s*\(\s*PyObject\s*\*.*?\)'),
                re.compile(fr'{cClassName}::{cFuncName}\s*\([^)]*\)'),
                re.compile(fr'Py::Object {cFuncName}\s*\([^)]*\)'),
            ]
        for searchRegex in regs:
            if match := re.search(searchRegex, self.impContent):
                return findFunctionCall(self.impContent, match.end())

    def __findParseTuple(self):
        yield from self._baseParse(pattern=self.REG_TUP, formatStrPosition=1,
                                   minSize=2, onlyPositional=True)

    def __findParseTupleAndKeywords(self):
        yield from self._baseParse(pattern=self.REG_TUP_KW, formatStrPosition=2,
                                   minSize=4, onlyPositional=False)

    def _getReturnSignature(self):
        rtc = ReturnTypeConverter(
            self.requiredImports, self._functionBody,
            self.classNameWithModules, self._cFunctionName)
        rt = rtc.getReturnType()
        ex = rtc.getExceptionsFromCode()
        return SelfSignature(unknown_parameters=True, return_annotation=rt, exceptions=ex)

    def _baseParse(self, pattern: re.Pattern, formatStrPosition: int,
                   minSize: int, onlyPositional: bool):
        for match in re.finditer(pattern, self._functionBody):
            funStart = match.start()
            funCall = findFunctionCall(self._functionBody, funStart, bracketL='(', bracketR=')')
            tc = TypesConverter(
                funCall, self.requiredImports, onlyPositional, formatStrPosition,
                argNumStart=self._argNumStart, realStartArgNum=minSize,
                xmlPath=self.baseGenFilePath)

            assert minSize <= len(tc.argumentStrings), "Invalid format - expected bigger size"

            kwargsList = []
            if not onlyPositional:
                kwargsArgumentName = tc.argumentStrings[formatStrPosition + 1]
                kwargsDeclaration = self._functionBody[:funStart]
                matches: list[str] = re.findall(
                    rf'{kwargsArgumentName}\s*\[\s*]\s*=\s*{{((?:.|\s)*?)}}', kwargsDeclaration)
                if matches:
                    # take the latest match and remove whitespaces
                    kwargsStr = ''.join(matches[-1].split())
                    kwargsList = [
                        kw[1:-1]
                        for kw in generateExpressionUntilChar(kwargsStr, 0, ',')
                        if kw.startswith('"') and kw.endswith('"')]

            params = list(tc.convertFormatToTypes(kwargsList))
            rtc = ReturnTypeConverter(
                self.requiredImports, self._functionBody,
                self.classNameWithModules, self._cFunctionName)
            rt = rtc.getReturnType()
            ex = rtc.getExceptionsFromCode()
            yield SelfSignature(params, return_annotation=rt, exceptions=ex)
