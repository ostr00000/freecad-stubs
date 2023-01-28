import typing

import FreeCAD
import Part as PartModule
import Part.Geom2d


# Curve2dPy.xml
class Curve2d(Part.Geom2d.Geometry2d):
    """The abstract class Geom2dCurve is the root class of all curve objects."""

    @property
    def Closed(self) -> bool:
        """Returns true if the curve is closed."""

    @property
    def Continuity(self) -> str:
        """Returns the global continuity of the curve."""

    @property
    def FirstParameter(self) -> float:
        """Returns the value of the first parameter."""

    @property
    def LastParameter(self) -> float:
        """Returns the value of the last parameter."""

    @property
    def Periodic(self) -> bool:
        """Returns true if the curve is periodic."""

    def approximateBSpline(self, tolerance: float, maxSegment: int, maxDegree: int, order: str = 'C2', /) -> Part.Geom2d.BSplineCurve2d:
        """
        Approximates a curve of any type to a B-Spline curve
        					approximateBSpline(Tolerance, MaxSegments, MaxDegree, [Order='C2']) -> B-Spline curve
				
        Possible exceptions: (RuntimeError, Part.OCCError).
        """

    def centerOfCurvature(self, u: float, /) -> FreeCAD.Vector2d:
        """
        Vector = centerOfCurvature(float pos) - Get the center of curvature at the given parameter [First|Last] if defined
        Possible exceptions: (Part.OCCError).
        """

    def curvature(self, u: float, /) -> float:
        """
        Float = curvature(pos) - Get the curvature at the given parameter [First|Last] if defined
        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def discretize(self, Number: int = -1, First: float = None, Last: float = None) -> list[FreeCAD.Vector2d]: ...

    @typing.overload
    def discretize(self, Distance: float = -1, First: float = None, Last: float = None) -> list[FreeCAD.Vector2d]: ...

    @typing.overload
    def discretize(self, Deflection: float, First: float = None, Last: float = None) -> list[FreeCAD.Vector2d]: ...

    @typing.overload
    def discretize(self, QuasiNumber: int, First: float = None, Last: float = None) -> list[FreeCAD.Vector2d]: ...

    @typing.overload
    def discretize(self, QuasiDeflection: float, First: float = None, Last: float = None) -> list[FreeCAD.Vector2d]: ...

    @typing.overload
    def discretize(self, Angular: float, Curvature: float, First: float = None, Last: float = None, Minimum: int = 2) -> list[FreeCAD.Vector2d]: ...

    @typing.overload
    def discretize(self, Number: int = -1, First: float = 3.14, Last: float = None) -> list[FreeCAD.Vector2d]: ...

    @typing.overload
    def discretize(self, Distance: float = -1, First: float = 3.14, Last: float = None) -> list[FreeCAD.Vector2d]: ...

    @typing.overload
    def discretize(self, Deflection: float, First: float = 3.14, Last: float = None) -> list[FreeCAD.Vector2d]: ...

    @typing.overload
    def discretize(self, QuasiNumber: int, First: float = 3.14, Last: float = None) -> list[FreeCAD.Vector2d]: ...

    @typing.overload
    def discretize(self, QuasiDeflection: float, First: float = 3.14, Last: float = None) -> list[FreeCAD.Vector2d]: ...

    @typing.overload
    def discretize(self, Angular: float, Curvature: float, First: float = 3.14, Last: float = 100, Minimum: int = 2) -> list[FreeCAD.Vector2d]:
        """
        Discretizes the curve and returns a list of points.
        The function accepts keywords as argument:
        discretize(Number=n) => gives a list of 'n' equidistant points
        discretize(QuasiNumber=n) => gives a list of 'n' quasi equidistant points (is faster than the method above)
        discretize(Distance=d) => gives a list of equidistant points with distance 'd'
        discretize(Deflection=d) => gives a list of points with a maximum deflection 'd' to the curve
        discretize(QuasiDeflection=d) => gives a list of points with a maximum deflection 'd' to the curve (faster)
        discretize(Angular=a,Curvature=c,[Minimum=m]) => gives a list of points with an angular deflection of 'a'
                                            and a curvature deflection of 'c'. Optionally a minimum number of points
                                            can be set which by default is set to 2.

        Optionally you can set the keywords 'First' and 'Last' to define a sub-range of the parameter range
        of the curve.

        If no keyword is given then it depends on whether the argument is an int or float.
        If it's an int then the behaviour is as if using the keyword 'Number', if it's float
        then the behaviour is as if using the keyword 'Distance'.

        Example:

        import Part
        c=PartGeom2d.Circle2d()
        c.Radius=5
        p=c.discretize(Number=50,First=3.14)
        s=Part.Compound([Part.Vertex(i) for i in p])
        Part.show(s)


        p=c.discretize(Angular=0.09,Curvature=0.01,Last=3.14,Minimum=100)
        s=Part.Compound([Part.Vertex(i) for i in p])
        Part.show(s)

        Possible exceptions: (Part.OCCError).
        """

    def intersectCC(self, p: Part.Geom2d.Curve2d, prec: float = None, /) -> list | list[FreeCAD.Vector2d]:
        """
        Returns all intersection points between this curve and the given curve.
                
        Possible exceptions: (RuntimeError, TypeError).
        """

    def length(self, u: float = None, v: float = None, t: float = None, /) -> float:
        """
        Computes the length of a curve
        length([uMin,uMax,Tol]) -> Float
        Possible exceptions: (Part.OCCError).
        """

    def normal(self, u: float, /) -> FreeCAD.Vector2d:
        """
        Vector = normal(pos) - Get the normal vector at the given parameter [First|Last] if defined
        Possible exceptions: (Part.OCCError).
        """

    def parameter(self, p, /) -> float:
        """
        Returns the parameter on the curve
        of the nearest orthogonal projection of the point.
        Possible exceptions: (Part.OCCError).
        """

    def parameterAtDistance(self, abscissa: float, u: float = 0, /) -> float:
        """
        Returns the parameter on the curve of a point at the given distance from a starting parameter.
        parameterAtDistance([abscissa, startingParameter]) -> Float the
        Possible exceptions: (Part.OCCError).
        """

    def reverse(self):
        """
        Changes the direction of parametrization of the curve.
        Possible exceptions: (Part.OCCError).
        """

    def tangent(self, u: float, /) -> FreeCAD.Vector2d:
        """
        Computes the tangent of parameter u on this curve
        Possible exceptions: (Part.OCCError).
        """

    def toBSpline(self, u: float = None, v: float = None, /) -> Part.Geom2d.BSplineCurve2d:
        """
        Converts a curve of any type (only part from First to Last)
        					toBSpline([Float=First, Float=Last]) -> B-Spline curve
				
        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def toShape(self) -> PartModule.Shape: ...

    @typing.overload
    def toShape(self, u1: float, u2: float, /) -> PartModule.Shape: ...

    @typing.overload
    def toShape(self, p: PartModule.GeometrySurface, /) -> PartModule.Shape: ...

    @typing.overload
    def toShape(self, p: PartModule.GeometrySurface, u1: float, u2: float, /) -> PartModule.Shape: ...

    @typing.overload
    def toShape(self, p: PartModule.Face, /) -> PartModule.Shape: ...

    @typing.overload
    def toShape(self, p: PartModule.Face, u1: float, u2: float, /) -> PartModule.Shape:
        """
        Return the shape for the geometry.
        Possible exceptions: (Part.OCCError, TypeError).
        """

    def value(self, u: float, /) -> FreeCAD.Vector2d:
        """
        Computes the point of parameter u on this curve
        Possible exceptions: (Part.OCCError).
        """


