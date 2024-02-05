"""
Based on stubs in:
https://github.com/python-qt-tools/PyQt5-stubs/blob/master/PyQt5-stubs/QtCore.pyi
"""

import typing

from qtpy.QtCore import QMetaObject, QObject
from qtpy.QtCore import (
    Signal as BaseSignal,  # pyright: ignore [reportPrivateImportUsage]
)
from qtpy.QtCore import (
    SignalInstance as BaseSignalInstance,  # pyright: ignore [reportPrivateImportUsage]
)

_Fun_t = typing.TypeVar('_Fun_t', bound=typing.Callable)

class Signal(BaseSignal, typing.Generic[_Fun_t]):
    signatures: tuple[str, ...]

    def __init__(self, *types: typing.Any, name: str = ...) -> None: ...
    @typing.overload
    def __get__(self, instance: None, owner: type[QObject]) -> Signal[_Fun_t]: ...
    @typing.overload
    def __get__(
        self, instance: QObject, owner: type[QObject]
    ) -> SignalInstance[_Fun_t]: ...

class SignalInstance(BaseSignalInstance, typing.Generic[_Fun_t]):
    signal: str

    def __getitem__(self, key: object) -> SignalInstance: ...
    @typing.overload
    def connect(self, slot: _Fun_t) -> QMetaObject.Connection: ...
    @typing.overload
    def connect(  # pyright: ignore [reportIncompatibleMethodOverride]
        self, slot: SignalInstance
    ) -> QMetaObject.Connection: ...
    @typing.overload
    def disconnect(self) -> None: ...
    @typing.overload
    def disconnect(  # pyright: ignore [reportIncompatibleMethodOverride]
        self, slot: _Fun_t | SignalInstance[typing.Any] | QMetaObject.Connection
    ) -> None: ...
    def emit(self, *args: typing.Any) -> None: ...
