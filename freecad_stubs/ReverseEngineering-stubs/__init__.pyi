import Points


# AppReverseEngineering.cpp
def approxSurface(Points: object, UDegree: int = None, VDegree: int = None, NbUPoles: int = None, NbVPoles: int = None, Smooth: bool = None, Weight: float = None, Grad: float = None, Bend: float = None, Curv: float = None, Iterations: int = None, Correction: bool = None, PatchFactor: float = None, UVDirs: tuple = None):
    """
    approxSurface(Points=,UDegree=3,VDegree=3,NbUPoles=6,NbVPoles=6,Smooth=True,
    Weight=0.1,Grad=1.0,Bend=0.0,
    Iterations=5,Correction=True,PatchFactor=1.0)
    """


def triangulate(Points: Points.Points, SearchRadius: float, Mu: float = None, KSearch: int = None, Normals: object = None):
    """triangulate(PointKernel,searchRadius[,mu=2.5])."""


def poissonReconstruction(Points: Points.Points, KSearch: int = None, OctreeDepth: int = None, SolverDivide: int = None, SamplesPerNode: float = None, Normals: object = None):
    """poissonReconstruction(PointKernel)."""


def viewTriangulation(Points: Points.Points, Width: int = None, Height: int = None):
    """viewTriangulation(PointKernel, width, height)."""


def gridProjection(Points: Points.Points, KSearch: int = None, Normals: object = None):
    """gridProjection(PointKernel)."""


def marchingCubesRBF(Points: Points.Points, KSearch: int = None, Normals: object = None):
    """marchingCubesRBF(PointKernel)."""


def marchingCubesHoppe(Points: Points.Points, KSearch: int = None, Normals: object = None):
    """marchingCubesHoppe(PointKernel)."""


def fitBSpline(Points: Points.Points, Degree: int = None, Refinement: int = None, Iterations: int = None, InteriorSmoothness: float = None, InteriorWeight: float = None, BoundarySmoothness: float = None, BoundaryWeight: float = None):
    """fitBSpline(PointKernel)."""


def filterVoxelGrid(Points: Points.Points, DimX: float, DimY: float = None, DimZ: float = None):
    """filterVoxelGrid(dim)."""


def normalEstimation(Points: Points.Points, KSearch: int = 0, SearchRadius: float = 0):
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


def regionGrowingSegmentation(Points: Points.Points, KSearch: int = None, Normals: object = None):
    """regionGrowingSegmentation()."""


def featureSegmentation(Points: Points.Points, KSearch: int = None):
    """featureSegmentation()."""


def sampleConsensus(SacModel: str, Points: Points.Points, Normals: object = None):
    """sampleConsensus()."""
