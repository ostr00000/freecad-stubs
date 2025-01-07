from __future__ import annotations

import enum
import logging
from typing import TYPE_CHECKING

import clang.cindex as cc

from stub_gen.scan.filter_gen import Gen, getFullQualifiedName
from stub_gen.scan.tu_storage import transactionUnitStorage
from stub_gen.scan.utils import uniqueIterator

if TYPE_CHECKING:
    from collections.abc import Iterable
    from pathlib import Path

    from stub_gen.scan.wrapper import CursorWrapper

logger = logging.getLogger(__name__)


def getString(cursorWrapper: CursorWrapper) -> str:
    wrapper = standardResolve(cursorWrapper)

    match wrapper.cursor.kind:
        case cc.CursorKind.STRING_LITERAL:
            stringValue = wrapper.cursor.spelling

        case cc.CursorKind.VAR_DECL:
            arrayWrapper = getAssignment(wrapper)
            stringValue = getString(arrayWrapper)

        case unknown:
            raise NotImplementedError(unknown)

    return stringValue.removeprefix('"').removesuffix('"')


class EmptySpelling(Exception):
    pass


def getInt(cursorWrapper: CursorWrapper) -> int:
    wrapper = resolveReference(cursorWrapper)

    match wrapper.cursor.kind:
        case cc.CursorKind.INTEGER_LITERAL:
            numText = wrapper.cursor.spelling
            if numText == '':
                # why? maybe because of macro?
                raise EmptySpelling

        case cc.CursorKind.VAR_DECL:
            valueWrapper = getAssignment(cursorWrapper)
            return getInt(valueWrapper)

        case unknown:
            raise NotImplementedError(unknown)

    return int(numText)


def getEnum[E: enum.IntFlag](cursorWrapper: CursorWrapper, enumClass: type[E]) -> E:
    wrapper = standardResolve(cursorWrapper)

    match wrapper.cursor.kind:
        case cc.CursorKind.INTEGER_LITERAL:
            try:
                i = getInt(wrapper)
            except EmptySpelling:
                [tok] = cursorWrapper.getSpellingTokens()
                return enumClass[tok]
            else:
                return enumClass(i)

        case cc.CursorKind.BINARY_OPERATOR:
            enumGen = (getEnum(c, enumClass) for c in wrapper.getChildren())
            enumObj = next(enumGen)
            for e in enumGen:
                enumObj |= e
            return enumObj

        case unknown:
            raise NotImplementedError(unknown)


def getList(cursorWrapper: CursorWrapper) -> list[CursorWrapper]:
    wrapper = standardResolve(cursorWrapper)

    match wrapper.cursor.kind:
        case cc.CursorKind.VAR_DECL:
            arrayWrapper = getAssignment(wrapper)
            return getList(arrayWrapper)

        case cc.CursorKind.INIT_LIST_EXPR:
            return wrapper.getChildren()

        case unknown:
            raise NotImplementedError(unknown)


def getAssignment(cursorWrapper: CursorWrapper) -> CursorWrapper:
    if a := getDirectAssignment(cursorWrapper):
        return a  # take the direct assignment to variable

    res = standardResolve(cursorWrapper)
    if a := getDirectAssignment(res):
        return a  # take assignment at declaration

    if a := getAssignmentFromTu(res, res.cursor.translation_unit):
        return a  # take any assignment in current tu

    visited = {res.filePathNotNone}
    for searchPath in uniqueIterator(_genAssignmentSearchPaths(res), visited=visited):
        tu = transactionUnitStorage[searchPath]
        if a := getAssignmentFromTu(res, tu):
            return a  # take any assignment using heuristic path for tu

    msg = f"Cannot find assignment {res.ed}"
    raise ValueError(msg)


def _genAssignmentSearchPaths(cursorWrapper: CursorWrapper) -> Iterable[Path]:
    # we should search all files for assignment for this value,
    # but we may use heuristic here are search in file with suffix `Py.h` first
    filePath = cursorWrapper.filePathNotNone

    if filePath.suffix == '.h':
        filePath = filePath.with_suffix('.cpp')
        yield filePath
        yield filePath.with_stem(filePath.stem + 'Py')

    msg = "Needs to add more heuristic or general search"
    raise NotImplementedError(msg)


