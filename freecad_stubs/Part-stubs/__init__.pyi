import typing

import FreeCAD
import Part
import Part as PartModule


class ReturnSuggestModesDict(typing.TypedDict):
    allApplicableModes: list[str]
    bestFitMode: str
    error: str
    message: str
    nextRefTypeHint: list[str]
    reachableModes: dict[object, list[list[str]]]
    references_Types: list[str]


class ReturnGetPrincipalPropertiesDict(typing.TypedDict):
    SymmetryAxis: bool
    SymmetryPoint: bool
    Moments: tuple[float, float, float]
    FirstAxisOfInertia: FreeCAD.Vector
    SecondAxisOfInertia: FreeCAD.Vector
    ThirdAxisOfInertia: FreeCAD.Vector
    RadiusOfGyration: tuple[float, float, float]

DocAndStr_t: typing.TypeAlias = tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]
LinkSub_t: typing.TypeAlias = FreeCAD.DocumentObject | None | tuple[()] | DocAndStr_t
LinkList_t: typing.TypeAlias = None | FreeCAD.DocumentObject
SequenceDoc_t: typing.TypeAlias = tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]
LinkSubList_t: typing.TypeAlias = typing.Sequence[SequenceDoc_t | FreeCAD.DocumentObject]
ReturnExportUnitsDict = typing.TypedDict('ReturnExportUnitsDict', {'write.iges.unit': str, 'write.step.unit': str})


# TopoShapeVertexPy.xml
class Vertex(PartModule.Shape):
    """
    This class can be imported.
    TopoShapeVertex is the OpenCasCade topological vertex wrapper
    """

    @typing.overload
    def __init__(self, arg1: float = None, arg2: float = None, arg3: float = None, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, arg1: tuple, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Point, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Shape, /):
        """
        TopoShapeVertex is the OpenCasCade topological vertex wrapper
        Possible exceptions: (TypeError).
        """

    @property
    def Point(self) -> FreeCAD.Vector:
        """Position of this Vertex as a Vector"""

    @property
    def Tolerance(self) -> float:
        """Set or get the tolerance of the vertex"""

    @property
    def X(self) -> float:
        """X component of this Vertex."""

    @property
    def Y(self) -> float:
        """Y component of this Vertex."""

    @property
    def Z(self) -> float:
        """Z component of this Vertex."""


# CylinderPy.xml
class Cylinder(PartModule.GeometrySurface):
    """
    This class can be imported.
    Describes a cylinder in 3D space
    				To create a cylinder there are several ways:
    				Part.Cylinder()
    					Creates a default cylinder with center (0,0,0) and radius 1

    				Part.Cylinder(Cylinder)
    					Creates a copy of the given cylinder

    				Part.Cylinder(Cylinder, Distance)
    					Creates a cylinder parallel to given cylinder at a certain distance

    				Part.Cylinder(Point1,Point2,Point2)
    					Creates a cylinder defined by three non-linear points

    				Part.Cylinder(Circle)
    					Creates a cylinder by a circular base
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Cylinder: PartModule.Cylinder): ...

    @typing.overload
    def __init__(self, Circle: PartModule.Circle): ...

    @typing.overload
    def __init__(self, Cylinder: PartModule.Cylinder, Distance: float): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, Point3: FreeCAD.Vector):
        """
        Describes a cylinder in 3D space
        				To create a cylinder there are several ways:
        				Part.Cylinder()
        					Creates a default cylinder with center (0,0,0) and radius 1

        				Part.Cylinder(Cylinder)
        					Creates a copy of the given cylinder

        				Part.Cylinder(Cylinder, Distance)
        					Creates a cylinder parallel to given cylinder at a certain distance

        				Part.Cylinder(Point1,Point2,Point2)
        					Creates a cylinder defined by three non-linear points

        				Part.Cylinder(Circle)
        					Creates a cylinder by a circular base
			
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Axis(self) -> FreeCAD.Vector:
        """The axis direction of the cylinder"""

    @Axis.setter
    def Axis(self, value: FreeCAD.Vector): ...

    @property
    def Center(self) -> FreeCAD.Vector:
        """Center of the cylinder."""

    @Center.setter
    def Center(self, value: FreeCAD.Vector): ...

    @property
    def Radius(self) -> float:
        """The radius of the cylinder."""

    @Radius.setter
    def Radius(self, value: float): ...

    def uIso(self, arg1: float, /) -> PartModule.Line:
        """
        Builds the U isoparametric circle of this cylinder
        Possible exceptions: (NotImplementedError, Part.OCCError).
        """

    def vIso(self, arg1: float, /) -> PartModule.Circle | PartModule.Ellipse:
        """
        Builds the V isoparametric circle of this cylinder
        Possible exceptions: (NotImplementedError, Part.OCCError).
        """


# AttachEnginePy.xml
class AttachEngine(FreeCAD.BaseClass):
    """
    This class can be imported.
    AttachEngine abstract class - the functinality of AttachableObject, but outside of DocumentObject
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: PartModule.AttachEngine, /): ...

    @typing.overload
    def __init__(self, arg1: str, /):
        """
        AttachEngine abstract class - the functinality of AttachableObject, but outside of DocumentObject
        Possible exceptions: (FreeCAD.FreeCADError).
        """

    @property
    def AttacherType(self) -> str:
        """Type of engine: 3d, plane, line, or point."""

    @property
    def AttachmentOffset(self) -> FreeCAD.Placement:
        """Current attachment mode."""

    @AttachmentOffset.setter
    def AttachmentOffset(self, value: FreeCAD.Placement): ...

    @property
    def CompleteModeList(self) -> list[str]:
        """List of all attachment modes of all AttachEngines. This is the list of modes in MapMode enum properties of AttachableObjects."""

    @property
    def CompleteRefTypeList(self) -> list[str]:
        """List of all reference shape types recognized by AttachEngine."""

    @property
    def ImplementedModes(self) -> list[str]:
        """List of all attachment modes of all AttachEngines. This is the list of modes in MapMode enum properties of AttachableObjects."""

    @property
    def Mode(self) -> str:
        """Current attachment mode."""

    @Mode.setter
    def Mode(self, value: str): ...

    @property
    def Parameter(self) -> float:
        """Value of parameter for some curve attachment modes. Range of 0..1 spans the length of the edge (parameter value can be outside of the range for curves that allow extrapolation."""

    @Parameter.setter
    def Parameter(self, value: float): ...

    @property
    def References(self) -> object:
        """Current attachment mode."""

    @References.setter
    def References(self, value: object): ...

    @property
    def Reverse(self) -> bool:
        """If True, Z axis of attached placement is flipped. X axis is flipped in addition (CS has to remain right-handed)."""

    @Reverse.setter
    def Reverse(self, value: bool): ...

    def calculateAttachedPlacement(self, orig_placement: FreeCAD.Placement, /) -> FreeCAD.Placement | None:
        """
        calculateAttachedPlacement(orig_placement): returns result of attachment, based
        on current Mode, References, etc. AttachmentOffset is included.

        original_placement is the previous placement of the object being attached. It
        is used to preserve orientation for Translate attachment mode. For other modes,
        it is ignored.

        Returns the new placement. If not attached, returns None. If attachment fails,
        an exception is raised.
        """

    def copy(self) -> PartModule.AttachEngine:
        """copy(): returns a new instance of AttachEngine."""

    def downgradeRefType(self, type: str, /) -> str:
        """downgradeRefType(type): returns next more general type. E.g. downgradeType('Circle') yields 'Curve'."""

    def getModeInfo(self, mode: str, /):
        """
        getModeInfo(mode): returns supported reference combinations, user-friendly name, and so on.
        Possible exceptions: (RuntimeError).
        """

    def getRefTypeInfo(self, type: str, /):
        """
        getRefTypeInfo(type): returns information (dict) on shape type. Keys:'UserFriendlyName', 'TypeIndex', 'Rank'. Rank is the number of times reftype can be downgraded, before it becomes 'Any'.
        Possible exceptions: (RuntimeError).
        """

    def getRefTypeOfShape(self, shape: PartModule.Shape, /) -> str:
        """getRefTypeOfShape(shape): returns shape type as interpreted by AttachEngine. Returns a string."""

    def isFittingRefType(self, type_shape: str, type_needed: str, /) -> bool:
        """isFittingRefType(type_shape, type_needed): tests if shape type, specified by type_shape (string), fits a type required by attachment mode type_needed (string). e.g. 'Circle' fits a requirement of 'Edge', and 'Curve' doesn't fit if a 'Circle' is required."""

    def readParametersFromFeature(self, document_object: FreeCAD.DocumentObject, /) -> None:
        """
        readParametersFromFeature(document_object): sets AttachEngine parameters (References, Mode, etc.) by reading out properties of AttachableObject-derived feature.
        Possible exceptions: (TypeError).
        """

    def suggestModes(self) -> ReturnSuggestModesDict:
        """
        suggestModes(): runs mode suggestion routine and returns a dictionary with
        results and supplementary information.

        Keys:
        'allApplicableModes': list of modes that can accept current references. Note
        that it is only a check by types, and does not guarantee the modes will
        actually work.

        'bestFitMode': mode that fits current references best. Note that the mode may
        not be valid for the set of references; check for if 'message' is 'OK'.

        'error': error message for when 'message' is 'UnexpectedError' or
        'LinkBroken'.

        'message': general result of suggestion. 'IncompatibleGeometry', 'NoModesFit':
        no modes accept current set of references; 'OK': some modes do accept current
        set of references (though it's not guarantted the modes will work - surrestor
        only checks for correct types); 'UnexpectedError': should never happen.

        'nextRefTypeHint': what more can be added to references to reach other modes
        ('reachableModes' provide more extended information on this)

        'reachableModes': a dict, where key is mode, and value is a list of sequences
        of references that can be added to fit that mode.

        'references_Types': a list of types of geometry linked by references (that's
        the input information for suggestor, actually).
        """

    def writeParametersToFeature(self, document_object: FreeCAD.DocumentObject, /) -> None:
        """
        writeParametersToFeature(document_object): updates properties of
        AttachableObject-derived feature with current AttachEngine parameters
        (References, Mode, etc.).

        Warning: if a feature linked by AttachEngine.References was deleted, this method
        will crash FreeCAD.
        Possible exceptions: (TypeError).
        """


# EllipsePy.xml
class Ellipse(PartModule.Conic):
    """
    This class can be imported.
    Describes an ellipse in 3D space
    				To create an ellipse there are several ways:
    				Part.Ellipse()
    					Creates an ellipse with major radius 2 and minor radius 1 with the
    					center in (0,0,0)

    				Part.Ellipse(Ellipse)
    					Create a copy of the given ellipse

    				Part.Ellipse(S1,S2,Center)
    					Creates an ellipse centered on the point Center, where
    					the plane of the ellipse is defined by Center, S1 and S2,
    					its major axis is defined by Center and S1,
    					its major radius is the distance between Center and S1, and
    					its minor radius is the distance between S2 and the major axis.

    				Part.Ellipse(Center,MajorRadius,MinorRadius)
    					Creates an ellipse with major and minor radii MajorRadius and
    					MinorRadius, and located in the plane defined by Center and
    					the normal (0,0,1)
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Ellipse: PartModule.Ellipse): ...

    @typing.overload
    def __init__(self, S1: FreeCAD.Vector, S2: FreeCAD.Vector, Center: FreeCAD.Vector): ...

    @typing.overload
    def __init__(self, Center: FreeCAD.Vector, MajorRadius: float, MinorRadius: float):
        """
        Describes an ellipse in 3D space
        				To create an ellipse there are several ways:
        				Part.Ellipse()
        					Creates an ellipse with major radius 2 and minor radius 1 with the
        					center in (0,0,0)

        				Part.Ellipse(Ellipse)
        					Create a copy of the given ellipse

        				Part.Ellipse(S1,S2,Center)
        					Creates an ellipse centered on the point Center, where
        					the plane of the ellipse is defined by Center, S1 and S2,
        					its major axis is defined by Center and S1,
        					its major radius is the distance between Center and S1, and
        					its minor radius is the distance between S2 and the major axis.

        				Part.Ellipse(Center,MajorRadius,MinorRadius)
        					Creates an ellipse with major and minor radii MajorRadius and
        					MinorRadius, and located in the plane defined by Center and
        					the normal (0,0,1)
			
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Focal(self) -> float:
        """The focal distance of the ellipse."""

    @property
    def Focus1(self) -> FreeCAD.Vector:
        """
        The first focus is on the positive side of the major axis of the ellipse;
        the second focus is on the negative side.
        """

    @property
    def Focus2(self) -> FreeCAD.Vector:
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


# TopoShapeSolidPy.xml
class Solid(PartModule.Shape):
    """
    This class can be imported.
    Part.Solid(shape): Create a solid out of shells of shape. If shape is a compsolid, the overall volume solid is created.
    """

    def __init__(self, shape: PartModule.Shape, /):
        """
        Part.Solid(shape): Create a solid out of shells of shape. If shape is a compsolid, the overall volume solid is created.
        Possible exceptions: (Part.OCCError).
        """

    @property
    def CenterOfMass(self) -> FreeCAD.Vector:
        """
        Returns the center of mass of the current system.
        If the gravitational field is uniform, it is the center of gravity.
        The coordinates returned for the center of mass are expressed in the
        absolute Cartesian coordinate system.
        """

    @property
    def Mass(self) -> float:
        """Returns the mass of the current system."""

    @property
    def MatrixOfInertia(self) -> FreeCAD.Matrix:
        """
        Returns the matrix of inertia. It is a symmetrical matrix. 
        The coefficients of the matrix are the quadratic moments of 
        inertia. 

         | Ixx Ixy Ixz 0 | 
         | Ixy Iyy Iyz 0 | 
         | Ixz Iyz Izz 0 | 
         | 0   0   0   1 | 

        The moments of inertia are denoted by Ixx, Iyy, Izz. 
        The products of inertia are denoted by Ixy, Ixz, Iyz. 
        The matrix of inertia is returned in the central coordinate 
        system (G, Gx, Gy, Gz) where G is the centre of mass of the 
        system and Gx, Gy, Gz the directions parallel to the X(1,0,0) 
        Y(0,1,0) Z(0,0,1) directions of the absolute cartesian 
        coordinate system.
        """

    @property
    def OuterShell(self) -> PartModule.Shell:
        """
        Returns the outer most shell of this solid or an null
        shape if the solid has no shells
        """

    @property
    def PrincipalProperties(self) -> ReturnGetPrincipalPropertiesDict:
        """
        Computes the principal properties of inertia of the current system. 
         There is always a set of axes for which the products 
         of inertia of a geometric system are equal to 0; i.e. the 
         matrix of inertia of the system is diagonal. These axes 
         are the principal axes of inertia. Their origin is 
         coincident with the center of mass of the system. The 
         associated moments are called the principal moments of inertia. 
         This function computes the eigen values and the 
         eigen vectors of the matrix of inertia of the system.
        """

    @property
    def StaticMoments(self) -> tuple[float, float, float]:
        """
        Returns Ix, Iy, Iz, the static moments of inertia of the 
         current system; i.e. the moments of inertia about the 
         three axes of the Cartesian coordinate system.
        """

    def getMomentOfInertia(self, point: FreeCAD.Vector, direction: FreeCAD.Vector, /) -> float:
        """
        computes the moment of inertia of the material system about the axis A.
        mySolid.getMomentOfInertia( point, direction )
        Possible exceptions: (Part.OCCError).
        """

    def getRadiusOfGyration(self, point: FreeCAD.Vector, direction: FreeCAD.Vector, /) -> float:
        """
        Returns the radius of gyration of the current system about the axis A.
        mySolid.getRadiusOfGyration( point, direction )
        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def offsetFaces(self, arg1, solid_Faces_1_2_0_: float, /) -> PartModule.Solid: ...

    @typing.overload
    def offsetFaces(self, arg1, arg2: float, /) -> PartModule.Solid:
        """
        Extrude single faces of the solid.
        Example:
        solid.offsetFaces({solid.Faces[0]:1.0,solid.Faces[1]:2.0})
        Example:
        solid.offsetFaces((solid.Faces[0],solid.Faces[1]), 1.5)
        
        Possible exceptions: (TypeError, Part.OCCError).
        """


# BoundedCurvePy.xml
class BoundedCurve(PartModule.Curve):
    """The abstract class BoundedCurve is the root class of all bounded curve objects."""

    @property
    def EndPoint(self) -> FreeCAD.Vector:
        """Returns the end point of the bounded curve."""

    @property
    def StartPoint(self) -> FreeCAD.Vector:
        """Returns the starting point of the bounded curve."""


# HyperbolaPy.xml
class Hyperbola(PartModule.Conic):
    """
    This class can be imported.
    Describes an hyperbola in 3D space
    				To create a hyperbola there are several ways:
    				Part.Hyperbola()
    					Creates an hyperbola with major radius 2 and minor radius 1 with the
    					center in (0,0,0)

    				Part.Hyperbola(Hyperbola)
    					Create a copy of the given hyperbola

    				Part.Hyperbola(S1,S2,Center)
    					Creates an hyperbola centered on the point Center, where
    					the plane of the hyperbola is defined by Center, S1 and S2,
    					its major axis is defined by Center and S1,
    					its major radius is the distance between Center and S1, and
    					its minor radius is the distance between S2 and the major axis.

    				Part.Hyperbola(Center,MajorRadius,MinorRadius)
    					Creates an hyperbola with major and minor radii MajorRadius and
    					MinorRadius, and located in the plane defined by Center and
    					the normal (0,0,1)
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Hyperbola: PartModule.Hyperbola): ...

    @typing.overload
    def __init__(self, S1: FreeCAD.Vector, S2: FreeCAD.Vector, Center: FreeCAD.Vector): ...

    @typing.overload
    def __init__(self, Center: FreeCAD.Vector, MajorRadius: float, MinorRadius: float):
        """
        Describes an hyperbola in 3D space
        				To create a hyperbola there are several ways:
        				Part.Hyperbola()
        					Creates an hyperbola with major radius 2 and minor radius 1 with the
        					center in (0,0,0)

        				Part.Hyperbola(Hyperbola)
        					Create a copy of the given hyperbola

        				Part.Hyperbola(S1,S2,Center)
        					Creates an hyperbola centered on the point Center, where
        					the plane of the hyperbola is defined by Center, S1 and S2,
        					its major axis is defined by Center and S1,
        					its major radius is the distance between Center and S1, and
        					its minor radius is the distance between S2 and the major axis.

        				Part.Hyperbola(Center,MajorRadius,MinorRadius)
        					Creates an hyperbola with major and minor radii MajorRadius and
        					MinorRadius, and located in the plane defined by Center and
        					the normal (0,0,1)
			
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Focal(self) -> float:
        """The focal distance of the hyperbola."""

    @property
    def Focus1(self) -> FreeCAD.Vector:
        """
        The first focus is on the positive side of the major axis of the hyperbola;
        the second focus is on the negative side.
        """

    @property
    def Focus2(self) -> FreeCAD.Vector:
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


# PlateSurfacePy.xml
class PlateSurface(PartModule.GeometrySurface):
    """This class can be imported."""

    def __init__(self, Surface: PartModule.Geometry = None, Points=None, Curves=None, Degree: int = None, NbPtsOnCur: int = None, NbIter: int = None, Tol2d: float = None, Tol3d: float = None, TolAng: float = None, TolCurv: float = None, Anisotropie: bool = None):
        """Possible exceptions: (ValueError, TypeError, Part.OCCError)."""

    def makeApprox(self, Tol3d: float = None, MaxSegments: int = None, MaxDegree: int = None, MaxDistance: float = None, CritOrder: int = None, Continuity: str = None, EnlargeCoeff: float = None) -> PartModule.BSplineSurface:
        """
        Approximate the plate surface to a B-Spline surface
        Possible exceptions: (RuntimeError).
        """


# OffsetCurvePy.xml
class OffsetCurve(PartModule.Curve):
    """This class can be imported."""

    def __init__(self, arg1: PartModule.Geometry, arg2: float, arg3: FreeCAD.Vector, /):
        """Possible exceptions: (TypeError, Part.OCCError)."""

    @property
    def BasisCurve(self) -> object:
        """Sets or gets the basic curve."""

    @property
    def OffsetDirection(self) -> FreeCAD.Vector:
        """Sets or gets the offset direction to offset the underlying curve."""

    @property
    def OffsetValue(self) -> float:
        """Sets or gets the offset value to offset the underlying curve."""


# CirclePy.xml
class Circle(PartModule.Conic):
    """
    This class can be imported.
    Describes a circle in 3D space
    To create a circle there are several ways:
    Part.Circle()
        Creates a default circle with center (0,0,0) and radius 1

    Part.Circle(Circle)
        Creates a copy of the given circle

    Part.Circle(Circle, Distance)
        Creates a circle parallel to given circle at a certain distance

    Part.Circle(Center,Normal,Radius)
        Creates a circle defined by center, normal direction and radius

    Part.Circle(Point1,Point2,Point3)
        Creates a circle defined by three non-linear points
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Circle: PartModule.Circle): ...

    @typing.overload
    def __init__(self, Circle: PartModule.Circle, Distance: float): ...

    @typing.overload
    def __init__(self, Center: FreeCAD.Vector, Normal: FreeCAD.Vector, Radius: float): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, Point3: FreeCAD.Vector):
        """
        Describes a circle in 3D space
        To create a circle there are several ways:
        Part.Circle()
            Creates a default circle with center (0,0,0) and radius 1

        Part.Circle(Circle)
            Creates a copy of the given circle

        Part.Circle(Circle, Distance)
            Creates a circle parallel to given circle at a certain distance

        Part.Circle(Center,Normal,Radius)
            Creates a circle defined by center, normal direction and radius

        Part.Circle(Point1,Point2,Point3)
            Creates a circle defined by three non-linear points
   
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Radius(self) -> float:
        """The radius of the circle."""

    @Radius.setter
    def Radius(self, value: float): ...


# ArcPy.xml
class Arc(PartModule.TrimmedCurve):
    """
    This class can be imported.
    Describes a portion of a curve
    """

    @typing.overload
    def __init__(self, arg1: PartModule.Circle, arg2: float, arg3: float, arg4: bool = None, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, arg3: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Ellipse, arg2: float, arg3: float, arg4: bool = None, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Parabola, arg2: float, arg3: float, arg4: bool = None, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Hyperbola, arg2: float, arg3: float, arg4: bool = None, /):
        """
        Describes a portion of a curve
        Possible exceptions: (Part.OCCError, TypeError).
        """


# OffsetSurfacePy.xml
class OffsetSurface(PartModule.GeometrySurface):
    """This class can be imported."""

    def __init__(self, arg1: PartModule.Geometry, arg2: float, /):
        """Possible exceptions: (TypeError, Part.OCCError)."""

    @property
    def BasisSurface(self) -> object:
        """Sets or gets the basic surface."""

    @property
    def OffsetValue(self) -> float:
        """Sets or gets the offset value to offset the underlying surface."""


# PlanePy.xml
class Plane(PartModule.GeometrySurface):
    """
    This class can be imported.
    Describes an infinite plane
    To create a plane there are several ways:
    Part.Plane()
        Creates a default plane with base (0,0,0) and normal (0,0,1)

    Part.Plane(Plane)
        Creates a copy of the given plane

    Part.Plane(Plane, Distance)
        Creates a plane parallel to given plane at a certain distance

    Part.Plane(Location,Normal)
        Creates a plane with a given location and normal

    Part.Plane(Point1,Point2,Point3)
        Creates a plane defined by three non-linear points

    Part.Plane(A,B,C,D)
        Creates a plane from its cartesian equation
        Ax+By+Cz+D=0
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Plane: PartModule.Plane): ...

    @typing.overload
    def __init__(self, Plane: PartModule.Plane, Distance: float): ...

    @typing.overload
    def __init__(self, Location: FreeCAD.Vector, Normal: FreeCAD.Vector): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, Point3: FreeCAD.Vector): ...

    @typing.overload
    def __init__(self, A: float, B: float, C: float, D: float):
        """
        Describes an infinite plane
        To create a plane there are several ways:
        Part.Plane()
            Creates a default plane with base (0,0,0) and normal (0,0,1)

        Part.Plane(Plane)
            Creates a copy of the given plane

        Part.Plane(Plane, Distance)
            Creates a plane parallel to given plane at a certain distance

        Part.Plane(Location,Normal)
            Creates a plane with a given location and normal

        Part.Plane(Point1,Point2,Point3)
            Creates a plane defined by three non-linear points

        Part.Plane(A,B,C,D)
            Creates a plane from its cartesian equation
            Ax+By+Cz+D=0

        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Axis(self) -> FreeCAD.Vector:
        """Returns the axis of this plane."""

    @Axis.setter
    def Axis(self, value: FreeCAD.Vector): ...

    @property
    def Position(self) -> FreeCAD.Vector:
        """Returns the position point of this plane."""

    @Position.setter
    def Position(self, value: FreeCAD.Vector): ...

    def uIso(self, arg1: float, /) -> PartModule.Line:
        """
        Builds the U isoparametric line of this plane
        Possible exceptions: (Part.OCCError).
        """

    def vIso(self, arg1: float, /) -> PartModule.Line:
        """
        Builds the V isoparametric line of this plane
        Possible exceptions: (Part.OCCError).
        """


# TopoShapeFacePy.xml
class Face(PartModule.Shape):
    """
    This class can be imported.
    TopoShapeFace is the OpenCasCade topological face wrapper
    """

    @typing.overload
    def __init__(self, arg1: PartModule.Shape, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Face, arg2: PartModule.Wire, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.GeometrySurface, arg2: PartModule.Wire, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Geometry, arg2: list = None, /): ...

    @typing.overload
    def __init__(self, arg1: list, /): ...

    @typing.overload
    def __init__(self, arg1, arg2: str, /):
        """
        TopoShapeFace is the OpenCasCade topological face wrapper
        Possible exceptions: (Part.OCCError, TypeError, FreeCAD.FreeCADError).
        """

    @property
    def CenterOfMass(self) -> FreeCAD.Vector:
        """
        Returns the center of mass of the current system.
        If the gravitational field is uniform, it is the center of gravity.
        The coordinates returned for the center of mass are expressed in the
        absolute Cartesian coordinate system.
        """

    @property
    def Mass(self) -> float:
        """Returns the mass of the current system."""

    @property
    def MatrixOfInertia(self) -> FreeCAD.Matrix:
        """
        Returns the matrix of inertia. It is a symmetrical matrix. 
        The coefficients of the matrix are the quadratic moments of 
        inertia. 

         | Ixx Ixy Ixz 0 | 
         | Ixy Iyy Iyz 0 | 
         | Ixz Iyz Izz 0 | 
         | 0   0   0   1 | 

        The moments of inertia are denoted by Ixx, Iyy, Izz. 
        The products of inertia are denoted by Ixy, Ixz, Iyz. 
        The matrix of inertia is returned in the central coordinate 
        system (G, Gx, Gy, Gz) where G is the centre of mass of the 
        system and Gx, Gy, Gz the directions parallel to the X(1,0,0) 
        Y(0,1,0) Z(0,0,1) directions of the absolute cartesian 
        coordinate system.
        """

    @property
    def OuterWire(self) -> PartModule.Wire:
        """The outer wire of this face"""

    @property
    def ParameterRange(self) -> tuple[float, float, float, float]:
        """Returns a 4 tuple with the parameter range"""

    @property
    def PrincipalProperties(self) -> ReturnGetPrincipalPropertiesDict:
        """
        Computes the principal properties of inertia of the current system. 
         There is always a set of axes for which the products 
         of inertia of a geometric system are equal to 0; i.e. the 
         matrix of inertia of the system is diagonal. These axes 
         are the principal axes of inertia. Their origin is 
         coincident with the center of mass of the system. The 
         associated moments are called the principal moments of inertia. 
         This function computes the eigen values and the 
         eigen vectors of the matrix of inertia of the system.
        """

    @property
    def StaticMoments(self) -> tuple[float, float, float]:
        """
        Returns Ix, Iy, Iz, the static moments of inertia of the 
         current system; i.e. the moments of inertia about the 
         three axes of the Cartesian coordinate system.
        """

    @property
    def Surface(self) -> object:
        """Returns the geometric surface of the face"""

    @property
    def Tolerance(self) -> float:
        """Set or get the tolerance of the vertex"""

    @property
    def Wire(self) -> object:
        """
        The outer wire of this face
        deprecated -- please use OuterWire
        """

    def curvatureAt(self, arg1: float, arg2: float, /) -> tuple[float, float]:
        """
        Float = curvatureAt(pos) - Get the curvature at the given parameter [0|Length] if defined
        Possible exceptions: (Part.OCCError).
        """

    def curveOnSurface(self, arg1: PartModule.Edge, /) -> tuple[object, float, float]:
        """
        curveonSurface(Edge) -> None or tuple
        Returns the curve  associated to the  edge in  the
        parametric  space of  the  face.  Returns None if this
        curve  does not exist. If this curve exists then a tuple
        of curve and and parameter range is returned.
                
        Possible exceptions: (RuntimeError, Part.OCCError).
        """

    def derivative1At(self, arg1: float, arg2: float, /) -> tuple[FreeCAD.Vector, FreeCAD.Vector]:
        """
        Vector = d1At(pos) - Get the first derivative at the given parameter [0|Length] if defined
        Possible exceptions: (Part.OCCError).
        """

    def derivative2At(self, arg1: float, arg2: float, /) -> tuple[FreeCAD.Vector, FreeCAD.Vector]:
        """
        Vector = d2At(pos) - Get the second derivative at the given parameter [0|Length] if defined
        Possible exceptions: (Part.OCCError).
        """

    def getUVNodes(self) -> list | list[tuple[float, float]]:
        """
        getUVNodes() --> list
        Get the list of (u,v) nodes of the tessellation
        An exception is raised if the face is not triangulated.

        Possible exceptions: (RuntimeError).
        """

    def isPartOfDomain(self, arg1: float, arg2: float, /) -> bool:
        """
        Check if a given (u,v) pair is inside the domain of a face
        Possible exceptions: (Part.OCCError).
        """

    def makeHalfSpace(self, arg1: FreeCAD.Vector, /) -> PartModule.Solid:
        """
        Make a half-space solid by this face and a reference point.
        Possible exceptions: (Part.OCCError).
        """

    def makeOffset(self, arg1: float, /) -> PartModule.Shape:
        """
        Offset the face by a given amount. Returns Compound of Wires. Deprecated - use makeOffset2D instead.
        Possible exceptions: (Part.OCCError).
        """

    def normalAt(self, arg1: float, arg2: float, /) -> FreeCAD.Vector:
        """
        Vector = normalAt(pos) - Get the normal vector at the given parameter [0|Length] if defined
        Possible exceptions: (Part.OCCError).
        """

    def tangentAt(self, arg1: float, arg2: float, /) -> tuple[FreeCAD.Vector, FreeCAD.Vector]:
        """
        Get the tangent in u and v isoparametric at the given point if defined
        Possible exceptions: (Part.OCCError).
        """

    def validate(self):
        """
        Validate the face.
        Possible exceptions: (Part.OCCError).
        """

    def valueAt(self, arg1: float, arg2: float, /) -> FreeCAD.Vector:
        """Vector = valueAt(pos) - Get the point at the given parameter [0|Length] if defined"""


# BRepOffsetAPI_MakePipeShellPy.xml
class BRepOffsetAPI_MakePipeShell(FreeCAD.PyObjectBase):
    """Describes a portion of a circle"""

    @typing.overload
    def add(self, Profile: PartModule.Shape, WithContact: bool = False, WithCorrection: bool = False): ...

    @typing.overload
    def add(self, Profile: PartModule.Shape, Location: PartModule.Vertex, WithContact: bool = False, WithCorrection: bool = False):
        """
        add(shape Profile, bool WithContact=False, bool WithCorrection=False)
        					add(shape Profile, vertex Location, bool WithContact=False, bool WithCorrection=False)
        					Adds the section Profile to this framework.
        					First and last sections may be punctual, so the shape Profile may be both wire and vertex.
        					If WithContact is true, the section is translated to be in contact with the spine.
        					If WithCorrection is true, the section is rotated to be orthogonal to the spine tangent in the correspondent point.
				
        Possible exceptions: (Part.OCCError, TypeError).
        """

    def build(self):
        """
        build()
        					Builds the resulting shape.
				
        Possible exceptions: (Part.OCCError).
        """

    def firstShape(self) -> PartModule.Shape:
        """
        firstShape()
        					Returns the Shape of the bottom of the sweep.
				
        Possible exceptions: (Part.OCCError).
        """

    def generated(self, shape_S: PartModule.Shape, /) -> list[PartModule.Shape]:
        """
        generated(shape S)
        					Returns a list of new shapes generated from the shape S by the shell-generating algorithm.
				
        Possible exceptions: (Part.OCCError).
        """

    def getStatus(self) -> int:
        """
        getStatus()
        					Get a status, when Simulate or Build failed.
				
        Possible exceptions: (Part.OCCError).
        """

    def isReady(self) -> bool:
        """
        isReady()
        					Returns true if this tool object is ready to build the shape.
				
        Possible exceptions: (Part.OCCError).
        """

    def lastShape(self) -> PartModule.Shape:
        """
        lastShape()
        					Returns the Shape of the top of the sweep.
				
        Possible exceptions: (Part.OCCError).
        """

    def makeSolid(self) -> bool:
        """
        makeSolid()
        					Transforms the sweeping Shell in Solid. If a propfile is not closed returns False.
				
        Possible exceptions: (Part.OCCError).
        """

    def remove(self, shape_Profile: PartModule.Shape, /):
        """
        remove(shape Profile)
        					Removes the section Profile from this framework.
				
        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def setAuxiliarySpine(self, wire: PartModule.Shape, CurvilinearEquivalence: bool, TypeOfContact: int, /): ...

    @typing.overload
    def setAuxiliarySpine(self, wire: PartModule.Shape, CurvilinearEquivalence: bool, TypeOfContact: bool, /):
        """
        setAuxiliarySpine(wire, CurvilinearEquivalence, TypeOfContact)
        					Sets an auxiliary spine to define the Normal.
					
        					CurvilinearEquivalence = bool
        					For each Point of the Spine P, an Point Q is evalued on AuxiliarySpine.
        					If CurvilinearEquivalence=True Q split AuxiliarySpine with the same length ratio than P split Spine.
					
        					* OCC before 6.7
        					TypeOfContact = bool
        					True = keep Contact
					
        					* OCC >= 6.7
        					TypeOfContact = long
        					0: No contact
        					1: Contact
        					2: Contact On Border (The auxiliary spine becomes a boundary of the swept surface)
				
        Possible exceptions: (TypeError, Part.OCCError).
        """

    def setBiNormalMode(self, direction: FreeCAD.Vector, /):
        """
        setBiNormalMode(direction)
        					Sets a fixed BiNormal direction to perform the sweeping.
        					Angular relations between the section(s) and the BiNormal direction will be constant.
				
        Possible exceptions: (Part.OCCError).
        """

    def setForceApproxC1(self, bool: bool, /):
        """
        setForceApproxC1(bool)
        					Set the flag that indicates attempt to approximate a C1-continuous surface if a swept surface proved to be C0.
				
        Possible exceptions: (RuntimeError, Part.OCCError).
        """

    def setFrenetMode(self, True_False: bool, /):
        """
        setFrenetMode(True|False)
        					Sets a Frenet or a CorrectedFrenet trihedron to perform the sweeping.
        					True  = Frenet
        					False = CorrectedFrenet
				
        Possible exceptions: (Part.OCCError).
        """

    def setMaxDegree(self, int_degree: int, /):
        """
        setMaxDegree(int degree)
        					Define the maximum V degree of resulting surface. 
				
        Possible exceptions: (RuntimeError, Part.OCCError).
        """

    def setMaxSegments(self, int_num: int, /):
        """
        setMaxSegments(int num)
        					Define the maximum number of spans in V-direction on resulting surface.
				
        Possible exceptions: (RuntimeError, Part.OCCError).
        """

    def setSpineSupport(self, shape: PartModule.Shape, /) -> bool:
        """
        setSpineSupport(shape)
        					Sets support to the spine to define the BiNormal of the trihedron, like the normal to the surfaces.
        					Warning: To be effective, Each edge of the spine must have an representation on one face of SpineSupport.
				
        Possible exceptions: (Part.OCCError).
        """

    def setTolerance(self, tol3d: float, boundTol: float, tolAngular: float, /):
        """
        setTolerance( tol3d, boundTol, tolAngular)
        					Tol3d = 3D tolerance
        					BoundTol = boundary tolerance
        					TolAngular = angular tolerance
				
        Possible exceptions: (Part.OCCError).
        """

    def setTransitionMode(self, arg1: int, /):
        """
        0: BRepBuilderAPI_Transformed
        					1: BRepBuilderAPI_RightCorner
        					2: BRepBuilderAPI_RoundCorner
				
        Possible exceptions: (Part.OCCError).
        """

    def setTrihedronMode(self, point: FreeCAD.Vector, direction: FreeCAD.Vector, /):
        """
        setTrihedronMode(point,direction)
        					Sets a fixed trihedron to perform the sweeping.
        					All sections will be parallel. 
				
        Possible exceptions: (Part.OCCError).
        """

    def shape(self) -> PartModule.Shape:
        """
        shape()
        					Returns the resulting shape.
				
        Possible exceptions: (Part.OCCError).
        """

    def simulate(self, int_nbsec: int, /) -> list[PartModule.Shape]:
        """
        simulate(int nbsec)
        					Simulates the resulting shape by calculating the given number of cross-sections.
				
        Possible exceptions: (Part.OCCError).
        """


