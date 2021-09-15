import logging
import re
from abc import ABC
from itertools import islice
from pathlib import Path
from typing import Optional

from freecad_stub_gen.generators.base import BaseGenerator

logger = logging.getLogger(__name__)


class FunctionFinder(BaseGenerator, ABC):
    def findFunctionBody(self, funcName: str, className: str = '') -> Optional[str]:
        if res := self._findFunction(funcName, className):
            return res

        redirectedName = funcName[0].lower() + funcName[1:]
        if res := self._findFunction(redirectedName, className):
            return res

        if self.parentXmlPath is None:
            return

        if not (baseClass := type(self).safeCreate(self.parentXmlPath)):
            if funcName == 'PyInit':
                pass  # skip implicit constructor - probably inherited from PyObject
            else:
                logger.error(f"Cannot find {self.parentXmlPath=} for {self.baseGenFilePath=}")
            return

        return baseClass.findFunctionBody(funcName, className)

    @property
    def parentXmlPath(self) -> Optional[Path]:
        return None

    def _findFunction(self, funcName: str, className: str = '') -> Optional[str]:
        for searchRegex in (
                fr'{funcName}\s*\(\s*PyObject\s*\*.*?\)',
                fr'{className}::{funcName}\s*\([^)]*\)',
                fr'Py::Object {funcName}\s*\([^)]*\)',
        ):
            if match := re.search(searchRegex, self.impContent):
                return findFunctionCall(self.impContent, match.end())


def findFunctionCall(text: str, bodyStart: int, bracketL='{', bracketR='}'):
    bracketDeep = 0
    bodyEnd = 0

    sliceIt = islice(text, bodyStart, len(text))
    for bodyEnd, char in enumerate(sliceIt, bodyStart):
        if char == bracketL:
            bracketDeep += 1
        elif char == bracketR:
            bracketDeep -= 1
            if not bracketDeep:
                break

    functionText = text[bodyStart:bodyEnd + 1]
    return functionText


def generateExpressionUntilChar(text: str, expStart: int, splitChar: str,
                                bracketL='(', bracketR=')'):
    assert splitChar not in f'\\"{bracketL}{bracketR}'

    bracketDeep = 0
    expEnd = 0
    ignore = False
    escaped = False

    sliceIt = islice(text, expStart, len(text) + 1)
    for expEnd, char in enumerate(sliceIt, expStart):
        if escaped:
            escaped = False
        elif char == '\\':
            escaped = True
        elif char == '"':
            ignore = not ignore
        elif ignore:
            pass
        elif char == bracketL:
            bracketDeep += 1
        elif char == bracketR:
            bracketDeep -= 1
            if bracketDeep < 0:
                yield text[expStart:expEnd]
                return
        elif char == splitChar and bracketDeep == 0:
            yield text[expStart:expEnd]
            expStart = expEnd + 1

    yield text[expStart:expEnd + 1]
