import logging
from collections.abc import Callable, Iterable

import clang.cindex as cc

type _Decorator[BaseFun: Callable] = Callable[[BaseFun], BaseFun]

def logCurrentTaskDecFactory(
    *, logger: logging.Logger | None = None, msg: str = ''
) -> _Decorator: ...
def uniqueIteratorDec[
    **Param, Ret
](fun: Callable[Param, Iterable[Ret]]) -> Callable[Param, Iterable[Ret]]: ...
def checkKindDecFactory[
    **Param, Ret
](kinds: list[cc.CursorKind]) -> _Decorator[Callable[Param, Ret]]: ...
