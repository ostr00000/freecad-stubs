import FreeCADGui
import SpreadsheetGui


# ViewProviderSpreadsheetPy.xml
class ViewProviderSpreadsheet(FreeCADGui.ViewProviderDocumentObject):
    """ViewProviderSheet class"""

    def getView(self) -> SpreadsheetGui.SheetView:
        """Get access to the sheet view"""


# AppSpreadsheetGui.cpp
def open(Name: str, DocName: str = None, /) -> None:
    """Possible exceptions: (Exception, RuntimeError)."""
