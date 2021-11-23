import typing

import FreeCAD
import Part as PartModule


# AppRaytracingPy.cpp
def writeProjectFile(arg1: typing.Sequence[str], /) -> None: ...


def getPartAsPovray(arg1: str, arg2: PartModule.Shape, arg3: float = None, arg4: float = None, arg5: float = None, /) -> str: ...


def getPartAsLux(arg1: str, arg2: PartModule.Shape, arg3: float = None, arg4: float = None, arg5: float = None, /) -> str: ...


def writePartFile(arg1: str, arg2: str, arg3: PartModule.Shape, /) -> None: ...


def writeDataFile(arg1: str, arg2: str, arg3: FreeCAD.ComplexGeoData, /) -> None: ...


def writePartFileCSV(arg1: PartModule.Shape, arg2: str, arg3: float, arg4: float, /) -> None: ...


def writeCameraFile(arg1: str, arg2: tuple, arg3: tuple, arg4: tuple, arg5: tuple, /) -> None: ...


def copyResource(arg1: str, arg2: str, /) -> None: ...
