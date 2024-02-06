import typing

import qtpy.QtCore
import qtpy.QtWidgets


# UiLoader.cpp
class UiLoader:
    """UiLoader to create widgets"""

    @typing.overload
    def load(self, string, /, QWidget_parent=None) -> qtpy.QtWidgets.QWidget | None: ...

    @typing.overload
    def load(self, QIODevice, /, QWidget_parent=None) -> qtpy.QtWidgets.QWidget | None:
        """
        load(string, QWidget parent=None) -> QWidget
        load(QIODevice, QWidget parent=None) -> QWidget
        Possible exceptions: (RuntimeError, TypeError).
        """

    def createWidget(self):
        """createWidget()"""

    def availableWidgets(self) -> list[str]:
        """availableWidgets()"""

    def clearPluginPaths(self) -> None:
        """clearPluginPaths()"""

    def pluginPaths(self) -> list[str]:
        """pluginPaths()"""

    def addPluginPath(self) -> None:
        """addPluginPath()"""

    def errorString(self) -> str:
        """errorString()"""

    def isLanguageChangeEnabled(self) -> bool:
        """isLanguageChangeEnabled()"""

    def setLanguageChangeEnabled(self) -> None:
        """setLanguageChangeEnabled()"""

    def setWorkingDirectory(self) -> None:
        """setWorkingDirectory()"""

    def workingDirectory(self) -> str:
        """workingDirectory()"""


# UiLoader.cpp

@typing.overload
def loadUi(args: tuple[str]) -> _OptWid_t: ...
@typing.overload
def loadUi(args: tuple[str, qtpy.QtCore.QObject | None]) -> _OptWid_t:
    """
    PySide lacks the "loadUiType" command, so we have to convert the ui file to py code in-memory first
    and then execute it in a special frame to retrieve the form_class.
    Possible exceptions: (Exception).
    """



class _UiGeneratedClass:
    def setupUi(self, widget: qtpy.QtWidgets.QWidget) -> None: ...
    def retranslateUi(self, widget: qtpy.QtWidgets.QWidget) -> None: ...

_LoadRes_t: typing.TypeAlias =  tuple[_UiGeneratedClass, qtpy.QtWidgets.QWidget]

def loadUiType(args: tuple[str]) -> _LoadRes_t | None:
    """
    Addition of "loadUi" to PySide.
    Possible exceptions: (Exception).
    """



_OptWid_t: typing.TypeAlias = qtpy.QtWidgets.QWidget | None

@typing.overload
def createCustomWidget(args: tuple[str]) -> _OptWid_t: ...
@typing.overload
def createCustomWidget(args: tuple[str, qtpy.QtWidgets.QWidget]) -> _OptWid_t: ...
@typing.overload
def createCustomWidget(args: tuple[str, qtpy.QtWidgets.QWidget, str]) -> _OptWid_t:
    """Create custom widgets."""
