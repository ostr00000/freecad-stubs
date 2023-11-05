"""
Based on stubs in:
https://github.com/python-qt-tools/PyQt5-stubs/blob/master/PyQt5-stubs/QtCore.pyi
"""
from __future__ import annotations

import typing

from PyQt5.QtCore import QMetaObject, QObject

Fun_t = typing.TypeVar('Fun_t', bound=typing.Callable)


class pyqtSignal(typing.Generic[Fun_t]):
    signatures: tuple[str, ...]

    def __init__(self, *types: typing.Any, name: str = ...) -> None:
        ...

    @typing.overload
    def __get__(self, instance: None, owner: type[QObject]) -> pyqtSignal[Fun_t]:
        ...

    @typing.overload
    def __get__(
        self, instance: QObject, owner: type[QObject]
    ) -> pyqtBoundSignal[Fun_t]:
        ...


class pyqtBoundSignal(typing.Generic[Fun_t]):
    signal: str

    def __getitem__(self, key: object) -> 'pyqtBoundSignal':
        ...

    @typing.overload
    def connect(self, slot: Fun_t) -> 'QMetaObject.Connection':
        ...

    @typing.overload
    def connect(self, slot: pyqtBoundSignal) -> 'QMetaObject.Connection':
        ...

    @typing.overload
    def disconnect(self) -> None:
        ...

    @typing.overload
    def disconnect(
        self, slot: Fun_t | pyqtBoundSignal[typing.Any] | QMetaObject.Connection
    ) -> None:
        ...

    def emit(self, *args: typing.Any) -> None:
        ...
