from collections.abc import Hashable, Iterable
from typing import Generic, TypeVar

T = TypeVar('T', bound=Hashable)


class OrderedSet(Generic[T]):
    def __init__(self, it: Iterable[T] = ()):
        self._data: dict[T, None] = dict.fromkeys(it)

    def add(self, item: T):
        self._data[item] = None

    def pop(self, item: T):
        self._data.pop(item)

    def first(self):
        return next(iter(self))

    def update(self, it: Iterable[T]):
        self._data.update(dict.fromkeys(it))

    def clear(self):
        self._data.clear()

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        return '|'.join(map(str, self))


class OrderedStrSet(OrderedSet[str]):
    pass
