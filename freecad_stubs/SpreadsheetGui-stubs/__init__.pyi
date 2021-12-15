import FreeCADGui


# ViewProviderSpreadsheetPy.xml
class ViewProviderSpreadsheet(FreeCADGui.ViewProviderDocumentObject):
    """ViewProviderSheet class"""

    def getView(self):
        """Get access to the sheet view"""


# AppSpreadsheetGui.cpp
def open(arg1: str, arg2: str = None, /) -> None:
    """Possible exceptions: (Exception, RuntimeError)."""
