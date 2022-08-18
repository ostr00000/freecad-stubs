import FreeCAD
import Part as PartModule
import Part.Geom2d
import Part.GeomPlate


# BuildPlateSurfacePy.xml
class BuildPlateSurfacePy(FreeCAD.PyObjectBase):
    """This class provides an algorithm for constructing such a plate surface."""

    def __init__(self, Surface: PartModule.GeometrySurface = None, Degree: int = None, NbPtsOnCur: int = None, NbIter: int = None, Tol2d: float = None, Tol3d: float = None, TolAng: float = None, TolCurv: float = None, Anisotropy: bool = None):
        """
        This class provides an algorithm for constructing such a plate surface.
        Possible exceptions: (ReferenceError, RuntimeError).
        """

    def G0Error(self, arg1: int = None, /) -> float:
        """
        Returns the max distance between the result and the constraints
        Possible exceptions: (RuntimeError).
        """

    def G1Error(self, arg1: int = None, /) -> float:
        """
        Returns the max angle between the result and the constraints
        Possible exceptions: (RuntimeError).
        """

    def G2Error(self, arg1: int = None, /) -> float:
        """
        Returns the max difference of curvature between the result and the constraints
        Possible exceptions: (RuntimeError).
        """

    def add(self, arg1, /):
        """
        Adds a linear or point constraint
        Possible exceptions: (TypeError, RuntimeError).
        """

    def curveConstraint(self, arg1: int, /) -> Part.GeomPlate.CurveConstraintPy:
        """
        Returns the curve constraint of order
        Possible exceptions: (RuntimeError).
        """

    def curves2d(self) -> list:
        """
        Extracts the array of curves on the plate surface which
                correspond to the curve constraints set in add()
        
        Possible exceptions: (RuntimeError).
        """

    def disc2dContour(self, arg1: int, /) -> list[tuple[float, float]]:
        """Possible exceptions: (RuntimeError)."""

    def disc3dContour(self, arg1: int, arg2: int, /) -> list[tuple[float, float, float]]:
        """Possible exceptions: (RuntimeError)."""

    def init(self):
        """
        Resets all constraints
        Possible exceptions: (RuntimeError).
        """

    def isDone(self) -> bool:
        """
        Tests whether computation of the plate has been completed
        Possible exceptions: (RuntimeError).
        """

    def loadInitSurface(self, arg1: PartModule.GeometrySurface, /):
        """
        Loads the initial surface
        Possible exceptions: (ReferenceError, RuntimeError).
        """

    def order(self) -> list[int]:
        """
        Returns the order of the curves in the array returned by curves2d
        Possible exceptions: (RuntimeError).
        """

    def perform(self):
        """
        Calls the algorithm and computes the plate surface
        Possible exceptions: (RuntimeError).
        """

    def pointConstraint(self, arg1: int, /) -> Part.GeomPlate.PointConstraintPy:
        """
        Returns the point constraint of order
        Possible exceptions: (RuntimeError).
        """

    def sense(self) -> list[int]:
        """
        Returns the orientation of the curves in the the array returned by curves2d
        Possible exceptions: (RuntimeError).
        """

    def setNbBounds(self, arg1: int, /):
        """Possible exceptions: (RuntimeError)."""

    def surfInit(self):
        """
        Returns the initial surface
        Possible exceptions: (RuntimeError).
        """

    def surface(self):
        """
        Returns the plate surface
        Possible exceptions: (RuntimeError).
        """


