import FreeCAD
import Part as PartModule


# AppRaytracingPy.cpp
def writeProjectFile(arg1: tuple[str], /) -> None:
    """Possible exceptions: (Exception)."""


def getProjectFile() -> str: ...


def getPartAsPovray(arg1: str, arg2: PartModule.Shape, arg3: float = None, arg4: float = None, arg5: float = None, /) -> str:
    """Possible exceptions: (Exception)."""


def getPartAsLux(arg1: str, arg2: PartModule.Shape, arg3: float = None, arg4: float = None, arg5: float = None, /) -> str:
    """Possible exceptions: (Exception)."""


def writePartFile(arg1: str, arg2: str, arg3: PartModule.Shape, /) -> None:
    """Possible exceptions: (Exception)."""


def writeDataFile(arg1: str, arg2: str, arg3: FreeCAD.ComplexGeoData, /) -> None:
    """Possible exceptions: (Exception)."""


def writePartFileCSV(arg1: PartModule.Shape, arg2: str, arg3: float, arg4: float, /) -> None:
    """Possible exceptions: (Exception)."""


def writeCameraFile(arg1: str, arg2: tuple, arg3: tuple, arg4: tuple, arg5: tuple, /) -> None:
    """Possible exceptions: (Exception, ValueError)."""


def copyResource(arg1: str, arg2: str, /) -> None:
    """Possible exceptions: (Exception)."""
