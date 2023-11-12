import atexit
import logging
from collections import defaultdict
from collections.abc import Hashable

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
