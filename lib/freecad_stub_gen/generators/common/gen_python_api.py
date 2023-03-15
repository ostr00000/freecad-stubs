import logging
import re
from abc import ABC
from itertools import chain
from pathlib import Path

import more_itertools

from freecad_stub_gen.generators.common.annotation_parameter import SelfSignature
from freecad_stub_gen.generators.common.arguments_converter import TypesConverter
from freecad_stub_gen.generators.common.cpp_function import findFunctionCall
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
        fnBody = self.findFunctionBody(cFunctionName, cClassName)
        if not isinstance(fnBody, str):
            return

        self._cFunctionName = cFunctionName
        self._functionBody = fnBody
        self._argNumStart = argNumStart

        returnSig = self._getReturnSignature()
        signatures = chain(
            self._findParseTuple(),
            self._findParseTupleAndKeywords(),
            # TODO P5 PyArg_UnpackTuple
            # https://docs.python.org/3/c-api/arg.html#c.PyArg_UnpackTuple
        )
        hasAnySig, sigIter = more_itertools.spy(signatures)
        for sig in sigIter:
            yield returnSig.replace(parameters=sig.parameters, unknown_parameters=False)

        if not hasAnySig:
            yield returnSig

    def findFunctionBody(self, cFuncName: str, cClassName: str) -> str | None:
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

        return None

    def _findParseTuple(self):
        yield from self._baseParse(pattern=self.REG_TUP, formatStrPosition=1,
                                   minSize=2, onlyPositional=True)

    def _findParseTupleAndKeywords(self):
        yield from self._baseParse(pattern=self.REG_TUP_KW, formatStrPosition=2,
                                   minSize=4, onlyPositional=False)

    def _getReturnSignature(self):
        rtc = ReturnTypeConverter(
            self._functionBody, self.requiredImports,
            self.classNameWithModules, self._cFunctionName)
        rt = rtc.getReturnType()
        ex = rtc.getExceptionsFromCode()
        return SelfSignature(unknown_parameters=True, return_annotation=rt, exceptions=ex)

    def _baseParse(self, pattern: re.Pattern, formatStrPosition: int,
                   minSize: int, onlyPositional: bool):
        for match in re.finditer(pattern, self._functionBody):
            funStart = match.start()
            tc = TypesConverter(
                self._functionBody, funStart, self.requiredImports,
                onlyPositional, formatStrPosition, self._argNumStart,
                realStartArgNum=minSize, xmlPath=self.baseGenFilePath,
                functionName=self._cFunctionName)

            assert minSize <= len(tc.argumentStrings), "Invalid format - expected bigger size"

            params = list(tc.convertFormatToTypes())
            yield SelfSignature(params)
