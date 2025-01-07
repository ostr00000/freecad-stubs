from __future__ import annotations

import logging
from contextvars import ContextVar
from functools import cached_property
from pathlib import Path
from pprint import pformat
from typing import TYPE_CHECKING, Any, Self, TypedDict

import clang.cindex as cc

from stub_gen.scan.utils import SafeAccess

if TYPE_CHECKING:
    from collections.abc import Iterable

logger = logging.getLogger(__name__)
transactionUnit = ContextVar[cc.TranslationUnit]('transactionUnit')


class CursorExposedData(TypedDict):
    type_kind: str
    kind: cc.CursorKind
    spelling: str
    location: cc.SourceLocation
    location_text: str
    result_type_kind: str
    raw_comment: str
    get_arguments: list[CursorWrapper]
    get_tokens: list[str]
    joined_tokens: str


class CursorWrapper:
    TOKEN_REPR_MAPPING = str.maketrans(
        {
            '{': '{\n',
            ';': ';\n',
        }
    )

    def __init__(self, cursor: cc.Cursor, visitorParent: CursorWrapper | None = None):
        self.cursor = cursor
        self.visitorParent = visitorParent
        self.cache: dict[str, Any] = {}

    @classmethod
    def toWrapper(cls, cursorLike: CursorLike = None) -> CursorWrapper:
        match cursorLike:
            case CursorWrapper() as wrapper:
                return wrapper
            case cc.Cursor() as cursor:
                return cls(cursor)
            case cc.TranslationUnit() as tu:
                return cls(tu.cursor)
            case None:
                return CursorWrapper.toWrapper(transactionUnit.get())
            case _:
                msg = f"Expected CursorLike, got {type(cursorLike).__name__}"
                raise TypeError(msg)

    def exposeData(self):
        tokens = [t.spelling for t in self.cursor.get_tokens()]
        joined_tokens = ' '.join(tokens).translate(self.TOKEN_REPR_MAPPING)
        return CursorExposedData(
            type_kind=self.cursor.type.kind,
            kind=self.cursor.kind,
            spelling=self.cursor.spelling,
            location=self.cursor.location,
            location_text=f'{self.filePath}:{self.cursor.location.line}',
            result_type_kind=self.cursor.result_type.kind,
            raw_comment=self.cursor.raw_comment,
            get_arguments=self.getArguments(),
            get_tokens=tokens,
            joined_tokens=joined_tokens,
        )

    @cached_property
    def ed(self) -> CursorExposedData:
        return self.exposeData()

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.cursor == other.cursor
        return NotImplemented

    def __hash__(self):
        return hash(self.cursor)

    def __str__(self):
        return pformat(self.ed, depth=1, sort_dicts=False)

    def getArguments(self) -> list[CursorWrapper]:
        return [type(self)(a) for a in self.cursor.get_arguments()]

    @property
    def semanticParent(self) -> Self | None:
        if p := self.cursor.semantic_parent:
            return type(self)(p)
        return None

    @property
    def lexicalParent(self) -> Self | None:
        if p := self.cursor.lexical_parent:
            return type(self)(p)
        return None

    @property
    def referenced(self) -> Self:
        if p := self.cursor.referenced:
            return type(self)(p)
        msg = "Please check first if this is a reference expression!"
        raise TypeError(msg)

    @classmethod
    def debug(cls, cursor: cc.Cursor):
        return logger.debug(str(cls(cursor)))

    def getChildren(self) -> list[Self]:
        return list(self.genChildren())

    def genChildren(self) -> Iterable[Self]:
        # TODO @PO: optimize
        #  we not always want to fetch all children in generator

        cFun = cc.callbacks['cursor_visit']  # type: ignore[reportAttributeAccessIssue]
        children: list[Self] = []
        cc.conf.lib.clang_visitChildren(
            self.cursor,
            cFun(self._childrenVisitorCallback),
            children,  # type: ignore[reportArgumentType]
        )

        yield from children

    def _childrenVisitorCallback(
        self, child: cc.Cursor, _parent: cc.Cursor, children: list[Self]
    ):
        child._tu = self.cursor._tu  # noqa: SLF001
        childWrapper: Self = type(self)(child, self)
        children.append(childWrapper)
        return 1  # continue

    def walkPreorder(self) -> Iterable[Self]:
        yield self
        for child in self.genChildren():
            yield from child.walkPreorder()

    def getTokens(self) -> list[cc.Token]:
        """Return tokens for a current cursor.

        This is broken in clang, so we must use workaround. See:
        https://github.com/llvm/llvm-project/issues/68340
        """
        tu = self.cursor.translation_unit

        start = self.cursor.extent.start
        start = cc.SourceLocation.from_position(
            tu, start.file, start.line, start.column
        )

        end = self.cursor.extent.end
        end = cc.SourceLocation.from_position(tu, end.file, end.line, end.column)

        extent = cc.SourceRange.from_locations(start, end)
        return list(tu.get_tokens(extent=extent))

    def getSpellingTokens(self) -> list[str]:
        return [t.spelling for t in self.getTokens()]

    @cached_property
    def filePath(self) -> Path | None:
        if filename := SafeAccess(self.cursor.location.file).name():
            return Path(filename)
        return None

    @cached_property
    def filePathNotNone(self):
        if self.filePath is None:
            msg = "CursorWrapper is not associated with a file."
            raise ValueError(msg)
        return self.filePath


type CursorLike = cc.Cursor | CursorWrapper | cc.TranslationUnit | None


class DiagnosticRepr:
    def __init__(self, tu: cc.TranslationUnit):
        self.tu = tu

    def genDiagnostics(self, level: int):
        for d in self.tu.diagnostics:
            if d.severity >= level:
                yield d.spelling

    def __str__(self):
        msgs = [f'{d.severity}: {d.spelling}' for d in self.tu.diagnostics]
        return '\n'.join(msgs)

    def logErrorDiagnostics(self):
        for text in self.genDiagnostics(level=cc.Diagnostic.Error):
            logger.error(f"There is a diagnostic: `{text}`")
