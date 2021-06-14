import typing

import FreeCAD
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


def findSectionParameters(arg1: Part.TopoShape, arg2: Mesh.MeshObject, arg3: FreeCAD.Vector, /):
    """Find the parameters of the edge where when projecting the corresponding point
    will lie on an edge of the mesh

    findSectionParameters(Edge, Mesh, Vector) -> list
    """


def projectPointsOnMesh(arg1: object, arg2: Mesh.MeshObject, arg3: FreeCAD.Vector, arg4: float = None, /):
    """Projects points onto a mesh with a given direction
    and tolerance.projectPointsOnMesh(list of points, Mesh, Vector, [float]) -> list of points
    """


def wireFromSegment(arg1: Mesh.MeshObject, arg2: list, /):
    """Create wire(s) from boundary of a mesh segment
    """


def wireFromMesh(arg1: Mesh.MeshObject, /):
    """Create wire(s) from boundary of a mesh
    """


@typing.overload
def projectShapeOnMesh(Shape: Part.TopoShape, Mesh: Mesh.MeshObject, MaxDistance: float): ...


@typing.overload
def projectShapeOnMesh(Shape: Part.TopoShape, Mesh: Mesh.MeshObject, Direction: FreeCAD.Vector): ...


@typing.overload
def projectShapeOnMesh(Polygons: object, Mesh: Mesh.MeshObject, Direction: FreeCAD.Vector):
    """Projects a shape onto a mesh with a given maximum distance
    projectShapeOnMesh(Shape, Mesh, float) -> polygon
    or projects the shape in a given direction

    Multiple signatures are available:

    projectShapeOnMesh(Shape, Mesh, float) -> list of polygons
    projectShapeOnMesh(Shape, Mesh, Vector) -> list of polygons
    projectShapeOnMesh(list of polygons, Mesh, Vector) -> list of polygons
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
def meshFromShape(Shape: Part.TopoShape, Fineness: int, SecondOrder: int = None, Optimize: int = None, AllowQuad: int = None, MinLength: float = None, MaxLength: float = None): ...


@typing.overload
def meshFromShape(Shape: Part.TopoShape, GrowthRate: float = None, SegPerEdge: float = None, SegPerRadius: float = None, SecondOrder: int = None, Optimize: int = None, AllowQuad: int = None, MinLength: float = None, MaxLength: float = None):
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