# TopoShapeCompSolidPy.xml
class CompSolid(PartModule.Shape):
    """
    This class can be imported.
    TopoShapeCompSolid is the OpenCasCade topological compound solid wrapper
    """

    def __init__(self, arg1, /):
        """
        TopoShapeCompSolid is the OpenCasCade topological compound solid wrapper
        Possible exceptions: (Part.OCCError).
        """

    def add(self, arg1: PartModule.Solid, /):
        """
        Add a solid to the compound.
        Possible exceptions: (Part.OCCError).
        """


# ParabolaPy.xml
class Parabola(PartModule.Conic):
    """
    This class can be imported.
    Describes a parabola in 3D space
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Parabola: PartModule.Parabola): ...

    @typing.overload
    def __init__(self, Focus: FreeCAD.Vector, Center: FreeCAD.Vector, Normal: FreeCAD.Vector):
        """
        Describes a parabola in 3D space
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Focal(self) -> float:
        """
        The focal distance is the distance between
        the apex and the focus of the parabola.
        """

    @Focal.setter
    def Focal(self, value: float): ...

    @property
    def Focus(self) -> FreeCAD.Vector:
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

    def compute(self, p1: FreeCAD.Vector, p2: FreeCAD.Vector, p3: FreeCAD.Vector, /):
        """
        compute(p1,p2,p3)
        					The three points must lie on a plane parallel to xy plane and must not be collinear
				
        Possible exceptions: (Part.OCCError).
        """