# ArcOfEllipse2dPy.xml
class ArcOfEllipse2d(Part.Geom2d.ArcOfConic2d):
    """Describes a portion of an ellipse"""

    def __init__(self, o: Part.Geom2d.Ellipse2d, u1: float, u2: float, sense: bool = True, /):
        """
        Describes a portion of an ellipse
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Ellipse(self) -> Part.Geom2d.Ellipse2d:
        """The internal ellipse representation"""

    @property
    def MajorRadius(self) -> float:
        """The major radius of the ellipse."""

    @MajorRadius.setter
    def MajorRadius(self, value: float): ...

    @property
    def MinorRadius(self) -> float:
        """The minor radius of the ellipse."""

    @MinorRadius.setter
    def MinorRadius(self, value: float): ...


# ArcOfConic2dPy.xml
class ArcOfConic2d(Part.Geom2d.Curve2d):
    """Describes an abstract arc of conic in 2d space"""

    @property
    def Eccentricity(self) -> float:
        """
        returns the eccentricity value of the conic e.
                    e = 0 for a circle
                    0 < e < 1 for an ellipse  (e = 0 if MajorRadius = MinorRadius)
                    e > 1 for a hyperbola
                    e = 1 for a parabola
        """

    @property
    def Location(self) -> FreeCAD.Vector2d:
        """Location of the conic."""

    @Location.setter
    def Location(self, value: FreeCAD.Vector2d): ...

    @property
    def XAxis(self) -> FreeCAD.Vector2d:
        """The X axis direction of the circle"""

    @XAxis.setter
    def XAxis(self, value: FreeCAD.Vector2d): ...

    @property
    def YAxis(self) -> FreeCAD.Vector2d:
        """The Y axis direction of the circle"""

    @YAxis.setter
    def YAxis(self, value: FreeCAD.Vector2d): ...


# Conic2dPy.xml
class Conic2d(Part.Geom2d.Curve2d):
    """Describes an abstract conic in 2d space"""

    @property
    def Eccentricity(self) -> float:
        """
        returns the eccentricity value of the conic e.
                    e = 0 for a circle
                    0 < e < 1 for an ellipse  (e = 0 if MajorRadius = MinorRadius)
                    e > 1 for a hyperbola
                    e = 1 for a parabola
        """

    @property
    def Location(self) -> FreeCAD.Vector2d:
        """Location of the conic."""

    @Location.setter
    def Location(self, value: FreeCAD.Vector2d): ...

    @property
    def XAxis(self) -> FreeCAD.Vector2d:
        """The X axis direction of the circle"""

    @XAxis.setter
    def XAxis(self, value: FreeCAD.Vector2d): ...

    @property
    def YAxis(self) -> FreeCAD.Vector2d:
        """The Y axis direction of the circle"""

    @YAxis.setter
    def YAxis(self, value: FreeCAD.Vector2d): ...


# Geometry2dPy.xml
class Geometry2d(FreeCAD.PyObjectBase):
    """
    The abstract class Geometry for 2D space is the root class of all geometric objects.
    It describes the common behavior of these objects when:
    - applying geometric transformations to objects, and
    - constructing objects by geometric transformation (including copying).
    """

    def copy(self):
        """
        Create a copy of this geometry
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def mirror(self, o, /): ...

    @typing.overload
    def mirror(self, o, axis, /):
        """
        Performs the symmetrical transformation of this geometric object
        Possible exceptions: (Part.OCCError).
        """

    def rotate(self, o, angle: float, /):
        """
        Rotates this geometric object at angle Ang (in radians) around a point
        Possible exceptions: (Part.OCCError).
        """

    def scale(self, o, scale: float, /):
        """
        Applies a scaling transformation on this geometric object with a center and scaling factor
        Possible exceptions: (Part.OCCError).
        """

    def transform(self, o, /):
        """Applies a transformation to this geometric object"""

    def translate(self, o, /):
        """
        Translates this geometric object
        Possible exceptions: (Part.OCCError).
        """


