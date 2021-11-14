from functools import cached_property

from freecad_stub_gen.generators.common.names import getModuleName
from freecad_stub_gen.util import OrderedSet


class EmptyType:
    @property
    def value(self):
        return self

    def __eq__(self, other):
        return other is None or other == 'object'

    def __hash__(self):
        return 1

    def __str__(self):
        return 'object'


Empty = EmptyType()


class ArgumentsIter:
    @cached_property
    def imports(self):
        return OrderedSet()

    def __iter__(self):
        """
        Cannot inherit this class from Iterable/Iterator
        because super() will not find correct class.
        """
        for argType in super().__iter__():
            match argType:
                case str() if '[' not in argType and (mod := getModuleName(argType)):
                    self.imports.add(mod)
                case UnionArguments() as ua:
                    self.imports.update(ua.imports)
            yield str(argType)


class UnionArguments(ArgumentsIter, OrderedSet):
    def __str__(self):
        return ' | '.join(self)


class TupleArgument(ArgumentsIter, list):
    def __str__(self):
        if self:
            return f'tuple[{", ".join(self)}]'
        return 'tuple'


RetType = UnionArguments[str] | EmptyType | str


class InvalidReturnType(ValueError):
    pass
