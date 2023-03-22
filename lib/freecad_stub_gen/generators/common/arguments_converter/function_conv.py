import logging
import re
from pathlib import Path

from freecad_stub_gen.generators.common.arguments_converter.definitions import DEFAULT_ARG_NAME
from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar

logger = logging.getLogger(__name__)


class FunctionConv:
    def __init__(self, xmlPath: Path, functionName: str, body: str,
                 funStart: int, formatStrPosition: int, onlyPositional: bool, argNumStart: int):
        self.xmlPath = xmlPath
        self.functionName = functionName

        self._body = body
        self._funStart = funStart

        self.formatStrPosition = formatStrPosition
        self.onlyPositional = onlyPositional
        self.argNumStart = argNumStart

        self.funCall = findFunctionCall(self._body, self._funStart, bracketL='(', bracketR=')')
        self.argumentStrings = self._getArgumentString()
        self._removeMacros()
        self.kwargList = self._getKwargList()

    REG_REMOVE_WHITESPACES = re.compile(r'\s+')

    def _getArgumentString(self) -> list[str]:
        sub = re.sub(self.REG_REMOVE_WHITESPACES, '', self.funCall)  # remove whitespace
        argStr = [c.removeprefix('&').strip()
                  for c in generateExpressionUntilChar(sub, sub.find('(') + 1, ',')]
        argStr = [a[1:-1] if a.startswith('(') and a.endswith(')') else a for a in argStr]
        return argStr

    # noinspection RegExpSuspiciousBackref
    REG_STRING = re.compile(r"""
    (["'])          # start with quotation mark as group 1,
    (?=             # do not consume matched characters - we match it after we are sure about it,
      (?P<text>     # save matched chars as `text`,
        .*?         # all chars but lazy,
        (?!\\\1)    # skip escaped char from group 1,
        \1          # matched text must ends with same char as group 1,
      )
    )
    (?P=text)       # then find again a content of group named 'text'
        """, re.VERBOSE)
    _FORBIDDEN_MACROS = ['PARAM_REF', 'PARAM_FARG', 'AREA_PARAMS_OPCODE']

    def _removeMacros(self):
        clearFormat = ''
        formatStr = self.argumentStrings[self.formatStrPosition]
        for strVal in re.finditer(self.REG_STRING, formatStr):
            clearFormat += strVal.group().removesuffix('"').removeprefix('"')
        self.argumentStrings[self.formatStrPosition] = clearFormat

        if 'PARAM_REF(' in self.funCall:
            varArg = slice(self.formatStrPosition + 1, None)
            self.argumentStrings[varArg] = [
                argS for argS in self.argumentStrings[varArg]
                if all(fm not in argS for fm in self._FORBIDDEN_MACROS)]

    def _getKwargList(self) -> list[str]:
        if self.onlyPositional:
            return []

        kwargsArgumentName = self.argumentStrings[self.formatStrPosition + 1]
        matches: list[str] = re.findall(
            rf'{kwargsArgumentName}\s*\[\s*]\s*=\s*{{((?:.|\s)*?)}}',
            self.varDeclarationCode)
        if not matches:
            return []

        # take the latest match and remove whitespaces
        kwargsStr = ''.join(matches[-1].split())
        return [
            kw[1:-1]
            for kw in generateExpressionUntilChar(kwargsStr, 0, ',')
            if kw.startswith('"') and kw.endswith('"')]

    @property
    def varDeclarationCode(self):
        return self._body[:self._funStart]

    @property
    def formatStr(self):
        return self.argumentStrings[self.formatStrPosition]

    def getPythonArgName(self, curFormat: str, cArgNum: int, pythonArgNum: int) -> str:
        if not self.onlyPositional:
            try:
                return self.kwargList[pythonArgNum]
            except IndexError:
                logger.error(f"Too few kw arguments for {curFormat=}, {self}")

        if cArgName := self.getCurArgName(curFormat, cArgNum):
            # Is this always a unique name?
            return cArgName

        return f'{DEFAULT_ARG_NAME}{self.argNumStart + pythonArgNum}'

    def getCurArgName(self, curFormat: str, cArgNum: int) -> str | None:
        if curFormat in ('O!', 'O&') or curFormat.startswith('e'):
            # variable offset - skip type_object/converter/encoding
            cArgNum += 1
        try:
            cArgName = self.argumentStrings[cArgNum]
        except IndexError:
            logger.error(f"Too few arguments for {self}")
        else:
            if cArgName.isalnum():
                return cArgName
        return None

    def __str__(self):
        return f'funCall={self.funCall}, xml={self.xmlPath}'