# Circle2dPy.xml
class Circle2d(Part.Geom2d.Conic2d):
    """
    Describes a circle in 3D space
    To create a circle there are several ways:
    Part.Geom2d.Circle2d()
        Creates a default circle with center (0,0) and radius 1

    Part.Geom2d.Circle2d(circle)
        Creates a copy of the given circle

    Part.Geom2d.Circle2d(circle, Distance)
        Creates a circle parallel to given circle at a certain distance

    Part.Geom2d.Circle2d(Center,Radius)
        Creates a circle defined by center and radius

    Part.Geom2d.Circle2d(Point1,Point2,Point3)
        Creates a circle defined by three non-linear points
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Circle: Part.Geom2d.Circle2d): ...

    @typing.overload
    def __init__(self, Circle: Part.Geom2d.Circle2d, Distance: float): ...

    @typing.overload
    def __init__(self, Center, Radius: float): ...

    @typing.overload
    def __init__(self, Point1, Point2, Point3):
        """
        Describes a circle in 3D space
        To create a circle there are several ways:
        Part.Geom2d.Circle2d()
            Creates a default circle with center (0,0) and radius 1

        Part.Geom2d.Circle2d(circle)
            Creates a copy of the given circle

        Part.Geom2d.Circle2d(circle, Distance)
            Creates a circle parallel to given circle at a certain distance

        Part.Geom2d.Circle2d(Center,Radius)
            Creates a circle defined by center and radius

        Part.Geom2d.Circle2d(Point1,Point2,Point3)
            Creates a circle defined by three non-linear points
   
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Radius(self) -> float:
        """The radius of the circle."""

    @Radius.setter
    def Radius(self, value: float): ...

    @staticmethod
    def getCircleCenter(p1, p2, p3, /) -> FreeCAD.Vector2d:
        """Get the circle center defined by three points"""


