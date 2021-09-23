import typing

import FreeCAD
import Mesh
import Part


# AppMeshPartPy.cpp
def loftOnCurve(curve: Part.Shape, poly: object, upVector: typing.Sequence[float, float, float], MaxSize: float, /):
    """
    Creates a mesh loft based on a curve and an up vector

    loftOnCurve(curve, poly, upVector, MaxSize)

    Args:
        curve (topology):
        poly (list of (x, y z) or (x, y) tuples of floats):
        upVector ((x, y, z) tuple):
        MaxSize (float):
    """


def findSectionParameters(Edge: Part.Edge, Mesh: Mesh.Mesh, Vector: FreeCAD.Vector, /):
    """
    Find the parameters of the edge where when projecting the corresponding point
    will lie on an edge of the mesh

    findSectionParameters(Edge, Mesh, Vector) -> list
    """


def projectPointsOnMesh(list_of_points: object, Mesh: Mesh.Mesh, Vector: FreeCAD.Vector, float: float = None, /):
    """
    Projects points onto a mesh with a given direction
    and tolerance.projectPointsOnMesh(list of points, Mesh, Vector, [float]) -> list of points
    """


def wireFromSegment(arg1: Mesh.Mesh, arg2: list, /):
    """Create wire(s) from boundary of a mesh segment"""


def wireFromMesh(arg1: Mesh.Mesh, /):
    """Create wire(s) from boundary of a mesh"""


@typing.overload
def projectShapeOnMesh(Shape: Part.Shape, Mesh: Mesh.Mesh, MaxDistance: float): ...


@typing.overload
def projectShapeOnMesh(Shape: Part.Shape, Mesh: Mesh.Mesh, Direction: FreeCAD.Vector): ...


@typing.overload
def projectShapeOnMesh(Polygons: object, Mesh: Mesh.Mesh, Direction: FreeCAD.Vector):
    """
    Projects a shape onto a mesh with a given maximum distance
    projectShapeOnMesh(Shape, Mesh, float) -> polygon
    or projects the shape in a given direction

    Multiple signatures are available:

    projectShapeOnMesh(Shape, Mesh, float) -> list of polygons
    projectShapeOnMesh(Shape, Mesh, Vector) -> list of polygons
    projectShapeOnMesh(list of polygons, Mesh, Vector) -> list of polygons
    """


@typing.overload
def meshFromShape(Shape: Part.Shape, /): ...


@typing.overload
def meshFromShape(Shape: Part.Shape, MaxLength: float): ...


@typing.overload
def meshFromShape(Shape: Part.Shape, MaxArea: float): ...


@typing.overload
def meshFromShape(Shape: Part.Shape, LocalLength: float): ...


@typing.overload
def meshFromShape(Shape: Part.Shape, Deflection: float): ...


@typing.overload
def meshFromShape(Shape: Part.Shape, MinLength: float, MaxLength: float):
    """
    Create surface mesh from shape

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
                             Optimize=1, AllowQuad=0, MaxLength=0, MinLength=0)
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
        SecondOrder (optional, integer boolean)
        Optimize (optional, integer boolean)
        AllowQuad (optional, integer boolean)
        GrowthRate (optional, float)
        SegPerEdge (optional, float)
        SegPerRadius (optional, float)
    """
