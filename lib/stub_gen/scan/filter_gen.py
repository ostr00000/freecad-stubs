from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator
from functools import partial
from typing import Self

from clang import cindex as cc

from stub_gen.decorators import checkKindDecFactory
from stub_gen.scan.utils import SafeAccess
from stub_gen.scan.wrapper import CursorLike, CursorWrapper


def _walkPreorderWithStack(
    cursorWrapper: CursorWrapper, stack: list[CursorWrapper]
) -> Iterable[CursorWrapper]:
    """Depth-first preorder walk over the cursor and its descendants.

    Yields cursors.
    Based on: `cindex.Cursor:walk_preorder`.
    """
    yield cursorWrapper

    stack.append(cursorWrapper)
    for child in cursorWrapper.genChildren():
        yield from _walkPreorderWithStack(child, stack)
    stack.pop()


class PreorderWithStack:
    def __init__(self, cursorWrapper: CursorWrapper):
        self.cursorWrapper = cursorWrapper
        self.stack: list[CursorWrapper] = []

    def __enter__(self):
        return self

    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        self.stack.clear()

    def __iter__(self):
        return self.walkPreorder()

    def walkPreorder(self):
        if self.stack:
            msg = "Stack is not empty"
            raise ValueError(msg)
        return _walkPreorderWithStack(self.cursorWrapper, self.stack)


def genCursorWithKind(
    curGen: Iterable[CursorWrapper], kind: cc.CursorKind
) -> Iterable[CursorWrapper]:
    for w in curGen:
        if w.cursor.kind == kind:
            yield w


genConstructors = partial(genCursorWithKind, kind=cc.CursorKind.CONSTRUCTOR)
genFunctions = partial(genCursorWithKind, kind=cc.CursorKind.FUNCTION_DECL)
genMethods = partial(genCursorWithKind, kind=cc.CursorKind.CXX_METHOD)
genVarDeclarations = partial(genCursorWithKind, kind=cc.CursorKind.VAR_DECL)
genCalls = partial(genCursorWithKind, kind=cc.CursorKind.CALL_EXPR)
genReturns = partial(genCursorWithKind, kind=cc.CursorKind.RETURN_STMT)
genLambdas = partial(genCursorWithKind, kind=cc.CursorKind.LAMBDA_EXPR)


def isDefinedInTU(*, cursorWrapper: CursorWrapper, tu: cc.TranslationUnit) -> bool:
    return SafeAccess(cursorWrapper.cursor.location).file.name() == tu.spelling


def genDefinedInTU(curGen: Iterable[CursorWrapper], tu: cc.TranslationUnit):
    for wrapper in curGen:
        if isDefinedInTU(cursorWrapper=wrapper, tu=tu):
            yield wrapper


type QualifiedName = tuple[str, ...]


@checkKindDecFactory([cc.CursorKind.VAR_DECL])
def getFullQualifiedName(wrapper: CursorWrapper) -> QualifiedName:
    if (maybeCachedQN := wrapper.cache.get(getFullQualifiedName.__name__)) is not None:
        return maybeCachedQN

    names = [wrapper.cursor.spelling]
    while wrapper.semanticParent is not None:
        wrapper = wrapper.semanticParent
        if wrapper.cursor.kind in (cc.CursorKind.NAMESPACE, cc.CursorKind.CLASS_DECL):
            names.insert(0, wrapper.cursor.spelling)

    qn = tuple(names)
    wrapper.cache[getFullQualifiedName.__name__] = qn
    return qn


@checkKindDecFactory([cc.CursorKind.CALL_EXPR])
def getCallArgs(
    wrapper: CursorWrapper, *, expectedArgNum: int | None = None
) -> list[CursorWrapper]:
    args = wrapper.getArguments()
    if expectedArgNum is not None and len(args) != expectedArgNum:
        msg = (
            f"In function {wrapper.cursor.spelling}: "
            f"expected {expectedArgNum} arguments, got {len(args)}"
        )
        raise ValueError(msg)
    return args


def genWithQualName(curGen: Iterable[CursorWrapper], qualName: QualifiedName):
    for wrapper in curGen:
        if getFullQualifiedName(wrapper) == qualName:
            yield wrapper


def genWithSpelling(curGen: Iterable[CursorWrapper], spelling: str):
    for wrapper in curGen:
        if wrapper.cursor.spelling == spelling:
            yield wrapper


class NonOverridableDict[K, V](dict[K, V]):
    def __setitem__(self, key, value):
        if key in self:
            msg = f"Cannot redefine key '{key}'"
            raise ValueError(msg)
        super().__setitem__(key, value)


type CursorIter = Iterable[CursorWrapper]
type IterFilter = Callable[[CursorIter], CursorIter]


class Gen:
    @classmethod
    def genChildren(cls, cursorLike: CursorLike) -> Self:
        cursorWrapper = CursorWrapper.toWrapper(cursorLike)
        return cls(cursorWrapper.genChildren())

    @classmethod
    def walkPreorder(cls, cursorLike: CursorLike) -> Self:
        cursorWrapper = CursorWrapper.toWrapper(cursorLike)
        return cls(cursorWrapper.walkPreorder())

    def __init__(self, it: CursorIter):
        self.it: Iterator[CursorWrapper] = iter(it)
        self.funToCost = NonOverridableDict[IterFilter, int]()

    def __iter__(self):
        it = self.it
        for fun in sorted(self.funToCost, key=self.funToCost.__getitem__):
            it = fun(it)

        return iter(it)

    ## based on kind
    def genConstructors(self):
        self.funToCost[genConstructors] = 10
        return self

    def genFunctions(self):
        self.funToCost[genFunctions] = 10
        return self

    def genMethods(self):
        self.funToCost[genMethods] = 10
        return self

    def genVarDeclarations(self):
        self.funToCost[genVarDeclarations] = 10
        return self

    def genCall(self):
        self.funToCost[genCalls] = 10
        return self

    ## special
    def genDefinedInTU(self, tu: cc.TranslationUnit):
        self.funToCost[partial(genDefinedInTU, tu=tu)] = 100
        return self

    def genWithQualName(self, qualName: QualifiedName):
        self.funToCost[partial(genWithQualName, qualName=qualName)] = 80
        return self

    def genWithSpelling(self, spelling: str):
        self.funToCost[partial(genWithSpelling, spelling=spelling)] = 50
        return self