# ArcOfParabola2dPy.xml
class ArcOfParabola2d(Part.Geom2d.ArcOfConic2d):
    """Describes a portion of a parabola"""

    def __init__(self, o: Part.Geom2d.Parabola2d, u1: float, u2: float, sense: bool = True, /):
        """
        Describes a portion of a parabola
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Focal(self) -> float:
        """The focal length of the parabola."""

    @Focal.setter
    def Focal(self, value: float): ...

    @property
    def Parabola(self) -> Part.Geom2d.Parabola2d:
        """The internal parabola representation"""


# Line2dSegmentPy.xml
class Line2dSegment(Part.Geom2d.Curve2d):
    """
    Describes a line segment in 2D space
    To create a line there are several ways:
    Part.Geom2d.Line2dSegment()
        Creates a default line

    Part.Geom2d.Line2dSegment(Line)
        Creates a copy of the given line

    Part.Geom2d.Line2dSegment(Point1,Point2)
        Creates a line that goes through two given points
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, pLine: Part.Geom2d.Line2dSegment, /): ...

    @typing.overload
    def __init__(self, pV1, pV2, /): ...

    @typing.overload
    def __init__(self, pLine: Part.Geom2d.Line2dSegment, first: float, last: float, /): ...

    @typing.overload
    def __init__(self, pLine: Part.Geom2d.Line2d, first: float, last: float, /):
        """
        Describes a line segment in 2D space
        To create a line there are several ways:
        Part.Geom2d.Line2dSegment()
            Creates a default line

        Part.Geom2d.Line2dSegment(Line)
            Creates a copy of the given line

        Part.Geom2d.Line2dSegment(Point1,Point2)
            Creates a line that goes through two given points
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def EndPoint(self) -> FreeCAD.Vector2d:
        """Returns the end point of this line segment."""

    @EndPoint.setter
    def EndPoint(self, value: FreeCAD.Vector2d): ...

    @property
    def StartPoint(self) -> FreeCAD.Vector2d:
        """Returns the start point of this line segment."""

    @StartPoint.setter
    def StartPoint(self, value: FreeCAD.Vector2d): ...

    def setParameterRange(self, first: float, last: float, /):
        """
        Set the parameter range of the underlying line segment geometry
        Possible exceptions: (Part.OCCError).
        """


# Ellipse2dPy.xml
class Ellipse2d(Part.Geom2d.Conic2d):
    """
    Describes an ellipse in 2D space
    				To create an ellipse there are several ways:
                    Part.Geom2d.Ellipse2d()
    					Creates an ellipse with major radius 2 and minor radius 1 with the
                        center in (0,0)

                    Part.Geom2d.Ellipse2d(Ellipse)
    					Create a copy of the given ellipse

                    Part.Geom2d.Ellipse2d(S1,S2,Center)
                        Creates an ellipse centered on the point Center,
    					its major axis is defined by Center and S1,
    					its major radius is the distance between Center and S1, and
    					its minor radius is the distance between S2 and the major axis.

                    Part.Geom2d.Ellipse2d(Center,MajorRadius,MinorRadius)
    					Creates an ellipse with major and minor radii MajorRadius and
                        MinorRadius
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Ellipse: Part.Geom2d.Ellipse2d): ...

    @typing.overload
    def __init__(self, S1, S2, Center): ...

    @typing.overload
    def __init__(self, Center, MajorRadius: float, MinorRadius: float):
        """
        Describes an ellipse in 2D space
        				To create an ellipse there are several ways:
                        Part.Geom2d.Ellipse2d()
        					Creates an ellipse with major radius 2 and minor radius 1 with the
                            center in (0,0)

                        Part.Geom2d.Ellipse2d(Ellipse)
        					Create a copy of the given ellipse

                        Part.Geom2d.Ellipse2d(S1,S2,Center)
                            Creates an ellipse centered on the point Center,
        					its major axis is defined by Center and S1,
        					its major radius is the distance between Center and S1, and
        					its minor radius is the distance between S2 and the major axis.

                        Part.Geom2d.Ellipse2d(Center,MajorRadius,MinorRadius)
        					Creates an ellipse with major and minor radii MajorRadius and
                            MinorRadius
			
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Focal(self) -> float:
        """The focal distance of the ellipse."""

    @property
    def Focus1(self) -> FreeCAD.Vector2d:
        """
        The first focus is on the positive side of the major axis of the ellipse;
        the second focus is on the negative side.
        """

    @property
    def Focus2(self) -> FreeCAD.Vector2d:
        """
        The first focus is on the positive side of the major axis of the ellipse;
        the second focus is on the negative side.
        """

    @property
    def MajorRadius(self) -> float:
        """The major radius of the ellipse."""

    @MajorRadius.setter
    def MajorRadius(self, value: float): ...

    @property
    def MinorRadius(self) -> float:
        """The minor radius of the ellipse."""

    @MinorRadius.setter
    def MinorRadius(self, value: float): ...


# ArcOfCircle2dPy.xml
class ArcOfCircle2d(Part.Geom2d.ArcOfConic2d):
    """Describes a portion of a circle"""

    @typing.overload
    def __init__(self, o: Part.Geom2d.Circle2d, u1: float, u2: float, sense: bool = True, /): ...

    @typing.overload
    def __init__(self, pV1, pV2, pV3, /):
        """
        Describes a portion of a circle
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Circle(self) -> Part.Geom2d.Circle2d:
        """The internal circle representation"""

    @property
    def Radius(self) -> float:
        """The radius of the circle."""

    @Radius.setter
    def Radius(self, value: float): ...


