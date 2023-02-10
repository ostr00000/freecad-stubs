from __future__ import annotations

import keyword
from abc import ABC
from collections.abc import Sized, Iterable
from functools import cached_property
from typing import TypeVar, Generator, Protocol, Iterator

from freecad_stub_gen.generators.common.names import getModuleName, useAliasedModule
from freecad_stub_gen.util import indent, OrderedStrSet, OrderedSet

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


class SizedIterable(Sized, Iterable, Protocol):
    pass


class WithImports:
    @cached_property
    def imports(self):
        return OrderedStrSet()


class ArgumentsIter(WithImports, SizedIterable, ABC):
    def __iter__(self) -> Iterator[str]:
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


class UnionArguments(ArgumentsIter, OrderedSet[str], SizedIterable):
    def __str__(self):
        values = list(self)
        if 'None' in values:
            values.remove('None')
            values.append('None')

        return ' | '.join(values)

    def add(self, item: RetType):
        val = str(item)
        super().add(val)
        match item:
            case UnionArguments():
                self.imports.update(item.imports)
            case EmptyType.value:
                self.imports.add('typing')


class TupleArgument(ArgumentsIter, list, SizedIterable):
    def __init__(self, gen: Generator[T, None, bool | None]):
        super().__init__()
        try:
            while True:
                self.append(next(gen))
        except StopIteration as st:
            self.repeated = st.value is True and len(set(self)) == 1

    def __str__(self):
        if self.repeated:
            # use iter instead of index [0] to map module
            return f'tuple[{next(iter(self))}, ...]'
        elif self:
            return f'tuple[{", ".join(self)}]'
        return 'tuple'

    def __eq__(self, other):
        return isinstance(other, type(self)) \
            and self.repeated == other.repeated \
            and super().__eq__(other)


RetType = UnionArguments | EmptyType | str


class InvalidReturnType(ValueError):
    pass


class DictArgument(WithImports):
    def __init__(self):
        self.keys = UnionArguments()
        self.values = UnionArguments()

    def add(self, key: RetType, value: RetType):
        self.keys.add(key)
        self.values.add(value)

    def __bool__(self):
        return bool(self.keys or self.values)

    def __str__(self):
        if not self:
            return 'dict'

        ret = f'dict[{self.keys}, {self.values}]'
        self.imports.update(self.keys.imports)
        self.imports.update(self.values.imports)
        return ret


class ListIter(ArgumentsIter, list, SizedIterable):
    pass


class TypedDictGen(WithImports):
    def __init__(self, funName: str):
        super().__init__()
        self.funName = funName
        self.alternativeSyntax = False
        self._data: dict[str, RetType] = {}

    def add(self, key: str, value: RetType):
        if not key.isidentifier() or keyword.iskeyword(key):
            self.alternativeSyntax |= True
        self._data[key] = value

    def __bool__(self):
        return bool(self._data)

    def __str__(self):
        typedDictName = f'Return{self.funName[0].upper() + self.funName[1:]}Dict'
        listIter = ListIter(self._data.values())

        if self.alternativeSyntax:  # TODO P4 better format
            content = ', '.join(f"'{k}': {v}" for k, v in zip(self._data.keys(), listIter))
            fun = f"{typedDictName} = typing.TypedDict('{typedDictName}', {{{content}}})"

        else:
            lines = [f'{k}: {v}' for k, v in zip(self._data.keys(), listIter)]
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
