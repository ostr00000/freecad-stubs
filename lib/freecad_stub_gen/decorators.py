import logging
import sys

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