# ArcOfHyperbola2dPy.xml
class ArcOfHyperbola2d(Part.Geom2d.ArcOfConic2d):
    """Describes a portion of an hyperbola"""

    def __init__(self, o: Part.Geom2d.Hyperbola2d, u1: float, u2: float, sense: bool = True, /):
        """
        Describes a portion of an hyperbola
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Hyperbola(self) -> Part.Geom2d.Hyperbola2d:
        """The internal hyperbola representation"""

    @property
    def MajorRadius(self) -> float:
        """The major radius of the hyperbola."""

    @MajorRadius.setter
    def MajorRadius(self, value: float): ...

    @property
    def MinorRadius(self) -> float:
        """The minor radius of the hyperbola."""

    @MinorRadius.setter
    def MinorRadius(self, value: float): ...


# Hyperbola2dPy.xml
class Hyperbola2d(Part.Geom2d.Conic2d):
    """
    Describes a hyperbola in 2D space
                    To create a hyperbola there are several ways:
                    Part.Geom2d.Hyperbola2d()
                        Creates a hyperbola with major radius 2 and minor radius 1 with the
                        center in (0,0)

                    Part.Geom2d.Hyperbola2d(Hyperbola)
    					Create a copy of the given hyperbola

                    Part.Geom2d.Hyperbola2d(S1,S2,Center)
                        Creates a hyperbola centered on the point Center, S1 and S2,
    					its major axis is defined by Center and S1,
    					its major radius is the distance between Center and S1, and
    					its minor radius is the distance between S2 and the major axis.

                    Part.Geom2d.Hyperbola2d(Center,MajorRadius,MinorRadius)
                        Creates a hyperbola with major and minor radii MajorRadius and
                        MinorRadius and located at Center
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Hyperbola: Part.Geom2d.Hyperbola2d): ...

    @typing.overload
    def __init__(self, S1, S2, Center): ...

    @typing.overload
    def __init__(self, Center, MajorRadius: float, MinorRadius: float):
        """
        Describes a hyperbola in 2D space
                        To create a hyperbola there are several ways:
                        Part.Geom2d.Hyperbola2d()
                            Creates a hyperbola with major radius 2 and minor radius 1 with the
                            center in (0,0)

                        Part.Geom2d.Hyperbola2d(Hyperbola)
        					Create a copy of the given hyperbola

                        Part.Geom2d.Hyperbola2d(S1,S2,Center)
                            Creates a hyperbola centered on the point Center, S1 and S2,
        					its major axis is defined by Center and S1,
        					its major radius is the distance between Center and S1, and
        					its minor radius is the distance between S2 and the major axis.

                        Part.Geom2d.Hyperbola2d(Center,MajorRadius,MinorRadius)
                            Creates a hyperbola with major and minor radii MajorRadius and
                            MinorRadius and located at Center
			
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Focal(self) -> float:
        """The focal distance of the hyperbola."""

    @property
    def Focus1(self) -> FreeCAD.Vector2d:
        """
        The first focus is on the positive side of the major axis of the hyperbola;
        the second focus is on the negative side.
        """

    @property
    def Focus2(self) -> FreeCAD.Vector2d:
        """
        The first focus is on the positive side of the major axis of the hyperbola;
        the second focus is on the negative side.
        """

    @property
    def MajorRadius(self) -> float:
        """The major radius of the hyperbola."""

    @MajorRadius.setter
    def MajorRadius(self, value: float): ...

    @property
    def MinorRadius(self) -> float:
        """The minor radius of the hyperbola."""

    @MinorRadius.setter
    def MinorRadius(self, value: float): ...


# BSplineCurve2dPy.xml
class BSplineCurve2d(Part.Geom2d.Curve2d):
    """Describes a B-Spline curve in 3D space"""

    def __init__(self):
        """
        Describes a B-Spline curve in 3D space
        Possible exceptions: (TypeError).
        """

    @property
    def Degree(self) -> int:
        """Returns the polynomial degree of this B-Spline curve."""

    @property
    def EndPoint(self) -> FreeCAD.Vector2d:
        """Returns the end point of this B-Spline curve."""

    @property
    def FirstUKnotIndex(self) -> int:
        """
        Returns the index in the knot array of the knot
        corresponding to the first or last parameter
        of this B-Spline curve.
        """

    @property
    def KnotSequence(self) -> list[float]:
        """Returns the knots sequence of this B-Spline curve."""

    @property
    def LastUKnotIndex(self) -> int:
        """
        Returns the index in the knot array of the knot
        corresponding to the first or last parameter
        of this B-Spline curve.
        """

    @property
    def MaxDegree(self) -> int:
        """
        Returns the value of the maximum polynomial degree of any
        B-Spline curve curve. This value is 25.
        """

    @property
    def NbKnots(self) -> int:
        """Returns the number of knots of this B-Spline curve."""

    @property
    def NbPoles(self) -> int:
        """Returns the number of poles of this B-Spline curve."""

    @property
    def StartPoint(self) -> FreeCAD.Vector2d:
        """Returns the start point of this B-Spline curve."""

    def approximate(self, Points, DegMax: int = 8, Continuity: str = 'C2', Tolerance: float = 0.001, DegMin: int = 3, ParamType: str = 'ChordLength', Parameters=None, LengthWeight: float = 0, CurvatureWeight: float = 0, TorsionWeight: float = 0):
        """
        Replaces this B-Spline curve by approximating a set of points.
        					The function accepts keywords as arguments.

        					approximate2(Points = list_of_points)

        					Optional arguments :

        					DegMin = integer (3) : Minimum degree of the curve.
        					DegMax = integer (8) : Maximum degree of the curve.
        					Tolerance = float (1e-3) : approximating tolerance.
        					Continuity = string ('C2') : Desired continuity of the curve.
        					Possible values : 'C0','G1','C1','G2','C2','C3','CN'

        					LengthWeight = float, CurvatureWeight = float, TorsionWeight = float
        					If one of these arguments is not null, the functions approximates the
        					points using variational smoothing algorithm, which tries to minimize
        					additional criterium:
        					LengthWeight*CurveLength + CurvatureWeight*Curvature + TorsionWeight*Torsion
        					Continuity must be C0, C1 or C2, else defaults to C2.

        					Parameters = list of floats : knot sequence of the approximated points.
        					This argument is only used if the weights above are all null.

        					ParamType = string ('Uniform','Centripetal' or 'ChordLength')
        					Parameterization type. Only used if weights and Parameters above aren't specified.

        					Note : Continuity of the spline defaults to C2. However, it may not be applied if
        					it conflicts with other parameters ( especially DegMax ).
				
        Possible exceptions: (Part.OCCError).
        """

    def buildFromPoles(self, obj, periodic: bool = False, degree: int = 3, interpolate: bool = False, /):
        """
        Builds a B-Spline by a list of poles.
				
        Possible exceptions: (Part.OCCError).
        """

    def buildFromPolesMultsKnots(self, poles=None, mults=None, knots=None, periodic: bool = False, degree: int = 3, weights=None):
        """
        Builds a B-Spline by a lists of Poles, Mults, Knots.
        				arguments: poles (sequence of Base.Vector), [mults , knots, periodic, degree, weights (sequence of float), CheckRational]

        				Examples:
        				from FreeCAD import Base
        				import Part
        				V=Base.Vector
        				poles=[V(-10,-10),V(10,-10),V(10,10),V(-10,10)]

        				# non-periodic spline
        				n=Part.BSplineCurve()
        				n.buildFromPolesMultsKnots(poles,(3,1,3),(0,0.5,1),False,2)
        				Part.show(n.toShape())

        				# periodic spline
        				p=Part.BSplineCurve()
        				p.buildFromPolesMultsKnots(poles,(1,1,1,1,1),(0,0.25,0.5,0.75,1),True,2)
        				Part.show(p.toShape())

        				# periodic and rational spline
        				r=Part.BSplineCurve()
        				r.buildFromPolesMultsKnots(poles,(1,1,1,1,1),(0,0.25,0.5,0.75,1),True,2,(1,0.8,0.7,0.2))
        				Part.show(r.toShape())
			
        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def getCardinalSplineTangents(self, Points, Parameter: float) -> list[FreeCAD.Vector2d]: ...

    @typing.overload
    def getCardinalSplineTangents(self, Points, Parameters) -> list[FreeCAD.Vector2d]:
        """Compute the tangents for a Cardinal spline"""

    def getKnot(self, Index: int, /) -> float:
        """Get a knot of the B-Spline curve."""

    def getKnots(self) -> list[float]:
        """
        Get all knots of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def getMultiplicities(self) -> list[int]:
        """
        Returns the multiplicities table M of the knots of this B-Spline curve.
				
        Possible exceptions: (Part.OCCError).
        """

    def getMultiplicity(self, index: int, /) -> int:
        """
        Returns the multiplicity of the knot of index
        from the knots table of this B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def getPole(self, index: int, /) -> FreeCAD.Vector2d:
        """
        Get a pole of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def getPoles(self) -> list[FreeCAD.Vector2d]:
        """
        Get all poles of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def getPolesAndWeights(self) -> list[tuple[float, float, float]]:
        """
        Returns the table of poles and weights in homogeneous coordinates.
        Possible exceptions: (Part.OCCError).
        """

    def getResolution(self, tol: float, /) -> float:
        """
        Computes for this B-Spline curve the parametric tolerance (UTolerance)
        for a given 3D tolerance (Tolerance3D).
        If f(t) is the equation of this B-Spline curve, the parametric tolerance
        ensures that:
        |t1-t0| < UTolerance ===> |f(t1)-f(t0)| < Tolerance3D
        Possible exceptions: (Part.OCCError).
        """

    def getWeight(self, index: int, /) -> float:
        """
        Get a weight of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def getWeights(self) -> list[float]:
        """
        Get all weights of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def increaseDegree(self, degree: int, /):
        """
        increase(Int=Degree)
        Increases the degree of this B-Spline curve to Degree.
        As a result, the poles, weights and multiplicities tables
        are modified; the knots table is not changed. Nothing is
        done if Degree is less than or equal to the current degree.
        Possible exceptions: (Part.OCCError).
        """

    def increaseMultiplicity(self, start: int, end: int, mult: int = -1, /):
        """
        increaseMultiplicity(int index, int mult)
        				increaseMultiplicity(int start, int end, int mult)
        				Increases multiplicity of knots up to mult.

        				index: the index of a knot to modify (1-based)
        				start, end: index range of knots to modify.
        				If mult is lower or equal to the current multiplicity nothing is done. If mult is higher than the degree the degree is used.
				
        Possible exceptions: (Part.OCCError).
        """

    def incrementMultiplicity(self, start: int, end: int, mult: int, /):
        """
        incrementMultiplicity(int start, int end, int mult)
        				Raises multiplicity of knots by mult.

        				start, end: index range of knots to modify.
				
        Possible exceptions: (Part.OCCError).
        """

    def insertKnot(self, U: float, M: int = 1, tol: float = 0.0, /):
        """
        insertKnot(u, mult = 1, tol = 0.0)
        				Inserts a knot value in the sequence of knots. If u is an existing knot the
        				multiplicity is increased by mult. 
        Possible exceptions: (Part.OCCError).
        """

    def insertKnots(self, obj1, obj2, tol: float = 0.0, add: bool = True, /):
        """
        insertKnots(list_of_floats, list_of_ints, tol = 0.0, bool_add = True)
        				Inserts a set of knots values in the sequence of knots.

        				For each u = list_of_floats[i], mult = list_of_ints[i]

        				If u is an existing knot the multiplicity is increased by mult if bool_add is
        				True, otherwise increased to mult.

        				If u is not on the parameter range nothing is done.

        				If the multiplicity is negative or null nothing is done. The new multiplicity
        				is limited to the degree.

        				The tolerance criterion for knots equality is the max of Epsilon(U) and ParametricTolerance.
				
        Possible exceptions: (Part.OCCError).
        """

    def interpolate(self, Points, PeriodicFlag: bool = False, Tolerance: float = None, InitialTangent=None, FinalTangent=None, Tangents=None, TangentFlags=None, Parameters=None):
        """
        Replaces this B-Spline curve by interpolating a set of points.
        					The function accepts keywords as arguments.

        					interpolate(Points = list_of_points)

        					Optional arguments :

        					PeriodicFlag = bool (False) : Sets the curve closed or opened.
        					Tolerance = float (1e-6) : interpolating tolerance

        					Parameters : knot sequence of the interpolated points.
        					If not supplied, the function defaults to chord-length parameterization.
        					If PeriodicFlag == True, one extra parameter must be appended.

        					EndPoint Tangent constraints :

        					InitialTangent = vector, FinalTangent = vector
        					specify tangent vectors for starting and ending points
        					of the BSpline. Either none, or both must be specified.

        					Full Tangent constraints :

        					Tangents = list_of_vectors, TangentFlags = list_of_bools
        					Both lists must have the same length as Points list.
        					Tangents specifies the tangent vector of each point in Points list.
        					TangentFlags (bool) activates or deactivates the corresponding tangent.
        					These arguments will be ignored if EndPoint Tangents (above) are also defined.

        					Note : Continuity of the spline defaults to C2. However, if periodic, or tangents
        					are supplied, the continuity will drop to C1.
				
        Possible exceptions: (Part.OCCError).
        """

    def isClosed(self) -> bool:
        """
        Returns true if the distance between the start point and end point of
        					this B-Spline curve is less than or equal to gp::Resolution().
        """

    def isPeriodic(self) -> bool:
        """Returns true if this BSpline curve is periodic."""

    def isRational(self) -> bool:
        """
        Returns true if this B-Spline curve is rational.
        					A B-Spline curve is rational if, at the time of construction,
        					the weight table has been initialized.
        """

    def join(self, c: Part.Geom2d.BSplineCurve2d, /) -> bool:
        """Build a new spline by joining this and a second spline."""

    @typing.overload
    def makeC1Continuous(self, tol=1e-6, ang_tol=1e-7): ...

    @typing.overload
    def makeC1Continuous(self, tol: float = None, /):
        """
        makeC1Continuous(tol = 1e-6, ang_tol = 1e-7)
        					Reduces as far as possible the multiplicities of the knots of this BSpline
        					(keeping the geometry). It returns a new BSpline, which could still be C0.
        					tol is a geometrical tolerance.
        					The tol_ang is angular tolerance, in radians. It sets tolerable angle mismatch
        					of the tangents on the left and on the right to decide if the curve is G1 or
        					not at a given point.
				
        Possible exceptions: (Part.OCCError).
        """

    def movePoint(self, U: float, pnt, index1: int, index2: int, /) -> tuple[int, int]:
        """
        movePoint(U, P, Index1, Index2)
        				Moves the point of parameter U of this B-Spline curve to P.
        Index1 and Index2 are the indexes in the table of poles of this B-Spline curve
        of the first and last poles designated to be moved.

        Returns: (FirstModifiedPole, LastModifiedPole). They are the indexes of the
        first and last poles which are effectively modified.
        Possible exceptions: (Part.OCCError).
        """

    def removeKnot(self, Index: int, M: int, tol: float, /) -> bool:
        """
        removeKnot(Index, M, tol)

        					Reduces the multiplicity of the knot of index Index to M.
        					If M is equal to 0, the knot is removed.
        					With a modification of this type, the array of poles is also modified.
        					Two different algorithms are systematically used to compute the new
        					poles of the curve. If, for each pole, the distance between the pole
        					calculated using the first algorithm and the same pole calculated using
        					the second algorithm, is less than Tolerance, this ensures that the curve
        					is not modified by more than Tolerance. Under these conditions, true is
        					returned; otherwise, false is returned.

        					A low tolerance is used to prevent modification of the curve.
        					A high tolerance is used to 'smooth' the curve.
				
        Possible exceptions: (Part.OCCError).
        """

    def segment(self, u1: float, u2: float, /):
        """
        segment(u1,u2)
        					Modifies this B-Spline curve by segmenting it.
        Possible exceptions: (Part.OCCError).
        """

    def setKnot(self, Index: int, K: float, M: int = -1, /):
        """Set a knot of the B-Spline curve."""

    def setKnots(self, obj, /):
        """
        Set knots of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def setNotPeriodic(self):
        """
        Changes this B-Spline curve into a non-periodic curve.
        If this curve is already non-periodic, it is not modified.
        Possible exceptions: (Part.OCCError).
        """

    def setOrigin(self, index: int, /):
        """
        Assigns the knot of index Index in the knots table
        as the origin of this periodic B-Spline curve. As a consequence,
        the knots and poles tables are modified.
        Possible exceptions: (Part.OCCError).
        """

    def setPeriodic(self):
        """
        Changes this B-Spline curve into a periodic curve.
        Possible exceptions: (Part.OCCError).
        """

    def setPole(self, index: int, p, weight: float = -1.0, /):
        """
        Modifies this B-Spline curve by assigning P
        to the pole of index Index in the poles table.
        Possible exceptions: (Part.OCCError).
        """

    def setWeight(self, index: int, weight: float, /):
        """
        Set a weight of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def toBezier(self) -> list[Part.Geom2d.BezierCurve2d]:
        """Build a list of Bezier splines."""

    def toBiArcs(self, tolerance: float = 0.001, /) -> list[Part.Geom2d.Geometry2d]:
        """
        Build a list of arcs and lines to approximate the B-spline.
        					toBiArcs(tolerance) -> list.
				
        Possible exceptions: (Part.OCCError).
        """


