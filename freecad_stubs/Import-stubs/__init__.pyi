import typing

import FreeCAD
import Part as PartModule


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
		
        Possible exceptions: (TypeError).
        """

    def read(self):
        """
        method read()
        Read a STEP file into memory and make it accessible
			  
        Possible exceptions: (NotImplementedError).
        """


# AppImportPy.cpp
def readDXF(arg1: str, arg2: str = None, arg3: int = None, arg4: str = None, /) -> None:
    """
    readDXF(filename,[document,ignore_errors]): Imports a DXF file into the given document. ignore_errors is True by default.
    Possible exceptions: (Exception, RuntimeError).
    """


@typing.overload
def writeDXFShape(arg1: list, arg2: str, arg3: int = None, arg4=None, arg5: str = None, /) -> None: ...


@typing.overload
def writeDXFShape(arg1: PartModule.Shape, arg2: str, arg3: int = None, arg4=None, arg5: str = None, /) -> None:
    """
    writeDXFShape([shape],filename [version,usePolyline,optionSource]): Exports Shape(s) to a DXF file.
    Possible exceptions: (RuntimeError, TypeError).
    """


@typing.overload
def writeDXFObject(objects: list, filename_: str, version: int = None, usePolyline=None, optionSource: str = None, /) -> None: ...


@typing.overload
def writeDXFObject(objects: FreeCAD.DocumentObject, filename_: str, version: int = None, usePolyline=None, optionSource: str = None, /) -> None:
    """
    writeDXFObject([objects],filename [,version,usePolyline,optionSource]): Exports DocumentObject(s) to a DXF file.
    Possible exceptions: (RuntimeError, TypeError).
    """


def open(name: str, docName: str = None, importHidden=None, merge=None, useLinkGroup=None, mode: int = None) -> list[tuple[typing.Any, FreeCAD.PropertyColorList]] | None:
    """
    open(string) -- Open the file and create a new document.
    Possible exceptions: (Exception, IOError, FreeCAD.Base.FreeCADError).
    """


def insert(name: str, docName: str = None, importHidden=None, merge=None, useLinkGroup=None, mode: int = None) -> list[tuple[typing.Any, FreeCAD.PropertyColorList]] | None:
    """
    insert(string,string) -- Insert the file into the given document.
    Possible exceptions: (Exception, IOError, FreeCAD.Base.FreeCADError).
    """


def export(obj, name: str, exportHidden=None, legacy=None, keepPlacement=None) -> None:
    """
    export(list,string) -- Export a list of objects into a single file.
    Possible exceptions: (Exception, FreeCAD.Base.FreeCADError).
    """
