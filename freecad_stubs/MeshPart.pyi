import typing

import Mesh
import Part


# AppMeshPartPy.cpp
def loftOnCurve(arg1: Part.TopoShape, arg2: object, arg3: typing.Sequence[float, float, float], arg4: float, /):
    """Creates a mesh loft based on a curve and an up vector

    loftOnCurve(curve, poly, upVector, MaxSize)

    Args:
        curve (topology):
        poly (list of (x, y z) or (x, y) tuples of floats):
        upVector ((x, y, z) tuple):
        MaxSize (float):
    """


def wireFromSegment(arg1: Mesh.MeshObject, arg2: list, /):
    """Create wire(s) from boundary of segment
    """


@typing.overload
def meshFromShape(arg1: Part.TopoShape, /): ...


@typing.overload
def meshFromShape(Shape: Part.TopoShape, LinearDeflection: float, AngularDeflection: float = None, Relative: bool = None, Segments: bool = None, GroupColors: object = None): ...


@typing.overload
def meshFromShape(Shape: Part.TopoShape, MaxLength: float): ...


@typing.overload
def meshFromShape(Shape: Part.TopoShape, MaxArea: float): ...


@typing.overload
def meshFromShape(Shape: Part.TopoShape, LocalLength: float): ...


@typing.overload
def meshFromShape(Shape: Part.TopoShape, Deflection: float): ...


@typing.overload
def meshFromShape(Shape: Part.TopoShape, MinLength: float, MaxLength: float): ...


@typing.overload
def meshFromShape(Shape: Part.TopoShape, Fineness: int, SecondOrder: int = None, Optimize: int = None, AllowQuad: int = None): ...


@typing.overload
def meshFromShape(Shape: Part.TopoShape, GrowthRate: float = None, SegPerEdge: float = None, SegPerRadius: float = None, SecondOrder: int = None, Optimize: int = None, AllowQuad: int = None):
    """Create surface mesh from shape

    Multiple signatures are available:

        meshFromShape(Shape)
        meshFromShape(Shape, LinearDeflection,
                             AngularDeflection=0.5,
                             Relative=False,                         Segments=False,
                             GroupColors=[])
        meshFromShape(Shape, MaxLength)
        meshFromShape(Shape, MaxArea)
        meshFromShape(Shape, LocalLength)
        meshFromShape(Shape, Deflection)
        meshFromShape(Shape, MinLength, MaxLength)

    Additionally, when FreeCAD is built with netgen, the following
    signatures are also available (they are "
    #ifndef HAVE_NETGEN
                "NOT "
    #endif
                "currently):

        meshFromShape(Shape, Fineness, SecondOrder=0,
                             Optimize=1, AllowQuad=0)
        meshFromShape(Shape, GrowthRate=0, SegPerEdge=0,
                      SegPerRadius=0, SecondOrder=0, Optimize=1,
                      AllowQuad=0)

    Args:
        Shape (required, topology) - TopoShape to create mesh of.
        LinearDeflection (required, float)
        AngularDeflection (optional, float)
        Segments (optional, boolean)
        GroupColors (optional, list of (Red, Green, Blue) tuples)
        MaxLength (required, float)
        MaxArea (required, float)
        LocalLength (required, float)
        Deflection (required, float)
        MinLength (required, float)
        Fineness (required, integer)
        SecondOrder (optional, integral boolean)
        Optimize (optional, integeral boolean)
        AllowQuad (optional, integeral boolean)
        GrowthRate (optional, float)
        SegPerEdge (optional, float)
        SegPerRadius (optional, float)
    """
