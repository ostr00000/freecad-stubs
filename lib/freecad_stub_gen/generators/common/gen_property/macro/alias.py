from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


class PropertyTypeAlias:
    def __init__(self, name: str, alias: str, *dependency: PropertyTypeAlias):
        self.name = name
        self.alias = alias
        self.dependency = dependency

    def __repr__(self):
        return f'{self.name}: typing.TypeAlias = {self.alias}'

    def __str__(self):
        res = self.join(self.dependency)
        res += repr(self)
        return res

    @classmethod
    def join(cls, typeAliases: Iterable[PropertyTypeAlias]):
        return ''.join(f'{ta}\n' for ta in typeAliases)


class PropertyTypeVar(PropertyTypeAlias):
    def __init__(self, name: str, *dependency: PropertyTypeAlias):
        super().__init__(name, '', *dependency)

    def __repr__(self):
        return f'{self.name} = typing.TypeVar("{self.name}")'
