import FreeCAD
import Part as PartModule


# AppRaytracingPy.cpp
def writeProjectFile(fromPython: tuple[str] = ('FreeCAD.pov',), /) -> None:
    """Possible exceptions: (Exception)."""


def getProjectFile() -> str: ...


def getPartAsPovray(PartName: str, ShapeObject: PartModule.Shape, r: float = 0.5, g: float = 0.5, b: float = 0.5, /) -> str:
    """Possible exceptions: (Exception)."""


def getPartAsLux(PartName: str, ShapeObject: PartModule.Shape, r: float = 0.5, g: float = 0.5, b: float = 0.5, /) -> str:
    """Possible exceptions: (Exception)."""


def writePartFile(FileName: str, PartName: str, ShapeObject: PartModule.Shape, /) -> None:
    """Possible exceptions: (Exception)."""


def writeDataFile(FileName: str, PartName: str, dataObject: FreeCAD.ComplexGeoData, /) -> None:
    """Possible exceptions: (Exception)."""


def writePartFileCSV(ShapeObject: PartModule.Shape, FileName: str, Acur: float, Length: float, /) -> None:
    """Possible exceptions: (Exception)."""


def writeCameraFile(FileName: str, arg2: tuple, arg3: tuple, arg4: tuple, arg5: tuple, /) -> None:
    """Possible exceptions: (Exception, ValueError)."""


def copyResource(FileName: str, DestDir: str, /) -> None:
    """Possible exceptions: (Exception)."""