# BezierCurve2dPy.xml
class BezierCurve2d(Part.Geom2d.Curve2d):
    """
    Describes a rational or non-rational Bezier curve in 2d space:
    				-- a non-rational Bezier curve is defined by a table of poles (also called control points)
    				-- a rational Bezier curve is defined by a table of poles with varying weights
    """

    def __init__(self):
        """
        Describes a rational or non-rational Bezier curve in 2d space:
        				-- a non-rational Bezier curve is defined by a table of poles (also called control points)
        				-- a rational Bezier curve is defined by a table of poles with varying weights
        """

    @property
    def Degree(self) -> int:
        """
        Returns the polynomial degree of this Bezier curve,
        which is equal to the number of poles minus 1.
        """

    @property
    def EndPoint(self) -> FreeCAD.Vector2d:
        """Returns the end point of this Bezier curve."""

    @property
    def MaxDegree(self) -> int:
        """
        Returns the value of the maximum polynomial degree of any
        Bezier curve curve. This value is 25.
        """

    @property
    def NbPoles(self) -> int:
        """Returns the number of poles of this Bezier curve."""

    @property
    def StartPoint(self) -> FreeCAD.Vector2d:
        """Returns the start point of this Bezier curve."""

    def getPole(self, index: int, /) -> FreeCAD.Vector2d:
        """
        Get a pole of the Bezier curve.
        Possible exceptions: (Part.OCCError).
        """

    def getPoles(self) -> list[FreeCAD.Vector2d]:
        """
        Get all poles of the Bezier curve.
        Possible exceptions: (Part.OCCError).
        """

    def getResolution(self, tol: float, /) -> float:
        """
        Computes for this Bezier curve the parametric tolerance (UTolerance)
        for a given 3D tolerance (Tolerance3D).
        If f(t) is the equation of this Bezier curve, the parametric tolerance
        ensures that:
        |t1-t0| < UTolerance ===> |f(t1)-f(t0)| < Tolerance3D
        Possible exceptions: (Part.OCCError).
        """

    def getWeight(self, index: int, /) -> float:
        """
        Get a weight of the Bezier curve.
        Possible exceptions: (Part.OCCError).
        """

    def getWeights(self) -> list[float]:
        """
        Get all weights of the Bezier curve.
        Possible exceptions: (Part.OCCError).
        """

    def increase(self, degree: int, /):
        """
        increase(Int=Degree)
        Increases the degree of this Bezier curve to Degree.
        As a result, the poles and weights tables are modified.
        """

    def insertPoleAfter(self, index: int, p, weight: float = 1.0, /):
        """
        Inserts after the pole of index.
        Possible exceptions: (Part.OCCError).
        """

    def insertPoleBefore(self, index: int, p, weight: float = 1.0, /):
        """
        Inserts before the pole of index.
        Possible exceptions: (Part.OCCError).
        """

    def isClosed(self) -> bool:
        """
        Returns true if the distance between the start point and end point of
        					this Bezier curve is less than or equal to gp::Resolution().
        """

    def isPeriodic(self) -> bool:
        """Returns false."""

    def isRational(self) -> bool:
        """Returns false if the weights of all the poles of this Bezier curve are equal."""

    def removePole(self, index: int, /):
        """
        Removes the pole of index Index from the table of poles of this Bezier curve.
        If this Bezier curve is rational, it can become non-rational.
        Possible exceptions: (Part.OCCError).
        """

    def segment(self, u1: float, u2: float, /):
        """
        Modifies this Bezier curve by segmenting it.
        Possible exceptions: (Part.OCCError).
        """

    def setPole(self, index: int, p, weight: float = -1.0, /):
        """
        Set a pole of the Bezier curve.
        Possible exceptions: (Part.OCCError).
        """

    def setPoles(self, plist, /):
        """
        Set the poles of the Bezier curve.
        Possible exceptions: (Part.OCCError).
        """

    def setWeight(self, index: int, weight: float, /):
        """
        Set a weight of the Bezier curve.
        Possible exceptions: (Part.OCCError).
        """


