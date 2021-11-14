import FreeCAD
import Spreadsheet


# SheetPy.xml
class Sheet(FreeCAD.DocumentObject):
    """With this object you can manipulate spreadsheets"""

    @property
    def cells(self) -> Spreadsheet.Sheet:
        """
        [Prop_Hidden] Property won't appear in the editor.
        Property group: Spreadsheet.
        Property TypeId: Spreadsheet::PropertySheet.
        Cell contents.
        """

    @cells.setter
    def cells(self, value: Spreadsheet.Sheet): ...

    @property
    def columnWidths(self) -> Spreadsheet.PropertyColumnWidths:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Hidden] Property won't appear in the editor.
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Spreadsheet.
        Property TypeId: Spreadsheet::PropertyColumnWidths.
        Column widths.
        """

    @property
    def rowHeights(self) -> Spreadsheet.PropertyRowHeights:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Hidden] Property won't appear in the editor.
        Property group: Spreadsheet.
        Property TypeId: Spreadsheet::PropertyRowHeights.
        Row heights.
        """

    @property
    def rowHeights(self) -> Spreadsheet.PropertyRowHeights:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Hidden] Property won't appear in the editor.
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Spreadsheet.
        Property TypeId: Spreadsheet::PropertyRowHeights.
        Row heights.
        """

    def clear(self, arg1: str, arg2: bool = None, /):
        """Clear a cell"""

    def clearAll(self):
        """Clear all cells in the spreadsheet"""

    def exportFile(self, arg1: str, arg2: str = None, arg3: str = None, arg4: str = None, /) -> bool:
        """Export file from spreadsheet"""

    def get(self, arg1: str, arg2: str = None, /) -> tuple[FreeCAD.Property] | FreeCAD.Property:
        """Get evaluated cell contents"""

    def getAlias(self, arg1: str, /) -> str | None:
        """Get alias for cell address"""

    def getAlignment(self, arg1: str, /) -> object | None:
        """Get alignment of the cell"""

    def getBackground(self, arg1: str, /) -> tuple[float, float, float, float] | None:
        """Get background color of the cell"""

    def getCellFromAlias(self, arg1: str, /) -> str | None:
        """Get cell address given an alias"""

    def getColumnWidth(self, arg1: str, /) -> int:
        """Get given spreadsheet column width"""

    def getContents(self, arg1: str, /) -> str:
        """Get cell contents"""

    def getDisplayUnit(self, arg1: str, /) -> str:
        """Get display unit for cell"""

    def getForeground(self, arg1: str, /) -> tuple[float, float, float, float] | None:
        """Get foreground color of the cell"""

    def getRowHeight(self, arg1: str, /) -> int:
        """Get given spreadsheet row height"""

    def getStyle(self, arg1: str, /) -> object | None:
        """Get style of the cell"""

    def importFile(self, arg1: str, arg2: str = None, arg3: str = None, arg4: str = None, /) -> bool:
        """Import file into spreadsheet"""

    def insertColumns(self, arg1: str, arg2: int, /):
        """Insert a given number of columns into the spreadsheet."""

    def insertRows(self, arg1: str, arg2: int, /):
        """Insert a given number of rows into the spreadsheet."""

    def mergeCells(self, arg1: str, /):
        """Merge given cell area into one cell"""

    def recomputeCells(self, from_: str, to: str = None, /):
        """
        recomputeCells(from, to=None)

        Manually recompute cells in the given range with the given order without
        following dependency order.
        """

    def removeColumns(self, arg1: str, arg2: int, /):
        """Remove a given number of columns from the spreadsheet."""

    def removeRows(self, arg1: str, arg2: int, /):
        """Remove a given number of rows from the spreadsheet."""

    def set(self, arg1: str, arg2: str, /):
        """Set data into a cell"""

    def setAlias(self, arg1: str, arg2, /):
        """Set alias for cell address"""

    def setAlignment(self, arg1: str, arg2, arg3: str = None, /):
        """Set alignment of the cell"""

    def setBackground(self, arg1: str, arg2, /):
        """Set background color of the cell"""

    def setColumnWidth(self, arg1: str, arg2: int, /):
        """Set given spreadsheet column to given width"""

    def setDisplayUnit(self, arg1: str, arg2: str, /):
        """Set display unit for cell"""

    def setForeground(self, arg1: str, arg2, /):
        """Set foreground color of the cell"""

    def setRowHeight(self, arg1: str, arg2: int, /):
        """Set given spreadsheet row to given height"""

    def setStyle(self, arg1: str, arg2, arg3: str = None, /):
        """Set style of the cell"""

    def splitCell(self, arg1: str, /):
        """Split a previously merged cell"""

    def touchCells(self, from_: str, to: str = None, /):
        """touchCells(from, to=None): touch cells in the given range"""


# PropertyRowHeightsPy.xml
class PropertyRowHeights(FreeCAD.Persistence):
    """Internal spreadsheet object"""


# PropertyColumnWidthsPy.xml
class PropertyColumnWidths(FreeCAD.Persistence):
    """Internal spreadsheet object"""


# PropertySheetPy.xml
class PropertySheet(FreeCAD.Persistence):
    """Internal spreadsheet object"""


# SpreadsheetView.cpp
class SheetViewPy:
    """Python binding class for the Sheet view class"""

    def getSheet(self) -> Spreadsheet.Sheet:
        """getSheet()"""