# TopoShapePy.xml
class Shape(FreeCAD.ComplexGeoData):
    """
    This class can be imported.
    TopoShape is the OpenCasCade topological shape wrapper.
    Sub-elements such as vertices, edges or faces are accessible as:
    * Vertex#, where # is in range(1, number of vertices)
    * Edge#, where # is in range(1, number of edges)
    * Face#, where # is in range(1, number of faces)
    """

    def __init__(self, arg1=None, /):
        """
        TopoShape is the OpenCasCade topological shape wrapper.
        Sub-elements such as vertices, edges or faces are accessible as:
        * Vertex#, where # is in range(1, number of vertices)
        * Edge#, where # is in range(1, number of edges)
        * Face#, where # is in range(1, number of faces)
        Possible exceptions: (Part.OCCError).
        """

    @property
    def Area(self) -> float:
        """Total area of the faces of the shape."""

    @property
    def CompSolids(self) -> list[FreeCAD.PyObjectBase]:
        """List of subsequent shapes in this shape."""

    @property
    def Compounds(self) -> list[FreeCAD.PyObjectBase]:
        """List of compounds in this shape."""

    @property
    def Edges(self) -> list[FreeCAD.PyObjectBase]:
        """List of Edges in this shape."""

    @property
    def Faces(self) -> list[FreeCAD.PyObjectBase]:
        """List of faces in this shape."""

    @property
    def Length(self) -> float:
        """Total length of the edges of the shape."""

    @property
    def Orientation(self) -> str:
        """Returns the orientation of the shape."""

    @Orientation.setter
    def Orientation(self, value: str): ...

    @property
    def ShapeType(self) -> str:
        """Returns the type of the shape."""

    @property
    def Shells(self) -> list[FreeCAD.PyObjectBase]:
        """List of subsequent shapes in this shape."""

    @property
    def Solids(self) -> list[FreeCAD.PyObjectBase]:
        """List of subsequent shapes in this shape."""

    @property
    def Vertexes(self) -> list[FreeCAD.PyObjectBase]:
        """List of vertexes in this shape."""

    @property
    def Volume(self) -> float:
        """Total volume of the solids of the shape."""

    @property
    def Wires(self) -> list[FreeCAD.PyObjectBase]:
        """List of wires in this shape."""

    def ancestorsOfType(self, shape: PartModule.Shape, shape_type: type, /) -> list[Part.Shape]:
        """
        ancestorsOfType(shape, shape type) -> list
        For a sub-shape of this shape get its ancestors of a type.
        
        Possible exceptions: (ValueError, Part.OCCError).
        """

    def check(self, runBopCheck: bool = False, /):
        """
        Checks the shape and report errors in the shape structure.
        This is a more detailed check as done in isValid().
        myShape.check(runBopCheck = False)
        if runBopCheck is True, a BOPCheck analysis is also performed.
        Possible exceptions: (ValueError).
        """

    def childShapes(self, cumOri: bool = True, cumLoc: bool = True, /) -> list[PartModule.Compound | PartModule.CompSolid | PartModule.Solid | PartModule.Shell | PartModule.Face | PartModule.Wire | PartModule.Edge | PartModule.Vertex]:
        """
        childShapes([cumOri=True, cumLoc=True]) -> list
        Return a list of sub-shapes that are direct children of this shape.
         * If cumOri is true, the function composes all
           sub-shapes with the orientation of this shape.
         * If cumLoc is true, the function multiplies all
           sub-shapes by the location of this shape, i.e. it applies to
           each sub-shape the transformation that is associated with this shape.
        
        Possible exceptions: (ValueError, Part.OCCError).
        """

    def cleaned(self):
        """
        This creates a cleaned copy of the shape with the triangulation removed.
        This can be useful to reduce file size when exporting as a BREP file.
        Warning: Use the cleaned shape with care because certain algorithms may work incorrectly
        if the shape has no internal triangulation any more.

        Possible exceptions: (TypeError).
        """

    @typing.overload
    def common(self, tool: PartModule.Shape, /) -> PartModule.Shape: ...

    @typing.overload
    def common(self, arg1: PartModule.Shape, tolerance: float, /) -> PartModule.Shape: ...

    @typing.overload
    def common(self, arg1, tolerance: float = 0.0, /) -> PartModule.Shape:
        """
        Intersection of this and a given (list of) topo shape.
        common(tool) -> Shape
          or
        common((tool1,tool2,...),[tolerance=0.0]) -> Shape

        Intersection of this and a given list of topo shapes.

        Supports:
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation (s1 AND (s2 OR s3))
        - Parallelization of Boolean Operations algorithm

        OCC 6.9.0 or later is required.
        Possible exceptions: (Part.OCCError, TypeError).
        """

    def complement(self):
        """
        Computes the complement of the orientation of this shape,
        i.e. reverses the interior/exterior status of boundaries of this shape.
        """

    def copy(self, copyGeom: bool = True, copyMesh: bool = False, /):
        """
        Create a copy of this shape
        copy(copyGeom=True, copyMesh=False) -> Shape
        If copyMesh is True, triangulation contained in original shape will be
        copied along with geometry.
        If copyGeom is False, only topological objects will be copied, while
        geometry and triangulation will be shared with original shape.

        Possible exceptions: (TypeError).
        """

    @typing.overload
    def cut(self, tool: PartModule.Shape, /) -> PartModule.Shape: ...

    @typing.overload
    def cut(self, arg1: PartModule.Shape, tolerance: float, /) -> PartModule.Shape: ...

    @typing.overload
    def cut(self, arg1, tolerance: float = 0.0, /) -> PartModule.Shape:
        """
        Difference of this and a given (list of) topo shape
        cut(tool) -> Shape
          or
        cut((tool1,tool2,...),[tolerance=0.0]) -> Shape

        Substraction of this and a given list of topo shapes.

        Supports:
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation
        - Parallelization of Boolean Operations algorithm

        OCC 6.9.0 or later is required.
        Possible exceptions: (Part.OCCError, TypeError).
        """

    def defeaturing(self, arg1, /):
        """
        Remove a feature defined by supplied faces and return a new shape.
        The parameter is a list of faces.
        Possible exceptions: (Part.OCCError).
        """

    def distToShape(self, Shape_s: PartModule.Shape, /) -> tuple[float, object, object]:
        """
        Find the minimum distance to another shape.
        distToShape(Shape s):  Returns a list of minimum distance and solution point pairs.

        Returned is a tuple of three: (dist, vectors, infos).

        dist is the minimum distance, in mm (float value).

        vectors is a list of pairs of App.Vector. Each pair corresponds to solution.
        Example: [(Vector (2.0, -1.0, 2.0), Vector (2.0, 0.0, 2.0)), (Vector (2.0,
        -1.0, 2.0), Vector (2.0, -1.0, 3.0))] First vector is a point on self, second
        vector is a point on s.

        infos contains additional info on the solutions. It is a list of tuples:
        (topo1, index1, params1, topo2, index2, params2)

            topo1, topo2 are strings identifying type of BREP element: 'Vertex',
            'Edge', or 'Face'.

            index1, index2 are indexes of the elements (zero-based).

            params1, params2 are parameters of internal space of the elements. For
            vertices, params is None. For edges, params is one float, u. For faces,
            params is a tuple (u,v). 
        Possible exceptions: (TypeError).
        """

    def dumpToString(self) -> str:
        """
        Dump information about the shape to a string.
        Possible exceptions: (Part.OCCError).
        """

    def exportBinary(self, arg1: str, /):
        """
        Export the content of this shape in binary format to a file.
        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def exportBrep(self, arg1: str, /): ...

    @typing.overload
    def exportBrep(self, arg1, /):
        """
        Export the content of this shape to an BREP file. BREP is a CasCade native format.
        Possible exceptions: (Part.OCCError, TypeError).
        """

    def exportBrepToString(self) -> str:
        """
        Export the content of this shape to a string in BREP format. BREP is a CasCade native format.
        Possible exceptions: (Part.OCCError).
        """

    def exportIges(self, arg1: str, /):
        """
        Export the content of this shape to an IGES file.
        Possible exceptions: (Part.OCCError).
        """

    def exportStep(self, arg1: str, /):
        """
        Export the content of this shape to an STEP file.
        Possible exceptions: (Part.OCCError).
        """

    def exportStl(self, arg1: str, arg2: float = None, /):
        """
        Export the content of this shape to an STL mesh file.
        Possible exceptions: (Part.OCCError).
        """

    def extrude(self, arg1: FreeCAD.Vector, /) -> PartModule.Compound | PartModule.CompSolid | PartModule.Solid | PartModule.Shell | PartModule.Face | PartModule.Edge:
        """
        Extrude the shape along a direction.
        Possible exceptions: (Part.OCCError).
        """

    def fix(self, working_precision: float, minimum_precision: float, maximum_precision: float, /) -> bool:
        """
        Tries to fix a broken shape. True is returned if the operation succeeded, False otherwise.
        fix(working precision, minimum precision, maximum precision)
        
        Possible exceptions: (RuntimeError).
        """

    def fixTolerance(self, value: float, ShapeType: type = None, /):
        """
        fixTolerance(value, ShapeType=Shape)

                Sets (enforces) tolerances in a shape to the given value
                ShapeType = Vertex : only vertices are set
                ShapeType = Edge   : only edges are set
                ShapeType = Face   : only faces are set
                ShapeType = Wire   : to have edges and their vertices set
                ShapeType = other value : all (vertices,edges,faces) are set
        
        Possible exceptions: (TypeError, Part.OCCError).
        """

    @typing.overload
    def fuse(self, tool: PartModule.Shape, /) -> PartModule.Shape: ...

    @typing.overload
    def fuse(self, arg1: PartModule.Shape, tolerance: float, /) -> PartModule.Shape: ...

    @typing.overload
    def fuse(self, arg1, tolerance: float = 0.0, /) -> PartModule.Shape:
        """
        Union of this and a given (list of) topo shape.
        fuse(tool) -> Shape
          or
        fuse((tool1,tool2,...),[tolerance=0.0]) -> Shape

        Union of this and a given list of topo shapes.

        Supports (OCCT 6.9.0 and above):
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation
        - Parallelization of Boolean Operations algorithm

        Beginning from OCCT 6.8.1 a tolerance value can be specified.
        Possible exceptions: (Part.OCCError, TypeError).
        """

    def generalFuse(self, list_of_other_shapes, fuzzy_value: float = 0.0, /) -> tuple[Part.Shape, list[list[Part.Shape]]]:
        """
        generalFuse(list_of_other_shapes, fuzzy_value = 0.0): Run general fuse algorithm (GFA) between this and given shapes.

        list_of_other_shapes: shapes to run the algorithm against (the list is
        effectively prepended by 'self').

        fuzzy_value: extra tolerance to apply when searching for interferences, in
        addition to tolerances of the input shapes.

        Returns a tuple of 2: (result, map).

        result is a compound containing all the pieces generated by the algorithm
        (e.g., for two spheres, the pieces are three touching solids). Pieces that
        touch share elements.

        map is a list of lists of shapes, providing the info on which children of
        result came from which argument. The length of list is equal to length of
        list_of_other_shapes + 1. First element is a list of pieces that came from
        shape of this, and the rest are those that come from corresponding shapes in
        list_of_other_shapes.
        hint: use isSame method to test shape equality

        Parallelization of Boolean Operations algorithm

        OCC 6.9.0 or later is required.

        Possible exceptions: (TypeError, Part.OCCError).
        """

    def getElement(self, arg1: str, /) -> PartModule.Face | PartModule.Edge | PartModule.Vertex:
        """
        Returns a SubElement
        Possible exceptions: (Part.OCCError).
        """

    def getTolerance(self, mode: int, ShapeType: type = None, /) -> float:
        """
        getTolerance(mode, ShapeType=Shape) -> float

                Determines a tolerance from the ones stored in a shape
                mode = 0 : returns the average value between sub-shapes,
                mode > 0 : returns the maximal found,
                mode < 0 : returns the minimal found.
                ShapeType defines what kinds of sub-shapes to consider:
                Shape (default) : all : Vertex, Edge, Face,
                Vertex : only vertices,
                Edge   : only edges,
                Face   : only faces,
                Shell  : combined Shell + Face, for each face (and containing
                         shell), also checks edge and Vertex
        
        Possible exceptions: (TypeError, Part.OCCError).
        """

    def globalTolerance(self, mode: int, /) -> float:
        """
        globalTolerance(mode) -> float

                Returns the computed tolerance according to the mode
                mode = 0 : average
                mode > 0 : maximal
                mode < 0 : minimal
        
        Possible exceptions: (Part.OCCError).
        """

    def hashCode(self, arg1: int = None, /) -> int:
        """
        This value is computed from the value of the underlying shape reference and the location.
        Orientation is not taken into account.
        """

    def importBinary(self, arg1: str, /):
        """
        Import the content to this shape of a string in BREP format.
        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def importBrep(self, arg1: str, /): ...

    @typing.overload
    def importBrep(self, arg1, /):
        """
        Load the shape from a file in BREP format.
        Possible exceptions: (Part.OCCError, TypeError).
        """

    def importBrepFromString(self, str: str, False_: int = None, /):
        """
        Load the shape from a string that keeps the content in BREP format.
        importBrepFromString(str,False) to not display a progress bar.
        
        Possible exceptions: (Part.OCCError).
        """

    def inTolerance(self, arg1: float, arg2: float, arg3: type = None, /) -> tuple[Part.Shape, ...]:
        """
        inTolerance(value, ShapeType=Shape) -> float

                Determines which shapes have a tolerance within a given interval
                ShapeType is interpreted as in the method getTolerance
        
        Possible exceptions: (TypeError, Part.OCCError).
        """

    def isClosed(self) -> bool:
        """
        Checks if the shape is closed
        If the shape is a shell it returns True if it has no free boundaries (edges).
        If the shape is a wire it returns True if it has no free ends (vertices).
        (Internal and External sub-shepes are ignored in these checks)
        If the shape is an edge it returns True if its vertices are the same.

        Possible exceptions: (RuntimeError).
        """

    def isEqual(self, arg1: PartModule.Shape, /) -> bool:
        """
        Checks if both shapes are equal.
                This means geometry, placement and orientation are equal.
        """

    def isInside(self, App_Vector: FreeCAD.Vector, float: float, Boolean: bool, /) -> bool:
        """
        Checks whether a point is inside or outside the shape.
        isInside(App.Vector, float, Boolean) => Boolean
        The App.Vector is the point you want to check if it's inside or not
        float gives the tolerance
        Boolean indicates if the point lying directly on a face is considered to be inside or not 
        
        Possible exceptions: (Part.OCCError).
        """

    def isNull(self) -> bool:
        """Checks if the shape is null."""

    def isPartner(self, arg1: PartModule.Shape, /) -> bool:
        """
        Checks if both shapes share the same geometry.
                Placement and orientation may differ.
        """

    def isSame(self, arg1: PartModule.Shape, /) -> bool:
        """
        Checks if both shapes share the same geometry
                and placement. Orientation may differ.
        """

    def isValid(self) -> bool:
        """
        Checks if the shape is valid, i.e. neither null, nor empty nor corrupted.
        Possible exceptions: (RuntimeError).
        """

    def limitTolerance(self, tmin: float, tmax: float = 0, ShapeType: type = None, /) -> bool:
        """
        limitTolerance(tmin, tmax=0, ShapeType=Shape)

                Limits tolerances in a shape as follows :
                tmin = tmax -> as fixTolerance (forces)
                tmin = 0   -> maximum tolerance will be tmax
                tmax = 0 or not given (more generally, tmax < tmin) ->
                tmax ignored, minimum will be tmin
                else, maximum will be max and minimum will be min
                ShapeType = Vertex : only vertices are set
                ShapeType = Edge   : only edges are set
                ShapeType = Face   : only faces are set
                ShapeType = Wire   : to have edges and their vertices set
                ShapeType = other value : all (vertices,edges,faces) are set
                Returns True if at least one tolerance of the sub-shape has
                been modified
        
        Possible exceptions: (TypeError, Part.OCCError).
        """

    @typing.overload
    def makeChamfer(self, arg1: float, arg2: float, arg3, /) -> PartModule.Shape: ...

    @typing.overload
    def makeChamfer(self, arg1: float, arg2, /) -> PartModule.Shape:
        """
        Make chamfer.
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @typing.overload
    def makeFillet(self, arg1: float, arg2: float, arg3, /) -> PartModule.Shape: ...

    @typing.overload
    def makeFillet(self, arg1: float, arg2, /) -> PartModule.Shape:
        """
        Make fillet.
        Possible exceptions: (Part.OCCError, TypeError).
        """

    def makeOffset2D(self, offset: float, join: int = None, fill: bool = None, openResult: bool = None, intersection: bool = None) -> Part.Shape:
        """
        makeOffset2D(offset, join = 0, fill = False, openResult = false, intersection =
        false): makes an offset shape (2d offsetting). The function supports keyword
        arguments. Input shape (self) can be edge, wire, face, or a compound of those.

        * offset: distance to expand the shape by. Negative value will shrink the
        shape.

        * join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
        intersection

        * fill: if true, the output is a face filling the space covered by offset. If
        false, the output is a wire.

        * openResult: affects the way open wires are processed. If False, an open wire
        is made. If True, a closed wire is made from a double-sided offset, with rounds
        around open vertices.

        * intersection: affects the way compounds are processed. If False, all children
        are offset independently. If True, and children are edges/wires, the children
        are offset in a collective manner. If compounding is nested, collectiveness
        does not spread across compounds (only direct children of a compound are taken
        collectively).

        Returns: result of offsetting (wire or face or compound of those). Compounding
        structure follows that of source shape.
        """

    def makeOffsetShape(self, offset: float, tolerance: float, inter: bool = None, self_inter: bool = None, offsetMode: int = None, join: int = None, fill: bool = None) -> PartModule.Shape:
        """
        makeOffsetShape(offset, tolerance, inter = False, self_inter = False,
        offsetMode = 0, join = 0, fill = False): makes an offset shape (3d offsetting).
        The function supports keyword arguments.

        * offset: distance to expand the shape by. Negative value will shrink the
        shape.

        * tolerance: precision of approximation.

        * inter: (parameter to OCC routine; not implemented)

        * self_inter: (parameter to OCC routine; not implemented)

        * offsetMode: 0 = skin; 1 = pipe; 2 = recto-verso

        * join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
        intersection

        * fill: if true, offsetting a shell is to yield a solid

        Returns: result of offsetting.
        Possible exceptions: (Part.OCCError).
        """

    def makeParallelProjection(self, shape: PartModule.Shape, dir: FreeCAD.Vector, /) -> PartModule.Shape:
        """
        Parallel projection of an edge or wire on this shape
        makeParallelProjection(shape, dir)
        
        Possible exceptions: (Part.OCCError).
        """

    def makePerspectiveProjection(self, shape: PartModule.Shape, pnt: FreeCAD.Vector, /) -> PartModule.Shape:
        """
        Perspective projection of an edge or wire on this shape
        makePerspectiveProjection(shape, pnt)
        
        Possible exceptions: (Part.OCCError).
        """

    def makeShapeFromMesh(self, arg1: tuple, arg2: float, /):
        """
        Make a compound shape out of mesh data.
        Note: This should be used for rather small meshes only.
        """

    def makeThickness(self, arg1, arg2: float, arg3: float, arg4: bool = None, arg5: bool = None, arg6: int = None, arg7: int = None, /) -> PartModule.Solid:
        """
        makeThickness(List of shapes, Offset (Float), Tolerance (Float)) -> Shape
        A hollowed solid is built from an initial solid and a set of faces on this solid,
        which are to be removed. The remaining faces of the solid become the walls of
        the hollowed solid, their thickness defined at the time of construction.
        Possible exceptions: (Part.OCCError).
        """

    def mirror(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, /) -> PartModule.Shape:
        """
        Mirror this shape on a given plane.
        The plane is given with its base point and its normal direction.
        Possible exceptions: (Part.OCCError).
        """

    def multiFuse(self, arg1, tolerance: float = 0.0, /) -> PartModule.Shape:
        """
        multiFuse((tool1,tool2,...),[tolerance=0.0]) -> Shape

        Union of this and a given list of topo shapes.

        Supports (OCCT 6.9.0 and above):
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation
        - Parallelization of Boolean Operations algorithm

        Beginning from OCCT 6.8.1 a tolerance value can be specified.
        Deprecated: use fuse() instead.
        Possible exceptions: (TypeError, Part.OCCError).
        """

    def nullify(self):
        """
        Destroys the reference to the underlying shape stored in this shape.
        As a result, this shape becomes null.
        """

    def oldFuse(self, arg1: PartModule.Shape, /) -> PartModule.Shape:
        """
        Union of this and a given topo shape (old algorithm).
        Possible exceptions: (Part.OCCError).
        """

    def optimalBoundingBox(self, useTriangulation: bool = True, useShapeTolerance=False, /) -> FreeCAD.BoundBox:
        """
        optimalBoundingBox(useTriangulation = True, useShapeTolerance = False) -> bound box
        
        Possible exceptions: (RuntimeError).
        """

    def overTolerance(self, value: float, ShapeType: type = None, /) -> tuple[Part.Shape, ...]:
        """
        overTolerance(value, ShapeType=Shape) -> float

                Determines which shapes have a tolerance over the given value
                ShapeType is interpreted as in the method getTolerance
        
        Possible exceptions: (TypeError, Part.OCCError).
        """

    def project(self, arg1, /) -> PartModule.Shape:
        """
        Project a list of shapes on this shape
        Possible exceptions: (Part.OCCError).
        """

    def proximity(self, arg1: PartModule.Shape, arg2: float = None, /) -> tuple[object, object]:
        """
        proximity(Shape s): Returns two lists of Face indexes for the Faces involved in the intersection.
        Possible exceptions: (ValueError, Part.OCCError, NotImplementedError).
        """

    def read(self, arg1: str, /):
        """Read in an IGES, STEP or BREP file."""

    def reflectLines(self, ViewDir: FreeCAD.Vector, ViewPos: FreeCAD.Vector, UpDir: FreeCAD.Vector) -> PartModule.Shape:
        """
        Build reflect lines on a shape according to the axes of view.
        Reflect lines are represented by edges in 3d.
        reflectLines(ViewDir, ViewPos, UpDir) -> Shape
        
        Possible exceptions: (Part.OCCError).
        """

    def removeInternalWires(self, arg1: float, /) -> bool:
        """
        Removes internal wires (also holes) from the shape.
        Possible exceptions: (Part.OCCError).
        """

    def removeShape(self, arg1, /):
        """
        Remove a sub-shape and return a new shape.
        The parameter is a list of shapes.
        Possible exceptions: (Part.OCCError).
        """

    def removeSplitter(self) -> PartModule.Shape:
        """
        Removes redundant edges from the B-REP model
        Possible exceptions: (Part.OCCError).
        """

    def replaceShape(self, arg1, /):
        """
        Replace a sub-shape with a new shape and return a new shape.
        The parameter is in the form list of tuples with the two shapes.
        Possible exceptions: (Part.OCCError).
        """

    def reverse(self):
        """Reverses the orientation of this shape."""

    @typing.overload
    def revolve(self, Vector_0_0_0_: FreeCAD.Vector, Vector_0_0_1_: FreeCAD.Vector, arg3: float = None, /) -> PartModule.Compound | PartModule.CompSolid | PartModule.Solid | PartModule.Shell | PartModule.Face | PartModule.Edge: ...

    @typing.overload
    def revolve(self, V_0_0_0_: FreeCAD.Vector, V_0_1_0_: FreeCAD.Vector, arg3: float = None, /) -> PartModule.Compound | PartModule.CompSolid | PartModule.Solid | PartModule.Shell | PartModule.Face | PartModule.Edge:
        """
        Revolve the shape around an Axis to a given degree.
        Part.revolve(Vector(0,0,0),Vector(0,0,1),360) - revolves the shape around the Z Axis 360 degree.

        Hints: Sometimes you want to create a rotation body out of a closed edge or wire.
        Example:
        from FreeCAD import Base
        import Part
        V=Base.Vector

        e=Part.Ellipse()
        s=e.toShape()
        r=s.revolve(V(0,0,0),V(0,1,0), 360)
        Part.show(r)

        However, you may possibly realize some rendering artifacts or that the mesh
        creation seems to hang. This is because this way the surface is created twice.
        Since the curve is a full ellipse it is sufficient to do a rotation of 180 degree
        only, i.e. r=s.revolve(V(0,0,0),V(0,1,0), 180)

        Now when rendering this object you may still see some artifacts at the poles. Now the
        problem seems to be that the meshing algorithm doesn't like to rotate around a point
        where there is no vertex.

        The idea to fix this issue is that you create only half of the ellipse so that its shape
        representation has vertexes at its start and end point.

        from FreeCAD import Base
        import Part
        V=Base.Vector

        e=Part.Ellipse()
        s=e.toShape(e.LastParameter/4,3*e.LastParameter/4)
        r=s.revolve(V(0,0,0),V(0,1,0), 360)
        Part.show(r)
        
        Possible exceptions: (Part.OCCError).
        """

    def rotate(self, Vector_0_0_0_, Vector_0_0_1_, arg3: float, /):
        """
        Apply the rotation (degree) to the current location of this shape
                  Shp.rotate(Vector(0,0,0),Vector(0,0,1),180) - rotate the shape around the Z Axis 180 degrees.
        """

    def scale(self, arg1: float, arg2: FreeCAD.Vector = None, /):
        """
        Apply scaling with point and factor to this shape.
        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def section(self, tool: PartModule.Shape, approximation: bool = False, /) -> PartModule.Shape: ...

    @typing.overload
    def section(self, arg1: PartModule.Shape, tolerance: float, approximation: bool = False, /) -> PartModule.Shape: ...

    @typing.overload
    def section(self, arg1, tolerance: float = 0.0, approximation: bool = False, /) -> PartModule.Shape:
        """
        Section of this with a given (list of) topo shape.
        section(tool,[approximation=False]) -> Shape
          or
        section((tool1,tool2,...),[tolerance=0.0, approximation=False]) -> Shape

        If approximation is True, section edges are approximated to a C1-continuous BSpline curve.

        Section of this and a given list of topo shapes.

        Supports:
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation (s1 AND (s2 OR s3))
        - Parallelization of Boolean Operations algorithm

        OCC 6.9.0 or later is required.
        Possible exceptions: (Part.OCCError, TypeError).
        """

    def sewShape(self):
        """
        Sew the shape if there is a gap.
        Possible exceptions: (Part.OCCError).
        """

    def slice(self, arg1: FreeCAD.Vector, arg2: float, /) -> list[PartModule.Wire]:
        """
        Make single slice of this shape.
        Possible exceptions: (Part.OCCError).
        """

    def slices(self, arg1: FreeCAD.Vector, arg2, /) -> PartModule.Compound:
        """
        Make slices of this shape.
        Possible exceptions: (Part.OCCError).
        """

    def tessellate(self, arg1: float, arg2: bool = None, /) -> tuple[list[FreeCAD.Vector], list[tuple[int, int, int]]]:
        """
        Tessellate the shape and return a list of vertices and face indices
        Possible exceptions: (Part.OCCError).
        """

    def toNurbs(self) -> PartModule.Shape:
        """
        Conversion of the complete geometry of a shape into NURBS geometry.
        For example, all curves supporting edges of the basis shape are converted
        into B-spline curves, and all surfaces supporting its faces are converted
        into B-spline surfaces.
        Possible exceptions: (Part.OCCError).
        """

    def transformGeometry(self, Matrix: FreeCAD.Matrix, /) -> PartModule.Shape:
        """
        Apply geometric transformation on this or a copy the shape.
        This method returns a new shape.
        The transformation to be applied is defined as a 4x4 matrix.
        The underlying geometry of the following shapes may change:
        - a curve which supports an edge of the shape, or
        - a surface which supports a face of the shape;

        For example, a circle may be transformed into an ellipse when
        applying an affinity transformation. It may also happen that
        the circle then is represented as a B-spline curve.

        The transformation is applied to:
        - all the curves which support edges of the shape, and
        - all the surfaces which support faces of the shape.

        Note: If you want to transform a shape without changing the
        underlying geometry then use the methods translate or rotate.

        transformGeometry(Matrix) -> Shape

        Possible exceptions: (Part.OCCError).
        """

    def transformShape(self, Matrix: FreeCAD.Matrix, boolean_copy: bool = False, /):
        """
        Apply transformation on a shape without changing
        the underlying geometry.
        transformShape(Matrix,[boolean copy=False]) -> None
        Possible exceptions: (Part.OCCError).
        """

    def translate(self, arg1, /):
        """
        Apply the translation to the current location of this shape.
        Possible exceptions: (TypeError).
        """

    def writeInventor(self, Mode: int = None, Deviation: float = None, Angle: float = None, FaceColors=None) -> str:
        """Write the mesh in OpenInventor format to a string."""


