import re
import sys
from functools import wraps


class MatchWrapper:
    def __init__(self, origMatch: re.Match):
        self.origMatch: re.Match | None = origMatch
        self.state: dict | None = None

    def __getstate__(self):
        if self.state is not None:
            return self.state

        if self.origMatch is None:
            msg = "Original match is `None`!"
            raise TypeError(msg)

        return {'groups': self.origMatch.groups()}

    def __setstate__(self, state):
        if not isinstance(state, dict):
            msg = f"Expected dict to restore state for {type(self)}"
            raise TypeError(msg)

        self.origMatch = None
        self.state = state

    def __getattr__(self, item):
        if self.origMatch is None:
            if self.state is None:
                msg = "State object is `None`!"
                raise TypeError(msg)
            try:
                return self.state[item]
            except KeyError as ke:
                raise AttributeError from ke

        return getattr(self.origMatch, item)


class Visitor:
    """Based on https://github.com/mbr/visitor/blob/master/visitor/__init__.py."""

    def visit(self, node):
        mro = (node if isinstance(node, type) else type(node)).mro()
        for cls in mro:
            meth = getattr(self, 'visit_' + cls.__name__, None)
            if meth is not None:
                return meth(node)

        return self.default(node)

    def default(self, node):
        pass


class PickleFixerVisitor(Visitor):
    def visit_list(self, listNode: list):
        return [self.visit(el) for el in listNode]

    def visit_tuple(self, tupleNode: list):
        return tuple(self.visit(t) for t in tupleNode)

    def visit_dict(self, dictNode: dict):
        return {self.visit(k): self.visit(v) for k, v in dictNode.items()}

    def visit_Match(self, match: re.Match):
        return MatchWrapper(match)

    def visit_MatchWrapper(self, node):
        return node

    def default(self, node):
        if hasattr(node, '__dict__'):
            for attrName, attrVal in node.__dict__.items():
                node.__dict__[attrName] = self.visit(attrVal)
        elif node.__class__.__module__ in sys.stdlib_module_names:
            return node

        return node


def preprocessPickleDec(fun):
    @wraps(fun)
    def _innerPreProcess(*arg, **kwargs):
        ret = fun(*arg, **kwargs)
        pfv = PickleFixerVisitor()
        return pfv.visit(ret)

    return _innerPreProcess
