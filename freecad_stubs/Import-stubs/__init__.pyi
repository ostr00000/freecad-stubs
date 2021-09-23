import typing

import FreeCAD
import Part


# StepShapePy.xml
class StepShape(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    StepShape in Import
    This class gives a interface to retrieve TopoShapes out of an loaded STEP file of any kind.
    """

    def __init__(self, arg1: str, /):
        """
        StepShape in Import
        This class gives a interface to retrieve TopoShapes out of an loaded STEP file of any kind.
        """

    def read(self):
        """
        method read()
        Read a STEP file into memory and make it accessible
        """


# AppImportPy.cpp
def readDXF(arg1: str, arg2: str = None, arg3: int = None, arg4: str = None, /):
    """readDXF(filename,[document,ignore_errors]): Imports a DXF file into the given document. ignore_errors is True by default."""


@typing.overload
def writeDXFShape(arg1: list, arg2: str, arg3: int = None, arg4: object = None, arg5: str = None, /): ...


@typing.overload
def writeDXFShape(arg1: Part.Shape, arg2: str, arg3: int = None, arg4: object = None, arg5: str = None, /):
    """writeDXFShape([shape],filename [version,usePolyline,optionSource]): Exports Shape(s) to a DXF file."""


@typing.overload
def writeDXFObject(objects: list, filename_: str, version: int = None, usePolyline: object = None, optionSource: str = None, /): ...


@typing.overload
def writeDXFObject(objects: FreeCAD.DocumentObject, filename_: str, version: int = None, usePolyline: object = None, optionSource: str = None, /):
    """writeDXFObject([objects],filename [,version,usePolyline,optionSource]): Exports DocumentObject(s) to a DXF file."""


def open(name: str, docName: str = None, importHidden: object = None, merge: object = None, useLinkGroup: object = None, mode: int = None):
    """open(string) -- Open the file and create a new document."""


def insert(name: str, docName: str = None, importHidden: object = None, merge: object = None, useLinkGroup: object = None, mode: int = None):
    """insert(string,string) -- Insert the file into the given document."""


def export(obj: object, name: str, exportHidden: object = None, legacy: object = None, keepPlacement: object = None):
    """export(list,string) -- Export a list of objects into a single file."""
