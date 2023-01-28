import typing

import FreeCAD
import Mesh as MeshModule
import Part as PartModule
import Points as PointsModule


# AppReverseEngineering.cpp
def approxSurface(Points, UDegree: int = 3, VDegree: int = 3, NbUPoles: int = 6, NbVPoles: int = 6, Smooth: bool = True, Weight: float = 0.1, Grad: float = 1.0, Bend: float = 0.0, Curv: float = 0.0, Iterations: int = 5, Correction: bool = True, PatchFactor: float = 1.0, UVDirs: tuple = None) -> PartModule.BSplineSurface:
    """
    approxSurface(Points, UDegree=3, VDegree=3, NbUPoles=6, NbVPoles=6,
    Smooth=True, Weight=0.1, Grad=1.0, Bend=0.0, Curv=0.0
    Iterations=5, Correction=True, PatchFactor=1.0, UVDirs=((ux, uy, uz), (vx, vy, vz)))

    Points: the input data (e.g. a point cloud or mesh)
    UDegree: the degree in u parametric direction
    VDegree: the degree in v parametric direction
    NbUPoles: the number of control points in u parametric direction
    NbVPoles: the number of control points in v parametric direction
    Smooth: use energy terms to create a smooth surface
    Weight: weight of the energy terms altogether
    Grad: weight of the gradient term
    Bend: weight of the bending energy term
    Curv: weight of the deviation of curvature term
    Iterations: number of iterations
    Correction: perform a parameter correction of each iteration step
    PatchFactor: create an extended surface
    UVDirs: set the u,v parameter directions as tuple of two vectors
            If not set then they will be determined by computing a best-fit plane

    Possible exceptions: (Exception, ValueError, RuntimeError).
    """


def triangulate(Points: PointsModule.Points, SearchRadius: float, Mu: float = 2.5, KSearch: int = 5, Normals=0) -> MeshModule.Mesh:
    """
    triangulate(PointKernel,searchRadius[,mu=2.5]).
    Possible exceptions: (Exception).
    """


def poissonReconstruction(Points: PointsModule.Points, KSearch: int = 5, OctreeDepth: int = -1, SolverDivide: int = -1, SamplesPerNode: float = -1.0, Normals=0) -> MeshModule.Mesh:
    """
    poissonReconstruction(PointKernel).
    Possible exceptions: (Exception).
    """


def viewTriangulation(Points: PointsModule.Points, Width: int = None, Height: int = None) -> MeshModule.Mesh:
    """
    viewTriangulation(PointKernel, width, height).
    Possible exceptions: (Exception, RuntimeError).
    """


def gridProjection(Points: PointsModule.Points, KSearch: int = 5, Normals=0) -> MeshModule.Mesh:
    """
    gridProjection(PointKernel).
    Possible exceptions: (Exception).
    """


def marchingCubesRBF(Points: PointsModule.Points, KSearch: int = 5, Normals=0) -> MeshModule.Mesh:
    """
    marchingCubesRBF(PointKernel).
    Possible exceptions: (Exception).
    """


def marchingCubesHoppe(Points: PointsModule.Points, KSearch: int = 5, Normals=0) -> MeshModule.Mesh:
    """
    marchingCubesHoppe(PointKernel).
    Possible exceptions: (Exception).
    """


def fitBSpline(Points: PointsModule.Points, Degree: int = 2, Refinement: int = 4, Iterations: int = 10, InteriorSmoothness: float = 0.2, InteriorWeight: float = 1.0, BoundarySmoothness: float = 0.2, BoundaryWeight: float = 0.0) -> PartModule.BSplineSurface:
    """
    fitBSpline(PointKernel).
    Possible exceptions: (Exception, RuntimeError).
    """


def filterVoxelGrid(Points: PointsModule.Points, DimX: float = 0, DimY: float = 0, DimZ: float = 0) -> PointsModule.Points:
    """
    filterVoxelGrid(dim).
    Possible exceptions: (Exception).
    """


def normalEstimation(Points: PointsModule.Points, KSearch: int = 0, SearchRadius: float = 0) -> list[FreeCAD.Vector]:
    """
    normalEstimation(Points,[KSearch=0, SearchRadius=0]) -> Normals
    KSearch is an int and used to search the k-nearest neighbours in
    the k-d tree. Alternatively, SearchRadius (a float) can be used
    as spatial distance to determine the neighbours of a point
    Example:

    import ReverseEngineering as Reen
    pts=App.ActiveDocument.ActiveObject.Points
    nor=Reen.normalEstimation(pts,KSearch=5)

    f=App.ActiveDocument.addObject('Points::FeaturePython','Normals')
    f.addProperty('Points::PropertyNormalList','Normal')
    f.Points=pts
    f.Normal=nor
    f.ViewObject.Proxy=0
    f.ViewObject.DisplayMode=1

    Possible exceptions: (Exception).
    """


@typing.overload
def regionGrowingSegmentation(): ...


@typing.overload
def regionGrowingSegmentation(Points: PointsModule.Points, KSearch: int = 5, Normals=0) -> list[tuple[int, ...]]:
    """
    regionGrowingSegmentation().
    Possible exceptions: (Exception).
    """


@typing.overload
def featureSegmentation(): ...


@typing.overload
def featureSegmentation(Points: PointsModule.Points, KSearch: int = 5) -> list[tuple[int, ...]]:
    """
    featureSegmentation().
    Possible exceptions: (Exception).
    """


def sampleConsensus(SacModel: str = None, Points: PointsModule.Points = None, Normals=None) -> dict[str, float | tuple[float, ...] | tuple[int, ...]]:
    """
    sampleConsensus().
    Possible exceptions: (Exception).
    """
