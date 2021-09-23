import FreeCAD
import Part


# AppDrawingPy.cpp
def project(arg1: Part.Shape, arg2: FreeCAD.Vector = None, /):
    """
    [visiblyG0,visiblyG1,hiddenG0,hiddenG1] = project(TopoShape[,App.Vector Direction, string type])
     -- Project a shape and return the visible/invisible parts of it.
    """


def projectEx(arg1: Part.Shape, arg2: FreeCAD.Vector = None, /):
    """
    [V,V1,VN,VO,VI,H,H1,HN,HO,HI] = projectEx(TopoShape[,App.Vector Direction, string type])
     -- Project a shape and return the all parts of it.
    """


def projectToDXF(arg1: Part.Shape, arg2: FreeCAD.Vector = None, arg3: str = None, arg4: float = None, arg5: float = None, /):
    """
    string = projectToDXF(TopoShape[,App.Vector Direction, string type])
     -- Project a shape and return the DXF representation as string.
    """


def removeSvgTags(string: str, /):
    """
    string = removeSvgTags(string) -- Removes the opening and closing svg tags
    and other metatags from a svg code, making it embeddable
    """


def projectToSVG(topoShape: Part.Shape, direction: FreeCAD.Vector = None, type: str = None, tolerance: float = None, vStyle: object = None, v0Style: object = None, v1Style: object = None, hStyle: object = None, h0Style: object = None, h1Style: object = None):
    """
    string = projectToSVG(TopoShape[, App.Vector direction, string type, float tolerance, dict vStyle, dict v0Style, dict v1Style, dict hStyle, dict h0Style, dict h1Style])
     -- Project a shape and return the SVG representation as string.
    """
