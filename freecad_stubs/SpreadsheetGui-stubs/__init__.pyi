import FreeCAD


# SpreadsheetViewPy.xml
class SheetView(FreeCAD.PyObjectBase):
    """SpreadsheetView object"""

    def getSheet(self):
        """returns the sheet being displayed"""


# AppSpreadsheetGui.cpp
def open(arg1: str, arg2: str = None, /): ...
