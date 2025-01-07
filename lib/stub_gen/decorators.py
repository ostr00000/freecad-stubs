import logging
import sys
from collections.abc import Callable, Iterable

import clang.cindex as cc
from decorator import decorator


@decorator
def logCurrentTaskDecFactory(
    fun,
    *args,
    logger: logging.Logger | None = None,
    msg: str = '',
    **kwargs,
):
    """Decorate function to write its task before and after execution."""
    if logger is None:
        mod = sys.modules[fun.__module__]
        sentinel = object()
        maybeLogger = getattr(mod, 'logger', sentinel)

        if maybeLogger is sentinel:
            msg = f"Module {fun.__module__} does not have global `logger`!"
            raise TypeError(msg)

        if not isinstance(maybeLogger, logging.Logger):
            msg = f"Module {fun.__module__}:logger is not a logging.Logger"
            raise TypeError(msg)

        logger = maybeLogger

    if not msg:
        msg = fun.__name__

    logger.info(f"{msg} started...")
    try:
        ret = fun(*args, **kwargs)
    except Exception:
        logger.exception(f"{msg} terminated with exception!")
        raise

    logger.info(f"{msg} successfully finished.")
    return ret


def uniqueIteratorDec[
    **Param, Ret
](fun: Callable[Param, Iterable[Ret]]) -> Callable[Param, Iterable[Ret]]:
    def uniqueIterator(*args: Param.args, **kwargs: Param.kwargs) -> Iterable[Ret]:
        seen = set()
        for item in fun(*args, **kwargs):
            if item not in seen:
                seen.add(item)
                yield item

    return uniqueIterator


def checkKindDecFactory(kinds: list[cc.CursorKind]):
    def checkKindDec(fun):
        def checkKindFun(*args, **kwargs):
            wrapper = args[0]
            if wrapper.cursor.kind not in kinds:
                msg = f"Invalid cursor kind: {wrapper.cursor.kind} (expected: {kinds})"
                raise TypeError(msg)
            return fun(*args, **kwargs)

        return checkKindFun

    return checkKindDec
