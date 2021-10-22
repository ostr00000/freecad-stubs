import FreeCAD
import Spreadsheet


# SpreadsheetViewPy.xml
class SpreadsheetView(FreeCAD.PyObjectBase):
    """SpreadsheetView object"""

    def getSheet(self) -> Spreadsheet.Sheet:
        """returns the sheet being displayed"""


# AppSpreadsheetGui.cpp
def open(arg1: str, arg2: str = None, /) -> None: ...