# ArcOfHyperbolaPy.xml
class ArcOfHyperbola(PartModule.ArcOfConic):
    """
    This class can be imported.
    Describes a portion of an hyperbola
    """

    def __init__(self, arg1: PartModule.Hyperbola, arg2: float, arg3: float, arg4: bool = None, /):
        """
        Describes a portion of an hyperbola
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Hyperbola(self) -> PartModule.Hyperbola:
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


# BSplineCurvePy.xml
class BSplineCurve(PartModule.BoundedCurve):
    """
    This class can be imported.
    Describes a B-Spline curve in 3D space
    """

    def __init__(self):
        """
        Describes a B-Spline curve in 3D space
        Possible exceptions: (TypeError).
        """

    @property
    def Degree(self) -> int:
        """Returns the polynomial degree of this B-Spline curve."""

    @property
    def EndPoint(self) -> FreeCAD.Vector:
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
    def StartPoint(self) -> FreeCAD.Vector:
        """Returns the start point of this B-Spline curve."""

    def __reduce__(self) -> tuple[object, tuple[typing.Callable, typing.Callable, typing.Callable, typing.Callable, object, typing.Callable, typing.Callable]]:
        """
        __reduce__()
        Serialization of Part.BSplineCurve objects
        """

    def approximate(self, Points, DegMax: int = None, Continuity: str = None, Tolerance: float = None, DegMin: int = None, ParamType: str = None, Parameters=None, LengthWeight: float = None, CurvatureWeight: float = None, TorsionWeight: float = None):
        """
        Replaces this B-Spline curve by approximating a set of points.
        					The function accepts keywords as arguments.

        					approximate(Points = list_of_points)

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
                                                Continuity must be C0, C1(with DegMax >= 3) or C2(with DegMax >= 5).

        					Parameters = list of floats : knot sequence of the approximated points.
        					This argument is only used if the weights above are all null.

        					ParamType = string ('Uniform','Centripetal' or 'ChordLength')
        					Parameterization type. Only used if weights and Parameters above aren't specified.

        					Note : Continuity of the spline defaults to C2. However, it may not be applied if
        					it conflicts with other parameters ( especially DegMax ).
				
        Possible exceptions: (Part.OCCError).
        """

    def buildFromPoles(self, arg1, arg2: bool = None, arg3: int = None, arg4: bool = None, /):
        """
        Builds a B-Spline by a list of poles.
				
        Possible exceptions: (Part.OCCError).
        """

    def buildFromPolesMultsKnots(self, poles, mults=None, knots=None, periodic: bool = None, degree: int = None, weights=None, CheckRational: bool = None):
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
    def getCardinalSplineTangents(self, Points, Parameter: float) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def getCardinalSplineTangents(self, Points, Parameters) -> list[FreeCAD.Vector]:
        """Compute the tangents for a Cardinal spline"""

    def getKnot(self, arg1: int, /) -> float:
        """
        Get a knot of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

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

    def getMultiplicity(self, arg1: int, /) -> int:
        """
        Returns the multiplicity of the knot of index
        from the knots table of this B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def getPole(self, arg1: int, /) -> FreeCAD.Vector:
        """
        Get a pole of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def getPoles(self) -> list[FreeCAD.Vector]:
        """
        Get all poles of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def getPolesAndWeights(self) -> list[tuple[float, float, float, float]]:
        """
        Returns the table of poles and weights in homogenous ccordinates.
        Possible exceptions: (Part.OCCError).
        """

    def getResolution(self, arg1: float, /) -> float:
        """
        Computes for this B-Spline curve the parametric tolerance (UTolerance)
        for a given 3D tolerance (Tolerance3D).
        If f(t) is the equation of this B-Spline curve, the parametric tolerance
        ensures that:
        |t1-t0| < UTolerance ===> |f(t1)-f(t0)| < Tolerance3D
        Possible exceptions: (Part.OCCError).
        """

    def getWeight(self, arg1: int, /) -> float:
        """
        Get a weight of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def getWeights(self) -> list[float]:
        """
        Get all weights of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def increaseDegree(self, arg1: int, /):
        """
        increase(Int=Degree)
        Increases the degree of this B-Spline curve to Degree.
        As a result, the poles, weights and multiplicities tables
        are modified; the knots table is not changed. Nothing is
        done if Degree is less than or equal to the current degree.
        """

    def increaseMultiplicity(self, int_start: int, int_end: int, int_mult: int = None, /):
        """
        increaseMultiplicity(int index, int mult)
        				increaseMultiplicity(int start, int end, int mult)
        				Increases multiplicity of knots up to mult.

        				index: the index of a knot to modify (1-based)
        				start, end: index range of knots to modify.
        				If mult is lower or equal to the current multiplicity nothing is done. If mult is higher than the degree the degree is used.
				
        Possible exceptions: (Part.OCCError).
        """

    def incrementMultiplicity(self, int_start: int, int_end: int, int_mult: int, /):
        """
        incrementMultiplicity(int start, int end, int mult)
        				Raises multiplicity of knots by mult.

        				start, end: index range of knots to modify.
				
        Possible exceptions: (Part.OCCError).
        """

    def insertKnot(self, arg1: float, arg2: int = None, arg3: float = None, arg4: bool = None, /):
        """
        insertKnot(u, mult = 1, tol = 0.0)
        				Inserts a knot value in the sequence of knots. If u is an existing knot the
        				multiplicity is increased by mult. 
        Possible exceptions: (Part.OCCError).
        """

    def insertKnots(self, list_of_floats, list_of_ints, tol: float = 0.0, bool_add: bool = True, /):
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

    def interpolate(self, Points, PeriodicFlag: bool = None, Tolerance: float = None, InitialTangent: FreeCAD.Vector = None, FinalTangent: FreeCAD.Vector = None, Tangents=None, TangentFlags=None, Parameters=None, Scale: bool = None):
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

    def join(self, arg1: PartModule.BSplineCurve, /) -> bool:
        """
        Build a new spline by joining this and a second spline.
				
        Possible exceptions: (Part.OCCError).
        """

    def makeC1Continuous(self, tol: float = 1e-6, ang_tol: float = 1e-7, /):
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

    def movePoint(self, U: float, P: FreeCAD.Vector, Index1: int, Index2: int, /) -> tuple[int, int]:
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

    def setKnot(self, arg1: int, arg2: float, arg3: int = None, /):
        """
        Set a knot of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def setKnots(self, arg1, /):
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

    def setOrigin(self, arg1: int, /):
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

    def setPole(self, arg1: int, arg2: FreeCAD.Vector, arg3: float = None, /):
        """
        Modifies this B-Spline curve by assigning P
        to the pole of index Index in the poles table.
        Possible exceptions: (Part.OCCError).
        """

    def setWeight(self, arg1: int, arg2: float, /):
        """
        Set a weight of the B-Spline curve.
        Possible exceptions: (Part.OCCError).
        """

    def toBezier(self) -> list[PartModule.BezierCurve]:
        """
        Build a list of Bezier splines.
				
        Possible exceptions: (Part.OCCError).
        """

    def toBiArcs(self, tolerance: float, /) -> list[PartModule.Geometry]:
        """
        Build a list of arcs and lines to approximate the B-spline.
        					toBiArcs(tolerance) -> list.
				
        Possible exceptions: (Part.OCCError).
        """


# ArcOfParabolaPy.xml
class ArcOfParabola(PartModule.ArcOfConic):
    """
    This class can be imported.
    Describes a portion of an parabola
    """

    def __init__(self, arg1: PartModule.Parabola, arg2: float, arg3: float, arg4: bool = None, /):
        """
        Describes a portion of an parabola
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Focal(self) -> float:
        """The focal length of the parabola."""

    @Focal.setter
    def Focal(self, value: float): ...

    @property
    def Parabola(self) -> PartModule.Parabola:
        """The internal parabola representation"""


# PartFeaturePy.xml
class Feature(FreeCAD.GeoFeature):
    """
    This class can be imported.
    This is the father of all shape object classes
    """

    @property
    def Shape(self) -> Part.Shape:
        """Property TypeId: Part::PropertyPartShape."""

    @Shape.setter
    def Shape(self, value: Part.Shape): ...


# TrimmedCurvePy.xml
class TrimmedCurve(PartModule.BoundedCurve):
    """The abstract class TrimmedCurve is the root class of all trimmed curve objects."""

    def setParameterRange(self, arg1: float = None, arg2: float = None, /):
        """
        Re-trims this curve to the provided parameter range ([Float=First, Float=Last])
                
        Possible exceptions: (Part.OCCError).
        """


# ArcOfCirclePy.xml
class ArcOfCircle(PartModule.ArcOfConic):
    """
    This class can be imported.
    Describes a portion of a circle
    """

    @typing.overload
    def __init__(self, arg1: PartModule.Circle, arg2: float, arg3: float, arg4: bool = None, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, arg3: FreeCAD.Vector, /):
        """
        Describes a portion of a circle
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Circle(self) -> PartModule.Circle:
        """The internal circle representation"""

    @property
    def Radius(self) -> float:
        """The radius of the circle."""

    @Radius.setter
    def Radius(self, value: float): ...


# SpherePy.xml
class Sphere(PartModule.GeometrySurface):
    """
    This class can be imported.
    Describes a sphere in 3D space
    """

    def __init__(self):
        """Describes a sphere in 3D space"""

    @property
    def Area(self) -> float:
        """Compute the area of the sphere."""

    @property
    def Axis(self) -> FreeCAD.Vector:
        """The axis direction of the circle"""

    @Axis.setter
    def Axis(self, value: FreeCAD.Vector): ...

    @property
    def Center(self) -> FreeCAD.Vector:
        """Center of the sphere."""

    @Center.setter
    def Center(self, value: FreeCAD.Vector): ...

    @property
    def Radius(self) -> float:
        """The radius of the sphere."""

    @Radius.setter
    def Radius(self, value: float): ...

    @property
    def Volume(self) -> float:
        """Compute the volume of the sphere."""


# TopoShapeCompoundPy.xml
class Compound(PartModule.Shape):
    """
    This class can be imported.
    Create a compound out of a list of shapes
    """

    def __init__(self, arg1, /):
        """
        Create a compound out of a list of shapes
        Possible exceptions: (Part.OCCError).
        """

    def add(self, arg1: PartModule.Shape, /):
        """
        Add a shape to the compound.
        Possible exceptions: (Part.OCCError).
        """

    def connectEdgesToWires(self, Shared: bool = True, Tolerance: float = 1e-7, /) -> PartModule.Compound:
        """
        Build a compound of wires out of the edges of this compound.
        myCompound.connectEdgesToWires( Shared = True, Tolerance = 1e-7)
        If Shared is True  connection is performed only when adjacent edges share the same vertex.
        If Shared is False connection is performed only when ends of adjacent edges are at distance less than Tolerance.
        Possible exceptions: (Part.OCCError).
        """


# TopoShapeWirePy.xml
class Wire(PartModule.Shape):
    """
    This class can be imported.
    TopoShapeWire is the OpenCasCade topological wire wrapper
    """

    @typing.overload
    def __init__(self, arg1: PartModule.Shape, /): ...

    @typing.overload
    def __init__(self, arg1, /):
        """
        TopoShapeWire is the OpenCasCade topological wire wrapper
        Possible exceptions: (TypeError, Part.OCCError).
        """

    @property
    def CenterOfMass(self) -> FreeCAD.Vector:
        """
        Returns the center of mass of the current system.
        If the gravitational field is uniform, it is the center of gravity.
        The coordinates returned for the center of mass are expressed in the
        absolute Cartesian coordinate system.
        """

    @property
    def Mass(self) -> float:
        """Returns the mass of the current system."""

    @property
    def MatrixOfInertia(self) -> FreeCAD.Matrix:
        """
        Returns the matrix of inertia. It is a symmetrical matrix. 
        The coefficients of the matrix are the quadratic moments of 
        inertia. 

         | Ixx Ixy Ixz 0 | 
         | Ixy Iyy Iyz 0 | 
         | Ixz Iyz Izz 0 | 
         | 0   0   0   1 | 

        The moments of inertia are denoted by Ixx, Iyy, Izz. 
        The products of inertia are denoted by Ixy, Ixz, Iyz. 
        The matrix of inertia is returned in the central coordinate 
        system (G, Gx, Gy, Gz) where G is the centre of mass of the 
        system and Gx, Gy, Gz the directions parallel to the X(1,0,0) 
        Y(0,1,0) Z(0,0,1) directions of the absolute cartesian 
        coordinate system.
        """

    @property
    def OrderedEdges(self) -> list[Part.Shape]:
        """List of ordered edges in this shape."""

    @property
    def OrderedVertexes(self) -> list[Part.Shape]:
        """List of ordered vertexes in this shape."""

    @property
    def PrincipalProperties(self) -> ReturnGetPrincipalPropertiesDict:
        """
        Computes the principal properties of inertia of the current system. 
         There is always a set of axes for which the products 
         of inertia of a geometric system are equal to 0; i.e. the 
         matrix of inertia of the system is diagonal. These axes 
         are the principal axes of inertia. Their origin is 
         coincident with the center of mass of the system. The 
         associated moments are called the principal moments of inertia. 
         This function computes the eigen values and the 
         eigen vectors of the matrix of inertia of the system.
        """

    @property
    def StaticMoments(self) -> tuple[float, float, float]:
        """
        Returns Ix, Iy, Iz, the static moments of inertia of the 
         current system; i.e. the moments of inertia about the 
         three axes of the Cartesian coordinate system.
        """

    def add(self, arg1: PartModule.Shape, /):
        """
        Add an edge to the wire
        Possible exceptions: (TypeError, Part.OCCError).
        """

    def approximate(self, arg1: float, arg2: float, arg3: int, arg4: int, /) -> PartModule.BSplineCurve:
        """
        Approximate B-Spline-curve from this wire
        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def discretize(self, Number, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiNumber, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Distance, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Deflection, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiDeflection, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Number: int, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Distance: float, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Deflection: float, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiNumber: int, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiDeflection: float, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Number: int, First: float = 0.01, Last: float = 100) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Distance: float, First: float = 0.01, Last: float = 100) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Deflection: float, First: float = 0.01, Last: float = 100) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiNumber: int, First: float = 0.01, Last: float = 100) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiDeflection: float, First: float = 0.01, Last: float = 100) -> list[FreeCAD.Vector]:
        """
        Discretizes the wire and returns a list of points.
        The function accepts keywords as argument:
        discretize(Number=n) => gives a list of 'n' equidistant points
        discretize(QuasiNumber=n) => gives a list of 'n' quasi equidistant points (is faster than the method above)
        discretize(Distance=d) => gives a list of equidistant points with distance 'd'
        discretize(Deflection=d) => gives a list of points with a maximum deflection 'd' to the wire
        discretize(QuasiDeflection=d) => gives a list of points with a maximum deflection 'd' to the wire (faster)
        discretize(Angular=a,Curvature=c,[Minimum=m]) => gives a list of points with an angular deflection of 'a'
                                            and a curvature deflection of 'c'. Optionally a minimum number of points
                                            can be set which by default is set to 2.

        Optionally you can set the keywords 'First' and 'Last' to define a sub-range of the parameter range
        of the wire.

        If no keyword is given then it depends on whether the argument is an int or float.
        If it's an int then the behaviour is as if using the keyword 'Number', if it's float
        then the behaviour is as if using the keyword 'Distance'.

        Example:

        import Part
        V=App.Vector

        e1=Part.makeCircle(5,V(0,0,0),V(0,0,1),0,180)
        e2=Part.makeCircle(5,V(10,0,0),V(0,0,1),180,360)
        w=Part.Wire([e1,e2])

        p=w.discretize(Number=50)
        s=Part.Compound([Part.Vertex(i) for i in p])
        Part.show(s)


        p=w.discretize(Angular=0.09,Curvature=0.01,Minimum=100)
        s=Part.Compound([Part.Vertex(i) for i in p])
        Part.show(s)

        Possible exceptions: (TypeError, Part.OCCError).
        """

    def fixWire(self, face: PartModule.Face = None, tolerance: float = None, /):
        """
        Fix wire
        A face and a tolerance can optionally be supplied to the algorithm:
        myWire.fixWire( face, tolerance )

        Possible exceptions: (Part.OCCError).
        """

    def makeHomogenousWires(self, arg1: PartModule.Wire, /) -> PartModule.Wire | object:
        """
        Make this and the given wire homogenous to have the same number of edges
        Possible exceptions: (Part.OCCError).
        """

    def makeOffset(self, arg1: float, /) -> PartModule.Shape:
        """
        Offset the shape by a given amount. DEPRECATED - use makeOffset2D instead.
        Possible exceptions: (Part.OCCError).
        """

    def makePipe(self, arg1: PartModule.Shape, /) -> PartModule.Shape:
        """
        Make a pipe by sweeping along a wire.
        Possible exceptions: (Part.OCCError).
        """

    def makePipeShell(self, shapeList, isSolid: bool = None, isFrenet: bool = None, transition: int = None, /) -> PartModule.Shape:
        """
        makePipeShell(shapeList,[isSolid,isFrenet,transition])
        Make a loft defined by a list of profiles along a wire. Transition can be
        0 (default), 1 (right corners) or 2 (rounded corners).
        Possible exceptions: (Part.OCCError).
        """


# SurfaceOfExtrusionPy.xml
class SurfaceOfExtrusion(PartModule.GeometrySurface):
    """
    This class can be imported.
    Describes a surface of linear extrusion
    """

    def __init__(self, arg1: PartModule.Geometry, arg2: FreeCAD.Vector, /):
        """
        Describes a surface of linear extrusion
        Possible exceptions: (TypeError, Part.OCCError).
        """

    @property
    def BasisCurve(self) -> object:
        """Sets or gets the basic curve."""

    @property
    def Direction(self) -> FreeCAD.Vector:
        """Sets or gets the direction of revolution."""

    def uIso(self, arg1: float, /) -> PartModule.Curve | PartModule.BezierCurve | PartModule.BSplineCurve | PartModule.Line:
        """
        Builds the U isoparametric curve
        Possible exceptions: (Part.OCCError).
        """

    def vIso(self, arg1: float, /) -> PartModule.Curve | PartModule.BezierCurve | PartModule.BSplineCurve | PartModule.Line:
        """
        Builds the V isoparametric curve
        Possible exceptions: (Part.OCCError).
        """


# PointPy.xml
class Point(PartModule.Geometry):
    """
    This class can be imported.
    Describes a point
    To create a point there are several ways:
    Part.Point()
        Creates a default point

    Part.Point(Point)
        Creates a copy of the given point

    Part.Point(Vector)
        Creates a line for the given coordinates
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Point: PartModule.Point, /): ...

    @typing.overload
    def __init__(self, Point: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, Vector: PartModule.Point, /): ...

    @typing.overload
    def __init__(self, Vector: FreeCAD.Vector, /):
        """
        Describes a point
        To create a point there are several ways:
        Part.Point()
            Creates a default point

        Part.Point(Point)
            Creates a copy of the given point

        Part.Point(Vector)
            Creates a line for the given coordinates
        Possible exceptions: (TypeError).
        """

    @property
    def X(self) -> float:
        """X component of this point."""

    @X.setter
    def X(self, value: float): ...

    @property
    def Y(self) -> float:
        """Y component of this point."""

    @Y.setter
    def Y(self, value: float): ...

    @property
    def Z(self) -> float:
        """Z component of this point."""

    @Z.setter
    def Z(self, value: float): ...

    def toShape(self) -> PartModule.Vertex:
        """
        Create a vertex from this point.
        Possible exceptions: (Part.OCCError).
        """


# TopoShapeShellPy.xml
class Shell(PartModule.Shape):
    """
    This class can be imported.
    Create a shell out of a list of faces
    """

    def __init__(self, arg1, /):
        """
        Create a shell out of a list of faces
        Possible exceptions: (Part.OCCError).
        """

    @property
    def CenterOfMass(self) -> FreeCAD.Vector:
        """
        Returns the center of mass of the current system.
        If the gravitational field is uniform, it is the center of gravity.
        The coordinates returned for the center of mass are expressed in the
        absolute Cartesian coordinate system.
        """

    @property
    def Mass(self) -> float:
        """Returns the mass of the current system."""

    @property
    def MatrixOfInertia(self) -> FreeCAD.Matrix:
        """
        Returns the matrix of inertia. It is a symmetrical matrix. 
        The coefficients of the matrix are the quadratic moments of 
        inertia. 

         | Ixx Ixy Ixz 0 | 
         | Ixy Iyy Iyz 0 | 
         | Ixz Iyz Izz 0 | 
         | 0   0   0   1 | 

        The moments of inertia are denoted by Ixx, Iyy, Izz. 
        The products of inertia are denoted by Ixy, Ixz, Iyz. 
        The matrix of inertia is returned in the central coordinate 
        system (G, Gx, Gy, Gz) where G is the centre of mass of the 
        system and Gx, Gy, Gz the directions parallel to the X(1,0,0) 
        Y(0,1,0) Z(0,0,1) directions of the absolute cartesian 
        coordinate system.
        """

    @property
    def PrincipalProperties(self) -> ReturnGetPrincipalPropertiesDict:
        """
        Computes the principal properties of inertia of the current system. 
         There is always a set of axes for which the products 
         of inertia of a geometric system are equal to 0; i.e. the 
         matrix of inertia of the system is diagonal. These axes 
         are the principal axes of inertia. Their origin is 
         coincident with the center of mass of the system. The 
         associated moments are called the principal moments of inertia. 
         This function computes the eigen values and the 
         eigen vectors of the matrix of inertia of the system.
        """

    @property
    def StaticMoments(self) -> tuple[float, float, float]:
        """
        Returns Ix, Iy, Iz, the static moments of inertia of the 
         current system; i.e. the moments of inertia about the 
         three axes of the Cartesian coordinate system.
        """

    def add(self, arg1: PartModule.Face, /):
        """
        Add a face to the shell.
        Possible exceptions: (Part.OCCError).
        """

    def getBadEdges(self) -> PartModule.Compound:
        """Get bad edges as compound."""

    def getFreeEdges(self) -> PartModule.Compound:
        """Get free edges as compound."""

    def makeHalfSpace(self, arg1: FreeCAD.Vector, /) -> PartModule.Solid:
        """
        Make a half-space solid by this shell and a reference point.
        Possible exceptions: (Part.OCCError).
        """


# ConicPy.xml
class Conic(PartModule.Curve):
    """
    This class can be imported.
    Describes an abstract conic in 3d space
    """

    @property
    def AngleXU(self) -> float:
        """The angle between the X axis and the major axis of the conic."""

    @AngleXU.setter
    def AngleXU(self, value: float): ...

    @property
    def Axis(self) -> FreeCAD.Vector:
        """The axis direction of the circle"""

    @Axis.setter
    def Axis(self, value: FreeCAD.Vector): ...

    @property
    def Center(self) -> FreeCAD.Vector:
        """Deprecated -- use Location."""

    @Center.setter
    def Center(self, value: FreeCAD.Vector): ...

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
    def Location(self) -> FreeCAD.Vector:
        """Location of the conic."""

    @Location.setter
    def Location(self, value: FreeCAD.Vector): ...

    @property
    def XAxis(self) -> FreeCAD.Vector:
        """The X axis direction of the circle"""

    @XAxis.setter
    def XAxis(self, value: FreeCAD.Vector): ...

    @property
    def YAxis(self) -> FreeCAD.Vector:
        """The Y axis direction of the circle"""

    @YAxis.setter
    def YAxis(self, value: FreeCAD.Vector): ...


