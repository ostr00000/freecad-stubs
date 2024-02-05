import typing

import qtpy.QtCore
import qtpy.QtWidgets



_OptWid_t: typing.TypeAlias = qtpy.QtWidgets.QWidget | None

@typing.overload
def createCustomWidget(args: tuple[str]) -> _OptWid_t: ...
@typing.overload
def createCustomWidget(args: tuple[str, qtpy.QtWidgets.QWidget]) -> _OptWid_t: ...
@typing.overload
def createCustomWidget(args: tuple[str, qtpy.QtWidgets.QWidget, str]) -> _OptWid_t: ...

@typing.overload
def loadUi(args: tuple[str]) -> _OptWid_t: ...
@typing.overload
def loadUi(args: tuple[str, qtpy.QtCore.QObject | None]) -> _OptWid_t: ...

class _UiGeneratedClass:
    def setupUi(self, widget: qtpy.QtWidgets.QWidget) -> None: ...
    def retranslateUi(self, widget: qtpy.QtWidgets.QWidget) -> None: ...

_LoadRes_t: typing.TypeAlias =  tuple[_UiGeneratedClass, qtpy.QtWidgets.QWidget]

def loadUiType(args: tuple[str]) -> _LoadRes_t | None: ...
