import logging
from collections.abc import Callable

type _Decorator[BaseFun: Callable] = Callable[[BaseFun], BaseFun]

def logCurrentTaskDecFactory(
    *, logger: logging.Logger | None = None, msg: str = ''
) -> _Decorator: ...
