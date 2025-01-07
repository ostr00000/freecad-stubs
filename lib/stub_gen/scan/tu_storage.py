import logging
from functools import cache
from pathlib import Path
from threading import Lock

import clang.cindex as cc

from stub_gen.scan.compile_commands import CompileEntry, getCompileEntries

logger = logging.getLogger(__name__)


@cache
def getFreeCADPath():
    curPath = Path(__file__).resolve()

    while not (freeCADPath := curPath / 'FreeCAD').exists():
        curPath = curPath.parent

    logger.debug(f'FreeCAD path: {freeCADPath}')
    return freeCADPath


class TransactionUnitStorage:
    def __init__(self):
        self.index = cc.Index.create()

        self._fileToTU: dict[Path, cc.TranslationUnit] = {}
        self._compileEntry: dict[Path, CompileEntry] = {
            ce.file: ce for ce in getCompileEntries(self._getCompileCommandsPath())
        }

        self._mainParsingLock = Lock()
        self._fileToParsingLock: dict[Path, Lock] = {}

    def _getCompileCommandsPath(self) -> Path:
        # TODO @PO: move this to configuration file
        return getFreeCADPath() / 'build/debug/compile_commands.json'

    def __getitem__(self, item: str | Path):
        tuPath = Path(item).resolve()
        if (tu := self._fileToTU.get(tuPath)) is not None:
            return tu

        with self._mainParsingLock:
            # using main lock to do not create multiple lock for same path
            if (lock := self._fileToParsingLock.get(tuPath)) is None:
                self._fileToParsingLock[tuPath] = lock = Lock()

        with lock:
            # try again - maybe another thread filled it in meantime
            if (tu := self._fileToTU.get(tuPath)) is None:
                self._fileToTU[tuPath] = tu = self._parse(tuPath)

        return tu

    def _parse(self, tuPath: Path) -> cc.TranslationUnit:
        ce = self._compileEntry[tuPath]
        return self.index.parse(
            tuPath,
            args=ce.commandArgs,
            # more options:
            # https://clang.llvm.org/doxygen/group__CINDEX__TRANSLATION__UNIT.html#gab1e4965c1ebe8e41d71e90203a723fe9
            options=(
                cc.TranslationUnit.PARSE_NONE
                # | cc.TranslationUnit.PARSE_PRECOMPILED_PREAMBLE
                # | next(iter({0x100: 'CXTranslationUnit_CreatePreambleOnFirstParse'}))
                # | next(iter({0x400: 'CXTranslationUnit_SingleFileParse'}))
                | cc.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD
            ),
        )


transactionUnitStorage = TransactionUnitStorage()
