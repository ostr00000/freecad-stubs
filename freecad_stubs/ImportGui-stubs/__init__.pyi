import typing


class ReturnExportOptionsDict(typing.TypedDict):
    exportHidden: bool
    keepPlacement: bool
    legacy: bool



# AppImportGuiPy.cpp
def exportOptions(Name: str, /) -> ReturnExportOptionsDict:
    """
    exportOptions(string) -- Return the export options of a file type.
    Possible exceptions: (Exception).
    """


def ocaf(Name: str, /) -> None:
    """
    ocaf(string) -- Browse the ocaf structure.
    Possible exceptions: (Exception, IOError, FreeCAD.Base.FreeCADError).
    """


def open(name: str, docName: str = None, importHidden: bool = None, merge: bool = None, useLinkGroup: bool = None, mode: int = -1) -> object | typing.Any | None:
    """
    open(string) -- Open the file and create a new document.
    Possible exceptions: (Exception, IOError, FreeCAD.Base.FreeCADError).
    """


def insert(name: str, docName: str = None, importHidden: bool = None, merge: bool = None, useLinkGroup: bool = None, mode: int = -1) -> object | typing.Any | None:
    """
    insert(string,string) -- Insert the file into the given document.
    Possible exceptions: (Exception, IOError, FreeCAD.Base.FreeCADError).
    """


def export(obj, name: str, options: dict = None, exportHidden: bool = None, legacy: bool = None, keepPlacement: bool = None) -> None:
    """
    export(list,string) -- Export a list of objects into a single file.
    Possible exceptions: (Exception, RuntimeError, FreeCAD.Base.FreeCADError).
    """