# BSplineSurfacePy.xml
class BSplineSurface(PartModule.GeometrySurface):
    """
    This class can be imported.
    Describes a B-Spline surface in 3D space
    """

    @property
    def FirstUKnotIndex(self) -> int:
        """
        Returns the index in the knot array associated with the u parametric direction,
        					which corresponds to the first parameter of this B-Spline surface in the specified
        					parametric direction.

        					The isoparametric curves corresponding to these values are the boundary curves of
        					this surface.

        					Note: The index does not correspond to the first knot of the surface in the specified
        					parametric direction unless the multiplicity of the first knot is equal to Degree + 1,
        					where Degree is the degree of this surface in the corresponding parametric direction.
        """

    @property
    def FirstVKnotIndex(self) -> int:
        """
        Returns the index in the knot array associated with the v parametric direction,
        					which corresponds to the first parameter of this B-Spline surface in the specified
        					parametric direction.

        					The isoparametric curves corresponding to these values are the boundary curves of
        					this surface.

        					Note: The index does not correspond to the first knot of the surface in the specified
        					parametric direction unless the multiplicity of the first knot is equal to Degree + 1,
        					where Degree is the degree of this surface in the corresponding parametric direction.
        """

    @property
    def LastUKnotIndex(self) -> int:
        """
        Returns the index in the knot array associated with the u parametric direction,
        					which corresponds to the last parameter of this B-Spline surface in the specified
        					parametric direction.

        					The isoparametric curves corresponding to these values are the boundary curves of
        					this surface.

        					Note: The index does not correspond to the first knot of the surface in the specified
        					parametric direction unless the multiplicity of the last knot is equal to Degree + 1,
        					where Degree is the degree of this surface in the corresponding parametric direction.
        """

    @property
    def LastVKnotIndex(self) -> int:
        """
        Returns the index in the knot array associated with the v parametric direction,
        					which corresponds to the last parameter of this B-Spline surface in the specified
        					parametric direction.

        					The isoparametric curves corresponding to these values are the boundary curves of
        					this surface.

        					Note: The index does not correspond to the first knot of the surface in the specified
        					parametric direction unless the multiplicity of the last knot is equal to Degree + 1,
        					where Degree is the degree of this surface in the corresponding parametric direction.
        """

    @property
    def MaxDegree(self) -> int:
        """
        Returns the value of the maximum polynomial degree of any
        					B-Spline surface surface in either parametric directions.
        					This value is 25.
        """

    @property
    def NbUKnots(self) -> int:
        """Returns the number of knots of this B-Spline surface in the u parametric direction."""

    @property
    def NbUPoles(self) -> int:
        """Returns the number of poles of this B-Spline surface in the u parametric direction."""

    @property
    def NbVKnots(self) -> int:
        """Returns the number of knots of this B-Spline surface in the v parametric direction."""

    @property
    def NbVPoles(self) -> int:
        """Returns the number of poles of this B-Spline surface in the v parametric direction."""

    @property
    def UDegree(self) -> int:
        """Returns the degree of this B-Spline surface in the u parametric direction."""

    @property
    def UKnotSequence(self) -> list[float]:
        """
        Returns the knots sequence of this B-Spline surface in
        						the u direction.
        """

    @property
    def VDegree(self) -> int:
        """Returns the degree of this B-Spline surface in the v parametric direction."""

    @property
    def VKnotSequence(self) -> list[float]:
        """
        Returns the knots sequence of this B-Spline surface in
        					the v direction.
        """

    def approximate(self, Points, DegMin: int = None, DegMax: int = None, Continuity: int = None, Tolerance: float = None, X0: float = None, dX: float = None, Y0: float = None, dY: float = None, ParamType: str = None, LengthWeight: float = None, CurvatureWeight: float = None, TorsionWeight: float = None):
        """
        Replaces this B-Spline surface by approximating a set of points.
        					This method uses keywords :
        					- Points = 2Darray of points (or floats, in combination with X0, dX, Y0, dY)
        					- DegMin (int), DegMax (int)
        					- Continuity = 0,1 or 2 (for C0, C1, C2)
        					- Tolerance (float)
        					- X0, dX, Y0, dY (floats) with Points = 2Darray of floats
        					- ParamType = 'Uniform','Centripetal' or 'ChordLength'
        					- LengthWeight, CurvatureWeight, TorsionWeight (floats)
        					(with this smoothing algorithm, continuity C1 requires DegMax >= 3 and C2, DegMax >=5)
					
        					Possible combinations :
        					- approximate(Points, DegMin, DegMax, Continuity, Tolerance)
        					- approximate(Points, DegMin, DegMax, Continuity, Tolerance, X0, dX, Y0, dY)
        					With explicit keywords :
        					- approximate(Points, DegMin, DegMax, Continuity, Tolerance, ParamType)
        					- approximate(Points, DegMax, Continuity, Tolerance, LengthWeight, CurvatureWeight, TorsionWeight)
				
        Possible exceptions: (Part.OCCError).
        """

    def bounds(self) -> tuple[float, float, float, float]:
        """Returns the parametric bounds (U1, U2, V1, V2) of this B-Spline surface."""

    def buildFromPolesMultsKnots(self, poles, umults, vmults, uknots=None, vknots=None, uperiodic: bool = None, vperiodic: bool = None, udegree: int = None, vdegree: int = None, weights=None):
        """
        Builds a B-Spline by a lists of Poles, Mults and Knots
        					arguments: poles (sequence of sequence of Base.Vector), umults, vmults, [uknots, vknots, uperiodic, vperiodic, udegree, vdegree, weights (sequence of sequence of float)]
				
        Possible exceptions: (Part.OCCError).
        """

    def exchangeUV(self):
        """
        Exchanges the u and v parametric directions on this B-Spline surface.
        					As a consequence:
        					-- the poles and weights tables are transposed,
        					-- the knots and multiplicities tables are exchanged,
        					-- degrees of continuity and rational, periodic and uniform
        					   characteristics are exchanged and
        					-- the orientation of the surface is reversed.
        """

    def getPole(self, arg1: int, arg2: int, /) -> FreeCAD.Vector:
        """
        Returns the pole of index (UIndex,VIndex) of this B-Spline surface.
				
        Possible exceptions: (Part.OCCError).
        """

    def getPoles(self) -> list[list[FreeCAD.Vector]]:
        """
        Returns the table of poles of this B-Spline surface.
        Possible exceptions: (Part.OCCError).
        """

    def getPolesAndWeights(self) -> list[list[tuple[float, float, float, float]]]:
        """
        Returns the table of poles and weights in homogenous ccordinates.
        Possible exceptions: (Part.OCCError).
        """

    def getResolution(self, arg1: float, /) -> tuple[float, float]:
        """
        Computes two tolerance values for this B-Spline surface, based on the
        					given tolerance in 3D space Tolerance3D. The tolerances computed are:
        					-- UTolerance in the u parametric direction and
        					-- VTolerance in the v parametric direction.

        					If f(u,v) is the equation of this B-Spline surface, UTolerance and
        					VTolerance guarantee that:
        					|u1 - u0| < UTolerance
        					|v1 - v0| < VTolerance
        					====> ||f(u1, v1) - f(u2, v2)|| < Tolerance3D
				
        Possible exceptions: (Part.OCCError).
        """

    def getUKnot(self, arg1: int, /) -> float:
        """
        Returns, for this B-Spline surface, in the u parametric direction
        					the knot of index UIndex of the knots table.
        """

    def getUKnots(self) -> list[float]:
        """
        Returns, for this B-Spline surface, the knots table
        					in the u parametric direction
				
        Possible exceptions: (Part.OCCError).
        """

    def getUMultiplicities(self) -> list[int]:
        """
        Returns, for this B-Spline surface, the table of
        					multiplicities in the u parametric direction
				
        Possible exceptions: (Part.OCCError).
        """

    def getUMultiplicity(self, arg1: int, /) -> int:
        """
        Returns, for this B-Spline surface, the multiplicity of
        					the knot of index UIndex in the u parametric direction.
				
        Possible exceptions: (Part.OCCError).
        """

    def getVKnot(self, arg1: int, /) -> float:
        """
        Returns, for this B-Spline surface, in the v parametric direction
        					the knot of index VIndex of the knots table.
        """

    def getVKnots(self) -> list[float]:
        """
        Returns, for this B-Spline surface, the knots table
        					in the v parametric direction
				
        Possible exceptions: (Part.OCCError).
        """

    def getVMultiplicities(self) -> list[int]:
        """
        Returns, for this B-Spline surface, the table of
        					multiplicities in the v parametric direction
				
        Possible exceptions: (Part.OCCError).
        """

    def getVMultiplicity(self, arg1: int, /) -> int:
        """
        Returns, for this B-Spline surface, the multiplicity of
        					the knot of index VIndex in the v parametric direction.
				
        Possible exceptions: (Part.OCCError).
        """

    def getWeight(self, arg1: int, arg2: int, /) -> float:
        """
        Return the weight of the pole of index (UIndex,VIndex)
        					in the poles table for this B-Spline surface.
				
        Possible exceptions: (Part.OCCError).
        """

    def getWeights(self) -> list[list[float]]:
        """
        Returns the table of weights of the poles for this B-Spline surface.
        Possible exceptions: (Part.OCCError).
        """

    def increaseDegree(self, arg1: int, arg2: int, /):
        """
        increase(Int=UDegree, int=VDegree)
        					Increases the degrees of this B-Spline surface to UDegree and VDegree
        					in the u and v parametric directions respectively.
        					As a result, the tables of poles, weights and multiplicities are modified.
        					The tables of knots is not changed.

        					Note: Nothing is done if the given degree is less than or equal to the
        					current degree in the corresponding parametric direction.
        """

    def increaseUMultiplicity(self, arg1: int, arg2: int, arg3: int = None, /):
        """Increases the multiplicity in the u direction."""

    def increaseVMultiplicity(self, arg1: int, arg2: int, arg3: int = None, /):
        """Increases the multiplicity in the v direction."""

    def incrementUMultiplicity(self, arg1: int, arg2: int, arg3: int, /):
        """
        Increment the multiplicity in the u direction
        Possible exceptions: (Part.OCCError).
        """

    def incrementVMultiplicity(self, arg1: int, arg2: int, arg3: int, /):
        """
        Increment the multiplicity in the v direction
        Possible exceptions: (Part.OCCError).
        """

    def insertUKnot(self, arg1: float, arg2: int, arg3: float, arg4: bool = None, /):
        """
        insertUKnote(float U, int Index, float Tolerance) - Insert or override a knot
        Possible exceptions: (Part.OCCError).
        """

    def insertUKnots(self, arg1, arg2, arg3: float = None, arg4: bool = None, /):
        """
        insertUKnote(List of float U, List of float Mult, float Tolerance) - Inserts knots.
        Possible exceptions: (Part.OCCError).
        """

    def insertVKnot(self, arg1: float, arg2: int, arg3: float, arg4: bool = None, /):
        """
        insertUKnote(float V, int Index, float Tolerance) - Insert or override a knot.
        Possible exceptions: (Part.OCCError).
        """

    def insertVKnots(self, arg1, arg2, arg3: float = None, arg4: bool = None, /):
        """
        insertUKnote(List of float V, List of float Mult, float Tolerance) - Inserts knots.
        Possible exceptions: (Part.OCCError).
        """

    def interpolate(self, zpoints, X0: float = None, dX: float = None, Y0: float = None, dY: float = None, /):
        """
        interpolate(points)
        					interpolate(zpoints, X0, dX, Y0, dY)
					
        					Replaces this B-Spline surface by interpolating a set of points.
        					The resulting surface is of degree 3 and continuity C2.
        					Arguments:
        					a 2 dimensional array of vectors, that the surface passes through
        					or
        					a 2 dimensional array of floats with the z values,
        					the x starting point X0 (float),
        					the x increment dX (float),
        					the y starting point Y0 and increment dY
				
        Possible exceptions: (Part.OCCError).
        """

    def isUClosed(self) -> bool:
        """
        Checks if this surface is closed in the u parametric direction.
        					Returns true if, in the table of poles the first row and the last
        					row are identical.
        """

    def isUPeriodic(self) -> bool:
        """Returns true if this surface is periodic in the u parametric direction."""

    def isURational(self) -> bool:
        """
        Returns false if the equation of this B-Spline surface is polynomial
        					(e.g. non-rational) in the u or v parametric direction.
        					In other words, returns false if for each row of poles, the associated
        					weights are identical
        """

    def isVClosed(self) -> bool:
        """
        Checks if this surface is closed in the v parametric direction.
        					Returns true if, in the table of poles the first column and the
        					last column are identical.
        """

    def isVPeriodic(self) -> bool:
        """Returns true if this surface is periodic in the v parametric direction."""

    def isVRational(self) -> bool:
        """
        Returns false if the equation of this B-Spline surface is polynomial
        					(e.g. non-rational) in the u or v parametric direction.
        					In other words, returns false if for each column of poles, the associated
        					weights are identical
        """

    def movePoint(self, arg1: float, arg2: float, arg3: FreeCAD.Vector, arg4: int, arg5: int, arg6: int, arg7: int, /) -> tuple[int, int, int, int]:
        """
        Moves the point of parameters (U, V) of this B-Spline surface to P.
        					UIndex1, UIndex2, VIndex1 and VIndex2 are the indexes in the poles
        					table of this B-Spline surface, of the first and last poles which
        					can be moved in each parametric direction.
        					The returned indexes UFirstIndex, ULastIndex, VFirstIndex and
        					VLastIndex are the indexes of the first and last poles effectively
        					modified in each parametric direction.
        					In the event of incompatibility between UIndex1, UIndex2, VIndex1,
        					VIndex2 and the values U and V:
        					-- no change is made to this B-Spline surface, and
        					-- UFirstIndex, ULastIndex, VFirstIndex and VLastIndex are set to
        					   null.
				
        Possible exceptions: (Part.OCCError).
        """

    def removeUKnot(self, arg1: int, arg2: int, arg3: float, /) -> bool:
        """
        Reduces to M the multiplicity of the knot of index Index in the given
        				parametric direction. If M is 0, the knot is removed.
        				With a modification of this type, the table of poles is also modified.
        				Two different algorithms are used systematically to compute the new
        				poles of the surface. For each pole, the distance between the pole
        				calculated using the first algorithm and the same pole calculated using
        				the second algorithm, is checked. If this distance is less than Tolerance
        				it ensures that the surface is not modified by more than Tolerance.
        				Under these conditions, the function returns true; otherwise, it returns
        				false.

        				A low tolerance prevents modification of the surface. A high tolerance
        				'smoothes' the surface.
				
        Possible exceptions: (Part.OCCError).
        """

    def removeVKnot(self, arg1: int, arg2: int, arg3: float, /) -> bool:
        """
        Reduces to M the multiplicity of the knot of index Index in the given
        				parametric direction. If M is 0, the knot is removed.
        				With a modification of this type, the table of poles is also modified.
        				Two different algorithms are used systematically to compute the new
        				poles of the surface. For each pole, the distance between the pole
        				calculated using the first algorithm and the same pole calculated using
        				the second algorithm, is checked. If this distance is less than Tolerance
        				it ensures that the surface is not modified by more than Tolerance.
        				Under these conditions, the function returns true; otherwise, it returns
        				false.

        				A low tolerance prevents modification of the surface. A high tolerance
        				'smoothes' the surface.
				
        Possible exceptions: (Part.OCCError).
        """

    def reparametrize(self, arg1: int, arg2: int, arg3: float = None, /) -> PartModule.BSplineSurface:
        """
        Returns a reparametrized copy of this surface
        Possible exceptions: (Part.OCCError).
        """

    def segment(self, arg1: float, arg2: float, arg3: float, arg4: float, /):
        """
        Modifies this B-Spline surface by segmenting it between U1 and U2 in the
        					u parametric direction and between V1 and V2 in the v parametric direction.
        					Any of these values can be outside the bounds of this surface, but U2 must
        					be greater than U1 and V2 must be greater than V1.

        					All the data structure tables of this B-Spline surface are modified but the
        					knots located between U1 and U2 in the u parametric direction, and between
        					V1 and V2 in the v parametric direction are retained.
        					The degree of the surface in each parametric direction is not modified.
				
        Possible exceptions: (Part.OCCError).
        """

    def setPole(self, arg1: int, arg2: int, arg3: FreeCAD.Vector, arg4: float = None, /):
        """
        Modifies this B-Spline surface by assigning P to the pole of
        					index (UIndex, VIndex) in the poles table.
        					The second syntax allows you also to change the weight of the
        					modified pole. The weight is set to Weight. This syntax must
        					only be used for rational surfaces.
        					Modifies this B-Spline curve by assigning P to the pole of
        					index Index in the poles table.
				
        Possible exceptions: (Part.OCCError).
        """

    def setPoleCol(self, arg1: int, arg2, arg3=None, /):
        """
        Modifies this B-Spline surface by assigning values to all or part
        					of the column of poles of index VIndex, of this B-Spline surface.
        					You can also change the weights of the modified poles. The weights
        					are set to the corresponding values of CPoleWeights.
        					These syntaxes must only be used for rational surfaces.
				
        Possible exceptions: (Part.OCCError).
        """

    def setPoleRow(self, arg1: int, arg2, arg3=None, /):
        """
        Modifies this B-Spline surface by assigning values to all or part
        					of the row of poles of index VIndex, of this B-Spline surface.
        					You can also change the weights of the modified poles. The weights
        					are set to the corresponding values of CPoleWeights.
        					These syntaxes must only be used for rational surfaces.
				
        Possible exceptions: (Part.OCCError).
        """

    def setUKnot(self, arg1: int, arg2: float, arg3: int = None, /):
        """
        Modifies this B-Spline surface by assigning the value K to the knot of index
        					UIndex of the knots table corresponding to the u parametric direction.
        					This modification remains relatively local, since K must lie between the values
        					of the knots which frame the modified knot.

        					You can also increase the multiplicity of the modified knot to M. Note however
        					that it is not possible to decrease the multiplicity of a knot with this function.
        """

    def setUKnots(self, arg1, /):
        """
        Changes all knots of this B-Spline surface in the u parametric
        					direction. The multiplicity of the knots is not modified.
				
        Possible exceptions: (Part.OCCError).
        """

    def setUNotPeriodic(self):
        """
        Changes this B-Spline surface into a non-periodic one in the u parametric direction.
        					If this B-Spline surface is already non-periodic in the given parametric direction,
        					it is not modified.
        					If this B-Spline surface is periodic in the given parametric direction, the boundaries
        					of the surface are not given by the first and last rows (or columns) of poles (because
        					the multiplicity of the first knot and of the last knot in the given parametric direction
        					are not modified, nor are they equal to Degree+1, where Degree is the degree of this
        					B-Spline surface in the given parametric direction). Only the function Segment ensures
        					this property.

        					Note: the poles and knots tables are modified.
				
        Possible exceptions: (Part.OCCError).
        """

    def setUOrigin(self, arg1: int, /):
        """
        Assigns the knot of index Index in the knots table
        					in the u parametric direction to be the origin of
        					this periodic B-Spline surface. As a consequence,
        					the knots and poles tables are modified.
				
        Possible exceptions: (Part.OCCError).
        """

    def setUPeriodic(self):
        """
        Modifies this surface to be periodic in the u parametric direction.
        					To become periodic in a given parametric direction a surface must
        					be closed in that parametric direction, and the knot sequence relative
        					to that direction must be periodic.
        					To generate this periodic sequence of knots, the functions FirstUKnotIndex
        					and LastUKnotIndex are used to compute I1 and I2. These are the indexes,
        					in the knot array associated with the given parametric direction, of the
        					knots that correspond to the first and last parameters of this B-Spline
        					surface in the given parametric direction. Hence the period is:

        					Knots(I1) - Knots(I2)

        					As a result, the knots and poles tables are modified.
				
        Possible exceptions: (Part.OCCError).
        """

    def setVKnot(self, arg1: int, arg2: float, arg3: int = None, /):
        """
        Modifies this B-Spline surface by assigning the value K to the knot of index
        					VIndex of the knots table corresponding to the v parametric direction.
        					This modification remains relatively local, since K must lie between the values
        					of the knots which frame the modified knot.

        					You can also increase the multiplicity of the modified knot to M. Note however
        					that it is not possible to decrease the multiplicity of a knot with this function.
        """

    def setVKnots(self, arg1, /):
        """
        Changes all knots of this B-Spline surface in the v parametric
        					direction. The multiplicity of the knots is not modified.
				
        Possible exceptions: (Part.OCCError).
        """

    def setVNotPeriodic(self):
        """
        Changes this B-Spline surface into a non-periodic one in the v parametric direction.
        					If this B-Spline surface is already non-periodic in the given parametric direction,
        					it is not modified.
        					If this B-Spline surface is periodic in the given parametric direction, the boundaries
        					of the surface are not given by the first and last rows (or columns) of poles (because
        					the multiplicity of the first knot and of the last knot in the given parametric direction
        					are not modified, nor are they equal to Degree+1, where Degree is the degree of this
        					B-Spline surface in the given parametric direction). Only the function Segment ensures
        					this property.

        					Note: the poles and knots tables are modified.
				
        Possible exceptions: (Part.OCCError).
        """

    def setVOrigin(self, arg1: int, /):
        """
        Assigns the knot of index Index in the knots table
        					in the v parametric direction to be the origin of
        					this periodic B-Spline surface. As a consequence,
        					the knots and poles tables are modified.
				
        Possible exceptions: (Part.OCCError).
        """

    def setVPeriodic(self):
        """
        Modifies this surface to be periodic in the v parametric direction.
        					To become periodic in a given parametric direction a surface must
        					be closed in that parametric direction, and the knot sequence relative
        					to that direction must be periodic.
        					To generate this periodic sequence of knots, the functions FirstUKnotIndex
        					and LastUKnotIndex are used to compute I1 and I2. These are the indexes,
        					in the knot array associated with the given parametric direction, of the
        					knots that correspond to the first and last parameters of this B-Spline
        					surface in the given parametric direction. Hence the period is:

        					Knots(I1) - Knots(I2)

        					As a result, the knots and poles tables are modified.
				
        Possible exceptions: (Part.OCCError).
        """

    def setWeight(self, arg1: int, arg2: int, arg3: float, /):
        """
        Modifies this B-Spline surface by assigning the value Weight to the weight
        					of the pole of index (UIndex, VIndex) in the poles tables of this B-Spline
        					surface.

        					This function must only be used for rational surfaces.
				
        Possible exceptions: (Part.OCCError).
        """

    def setWeightCol(self, arg1: int, arg2, /):
        """
        Modifies this B-Spline surface by assigning values to all or part of the
        					weights of the column of poles of index VIndex of this B-Spline surface.

        					The modified part of the column of weights is defined by the bounds
        					of the array CPoleWeights.

        					This function must only be used for rational surfaces.
				
        Possible exceptions: (Part.OCCError).
        """

    def setWeightRow(self, arg1: int, arg2, /):
        """
        Modifies this B-Spline surface by assigning values to all or part of the
        					weights of the row of poles of index UIndex of this B-Spline surface.

        					The modified part of the row of weights is defined by the bounds of the
        					array CPoleWeights.

        					This function must only be used for rational surfaces.
				
        Possible exceptions: (Part.OCCError).
        """

    def uIso(self, arg1: float, /) -> PartModule.BSplineCurve:
        """
        Builds the U isoparametric B-Spline curve of this B-Spline surface
        Possible exceptions: (Part.OCCError).
        """

    def vIso(self, arg1: float, /) -> PartModule.BSplineCurve:
        """
        Builds the V isoparametric B-Spline curve of this B-Spline surface
        Possible exceptions: (Part.OCCError).
        """


# RectangularTrimmedSurfacePy.xml
class RectangularTrimmedSurface(PartModule.GeometrySurface):
    """
    This class can be imported.
    Describes a portion of a surface (a patch) limited by two values of the
    u parameter in the u parametric direction, and two values of the v parameter in the v parametric
    direction. The domain of the trimmed surface must be within the domain of the surface being trimmed.

    The trimmed surface is defined by:
    - the basis surface, and
    - the values (umin, umax) and (vmin, vmax) which limit it in the u and v parametric directions.

    The trimmed surface is built from a copy of the basis surface. Therefore, when the basis surface
    is modified the trimmed surface is not changed. Consequently, the trimmed surface does not
    necessarily have the same orientation as the basis surface.
    """

    @typing.overload
    def __init__(self, arg1: PartModule.GeometrySurface, arg2: float, arg3: float, arg4: float, arg5: float, arg6: bool = None, arg7: bool = None, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.GeometrySurface, arg2: float, arg3: float, arg4: bool, arg5: bool = None, /):
        """
        Describes a portion of a surface (a patch) limited by two values of the
        u parameter in the u parametric direction, and two values of the v parameter in the v parametric
        direction. The domain of the trimmed surface must be within the domain of the surface being trimmed.

        The trimmed surface is defined by:
        - the basis surface, and
        - the values (umin, umax) and (vmin, vmax) which limit it in the u and v parametric directions.

        The trimmed surface is built from a copy of the basis surface. Therefore, when the basis surface
        is modified the trimmed surface is not changed. Consequently, the trimmed surface does not
        necessarily have the same orientation as the basis surface.
        Possible exceptions: (Part.OCCError).
        """

    def uIso(self, arg1: float, /) -> PartModule.Curve:
        """
        Builds the U isoparametric curve
        Possible exceptions: (Part.OCCError).
        """

    def vIso(self, arg1: float, /) -> PartModule.Curve:
        """
        Builds the V isoparametric curve
        Possible exceptions: (Part.OCCError).
        """


