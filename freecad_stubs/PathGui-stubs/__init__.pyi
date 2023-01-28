# AppPathGuiPy.cpp
def open(Name: str, /) -> None:
    """
    open(filename): Opens a GCode file as a new document
    Possible exceptions: (Exception, RuntimeError).
    """


def insert(Name: str, DocName: str = None, /) -> None:
    """
    insert(filename,docname): Imports a given GCode file into the given document
    Possible exceptions: (Exception, RuntimeError).
    """


def export(object, Name: str, /) -> None:
    """
    export(objectslist,filename): Exports a given list of Path objects to a GCode file
    Possible exceptions: (Exception, RuntimeError).
    """
