import FreeCAD
import Part
import Part.Geom2d


# BuildPlateSurfacePy.xml
class BuildPlateSurfacePy(FreeCAD.PyObjectBase):
    """This class provides an algorithm for constructing such a plate surface."""

    def __init__(self, Surface: Part.GeometrySurface = None, Degree: int = None, NbPtsOnCur: int = None, NbIter: int = None, Tol2d: float = None, Tol3d: float = None, TolAng: float = None, TolCurv: float = None, Anisotropy: bool = None):
        """This class provides an algorithm for constructing such a plate surface."""

    def G0Error(self, arg1: int = None, /):
        """Returns the max distance between the result and the constraints"""

    def G1Error(self, arg1: int = None, /):
        """Returns the max angle between the result and the constraints"""

    def G2Error(self, arg1: int = None, /):
        """Returns the max difference of curvature between the result and the constraints"""

    def add(self, arg1: object, /):
        """Adds a linear or point constraint"""

    def curveConstraint(self, arg1: int, /):
        """Returns the curve constraint of order"""

    def curves2d(self):
        """
        Extracts the array of curves on the plate surface which
                correspond to the curve constraints set in add()
        """

    def disc2dContour(self, arg1: int, /): ...

    def disc3dContour(self, arg1: int, arg2: int, /): ...

    def init(self):
        """Resets all constraints"""

    def isDone(self):
        """Tests whether computation of the plate has been completed"""

    def loadInitSurface(self, arg1: Part.GeometrySurface, /):
        """Loads the initial surface"""

    def order(self):
        """Returns the order of the curves in the array returned by curves2d"""

    def perform(self):
        """Calls the algorithm and computes the plate surface"""

    def pointConstraint(self, arg1: int, /):
        """Returns the point constraint of order"""

    def sense(self):
        """Returns the orientation of the curves in the the array returned by curves2d"""

    def setNbBounds(self, arg1: int, /): ...

    def surfInit(self):
        """Returns the initial surface"""

    def surface(self):
        """Returns the plate surface"""


# CurveConstraintPy.xml
class CurveConstraintPy(FreeCAD.PyObjectBase):
    """Defines curves as constraints to be used to deform a surface"""

    def __init__(self, Boundary: Part.Curve, Order: int = None, NbPts: int = None, TolDist: float = None, TolAng: float = None, TolCurv: float = None):
        """Defines curves as constraints to be used to deform a surface"""

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

    def G0Criterion(self, arg1: float, /):
        """
        Returns the G0 criterion at the parametric point U on
        the curve. This is the greatest distance allowed between
        the constraint and the target surface at U.
        """

    def G1Criterion(self, arg1: float, /):
        """
        Returns the G1 criterion at the parametric point U on
        the curve. This is the greatest angle allowed between
        the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
        """

    def G2Criterion(self, arg1: float, /):
        """
        Returns the G2 criterion at the parametric point U on
        the curve. This is the greatest difference in curvature
        allowed between the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
        """

    def curve2dOnSurf(self): ...

    def curve3d(self): ...

    def order(self):
        """Returns the order of constraint, one of G0, G1 or G2"""

    def projectedCurve(self): ...

    def setCurve2dOnSurf(self, arg1: Part.Geom2d.Curve2d, /): ...

    def setOrder(self, arg1: int, /):
        """
        Allows you to set the order of continuity required for
        the constraints: G0, G1, and G2, controlled
        respectively by G0Criterion G1Criterion and G2Criterion.
        """

    def setProjectedCurve(self, arg1: Part.Geom2d.Curve2d, arg2: float, arg3: float, /): ...


# PointConstraintPy.xml
class PointConstraintPy(FreeCAD.PyObjectBase):
    """Defines points as constraints to be used to deform a surface"""

    def __init__(self, Point: FreeCAD.Vector, Order: int = None, TolDist: float = None):
        """Defines points as constraints to be used to deform a surface"""

    def G0Criterion(self):
        """
        Returns the G0 criterion at the parametric point U on
        the curve. This is the greatest distance allowed between
        the constraint and the target surface at U.
        """

    def G1Criterion(self):
        """
        Returns the G1 criterion at the parametric point U on
        the curve. This is the greatest angle allowed between
        the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
        """

    def G2Criterion(self):
        """
        Returns the G2 criterion at the parametric point U on
        the curve. This is the greatest difference in curvature
        allowed between the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
        """

    def hasPnt2dOnSurf(self): ...

    def order(self):
        """Returns the order of constraint, one of G0, G1 or G2"""

    def pnt2dOnSurf(self): ...

    def setG0Criterion(self, arg1: float, /):
        """
        Allows you to set the G0 criterion. This is the law
        defining the greatest distance allowed between the
        constraint and the target surface for each point of the
        constraint. If this criterion is not set, TolDist, the
        distance tolerance from the constructor, is used.
        """

    def setG1Criterion(self, arg1: float, /):
        """
        Allows you to set the G1 criterion. This is the law
        defining the greatest angle allowed between the
        constraint and the target surface. If this criterion is not
        set, TolAng, the angular tolerance from the constructor, is used.
        Raises an exception if  the  curve  is  not  on  a  surface
        """

    def setG2Criterion(self, arg1: float, /): ...

    def setOrder(self, arg1: int, /):
        """
        Allows you to set the order of continuity required for
        the constraints: G0, G1, and G2, controlled
        respectively by G0Criterion G1Criterion and G2Criterion.
        """

    def setPnt2dOnSurf(self, arg1: float, arg2: float, /): ...
