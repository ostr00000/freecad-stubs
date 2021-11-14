import typing

import FreeCAD
import FreeCADGui
import Spreadsheet


# ViewProviderSpreadsheetPy.xml
class ViewProviderSpreadsheet(FreeCADGui.ViewProviderDocumentObject):
    """ViewProviderSheet class"""

    def getView(self):
        """Get access to the sheet view"""

    @typing.overload
    def select(self, index: str, flags: int, /): ...

    @typing.overload
    def select(self, topLeft: str, bottomRight: str, flags: int, /):
        """
        select(index, flags): Select the specified cell using the given QItemSelectionModel.SelectionFlag set
        select(topLeft, bottomRight, flags): Select the specified range using the given QItemSelectionModel.SelectionFlag set
        """

    def setCurrentIndex(self, arg1: str, /):
        """Set the current active cell"""


# SpreadsheetViewPy.xml
class SpreadsheetView(FreeCAD.PyObjectBase):
    """SpreadsheetView object"""

    def getSheet(self) -> Spreadsheet.Sheet:
        """returns the sheet being displayed"""


# AppSpreadsheetGui.cpp
def open(arg1: str, arg2: str = None, /) -> None: ...
