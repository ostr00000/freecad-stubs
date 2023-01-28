import typing

import FreeCAD
import Spreadsheet


# SheetPy.xml
class Sheet(FreeCAD.DocumentObject):
    """With this object you can manipulate spreadsheets"""

    def __init__(self):
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

    def clear(self, strAddress: str, all: bool = 1, /):
        """
        Clear a cell
        Possible exceptions: (ValueError).
        """

    def clearAll(self):
        """Clear all cells in the spreadsheet"""

    def exportFile(self, filename: str, delimiter: str = '\t', quoteChar: str = '"', escapeChar: str = '\\', /) -> bool:
        """Export file from spreadsheet"""

    def get(self, address: str, address2: str = None, /) -> tuple[FreeCAD.Property, ...] | FreeCAD.Property:
        """Get evaluated cell contents"""

    def getAlias(self, strAddress: str, /) -> str:
        """
        Get alias for cell address
        Possible exceptions: (ValueError).
        """

    def getAlignment(self, strAddress: str, /) -> typing.Any | None:
        """
        Get alignment of the cell
        Possible exceptions: (ValueError).
        """

    def getBackground(self, strAddress: str, /) -> tuple[float, float, float, float] | None:
        """
        Get background color of the cell
        Possible exceptions: (ValueError).
        """

    def getCellFromAlias(self, alias: str, /) -> str:
        """
        Get cell address given an alias
        Possible exceptions: (ValueError).
        """

    def getColumnWidth(self, columnStr: str, /) -> int:
        """
        Get given spreadsheet column width
        Possible exceptions: (ValueError).
        """

    def getContents(self, strAddress: str, /) -> str:
        """
        Get cell contents
        Possible exceptions: (ValueError).
        """

    def getDisplayUnit(self, strAddress: str, /) -> str:
        """
        Get display unit for cell
        Possible exceptions: (ValueError).
        """

    def getForeground(self, strAddress: str, /) -> tuple[float, float, float, float] | None:
        """
        Get foreground color of the cell
        Possible exceptions: (ValueError).
        """

    def getNonEmptyCells(self) -> list[str]:
        """
        getNonEmptyCells()

        Get a list of the names of all cells with data in them.
        """

    def getNonEmptyRange(self) -> tuple[str, str]:
        """
        getNonEmptyRange()

        Get a the total range of the used cells in a sheet, as a pair of cell addresses
        representing the lowest row and column that contain data, and the highest row and
        column that contain data (inclusive). Note that the actual first and last cell
        of the block do not necessarily contain anything.
        """

    def getRowHeight(self, rowStr: str, /) -> int:
        """
        Get given spreadsheet row height
        Possible exceptions: (ValueError).
        """

    def getStyle(self, strAddress: str, /) -> typing.Any | None:
        """
        Get style of the cell
        Possible exceptions: (ValueError).
        """

    def getUsedCells(self) -> list[str]:
        """
        getUsedCells()

        Get a list of the names of all cells that are marked as used. These cells may
        or may not have a non-empty string content.
        """

    def getUsedRange(self) -> tuple[str, str]:
        """
        getUsedRange()

        Get a the total range of the used cells in a sheet, as a pair of strings
        representing the lowest row and column that are used, and the highest row and
        column that are used (inclusive). Note that the actual first and last cell
        of the block are not necessarily used.
        """

    def importFile(self, filename: str, delimiter: str = '\t', quoteChar: str = '"', escapeChar: str = '\\', /) -> bool:
        """Import file into spreadsheet"""

    def insertColumns(self, column: str, count: int, /):
        """Insert a given number of columns into the spreadsheet."""

    def insertRows(self, row: str, count: int, /):
        """Insert a given number of rows into the spreadsheet."""

    def mergeCells(self, range: str, /):
        """Merge given cell area into one cell"""

    def recomputeCells(self, address: str, address2: str = None, /):
        """
        recomputeCells(from, to=None)

        Manually recompute cells in the given range with the given order without
        following dependency order.
        """

    def removeColumns(self, column: str, count: int, /):
        """Remove a given number of columns from the spreadsheet."""

    def removeRows(self, row: str, count: int, /):
        """Remove a given number of rows from the spreadsheet."""

    def set(self, address: str, contents: str, /):
        """
        Set data into a cell
        Possible exceptions: (ValueError).
        """

    def setAlias(self, strAddress: str, value, /):
        """
        Set alias for cell address
        Possible exceptions: (ValueError).
        """

    def setAlignment(self, cell: str, value, options: str = 'replace', /):
        """
        Set alignment of the cell
        Possible exceptions: (TypeError, ValueError).
        """

    def setBackground(self, strAddress: str, value, /):
        """
        Set background color of the cell
        Possible exceptions: (TypeError, ValueError).
        """

    def setColumnWidth(self, columnStr: str, width: int, /):
        """
        Set given spreadsheet column to given width
        Possible exceptions: (ValueError).
        """

    def setDisplayUnit(self, cell: str, value: str, /):
        """
        Set display unit for cell
        Possible exceptions: (ValueError).
        """

    def setForeground(self, range: str, value, /):
        """
        Set foreground color of the cell
        Possible exceptions: (TypeError, ValueError).
        """

    def setRowHeight(self, rowStr: str, height: int, /):
        """
        Set given spreadsheet row to given height
        Possible exceptions: (ValueError).
        """

    def setStyle(self, cell: str, value, options: str = 'replace', /):
        """
        Set style of the cell
        Possible exceptions: (TypeError, ValueError).
        """

    def splitCell(self, strAddress: str, /):
        """
        Split a previously merged cell
        Possible exceptions: (ValueError).
        """

    def touchCells(self, address: str, address2: str = None, /):
        """touchCells(from, to=None): touch cells in the given range"""


# PropertyRowHeightsPy.xml
class PropertyRowHeights(FreeCAD.Persistence):
    """Internal spreadsheet object"""

    def __init__(self):
        """Internal spreadsheet object"""


# PropertyColumnWidthsPy.xml
class PropertyColumnWidths(FreeCAD.Persistence):
    """Internal spreadsheet object"""

    def __init__(self):
        """Internal spreadsheet object"""


# PropertySheetPy.xml
class PropertySheet(FreeCAD.Persistence):
    """Internal spreadsheet object"""

    def __init__(self):
        """Internal spreadsheet object"""


# SpreadsheetView.cpp
class SheetViewPy:
    """Python binding class for the Sheet view class"""

    def selectedRanges(self) -> list[str]:
        """
        selectedRanges(): Get a list of all selected ranges
        Possible exceptions: (Exception).
        """

    def selectedCells(self) -> list[str]:
        """
        selectedCells(): Get a list of all selected cells
        Possible exceptions: (Exception).
        """

    @typing.overload
    def select(self, cell: str, flags: int = 0, /) -> None: ...

    @typing.overload
    def select(self, topLeft: str, bottomRight: str, flags: int = 0, /) -> None:
        """
        select(cell,flags): Select (or deselect) the given cell, applying QItemSelectionModel.SelectionFlags
        select(topLeft,bottomRight,flags): Select (or deselect) the given range, applying QItemSelectionModel.SelectionFlags
        """

    def currentIndex(self) -> str:
        """
        currentIndex(): Get the current index
        Possible exceptions: (Exception).
        """

    def setCurrentIndex(self, cell: str, /) -> None:
        """setCurrentIndex(cell): Set the current index to the named cell (e.g. 'A1')"""

    def getSheet(self) -> Spreadsheet.Sheet:
        """
        getSheet()
        Possible exceptions: (Exception).
        """

    def cast_to_base(self):
        """cast_to_base() cast to MDIView class"""