# LinePy.xml
class Line(PartModule.Curve):
    """
    This class can be imported.
    Describes an infinite line
    To create a line there are several ways:
    Part.Line()
        Creates a default line

    Part.Line(Line)
        Creates a copy of the given line

    Part.Line(Point1,Point2)
        Creates a line that goes through two given points
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Line: PartModule.Line, /): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, /):
        """
        Describes an infinite line
        To create a line there are several ways:
        Part.Line()
            Creates a default line

        Part.Line(Line)
            Creates a copy of the given line

        Part.Line(Point1,Point2)
            Creates a line that goes through two given points
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Direction(self) -> FreeCAD.Vector:
        """Returns the direction of this line."""

    @Direction.setter
    def Direction(self, value: FreeCAD.Vector): ...

    @property
    def Location(self) -> FreeCAD.Vector:
        """Returns the location of this line."""

    @Location.setter
    def Location(self, value: FreeCAD.Vector): ...


# GeometrySurfacePy.xml
class GeometrySurface(PartModule.Geometry):
    """The abstract class GeometrySurface is the root class of all surface objects."""

    @property
    def Continuity(self) -> str:
        """Returns the global continuity of the surface."""

    def UPeriod(self) -> float:
        """
        Returns the period of this patch in the u parametric direction.
				
        Possible exceptions: (Part.OCCError).
        """

    def VPeriod(self) -> float:
        """
        Returns the period of this patch in the v parametric direction.
				
        Possible exceptions: (Part.OCCError).
        """

    def bounds(self) -> tuple[float, float, float, float]:
        """Returns the parametric bounds (U1, U2, V1, V2) of this trimmed surface."""

    def curvature(self, u: float, v: float, type: str, /) -> float:
        """
        curvature(u,v,type) -> float
        The value of type must be one of this: Max, Min, Mean or Gauss
        Computes the curvature of parameter (u,v) on this geometry
        Possible exceptions: (ValueError, Part.OCCError).
        """

    def curvatureDirections(self, u: float, v: float, /) -> tuple[FreeCAD.Vector, FreeCAD.Vector]:
        """
        curvatureDirections(u,v) -> (Vector,Vector)
        Computes the directions of maximum and minimum curvature
        of parameter (u,v) on this geometry.
        The first vector corresponds to the maximum curvature,
        the second vector corresponds to the minimum curvature.

        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def intersect(self, arg1: PartModule.GeometrySurface, arg2: float = None, /): ...

    @typing.overload
    def intersect(self, arg1: PartModule.Curve, arg2: float = None, /):
        """
        Returns all intersection points/curves between the surface and the curve/surface.
                
        Possible exceptions: (RuntimeError, TypeError).
        """

    def intersectSS(self, arg1: PartModule.GeometrySurface, arg2: float = None, /) -> list:
        """
        Returns all intersection curves of this surface and the given surface.
        The required arguments are:
        * Second surface
        * precision code (optional, default=0)
                
        Possible exceptions: (RuntimeError, TypeError).
        """

    def isPlanar(self, float: float = None, /) -> bool:
        """
        isPlanar([float]) -> Bool
        Checks if the surface is planar within a certain tolerance.
                
        Possible exceptions: (Part.OCCError).
        """

    def isUClosed(self) -> bool:
        """Checks if this surface is closed in the u parametric direction."""

    def isUPeriodic(self) -> bool:
        """Returns true if this patch is periodic in the given parametric direction."""

    def isUmbillic(self, u: float, v: float, /) -> bool:
        """
        isUmbillic(u,v) -> bool
        Check if the geometry on parameter is an umbillic point,
        i.e. maximum and minimum curvature are equal.
        Possible exceptions: (Part.OCCError).
        """

    def isVClosed(self) -> bool:
        """Checks if this surface is closed in the v parametric direction."""

    def isVPeriodic(self) -> bool:
        """Returns true if this patch is periodic in the given parametric direction."""

    def normal(self, u: float, v: float, /) -> FreeCAD.Vector:
        """
        normal(u,v) -> Vector
        Computes the normal of parameter (u,v) on this geometry
        Possible exceptions: (RuntimeError, Part.OCCError).
        """

    def parameter(self, arg1: FreeCAD.Vector, arg2: float = None, /) -> tuple[float, float]:
        """
        Returns the parameter on the curve
        of the nearest orthogonal projection of the point.
        Possible exceptions: (Part.OCCError).
        """

    def tangent(self, u: float, v: float, /) -> tuple[FreeCAD.Vector, FreeCAD.Vector]:
        """
        tangent(u,v) -> (Vector,Vector)
        Computes the tangent of parameter (u,v) on this geometry
        Possible exceptions: (Part.OCCError).
        """

    def toBSpline(self, arg1: float, arg2: str, arg3: str, arg4: int, arg5: int, arg6: int, arg7: int = None, /) -> PartModule.BSplineSurface:
        """
        Returns a B-Spline representation of this surface. 
        The required arguments are:
        * tolerance
        * continuity in u (as string e.g. C0, G0, G1, C1, G2, C3, CN)
        * continuity in v (as string e.g. C0, G0, G1, C1, G2, C3, CN)
        * maximum degree in u
        * maximum degree in v
        * maximum number of segments
        * precision code (optional, default=0)
				
        Possible exceptions: (Part.OCCError).
        """

    def toShape(self, arg1: float = None, arg2: float = None, arg3: float = None, arg4: float = None, /) -> PartModule.Face:
        """
        Return the shape for the geometry.
        Possible exceptions: (Part.OCCError).
        """

    def uIso(self, arg1: float, /) -> PartModule.Line | object:
        """
        Builds the U isoparametric curve
        Possible exceptions: (RuntimeError, Part.OCCError).
        """

    def vIso(self, arg1: float, /) -> PartModule.Line | object:
        """
        Builds the V isoparametric curve
        Possible exceptions: (RuntimeError, Part.OCCError).
        """

    def value(self, u: float, v: float, /) -> FreeCAD.Vector:
        """
        value(u,v) -> Point
        Computes the point of parameter (u,v) on this surface
        Possible exceptions: (Part.OCCError).
        """


# TopoShapeEdgePy.xml
class Edge(PartModule.Shape):
    """
    This class can be imported.
    TopoShapeEdge is the OpenCasCade topological edge wrapper
    """

    @typing.overload
    def __init__(self, arg1: PartModule.Geometry, arg2: float = None, arg3: float = None, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Shape, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Vertex, arg2: PartModule.Vertex, /):
        """
        TopoShapeEdge is the OpenCasCade topological edge wrapper
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def CenterOfMass(self) -> FreeCAD.Vector:
        """
        Returns the center of mass of the current system.
        If the gravitational field is uniform, it is the center of gravity.
        The coordinates returned for the center of mass are expressed in the
        absolute Cartesian coordinate system.
        """

    @property
    def Closed(self) -> bool:
        """Returns true if the edge is closed"""

    @property
    def Curve(self) -> object:
        """Returns the 3D curve of the edge"""

    @property
    def Degenerated(self) -> bool:
        """Returns true if the edge is degenerated"""

    @property
    def FirstParameter(self) -> float:
        """
        Returns the start value of the range of the primary parameter 
        defining the curve.

        What the parameter is depends on what type of edge it is. For a 
        Line the parameter is simply its cartesian length. Some other 
        examples are shown below:

        Type                 Parameter
        -----------------------------------------------------------
        Circle               Angle swept by circle (or arc) in radians
        BezierCurve          Unitless number in the range 0.0 to 1.0
        Helix                Angle swept by helical turns in radians
        """

    @property
    def LastParameter(self) -> float:
        """
        Returns the end value of the range of the primary parameter 
        defining the curve.

        What the parameter is depends on what type of edge it is. For a 
        Line the parameter is simply its cartesian length. Some other 
        examples are shown below:

        Type                 Parameter
        -----------------------------------------------------------
        Circle               Angle swept by circle (or arc) in radians
        BezierCurve          Unitless number in the range 0.0 to 1.0
        Helix                Angle swept by helical turns in radians
        """

    @property
    def Length(self) -> float:
        """Returns the cartesian length of the curve"""

    @property
    def Mass(self) -> float:
        """Returns the mass of the current system."""

    @property
    def MatrixOfInertia(self) -> FreeCAD.Matrix:
        """
        Returns the matrix of inertia. It is a symmetrical matrix. 
        The coefficients of the matrix are the quadratic moments of 
        inertia. 

         | Ixx Ixy Ixz 0 | 
         | Ixy Iyy Iyz 0 | 
         | Ixz Iyz Izz 0 | 
         | 0   0   0   1 | 

        The moments of inertia are denoted by Ixx, Iyy, Izz. 
        The products of inertia are denoted by Ixy, Ixz, Iyz. 
        The matrix of inertia is returned in the central coordinate 
        system (G, Gx, Gy, Gz) where G is the centre of mass of the 
        system and Gx, Gy, Gz the directions parallel to the X(1,0,0) 
        Y(0,1,0) Z(0,0,1) directions of the absolute cartesian 
        coordinate system.
        """

    @property
    def ParameterRange(self) -> tuple[float, float]:
        """
        Returns a 2 tuple with the range of the primary parameter 
        defining the curve. This is the same as would be returned by 
        the FirstParameter and LastParameter properties, i.e.

        (LastParameter,FirstParameter)

        What the parameter is depends on what type of edge it is. For a 
        Line the parameter is simply its cartesian length. Some other 
        examples are shown below:

        Type                 Parameter
        ---------------------------------------------------------------
        Circle               Angle swept by circle (or arc) in radians
        BezierCurve          Unitless number in the range 0.0 to 1.0
        Helix                Angle swept by helical turns in radians
        """

    @property
    def PrincipalProperties(self) -> ReturnGetPrincipalPropertiesDict:
        """
        Computes the principal properties of inertia of the current system. 
         There is always a set of axes for which the products 
         of inertia of a geometric system are equal to 0; i.e. the 
         matrix of inertia of the system is diagonal. These axes 
         are the principal axes of inertia. Their origin is 
         coincident with the center of mass of the system. The 
         associated moments are called the principal moments of inertia. 
         This function computes the eigen values and the 
         eigen vectors of the matrix of inertia of the system.
        """

    @property
    def StaticMoments(self) -> tuple[float, float, float]:
        """
        Returns Ix, Iy, Iz, the static moments of inertia of the 
         current system; i.e. the moments of inertia about the 
         three axes of the Cartesian coordinate system.
        """

    @property
    def Tolerance(self) -> float:
        """Set or get the tolerance of the vertex"""

    def centerOfCurvatureAt(self, float_pos: float, /) -> FreeCAD.Vector:
        """
        Vector = centerOfCurvatureAt(float pos) - Get the center of curvature at the given parameter [First|Last] if defined
        Possible exceptions: (Part.OCCError).
        """

    def curvatureAt(self, paramval: float, /) -> float:
        """
        Float = curvatureAt(paramval) - Get the curvature at the given parameter [First|Last] if defined
        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def derivative1At(self, paramval: float, /) -> FreeCAD.Vector: ...

    @typing.overload
    def derivative1At(self, x_FirstParameter_0_5_x_LastParameter_x_FirstParameter_: float, /) -> FreeCAD.Vector: ...

    @typing.overload
    def derivative1At(self, x_FirstParameter_3_5_x_LastParameter_x_FirstParameter_: float, /) -> FreeCAD.Vector:
        """
        Vector = derivative1At(paramval)
        Get the first derivative at the given parameter value along the Edge if it 
        is defined

        Args:
            paramval (float or int): The parameter value along the Edge at which to 
                determine the first derivative e.g:
        
                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)    
                y = x.derivative1At(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))

                y is the Vector (-0.7071067811865475, 0.7071067811865476, 0.0)

                Values with magnitude greater than the Edge length return 
                values of the first derivative on the curve extrapolated 
                beyond its length. This may not be valid for all Edges. 
                Negative values similarly return a first derivative on the 
                curve extrapolated backwards (before the start point of the 
                Edge). For example, using the same shape as above:

                >>> x.derivative1At(x.FirstParameter + 3.5*(x.LastParameter - x.FirstParameter))
                Vector (0.7071067811865477, 0.7071067811865474, 0.0)

                Which gives the same result as 

                >>> x.derivative1At(x.FirstParameter -0.5*(x.LastParameter - x.FirstParameter))
                Vector (0.7071067811865475, 0.7071067811865476, 0.0)

                Since it is a circle

        Returns:

            Vector: representing the first derivative to the Edge at the 
               given location along its length (or extrapolated length)

        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def derivative2At(self, paramval: float, /) -> FreeCAD.Vector: ...

    @typing.overload
    def derivative2At(self, x_FirstParameter_0_5_x_LastParameter_x_FirstParameter_: float, /) -> FreeCAD.Vector: ...

    @typing.overload
    def derivative2At(self, x_FirstParameter_3_5_x_LastParameter_x_FirstParameter_: float, /) -> FreeCAD.Vector:
        """
        Vector = derivative2At(paramval)
        Get the second derivative at the given parameter value along the Edge if it 
        is defined

        Args:
            paramval (float or int): The parameter value along the Edge at which to 
                determine the second derivative e.g:
        
                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)    
                y = x.derivative2At(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))

                y is the Vector (-0.7071067811865476, -0.7071067811865475, 0.0)

                Values with magnitude greater than the Edge length return 
                values of the second derivative on the curve extrapolated 
                beyond its length. This may not be valid for all Edges. 
                Negative values similarly return a second derivative on the 
                curve extrapolated backwards (before the start point of the 
                Edge). For example, using the same shape as above:

                >>> x.derivative2At(x.FirstParameter + 3.5*(x.LastParameter - x.FirstParameter))
                Vector (-0.7071067811865474, 0.7071067811865477, 0.0)

                Which gives the same result as 

                >>> x.derivative2At(x.FirstParameter -0.5*(x.LastParameter - x.FirstParameter))
                Vector (-0.7071067811865476, 0.7071067811865475, 0.0)

                Since it is a circle

        Returns:

            Vector: representing the second derivative to the Edge at the 
               given location along its length (or extrapolated length)

        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def derivative3At(self, paramval: float, /) -> FreeCAD.Vector: ...

    @typing.overload
    def derivative3At(self, x_FirstParameter_0_5_x_LastParameter_x_FirstParameter_: float, /) -> FreeCAD.Vector: ...

    @typing.overload
    def derivative3At(self, x_FirstParameter_3_5_x_LastParameter_x_FirstParameter_: float, /) -> FreeCAD.Vector:
        """
        Vector = derivative3At(paramval)
        Get the third derivative at the given parameter value along the Edge if it 
        is defined

        Args:
            paramval (float or int): The parameter value along the Edge at which to 
                determine the third derivative e.g:
        
                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)    
                y = x.derivative3At(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))

                y is the Vector (0.7071067811865475, -0.7071067811865476, -0.0)

                Values with magnitude greater than the Edge length return 
                values of the third derivative on the curve extrapolated 
                beyond its length. This may not be valid for all Edges. 
                Negative values similarly return a third derivative on the 
                curve extrapolated backwards (before the start point of the 
                Edge). For example, using the same shape as above:

                >>> x.derivative3At(x.FirstParameter + 3.5*(x.LastParameter - x.FirstParameter))
                Vector (-0.7071067811865477, -0.7071067811865474, 0.0)

                Which gives the same result as 

                >>> x.derivative3At(x.FirstParameter -0.5*(x.LastParameter - x.FirstParameter))
                Vector (-0.7071067811865475, -0.7071067811865476, 0.0)

                Since it is a circle

        Returns:

            Vector: representing the third derivative to the Edge at the 
               given location along its length (or extrapolated length)

        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def discretize(self, Number, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiNumber, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Distance, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Deflection, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiDeflection, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Number: int, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Distance: float, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Deflection: float, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiNumber: int, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiDeflection: float, First: float = None, Last: float = None) -> list[FreeCAD.Vector]:
        """
        Discretizes the edge and returns a list of points.
        The function accepts keywords as argument:
        discretize(Number=n) => gives a list of 'n' equidistant points
        discretize(QuasiNumber=n) => gives a list of 'n' quasi equidistant points (is faster than the method above)
        discretize(Distance=d) => gives a list of equidistant points with distance 'd'
        discretize(Deflection=d) => gives a list of points with a maximum deflection 'd' to the edge
        discretize(QuasiDeflection=d) => gives a list of points with a maximum deflection 'd' to the edge (faster)
        discretize(Angular=a,Curvature=c,[Minimum=m]) => gives a list of points with an angular deflection of 'a'
                                            and a curvature deflection of 'c'. Optionally a minimum number of points
                                            can be set which by default is set to 2.

        Optionally you can set the keywords 'First' and 'Last' to define a sub-range of the parameter range
        of the edge.

        If no keyword is given then it depends on whether the argument is an int or float.
        If it's an int then the behaviour is as if using the keyword 'Number', if it's float
        then the behaviour is as if using the keyword 'Distance'.

        Example:

        import Part
        e=Part.makeCircle(5)
        p=e.discretize(Number=50,First=3.14)
        s=Part.Compound([Part.Vertex(i) for i in p])
        Part.show(s)


        p=e.discretize(Angular=0.09,Curvature=0.01,Last=3.14,Minimum=100)
        s=Part.Compound([Part.Vertex(i) for i in p])
        Part.show(s)

        Possible exceptions: (TypeError, Part.OCCError).
        """

    def firstVertex(self, Orientation: bool = False, /) -> PartModule.Vertex:
        """
        Vertex = firstVertex(Orientation=False)
        Returns the Vertex of orientation FORWARD in this edge.
        If there is none a Null shape is returned.
        Orientation = True : taking into account the edge orientation
        """

    def getParameterByLength(self, pos: float, tolerance: float = 1e-7, /) -> float:
        """
        paramval = getParameterByLength(pos, [tolerance = 1e-7])
        Get the value of the primary parameter at the given distance along the cartesian
        length of the edge.

        Args:
            pos (float or int): The distance along the length of the edge at which to 
                determine the primary parameter value. See help for the FirstParameter or 
                LastParameter properties for more information on the primary parameter.
                If the given value is positive, the distance from edge start is used.
                If the given value is negative, the distance from edge end is used.
            tol (float): Computing tolerance. Optional, defaults to 1e-7.

        Returns:

            paramval (float): the value of the primary parameter defining the edge at the 
                given position along its cartesian length.

        Possible exceptions: (ValueError).
        """

    def isSeam(self, Face: PartModule.Face, /) -> bool:
        """
        isSeam(Face) - Checks whether the edge is a seam edge.
        Possible exceptions: (Part.OCCError).
        """

    def lastVertex(self, Orientation: bool = False, /) -> PartModule.Vertex:
        """
        Vertex = lastVertex(Orientation=False)
        Returns the Vertex of orientation REVERSED in this edge.
        If there is none a Null shape is returned.
        Orientation = True : taking into account the edge orientation
        """

    @typing.overload
    def normalAt(self, paramval: float, /) -> FreeCAD.Vector: ...

    @typing.overload
    def normalAt(self, x_FirstParameter_0_5_x_LastParameter_x_FirstParameter_: float, /) -> FreeCAD.Vector: ...

    @typing.overload
    def normalAt(self, x_FirstParameter_3_5_x_LastParameter_x_FirstParameter_: float, /) -> FreeCAD.Vector:
        """
        Vector = normalAt(paramval)
        Get the normal direction at the given parameter value along the Edge if it 
        is defined

        Args:
            paramval (float or int): The parameter value along the Edge at which to 
                determine the normal direction e.g:
        
                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)    
                y = x.normalAt(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))

                y is the Vector (-0.7071067811865476, -0.7071067811865475, 0.0)

                Values with magnitude greater than the Edge length return 
                values of the normal on the curve extrapolated beyond its 
                length. This may not be valid for all Edges. Negative values 
                similarly return a normal on the curve extrapolated backwards 
                (before the start point of the Edge). For example, using the 
                same shape as above:

                >>> x.normalAt(x.FirstParameter + 3.5*(x.LastParameter - x.FirstParameter))
                Vector (-0.7071067811865474, 0.7071067811865477, 0.0)

                Which gives the same result as 

                >>> x.normalAt(x.FirstParameter -0.5*(x.LastParameter - x.FirstParameter))
                Vector (-0.7071067811865476, 0.7071067811865475, 0.0)

                Since it is a circle

        Returns:

            Vector: representing the normal to the Edge at the given 
               location along its length (or extrapolated length)

        Possible exceptions: (Part.OCCError).
        """

    def parameterAt(self, arg1: PartModule.Vertex, arg2: PartModule.Face = None, /) -> float:
        """
        Float = parameterAt(Vertex) - Get the parameter at the given vertex if lying on the edge
        Possible exceptions: (Part.OCCError).
        """

    def parameters(self, face: PartModule.Face = None, /) -> list | list[float]:
        """
        parameters([face]) --> list
        Get the list of parameters of the tessellation of an edge. If the edge is part of
        a face then this face is required as argument.
        An exception is raised if the edge has no polygon.

        Possible exceptions: (ValueError, RuntimeError).
        """

    def split(self, paramval, /) -> PartModule.Wire:
        """
        Wire = split(paramval) 
        Splits the edge at the given parameter values and builds a wire out of it

        Args:
            paramval (float or int): The parameter value along the Edge at which to 
                split it e.g:
        
                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)    
                y = x.derivative3At(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))

        Returns:

            Wire: wire made up of two Edges

        Possible exceptions: (ValueError, TypeError, Part.OCCError).
        """

    @typing.overload
    def tangentAt(self, paramval: float, /) -> FreeCAD.Vector: ...

    @typing.overload
    def tangentAt(self, x_FirstParameter_0_5_x_LastParameter_x_FirstParameter_: float, /) -> FreeCAD.Vector: ...

    @typing.overload
    def tangentAt(self, x_FirstParameter_3_5_x_LastParameter_x_FirstParameter_: float, /) -> FreeCAD.Vector:
        """
        Vector = tangentAt(paramval)
        Get the tangent direction at the given primary parameter value along the Edge 
        if it is defined

        Args:
            paramval (float or int): The parameter value along the Edge at which to 
                determine the tangent direction e.g:
        
                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)    
                y = x.tangentAt(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))

                y is the Vector (-0.7071067811865475, 0.7071067811865476, 0.0)

                Values with magnitude greater than the Edge length return 
                values of the tangent on the curve extrapolated beyond its 
                length. This may not be valid for all Edges. Negative values 
                similarly return a tangent on the curve extrapolated backwards 
                (before the start point of the Edge). For example, using the 
                same shape as above:

                >>> x.tangentAt(x.FirstParameter + 3.5*(x.LastParameter - x.FirstParameter))
                Vector (0.7071067811865477, 0.7071067811865474, 0.0)

                Which gives the same result as 

                >>> x.tangentAt(x.FirstParameter -0.5*(x.LastParameter - x.FirstParameter))
                Vector (0.7071067811865475, 0.7071067811865476, 0.0)

                Since it is a circle

        Returns:

            Vector: representing the tangent to the Edge at the given 
               location along its length (or extrapolated length)

        Possible exceptions: (NotImplementedError).
        """

    @typing.overload
    def valueAt(self, paramval: float, /) -> FreeCAD.Vector: ...

    @typing.overload
    def valueAt(self, x_FirstParameter_0_5_x_LastParameter_x_FirstParameter_: float, /) -> FreeCAD.Vector: ...

    @typing.overload
    def valueAt(self, x_FirstParameter_3_5_x_LastParameter_x_FirstParameter_: float, /) -> FreeCAD.Vector:
        """
        Vector = valueAt(paramval)
        Get the value of the cartesian parameter value at the given parameter value along 
        the Edge

        Args:
            paramval (float or int): The parameter value along the Edge at which to 
                determine the value in terms of the main parameter defining 
                the edge, what the parameter value is depends on the type of
                edge. See  e.g:
        
                For a circle value

                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)    
                y = x.valueAt(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))

                y is theVector (0.7071067811865476, 0.7071067811865475, 0.0)

                Values with magnitude greater than the Edge length return 
                values on the curve extrapolated beyond its length. This may 
                not be valid for all Edges. Negative values similarly return 
                a parameter value on the curve extrapolated backwards (before the 
                start point of the Edge). For example, using the same shape 
                as above:

                >>> x.valueAt(x.FirstParameter + 3.5*(x.LastParameter - x.FirstParameter))
                Vector (0.7071067811865474, -0.7071067811865477, 0.0)

                Which gives the same result as 

                >>> x.valueAt(x.FirstParameter -0.5*(x.LastParameter - x.FirstParameter))
                Vector (0.7071067811865476, -0.7071067811865475, 0.0)

                Since it is a circle

        Returns:

            Vector: representing the cartesian location on the Edge at the given 
               distance along its length (or extrapolated length)
        """


