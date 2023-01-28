import typing

import FreeCAD
import Mesh as MeshModule
import Part as PartModule


# AppMeshPartPy.cpp
def loftOnCurve(pcTopoObj: PartModule.Shape, pcListObj, x_y_z: tuple[float, float, float] = (0.0, 0.0, 1.0), size: float = 0.1, /) -> MeshModule.Mesh:
    """
    Creates a mesh loft based on a curve and an up vector

    loftOnCurve(curve, poly, upVector, MaxSize)

    Args:
        curve (topology):
        poly (list of (x, y z) or (x, y) tuples of floats):
        upVector ((x, y, z) tuple):
        MaxSize (float):

    Possible exceptions: (Exception, TypeError, ValueError).
    """


def findSectionParameters(e: PartModule.Edge, m: MeshModule.Mesh, v: FreeCAD.Vector, /) -> list[float]:
    """
    Find the parameters of the edge where when projecting the corresponding point
    will lie on an edge of the mesh

    findSectionParameters(Edge, Mesh, Vector) -> list

    Possible exceptions: (Exception).
    """


def projectPointsOnMesh(seq, m: MeshModule.Mesh, v: FreeCAD.Vector, precision: float = -1, /) -> list[FreeCAD.Vector]:
    """
    Projects points onto a mesh with a given direction
    and tolerance.projectPointsOnMesh(list of points, Mesh, Vector, [float]) -> list of points

    Possible exceptions: (Exception).
    """


def wireFromSegment(m: MeshModule.Mesh, o: list, /) -> list[PartModule.Wire]:
    """
    Create wire(s) from boundary of a mesh segment

    Possible exceptions: (Exception).
    """


def wireFromMesh(m: MeshModule.Mesh, /) -> list[PartModule.Wire]:
    """
    Create wire(s) from boundary of a mesh

    Possible exceptions: (Exception).
    """


@typing.overload
def projectShapeOnMesh(Shape: PartModule.Shape, Mesh: MeshModule.Mesh, MaxDistance: float) -> list[list[FreeCAD.Vector]]: ...


@typing.overload
def projectShapeOnMesh(Shape: PartModule.Shape, Mesh: MeshModule.Mesh, Direction: FreeCAD.Vector) -> list[list[FreeCAD.Vector]]: ...


@typing.overload
def projectShapeOnMesh(Polygons, Mesh: MeshModule.Mesh, Direction: FreeCAD.Vector) -> list[list[FreeCAD.Vector]]:
    """
    Projects a shape onto a mesh with a given maximum distance
    projectShapeOnMesh(Shape, Mesh, float) -> polygon
    or projects the shape in a given direction

    Multiple signatures are available:

    projectShapeOnMesh(Shape, Mesh, float) -> list of polygons
    projectShapeOnMesh(Shape, Mesh, Vector) -> list of polygons
    projectShapeOnMesh(list of polygons, Mesh, Vector) -> list of polygons

    Possible exceptions: (TypeError).
    """


@typing.overload
def meshFromShape(shape: PartModule.Shape, /) -> MeshModule.Mesh: ...


@typing.overload
def meshFromShape(Shape: PartModule.Shape, LinearDeflection: float = 0, AngularDeflection: float = 0.5, Relative: bool = False, Segments: bool = False, GroupColors=None) -> MeshModule.Mesh: ...


@typing.overload
def meshFromShape(Shape: PartModule.Shape, MaxLength: float = 0) -> MeshModule.Mesh: ...


@typing.overload
def meshFromShape(Shape: PartModule.Shape, MaxArea: float = 0) -> MeshModule.Mesh: ...


@typing.overload
def meshFromShape(Shape: PartModule.Shape, LocalLength: float = 0) -> MeshModule.Mesh: ...


@typing.overload
def meshFromShape(Shape: PartModule.Shape, Deflection: float = 0) -> MeshModule.Mesh: ...


@typing.overload
def meshFromShape(Shape: PartModule.Shape, MinLength: float = 0, MaxLength: float = 0) -> MeshModule.Mesh: ...


@typing.overload
def meshFromShape(Shape: PartModule.Shape, Fineness: int = 0, SecondOrder: int = 0, Optimize: int = 1, AllowQuad: int = 0, MinLength: float = 0, MaxLength: float = 0) -> MeshModule.Mesh: ...


@typing.overload
def meshFromShape(Shape: PartModule.Shape, GrowthRate: float = 0, SegPerEdge: float = 0, SegPerRadius: float = 0, SecondOrder: int = 0, Optimize: int = 1, AllowQuad: int = 0, MinLength: float = 0, MaxLength: float = 0) -> MeshModule.Mesh:
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

    Possible exceptions: (RuntimeError, TypeError).
    """
