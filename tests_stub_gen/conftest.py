from dataclasses import dataclass
from functools import cached_property
from typing import ClassVar

import clang.cindex as cc
import logging

from stub_gen.scan.wrapper import CursorWrapper

logger = logging.getLogger(__name__)


@dataclass
class InputCode:
    code: str
    returnCount: int = 1

    DIAGNOSTIC_ERROR_LEVEL: ClassVar[int] = 4
    # https://clang.llvm.org/docs/InternalsManual.html#the-diagnostic-kinds-td-files

    @cached_property
    def trUnit(self) -> cc.TranslationUnit:
        tu = cc.TranslationUnit.from_source(
            'tmp.cpp',
            args=['-std=c++11'],
            unsaved_files=[('tmp.cpp', self.code)],
            options=0,
        )
        for d in tu.diagnostics:
            if d.severity >= self.DIAGNOSTIC_ERROR_LEVEL:
                logger.error(f"There is a diagnostic: `{d.spelling}`")
        return tu

    @cached_property
    def trWrapper(self) -> CursorWrapper:
        return CursorWrapper.toWrapper(self.trUnit)

    def getParameterName(self) -> str:
        rawCode = self.code.strip().replace('\n', ' ')
        codeBeginning = rawCode.split(' ', maxsplit=2)[:2]
        return ' '.join(codeBeginning)


def pytest_make_parametrize_id(config, val):
    if isinstance(val, InputCode):
        return val.getParameterName()
    return None
