import atexit
import functools
import logging
import time
from collections import defaultdict
from collections.abc import Callable, Hashable, Iterable, Iterator
from pathlib import Path

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


def logProgress[T](it: Iterable[T], total: int, desc='') -> Iterator[T]:
    for i, val in enumerate(it):
        logger.debug(f'Progress {desc}[{i:{len(str(total))}}/{total}]')
        yield val


def _sortByCoreLib(p: Path):
    isCore = any(c in p.parts for c in ('Gui', 'Base', 'App'))
    return -isCore, p


def genFilesWithLog(gen: Callable[[], Iterable[Path]], **kwargs):
    total = sum(1 for _ in gen())
    g = sorted(gen(), key=_sortByCoreLib)
    yield from logProgress(g, total, **kwargs)


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
