import FreeCAD
import Mesh as MeshModule
import Part
import Points as PointsModule


# AppReverseEngineering.cpp
def approxSurface(Points, UDegree: int = None, VDegree: int = None, NbUPoles: int = None, NbVPoles: int = None, Smooth: bool = None, Weight: float = None, Grad: float = None, Bend: float = None, Curv: float = None, Iterations: int = None, Correction: bool = None, PatchFactor: float = None, UVDirs: tuple = None) -> Part.BSplineSurface:
    """
    approxSurface(Points=,UDegree=3,VDegree=3,NbUPoles=6,NbVPoles=6,Smooth=True,
    Weight=0.1,Grad=1.0,Bend=0.0,
    Iterations=5,Correction=True,PatchFactor=1.0)
    """


def triangulate(Points: PointsModule.Points, SearchRadius: float, Mu: float = None, KSearch: int = None, Normals=None) -> MeshModule.Mesh:
    """triangulate(PointKernel,searchRadius[,mu=2.5])."""


def poissonReconstruction(Points: PointsModule.Points, KSearch: int = None, OctreeDepth: int = None, SolverDivide: int = None, SamplesPerNode: float = None, Normals=None) -> MeshModule.Mesh:
    """poissonReconstruction(PointKernel)."""


def viewTriangulation(Points: PointsModule.Points, Width: int = None, Height: int = None) -> MeshModule.Mesh:
    """viewTriangulation(PointKernel, width, height)."""


def gridProjection(Points: PointsModule.Points, KSearch: int = None, Normals=None) -> MeshModule.Mesh:
    """gridProjection(PointKernel)."""


def marchingCubesRBF(Points: PointsModule.Points, KSearch: int = None, Normals=None) -> MeshModule.Mesh:
    """marchingCubesRBF(PointKernel)."""


def marchingCubesHoppe(Points: PointsModule.Points, KSearch: int = None, Normals=None) -> MeshModule.Mesh:
    """marchingCubesHoppe(PointKernel)."""


def fitBSpline(Points: PointsModule.Points, Degree: int = None, Refinement: int = None, Iterations: int = None, InteriorSmoothness: float = None, InteriorWeight: float = None, BoundarySmoothness: float = None, BoundaryWeight: float = None) -> Part.BSplineSurface:
    """fitBSpline(PointKernel)."""


def filterVoxelGrid(Points: PointsModule.Points, DimX: float, DimY: float = None, DimZ: float = None) -> PointsModule.Points:
    """filterVoxelGrid(dim)."""


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
    """


def regionGrowingSegmentation(Points: PointsModule.Points, KSearch: int = None, Normals=None) -> list[tuple[int]]:
    """regionGrowingSegmentation()."""


def featureSegmentation(Points: PointsModule.Points, KSearch: int = None) -> list[tuple[int]]:
    """featureSegmentation()."""


def sampleConsensus(SacModel: str, Points: PointsModule.Points, Normals=None) -> dict[str, float | tuple[float] | tuple[int]]:
    """sampleConsensus()."""
