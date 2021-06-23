import typing

import FreeCAD
import Part


# AppRaytracingPy.cpp
def writeProjectFile(arg1: typing.Sequence[str], /): ...


def getPartAsPovray(arg1: str, arg2: Part.TopoShape, arg3: float = None, arg4: float = None, arg5: float = None, /): ...


def getPartAsLux(arg1: str, arg2: Part.TopoShape, arg3: float = None, arg4: float = None, arg5: float = None, /): ...


def writePartFile(arg1: str, arg2: str, arg3: Part.TopoShape, /): ...


def writeDataFile(arg1: str, arg2: str, arg3: FreeCAD.ComplexGeoData, /): ...


def writePartFileCSV(arg1: Part.TopoShape, arg2: str, arg3: float, arg4: float, /): ...


def writeCameraFile(arg1: str, arg2: tuple, arg3: tuple, arg4: tuple, arg5: tuple, /): ...


def copyResource(arg1: str, arg2: str, /): ...
