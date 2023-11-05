import atexit
from collections import defaultdict
from typing import Hashable

from freecad_stub_gen.ordered_set import OrderedSet

printAllValues = defaultdict[str, OrderedSet](OrderedSet)


def addPrintAllValue(topic: str, value: Hashable):
    if topic not in printAllValues:
        @atexit.register
        def printValues():
            print(f"Values for {topic}:")
            for k in printAllValues[topic]:
                print(f" - `{k}`")

    printAllValues[topic].add(value)