# OffsetCurve2dPy.xml
class OffsetCurve2d(Part.Geom2d.Curve2d):
    def __init__(self, pGeom: Part.Geom2d.Curve2d, offset: float, /):
        """Possible exceptions: (TypeError, Part.OCCError)."""

    @property
    def BasisCurve(self) -> typing.Any | None:
        """Sets or gets the basic curve."""

    @property
    def OffsetValue(self) -> float:
        """Sets or gets the offset value to offset the underlying curve."""


# Parabola2dPy.xml
class Parabola2d(Part.Geom2d.Conic2d):
    """Describes a parabola in 2D space"""

    def __init__(self):
        """Describes a parabola in 2D space"""

    @property
    def Focal(self) -> float:
        """
        The focal distance is the distance between
        the apex and the focus of the parabola.
        """

    @Focal.setter
    def Focal(self, value: float): ...

    @property
    def Focus(self) -> FreeCAD.Vector2d:
        """
        The focus is on the positive side of the
        'X Axis' of the local coordinate system of the parabola.
        """

    @property
    def Parameter(self) -> float:
        """
        Compute the parameter of this parabola
        which is the distance between its focus
        and its directrix. This distance is twice the focal length.
        """


# Line2dPy.xml
class Line2d(Part.Geom2d.Curve2d):
    """
    Describes an infinite line in 2D space
    To create a line there are several ways:
    Part.Geom2d.Line2d()
        Creates a default line

    Part.Geom2d.Line2d(Line)
        Creates a copy of the given line

    Part.Geom2d.Line2d(Point,Dir)
        Creates a line that goes through two given points
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, pLine: Part.Geom2d.Line2d, /): ...

    @typing.overload
    def __init__(self, pV1, pV2, /):
        """
        Describes an infinite line in 2D space
        To create a line there are several ways:
        Part.Geom2d.Line2d()
            Creates a default line

        Part.Geom2d.Line2d(Line)
            Creates a copy of the given line

        Part.Geom2d.Line2d(Point,Dir)
            Creates a line that goes through two given points
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Direction(self) -> FreeCAD.Vector2d:
        """Returns the direction of this line."""

    @Direction.setter
    def Direction(self, value: FreeCAD.Vector2d): ...

    @property
    def Location(self) -> FreeCAD.Vector2d:
        """Returns the location of this line."""

    @Location.setter
    def Location(self, value: FreeCAD.Vector2d): ...
