import atexit
import functools
import logging
import time
from collections import defaultdict
from collections.abc import Hashable, Iterator

from freecad_stub_gen.ordered_set import OrderedSet

logger = logging.getLogger(__name__)
printAllValues = defaultdict[str, OrderedSet](OrderedSet)


def addPrintAllValue(topic: str, value: Hashable):
    if topic not in printAllValues:

        @atexit.register
        def printValues():
            logger.debug(f"Values for {topic}:")
            for k in printAllValues[topic]:
                logger.debug(f" - `{k}`")

    printAllValues[topic].add(value)


def logProgress[T](it: Iterator[T], total: int, desc='') -> Iterator[T]:
    for i, val in enumerate(it):
        logger.debug(f'Progress {desc}[{i:{len(str(total))}}/{total}]')
        yield val


def timeDec(fun):
    @functools.wraps(fun)
    def timeDecWrapper(*args, **kwargs):
        t0 = time.time()
        try:
            return fun(*args, **kwargs)
        finally:
            t1 = time.time()
            logger.info(f"Generating time: {t1-t0}[s]")

    return timeDecWrapper
