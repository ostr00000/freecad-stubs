# AppPathGuiPy.cpp
def open(filename: str, /) -> None:
    """open(filename): Opens a GCode file as a new document"""


def insert(filename: str, docname: str = None, /) -> None:
    """insert(filename,docname): Imports a given GCode file into the given document"""


def export(objectslist, filename: str, /) -> None:
    """export(objectslist,filename): Exports a given list of Path objects to a GCode file"""