# BezierCurvePy.xml
class BezierCurve(PartModule.BoundedCurve):
    """
    This class can be imported.

    				Describes a rational or non-rational Bezier curve:
    				-- a non-rational Bezier curve is defined by a table of poles (also called control points)
    				-- a rational Bezier curve is defined by a table of poles with varying weights

    				Constructor takes no arguments.

    				Example usage:
    					p1 = Base.Vector(-1, 0, 0)
    					p2 = Base.Vector(0, 1, 0.2)
    					p3 = Base.Vector(1, 0, 0.4)
    					p4 = Base.Vector(0, -1, 1)

    					bc = BezierCurve()
    					bc.setPoles([p1, p2, p3, p4])
    					curveShape = bc.toShape()
    """

    def __init__(self):
        """
        Describes a rational or non-rational Bezier curve:
        				-- a non-rational Bezier curve is defined by a table of poles (also called control points)
        				-- a rational Bezier curve is defined by a table of poles with varying weights

        				Constructor takes no arguments.

        				Example usage:
        					p1 = Base.Vector(-1, 0, 0)
        					p2 = Base.Vector(0, 1, 0.2)
        					p3 = Base.Vector(1, 0, 0.4)
        					p4 = Base.Vector(0, -1, 1)

        					bc = BezierCurve()
        					bc.setPoles([p1, p2, p3, p4])
        					curveShape = bc.toShape()
        """

    @property
    def Degree(self) -> int:
        """
        Returns the polynomial degree of this Bezier curve,
        which is equal to the number of poles minus 1.
        """

    @property
    def EndPoint(self) -> FreeCAD.Vector:
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
    def StartPoint(self) -> FreeCAD.Vector:
        """Returns the start point of this Bezier curve."""

    def getPole(self, arg1: int, /) -> FreeCAD.Vector:
        """
        Get a pole of the Bezier curve.
        Possible exceptions: (Part.OCCError).
        """

    def getPoles(self) -> list[FreeCAD.Vector]:
        """
        Get all poles of the Bezier curve.
        Possible exceptions: (Part.OCCError).
        """

    def getResolution(self, arg1: float, /) -> float:
        """
        Computes for this Bezier curve the parametric tolerance (UTolerance)
        for a given 3D tolerance (Tolerance3D).
        If f(t) is the equation of this Bezier curve, the parametric tolerance
        ensures that:
        |t1-t0| < UTolerance ===> |f(t1)-f(t0)| < Tolerance3D
        Possible exceptions: (Part.OCCError).
        """

    def getWeight(self, arg1: int, /) -> float:
        """
        Get a weight of the Bezier curve.
        Possible exceptions: (Part.OCCError).
        """

    def getWeights(self) -> list[float]:
        """
        Get all weights of the Bezier curve.
        Possible exceptions: (Part.OCCError).
        """

    def increase(self, Int: int, /):
        """
        increase(Int=Degree)
        Increases the degree of this Bezier curve to Degree.
        As a result, the poles and weights tables are modified.
        """

    def insertPoleAfter(self, arg1: int, arg2: FreeCAD.Vector, arg3: float = None, /):
        """
        Inserts after the pole of index.
        Possible exceptions: (Part.OCCError).
        """

    def insertPoleBefore(self, arg1: int, arg2: FreeCAD.Vector, arg3: float = None, /):
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

    def removePole(self, arg1: int, /):
        """
        Removes the pole of index Index from the table of poles of this Bezier curve.
        If this Bezier curve is rational, it can become non-rational.
        Possible exceptions: (Part.OCCError).
        """

    def segment(self, arg1: float, arg2: float, /):
        """
        Modifies this Bezier curve by segmenting it.
        Possible exceptions: (Part.OCCError).
        """

    def setPole(self, arg1: int, arg2: FreeCAD.Vector, arg3: float = None, /):
        """
        Set a pole of the Bezier curve.
        Possible exceptions: (Part.OCCError).
        """

    def setPoles(self, arg1, /):
        """
        Set the poles of the Bezier curve.

        				Takes a list of 3D Base.Vector objects.
        Possible exceptions: (Part.OCCError).
        """

    def setWeight(self, arg1: int, arg2: float, /):
        """
        (id, weight) Set a weight of the Bezier curve.
				
        Possible exceptions: (Part.OCCError).
        """


# SurfaceOfRevolutionPy.xml
class SurfaceOfRevolution(PartModule.GeometrySurface):
    """
    This class can be imported.
    Describes a surface of revolution
    """

    def __init__(self, arg1: PartModule.Geometry, arg2: FreeCAD.Vector, arg3: FreeCAD.Vector, /):
        """
        Describes a surface of revolution
        Possible exceptions: (TypeError, Part.OCCError).
        """

    @property
    def BasisCurve(self) -> object:
        """Sets or gets the basic curve."""

    @property
    def Direction(self) -> FreeCAD.Vector:
        """Sets or gets the direction of revolution."""

    @property
    def Location(self) -> FreeCAD.Vector:
        """Sets or gets the location of revolution."""


# LineSegmentPy.xml
class LineSegment(PartModule.TrimmedCurve):
    """
    This class can be imported.
    Describes a line segment
    To create a line segment there are several ways:
    Part.LineSegment()
        Creates a default line segment

    Part.LineSegment(LineSegment)
        Creates a copy of the given line segment

    Part.LineSegment(Point1,Point2)
        Creates a line segment that goes through two given points
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, LineSegment: PartModule.LineSegment, /): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, /):
        """
        Describes a line segment
        To create a line segment there are several ways:
        Part.LineSegment()
            Creates a default line segment

        Part.LineSegment(LineSegment)
            Creates a copy of the given line segment

        Part.LineSegment(Point1,Point2)
            Creates a line segment that goes through two given points
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def EndPoint(self) -> FreeCAD.Vector:
        """Returns the end point point of this line."""

    @EndPoint.setter
    def EndPoint(self, value: FreeCAD.Vector): ...

    @property
    def StartPoint(self) -> FreeCAD.Vector:
        """Returns the start point of this line."""

    @StartPoint.setter
    def StartPoint(self, value: FreeCAD.Vector): ...

    def setParameterRange(self, arg1: float, arg2: float, /):
        """
        Set the parameter range of the underlying line geometry
        Possible exceptions: (Part.OCCError).
        """


# GeometryPy.xml
class Geometry(FreeCAD.PyObjectBase):
    """
    The abstract class Geometry for 3D space is the root class of all geometric objects.
    It describes the common behavior of these objects when:
    - applying geometric transformations to objects, and
    - constructing objects by geometric transformation (including copying).
    """

    @property
    def Construction(self) -> bool:
        """
        Defines this geometry as a construction one which
        means that it is not part of a later built shape.
        """

    @Construction.setter
    def Construction(self, value: bool): ...

    @property
    def Tag(self) -> str:
        """Gives the tag of the geometry as string."""

    def clone(self):
        """
        Create a clone of this geometry with the same Tag
        Possible exceptions: (TypeError).
        """

    def copy(self):
        """
        Create a copy of this geometry
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def mirror(self, arg1: FreeCAD.Vector, /): ...

    @typing.overload
    def mirror(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, /):
        """
        Performs the symmetrical transformation of this geometric object
        Possible exceptions: (Part.OCCError).
        """

    def rotate(self, arg1: FreeCAD.Placement, /):
        """Rotates this geometric object at angle Ang (in radians) about axis"""

    @typing.overload
    def scale(self, arg1: FreeCAD.Vector, arg2: float, /): ...

    @typing.overload
    def scale(self, arg1: tuple, arg2: float, /):
        """
        Applies a scaling transformation on this geometric object with a center and scaling factor
        Possible exceptions: (Part.OCCError).
        """

    def transform(self, arg1: FreeCAD.Matrix, /):
        """Applies a transformation to this geometric object"""

    @typing.overload
    def translate(self, arg1: FreeCAD.Vector, /): ...

    @typing.overload
    def translate(self, arg1: tuple, /):
        """
        Translates this geometric object
        Possible exceptions: (Part.OCCError).
        """


# GeometryCurvePy.xml
class Curve(PartModule.Geometry):
    """The abstract class GeometryCurve is the root class of all curve objects."""

    @property
    def Continuity(self) -> str:
        """Returns the global continuity of the curve."""

    @property
    def FirstParameter(self) -> float:
        """Returns the value of the first parameter."""

    @property
    def LastParameter(self) -> float:
        """Returns the value of the last parameter."""

    def approximateBSpline(self, Tolerance: float, MaxSegments: int, MaxDegree: int, Order: str = 'C2', /) -> PartModule.BSplineCurve:
        """
        Approximates a curve of any type to a B-Spline curve
        					approximateBSpline(Tolerance, MaxSegments, MaxDegree, [Order='C2']) -> B-Spline curve
				
        Possible exceptions: (RuntimeError, Part.OCCError).
        """

    def centerOfCurvature(self, float_pos: float, /) -> FreeCAD.Vector:
        """
        Vector = centerOfCurvature(float pos) - Get the center of curvature at the given parameter [First|Last] if defined
        Possible exceptions: (Part.OCCError).
        """

    def curvature(self, pos: float, /) -> float:
        """
        Float = curvature(pos) - Get the curvature at the given parameter [First|Last] if defined
        Possible exceptions: (Part.OCCError).
        """

    @typing.overload
    def discretize(self, Number, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiNumber, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Distance, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Deflection, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiDeflection, /) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Number: int, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Distance: float, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, Deflection: float, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiNumber: int, First: float = None, Last: float = None) -> list[FreeCAD.Vector]: ...

    @typing.overload
    def discretize(self, QuasiDeflection: float, First: float = None, Last: float = None) -> list[FreeCAD.Vector]:
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
        c=Part.Circle()
        c.Radius=5
        p=c.discretize(Number=50,First=3.14)
        s=Part.Compound([Part.Vertex(i) for i in p])
        Part.show(s)


        p=c.discretize(Angular=0.09,Curvature=0.01,Last=3.14,Minimum=100)
        s=Part.Compound([Part.Vertex(i) for i in p])
        Part.show(s)

        Possible exceptions: (Part.OCCError, TypeError).
        """

    @typing.overload
    def intersect(self, arg1: PartModule.Curve, arg2: float = None, /): ...

    @typing.overload
    def intersect(self, arg1: PartModule.GeometrySurface, arg2: float = None, /):
        """
        Returns all intersection points and curve segments between the curve and the curve/surface.
              
        Possible exceptions: (RuntimeError, TypeError).
        """

    def intersect2d(self, arg1: PartModule.Curve, arg2: PartModule.Plane, /) -> list[tuple[float, float]]:
        """
        Get intersection points with another curve lying on a plane.
        Possible exceptions: (Part.OCCError).
        """

    def intersectCC(self, arg1: PartModule.Curve, arg2: float = None, /) -> list | list[PartModule.Point]:
        """
        Returns all intersection points between this curve and the given curve.
              
        Possible exceptions: (RuntimeError).
        """

    def intersectCS(self, arg1: PartModule.GeometrySurface, arg2: float = None, /) -> tuple[list[PartModule.Point], list]:
        """
        Returns all intersection points and curve segments between the curve and the surface.
              
        Possible exceptions: (RuntimeError, TypeError).
        """

    def isClosed(self) -> bool:
        """
        Returns true if the curve is closed.
            
        Possible exceptions: (RuntimeError).
        """

    def isPeriodic(self) -> bool:
        """
        Returns true if this curve is periodic.
        Possible exceptions: (RuntimeError).
        """

    def length(self, uMin: float = None, uMax: float = None, Tol: float = None, /) -> float:
        """
        Computes the length of a curve
        length([uMin,uMax,Tol]) -> Float
        Possible exceptions: (Part.OCCError).
        """

    def makeRuledSurface(self, arg1: PartModule.Curve, /) -> PartModule.RectangularTrimmedSurface | PartModule.BSplineSurface:
        """
        Make a ruled surface of this and the given curves
        Possible exceptions: (Part.OCCError).
        """

    def normal(self, pos: float, /) -> FreeCAD.Vector:
        """
        Vector = normal(pos) - Get the normal vector at the given parameter [First|Last] if defined
        Possible exceptions: (Part.OCCError).
        """

    def parameter(self, arg1: FreeCAD.Vector, /) -> float:
        """
        Returns the parameter on the curve
        of the nearest orthogonal projection of the point.
        Possible exceptions: (Part.OCCError).
        """

    def parameterAtDistance(self, abscissa: float, startingParameter: float = None, /) -> float:
        """
        Returns the parameter on the curve of a point at the given distance from a starting parameter. 
        parameterAtDistance([abscissa, startingParameter]) -> Float the
        Possible exceptions: (Part.OCCError).
        """

    def period(self) -> float:
        """
        Returns the period of this curve
        or raises an exception if it is not periodic.
        Possible exceptions: (RuntimeError).
        """

    def reverse(self):
        """
        Changes the direction of parametrization of the curve.
        Possible exceptions: (RuntimeError).
        """

    def reversedParameter(self, arg1: float, /) -> float:
        """
        Returns the parameter on the reversed curve for
        the point of parameter U on this curve.
        Possible exceptions: (RuntimeError).
        """

    def tangent(self, arg1: float, /) -> tuple[FreeCAD.Vector, ...]:
        """
        Computes the tangent of parameter u on this curve
        Possible exceptions: (Part.OCCError).
        """

    def toBSpline(self, Float: float = None, Float2: float = None, /) -> PartModule.BSplineCurve:
        """
        Converts a curve of any type (only part from First to Last)
        					toBSpline([Float=First, Float=Last]) -> B-Spline curve
				
        Possible exceptions: (Part.OCCError).
        """

    def toNurbs(self, Float: float = None, Float2: float = None, /) -> PartModule.BSplineCurve:
        """
        Converts a curve of any type (only part from First to Last)
                            toNurbs([Float=First, Float=Last]) -> NURBS curve
                
        Possible exceptions: (Part.OCCError).
        """

    def toShape(self, arg1: float = None, arg2: float = None, /) -> PartModule.Edge:
        """
        Return the shape for the geometry.
        Possible exceptions: (Part.OCCError).
        """

    def trim(self, Float: float = None, Float2: float = None, /):
        """
        Returns a trimmed curve defined in the given parameter range
                            trim([Float=First, Float=Last]) -> trimmed curve
                
        Possible exceptions: (Part.OCCError).
        """

    def value(self, arg1: float, /) -> FreeCAD.Vector:
        """
        Computes the point of parameter u on this curve
        Possible exceptions: (Part.OCCError).
        """


# ConePy.xml
class Cone(PartModule.GeometrySurface):
    """
    This class can be imported.
    Describes a cone in 3D space
    				To create a cone there are several ways:
    				Part.Cone()
    				    Creates a default cone with radius 1

    				Part.Cone(Cone)
    				    Creates a copy of the given cone

    				Part.Cone(Cone, Distance)
    				    Creates a cone parallel to given cone at a certain distance

    				Part.Cone(Point1,Point2,Radius1,Radius2)
    				    Creates a cone defined by two points and two radii
    				    The axis of the cone is the line passing through
    				    Point1 and Poin2.
    				    Radius1 is the radius of the section passing through
    				    Point1 and Radius2 the radius of the section passing
    				    through Point2.

    				Part.Cone(Point1,Point2,Point3,Point4)
    				    Creates a cone passing through three points Point1,
    				    Point2 and Point3.
    				    Its axis is defined by Point1 and Point2 and the radius of
    				    its base is the distance between Point3 and its axis.
    				    The distance between Point and the axis is the radius of
    				    the section passing through Point4.
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Cone: PartModule.Cone, Distance: float): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, Radius1: float, Radius2: float): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, Point3: FreeCAD.Vector, Point4: FreeCAD.Vector):
        """
        Describes a cone in 3D space
        				To create a cone there are several ways:
        				Part.Cone()
        				    Creates a default cone with radius 1

        				Part.Cone(Cone)
        				    Creates a copy of the given cone

        				Part.Cone(Cone, Distance)
        				    Creates a cone parallel to given cone at a certain distance

        				Part.Cone(Point1,Point2,Radius1,Radius2)
        				    Creates a cone defined by two points and two radii
        				    The axis of the cone is the line passing through
        				    Point1 and Poin2.
        				    Radius1 is the radius of the section passing through
        				    Point1 and Radius2 the radius of the section passing
        				    through Point2.

        				Part.Cone(Point1,Point2,Point3,Point4)
        				    Creates a cone passing through three points Point1,
        				    Point2 and Point3.
        				    Its axis is defined by Point1 and Point2 and the radius of
        				    its base is the distance between Point3 and its axis.
        				    The distance between Point and the axis is the radius of
        				    the section passing through Point4.
			
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Apex(self) -> FreeCAD.Vector:
        """Compute the apex of the cone."""

    @property
    def Axis(self) -> FreeCAD.Vector:
        """The axis direction of the cone"""

    @Axis.setter
    def Axis(self, value: FreeCAD.Vector): ...

    @property
    def Center(self) -> FreeCAD.Vector:
        """Center of the cone."""

    @Center.setter
    def Center(self, value: FreeCAD.Vector): ...

    @property
    def Radius(self) -> float:
        """The radius of the cone."""

    @Radius.setter
    def Radius(self, value: float): ...

    @property
    def SemiAngle(self) -> float:
        """The semi-angle of the cone."""

    @SemiAngle.setter
    def SemiAngle(self, value: float): ...

    def uIso(self, arg1: float, /) -> PartModule.Line:
        """
        Builds the U isoparametric circle of this cone
        Possible exceptions: (Part.OCCError).
        """

    def vIso(self, arg1: float, /) -> PartModule.Circle:
        """
        Builds the V isoparametric circle of this cone
        Possible exceptions: (Part.OCCError).
        """


# ToroidPy.xml
class Toroid(PartModule.GeometrySurface):
    """
    This class can be imported.
    Describes a toroid in 3D space
    """

    def __init__(self):
        """Describes a toroid in 3D space"""

    @property
    def Area(self) -> float:
        """Compute the area of the toroid."""

    @property
    def Axis(self) -> FreeCAD.Vector:
        """The axis direction of the toroid"""

    @Axis.setter
    def Axis(self, value: FreeCAD.Vector): ...

    @property
    def Center(self) -> FreeCAD.Vector:
        """Center of the toroid."""

    @Center.setter
    def Center(self, value: FreeCAD.Vector): ...

    @property
    def MajorRadius(self) -> float:
        """The major radius of the toroid."""

    @MajorRadius.setter
    def MajorRadius(self, value: float): ...

    @property
    def MinorRadius(self) -> float:
        """The minor radius of the toroid."""

    @MinorRadius.setter
    def MinorRadius(self, value: float): ...

    @property
    def Volume(self) -> float:
        """Compute the volume of the toroid."""

    def uIso(self, arg1: float, /) -> PartModule.Circle:
        """
        Builds the U isoparametric circle of this toroid
        Possible exceptions: (Part.OCCError).
        """

    def vIso(self, arg1: float, /) -> PartModule.Circle:
        """
        Builds the V isoparametric circle of this toroid
        Possible exceptions: (Part.OCCError).
        """


# AttachExtensionPy.xml
class AttachExtension(FreeCAD.DocumentObjectExtension):
    """This object represents an attachable object with OCC shape."""

    @property
    def Attacher(self) -> PartModule.AttachEngine | None:
        """AttachEngine object driving this AttachableObject. Returns a copy."""

    @property
    def AttacherType(self) -> str:
        """
        Property group: Attachment.
        Property TypeId: App::PropertyString.
        Class name of attach engine object driving the attachment.
        """

    @AttacherType.setter
    def AttacherType(self, value: str): ...

    @property
    def AttachmentOffset(self) -> FreeCAD.Placement:
        """
        Property group: Attachment.
        Property TypeId: App::PropertyPlacement.
        Extra placement to apply in addition to attachment (in local coordinates).
        """

    @AttachmentOffset.setter
    def AttachmentOffset(self, value: FreeCAD.Matrix | FreeCAD.Placement): ...

    @property
    def MapMode(self) -> int:
        """
        Property group: Attachment.
        Property TypeId: App::PropertyEnumeration.
        Mode of attachment to other object.
        """

    @MapMode.setter
    def MapMode(self, value): ...

    @property
    def MapPathParameter(self) -> float:
        """
        Property group: Attachment.
        Property TypeId: App::PropertyFloat.
        Sets point of curve to map the sketch to. 0..1 = start..end.
        """

    @MapPathParameter.setter
    def MapPathParameter(self, value: float): ...

    @property
    def MapReversed(self) -> bool:
        """
        Property group: Attachment.
        Property TypeId: App::PropertyBool.
        Reverse Z direction (flip sketch upside down).
        """

    @MapReversed.setter
    def MapReversed(self, value: int | bool): ...

    @property
    def Support(self) -> list[tuple[FreeCAD.DocumentObject, list[str]]]:
        """
        Property group: Attachment.
        Property TypeId: App::PropertyLinkSubList.
        Support of the 2D geometry.
        """

    @Support.setter
    def Support(self, value: LinkSub_t | LinkList_t | LinkSubList_t): ...

    def changeAttacherType(self, typename: str, /) -> bool:
        """
        changeAttacherType(typename): Changes Attacher class of this object.
        typename: string. The following are accepted so far:
        'Attacher::AttachEngine3D'
        'Attacher::AttachEnginePlane'
        'Attacher::AttachEngineLine'
        'Attacher::AttachEnginePoint'
        Possible exceptions: (Part.OCCError, FreeCAD.FreeCADError).
        """

    def positionBySupport(self) -> bool:
        """
        positionBySupport(): Reposition object based on Support, MapMode and MapPathParameter properties.
        Returns True if attachment calculation was successful, false if object is not attached and Placement wasn't updated,
        and raises an exception if attachment calculation fails.
        Possible exceptions: (Part.OCCError, FreeCAD.FreeCADError).
        """


