import typing

import FreeCAD
import Part


# AppRaytracingPy.cpp
def writeProjectFile(arg1: typing.Sequence[str], /):
    """&Module::writeProjectFile"""


def getPartAsPovray(arg1: str, arg2: Part.TopoShape, arg3: float = None, arg4: float = None, arg5: float = None, /):
    """&Module::getPartAsPovray"""


def getPartAsLux(arg1: str, arg2: Part.TopoShape, arg3: float = None, arg4: float = None, arg5: float = None, /):
    """&Module::getPartAsLux"""


def writePartFile(arg1: str, arg2: str, arg3: Part.TopoShape, /):
    """&Module::writePartFile"""


def writeDataFile(arg1: str, arg2: str, arg3: FreeCAD.ComplexGeoData, /):
    """&Module::writeDataFile"""


def writePartFileCSV(arg1: Part.TopoShape, arg2: str, arg3: float, arg4: float, /):
    """&Module::writePartFileCSV"""


def writeCameraFile(arg1: str, arg2: tuple, arg3: tuple, arg4: tuple, arg5: tuple, /):
    """&Module::writeCameraFile"""


def copyResource(arg1: str, arg2: str, /):
    """&Module::copyResource"""


# AppRaytracingGuiPy.cpp
def open(arg1: str, arg2: str = None, /):
    """open(string) -- Create a new text document and load the file into the document."""


def insert(string: str, string1: str = None, /):
    """insert(string,string) -- Create a new text document and load the file into the document."""


def povViewCamera():
    """string povViewCamera() -- returns the povray camera definition of the active 3D view."""


def luxViewCamera():
    """string luxViewCamera() -- returns the luxrender camera definition of the active 3D view."""
