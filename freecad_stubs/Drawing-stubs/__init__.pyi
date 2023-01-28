import typing

import FreeCAD
import Part as PartModule


# AppDrawingPy.cpp
@typing.overload
def project(TopoShape_, App_Vector_Direction, string_type, /): ...


@typing.overload
def project(pcObjShape: PartModule.Shape, pcObjDir: FreeCAD.Vector = None, /) -> list[PartModule.Shape]:
    """
    [visiblyG0,visiblyG1,hiddenG0,hiddenG1] = project(TopoShape[,App.Vector Direction, string type])
     -- Project a shape and return the visible/invisible parts of it.
    Possible exceptions: (Exception).
    """


@typing.overload
def projectEx(TopoShape_, App_Vector_Direction, string_type, /): ...


@typing.overload
def projectEx(pcObjShape: PartModule.Shape, pcObjDir: FreeCAD.Vector = None, /) -> list[PartModule.Shape]:
    """
    [V,V1,VN,VO,VI,H,H1,HN,HO,HI] = projectEx(TopoShape[,App.Vector Direction, string type])
     -- Project a shape and return the all parts of it.
    Possible exceptions: (Exception).
    """


def projectToDXF(pcObjShape: PartModule.Shape, pcObjDir: FreeCAD.Vector = None, type: str = None, scale: float = 1.0, tol: float = 0.1, /) -> str:
    """
    string = projectToDXF(TopoShape[,App.Vector Direction, string type])
     -- Project a shape and return the DXF representation as string.
    Possible exceptions: (Exception).
    """


def removeSvgTags(svgcode: str, /) -> str:
    """
    string = removeSvgTags(string) -- Removes the opening and closing svg tags
    and other metatags from a svg code, making it embeddable
    Possible exceptions: (Exception).
    """


def projectToSVG(topoShape: PartModule.Shape = None, direction: FreeCAD.Vector = None, type: str = None, tolerance: float = 0.1, vStyle=None, v0Style=None, v1Style=None, hStyle=None, h0Style=None, h1Style=None) -> str:
    """
    string = projectToSVG(TopoShape[, App.Vector direction, string type, float tolerance, dict vStyle, dict v0Style, dict v1Style, dict hStyle, dict h0Style, dict h1Style])
     -- Project a shape and return the SVG representation as string.
    Possible exceptions: (Exception).
    """