# Part2DObjectPy.xml
class Part2DObject(PartModule.Feature):
    """This object represents a 2D Shape in a 3D World"""


# ArcOfEllipsePy.xml
class ArcOfEllipse(PartModule.ArcOfConic):
    """
    This class can be imported.
    Describes a portion of an ellipse
    """

    def __init__(self, arg1: PartModule.Ellipse, arg2: float, arg3: float, arg4: bool = None, /):
        """
        Describes a portion of an ellipse
        Possible exceptions: (Part.OCCError, TypeError).
        """

    @property
    def Ellipse(self) -> PartModule.Ellipse:
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


# BezierSurfacePy.xml
class BezierSurface(PartModule.GeometrySurface):
    """
    This class can be imported.
    Describes a rational or non-rational Bezier surface
    				-- A non-rational Bezier surface is defined by a table of poles (also known as control points).
    				-- A rational Bezier surface is defined by a table of poles with varying associated weights.
    """

    @property
    def MaxDegree(self) -> int:
        """
        Returns the value of the maximum polynomial degree of any
        					Bezier surface. This value is 25.
        """

    @property
    def NbUPoles(self) -> int:
        """Returns the number of poles in u direction of this Bezier surface."""

    @property
    def NbVPoles(self) -> int:
        """Returns the number of poles in v direction of this Bezier surface."""

    @property
    def UDegree(self) -> int:
        """
        Returns the polynomial degree in u direction of this Bezier surface,
        					which is equal to the number of poles minus 1.
        """

    @property
    def VDegree(self) -> int:
        """
        Returns the polynomial degree in v direction of this Bezier surface,
        					which is equal to the number of poles minus 1.
        """

    def bounds(self) -> tuple[float, float, float, float]:
        """Returns the parametric bounds (U1, U2, V1, V2) of this Bezier surface."""

    def exchangeUV(self):
        """
        Exchanges the u and v parametric directions on this Bezier surface.
        					As a consequence:
        					-- the poles and weights tables are transposed,
        					-- degrees, rational characteristics and so on are exchanged between
        					   the two parametric directions, and
        					-- the orientation of the surface is reversed.
				
        Possible exceptions: (Part.OCCError).
        """

    def getPole(self, arg1: int, arg2: int, /) -> FreeCAD.Vector:
        """
        Get a pole of index (UIndex,VIndex) of the Bezier surface.
        Possible exceptions: (Part.OCCError).
        """

    def getPoles(self) -> list[list[FreeCAD.Vector]]:
        """
        Get all poles of the Bezier surface.
        Possible exceptions: (Part.OCCError).
        """

    def getResolution(self, arg1: float, /) -> tuple[float, float]:
        """
        Computes two tolerance values for this Bezier surface, based on the
        					given tolerance in 3D space Tolerance3D. The tolerances computed are:
        					-- UTolerance in the u parametric direction and
        					-- VTolerance in the v parametric direction.

        					If f(u,v) is the equation of this Bezier surface, UTolerance and VTolerance
        					guarantee that:
        					|u1 - u0| < UTolerance
        					|v1 - v0| < VTolerance
        					====> ||f(u1, v1) - f(u2, v2)|| < Tolerance3D
				
        Possible exceptions: (Part.OCCError).
        """

    def getWeight(self, arg1: int, arg2: int, /) -> float:
        """
        Get a weight of the pole of index (UIndex,VIndex)
        					of the Bezier surface.
				
        Possible exceptions: (Part.OCCError).
        """

    def getWeights(self) -> list[list[float]]:
        """
        Get all weights of the Bezier surface.
        Possible exceptions: (Part.OCCError).
        """

    def increase(self, Int: int, Int2: int, /):
        """
        increase(Int=DegreeU,Int=DegreeV)
        					Increases the degree of this Bezier surface in the two
        					parametric directions.
				
        Possible exceptions: (Part.OCCError).
        """

    def insertPoleColAfter(self, arg1: int, arg2, arg3=None, /):
        """
        Inserts into the table of poles of this surface, after the column
        					of poles of index.
        					If this Bezier surface is non-rational, it can become rational if
        					the weights associated with the new poles are different from each
        					other, or collectively different from the existing weights in the
        					table.
				
        Possible exceptions: (Part.OCCError).
        """

    def insertPoleColBefore(self, arg1: int, arg2, arg3=None, /):
        """
        Inserts into the table of poles of this surface, before the column
        					of poles of index.
        					If this Bezier surface is non-rational, it can become rational if
        					the weights associated with the new poles are different from each
        					other, or collectively different from the existing weights in the
        					table.
				
        Possible exceptions: (Part.OCCError).
        """

    def insertPoleRowAfter(self, arg1: int, arg2, arg3=None, /):
        """
        Inserts into the table of poles of this surface, after the row
        					of poles of index.
        					If this Bezier surface is non-rational, it can become rational if
        					the weights associated with the new poles are different from each
        					other, or collectively different from the existing weights in the
        					table.
				
        Possible exceptions: (Part.OCCError).
        """

    def insertPoleRowBefore(self, arg1: int, arg2, arg3=None, /):
        """
        Inserts into the table of poles of this surface, before the row
        					of poles of index.
        					If this Bezier surface is non-rational, it can become rational if
        					the weights associated with the new poles are different from each
        					other, or collectively different from the existing weights in the
        					table.
				
        Possible exceptions: (Part.OCCError).
        """

    def isUClosed(self) -> bool:
        """
        Checks if this surface is closed in the u parametric direction.
        					Returns true if, in the table of poles the first row and the last
        					row are identical.
        """

    def isUPeriodic(self) -> bool:
        """Returns false."""

    def isURational(self) -> bool:
        """
        Returns false if the equation of this Bezier surface is polynomial
        					(e.g. non-rational) in the u or v parametric direction.
        					In other words, returns false if for each row of poles, the associated
        					weights are identical
        """

    def isVClosed(self) -> bool:
        """
        Checks if this surface is closed in the v parametric direction.
        					Returns true if, in the table of poles the first column and the
        					last column are identical.
        """

    def isVPeriodic(self) -> bool:
        """Returns false."""

    def isVRational(self) -> bool:
        """
        Returns false if the equation of this Bezier surface is polynomial
        					(e.g. non-rational) in the u or v parametric direction.
        					In other words, returns false if for each column of poles, the associated
        					weights are identical
        """

    def removePoleCol(self, arg1: int, /):
        """
        removePoleRow(int=VIndex)
        					Removes the column of poles of index VIndex from the table of
        					poles of this Bezier surface.
        					If this Bezier curve is rational, it can become non-rational.
				
        Possible exceptions: (Part.OCCError).
        """

    def removePoleRow(self, int: int, /):
        """
        removePoleRow(int=UIndex)
        					Removes the row of poles of index UIndex from the table of
        					poles of this Bezier surface.
        					If this Bezier curve is rational, it can become non-rational.
				
        Possible exceptions: (Part.OCCError).
        """

    def segment(self, double: float, double2: float, double3: float, double4: float, /):
        """
        segment(double=U1,double=U2,double=V1,double=V2)
        					Modifies this Bezier surface by segmenting it between U1 and U2
        					in the u parametric direction, and between V1 and V2 in the v
        					parametric direction.
        					U1, U2, V1, and V2 can be outside the bounds of this surface.
					
        					-- U1 and U2 isoparametric Bezier curves, segmented between
        					   V1 and V2, become the two bounds of the surface in the v
        					   parametric direction (0. and 1. u isoparametric curves).
        					-- V1 and V2 isoparametric Bezier curves, segmented between
        					   U1 and U2, become the two bounds of the surface in the u
        					   parametric direction (0. and 1. v isoparametric curves).
					
        					The poles and weights tables are modified, but the degree of
        					this surface in the u and v parametric directions does not
        					change.U1 can be greater than U2, and V1 can be greater than V2.
        					In these cases, the corresponding parametric direction is inverted.
        					The orientation of the surface is inverted if one (and only one)
        					parametric direction is inverted.
				
        Possible exceptions: (Part.OCCError).
        """

    def setPole(self, arg1: int, arg2: int, arg3: FreeCAD.Vector, arg4: float = None, /):
        """
        Set a pole of the Bezier surface.
        Possible exceptions: (Part.OCCError).
        """

    def setPoleCol(self, arg1: int, arg2, arg3=None, /):
        """
        Set the column of poles of the Bezier surface.
        Possible exceptions: (Part.OCCError).
        """

    def setPoleRow(self, arg1: int, arg2, arg3=None, /):
        """
        Set the row of poles of the Bezier surface.
        Possible exceptions: (Part.OCCError).
        """

    def setWeight(self, arg1: int, arg2: int, arg3: float, /):
        """
        Set the weight of pole of the index (UIndex, VIndex)
        					for the Bezier surface.
				
        Possible exceptions: (Part.OCCError).
        """

    def setWeightCol(self, arg1: int, arg2, /):
        """
        Set the weights of the poles in the column of poles
        					of index VIndex of the Bezier surface.
				
        Possible exceptions: (Part.OCCError).
        """

    def setWeightRow(self, arg1: int, arg2, /):
        """
        Set the weights of the poles in the row of poles
        					of index UIndex of the Bezier surface.
				
        Possible exceptions: (Part.OCCError).
        """

    def uIso(self, arg1: float, /) -> PartModule.BezierCurve:
        """
        Builds the U isoparametric Bezier curve of this Bezier surface
        Possible exceptions: (Part.OCCError).
        """

    def vIso(self, arg1: float, /) -> PartModule.BezierCurve:
        """
        Builds the V isoparametric Bezier curve of this Bezier surface
        Possible exceptions: (Part.OCCError).
        """


# BodyBasePy.xml
class BodyBase(PartModule.Feature):
    """Base class of all Body objects"""

    @property
    def BaseFeature(self) -> FreeCAD.DocumentObject | None:
        """Property TypeId: App::PropertyLink."""

    @BaseFeature.setter
    def BaseFeature(self, value: FreeCAD.DocumentObject | None): ...

    @property
    def Tip(self) -> FreeCAD.DocumentObject | None:
        """Property TypeId: App::PropertyLink."""

    @Tip.setter
    def Tip(self, value: FreeCAD.DocumentObject | None): ...


# ArcOfConicPy.xml
class ArcOfConic(PartModule.TrimmedCurve):
    """
    This class can be imported.
    Describes a portion of a conic
    """

    @property
    def AngleXU(self) -> float:
        """The angle between the X axis and the major axis of the conic."""

    @AngleXU.setter
    def AngleXU(self, value: float): ...

    @property
    def Axis(self) -> FreeCAD.Vector:
        """The axis direction of the conic"""

    @Axis.setter
    def Axis(self, value: FreeCAD.Vector): ...

    @property
    def Center(self) -> FreeCAD.Vector:
        """Deprecated -- use Location."""

    @Center.setter
    def Center(self, value: FreeCAD.Vector): ...

    @property
    def Location(self) -> FreeCAD.Vector:
        """Center of the conic."""

    @Location.setter
    def Location(self, value: FreeCAD.Vector): ...

    @property
    def XAxis(self) -> FreeCAD.Vector:
        """The X axis direction of the circle"""

    @XAxis.setter
    def XAxis(self, value: FreeCAD.Vector): ...

    @property
    def YAxis(self) -> FreeCAD.Vector:
        """The Y axis direction of the circle"""

    @YAxis.setter
    def YAxis(self, value: FreeCAD.Vector): ...


# AppPartPy.cpp
def open(string: str, /) -> None:
    """open(string) -- Create a new document and load the file into the document."""


def insert(string: str, string1: str, /) -> None:
    """insert(string,string) -- Insert the file into the given document."""


def export(list, string: str, /) -> None:
    """export(list,string) -- Export a list of objects into a single file."""


def read(string: str, /) -> PartModule.Shape:
    """read(string) -- Load the file and return the shape."""


def show(shape: PartModule.Shape, string: str = None, /) -> None:
    """show(shape,[string]) -- Add the shape to the active document or create one if no document exists."""


def makeCompound(list, /) -> PartModule.Compound:
    """makeCompound(list) -- Create a compound out of a list of shapes."""


def makeShell(list, /) -> PartModule.Shell:
    """makeShell(list) -- Create a shell out of a list of faces."""


def makeFace(list_of_shapes_or_compound, maker_class_name: str, /) -> PartModule.Shape | PartModule.Face | PartModule.Compound:
    """
    makeFace(list_of_shapes_or_compound, maker_class_name) -- Create a face (faces) using facemaker class.
    maker_class_name is a string like 'Part::FaceMakerSimple'.
    """


def makeFilledFace(arg1, arg2: PartModule.Face = None, /) -> PartModule.Face:
    """makeFilledFace(list) -- Create a face out of a list of edges."""


def makeSolid(shape: PartModule.Shape, /) -> PartModule.Solid | None:
    """makeSolid(shape): Create a solid out of shells of shape. If shape is a compsolid, the overall volume solid is created."""


def makePlane(length: float, width: float, pnt: FreeCAD.Vector = None, dirZ: FreeCAD.Vector = None, dirX: FreeCAD.Vector = None, /) -> PartModule.Face:
    """
    makePlane(length,width,[pnt,dirZ,dirX]) -- Make a plane
    By default pnt=Vector(0,0,0) and dirZ=Vector(0,0,1), dirX is ignored in this case
    """


def makeBox(length: float, width: float, height: float, pnt: FreeCAD.Vector = None, dir: FreeCAD.Vector = None, /) -> PartModule.Solid:
    """
    makeBox(length,width,height,[pnt,dir]) -- Make a box located
    in pnt with the dimensions (length,width,height)
    By default pnt=Vector(0,0,0) and dir=Vector(0,0,1)
    """


def makeWedge(arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: FreeCAD.Vector = None, arg12: FreeCAD.Vector = None, /) -> PartModule.Solid:
    """
    makeWedge(xmin, ymin, zmin, z2min, x2min,
    xmax, ymax, zmax, z2max, x2max,[pnt,dir])
     -- Make a wedge located in pnt
    By default pnt=Vector(0,0,0) and dir=Vector(0,0,1)
    """


def makeLine(startpnt, endpnt, /) -> PartModule.Edge:
    """
    makeLine(startpnt,endpnt) -- Make a line between two points

    Args:
        startpnt (Vector or tuple): Vector or 3 element tuple 
            containing the x,y and z coordinates of the start point,
            i.e. (x1,y1,z1).
        endpnt (Vector or tuple): Vector or 3 element tuple 
            containing the x,y and z coordinates of the start point,
            i.e. (x1,y1,z1).

    Returns:
        Edge: Part.Edge object
    """


def makePolygon(arg1, arg2: bool = None, /) -> PartModule.Wire:
    """
    makePolygon(pntslist) -- Make a polygon from a list of points

    Args:
        pntslist (list(Vector)): list of Vectors representing the 
            points of the polygon.

    Returns:
        Wire: Part.Wire object. If the last point in the list is 
            not the same as the first point, the Wire will not be 
            closed and cannot be used to create a face.
    """


def makeCircle(radius: float, pnt: FreeCAD.Vector = None, dir: FreeCAD.Vector = None, angle1: float = None, angle2: float = None, /) -> PartModule.Edge:
    """
    makeCircle(radius,[pnt,dir,angle1,angle2]) -- Make a circle with a given radius
    By default pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=0 and angle2=360
    """


def makeSphere(radius: float, pnt: FreeCAD.Vector = None, dir: FreeCAD.Vector = None, angle1: float = None, angle2: float = None, angle3: float = None, /) -> PartModule.Solid:
    """
    makeSphere(radius,[pnt, dir, angle1,angle2,angle3]) -- Make a sphere with a given radius
    By default pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=0, angle2=90 and angle3=360
    """


def makeCylinder(radius: float, height: float, pnt: FreeCAD.Vector = None, dir: FreeCAD.Vector = None, angle: float = None, /) -> PartModule.Solid:
    """
    makeCylinder(radius,height,[pnt,dir,angle]) -- Make a cylinder with a given radius and height
    By default pnt=Vector(0,0,0),dir=Vector(0,0,1) and angle=360
    """


def makeCone(radius1: float, radius2: float, height: float, pnt: FreeCAD.Vector = None, dir: FreeCAD.Vector = None, angle: float = None, /) -> PartModule.Solid:
    """
    makeCone(radius1,radius2,height,[pnt,dir,angle]) -- Make a cone with given radii and height
    By default pnt=Vector(0,0,0), dir=Vector(0,0,1) and angle=360
    """


def makeTorus(radius1: float, radius2: float, pnt: FreeCAD.Vector = None, dir: FreeCAD.Vector = None, angle1: float = None, angle2: float = None, angle: float = None, /) -> PartModule.Solid:
    """
    makeTorus(radius1,radius2,[pnt,dir,angle1,angle2,angle]) -- Make a torus with a given radii and angles
    By default pnt=Vector(0,0,0),dir=Vector(0,0,1),angle1=0,angle1=360 and angle=360
    """


def makeHelix(arg1: float, arg2: float, arg3: float, arg4: float = None, arg5: bool = None, arg6: bool = None, /) -> PartModule.Wire:
    """
    makeHelix(pitch,height,radius,[angle]) -- Make a helix with a given pitch, height and radius
    By default a cylindrical surface is used to create the helix. If the fourth parameter is set
    (the apex given in degree) a conical surface is used instead
    """


def makeLongHelix(pitch: float, height: float, radius: float, angle: float = None, hand: bool = None, /) -> PartModule.Wire:
    """
    makeLongHelix(pitch,height,radius,[angle],[hand]) -- Make a (multi-edge) helix with a given pitch, height and radius
    By default a cylindrical surface is used to create the helix. If the fourth parameter is set
    (the apex given in degree) a conical surface is used instead.
    """


def makeThread(pitch: float, depth: float, height: float, radius: float, /) -> PartModule.Wire:
    """makeThread(pitch,depth,height,radius) -- Make a thread with a given pitch, depth, height and radius"""


def makeRevolution(Curve: PartModule.Geometry, vmin: float = None, vmax: float = None, angle: float = None, pnt: FreeCAD.Vector = None, dir: FreeCAD.Vector = None, shapetype: type = None, /) -> PartModule.Solid | PartModule.Shell | PartModule.Face | PartModule.Shape:
    """
    makeRevolution(Curve,[vmin,vmax,angle,pnt,dir,shapetype]) -- Make a revolved shape
    by rotating the curve or a portion of it around an axis given by (pnt,dir).
    By default vmin/vmax=bounds of the curve,angle=360,pnt=Vector(0,0,0) and
    dir=Vector(0,0,1) and shapetype=Part.Solid
    """


def makeRuledSurface(Edge_Wire: PartModule.Shape, Edge_Wire1: PartModule.Shape, /) -> PartModule.Face | PartModule.Shell:
    """
    makeRuledSurface(Edge|Wire,Edge|Wire) -- Make a ruled surface
    Create a ruled surface out of two edges or wires. If wires are used thenthese must have the same number of edges.
    """


def makeTube(edge: PartModule.Shape, radius: float, continuity: str = None, max_degree: int = None, max_segments: int = None, /) -> PartModule.Face:
    """
    makeTube(edge,radius,[continuity,max degree,max segments]) -- Create a tube.
    continuity is a string which must be 'C0','C1','C2','C3','CN','G1' or 'G1',
    """


def makeSweepSurface(arg1: PartModule.Shape, arg2: PartModule.Shape, arg3: float = None, arg4: int = None, /) -> PartModule.Face:
    """makeSweepSurface(edge(path),edge(profile),[float]) -- Create a profile along a path."""


def makeLoft(list_of_wires, solid: bool = False, ruled: bool = False, closed: bool = False, maxDegree: int = 5, /) -> PartModule.BSplineSurface | PartModule.Shape:
    """makeLoft(list of wires,[solid=False,ruled=False,closed=False,maxDegree=5]) -- Create a loft shape."""


def makeWireString(string, fontdir: str, fontfile: str, height: float, track: float = None, /):
    """makeWireString(string,fontdir,fontfile,height,[track]) -- Make list of wires in the form of a string's characters."""


def makeSplitShape(shape: PartModule.Shape, list_of_shape_pairs, check_Interior: bool = True, /) -> tuple[list[Part.Shape], list[Part.Shape]]:
    """
    makeSplitShape(shape, list of shape pairs,[check Interior=True]) -> two lists of shapes.
    The following shape pairs are supported:
    * Wire, Face
    * Edge, Face
    * Compound, Face
    * Edge, Edge
    * The face must be part of the specified shape and the edge, wire or compound must
    lie on the face.
    Output:
    The first list contains the faces that are the left of the projected wires.
    The second list contains the left part on the shape.

    Example:
    face = ...
    edges = ...
    split = [(edges[0],face),(edges[1],face)]
    r = Part.makeSplitShape(face, split)
    Part.show(r[0][0])
    Part.show(r[1][0])
    """


def exportUnits(string: str = None, /) -> ReturnExportUnitsDict:
    """exportUnits([string=MM|M|IN]) -- Set units for exporting STEP/IGES files and returns the units."""


@typing.overload
def setStaticValue(string: str, string_int_float: str, /) -> None: ...


@typing.overload
def setStaticValue(string: str, string_int_float, /) -> None:
    """setStaticValue(string,string|int|float) -- Set a name to a value The value can be a string, int or float."""


def cast_to_shape(shape: PartModule.Shape, /) -> PartModule.Compound | PartModule.CompSolid | PartModule.Solid | PartModule.Shell | PartModule.Face | PartModule.Wire | PartModule.Edge | PartModule.Vertex | PartModule.Shape:
    """cast_to_shape(shape) -- Cast to the actual shape type"""


def getSortedClusters(list_of_edges, /) -> list[list[PartModule.Edge]]:
    """getSortedClusters(list of edges) -- Helper method to sort and cluster a variety of edges"""


def __sortEdges__(list_of_edges, /) -> list[PartModule.Edge]:
    """
    __sortEdges__(list of edges) -- Helper method to sort an unsorted list of edges so that afterwards
    two adjacent edges share a common vertex
    """


def sortEdges(list_of_edges, /) -> list[list[PartModule.Edge]]:
    """sortEdges(list of edges) -- Helper method to sort a list of edges into a list of list of connected edges"""


def __toPythonOCC__(shape: PartModule.Shape, /):
    """__toPythonOCC__(shape) -- Helper method to convert an internal shape to pythonocc shape"""


def __fromPythonOCC__(occ, /) -> PartModule.Shape:
    """__fromPythonOCC__(occ) -- Helper method to convert a pythonocc shape to an internal shape"""


# AttacherTexts.cpp
def getModeStrings(attacher_type: str, mode_index: int, /) -> list[str]:
    """getModeStrings(attacher_type, mode_index) - gets mode user-friendly name and brief description."""


def getRefTypeUserFriendlyName(type_index: int, /) -> str:
    """getRefTypeUserFriendlyName(type_index) - gets user-friendly name of AttachEngine's shape type."""


class OCCError(FreeCAD.Base.FreeCADError):
    pass


class OCCDomainError(OCCError):
    pass


class OCCRangeError(OCCDomainError):
    pass


class OCCConstructionError(OCCDomainError):
    pass


class OCCDimensionError(OCCDomainError):
    pass
