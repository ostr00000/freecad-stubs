from __future__ import annotations

from typing import TYPE_CHECKING

from clang import cindex as cc

from stub_gen.decorators import checkKindDecFactory, uniqueIteratorDec
from stub_gen.scan.filter_gen import PreorderWithStack, genLambdas, genReturns
from stub_gen.scan.walk import STANDARD_RESOLVE_KINDS, standardResolve

if TYPE_CHECKING:
    from collections.abc import Iterable

    from stub_gen.scan.wrapper import CursorWrapper


@checkKindDecFactory(
    [
        cc.CursorKind.FUNCTION_DECL,
        cc.CursorKind.CXX_METHOD,
        *STANDARD_RESOLVE_KINDS,
    ]
)
@uniqueIteratorDec
def genFunctionReturnValues(
    functionDeclaration: CursorWrapper,
) -> Iterable[CursorWrapper]:
    res = standardResolve(functionDeclaration)
    # TODO @PO: getMethodImplementation
    with PreorderWithStack(res) as ps:
        for maybeReturn in genReturns(ps.walkPreorder()):
            if any(genLambdas(ps.stack)):
                continue  # this return is inside a lambda expression
            yield maybeReturn
