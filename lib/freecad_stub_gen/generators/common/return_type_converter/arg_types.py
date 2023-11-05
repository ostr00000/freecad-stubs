from __future__ import annotations

import keyword
from abc import ABC
from collections.abc import Iterable, Sized
from functools import cached_property
from typing import Generator, Iterator, Protocol, TypeAlias, TypeVar

from ordered_set import OrderedSet

from freecad_stub_gen.generators.common.names import getModuleName, useAliasedModule
from freecad_stub_gen.python_code import indent

T = TypeVar('T')


class AnyValueType:
    @property
    def value(self):
        return self

    def __eq__(self, other):
        return other is AnyValue or other == 'typing.Any'

    def __hash__(self):
        return 1

    def __str__(self):
        return 'typing.Any'


AnyValue = AnyValueType()


class ComplexArgumentBase(ABC):
    """Base class for generating complex arguments."""

    @cached_property
    def imports(self):
        return OrderedSet[str]()

    def getPythonSignature(self) -> str:
        raise NotImplementedError

    def __str__(self):
        return self.getPythonSignature()


class SizedIterable(Sized, Iterable['RetType'], Protocol):
    """Protocol class for `SignatureWithImports`.

    When adding `SignatureWithImports` to base classes,
    this class must also be added to properly resolve MRO.
    Correct order:
        - SignatureWithImports,
        - class implementing this protocol (__len__ + __iter__),
        - SizedIterable.
    """


class CollectImportsArgument(ComplexArgumentBase, SizedIterable, ABC):
    """Mixin class for arguments that additionally collect imports."""

    def __iter__(self) -> Iterator[str]:
        for argType in super().__iter__():
            match argType:
                case str() if '[' not in argType and getModuleName(argType):
                    argType = useAliasedModule(argType, self.imports)
                case AnyValueType() if len(self) > 1:
                    self.imports.add('typing')
                case UnionArgument() as ua:
                    self.imports.update(ua.imports)
            yield str(argType)

    def __len__(self):
        return super().__len__()


class UnionArgument(CollectImportsArgument, OrderedSet['RetType'], SizedIterable):
    """Represents `typing.Union` argument."""

    def getPythonSignature(self) -> str:
        values = list(iter(self))
        if 'None' in values:
            values.remove('None')
            values.append('None')

        return ' | '.join(values)

    def add(self, item: RetType):
        val = str(item)
        super().add(val)
        match item:
            case UnionArgument():
                self.imports.update(item.imports)
            case AnyValueType.value:
                self.imports.add('typing')


RetType: TypeAlias = UnionArgument | AnyValueType | str


class TupleArgument(CollectImportsArgument, list[RetType], SizedIterable):
    """Represents `tuple` argument."""

    repeated: bool

    def __init__(self, gen: Generator[RetType, None, bool | None]):
        super().__init__()
        try:
            while True:
                self.append(next(gen))
        except StopIteration as st:
            self.repeated = st.value is True and len(set(self)) == 1

    def getPythonSignature(self) -> str:
        if self.repeated:
            # use iter instead of index [0] to map module
            return f'tuple[{next(iter(self))}, ...]'

        if self:
            return f'tuple[{", ".join(iter(self))}]'

        return 'tuple'

    def __eq__(self, other):
        return (
            isinstance(other, type(self))
            and self.repeated == other.repeated
            and super().__eq__(other)
        )


class InvalidReturnType(ValueError):
    pass


class DictArgument(ComplexArgumentBase):
    """Represents `dict` argument."""

    def __init__(self):
        self.keys = UnionArgument()
        self.values = UnionArgument()

    def add(self, key: RetType, value: RetType):
        self.keys.add(key)
        self.values.add(value)

    def __bool__(self):
        return bool(self.keys or self.values)

    def getPythonSignature(self) -> str:
        if not self:
            return 'dict'

        ret = f'dict[{self.keys}, {self.values}]'
        self.imports.update(self.keys.imports)
        self.imports.update(self.values.imports)
        return ret


class _ListIter(CollectImportsArgument, list[RetType], SizedIterable):
    """Stores arguments sequentially.

    Note that argument for `list` is `UnionArgument`,
    because we want to skip duplicated elements.
    """


class TypedDictGen(ComplexArgumentBase):
    """Generates `TypedDict` for provided types."""

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

    def getPythonSignature(self) -> str:
        listIter = _ListIter(self._data.values())

        if self.alternativeSyntax:
            zipPattern = "'{k}': {v}"
            joinPattern = ',\n'
        else:
            zipPattern = '{k}: {v}'
            joinPattern = '\n'
        lines = (
            zipPattern.format(k=k, v=v) for k, v in zip(self._data.keys(), listIter)
        )
        content = indent(joinPattern.join(lines))

        typedDictName = f'Return{self.funName[0].upper() + self.funName[1:]}Dict'
        if self.alternativeSyntax:
            fun = f"{typedDictName} = typing.TypedDict('{typedDictName}', {{\n{content},\n}})"
        else:
            fun = f"class {typedDictName}(typing.TypedDict):\n{content}"

        self.imports.add('typing')
        self.imports.update(listIter.imports)
        self.imports.add(fun)
        return typedDictName

    def __eq__(self, other):
        return (
            isinstance(other, type(self))
            and self.funName == other.funName
            and self.alternativeSyntax == other.alternativeSyntax
            and super().__eq__(other)
        )