def getAssignmentFromTu(
    cursorWrapper: CursorWrapper, tu: cc.TranslationUnit
) -> CursorWrapper | None:
    qn = getFullQualifiedName(cursorWrapper)

    for w in (
        Gen.genChildren(tu).genVarDeclarations().genWithQualName(qn).genDefinedInTU(tu)
    ):
        if a := getDirectAssignment(w):
            return a

    return None


def getDirectAssignment(cursorWrapper: CursorWrapper) -> CursorWrapper | None:
    match cursorWrapper.cursor.kind, cursorWrapper.cursor.type.kind:
        case cc.CursorKind.VAR_DECL, cc.TypeKind.INCOMPLETEARRAY:
            return None

        case cc.CursorKind.VAR_DECL, cc.TypeKind.CONSTANTARRAY:
            assignChildren = cursorWrapper.getChildren()
            for a in reversed(assignChildren):
                if a.cursor.type.kind != cc.TypeKind.CONSTANTARRAY:
                    continue
                return a
            msg = "Cannot find assigned value in constant array"
            raise ValueError(msg)

        case cc.CursorKind.VAR_DECL, _:
            # TODO @PO: add more allowed types
            raise NotImplementedError

        case cc.CursorKind.INIT_LIST_EXPR, _:
            return cursorWrapper

    return None


def stripCast(cursorWrapper: CursorWrapper) -> CursorWrapper:
    match cursorWrapper.cursor.kind:
        case (
            cc.CursorKind.CSTYLE_CAST_EXPR
            | cc.CursorKind.CXX_REINTERPRET_CAST_EXPR
            | cc.CursorKind.CXX_STATIC_CAST_EXPR
            | cc.CursorKind.CXX_DYNAMIC_CAST_EXPR
            | cc.CursorKind.CXX_CONST_CAST_EXPR
        ):
            children = cursorWrapper.getChildren()
            try:
                _cast, obj = children
            except ValueError:
                # why is there sometimes a missing `_cast`?
                obj = children[-1]
            return obj

    return cursorWrapper


def stripPointer(cursorWrapper: CursorWrapper) -> CursorWrapper:
    match cursorWrapper.cursor.kind, cursorWrapper.cursor.type.kind:
        case cc.CursorKind.UNARY_OPERATOR, cc.TypeKind.POINTER:
            children = cursorWrapper.getChildren()
            (obj,) = children
            return obj

    return cursorWrapper


def resolveReference(cursorWrapper: CursorWrapper) -> CursorWrapper:
    match cursorWrapper.cursor.kind:
        case cc.CursorKind.DECL_REF_EXPR:
            return cursorWrapper.referenced
    return cursorWrapper


def stripElaborated(cursorWrapper: CursorWrapper) -> CursorWrapper:
    match cursorWrapper.cursor.kind, cursorWrapper.cursor.type.kind:
        case cc.CursorKind.VAR_DECL, cc.TypeKind.ELABORATED:
            elaboratedChild = cursorWrapper.getChildren()
            (_qualifiers, obj) = elaboratedChild
            return obj

    return cursorWrapper


def standardResolve(cursorWrapper: CursorWrapper) -> CursorWrapper:
    cur = cursorWrapper
    _debug_prev = []
    while True:
        prev = cur
        _debug_prev.append(prev)

        cur = resolveReference(cur)
        cur = stripCast(cur)
        cur = stripPointer(cur)
        cur = stripElaborated(cur)

        if cur is prev:
            break

    return cur


STANDARD_RESOLVE_KINDS = (
    cc.CursorKind.DECL_REF_EXPR,
    cc.CursorKind.CXX_REINTERPRET_CAST_EXPR,
    cc.CursorKind.CXX_STATIC_CAST_EXPR,
    cc.CursorKind.CXX_DYNAMIC_CAST_EXPR,
    cc.CursorKind.CXX_CONST_CAST_EXPR,
    cc.CursorKind.CSTYLE_CAST_EXPR,
    cc.CursorKind.UNARY_OPERATOR,
    cc.CursorKind.VAR_DECL,
)