# CurveConstraintPy.xml
class CurveConstraintPy(FreeCAD.PyObjectBase):
    """Defines curves as constraints to be used to deform a surface"""

    def __init__(self, Boundary: PartModule.Curve, Order: int = None, NbPts: int = None, TolDist: float = None, TolAng: float = None, TolCurv: float = None):
        """
        Defines curves as constraints to be used to deform a surface
        Possible exceptions: (ReferenceError, RuntimeError).
        """

    @property
    def FirstParameter(self) -> float: ...

    @property
    def LastParameter(self) -> float: ...

    @property
    def Length(self) -> float: ...

    @property
    def NbPoints(self) -> int:
        """
        The number of points on the curve used as a
        constraint. The default setting is 10. This parameter
        affects computation time, which increases by the cube of
        the number of points.
        """

    def G0Criterion(self, arg1: float, /) -> float:
        """
        Returns the G0 criterion at the parametric point U on
        the curve. This is the greatest distance allowed between
        the constraint and the target surface at U.
        
        Possible exceptions: (RuntimeError).
        """

    def G1Criterion(self, arg1: float, /) -> float:
        """
        Returns the G1 criterion at the parametric point U on
        the curve. This is the greatest angle allowed between
        the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
        
        Possible exceptions: (RuntimeError).
        """

    def G2Criterion(self, arg1: float, /) -> float:
        """
        Returns the G2 criterion at the parametric point U on
        the curve. This is the greatest difference in curvature
        allowed between the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
        
        Possible exceptions: (RuntimeError).
        """

    def curve2dOnSurf(self):
        """Possible exceptions: (RuntimeError)."""

    def curve3d(self):
        """Possible exceptions: (RuntimeError)."""

    def order(self) -> int:
        """
        Returns the order of constraint, one of G0, G1 or G2
        Possible exceptions: (RuntimeError).
        """

    def projectedCurve(self):
        """Possible exceptions: (RuntimeError)."""

    def setCurve2dOnSurf(self, arg1: Part.Geom2d.Curve2d, /):
        """Possible exceptions: (ReferenceError, RuntimeError)."""

    def setG0Criterion(self):
        """
        Allows you to set the G0 criterion. This is the law
        defining the greatest distance allowed between the
        constraint and the target surface for each point of the
        constraint. If this criterion is not set, TolDist, the
        distance tolerance from the constructor, is used.
        
        Possible exceptions: (NotImplementedError).
        """

    def setG1Criterion(self):
        """
        Allows you to set the G1 criterion. This is the law
        defining the greatest angle allowed between the
        constraint and the target surface. If this criterion is not
        set, TolAng, the angular tolerance from the constructor, is used.
        Raises an exception if  the  curve  is  not  on  a  surface
        
        Possible exceptions: (NotImplementedError).
        """

    def setG2Criterion(self):
        """Possible exceptions: (NotImplementedError)."""

    def setOrder(self, arg1: int, /):
        """
        Allows you to set the order of continuity required for
        the constraints: G0, G1, and G2, controlled
        respectively by G0Criterion G1Criterion and G2Criterion.
        
        Possible exceptions: (RuntimeError).
        """

    def setProjectedCurve(self, arg1: Part.Geom2d.Curve2d, arg2: float, arg3: float, /):
        """Possible exceptions: (ReferenceError, RuntimeError)."""


# PointConstraintPy.xml
class PointConstraintPy(FreeCAD.PyObjectBase):
    """Defines points as constraints to be used to deform a surface"""

    def __init__(self, Point: FreeCAD.Vector, Order: int = None, TolDist: float = None):
        """
        Defines points as constraints to be used to deform a surface
        Possible exceptions: (RuntimeError).
        """

    def G0Criterion(self) -> float:
        """
        Returns the G0 criterion at the parametric point U on
        the curve. This is the greatest distance allowed between
        the constraint and the target surface at U.
        
        Possible exceptions: (RuntimeError).
        """

    def G1Criterion(self) -> float:
        """
        Returns the G1 criterion at the parametric point U on
        the curve. This is the greatest angle allowed between
        the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
        
        Possible exceptions: (RuntimeError).
        """

    def G2Criterion(self) -> float:
        """
        Returns the G2 criterion at the parametric point U on
        the curve. This is the greatest difference in curvature
        allowed between the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
        
        Possible exceptions: (RuntimeError).
        """

    def hasPnt2dOnSurf(self) -> bool:
        """Possible exceptions: (RuntimeError)."""

    def order(self) -> int:
        """
        Returns the order of constraint, one of G0, G1 or G2
        Possible exceptions: (RuntimeError).
        """

    def pnt2dOnSurf(self) -> tuple[float, float]:
        """Possible exceptions: (RuntimeError)."""

    def setG0Criterion(self, arg1: float, /):
        """
        Allows you to set the G0 criterion. This is the law
        defining the greatest distance allowed between the
        constraint and the target surface for each point of the
        constraint. If this criterion is not set, TolDist, the
        distance tolerance from the constructor, is used.
        
        Possible exceptions: (RuntimeError).
        """

    def setG1Criterion(self, arg1: float, /):
        """
        Allows you to set the G1 criterion. This is the law
        defining the greatest angle allowed between the
        constraint and the target surface. If this criterion is not
        set, TolAng, the angular tolerance from the constructor, is used.
        Raises an exception if  the  curve  is  not  on  a  surface
        
        Possible exceptions: (RuntimeError).
        """

    def setG2Criterion(self, arg1: float, /):
        """Possible exceptions: (RuntimeError)."""

    def setOrder(self, arg1: int, /):
        """
        Allows you to set the order of continuity required for
        the constraints: G0, G1, and G2, controlled
        respectively by G0Criterion G1Criterion and G2Criterion.
        
        Possible exceptions: (RuntimeError).
        """

    def setPnt2dOnSurf(self, arg1: float, arg2: float, /):
        """Possible exceptions: (RuntimeError)."""
