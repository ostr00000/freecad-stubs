from collections.abc import Hashable, Iterable


class SafeAccess[V]:
    # I need safe access:
    # https://discuss.python.org/t/revisiting-pep-505/74568
    # https://peps.python.org/pep-0505/

    def __init__(self, val: V, default=None):
        self.val = val
        self.default = default

    def __getattr__(self, item):
        return SafeAccess(getattr(self.val, item, self.default), self.default)

    def __call__(self):
        return self.val


def uniqueIterator[
    Item: Hashable
](it: Iterable[Item], visited: set[Item] | None = None) -> Iterable[Item]:
    seen = visited if visited is not None else set[Item]()

    for item in it:
        if item in seen:
            continue

        seen.add(item)
        yield item
