from functools import cached_property
from typing import TypeVar, Generator, Protocol

from freecad_stub_gen.generators.common.names import getModuleName, useAliasedModule
from freecad_stub_gen.util import OrderedSet, indent

T = TypeVar('T')


class EmptyType:
    @property
    def value(self):
        return self

    def __eq__(self, other):
        return other is Empty or other == 'typing.Any'

    def __hash__(self):
        return 1

    def __str__(self):
        return 'typing.Any'


Empty = EmptyType()


class SizedIterable(Protocol):
    """
    We cannot use `Collection` from collections.abc,
    because mro first chose collections over list/dict.
    """

    def __iter__(self):
        return super().__iter__()

    def __len__(self):
        return super().__len__()


class ArgumentsIter(SizedIterable):
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
                case str() if '[' not in argType and getModuleName(argType):
                    argType = useAliasedModule(argType, self.imports)
                case EmptyType() if len(self) > 1:
                    self.imports.add('typing')
                case UnionArguments() as ua:
                    self.imports.update(ua.imports)
            yield str(argType)


class UnionArguments(ArgumentsIter, OrderedSet[T]):
    def __str__(self):
        values = list(self)
        if 'None' in values:
            values.remove('None')
            values.append('None')

        return ' | '.join(values)


class TupleArgument(ArgumentsIter, list):
    def __init__(self, gen: Generator[T, None, bool | None] = ()):
        super().__init__()
        try:
            while True:
                self.append(next(gen))
        except StopIteration as st:
            self.repeated = len(self) == 1 and st.value is True

    def __str__(self):
        if len(self) == 1 and self.repeated:
            # use iter instead of index [0] to map module
            return f'tuple[{next(iter(self))}, ...]'
        elif self:
            return f'tuple[{", ".join(self)}]'
        return 'tuple'

    def __eq__(self, other):
        return isinstance(other, type(self)) \
               and self.repeated == other.repeated \
               and super().__eq__(other)


RetType = UnionArguments[str] | EmptyType | str


class InvalidReturnType(ValueError):
    pass


class DictArgument(ArgumentsIter):
    def __init__(self):
        self.keys = UnionArguments()
        self.values = UnionArguments()

    def add(self, key: RetType, value: RetType):
        if isinstance(key, UnionArguments):
            keyStr = str(key)
            self.imports.update(key.imports)
            key = keyStr
        self.keys.add(key)
        self.values.add(value)

    def __bool__(self):
        return bool(self.keys and self.values)

    def __str__(self):
        if not self:
            return 'dict'

        ret = f'dict[{self.keys}, {self.values}]'
        self.imports.update(self.keys.imports)
        self.imports.update(self.values.imports)
        return ret


class ListIter(list, ArgumentsIter):
    pass


class TypedDictGen(dict, ArgumentsIter):
    def __init__(self, funName: str):
        super().__init__()
        self.funName = funName
        self.alternativeSyntax = False

    def add(self, key: str, value: RetType):
        if not key.isidentifier():  # + keyword (not implemented)
            self.alternativeSyntax |= True
        self[key] = value

    def __str__(self):
        typedDictName = f'Return{self.funName[0].upper() + self.funName[1:]}Dict'
        listIter = ListIter(self.values())

        if self.alternativeSyntax:
            content = ', '.join(f"'{k}': {v}" for k, v in zip(self.keys(), listIter))
            fun = f"{typedDictName} = typing.TypedDict('{typedDictName}', {{{content}}})"

        else:
            lines = [f'{k}: {v}' for k, v in zip(self.keys(), listIter)]
            content = indent('\n'.join(lines))
            fun = f"class {typedDictName}(typing.TypedDict):\n{content}"

        self.imports.add('typing')
        self.imports.update(listIter.imports)
        self.imports.add(fun)
        return typedDictName

    def __eq__(self, other):
        return isinstance(other, type(self)) \
               and self.funName == other.funName \
               and self.alternativeSyntax == other.alternativeSyntax \
               and super().__eq__(other)
