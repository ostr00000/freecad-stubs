import typing

import FreeCAD
import Part


# TopoShapeVertexPy.xml
class TopoShape(Part.TopoShape):
    """TopoShapeVertex is the OpenCasCade topological vertex wrapper"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: float = None, arg2: float = None, arg3: float = None, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, arg1: tuple, /): ...

    @typing.overload
    def __init__(self, arg1: Part.Point, /): ...

    @typing.overload
    def __init__(self, arg1: Part.TopoShape, /):
        """TopoShapeVertex is the OpenCasCade topological vertex wrapper"""

    @property
    def Point(self) -> object:
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
class Cylinder(Part.GeometrySurface):
    """Describes a cylinder in 3D space
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
    def __init__(self, Cylinder: Part.Cylinder): ...

    @typing.overload
    def __init__(self, Circle: Part.Circle): ...

    @typing.overload
    def __init__(self, Cylinder: Part.Cylinder, Distance: float): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, Point3: FreeCAD.Vector):
        """Describes a cylinder in 3D space
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

    @property
    def Axis(self) -> object:
        """The axis direction of the cylinder"""

    @Axis.setter
    def Axis(self, value: object): ...

    @property
    def Center(self) -> object:
        """Center of the cylinder."""

    @Center.setter
    def Center(self, value: object): ...

    @property
    def Radius(self) -> float:
        """The radius of the cylinder."""

    @Radius.setter
    def Radius(self, value: float): ...


# GeometryBoolExtensionPy.xml
class GeometryBoolExtension(Part.GeometryExtension):
    """A GeometryExtension extending geometry objects with a boolean."""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: bool, /): ...

    @typing.overload
    def __init__(self, arg1: bool, arg2: str, /):
        """A GeometryExtension extending geometry objects with a boolean."""

    @property
    def Value(self) -> bool:
        """
                        returns the value of the GeometryBoolExtension.
                    """

    @Value.setter
    def Value(self, value: bool): ...


# AttachEnginePy.xml
class AttachEngine(FreeCAD.BaseClass):
    """AttachEngine abstract class - the functionality of AttachableObject, but outside of DocumentObject"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: Part.AttachEngine, /): ...

    @typing.overload
    def __init__(self, arg1: str, /):
        """AttachEngine abstract class - the functionality of AttachableObject, but outside of DocumentObject"""

    @property
    def AttacherType(self) -> str:
        """Type of engine: 3d, plane, line, or point."""

    @property
    def AttachmentOffset(self) -> object:
        """Current attachment mode."""

    @AttachmentOffset.setter
    def AttachmentOffset(self, value: object): ...

    @property
    def CompleteModeList(self) -> list:
        """List of all attachment modes of all AttachEngines. This is the list of modes in MapMode enum properties of AttachableObjects."""

    @property
    def CompleteRefTypeList(self) -> list:
        """List of all reference shape types recognized by AttachEngine."""

    @property
    def ImplementedModes(self) -> list:
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

    def calculateAttachedPlacement(self, orig_placement: FreeCAD.Placement, /):
        """calculateAttachedPlacement(orig_placement): returns result of attachment, based
        on current Mode, References, etc. AttachmentOffset is included.

        original_placement is the previous placement of the object being attached. It
        is used to preserve orientation for Translate attachment mode. For other modes,
        it is ignored.

        Returns the new placement. If not attached, returns None. If attachment fails,
        an exception is raised."""

    def copy(self):
        """copy(): returns a new instance of AttachEngine."""

    def downgradeRefType(self, type: str, /):
        """downgradeRefType(type): returns next more general type. E.g. downgradeType('Circle') yields 'Curve'."""

    def getModeInfo(self, mode: str, /):
        """getModeInfo(mode): returns supported reference combinations, user-friendly name, and so on."""

    def getRefTypeInfo(self, type: str, /):
        """getRefTypeInfo(type): returns information (dict) on shape type. Keys:'UserFriendlyName', 'TypeIndex', 'Rank'. Rank is the number of times reftype can be downgraded, before it becomes 'Any'."""

    def getRefTypeOfShape(self, shape: Part.TopoShape, /):
        """getRefTypeOfShape(shape): returns shape type as interpreted by AttachEngine. Returns a string."""

    def isFittingRefType(self, type_shape: str, type_needed: str, /):
        """isFittingRefType(type_shape, type_needed): tests if shape type, specified by type_shape (string), fits a type required by attachment mode type_needed (string). e.g. 'Circle' fits a requirement of 'Edge', and 'Curve' doesn't fit if a 'Circle' is required."""

    def readParametersFromFeature(self, document_object: FreeCAD.DocumentObject, /):
        """readParametersFromFeature(document_object): sets AttachEngine parameters (References, Mode, etc.) by reading out properties of AttachableObject-derived feature."""

    def suggestModes(self):
        """suggestModes(): runs mode suggestion routine and returns a dictionary with
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
        the input information for suggestor, actually)."""

    def writeParametersToFeature(self, document_object: FreeCAD.DocumentObject, /):
        """writeParametersToFeature(document_object): updates properties of
        AttachableObject-derived feature with current AttachEngine parameters
        (References, Mode, etc.).

        Warning: if a feature linked by AttachEngine.References was deleted, this method
        will crash FreeCAD."""


# EllipsePy.xml
class Ellipse(Part.Conic):
    """Describes an ellipse in 3D space
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
    def __init__(self, Ellipse: Part.Ellipse): ...

    @typing.overload
    def __init__(self, S1: FreeCAD.Vector, S2: FreeCAD.Vector, Center: FreeCAD.Vector): ...

    @typing.overload
    def __init__(self, Center: FreeCAD.Vector, MajorRadius: float, MinorRadius: float):
        """Describes an ellipse in 3D space
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

    @property
    def Focal(self) -> float:
        """The focal distance of the ellipse."""

    @property
    def Focus1(self) -> object:
        """The first focus is on the positive side of the major axis of the ellipse;
        the second focus is on the negative side."""

    @property
    def Focus2(self) -> object:
        """The first focus is on the positive side of the major axis of the ellipse;
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
class TopoShape(Part.TopoShape):
    """Part.Solid(shape): Create a solid out of shells of shape. If shape is a compsolid, the overall volume solid is created."""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: Part.TopoShape, /):
        """Part.Solid(shape): Create a solid out of shells of shape. If shape is a compsolid, the overall volume solid is created."""

    @property
    def CenterOfMass(self) -> object:
        """Returns the center of mass of the current system.
        If the gravitational field is uniform, it is the center of gravity.
        The coordinates returned for the center of mass are expressed in the
        absolute Cartesian coordinate system."""

    @property
    def Mass(self) -> object:
        """Returns the mass of the current system."""

    @property
    def MatrixOfInertia(self) -> object:
        """Returns the matrix of inertia. It is a symmetrical matrix.
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
        coordinate system."""

    @property
    def OuterShell(self) -> object:
        """
        Returns the outer most shell of this solid or an null
        shape if the solid has no shells"""

    @property
    def PrincipalProperties(self) -> dict:
        """Computes the principal properties of inertia of the current system.
         There is always a set of axes for which the products
         of inertia of a geometric system are equal to 0; i.e. the
         matrix of inertia of the system is diagonal. These axes
         are the principal axes of inertia. Their origin is
         coincident with the center of mass of the system. The
         associated moments are called the principal moments of inertia.
         This function computes the eigen values and the
         eigen vectors of the matrix of inertia of the system."""

    @property
    def StaticMoments(self) -> object:
        """Returns Ix, Iy, Iz, the static moments of inertia of the
         current system; i.e. the moments of inertia about the
         three axes of the Cartesian coordinate system."""

    def getMomentOfInertia(self, point: FreeCAD.Vector, direction: FreeCAD.Vector, /):
        """computes the moment of inertia of the material system about the axis A.
        getMomentOfInertia(point,direction) -> Float
                """

    def getRadiusOfGyration(self, point: FreeCAD.Vector, direction: FreeCAD.Vector, /):
        """Returns the radius of gyration of the current system about the axis A.
        getRadiusOfGyration(point,direction) -> Float
                """

    @typing.overload
    def offsetFaces(self, facesTuple: object, offset: float, /): ...

    @typing.overload
    def offsetFaces(self, dict: dict, /): ...

    @typing.overload
    def offsetFaces(self, arg: object, arg2: float, /): ...

    @typing.overload
    def offsetFaces(self, arg: object, solid_Faces_1_2_0_: float, /):
        """Extrude single faces of the solid.
        offsetFaces(facesTuple, offset) -> Solid
        or
        offsetFaces(dict) -> Solid
        --
        Example:
        solid.offsetFaces((solid.Faces[0],solid.Faces[1]), 1.5)

        solid.offsetFaces({solid.Faces[0]:1.0,solid.Faces[1]:2.0})
                """


# BoundedCurvePy.xml
class BoundedCurve(Part.Curve):
    """
                    The abstract class BoundedCurve is the root class of all bounded curve objects.
                """

    @property
    def EndPoint(self) -> object:
        """
                            Returns the end point of the bounded curve.
                        """

    @property
    def StartPoint(self) -> object:
        """
                            Returns the starting point of the bounded curve.
        		"""


# HyperbolaPy.xml
class Hyperbola(Part.Conic):
    """Describes an hyperbola in 3D space
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
    def __init__(self, Hyperbola: Part.Hyperbola): ...

    @typing.overload
    def __init__(self, S1: FreeCAD.Vector, S2: FreeCAD.Vector, Center: FreeCAD.Vector): ...

    @typing.overload
    def __init__(self, Center: FreeCAD.Vector, MajorRadius: float, MinorRadius: float):
        """Describes an hyperbola in 3D space
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

    @property
    def Focal(self) -> float:
        """The focal distance of the hyperbola."""

    @property
    def Focus1(self) -> object:
        """The first focus is on the positive side of the major axis of the hyperbola;
        the second focus is on the negative side."""

    @property
    def Focus2(self) -> object:
        """The first focus is on the positive side of the major axis of the hyperbola;
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
class PlateSurface(Part.GeometrySurface):
    def __init__(self, Surface: Part.Geometry = None, Points: object = None, Curves: object = None, Degree: int = None, NbPtsOnCur: int = None, NbIter: int = None, Tol2d: float = None, Tol3d: float = None, TolAng: float = None, TolCurv: float = None, Anisotropie: bool = None): ...

    def makeApprox(self, Tol3d: float = None, MaxSegments: int = None, MaxDegree: int = None, MaxDistance: float = None, CritOrder: int = None, Continuity: str = None, EnlargeCoeff: float = None):
        """Approximate the plate surface to a B-Spline surface"""


# OffsetCurvePy.xml
class OffsetCurve(Part.Curve):
    def __init__(self, arg1: Part.Geometry, arg2: float, arg3: FreeCAD.Vector, /): ...

    @property
    def BasisCurve(self) -> object:
        """
        					Sets or gets the basic curve.
        				"""

    @property
    def OffsetDirection(self) -> object:
        """
        					Sets or gets the offset direction to offset the underlying curve.
        				"""

    @property
    def OffsetValue(self) -> float:
        """
        					Sets or gets the offset value to offset the underlying curve.
        				"""


# CirclePy.xml
class Circle(Part.Conic):
    """Describes a circle in 3D space
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
    def __init__(self, Circle: Part.Circle): ...

    @typing.overload
    def __init__(self, Circle: Part.Circle, Distance: float): ...

    @typing.overload
    def __init__(self, Center: FreeCAD.Vector, Normal: FreeCAD.Vector, Radius: float): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, Point3: FreeCAD.Vector):
        """Describes a circle in 3D space
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

    @property
    def Radius(self) -> float:
        """The radius of the circle."""

    @Radius.setter
    def Radius(self, value: float): ...


# ArcPy.xml
class Arc(Part.TrimmedCurve):
    """Describes a portion of a curve"""

    @typing.overload
    def __init__(self, arg1: Part.Circle, arg2: float, arg3: float, arg4: bool = None, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, arg3: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, arg1: Part.Ellipse, arg2: float, arg3: float, arg4: bool = None, /): ...

    @typing.overload
    def __init__(self, arg1: Part.Parabola, arg2: float, arg3: float, arg4: bool = None, /): ...

    @typing.overload
    def __init__(self, arg1: Part.Hyperbola, arg2: float, arg3: float, arg4: bool = None, /):
        """Describes a portion of a curve"""


# OffsetSurfacePy.xml
class OffsetSurface(Part.GeometrySurface):
    def __init__(self, arg1: Part.Geometry, arg2: float, /): ...

    @property
    def BasisSurface(self) -> object:
        """
        					Sets or gets the basic surface.
        				"""

    @property
    def OffsetValue(self) -> float:
        """
        					Sets or gets the offset value to offset the underlying surface.
        				"""


# PlanePy.xml
class Plane(Part.GeometrySurface):
    """Describes an infinite plane
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
    def __init__(self, Plane: Part.Plane): ...

    @typing.overload
    def __init__(self, Plane: Part.Plane, Distance: float): ...

    @typing.overload
    def __init__(self, Location: FreeCAD.Vector, Normal: FreeCAD.Vector): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, Point3: FreeCAD.Vector): ...

    @typing.overload
    def __init__(self, A: float, B: float, C: float, D: float):
        """Describes an infinite plane
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

    @property
    def Axis(self) -> object:
        """Returns the axis of this plane."""

    @Axis.setter
    def Axis(self, value: object): ...

    @property
    def Position(self) -> object:
        """Returns the position point of this plane."""

    @Position.setter
    def Position(self, value: object): ...


# TopoShapeFacePy.xml
class TopoShape(Part.TopoShape):
    """TopoShapeFace is the OpenCasCade topological face wrapper"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: Part.TopoShape, /): ...

    @typing.overload
    def __init__(self, arg1: Part.TopoShape, arg2: Part.TopoShape, /): ...

    @typing.overload
    def __init__(self, arg1: Part.GeometrySurface, arg2: Part.TopoShape, /): ...

    @typing.overload
    def __init__(self, arg1: Part.Geometry, arg2: list = None, /): ...

    @typing.overload
    def __init__(self, arg1: list, /): ...

    @typing.overload
    def __init__(self, arg1: object, arg2: str, /):
        """TopoShapeFace is the OpenCasCade topological face wrapper"""

    @property
    def CenterOfMass(self) -> object:
        """Returns the center of mass of the current system.
        If the gravitational field is uniform, it is the center of gravity.
        The coordinates returned for the center of mass are expressed in the
        absolute Cartesian coordinate system."""

    @property
    def Mass(self) -> object:
        """Returns the mass of the current system."""

    @property
    def MatrixOfInertia(self) -> object:
        """Returns the matrix of inertia. It is a symmetrical matrix.
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
        coordinate system."""

    @property
    def OuterWire(self) -> object:
        """The outer wire of this face"""

    @property
    def ParameterRange(self) -> tuple:
        """Returns a 4 tuple with the parameter range"""

    @property
    def PrincipalProperties(self) -> dict:
        """Computes the principal properties of inertia of the current system.
         There is always a set of axes for which the products
         of inertia of a geometric system are equal to 0; i.e. the
         matrix of inertia of the system is diagonal. These axes
         are the principal axes of inertia. Their origin is
         coincident with the center of mass of the system. The
         associated moments are called the principal moments of inertia.
         This function computes the eigen values and the
         eigen vectors of the matrix of inertia of the system."""

    @property
    def StaticMoments(self) -> object:
        """Returns Ix, Iy, Iz, the static moments of inertia of the
         current system; i.e. the moments of inertia about the
         three axes of the Cartesian coordinate system."""

    @property
    def Surface(self) -> object:
        """Returns the geometric surface of the face"""

    @property
    def Tolerance(self) -> float:
        """Set or get the tolerance of the vertex"""

    @property
    def Wire(self) -> object:
        """The outer wire of this face
        deprecated -- please use OuterWire"""

    def addWire(self, wire: Part.TopoShape, /):
        """Adds a wire to the face.
        addWire(wire)
                        """

    def curvatureAt(self, u: float, v: float, /):
        """Get the curvature at the given parameter [0|Length] if defined
        curvatureAt(u,v) -> Float
                        """

    def curveOnSurface(self, Edge: Part.TopoShape, /):
        """Returns the curve associated to the edge in the parametric space of the face.
        curveOnSurface(Edge) -> (curve, min, max) or None
        --
        If this curve exists then a tuple of curve and parameter range is returned.
        Returns None if this curve  does not exist.
                        """

    def cutHoles(self, list_of_wires: list, /):
        """Cut holes in the face.
        cutHoles(list_of_wires)
                        """

    def derivative1At(self, u: float, v: float, /):
        """Get the first derivative at the given parameter [0|Length] if defined
        derivative1At(u,v) -> (vectorU,vectorV)
                        """

    def derivative2At(self, u: float, v: float, /):
        """Vector = d2At(pos) - Get the second derivative at the given parameter [0|Length] if defined
        derivative2At(u,v) -> (vectorU,vectorV)
                        """

    def getUVNodes(self):
        """Get the list of (u,v) nodes of the tessellation
        getUVNodes() -> list
        --
        An exception is raised if the face is not triangulated.
        """

    def isPartOfDomain(self, u: float, v: float, /):
        """Check if a given (u,v) pair is inside the domain of a face
        isPartOfDomain(u,v) -> bool
                        """

    def makeHalfSpace(self, pos: FreeCAD.Vector, /):
        """Make a half-space solid by this face and a reference point.
        makeHalfSpace(pos) -> Shape
                        """

    def makeOffset(self, dist: float, /):
        """Offset the face by a given amount.
        makeOffset(dist) -> Face
        --
        Returns Compound of Wires. Deprecated - use makeOffset2D instead.
                        """

    def normalAt(self, arg1: float, arg2: float, /):
        """Get the normal vector at the given parameter [0|Length] if defined
        normalAt(pos) -> Vector
                        """

    def tangentAt(self, u: float, v: float, /):
        """Get the tangent in u and v isoparametric at the given point if defined
        tangentAt(u,v) -> Vector
                        """

    def validate(self):
        """Validate the face.
        validate()
                        """

    def valueAt(self, u: float, v: float, /):
        """Get the point at the given parameter [0|Length] if defined
        valueAt(u,v) -> Vector
                        """


# BRepOffsetAPI_MakePipeShellPy.xml
class BRepOffsetAPI_MakePipeShell(FreeCAD.PyObjectBase):
    """Describes a portion of a circle"""

    @typing.overload
    def add(self, Profile: Part.TopoShape, WithContact: bool = False, WithCorrection: bool = False): ...

    @typing.overload
    def add(self, Profile: Part.TopoShape, Location: Part.TopoShape, WithContact: bool = False, WithCorrection: bool = False):
        """
        					add(shape Profile, bool WithContact=False, bool WithCorrection=False)
        					add(shape Profile, vertex Location, bool WithContact=False, bool WithCorrection=False)
        					Adds the section Profile to this framework.
        					First and last sections may be punctual, so the shape Profile may be both wire and vertex.
        					If WithContact is true, the section is translated to be in contact with the spine.
        					If WithCorrection is true, the section is rotated to be orthogonal to the spine tangent in the correspondent point.
        				"""

    def build(self):
        """
        					build()
        					Builds the resulting shape.
        				"""

    def firstShape(self):
        """
        					firstShape()
        					Returns the Shape of the bottom of the sweep.
        				"""

    def generated(self, shape_S: Part.TopoShape, /):
        """
        					generated(shape S)
        					Returns a list of new shapes generated from the shape S by the shell-generating algorithm.
        				"""

    def getStatus(self):
        """
        					getStatus()
        					Get a status, when Simulate or Build failed.
        				"""

    def isReady(self):
        """
        					isReady()
        					Returns true if this tool object is ready to build the shape.
        				"""

    def lastShape(self):
        """
        					lastShape()
        					Returns the Shape of the top of the sweep.
        				"""

    def makeSolid(self):
        """
        					makeSolid()
        					Transforms the sweeping Shell in Solid. If a propfile is not closed returns False.
        				"""

    def remove(self, shape_Profile: Part.TopoShape, /):
        """
        					remove(shape Profile)
        					Removes the section Profile from this framework.
        				"""

    @typing.overload
    def setAuxiliarySpine(self, wire: Part.TopoShape, CurvilinearEquivalence: bool, TypeOfContact: int, /): ...

    @typing.overload
    def setAuxiliarySpine(self, wire: Part.TopoShape, CurvilinearEquivalence: bool, TypeOfContact: bool, /):
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
        				"""

    def setBiNormalMode(self, direction: FreeCAD.Vector, /):
        """
        					setBiNormalMode(direction)
        					Sets a fixed BiNormal direction to perform the sweeping.
        					Angular relations between the section(s) and the BiNormal direction will be constant.
        				"""

    def setForceApproxC1(self, bool: bool, /):
        """
        					setForceApproxC1(bool)
        					Set the flag that indicates attempt to approximate a C1-continuous surface if a swept surface proved to be C0.
        				"""

    def setFrenetMode(self, True_False: bool, /):
        """
        					setFrenetMode(True|False)
        					Sets a Frenet or a CorrectedFrenet trihedron to perform the sweeping.
        					True  = Frenet
        					False = CorrectedFrenet
        				"""

    def setMaxDegree(self, int_degree: int, /):
        """
        					setMaxDegree(int degree)
        					Define the maximum V degree of resulting surface. 
        				"""

    def setMaxSegments(self, int_num: int, /):
        """
        					setMaxSegments(int num)
        					Define the maximum number of spans in V-direction on resulting surface.
        				"""

    def setSpineSupport(self, shape: Part.TopoShape, /):
        """
        					setSpineSupport(shape)
        					Sets support to the spine to define the BiNormal of the trihedron, like the normal to the surfaces.
        					Warning: To be effective, Each edge of the spine must have an representation on one face of SpineSupport.
        				"""

    def setTolerance(self, tol3d: float, boundTol: float, tolAngular: float, /):
        """
        					setTolerance( tol3d, boundTol, tolAngular)
        					Tol3d = 3D tolerance
        					BoundTol = boundary tolerance
        					TolAngular = angular tolerance
        				"""

    def setTransitionMode(self, arg1: int, /):
        """
        					0: BRepBuilderAPI_Transformed
        					1: BRepBuilderAPI_RightCorner
        					2: BRepBuilderAPI_RoundCorner
        				"""

    def setTrihedronMode(self, point: FreeCAD.Vector, direction: FreeCAD.Vector, /):
        """
        					setTrihedronMode(point,direction)
        					Sets a fixed trihedron to perform the sweeping.
        					All sections will be parallel. 
        				"""

    def shape(self):
        """
        					shape()
        					Returns the resulting shape.
        				"""

    def simulate(self, int_nbsec: int, /):
        """
        					simulate(int nbsec)
        					Simulates the resulting shape by calculating the given number of cross-sections.
        				"""


# TopoShapeCompSolidPy.xml
class TopoShape(Part.TopoShape):
    """TopoShapeCompSolid is the OpenCasCade topological compound solid wrapper"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: object, /):
        """TopoShapeCompSolid is the OpenCasCade topological compound solid wrapper"""

    def add(self, solid: Part.TopoShape, /):
        """Add a solid to the compound.
        add(solid)
                """


# ParabolaPy.xml
class Parabola(Part.Conic):
    """Describes a parabola in 3D space"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Parabola: Part.Parabola): ...

    @typing.overload
    def __init__(self, Focus: FreeCAD.Vector, Center: FreeCAD.Vector, Normal: FreeCAD.Vector):
        """Describes a parabola in 3D space"""

    @property
    def Focal(self) -> float:
        """The focal distance is the distance between
        the apex and the focus of the parabola."""

    @Focal.setter
    def Focal(self, value: float): ...

    @property
    def Focus(self) -> object:
        """The focus is on the positive side of the
        'X Axis' of the local coordinate system of the parabola."""

    @property
    def Parameter(self) -> float:
        """Compute the parameter of this parabola
        which is the distance between its focus
        and its directrix. This distance is twice the focal length.
        				"""

    def compute(self, p1: FreeCAD.Vector, p2: FreeCAD.Vector, p3: FreeCAD.Vector, /):
        """
        					compute(p1,p2,p3)
        					The three points must lie on a plane parallel to xy plane and must not be collinear
        				"""


# TopoShapePy.xml
class TopoShape(FreeCAD.ComplexGeoData):
    """TopoShape is the OpenCasCade topological shape wrapper.
    Sub-elements such as vertices, edges or faces are accessible as:
    * Vertex#, where # is in range(1, number of vertices)
    * Edge#, where # is in range(1, number of edges)
    * Face#, where # is in range(1, number of faces)"""

    def __init__(self, arg1: object = None, /):
        """TopoShape is the OpenCasCade topological shape wrapper.
        Sub-elements such as vertices, edges or faces are accessible as:
        * Vertex#, where # is in range(1, number of vertices)
        * Edge#, where # is in range(1, number of edges)
        * Face#, where # is in range(1, number of faces)"""

    @property
    def Area(self) -> float:
        """Total area of the faces of the shape."""

    @property
    def CompSolids(self) -> list:
        """List of subsequent shapes in this shape."""

    @property
    def Compounds(self) -> list:
        """List of compounds in this shape."""

    @property
    def Edges(self) -> list:
        """List of Edges in this shape."""

    @property
    def Faces(self) -> list:
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
    def Shells(self) -> list:
        """List of subsequent shapes in this shape."""

    @property
    def Solids(self) -> list:
        """List of subsequent shapes in this shape."""

    @property
    def SubShapes(self) -> list:
        """List of sub-shapes in this shape."""

    @property
    def Vertexes(self) -> list:
        """List of vertexes in this shape."""

    @property
    def Volume(self) -> float:
        """Total volume of the solids of the shape."""

    @property
    def Wires(self) -> list:
        """List of wires in this shape."""

    def ancestorsOfType(self, shape: Part.TopoShape, shape_type: type, /):
        """For a sub-shape of this shape get its ancestors of a type.
        ancestorsOfType(shape, shape type) -> list
                """

    def check(self, runBopCheck: bool = False, /):
        """Checks the shape and report errors in the shape structure.
        check([runBopCheck = False])
        --
        This is a more detailed check as done in isValid().
        if runBopCheck is True, a BOPCheck analysis is also performed."""

    def childShapes(self, cumOri: bool = True, cumLoc: bool = True, /):
        """Return a list of sub-shapes that are direct children of this shape.
        childShapes([cumOri=True, cumLoc=True]) -> list
        --
         * If cumOri is true, the function composes all
           sub-shapes with the orientation of this shape.
         * If cumLoc is true, the function multiplies all
           sub-shapes by the location of this shape, i.e. it applies to
           each sub-shape the transformation that is associated with this shape.
                """

    def cleaned(self):
        """This creates a cleaned copy of the shape with the triangulation removed.
        clean()
        --
        This can be useful to reduce file size when exporting as a BREP file.
        Warning: Use the cleaned shape with care because certain algorithms may work incorrectly
        if the shape has no internal triangulation any more.
        """

    @typing.overload
    def common(self, tool: Part.TopoShape, /): ...

    @typing.overload
    def common(self, arg: Part.TopoShape, tolerance: float, /): ...

    @typing.overload
    def common(self, arg: object, tolerance: float = 0.0, /):
        """Intersection of this and a given (list of) topo shape.
        common(tool) -> Shape
          or
        common((tool1,tool2,...),[tolerance=0.0]) -> Shape
        --
        Supports:
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation (s1 AND (s2 OR s3))
        - Parallelization of Boolean Operations algorithm

        OCC 6.9.0 or later is required."""

    def complement(self):
        """Computes the complement of the orientation of this shape,
        i.e. reverses the interior/exterior status of boundaries of this shape.
        complement()
                """

    def copy(self, copyGeom: bool = True, copyMesh: bool = False, /):
        """Create a copy of this shape
        copy(copyGeom=True, copyMesh=False) -> Shape
        --
        If copyMesh is True, triangulation contained in original shape will be
        copied along with geometry.
        If copyGeom is False, only topological objects will be copied, while
        geometry and triangulation will be shared with original shape.
        """

    def countElement(self, type: str, /):
        """Returns the count of a type of element
        countElement(type) -> int
                """

    @typing.overload
    def cut(self, tool: Part.TopoShape, /): ...

    @typing.overload
    def cut(self, arg: Part.TopoShape, tolerance: float, /): ...

    @typing.overload
    def cut(self, arg: object, tolerance: float = 0.0, /):
        """Difference of this and a given (list of) topo shape
        cut(tool) -> Shape
          or
        cut((tool1,tool2,...),[tolerance=0.0]) -> Shape
        --
        Supports:
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation
        - Parallelization of Boolean Operations algorithm

        OCC 6.9.0 or later is required."""

    def defeaturing(self, shapeList: object, /):
        """Remove a feature defined by supplied faces and return a new shape.
        defeaturing(shapeList) -> Shape
        --
        The parameter is a list of faces."""

    def distToShape(self, shape: Part.TopoShape, /):
        """Find the minimum distance to another shape.
        distToShape(shape) -> (dist, vectors, infos)
        --
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
            params is a tuple (u,v). """

    def dumpToString(self):
        """Dump information about the shape to a string.
        dumpToString() -> string"""

    def exportBinary(self, filename: str, /):
        """Export the content of this shape in binary format to a file.
        exportBinary(filename)
                """

    @typing.overload
    def exportBrep(self, filename: str, /): ...

    @typing.overload
    def exportBrep(self, filename: object, /):
        """Export the content of this shape to an BREP file.
        exportBrep(filename)
        --
        BREP is an OpenCasCade native format.
                """

    def exportBrepToString(self):
        """Export the content of this shape to a string in BREP format.
        exportBrepToString() -> string
        --
        BREP is an OpenCasCade native format."""

    def exportIges(self, filename: str, /):
        """Export the content of this shape to an IGES file.
        exportIges(filename)
                """

    def exportStep(self, filename: str, /):
        """Export the content of this shape to an STEP file.
        exportStep(filename)
                """

    def exportStl(self, arg1: str, arg2: float = None, /):
        """Export the content of this shape to an STL mesh file.
        exportStl(filename)"""

    def extrude(self, arg1: FreeCAD.Vector, /):
        """Extrude the shape along a direction.
        extrude(direction, length)"""

    def findPlane(self, tol: float = None, /):
        """return a plane if the shape is planar
        findPlane(tol=None) -> Shape
                  """

    def fix(self, working_precision: float, minimum_precision: float, maximum_precision: float, /):
        """Tries to fix a broken shape.
        fix(working precision, minimum precision, maximum precision) -> bool
        --
        True is returned if the operation succeeded, False otherwise.
                """

    def fixTolerance(self, value: float, ShapeType: type = None, /):
        """Sets (enforces) tolerances in a shape to the given value
        fixTolerance(value, [ShapeType=Shape])
        --
        ShapeType = Vertex : only vertices are set
        ShapeType = Edge   : only edges are set
        ShapeType = Face   : only faces are set
        ShapeType = Wire   : to have edges and their vertices set
        ShapeType = other value : all (vertices,edges,faces) are set
                """

    @typing.overload
    def fuse(self, tool: Part.TopoShape, /): ...

    @typing.overload
    def fuse(self, arg: Part.TopoShape, tolerance: float, /): ...

    @typing.overload
    def fuse(self, arg: object, tolerance: float = 0.0, /):
        """Union of this and a given (list of) topo shape.
        fuse(tool) -> Shape
          or
        fuse((tool1,tool2,...),[tolerance=0.0]) -> Shape
        --
        Union of this and a given list of topo shapes.

        Supports (OCCT 6.9.0 and above):
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation
        - Parallelization of Boolean Operations algorithm

        Beginning from OCCT 6.8.1 a tolerance value can be specified."""

    def generalFuse(self, list_of_other_shapes: object, fuzzy_value: float = 0.0, /):
        """Run general fuse algorithm (GFA) between this and given shapes.
        generalFuse(list_of_other_shapes, [fuzzy_value = 0.0]) -> (result, map)
        --
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
        """

    def getElement(self, elementName: str, /):
        """Returns a SubElement
        getElement(elementName) -> Face | Edge | Vertex
                """

    def getTolerance(self, mode: int, ShapeType: type = None, /):
        """Determines a tolerance from the ones stored in a shape
        getTolerance(mode, ShapeType=Shape) -> float
        --
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
                """

    def globalTolerance(self, mode: int, /):
        """Returns the computed tolerance according to the mode
        globalTolerance(mode) -> float
        --
        mode = 0 : average
        mode > 0 : maximal
        mode < 0 : minimal
                """

    def hashCode(self, arg1: int = None, /):
        """This value is computed from the value of the underlying shape reference and the location.
        hashCode() -> int
        --
        Orientation is not taken into account."""

    def importBinary(self, filename: str, /):
        """Import the content to this shape of a string in BREP format.
        importBinary(filename)"""

    @typing.overload
    def importBrep(self, filename: str, /): ...

    @typing.overload
    def importBrep(self, filename: object, /):
        """Load the shape from a file in BREP format.
        importBrep(filename)"""

    @typing.overload
    def importBrepFromString(self, string: str, displayProgressBar: int = True, /): ...

    @typing.overload
    def importBrepFromString(self, str: str, False_: int = None, /):
        """Load the shape from a string that keeps the content in BREP format.
        importBrepFromString(string, [displayProgressBar=True])
        --
        importBrepFromString(str,False) to not display a progress bar.
                """

    def inTolerance(self, arg1: float, arg2: float, arg3: type = None, /):
        """Determines which shapes have a tolerance within a given interval
        inTolerance(value, [ShapeType=Shape]) -> ShapeList
        --
        ShapeType is interpreted as in the method getTolerance
                """

    def isClosed(self):
        """Checks if the shape is closed.
        isClosed() -> bool
        --
        If the shape is a shell it returns True if it has no free boundaries (edges).
        If the shape is a wire it returns True if it has no free ends (vertices).
        (Internal and External sub-shepes are ignored in these checks)
        If the shape is an edge it returns True if its vertices are the same.
        """

    def isCoplanar(self, shape: Part.TopoShape, tol: float = None, /):
        """Checks if this shape is coplanar with the given shape.
        isCoplanar(shape,tol=None) -> bool
                """

    def isEqual(self, shape: Part.TopoShape, /):
        """Checks if both shapes are equal.
                This means geometry, placement and orientation are equal.
        isEqual(shape) -> bool
                """

    def isInfinite(self):
        """Checks if this shape has an infinite expansion.
        isInfinite() -> bool
                """

    def isInside(self, point: FreeCAD.Vector, tolerance: float, checkFace: bool, /):
        """Checks whether a point is inside or outside the shape.
        isInside(point, tolerance, checkFace) => Boolean
        --
        checkFace indicates if the point lying directly on a face is considered to be inside or not
                """

    def isNull(self):
        """Checks if the shape is null.
        isNull() -> bool"""

    def isPartner(self, shape: Part.TopoShape, /):
        """Checks if both shapes share the same geometry.
        Placement and orientation may differ.
        isPartner(shape) -> bool
                """

    def isSame(self, shape: Part.TopoShape, /):
        """Checks if both shapes share the same geometry
                and placement. Orientation may differ.
        isSame(shape) -> bool
                """

    def isValid(self):
        """Checks if the shape is valid, i.e. neither null, nor empty nor corrupted.
        isValid() -> bool
                """

    def limitTolerance(self, tmin: float, tmax: float = 0, ShapeType: type = None, /):
        """Limits tolerances in a shape
        limitTolerance(tmin, [tmax=0, ShapeType=Shape]) -> bool
        --
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
        Returns True if at least one tolerance of the sub-shape has been modified
                """

    @typing.overload
    def makeChamfer(self, radius: float, edgeList: object, /): ...

    @typing.overload
    def makeChamfer(self, radius1: float, radius2: float, edgeList: object, /):
        """Make chamfer.
        makeChamfer(radius,edgeList) -> Shape
        or
        makeChamfer(radius1,radius2,edgeList) -> Shape"""

    @typing.overload
    def makeFillet(self, radius: float, edgeList: object, /): ...

    @typing.overload
    def makeFillet(self, radius1: float, radius2: float, edgeList: object, /):
        """Make fillet.
        makeFillet(radius,edgeList) -> Shape
        or
        makeFillet(radius1,radius2,edgeList) -> Shape
                """

    def makeOffset2D(self, offset: float, join: int = None, fill: bool = None, openResult: bool = None, intersection: bool = None):
        """makes an offset shape (2d offsetting).
        makeOffset2D(offset, [join = 0, fill = False, openResult = false, intersection =
        false]) -> Shape
        --
        The function supports keyword
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
        structure follows that of source shape."""

    def makeOffsetShape(self, offset: float, tolerance: float, inter: bool = None, self_inter: bool = None, offsetMode: int = None, join: int = None, fill: bool = None):
        """makes an offset shape (3d offsetting).
        makeOffsetShape(offset, tolerance, [inter = False, self_inter = False,
        offsetMode = 0, join = 0, fill = False]) -> Shape
        --
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

        Returns: result of offsetting."""

    def makeParallelProjection(self, shape: Part.TopoShape, dir: FreeCAD.Vector, /):
        """Parallel projection of an edge or wire on this shape
        makeParallelProjection(shape, dir) -> Shape
                """

    def makePerspectiveProjection(self, shape: Part.TopoShape, pnt: FreeCAD.Vector, /):
        """Perspective projection of an edge or wire on this shape
        makePerspectiveProjection(shape, pnt) -> Shape
                """

    def makeShapeFromMesh(self, arg: tuple, tolerance: float, /):
        """Make a compound shape out of mesh data.
        makeShapeFromMesh((vertex,facets),tolerance) -> Shape
        --
        Note: This should be used for rather small meshes only."""

    def makeThickness(self, arg1: object, arg2: float, arg3: float, arg4: bool = None, arg5: bool = None, arg6: int = None, arg7: int = None, /):
        """Hollow a solid according to given thickness and faces.
        makeThickness(List of faces, Offset (Float), Tolerance (Float)) -> Shape
        --
        A hollowed solid is built from an initial solid and a set of faces on this solid,
        which are to be removed. The remaining faces of the solid become the walls of
        the hollowed solid, their thickness defined at the time of construction."""

    def makeWires(self, op: str, /):
        """make wire(s) using the edges of this shape
        makeWires([op=None])
        --
        The function will sort any edges inside the current shape, and connect them
        into wire. If more than one wire is found, then it will make a compound out of
        all found wires.

        This function is element mapping aware. If the input shape has non-zero Tag,
        it will map any edge and vertex element name inside the input shape into the
        itself.

        op: an optional string to be appended when auto generates element mapping.
                """

    def mirror(self, base: FreeCAD.Vector, norm: FreeCAD.Vector, /):
        """Mirror this shape on a given plane.
        mirror(base, norm) -> Shape
        --
        The plane is given with its base point and its normal direction."""

    def multiFuse(self, arg: object, tolerance: float = 0.0, /):
        """Union of this and a given list of topo shapes.
        multiFuse((tool1,tool2,...),[tolerance=0.0]) -> Shape
        --
        Supports (OCCT 6.9.0 and above):
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation
        - Parallelization of Boolean Operations algorithm

        Beginning from OCCT 6.8.1 a tolerance value can be specified.
        Deprecated: use fuse() instead."""

    def nullify(self):
        """Destroys the reference to the underlying shape stored in this shape.
        As a result, this shape becomes null.
        nullify()
                """

    def oldFuse(self, tool: Part.TopoShape, /):
        """Union of this and a given topo shape (old algorithm).
        oldFuse(tool) -> Shape
                """

    def optimalBoundingBox(self, useTriangulation: bool = True, useShapeTolerance: object = False, /):
        """Get the optimal bounding box
        optimalBoundingBox([useTriangulation = True, useShapeTolerance = False]) -> bound box
                """

    def overTolerance(self, value: float, ShapeType: type = None, /):
        """Determines which shapes have a tolerance over the given value
        overTolerance(value, [ShapeType=Shape]) -> ShapeList
        --
        ShapeType is interpreted as in the method getTolerance
                """

    def project(self, shapeList: object, /):
        """Project a list of shapes on this shape
        project(shapeList) -> Shape
                """

    def proximity(self, shape: Part.TopoShape, tolerance: float = None, /):
        """Returns two lists of Face indexes for the Faces involved in the intersection.
        proximity(shape,[tolerance]) -> (selfFaces, shapeFaces)
                """

    def read(self, filename: str, /):
        """Read in an IGES, STEP or BREP file.
        read(filename)
                """

    def reflectLines(self, ViewDir: FreeCAD.Vector, ViewPos: FreeCAD.Vector = None, UpDir: FreeCAD.Vector = None, EdgeType: str = None, Visible: bool = None, OnShape: bool = None):
        """Build projection or reflect lines of a shape according to a view direction.
        reflectLines(ViewDir, [ViewPos, UpDir, EdgeType, Visible, OnShape]) -> Shape (Compound of edges)
        --
        This algorithm computes the projection of the shape in the ViewDir direction.
        If OnShape is False(default), the returned edges are flat on the XY plane defined by
        ViewPos(origin) and UpDir(up direction).
        If OnShape is True, the returned edges are the corresponding 3D reflect lines located on the shape.
        EdgeType is a string defining the type of result edges :
        - IsoLine : isoparametric line
        - OutLine : outline (silhouette) edge
        - Rg1Line : smooth edge of G1-continuity between two surfaces
        - RgNLine : sewn edge of CN-continuity on one surface
        - Sharp : sharp edge (of C0-continuity)
        If Visible is True (default), only visible edges are returned.
        If Visible is False, only invisible edges are returned.
                """

    def removeInternalWires(self, minimalArea: float, /):
        """Removes internal wires (also holes) from the shape.
        removeInternalWires(minimalArea) -> bool
                """

    def removeShape(self, shapeList: object, /):
        """Remove a sub-shape and return a new shape.
        removeShape(shapeList) -> Shape
        --
        The parameter is a list of shapes."""

    def removeSplitter(self):
        """Removes redundant edges from the B-REP model
        removeSplitter() -> Shape
        """

    def replaceShape(self, tupleList: object, /):
        """Replace a sub-shape with a new shape and return a new shape.
        replaceShape(tupleList) -> Shape
        --
        The parameter is in the form list of tuples with the two shapes."""

    def reverse(self):
        """Reverses the orientation of this shape.
        reverse()
                """

    def reversed(self):
        """Reverses the orientation of a copy of this shape.
        reversed() -> Shape
                """

    @typing.overload
    def revolve(self, base: FreeCAD.Vector, direction: FreeCAD.Vector, angle: float = None, /): ...

    @typing.overload
    def revolve(self, Vector_0_0_0_: FreeCAD.Vector, Vector_0_0_1_: FreeCAD.Vector, arg: float = None, /): ...

    @typing.overload
    def revolve(self, V_0_0_0_: FreeCAD.Vector, V_0_1_0_: FreeCAD.Vector, arg: float = None, /):
        """Revolve the shape around an Axis to a given degree.
        revolve(base, direction, angle)
        --
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
                """

    @typing.overload
    def rotate(self, base: object, dir: object, degree: float, /): ...

    @typing.overload
    def rotate(self, Vector_0_0_0_: object, Vector_0_0_1_: object, arg: float, /):
        """Apply the rotation (base,dir,degree) to the current location of this shape
        rotate(base,dir,degree)
        --
        Shp.rotate(Vector(0,0,0),Vector(0,0,1),180) - rotate the shape around the Z Axis 180 degrees.
                """

    def rotated(self, base, dir, degree):
        """Create a new shape with rotation.
        rotated(base,dir,degree) -> shape
                """

    def scale(self, factor: float, base: FreeCAD.Vector = None, /):
        """Apply scaling with point and factor to this shape.
        scale(factor,[base=Vector(0,0,0)])
                """

    def scaled(self, factor, base):
        """Create a new shape with scale.
        scaled(factor,[base=Vector(0,0,0)]) -> shape
                  """

    @typing.overload
    def section(self, tool: Part.TopoShape, approximation: bool = False, /): ...

    @typing.overload
    def section(self, arg: Part.TopoShape, tolerance: float, approximation: bool = False, /): ...

    @typing.overload
    def section(self, arg: object, tolerance: float = 0.0, approximation: bool = False, /):
        """Section of this with a given (list of) topo shape.
        section(tool,[approximation=False]) -> Shape
          or
        section((tool1,tool2,...),[tolerance=0.0, approximation=False]) -> Shape
        --
        If approximation is True, section edges are approximated to a C1-continuous BSpline curve.

        Supports:
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation (s1 AND (s2 OR s3))
        - Parallelization of Boolean Operations algorithm

        OCC 6.9.0 or later is required."""

    def sewShape(self):
        """Sew the shape if there is a gap.
        sewShape()
                """

    def slice(self, direction: FreeCAD.Vector, distance: float, /):
        """Make single slice of this shape.
        slice(direction, distance) --> Wires"""

    def slices(self, direction: FreeCAD.Vector, distancesList: object, /):
        """Make slices of this shape.
        slices(direction, distancesList) --> Wires
                """

    def tessellate(self, arg1: float, arg2: bool = None, /):
        """Tessellate the shape and return a list of vertices and face indices
        tessellate() -> (vertex,facets)
                """

    def toNurbs(self):
        """Conversion of the complete geometry of a shape into NURBS geometry.
        toNurbs() -> Shape
        --
        For example, all curves supporting edges of the basis shape are converted
        into B-spline curves, and all surfaces supporting its faces are converted
        into B-spline surfaces."""

    def transformGeometry(self, matrix: FreeCAD.Matrix, /):
        """Apply geometric transformation on this or a copy the shape.
        transformGeometry(matrix) -> Shape
        --
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
        """

    def transformShape(self, Matrix: FreeCAD.Matrix, boolean_copy: bool = False, checkScale: object = False, /):
        """Apply transformation on a shape without changing the underlying geometry.
        transformShape(Matrix,[boolean copy=False, checkScale=False]) -> None
        --
        If checkScale is True, it will use transformGeometry if non-uniform
        scaling is detected."""

    def transformed(self, matrix: FreeCAD.Matrix, copy: object = False, checkScale: object = False, op: str = None):
        """Create a new transformed shape
        transformed(Matrix,copy=False,checkScale=False,op=None) -> shape
                """

    def translate(self, vector: object, /):
        """Apply the translation to the current location of this shape.
        translate(vector)
                """

    def translated(self, vector):
        """Create a new shape with translation
        translated(vector) -> shape
                 """

    def writeInventor(self, Mode: int = None, Deviation: float = None, Angle: float = None, FaceColors: object = None):
        """Write the mesh in OpenInventor format to a string.
        writeInventor() -> string
                """


# ArcOfHyperbolaPy.xml
class ArcOfHyperbola(Part.ArcOfConic):
    """Describes a portion of an hyperbola"""

    def __init__(self, arg1: Part.Hyperbola, arg2: float, arg3: float, arg4: bool = None, /):
        """Describes a portion of an hyperbola"""

    @property
    def Hyperbola(self) -> object:
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
class BSplineCurve(Part.BoundedCurve):
    """Describes a B-Spline curve in 3D space"""

    def __init__(self):
        """Describes a B-Spline curve in 3D space"""

    @property
    def Degree(self) -> int:
        """Returns the polynomial degree of this B-Spline curve."""

    @property
    def EndPoint(self) -> object:
        """Returns the end point of this B-Spline curve."""

    @property
    def FirstUKnotIndex(self) -> object:
        """Returns the index in the knot array of the knot
        corresponding to the first or last parameter
        of this B-Spline curve."""

    @property
    def KnotSequence(self) -> list:
        """Returns the knots sequence of this B-Spline curve."""

    @property
    def LastUKnotIndex(self) -> object:
        """Returns the index in the knot array of the knot
        corresponding to the first or last parameter
        of this B-Spline curve."""

    @property
    def MaxDegree(self) -> int:
        """Returns the value of the maximum polynomial degree of any
        B-Spline curve curve. This value is 25."""

    @property
    def NbKnots(self) -> int:
        """
        					Returns the number of knots of this B-Spline curve.
        				"""

    @property
    def NbPoles(self) -> int:
        """Returns the number of poles of this B-Spline curve.
        				"""

    @property
    def StartPoint(self) -> object:
        """Returns the start point of this B-Spline curve."""

    def __reduce__(self):
        """__reduce__()
        Serialization of Part.BSplineCurve objects
                        """

    @typing.overload
    def approximate(self, MaxDegree: int, MaxSegments: int = None, Continuity: str = None, Tolerance: float = None): ...

    @typing.overload
    def approximate(self, Points: object, DegMax: int = None, Continuity: str = None, Tolerance: float = None, DegMin: int = None, ParamType: str = None, Parameters: object = None, LengthWeight: float = None, CurvatureWeight: float = None, TorsionWeight: float = None):
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
        				"""

    def buildFromPoles(self, arg1: object, arg2: bool = None, arg3: int = None, arg4: bool = None, /):
        """
        					Builds a B-Spline by a list of poles.
        					arguments: poles (sequence of Base.Vector), [periodic (default is False), degree (default is 3), interpolate (default is False)]

        					Examples:
        					from FreeCAD import Base
        					import Part
        					V = Base.Vector
        					poles = [V(-2, 2, 0),V(0, 2, 1),V(2, 2, 0),V(2, -2, 0),V(0, -2, 1),V(-2, -2, 0)]

        					# non-periodic spline
        					n=Part.BSplineCurve()
        					n.buildFromPoles(poles)
        					Part.show(n.toShape())

        					# periodic spline
        					n=Part.BSplineCurve()
        					n.buildFromPoles(poles, True)
        					Part.show(n.toShape())
        				"""

    def buildFromPolesMultsKnots(self, poles: object, mults: object = None, knots: object = None, periodic: bool = None, degree: int = None, weights: object = None, CheckRational: bool = None):
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
        			"""

    @typing.overload
    def getCardinalSplineTangents(self, Points: object, Parameter: float): ...

    @typing.overload
    def getCardinalSplineTangents(self, Points: object, Parameters: object):
        """Compute the tangents for a Cardinal spline"""

    def getKnot(self, arg1: int, /):
        """Get a knot of the B-Spline curve."""

    def getKnots(self):
        """Get all knots of the B-Spline curve."""

    def getMultiplicities(self):
        """
        					Returns the multiplicities table M of the knots of this B-Spline curve.
        				"""

    def getMultiplicity(self, arg1: int, /):
        """Returns the multiplicity of the knot of index
        from the knots table of this B-Spline curve."""

    def getPole(self, arg1: int, /):
        """Get a pole of the B-Spline curve."""

    def getPoles(self):
        """Get all poles of the B-Spline curve."""

    def getPolesAndWeights(self):
        """Returns the table of poles and weights in homogeneous coordinates."""

    def getResolution(self, arg1: float, /):
        """Computes for this B-Spline curve the parametric tolerance (UTolerance)
        for a given 3D tolerance (Tolerance3D).
        If f(t) is the equation of this B-Spline curve, the parametric tolerance
        ensures that:
        |t1-t0| < UTolerance =""==> |f(t1)-f(t0)| < Tolerance3D"""

    def getWeight(self, arg1: int, /):
        """Get a weight of the B-Spline curve."""

    def getWeights(self):
        """Get all weights of the B-Spline curve."""

    def increaseDegree(self, arg1: int, /):
        """increase(Int=Degree)
        Increases the degree of this B-Spline curve to Degree.
        As a result, the poles, weights and multiplicities tables
        are modified; the knots table is not changed. Nothing is
        done if Degree is less than or equal to the current degree."""

    def increaseMultiplicity(self, int_start: int, int_end: int, int_mult: int = None, /):
        """
        				increaseMultiplicity(int index, int mult)
        				increaseMultiplicity(int start, int end, int mult)
        				Increases multiplicity of knots up to mult.

        				index: the index of a knot to modify (1-based)
        				start, end: index range of knots to modify.
        				If mult is lower or equal to the current multiplicity nothing is done. If mult is higher than the degree the degree is used.
        				"""

    def incrementMultiplicity(self, int_start: int, int_end: int, int_mult: int, /):
        """
        				incrementMultiplicity(int start, int end, int mult)
        				Raises multiplicity of knots by mult.

        				start, end: index range of knots to modify.
        				"""

    def insertKnot(self, arg1: float, arg2: int = None, arg3: float = None, arg4: bool = None, /):
        """
        				insertKnot(u, mult = 1, tol = 0.0)
        				Inserts a knot value in the sequence of knots. If u is an existing knot the
        				multiplicity is increased by mult. """

    def insertKnots(self, list_of_floats: object, list_of_ints: object, tol: float = 0.0, bool_add: bool = True, /):
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
        				"""

    def interpolate(self, Points: object, PeriodicFlag: bool = None, Tolerance: float = None, InitialTangent: FreeCAD.Vector = None, FinalTangent: FreeCAD.Vector = None, Tangents: object = None, TangentFlags: object = None, Parameters: object = None, Scale: bool = None):
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
        				"""

    def isClosed(self):
        """
        					Returns true if the distance between the start point and end point of
        					this B-Spline curve is less than or equal to gp::Resolution().
        				"""

    def isPeriodic(self):
        """Returns true if this BSpline curve is periodic."""

    def isRational(self):
        """
        					Returns true if this B-Spline curve is rational.
        					A B-Spline curve is rational if, at the time of construction,
        					the weight table has been initialized.
        				"""

    def join(self, arg1: Part.BSplineCurve, /):
        """
        					Build a new spline by joining this and a second spline.
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
        				"""

    def movePoint(self, U: float, P: FreeCAD.Vector, Index1: int, Index2: int, /):
        """
        				movePoint(U, P, Index1, Index2)
        				Moves the point of parameter U of this B-Spline curve to P.
        Index1 and Index2 are the indexes in the table of poles of this B-Spline curve
        of the first and last poles designated to be moved.

        Returns: (FirstModifiedPole, LastModifiedPole). They are the indexes of the
        first and last poles which are effectively modified."""

    def removeKnot(self, Index: int, M: int, tol: float, /):
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
        				"""

    def segment(self, u1: float, u2: float, /):
        """
        					segment(u1,u2)
        					Modifies this B-Spline curve by segmenting it."""

    def setKnot(self, arg1: int, arg2: float, arg3: int = None, /):
        """Set a knot of the B-Spline curve."""

    def setKnots(self, arg1: object, /):
        """Set knots of the B-Spline curve."""

    def setNotPeriodic(self):
        """Changes this B-Spline curve into a non-periodic curve.
        If this curve is already non-periodic, it is not modified."""

    def setOrigin(self, arg1: int, /):
        """Assigns the knot of index Index in the knots table
        as the origin of this periodic B-Spline curve. As a consequence,
        the knots and poles tables are modified."""

    def setPeriodic(self):
        """Changes this B-Spline curve into a periodic curve."""

    def setPole(self, arg1: int, arg2: FreeCAD.Vector, arg3: float = None, /):
        """Modifies this B-Spline curve by assigning P
        to the pole of index Index in the poles table."""

    def setWeight(self, arg1: int, arg2: float, /):
        """Set a weight of the B-Spline curve."""

    def toBezier(self):
        """
        					Build a list of Bezier splines.
        				"""

    def toBiArcs(self, tolerance: float, /):
        """
        					Build a list of arcs and lines to approximate the B-spline.
        					toBiArcs(tolerance) -> list.
        				"""


# ArcOfParabolaPy.xml
class ArcOfParabola(Part.ArcOfConic):
    """Describes a portion of an parabola"""

    def __init__(self, arg1: Part.Parabola, arg2: float, arg3: float, arg4: bool = None, /):
        """Describes a portion of an parabola"""

    @property
    def Focal(self) -> float:
        """The focal length of the parabola."""

    @Focal.setter
    def Focal(self, value: float): ...

    @property
    def Parabola(self) -> object:
        """The internal parabola representation"""


# PartFeaturePy.xml
class Feature(FreeCAD.GeoFeature):
    """This is the father of all shape object classes"""


# TrimmedCurvePy.xml
class TrimmedCurve(Part.BoundedCurve):
    """
                    The abstract class TrimmedCurve is the root class of all trimmed curve objects.
                """

    def setParameterRange(self, arg1: float = None, arg2: float = None, /):
        """
                            Re-trims this curve to the provided parameter range ([Float=First, Float=Last])
                        """


# ArcOfCirclePy.xml
class ArcOfCircle(Part.ArcOfConic):
    """Describes a portion of a circle"""

    @typing.overload
    def __init__(self, arg1: Part.Circle, arg2: float, arg3: float, arg4: bool = None, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, arg3: FreeCAD.Vector, /):
        """Describes a portion of a circle"""

    @property
    def Circle(self) -> object:
        """The internal circle representation"""

    @property
    def Radius(self) -> float:
        """The radius of the circle."""

    @Radius.setter
    def Radius(self, value: float): ...


# SpherePy.xml
class Sphere(Part.GeometrySurface):
    """Describes a sphere in 3D space"""

    def __init__(self):
        """Describes a sphere in 3D space"""

    @property
    def Area(self) -> float:
        """Compute the area of the sphere."""

    @property
    def Axis(self) -> object:
        """The axis direction of the circle"""

    @Axis.setter
    def Axis(self, value: object): ...

    @property
    def Center(self) -> object:
        """Center of the sphere."""

    @Center.setter
    def Center(self, value: object): ...

    @property
    def Radius(self) -> float:
        """The radius of the sphere."""

    @Radius.setter
    def Radius(self, value: float): ...

    @property
    def Volume(self) -> float:
        """Compute the volume of the sphere."""


# TopoShapeCompoundPy.xml
class TopoShape(Part.TopoShape):
    """Create a compound out of a list of shapes"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: object, /):
        """Create a compound out of a list of shapes"""

    def add(self, shape: Part.TopoShape, /):
        """Add a shape to the compound.
        add(shape)
                """

    def connectEdgesToWires(self, Shared: bool = True, Tolerance: float = 1e-7, /):
        """Build a compound of wires out of the edges of this compound.
        connectEdgesToWires([Shared = True, Tolerance = 1e-7]) -> Compound
        --
        If Shared is True  connection is performed only when adjacent edges share the same vertex.
        If Shared is False connection is performed only when ends of adjacent edges are at distance less than Tolerance."""


# TopoShapeWirePy.xml
class TopoShape(Part.TopoShape):
    """TopoShapeWire is the OpenCasCade topological wire wrapper"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: Part.TopoShape, /): ...

    @typing.overload
    def __init__(self, arg1: object, /):
        """TopoShapeWire is the OpenCasCade topological wire wrapper"""

    @property
    def CenterOfMass(self) -> object:
        """Returns the center of mass of the current system.
        If the gravitational field is uniform, it is the center of gravity.
        The coordinates returned for the center of mass are expressed in the
        absolute Cartesian coordinate system."""

    @property
    def Continuity(self) -> str:
        """Returns the continuity"""

    @property
    def Mass(self) -> object:
        """Returns the mass of the current system."""

    @property
    def MatrixOfInertia(self) -> object:
        """Returns the matrix of inertia. It is a symmetrical matrix.
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
        coordinate system."""

    @property
    def OrderedEdges(self) -> list:
        """List of ordered edges in this shape."""

    @property
    def OrderedVertexes(self) -> list:
        """List of ordered vertexes in this shape."""

    @property
    def PrincipalProperties(self) -> dict:
        """Computes the principal properties of inertia of the current system.
         There is always a set of axes for which the products
         of inertia of a geometric system are equal to 0; i.e. the
         matrix of inertia of the system is diagonal. These axes
         are the principal axes of inertia. Their origin is
         coincident with the center of mass of the system. The
         associated moments are called the principal moments of inertia.
         This function computes the eigen values and the
         eigen vectors of the matrix of inertia of the system."""

    @property
    def StaticMoments(self) -> object:
        """Returns Ix, Iy, Iz, the static moments of inertia of the
         current system; i.e. the moments of inertia about the
         three axes of the Cartesian coordinate system."""

    def add(self, edge: Part.TopoShape, /):
        """Add an edge to the wire
        add(edge)
                        """

    def approximate(self, Tol2d: float = None, Tol3d: float = 1e-4, MaxSegments: int = 10, MaxDegree: int = 3):
        """Approximate B-Spline-curve from this wire
        approximate([Tol2d,Tol3d=1e-4,MaxSegments=10,MaxDegree=3]) -> BSpline
                """

    @typing.overload
    def discretize(self, kwargs: object, /): ...

    @typing.overload
    def discretize(self, Number: object, /): ...

    @typing.overload
    def discretize(self, QuasiNumber: object, /): ...

    @typing.overload
    def discretize(self, Distance: object, /): ...

    @typing.overload
    def discretize(self, Deflection: object, /): ...

    @typing.overload
    def discretize(self, QuasiDeflection: object, /): ...

    @typing.overload
    def discretize(self, Number: int, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, Distance: float, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, Deflection: float, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, QuasiNumber: int, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, QuasiDeflection: float, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, Number: int, First: float = 0.01, Last: float = 100): ...

    @typing.overload
    def discretize(self, Distance: float, First: float = 0.01, Last: float = 100): ...

    @typing.overload
    def discretize(self, Deflection: float, First: float = 0.01, Last: float = 100): ...

    @typing.overload
    def discretize(self, QuasiNumber: int, First: float = 0.01, Last: float = 100): ...

    @typing.overload
    def discretize(self, QuasiDeflection: float, First: float = 0.01, Last: float = 100):
        """Discretizes the wire and returns a list of points.
        discretize(kwargs) -> list
        --
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
                """

    def fixWire(self, face: Part.TopoShape = None, tolerance: float = None, /):
        """Fix wire
        fixWire([face, tolerance])
        --
        A face and a tolerance can optionally be supplied to the algorithm:
                        """

    def makeHomogenousWires(self, wire: Part.TopoShape, /):
        """Make this and the given wire homogeneous to have the same number of edges
        makeHomogenousWires(wire) -> Wire
                    """

    def makeOffset(self, arg1: float, /):
        """Offset the shape by a given amount. DEPRECATED - use makeOffset2D instead."""

    def makePipe(self, profile: Part.TopoShape, /):
        """Make a pipe by sweeping along a wire.
        makePipe(profile) -> Shape
                """

    def makePipeShell(self, shapeList: object, isSolid: bool = False, isFrenet: bool = False, transition: int = 0, /):
        """Make a loft defined by a list of profiles along a wire.
        makePipeShell(shapeList,[isSolid=False,isFrenet=False,transition=0]) -> Shape
        --
        Transition can be 0 (default), 1 (right corners) or 2 (rounded corners).
                """


# SurfaceOfExtrusionPy.xml
class SurfaceOfExtrusion(Part.GeometrySurface):
    """Describes a surface of linear extrusion"""

    def __init__(self, arg1: Part.Geometry, arg2: FreeCAD.Vector, /):
        """Describes a surface of linear extrusion"""

    @property
    def BasisCurve(self) -> object:
        """
        					Sets or gets the basic curve.
        				"""

    @property
    def Direction(self) -> object:
        """
        					Sets or gets the direction of revolution.
        				"""


# PointPy.xml
class Point(Part.Geometry):
    """Describes a point
    To create a point there are several ways:
    Part.Point()
        Creates a default point

    Part.Point(Point)
        Creates a copy of the given point

    Part.Point(Vector)
        Creates a line for the given coordinates"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Point: Part.Point, /): ...

    @typing.overload
    def __init__(self, Point: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, Vector: Part.Point, /): ...

    @typing.overload
    def __init__(self, Vector: FreeCAD.Vector, /):
        """Describes a point
        To create a point there are several ways:
        Part.Point()
            Creates a default point

        Part.Point(Point)
            Creates a copy of the given point

        Part.Point(Vector)
            Creates a line for the given coordinates"""

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

    def toShape(self):
        """Create a vertex from this point."""


# TopoShapeShellPy.xml
class TopoShape(Part.TopoShape):
    """Create a shell out of a list of faces"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: object, /):
        """Create a shell out of a list of faces"""

    @property
    def CenterOfMass(self) -> object:
        """Returns the center of mass of the current system.
        If the gravitational field is uniform, it is the center of gravity.
        The coordinates returned for the center of mass are expressed in the
        absolute Cartesian coordinate system."""

    @property
    def Mass(self) -> object:
        """Returns the mass of the current system."""

    @property
    def MatrixOfInertia(self) -> object:
        """Returns the matrix of inertia. It is a symmetrical matrix.
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
        coordinate system."""

    @property
    def PrincipalProperties(self) -> dict:
        """Computes the principal properties of inertia of the current system.
         There is always a set of axes for which the products
         of inertia of a geometric system are equal to 0; i.e. the
         matrix of inertia of the system is diagonal. These axes
         are the principal axes of inertia. Their origin is
         coincident with the center of mass of the system. The
         associated moments are called the principal moments of inertia.
         This function computes the eigen values and the
         eigen vectors of the matrix of inertia of the system."""

    @property
    def StaticMoments(self) -> object:
        """Returns Ix, Iy, Iz, the static moments of inertia of the
         current system; i.e. the moments of inertia about the
         three axes of the Cartesian coordinate system."""

    def add(self, face: Part.TopoShape, /):
        """Add a face to the shell.
        add(face)
                """

    def getBadEdges(self):
        """Get bad edges as compound.
        getBadEdges() -> compound
                """

    def getFreeEdges(self):
        """Get free edges as compound.
        getFreeEdges() -> compound
                """

    def makeHalfSpace(self, point: FreeCAD.Vector, /):
        """Make a half-space solid by this shell and a reference point.
        makeHalfSpace(point) -> Solid
                """


# ConicPy.xml
class Conic(Part.Curve):
    """Describes an abstract conic in 3d space"""

    @property
    def AngleXU(self) -> float:
        """The angle between the X axis and the major axis of the conic."""

    @AngleXU.setter
    def AngleXU(self, value: float): ...

    @property
    def Axis(self) -> object:
        """The axis direction of the circle"""

    @Axis.setter
    def Axis(self, value: object): ...

    @property
    def Center(self) -> object:
        """Deprecated -- use Location."""

    @Center.setter
    def Center(self, value: object): ...

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
    def Location(self) -> object:
        """Location of the conic."""

    @Location.setter
    def Location(self, value: object): ...

    @property
    def XAxis(self) -> object:
        """The X axis direction of the circle"""

    @XAxis.setter
    def XAxis(self, value: object): ...

    @property
    def YAxis(self) -> object:
        """The Y axis direction of the circle"""

    @YAxis.setter
    def YAxis(self, value: object): ...


# GeometryIntExtensionPy.xml
class GeometryIntExtension(Part.GeometryExtension):
    """A GeometryExtension extending geometry objects with an int."""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: int, /): ...

    @typing.overload
    def __init__(self, arg1: int, arg2: str, /):
        """A GeometryExtension extending geometry objects with an int."""

    @property
    def Value(self) -> int:
        """
                        returns the value of the GeometryIntExtension.
                    """

    @Value.setter
    def Value(self, value: int): ...


# BSplineSurfacePy.xml
class BSplineSurface(Part.GeometrySurface):
    """Describes a B-Spline surface in 3D space"""

    @property
    def FirstUKnotIndex(self) -> object:
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
    def FirstVKnotIndex(self) -> object:
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
    def LastUKnotIndex(self) -> object:
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
    def LastVKnotIndex(self) -> object:
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
        """
        					Returns the number of knots of this B-Spline surface in the u parametric direction.
        				"""

    @property
    def NbUPoles(self) -> int:
        """
        					Returns the number of poles of this B-Spline surface in the u parametric direction.
        				"""

    @property
    def NbVKnots(self) -> int:
        """
        					Returns the number of knots of this B-Spline surface in the v parametric direction.
        				"""

    @property
    def NbVPoles(self) -> int:
        """
        					Returns the number of poles of this B-Spline surface in the v parametric direction.
        				"""

    @property
    def UDegree(self) -> int:
        """
        					Returns the degree of this B-Spline surface in the u parametric direction.
        				"""

    @property
    def UKnotSequence(self) -> list:
        """
        						Returns the knots sequence of this B-Spline surface in
        						the u direction.
        				"""

    @property
    def VDegree(self) -> int:
        """
        					Returns the degree of this B-Spline surface in the v parametric direction.
        				"""

    @property
    def VKnotSequence(self) -> list:
        """
        					Returns the knots sequence of this B-Spline surface in
        					the v direction.
        				"""

    def approximate(self, Points: object, DegMin: int = None, DegMax: int = None, Continuity: int = None, Tolerance: float = None, X0: float = None, dX: float = None, Y0: float = None, dY: float = None, ParamType: str = None, LengthWeight: float = None, CurvatureWeight: float = None, TorsionWeight: float = None):
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
        				"""

    def bounds(self):
        """
        					Returns the parametric bounds (U1, U2, V1, V2) of this B-Spline surface.
        				"""

    def buildFromNSections(self, arg1: object, arg2: bool = None, /):
        """
        					Builds a B-Spline from a list of control curves
        				"""

    def buildFromPolesMultsKnots(self, poles: object, umults: object, vmults: object, uknots: object = None, vknots: object = None, uperiodic: bool = None, vperiodic: bool = None, udegree: int = None, vdegree: int = None, weights: object = None):
        """
        					Builds a B-Spline by a lists of Poles, Mults and Knots
        					arguments: poles (sequence of sequence of Base.Vector), umults, vmults, [uknots, vknots, uperiodic, vperiodic, udegree, vdegree, weights (sequence of sequence of float)]
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

    def getPole(self, arg1: int, arg2: int, /):
        """
        					Returns the pole of index (UIndex,VIndex) of this B-Spline surface.
        				"""

    def getPoles(self):
        """Returns the table of poles of this B-Spline surface."""

    def getPolesAndWeights(self):
        """Returns the table of poles and weights in homogeneous coordinates."""

    def getResolution(self, arg1: float, /):
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
        				"""

    def getUKnot(self, arg1: int, /):
        """
        					Returns, for this B-Spline surface, in the u parametric direction
        					the knot of index UIndex of the knots table.
        				"""

    def getUKnots(self):
        """
        					Returns, for this B-Spline surface, the knots table
        					in the u parametric direction
        				"""

    def getUMultiplicities(self):
        """
        					Returns, for this B-Spline surface, the table of
        					multiplicities in the u parametric direction
        				"""

    def getUMultiplicity(self, arg1: int, /):
        """
        					Returns, for this B-Spline surface, the multiplicity of
        					the knot of index UIndex in the u parametric direction.
        				"""

    def getVKnot(self, arg1: int, /):
        """
        					Returns, for this B-Spline surface, in the v parametric direction
        					the knot of index VIndex of the knots table.
        				"""

    def getVKnots(self):
        """
        					Returns, for this B-Spline surface, the knots table
        					in the v parametric direction
        				"""

    def getVMultiplicities(self):
        """
        					Returns, for this B-Spline surface, the table of
        					multiplicities in the v parametric direction
        				"""

    def getVMultiplicity(self, arg1: int, /):
        """
        					Returns, for this B-Spline surface, the multiplicity of
        					the knot of index VIndex in the v parametric direction.
        				"""

    def getWeight(self, arg1: int, arg2: int, /):
        """
        					Return the weight of the pole of index (UIndex,VIndex)
        					in the poles table for this B-Spline surface.
        				"""

    def getWeights(self):
        """Returns the table of weights of the poles for this B-Spline surface."""

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
        """Increment the multiplicity in the u direction"""

    def incrementVMultiplicity(self, arg1: int, arg2: int, arg3: int, /):
        """Increment the multiplicity in the v direction"""

    def insertUKnot(self, arg1: float, arg2: int, arg3: float, arg4: bool = None, /):
        """insertUKnote(float U, int Index, float Tolerance) - Insert or override a knot"""

    def insertUKnots(self, arg1: object, arg2: object, arg3: float = None, arg4: bool = None, /):
        """insertUKnote(List of float U, List of float Mult, float Tolerance) - Inserts knots."""

    def insertVKnot(self, arg1: float, arg2: int, arg3: float, arg4: bool = None, /):
        """insertUKnote(float V, int Index, float Tolerance) - Insert or override a knot."""

    def insertVKnots(self, arg1: object, arg2: object, arg3: float = None, arg4: bool = None, /):
        """insertUKnote(List of float V, List of float Mult, float Tolerance) - Inserts knots."""

    def interpolate(self, zpoints: object, X0: float = None, dX: float = None, Y0: float = None, dY: float = None, /):
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
        				"""

    def isUClosed(self):
        """
        					Checks if this surface is closed in the u parametric direction.
        					Returns true if, in the table of poles the first row and the last
        					row are identical.
        				"""

    def isUPeriodic(self):
        """Returns true if this surface is periodic in the u parametric direction."""

    def isURational(self):
        """
        					Returns false if the equation of this B-Spline surface is polynomial
        					(e.g. non-rational) in the u or v parametric direction.
        					In other words, returns false if for each row of poles, the associated
        					weights are identical
        				"""

    def isVClosed(self):
        """
        					Checks if this surface is closed in the v parametric direction.
        					Returns true if, in the table of poles the first column and the
        					last column are identical.
        				"""

    def isVPeriodic(self):
        """Returns true if this surface is periodic in the v parametric direction."""

    def isVRational(self):
        """
        					Returns false if the equation of this B-Spline surface is polynomial
        					(e.g. non-rational) in the u or v parametric direction.
        					In other words, returns false if for each column of poles, the associated
        					weights are identical
        				"""

    def movePoint(self, arg1: float, arg2: float, arg3: FreeCAD.Vector, arg4: int, arg5: int, arg6: int, arg7: int, /):
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
        				"""

    def removeUKnot(self, arg1: int, arg2: int, arg3: float, /):
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
        				"""

    def removeVKnot(self, arg1: int, arg2: int, arg3: float, /):
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
        				"""

    def reparametrize(self, arg1: int, arg2: int, arg3: float = None, /):
        """Returns a reparametrized copy of this surface"""

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
        				"""

    def setPoleCol(self, arg1: int, arg2: object, arg3: object = None, /):
        """
        					Modifies this B-Spline surface by assigning values to all or part
        					of the column of poles of index VIndex, of this B-Spline surface.
        					You can also change the weights of the modified poles. The weights
        					are set to the corresponding values of CPoleWeights.
        					These syntaxes must only be used for rational surfaces.
        				"""

    def setPoleRow(self, arg1: int, arg2: object, arg3: object = None, /):
        """
        					Modifies this B-Spline surface by assigning values to all or part
        					of the row of poles of index VIndex, of this B-Spline surface.
        					You can also change the weights of the modified poles. The weights
        					are set to the corresponding values of CPoleWeights.
        					These syntaxes must only be used for rational surfaces.
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

    def setUKnots(self, arg1: object, /):
        """
        					Changes all knots of this B-Spline surface in the u parametric
        					direction. The multiplicity of the knots is not modified.
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
        				"""

    def setUOrigin(self, arg1: int, /):
        """
        					Assigns the knot of index Index in the knots table
        					in the u parametric direction to be the origin of
        					this periodic B-Spline surface. As a consequence,
        					the knots and poles tables are modified.
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

    def setVKnots(self, arg1: object, /):
        """
        					Changes all knots of this B-Spline surface in the v parametric
        					direction. The multiplicity of the knots is not modified.
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
        				"""

    def setVOrigin(self, arg1: int, /):
        """
        					Assigns the knot of index Index in the knots table
        					in the v parametric direction to be the origin of
        					this periodic B-Spline surface. As a consequence,
        					the knots and poles tables are modified.
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
        				"""

    def setWeight(self, arg1: int, arg2: int, arg3: float, /):
        """
        					Modifies this B-Spline surface by assigning the value Weight to the weight
        					of the pole of index (UIndex, VIndex) in the poles tables of this B-Spline
        					surface.

        					This function must only be used for rational surfaces.
        				"""

    def setWeightCol(self, arg1: int, arg2: object, /):
        """
        					Modifies this B-Spline surface by assigning values to all or part of the
        					weights of the column of poles of index VIndex of this B-Spline surface.

        					The modified part of the column of weights is defined by the bounds
        					of the array CPoleWeights.

        					This function must only be used for rational surfaces.
        				"""

    def setWeightRow(self, arg1: int, arg2: object, /):
        """
        					Modifies this B-Spline surface by assigning values to all or part of the
        					weights of the row of poles of index UIndex of this B-Spline surface.

        					The modified part of the row of weights is defined by the bounds of the
        					array CPoleWeights.

        					This function must only be used for rational surfaces.
        				"""


# RectangularTrimmedSurfacePy.xml
class RectangularTrimmedSurface(Part.GeometrySurface):
    """Describes a portion of a surface (a patch) limited by two values of the
    u parameter in the u parametric direction, and two values of the v parameter in the v parametric
    direction. The domain of the trimmed surface must be within the domain of the surface being trimmed.

    The trimmed surface is defined by:
    - the basis surface, and
    - the values (umin, umax) and (vmin, vmax) which limit it in the u and v parametric directions.

    The trimmed surface is built from a copy of the basis surface. Therefore, when the basis surface
    is modified the trimmed surface is not changed. Consequently, the trimmed surface does not
    necessarily have the same orientation as the basis surface."""

    @typing.overload
    def __init__(self, arg1: Part.GeometrySurface, arg2: float, arg3: float, arg4: float, arg5: float, arg6: bool = None, arg7: bool = None, /): ...

    @typing.overload
    def __init__(self, arg1: Part.GeometrySurface, arg2: float, arg3: float, arg4: bool, arg5: bool = None, /):
        """Describes a portion of a surface (a patch) limited by two values of the
        u parameter in the u parametric direction, and two values of the v parameter in the v parametric
        direction. The domain of the trimmed surface must be within the domain of the surface being trimmed.

        The trimmed surface is defined by:
        - the basis surface, and
        - the values (umin, umax) and (vmin, vmax) which limit it in the u and v parametric directions.

        The trimmed surface is built from a copy of the basis surface. Therefore, when the basis surface
        is modified the trimmed surface is not changed. Consequently, the trimmed surface does not
        necessarily have the same orientation as the basis surface."""

    @property
    def BasisSurface(self) -> object: ...

    def setTrim(self, arg1: float, arg2: float, arg3: float, arg4: float, /):
        """Modifies this patch by changing the trim values applied to the original surface"""


# LinePy.xml
class Line(Part.Curve):
    """Describes an infinite line
    To create a line there are several ways:
    Part.Line()
        Creates a default line

    Part.Line(Line)
        Creates a copy of the given line

    Part.Line(Point1,Point2)
        Creates a line that goes through two given points"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Line: Part.Line, /): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, /):
        """Describes an infinite line
        To create a line there are several ways:
        Part.Line()
            Creates a default line

        Part.Line(Line)
            Creates a copy of the given line

        Part.Line(Point1,Point2)
            Creates a line that goes through two given points"""

    @property
    def Direction(self) -> object:
        """Returns the direction of this line."""

    @Direction.setter
    def Direction(self, value: object): ...

    @property
    def Location(self) -> object:
        """Returns the location of this line."""

    @Location.setter
    def Location(self, value: object): ...


# GeometrySurfacePy.xml
class GeometrySurface(Part.Geometry):
    """
    				The abstract class GeometrySurface is the root class of all surface objects.
    			"""

    @property
    def Continuity(self) -> str:
        """
        					Returns the global continuity of the surface.
        				"""

    @property
    def Rotation(self) -> object:
        """Returns a rotation object to describe the orientation for surface that supports it"""

    def UPeriod(self):
        """
        					Returns the period of this patch in the u parametric direction.
        				"""

    def VPeriod(self):
        """
        					Returns the period of this patch in the v parametric direction.
        				"""

    def bounds(self):
        """
        					Returns the parametric bounds (U1, U2, V1, V2) of this trimmed surface.
        				"""

    def curvature(self, u: float, v: float, type: str, /):
        """curvature(u,v,type) -> float
        The value of type must be one of this: Max, Min, Mean or Gauss
        Computes the curvature of parameter (u,v) on this geometry"""

    def curvatureDirections(self, u: float, v: float, /):
        """curvatureDirections(u,v) -> (Vector,Vector)
        Computes the directions of maximum and minimum curvature
        of parameter (u,v) on this geometry.
        The first vector corresponds to the maximum curvature,
        the second vector corresponds to the minimum curvature.
        """

    def getD0(self, arg1: float, arg2: float, /):
        """Returns the point of given parameter"""

    def getDN(self, arg1: float, arg2: float, arg3: int, arg4: int, /):
        """Returns the n-th derivative"""

    @typing.overload
    def intersect(self, arg1: Part.GeometrySurface, arg2: float = None, /): ...

    @typing.overload
    def intersect(self, arg1: Part.Curve, arg2: float = None, /):
        """
                            Returns all intersection points/curves between the surface and the curve/surface.
                        """

    def intersectSS(self, arg1: Part.GeometrySurface, arg2: float = None, /):
        """
        Returns all intersection curves of this surface and the given surface.
        The required arguments are:
        * Second surface
        * precision code (optional, default=0)
                        """

    def isPlanar(self, float: float = None, /):
        """
        isPlanar([float]) -> Bool
        Checks if the surface is planar within a certain tolerance.
                        """

    def isUClosed(self):
        """
        					Checks if this surface is closed in the u parametric direction.
        				"""

    def isUPeriodic(self):
        """Returns true if this patch is periodic in the given parametric direction."""

    def isUmbillic(self, u: float, v: float, /):
        """isUmbillic(u,v) -> bool
        Check if the geometry on parameter is an umbillic point,
        i.e. maximum and minimum curvature are equal."""

    def isVClosed(self):
        """
        					Checks if this surface is closed in the v parametric direction.
        				"""

    def isVPeriodic(self):
        """Returns true if this patch is periodic in the given parametric direction."""

    def normal(self, u: float, v: float, /):
        """normal(u,v) -> Vector
        Computes the normal of parameter (u,v) on this geometry"""

    def parameter(self, arg1: FreeCAD.Vector, arg2: float = None, /):
        """Returns the parameter on the curve
        of the nearest orthogonal projection of the point."""

    def projectPoint(self, Point: FreeCAD.Vector, Method: str = None):
        """
        Computes the projection of a point on the surface

        projectPoint(Point=Vector,[Method=\"NearestPoint\"])
        projectPoint(Vector,\"NearestPoint\") -> Vector
        projectPoint(Vector,\"LowerDistance\") -> float
        projectPoint(Vector,\"LowerDistanceParameters\") -> tuple of floats (u,v)
        projectPoint(Vector,\"Distance\") -> list of floats
        projectPoint(Vector,\"Parameters\") -> list of tuples of floats
        projectPoint(Vector,\"Point\") -> list of points
        """

    def tangent(self, u: float, v: float, /):
        """tangent(u,v) -> (Vector,Vector)
        Computes the tangent of parameter (u,v) on this geometry"""

    def toBSpline(self, Tol3d: float = None, UContinuity: str = None, VContinuity: str = None, MaxDegreeU: int = None, MaxDegreeV: int = None, MaxSegments: int = None, PrecisCode: int = None):
        """
        					Returns a B-Spline representation of this surface. 
        					The optional arguments are:
        					* tolerance (default=1e-7)
        					* continuity in u (as string e.g. C0, G0, G1, C1, G2, C3, CN) (default='C1')
        					* continuity in v (as string e.g. C0, G0, G1, C1, G2, C3, CN) (default='C1')
        					* maximum degree in u (default=25)
        					* maximum degree in v (default=25)
        					* maximum number of segments (default=1000)
        					* precision code (default=0)
        					Will raise an exception if surface is infinite in U or V (like planes, cones or cylinders)
        				"""

    def toShape(self, arg1: float = None, arg2: float = None, arg3: float = None, arg4: float = None, /):
        """Return the shape for the geometry."""

    def uIso(self, arg1: float, /):
        """Builds the U isoparametric curve"""

    def vIso(self, arg1: float, /):
        """Builds the V isoparametric curve"""

    def value(self, u: float, v: float, /):
        """value(u,v) -> Point
        Computes the point of parameter (u,v) on this surface"""


# TopoShapeEdgePy.xml
class TopoShape(Part.TopoShape):
    """TopoShapeEdge is the OpenCasCade topological edge wrapper"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: Part.Geometry, arg2: float = None, arg3: float = None, /): ...

    @typing.overload
    def __init__(self, arg1: Part.TopoShape, /): ...

    @typing.overload
    def __init__(self, arg1: Part.TopoShape, arg2: Part.TopoShape, /):
        """TopoShapeEdge is the OpenCasCade topological edge wrapper"""

    @property
    def CenterOfMass(self) -> object:
        """Returns the center of mass of the current system.
        If the gravitational field is uniform, it is the center of gravity.
        The coordinates returned for the center of mass are expressed in the
        absolute Cartesian coordinate system."""

    @property
    def Closed(self) -> bool:
        """Returns true if the edge is closed"""

    @property
    def Continuity(self) -> str:
        """Returns the continuity"""

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
    def Mass(self) -> object:
        """Returns the mass of the current system."""

    @property
    def MatrixOfInertia(self) -> object:
        """Returns the matrix of inertia. It is a symmetrical matrix.
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
        coordinate system."""

    @property
    def ParameterRange(self) -> tuple:
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
    def PrincipalProperties(self) -> dict:
        """Computes the principal properties of inertia of the current system.
         There is always a set of axes for which the products
         of inertia of a geometric system are equal to 0; i.e. the
         matrix of inertia of the system is diagonal. These axes
         are the principal axes of inertia. Their origin is
         coincident with the center of mass of the system. The
         associated moments are called the principal moments of inertia.
         This function computes the eigen values and the
         eigen vectors of the matrix of inertia of the system."""

    @property
    def StaticMoments(self) -> object:
        """Returns Ix, Iy, Iz, the static moments of inertia of the
         current system; i.e. the moments of inertia about the
         three axes of the Cartesian coordinate system."""

    @property
    def Tolerance(self) -> float:
        """Set or get the tolerance of the vertex"""

    def centerOfCurvatureAt(self, paramval: float, /):
        """Get the center of curvature at the given parameter [First|Last] if defined
        centerOfCurvatureAt(paramval) -> Vector
                  """

    def curvatureAt(self, paramval: float, /):
        """Get the curvature at the given parameter [First|Last] if defined
        curvatureAt(paramval) -> Float
                  """

    def curveOnSurface(self, idx: int, /):
        """Returns the 2D curve, the surface, the placement and the parameter range of index idx.
        curveOnSurface(idx) -> None or tuple
        --
        Returns None if index idx is out of range.
        Returns a 5-items tuple of a curve, a surface, a placement, first parameter and last parameter.
                  """

    @typing.overload
    def derivative1At(self, paramval: float, /): ...

    @typing.overload
    def derivative1At(self, x_FirstParameter_0_5_x_LastParameter_x_FirstParameter_: float, /): ...

    @typing.overload
    def derivative1At(self, x_FirstParameter_3_5_x_LastParameter_x_FirstParameter_: float, /):
        """Get the first derivative at the given parameter value along the Edge if it is defined
        derivative1At(paramval) -> Vector
        --
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
                  """

    @typing.overload
    def derivative2At(self, paramval: float, /): ...

    @typing.overload
    def derivative2At(self, x_FirstParameter_0_5_x_LastParameter_x_FirstParameter_: float, /): ...

    @typing.overload
    def derivative2At(self, x_FirstParameter_3_5_x_LastParameter_x_FirstParameter_: float, /):
        """Get the second derivative at the given parameter value along the Edge if it is defined
        derivative2At(paramval) -> Vector
        --
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
                  """

    @typing.overload
    def derivative3At(self, paramval: float, /): ...

    @typing.overload
    def derivative3At(self, x_FirstParameter_0_5_x_LastParameter_x_FirstParameter_: float, /): ...

    @typing.overload
    def derivative3At(self, x_FirstParameter_3_5_x_LastParameter_x_FirstParameter_: float, /):
        """Get the third derivative at the given parameter value along the Edge if it is defined
        derivative3At(paramval) -> Vector
        --
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
                  """

    @typing.overload
    def discretize(self, kwargs: object, /): ...

    @typing.overload
    def discretize(self, Number: object, /): ...

    @typing.overload
    def discretize(self, QuasiNumber: object, /): ...

    @typing.overload
    def discretize(self, Distance: object, /): ...

    @typing.overload
    def discretize(self, Deflection: object, /): ...

    @typing.overload
    def discretize(self, QuasiDeflection: object, /): ...

    @typing.overload
    def discretize(self, Number: int, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, Distance: float, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, Deflection: float, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, QuasiNumber: int, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, QuasiDeflection: float, First: float = None, Last: float = None):
        """Discretizes the edge and returns a list of points.
        discretize(kwargs) -> list
        --
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
                  """

    def firstVertex(self, Orientation: bool = False, /):
        """Returns the Vertex of orientation FORWARD in this edge.
        firstVertex([Orientation=False]) -> Vertex
        --
        If there is none a Null shape is returned.
        Orientation = True : taking into account the edge orientation
                  """

    def getParameterByLength(self, pos: float, tolerance: float = 1e-7, /):
        """Get the value of the primary parameter at the given distance along the cartesian length of the edge.
        getParameterByLength(pos, [tolerance = 1e-7]) -> Float
        --
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
                """

    def isSeam(self, Face: Part.TopoShape, /):
        """Checks whether the edge is a seam edge.
        isSeam(Face)
                  """

    def lastVertex(self, Orientation: bool = False, /):
        """Returns the Vertex of orientation REVERSED in this edge.
        lastVertex([Orientation=False]) -> Vertex
        --
        If there is none a Null shape is returned.
        Orientation = True : taking into account the edge orientation
                  """

    @typing.overload
    def normalAt(self, paramval: float, /): ...

    @typing.overload
    def normalAt(self, x_FirstParameter_0_5_x_LastParameter_x_FirstParameter_: float, /): ...

    @typing.overload
    def normalAt(self, x_FirstParameter_3_5_x_LastParameter_x_FirstParameter_: float, /):
        """Get the normal direction at the given parameter value along the Edge if it is defined
        normalAt(paramval) -> Vector
        --
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
                  """

    def parameterAt(self, arg1: Part.TopoShape, arg2: Part.TopoShape = None, /):
        """Get the parameter at the given vertex if lying on the edge
        parameterAt(Vertex) -> Float
                    """

    def parameters(self, face: Part.TopoShape = None, /):
        """Get the list of parameters of the tessellation of an edge.
        parameters([face]) -> list
        --
        If the edge is part of a face then this face is required as argument.
        An exception is raised if the edge has no polygon.
                  """

    def split(self, paramval: object, /):
        """Splits the edge at the given parameter values and builds a wire out of it
        split(paramval) -> Wire
        --
        Args:
            paramval (float or int): The parameter value along the Edge at which to
                split it e.g:

                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)
                y = x.derivative3At(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))

        Returns:
            Wire: wire made up of two Edges
                  """

    @typing.overload
    def tangentAt(self, paramval: float, /): ...

    @typing.overload
    def tangentAt(self, x_FirstParameter_0_5_x_LastParameter_x_FirstParameter_: float, /): ...

    @typing.overload
    def tangentAt(self, x_FirstParameter_3_5_x_LastParameter_x_FirstParameter_: float, /):
        """Get the tangent direction at the given primary parameter value along the Edge if it is defined
        tangentAt(paramval) -> Vector
        --
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
                """

    @typing.overload
    def valueAt(self, paramval: float, /): ...

    @typing.overload
    def valueAt(self, x_FirstParameter_0_5_x_LastParameter_x_FirstParameter_: float, /): ...

    @typing.overload
    def valueAt(self, x_FirstParameter_3_5_x_LastParameter_x_FirstParameter_: float, /):
        """Get the value of the cartesian parameter value at the given parameter value along the Edge
        valueAt(paramval) -> Vector
        --
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
class BezierCurve(Part.BoundedCurve):
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
        """Returns the polynomial degree of this Bezier curve,
        which is equal to the number of poles minus 1."""

    @property
    def EndPoint(self) -> object:
        """Returns the end point of this Bezier curve."""

    @property
    def MaxDegree(self) -> int:
        """Returns the value of the maximum polynomial degree of any
        Bezier curve curve. This value is 25."""

    @property
    def NbPoles(self) -> int:
        """Returns the number of poles of this Bezier curve.
        				"""

    @property
    def StartPoint(self) -> object:
        """Returns the start point of this Bezier curve."""

    def getPole(self, arg1: int, /):
        """Get a pole of the Bezier curve."""

    def getPoles(self):
        """Get all poles of the Bezier curve."""

    def getResolution(self, arg1: float, /):
        """Computes for this Bezier curve the parametric tolerance (UTolerance)
        for a given 3D tolerance (Tolerance3D).
        If f(t) is the equation of this Bezier curve, the parametric tolerance
        ensures that:
        |t1-t0| < UTolerance =""==> |f(t1)-f(t0)| < Tolerance3D"""

    def getWeight(self, arg1: int, /):
        """Get a weight of the Bezier curve."""

    def getWeights(self):
        """Get all weights of the Bezier curve."""

    def increase(self, Int: int, /):
        """increase(Int=Degree)
        Increases the degree of this Bezier curve to Degree.
        As a result, the poles and weights tables are modified."""

    def insertPoleAfter(self, arg1: int, arg2: FreeCAD.Vector, arg3: float = None, /):
        """Inserts after the pole of index."""

    def insertPoleBefore(self, arg1: int, arg2: FreeCAD.Vector, arg3: float = None, /):
        """Inserts before the pole of index."""

    def interpolate(self, arg1: object, arg2: object = None, /):
        """Interpolates a list of constraints.
        				Each constraint is a list of a point and some optional derivatives
        				An optional list of parameters can be passed. It must be of same size as constraint list.
        				Otherwise, a simple uniform parametrization is used.
        				Example :
        				bezier.interpolate([[pt1, deriv11, deriv12], [pt2,], [pt3, deriv31]], [0, 0.4, 1.0])"""

    def isClosed(self):
        """Returns true if the distance between the start point and end point of
        					this Bezier curve is less than or equal to gp::Resolution().
        				"""

    def isPeriodic(self):
        """Returns false."""

    def isRational(self):
        """Returns false if the weights of all the poles of this Bezier curve are equal."""

    def removePole(self, arg1: int, /):
        """Removes the pole of index Index from the table of poles of this Bezier curve.
        If this Bezier curve is rational, it can become non-rational."""

    def segment(self, arg1: float, arg2: float, /):
        """Modifies this Bezier curve by segmenting it."""

    def setPole(self, arg1: int, arg2: FreeCAD.Vector, arg3: float = None, /):
        """Set a pole of the Bezier curve."""

    def setPoles(self, arg1: object, /):
        """Set the poles of the Bezier curve.

        				Takes a list of 3D Base.Vector objects."""

    def setWeight(self, arg1: int, arg2: float, /):
        """(id, weight) Set a weight of the Bezier curve.
        				"""


# GeometryStringExtensionPy.xml
class GeometryStringExtension(Part.GeometryExtension):
    """A GeometryExtension extending geometry objects with a string."""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: str, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: str, /):
        """A GeometryExtension extending geometry objects with a string."""

    @property
    def Value(self) -> str:
        """
                            returns the value of the GeometryStringExtension.
                        """

    @Value.setter
    def Value(self, value: str): ...


# GeometryDoubleExtensionPy.xml
class GeometryDoubleExtension(Part.GeometryExtension):
    """A GeometryExtension extending geometry objects with a double."""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: float, /): ...

    @typing.overload
    def __init__(self, arg1: float, arg2: str, /):
        """A GeometryExtension extending geometry objects with a double."""

    @property
    def Value(self) -> float:
        """
                        returns the value of the GeometryDoubleExtension.
                    """

    @Value.setter
    def Value(self, value: float): ...


# SurfaceOfRevolutionPy.xml
class SurfaceOfRevolution(Part.GeometrySurface):
    """Describes a surface of revolution"""

    def __init__(self, arg1: Part.Geometry, arg2: FreeCAD.Vector, arg3: FreeCAD.Vector, /):
        """Describes a surface of revolution"""

    @property
    def BasisCurve(self) -> object:
        """
        					Sets or gets the basic curve.
        				"""

    @property
    def Direction(self) -> object:
        """
        					Sets or gets the direction of revolution.
        				"""

    @property
    def Location(self) -> object:
        """
        					Sets or gets the location of revolution.
        				"""


# LineSegmentPy.xml
class LineSegment(Part.TrimmedCurve):
    """Describes a line segment
    To create a line segment there are several ways:
    Part.LineSegment()
        Creates a default line segment

    Part.LineSegment(LineSegment)
        Creates a copy of the given line segment

    Part.LineSegment(Point1,Point2)
        Creates a line segment that goes through two given points"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, LineSegment: Part.LineSegment, /): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, /):
        """Describes a line segment
        To create a line segment there are several ways:
        Part.LineSegment()
            Creates a default line segment

        Part.LineSegment(LineSegment)
            Creates a copy of the given line segment

        Part.LineSegment(Point1,Point2)
            Creates a line segment that goes through two given points"""

    @property
    def EndPoint(self) -> object:
        """Returns the end point point of this line."""

    @EndPoint.setter
    def EndPoint(self, value: object): ...

    @property
    def StartPoint(self) -> object:
        """Returns the start point of this line."""

    @StartPoint.setter
    def StartPoint(self, value: object): ...

    def setParameterRange(self, arg1: float, arg2: float, /):
        """Set the parameter range of the underlying line geometry"""


# GeometryPy.xml
class Geometry(FreeCAD.Persistence):
    """The abstract class Geometry for 3D space is the root class of all geometric objects.
    It describes the common behavior of these objects when:
    - applying geometric transformations to objects, and
    - constructing objects by geometric transformation (including copying)."""

    @property
    def Tag(self) -> str:
        """Gives the tag of the geometry as string."""

    def clone(self):
        """Create a clone of this geometry with the same Tag"""

    def copy(self):
        """Create a copy of this geometry"""

    def deleteExtensionOfName(self, arg1: str, /):
        """Deletes all extensions of the indicated name."""

    def deleteExtensionOfType(self, arg1: str, /):
        """Deletes all extensions of the indicated type."""

    def getExtensionOfName(self, arg1: str, /):
        """Gets the first geometry extension of the name indicated by the string."""

    def getExtensionOfType(self, arg1: str, /):
        """Gets the first geometry extension of the type indicated by the string."""

    def getExtensions(self):
        """Returns a list with information about the geometry extensions."""

    def hasExtensionOfName(self, arg1: str, /):
        """Returns a boolean indicating whether a geometry extension with the name indicated as a string exists."""

    def hasExtensionOfType(self, arg1: str, /):
        """Returns a boolean indicating whether a geometry extension of the type indicated as a string exists."""

    @typing.overload
    def mirror(self, arg1: FreeCAD.Vector, /): ...

    @typing.overload
    def mirror(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, /):
        """Performs the symmetrical transformation of this geometric object"""

    def rotate(self, arg1: FreeCAD.Placement, /):
        """Rotates this geometric object at angle Ang (in radians) about axis"""

    @typing.overload
    def scale(self, arg1: FreeCAD.Vector, arg2: float, /): ...

    @typing.overload
    def scale(self, arg1: tuple, arg2: float, /):
        """Applies a scaling transformation on this geometric object with a center and scaling factor"""

    def setExtension(self, arg1: Part.GeometryExtension, /):
        """Sets a geometry extension of the indicated type."""

    def transform(self, arg1: FreeCAD.Matrix, /):
        """Applies a transformation to this geometric object"""

    @typing.overload
    def translate(self, arg1: FreeCAD.Vector, /): ...

    @typing.overload
    def translate(self, arg1: tuple, /):
        """Translates this geometric object"""


# GeometryCurvePy.xml
class Curve(Part.Geometry):
    """
    				The abstract class GeometryCurve is the root class of all curve objects.
    			"""

    @property
    def Continuity(self) -> str:
        """
        					Returns the global continuity of the curve.
        				"""

    @property
    def FirstParameter(self) -> float:
        """
        					Returns the value of the first parameter.
        				"""

    @property
    def LastParameter(self) -> float:
        """
        					Returns the value of the last parameter.
        				"""

    @property
    def Rotation(self) -> object:
        """Returns a rotation object to describe the orientation for curve that supports it"""

    def approximateBSpline(self, Tolerance: float, MaxSegments: int, MaxDegree: int, Order: str = 'C2', /):
        """
        					Approximates a curve of any type to a B-Spline curve
        					approximateBSpline(Tolerance, MaxSegments, MaxDegree, [Order='C2']) -> B-Spline curve
        				"""

    def centerOfCurvature(self, float_pos: float, /):
        """Vector = centerOfCurvature(float pos) - Get the center of curvature at the given parameter [First|Last] if defined"""

    def continuityWith(self, arg1: Part.Curve, arg2: float = None, arg3: float = None, arg4: bool = None, arg5: bool = None, arg6: float = None, arg7: float = None, /):
        """Computes the continuity of two curves"""

    def curvature(self, pos: float, /):
        """Float = curvature(pos) - Get the curvature at the given parameter [First|Last] if defined"""

    @typing.overload
    def discretize(self, Number: object, /): ...

    @typing.overload
    def discretize(self, QuasiNumber: object, /): ...

    @typing.overload
    def discretize(self, Distance: object, /): ...

    @typing.overload
    def discretize(self, Deflection: object, /): ...

    @typing.overload
    def discretize(self, QuasiDeflection: object, /): ...

    @typing.overload
    def discretize(self, Number: int, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, Distance: float, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, Deflection: float, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, QuasiNumber: int, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, QuasiDeflection: float, First: float = None, Last: float = None):
        """Discretizes the curve and returns a list of points.
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
        """

    def getD0(self, arg1: float, /):
        """Returns the point of given parameter"""

    def getD1(self, arg1: float, /):
        """Returns the point and first derivative of given parameter"""

    def getD2(self, arg1: float, /):
        """Returns the point, first and second derivatives"""

    def getD3(self, arg1: float, /):
        """Returns the point, first, second and third derivatives"""

    def getDN(self, arg1: float, arg2: int, /):
        """Returns the n-th derivative"""

    @typing.overload
    def intersect(self, arg1: Part.Curve, arg2: float = None, /): ...

    @typing.overload
    def intersect(self, arg1: Part.GeometrySurface, arg2: float = None, /):
        """
                          Returns all intersection points and curve segments between the curve and the curve/surface.

        				  arguments: curve/surface (for the intersection), precision (float)
                      """

    def intersect2d(self, arg1: Part.Curve, arg2: Part.Plane, /):
        """Get intersection points with another curve lying on a plane."""

    def intersectCC(self, arg1: Part.Curve, arg2: float = None, /):
        """
                          Returns all intersection points between this curve and the given curve.
                      """

    def intersectCS(self, arg1: Part.GeometrySurface, arg2: float = None, /):
        """
                          Returns all intersection points and curve segments between the curve and the surface.
                      """

    def isClosed(self):
        """
                      Returns true if the curve is closed.
                    """

    def isPeriodic(self):
        """Returns true if this curve is periodic."""

    def length(self, uMin: float = None, uMax: float = None, Tol: float = None, /):
        """Computes the length of a curve
        length([uMin,uMax,Tol]) -> Float"""

    def makeRuledSurface(self, arg1: Part.Curve, /):
        """Make a ruled surface of this and the given curves"""

    def normal(self, pos: float, /):
        """Vector = normal(pos) - Get the normal vector at the given parameter [First|Last] if defined"""

    def parameter(self, arg1: FreeCAD.Vector, /):
        """Returns the parameter on the curve
        of the nearest orthogonal projection of the point."""

    def parameterAtDistance(self, abscissa: float, startingParameter: float = None, /):
        """Returns the parameter on the curve of a point at the given distance from a starting parameter.
        parameterAtDistance([abscissa, startingParameter]) -> Float the"""

    def period(self):
        """Returns the period of this curve
        or raises an exception if it is not periodic."""

    def reverse(self):
        """Changes the direction of parametrization of the curve."""

    def reversedParameter(self, arg1: float, /):
        """Returns the parameter on the reversed curve for
        the point of parameter U on this curve."""

    def tangent(self, arg1: float, /):
        """Computes the tangent of parameter u on this curve"""

    def toBSpline(self, Float: float = None, Float2: float = None, /):
        """
        					Converts a curve of any type (only part from First to Last)
        					toBSpline([Float=First, Float=Last]) -> B-Spline curve
        				"""

    def toNurbs(self, Float: float = None, Float2: float = None, /):
        """
                            Converts a curve of any type (only part from First to Last)
                            toNurbs([Float=First, Float=Last]) -> NURBS curve
                        """

    def toShape(self, arg1: float = None, arg2: float = None, /):
        """Return the shape for the geometry."""

    def trim(self, Float: float = None, Float2: float = None, /):
        """
                            Returns a trimmed curve defined in the given parameter range
                            trim([Float=First, Float=Last]) -> trimmed curve
                        """

    def value(self, arg1: float, /):
        """Computes the point of parameter u on this curve"""


# ConePy.xml
class Cone(Part.GeometrySurface):
    """Describes a cone in 3D space
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
    def __init__(self, Cone: Part.Cone, Distance: float): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, Radius1: float, Radius2: float): ...

    @typing.overload
    def __init__(self, Point1: FreeCAD.Vector, Point2: FreeCAD.Vector, Point3: FreeCAD.Vector, Point4: FreeCAD.Vector):
        """Describes a cone in 3D space
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

    @property
    def Apex(self) -> object:
        """Compute the apex of the cone."""

    @property
    def Axis(self) -> object:
        """The axis direction of the cone"""

    @Axis.setter
    def Axis(self, value: object): ...

    @property
    def Center(self) -> object:
        """Center of the cone."""

    @Center.setter
    def Center(self, value: object): ...

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


# ToroidPy.xml
class Toroid(Part.GeometrySurface):
    """Describes a toroid in 3D space"""

    def __init__(self):
        """Describes a toroid in 3D space"""

    @property
    def Area(self) -> float:
        """Compute the area of the toroid."""

    @property
    def Axis(self) -> object:
        """The axis direction of the toroid"""

    @Axis.setter
    def Axis(self, value: object): ...

    @property
    def Center(self) -> object:
        """Center of the toroid."""

    @Center.setter
    def Center(self, value: object): ...

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


# AttachExtensionPy.xml
class AttachExtension(FreeCAD.DocumentObjectExtension):
    """This object represents an attachable object with OCC shape."""

    @property
    def Attacher(self) -> object:
        """AttachEngine object driving this AttachableObject. Returns a copy."""

    def changeAttacherType(self, typename: str, /):
        """changeAttacherType(typename): Changes Attacher class of this object.
        typename: string. The following are accepted so far:
        'Attacher::AttachEngine3D'
        'Attacher::AttachEnginePlane'
        'Attacher::AttachEngineLine'
        'Attacher::AttachEnginePoint'"""

    def positionBySupport(self):
        """positionBySupport(): Reposition object based on Support, MapMode and MapPathParameter properties.
        Returns True if attachment calculation was successful, false if object is not attached and Placement wasn't updated,
        and raises an exception if attachment calculation fails."""


# Part2DObjectPy.xml
class Part2DObject(Part.Feature):
    """This object represents a 2D Shape in a 3D World"""


# ArcOfEllipsePy.xml
class ArcOfEllipse(Part.ArcOfConic):
    """Describes a portion of an ellipse"""

    def __init__(self, arg1: Part.Ellipse, arg2: float, arg3: float, arg4: bool = None, /):
        """Describes a portion of an ellipse"""

    @property
    def Ellipse(self) -> object:
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


# GeometryExtensionPy.xml
class GeometryExtension(FreeCAD.PyObjectBase):
    """The abstract class GeometryExtension enables to extend geometry objects with application specific data."""

    @property
    def Name(self) -> str:
        """Sets/returns the name of this extension."""

    @Name.setter
    def Name(self, value: str): ...

    def copy(self):
        """Create a copy of this geometry extension."""


# BRepOffsetAPI_MakeFillingPy.xml
class BRepOffsetAPI_MakeFilling(FreeCAD.PyObjectBase):
    """N-Side Filling"""

    def __init__(self, Degree: int = None, NbPtsOnCur: int = None, NbIter: int = None, MaxDegree: int = None, MaxSegments: int = None, Tol2d: float = None, Tol3d: float = None, TolAng: float = None, TolCurv: float = None, Anisotropy: bool = None):
        """N-Side Filling"""

    def G0Error(self, int: int = None, /):
        """
                          G0Error([int])
                          Returns the maximum distance between the result and the constraints.
                      """

    def G1Error(self, int: int = None, /):
        """
                          G1Error([int])
                          Returns the maximum angle between the result and the constraints.
                      """

    def G2Error(self, int: int = None, /):
        """
                          G2Error([int])
                          Returns the greatest difference in curvature between the result and the constraints.
                      """

    @typing.overload
    def add(self, Constraint: Part.TopoShape, Order: int, IsBound: bool = True): ...

    @typing.overload
    def add(self, Constraint: Part.TopoShape, Support: Part.TopoShape, Order: int, IsBound: bool = True): ...

    @typing.overload
    def add(self, U: float, V: float, Support: Part.TopoShape, Order: int): ...

    @typing.overload
    def add(self, Support: Part.TopoShape, Order: int): ...

    @typing.overload
    def add(self, Point: FreeCAD.Vector): ...

    @typing.overload
    def add(self, Constraint: Part.TopoShape, Support: Part.TopoShape, Order: int, IsBound: bool = None):
        """
                          add(Edge, Order, IsBound=True)
                          add(Edge, Support, Order, IsBound=True)
                          add(Support, Order)
                          add(Point)
                          add(U, V, Support, Order)
                          Adds a new constraint.
                      """

    def build(self):
        """Builds the resulting faces."""

    def isDone(self):
        """Tests whether computation of the filling plate has been completed."""

    def loadInitSurface(self, face: Part.TopoShape, /):
        """
                          loadInitSurface(face)
                          Loads the initial surface.
                      """

    def setApproxParam(self, MaxDegree: int = 8, MaxSegments: int = 9):
        """
                          setApproxParam(MaxDeg=8, MaxSegments=9)
                          Sets the parameters used to approximate the filling the surface
                      """

    def setConstrParam(self, Tol2d: float = 0.00001, Tol3d: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1):
        """
                          setConstrParam(Tol2d=0.00001, Tol3d=0.0001, TolAng=0.01, TolCurv=0.1)
                          Sets the values of Tolerances used to control the constraint.
                      """

    def setResolParam(self, Degree: int = 3, NbPtsOnCur: int = 15, NbIter: int = 2, Anisotropy: bool = False):
        """
                          setResolParam(Degree=3, NbPtsOnCur=15, NbIter=2, Anisotropy=False)
                          Sets the parameters used for resolution.
                      """

    def shape(self):
        """
                          shape()
                          Returns the resulting shape.
                      """


# BezierSurfacePy.xml
class BezierSurface(Part.GeometrySurface):
    """Describes a rational or non-rational Bezier surface
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
        """
        					Returns the number of poles in u direction of this Bezier surface.
        				"""

    @property
    def NbVPoles(self) -> int:
        """
        					Returns the number of poles in v direction of this Bezier surface.
        				"""

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

    def bounds(self):
        """
        					Returns the parametric bounds (U1, U2, V1, V2) of this Bezier surface.
        				"""

    def exchangeUV(self):
        """
        					Exchanges the u and v parametric directions on this Bezier surface.
        					As a consequence:
        					-- the poles and weights tables are transposed,
        					-- degrees, rational characteristics and so on are exchanged between
        					   the two parametric directions, and
        					-- the orientation of the surface is reversed.
        				"""

    def getPole(self, arg1: int, arg2: int, /):
        """Get a pole of index (UIndex,VIndex) of the Bezier surface."""

    def getPoles(self):
        """Get all poles of the Bezier surface."""

    def getResolution(self, arg1: float, /):
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
        				"""

    def getWeight(self, arg1: int, arg2: int, /):
        """
        					Get a weight of the pole of index (UIndex,VIndex)
        					of the Bezier surface.
        				"""

    def getWeights(self):
        """Get all weights of the Bezier surface."""

    def increase(self, Int: int, Int2: int, /):
        """
        					increase(Int=DegreeU,Int=DegreeV)
        					Increases the degree of this Bezier surface in the two
        					parametric directions.
        				"""

    def insertPoleColAfter(self, arg1: int, arg2: object, arg3: object = None, /):
        """
        					Inserts into the table of poles of this surface, after the column
        					of poles of index.
        					If this Bezier surface is non-rational, it can become rational if
        					the weights associated with the new poles are different from each
        					other, or collectively different from the existing weights in the
        					table.
        				"""

    def insertPoleColBefore(self, arg1: int, arg2: object, arg3: object = None, /):
        """
        					Inserts into the table of poles of this surface, before the column
        					of poles of index.
        					If this Bezier surface is non-rational, it can become rational if
        					the weights associated with the new poles are different from each
        					other, or collectively different from the existing weights in the
        					table.
        				"""

    def insertPoleRowAfter(self, arg1: int, arg2: object, arg3: object = None, /):
        """
        					Inserts into the table of poles of this surface, after the row
        					of poles of index.
        					If this Bezier surface is non-rational, it can become rational if
        					the weights associated with the new poles are different from each
        					other, or collectively different from the existing weights in the
        					table.
        				"""

    def insertPoleRowBefore(self, arg1: int, arg2: object, arg3: object = None, /):
        """
        					Inserts into the table of poles of this surface, before the row
        					of poles of index.
        					If this Bezier surface is non-rational, it can become rational if
        					the weights associated with the new poles are different from each
        					other, or collectively different from the existing weights in the
        					table.
        				"""

    def isUClosed(self):
        """
        					Checks if this surface is closed in the u parametric direction.
        					Returns true if, in the table of poles the first row and the last
        					row are identical.
        				"""

    def isUPeriodic(self):
        """Returns false."""

    def isURational(self):
        """
        					Returns false if the equation of this Bezier surface is polynomial
        					(e.g. non-rational) in the u or v parametric direction.
        					In other words, returns false if for each row of poles, the associated
        					weights are identical
        				"""

    def isVClosed(self):
        """
        					Checks if this surface is closed in the v parametric direction.
        					Returns true if, in the table of poles the first column and the
        					last column are identical.
        				"""

    def isVPeriodic(self):
        """Returns false."""

    def isVRational(self):
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
        				"""

    def removePoleRow(self, int: int, /):
        """
        					removePoleRow(int=UIndex)
        					Removes the row of poles of index UIndex from the table of
        					poles of this Bezier surface.
        					If this Bezier curve is rational, it can become non-rational.
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
        				"""

    def setPole(self, arg1: int, arg2: int, arg3: FreeCAD.Vector, arg4: float = None, /):
        """Set a pole of the Bezier surface."""

    def setPoleCol(self, arg1: int, arg2: object, arg3: object = None, /):
        """Set the column of poles of the Bezier surface."""

    def setPoleRow(self, arg1: int, arg2: object, arg3: object = None, /):
        """Set the row of poles of the Bezier surface."""

    def setWeight(self, arg1: int, arg2: int, arg3: float, /):
        """
        					Set the weight of pole of the index (UIndex, VIndex)
        					for the Bezier surface.
        				"""

    def setWeightCol(self, arg1: int, arg2: object, /):
        """
        					Set the weights of the poles in the column of poles
        					of index VIndex of the Bezier surface.
        				"""

    def setWeightRow(self, arg1: int, arg2: object, /):
        """
        					Set the weights of the poles in the row of poles
        					of index UIndex of the Bezier surface.
        				"""


# BodyBasePy.xml
class BodyBase(Part.Feature):
    """Base class of all Body objects"""


# ArcOfConicPy.xml
class ArcOfConic(Part.TrimmedCurve):
    """Describes a portion of a conic"""

    @property
    def AngleXU(self) -> float:
        """The angle between the X axis and the major axis of the conic."""

    @AngleXU.setter
    def AngleXU(self, value: float): ...

    @property
    def Axis(self) -> object:
        """The axis direction of the conic"""

    @Axis.setter
    def Axis(self, value: object): ...

    @property
    def Center(self) -> object:
        """Deprecated -- use Location."""

    @Center.setter
    def Center(self, value: object): ...

    @property
    def Location(self) -> object:
        """Center of the conic."""

    @Location.setter
    def Location(self, value: object): ...

    @property
    def XAxis(self) -> object:
        """The X axis direction of the circle"""

    @XAxis.setter
    def XAxis(self, value: object): ...

    @property
    def YAxis(self) -> object:
        """The Y axis direction of the circle"""

    @YAxis.setter
    def YAxis(self, value: object): ...


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
        """Extracts the array of curves on the plate surface which
                correspond to the curve constraints set in add()
                """

    def disc2dContour(self, arg1: int, /): ...

    def disc3dContour(self, arg1: int, arg2: int, /): ...

    def init(self):
        """Resets all constraints"""

    def isDone(self):
        """Tests whether computation of the plate has been completed"""

    def loadInitSurface(self, arg1: Part.GeometrySurface, /):
        """ Loads the initial surface"""

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
        """ Returns the initial surface"""

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
        """The number of points on the curve used as a
        constraint. The default setting is 10. This parameter
        affects computation time, which increases by the cube of
        the number of points."""

    def G0Criterion(self, arg1: float, /):
        """Returns the G0 criterion at the parametric point U on
        the curve. This is the greatest distance allowed between
        the constraint and the target surface at U.
                """

    def G1Criterion(self, arg1: float, /):
        """Returns the G1 criterion at the parametric point U on
        the curve. This is the greatest angle allowed between
        the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
                """

    def G2Criterion(self, arg1: float, /):
        """Returns the G2 criterion at the parametric point U on
        the curve. This is the greatest difference in curvature
        allowed between the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
                """

    def curve2dOnSurf(self): ...

    def curve3d(self): ...

    def order(self):
        """Returns the order of constraint, one of G0, G1 or G2"""

    def projectedCurve(self): ...

    def setCurve2dOnSurf(self, arg1: Part.Curve2d, /): ...

    def setOrder(self, arg1: int, /):
        """Allows you to set the order of continuity required for
        the constraints: G0, G1, and G2, controlled
        respectively by G0Criterion G1Criterion and G2Criterion.
                """

    def setProjectedCurve(self, arg1: Part.Curve2d, arg2: float, arg3: float, /): ...


# PointConstraintPy.xml
class PointConstraintPy(FreeCAD.PyObjectBase):
    """Defines points as constraints to be used to deform a surface"""

    def __init__(self, Point: FreeCAD.Vector, Order: int = None, TolDist: float = None):
        """Defines points as constraints to be used to deform a surface"""

    def G0Criterion(self):
        """Returns the G0 criterion at the parametric point U on
        the curve. This is the greatest distance allowed between
        the constraint and the target surface at U.
                """

    def G1Criterion(self):
        """Returns the G1 criterion at the parametric point U on
        the curve. This is the greatest angle allowed between
        the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
                """

    def G2Criterion(self):
        """Returns the G2 criterion at the parametric point U on
        the curve. This is the greatest difference in curvature
        allowed between the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
                """

    def hasPnt2dOnSurf(self): ...

    def order(self):
        """Returns the order of constraint, one of G0, G1 or G2"""

    def pnt2dOnSurf(self): ...

    def setG0Criterion(self, arg1: float, /):
        """Allows you to set the G0 criterion. This is the law
        defining the greatest distance allowed between the
        constraint and the target surface for each point of the
        constraint. If this criterion is not set, TolDist, the
        distance tolerance from the constructor, is used.
                """

    def setG1Criterion(self, arg1: float, /):
        """Allows you to set the G1 criterion. This is the law
        defining the greatest angle allowed between the
        constraint and the target surface. If this criterion is not
        set, TolAng, the angular tolerance from the constructor, is used.
        Raises an exception if  the  curve  is  not  on  a  surface
                """

    def setG2Criterion(self, arg1: float, /): ...

    def setOrder(self, arg1: int, /):
        """Allows you to set the order of continuity required for
        the constraints: G0, G1, and G2, controlled
        respectively by G0Criterion G1Criterion and G2Criterion.
                """

    def setPnt2dOnSurf(self, arg1: float, arg2: float, /): ...


# Curve2dPy.xml
class Curve2d(Part.Geometry2d):
    """
                    The abstract class Geom2dCurve is the root class of all curve objects.
    			"""

    @property
    def Closed(self) -> bool:
        """
                            Returns true if the curve is closed.
                        """

    @property
    def Continuity(self) -> str:
        """
        					Returns the global continuity of the curve.
        				"""

    @property
    def FirstParameter(self) -> float:
        """
        					Returns the value of the first parameter.
        				"""

    @property
    def LastParameter(self) -> float:
        """
        					Returns the value of the last parameter.
        				"""

    @property
    def Periodic(self) -> bool:
        """
                            Returns true if the curve is periodic.
                        """

    def approximateBSpline(self, Tolerance: float, MaxSegments: int, MaxDegree: int, Order: str = 'C2', /):
        """
        					Approximates a curve of any type to a B-Spline curve
        					approximateBSpline(Tolerance, MaxSegments, MaxDegree, [Order='C2']) -> B-Spline curve
        				"""

    def centerOfCurvature(self, float_pos: float, /):
        """Vector = centerOfCurvature(float pos) - Get the center of curvature at the given parameter [First|Last] if defined"""

    def curvature(self, pos: float, /):
        """Float = curvature(pos) - Get the curvature at the given parameter [First|Last] if defined"""

    @typing.overload
    def discretize(self, Number: int, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, Distance: float, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, Deflection: float, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, QuasiNumber: int, First: float = None, Last: float = None): ...

    @typing.overload
    def discretize(self, QuasiDeflection: float, First: float = None, Last: float = None):
        """Discretizes the curve and returns a list of points.
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
        """

    def intersectCC(self, arg1: Part.Curve2d, arg2: float = None, /):
        """
                            Returns all intersection points between this curve and the given curve.
                        """

    def length(self, uMin: float = None, uMax: float = None, Tol: float = None, /):
        """Computes the length of a curve
        length([uMin,uMax,Tol]) -> Float"""

    def normal(self, pos: float, /):
        """Vector = normal(pos) - Get the normal vector at the given parameter [First|Last] if defined"""

    def parameter(self, arg1: object, /):
        """Returns the parameter on the curve
        of the nearest orthogonal projection of the point."""

    def parameterAtDistance(self, abscissa: float, startingParameter: float = None, /):
        """Returns the parameter on the curve of a point at the given distance from a starting parameter. 
        parameterAtDistance([abscissa, startingParameter]) -> Float the"""

    def reverse(self):
        """Changes the direction of parametrization of the curve."""

    def tangent(self, arg1: float, /):
        """Computes the tangent of parameter u on this curve"""

    def toBSpline(self, Float: float = None, Float2: float = None, /):
        """
        					Converts a curve of any type (only part from First to Last)
        					toBSpline([Float=First, Float=Last]) -> B-Spline curve
        				"""

    @typing.overload
    def toShape(self): ...

    @typing.overload
    def toShape(self, arg1: float, arg2: float, /): ...

    @typing.overload
    def toShape(self, arg1: Part.GeometrySurface, /): ...

    @typing.overload
    def toShape(self, arg1: Part.GeometrySurface, arg2: float, arg3: float, /): ...

    @typing.overload
    def toShape(self, arg1: Part.TopoShape, /): ...

    @typing.overload
    def toShape(self, arg1: Part.TopoShape, arg2: float, arg3: float, /):
        """Return the shape for the geometry."""

    def value(self, arg1: float, /):
        """Computes the point of parameter u on this curve"""


# ArcOfEllipse2dPy.xml
class ArcOfEllipse2d(Part.ArcOfConic2d):
    """Describes a portion of an ellipse"""

    def __init__(self, arg1: Part.Ellipse2d, arg2: float, arg3: float, arg4: bool = None, /):
        """Describes a portion of an ellipse"""

    @property
    def Ellipse(self) -> object:
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
class ArcOfConic2d(Part.Curve2d):
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
    def Location(self) -> object:
        """Location of the conic."""

    @Location.setter
    def Location(self, value: object): ...

    @property
    def XAxis(self) -> object:
        """The X axis direction of the circle"""

    @XAxis.setter
    def XAxis(self, value: object): ...

    @property
    def YAxis(self) -> object:
        """The Y axis direction of the circle"""

    @YAxis.setter
    def YAxis(self, value: object): ...


# Conic2dPy.xml
class Conic2d(Part.Curve2d):
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
    def Location(self) -> object:
        """Location of the conic."""

    @Location.setter
    def Location(self, value: object): ...

    @property
    def XAxis(self) -> object:
        """The X axis direction of the circle"""

    @XAxis.setter
    def XAxis(self, value: object): ...

    @property
    def YAxis(self) -> object:
        """The Y axis direction of the circle"""

    @YAxis.setter
    def YAxis(self, value: object): ...


# Geometry2dPy.xml
class Geometry2d(FreeCAD.PyObjectBase):
    """The abstract class Geometry for 2D space is the root class of all geometric objects.
    It describes the common behavior of these objects when:
    - applying geometric transformations to objects, and
    - constructing objects by geometric transformation (including copying)."""

    def copy(self):
        """Create a copy of this geometry"""

    @typing.overload
    def mirror(self, arg1: object, /): ...

    @typing.overload
    def mirror(self, arg1: object, arg2: object, /):
        """Performs the symmetrical transformation of this geometric object"""

    def rotate(self, arg1: object, arg2: float, /):
        """Rotates this geometric object at angle Ang (in radians) around a point"""

    def scale(self, arg1: object, arg2: float, /):
        """Applies a scaling transformation on this geometric object with a center and scaling factor"""

    def transform(self, arg1: object, /):
        """Applies a transformation to this geometric object"""

    def translate(self, arg1: object, /):
        """Translates this geometric object"""


# Circle2dPy.xml
class Circle2d(Part.Conic2d):
    """Describes a circle in 3D space
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
    def __init__(self, Circle: Part.Circle2d): ...

    @typing.overload
    def __init__(self, Circle: Part.Circle2d, Distance: float): ...

    @typing.overload
    def __init__(self, Center: object, Radius: float): ...

    @typing.overload
    def __init__(self, Point1: object, Point2: object, Point3: object):
        """Describes a circle in 3D space
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

    @property
    def Radius(self) -> float:
        """The radius of the circle."""

    @Radius.setter
    def Radius(self, value: float): ...


# ArcOfParabola2dPy.xml
class ArcOfParabola2d(Part.ArcOfConic2d):
    """Describes a portion of a parabola"""

    def __init__(self, arg1: Part.Parabola2d, arg2: float, arg3: float, arg4: bool = None, /):
        """Describes a portion of a parabola"""

    @property
    def Focal(self) -> float:
        """The focal length of the parabola."""

    @Focal.setter
    def Focal(self, value: float): ...

    @property
    def Parabola(self) -> object:
        """The internal parabola representation"""


# Line2dSegmentPy.xml
class Line2dSegment(Part.Curve2d):
    """Describes a line segment in 2D space
    To create a line there are several ways:
    Part.Geom2d.Line2dSegment()
        Creates a default line

    Part.Geom2d.Line2dSegment(Line)
        Creates a copy of the given line

    Part.Geom2d.Line2dSegment(Point1,Point2)
        Creates a line that goes through two given points"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Line: Part.Line2dSegment, /): ...

    @typing.overload
    def __init__(self, Point1: object, Point2: object, /):
        """Describes a line segment in 2D space
        To create a line there are several ways:
        Part.Geom2d.Line2dSegment()
            Creates a default line

        Part.Geom2d.Line2dSegment(Line)
            Creates a copy of the given line

        Part.Geom2d.Line2dSegment(Point1,Point2)
            Creates a line that goes through two given points"""

    @property
    def EndPoint(self) -> object:
        """Returns the end point of this line segment."""

    @EndPoint.setter
    def EndPoint(self, value: object): ...

    @property
    def StartPoint(self) -> object:
        """Returns the start point of this line segment."""

    @StartPoint.setter
    def StartPoint(self, value: object): ...

    def setParameterRange(self, arg1: float, arg2: float, /):
        """Set the parameter range of the underlying line segment geometry"""


# Ellipse2dPy.xml
class Ellipse2d(Part.Conic2d):
    """Describes an ellipse in 2D space
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
    def __init__(self, Ellipse: Part.Ellipse2d): ...

    @typing.overload
    def __init__(self, S1: object, S2: object, Center: object): ...

    @typing.overload
    def __init__(self, Center: object, MajorRadius: float, MinorRadius: float):
        """Describes an ellipse in 2D space
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

    @property
    def Focal(self) -> float:
        """The focal distance of the ellipse."""

    @property
    def Focus1(self) -> object:
        """The first focus is on the positive side of the major axis of the ellipse;
        the second focus is on the negative side."""

    @property
    def Focus2(self) -> object:
        """The first focus is on the positive side of the major axis of the ellipse;
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
class ArcOfCircle2d(Part.ArcOfConic2d):
    """Describes a portion of a circle"""

    @typing.overload
    def __init__(self, arg1: Part.Circle2d, arg2: float, arg3: float, arg4: bool = None, /): ...

    @typing.overload
    def __init__(self, arg1: object, arg2: object, arg3: object, /):
        """Describes a portion of a circle"""

    @property
    def Circle(self) -> object:
        """The internal circle representation"""

    @property
    def Radius(self) -> float:
        """The radius of the circle."""

    @Radius.setter
    def Radius(self, value: float): ...


# ArcOfHyperbola2dPy.xml
class ArcOfHyperbola2d(Part.ArcOfConic2d):
    """Describes a portion of an hyperbola"""

    def __init__(self, arg1: Part.Hyperbola2d, arg2: float, arg3: float, arg4: bool = None, /):
        """Describes a portion of an hyperbola"""

    @property
    def Hyperbola(self) -> object:
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
class Hyperbola2d(Part.Conic2d):
    """Describes a hyperbola in 2D space
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
    def __init__(self, Hyperbola: Part.Hyperbola2d): ...

    @typing.overload
    def __init__(self, S1: object, S2: object, Center: object): ...

    @typing.overload
    def __init__(self, Center: object, MajorRadius: float, MinorRadius: float):
        """Describes a hyperbola in 2D space
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

    @property
    def Focal(self) -> float:
        """The focal distance of the hyperbola."""

    @property
    def Focus1(self) -> object:
        """The first focus is on the positive side of the major axis of the hyperbola;
        the second focus is on the negative side."""

    @property
    def Focus2(self) -> object:
        """The first focus is on the positive side of the major axis of the hyperbola;
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
class BSplineCurve2d(Part.Curve2d):
    """Describes a B-Spline curve in 3D space"""

    def __init__(self):
        """Describes a B-Spline curve in 3D space"""

    @property
    def Degree(self) -> int:
        """Returns the polynomial degree of this B-Spline curve."""

    @property
    def EndPoint(self) -> object:
        """Returns the end point of this B-Spline curve."""

    @property
    def FirstUKnotIndex(self) -> object:
        """Returns the index in the knot array of the knot
        corresponding to the first or last parameter
        of this B-Spline curve."""

    @property
    def KnotSequence(self) -> list:
        """Returns the knots sequence of this B-Spline curve."""

    @property
    def LastUKnotIndex(self) -> object:
        """Returns the index in the knot array of the knot
        corresponding to the first or last parameter
        of this B-Spline curve."""

    @property
    def MaxDegree(self) -> int:
        """Returns the value of the maximum polynomial degree of any
        B-Spline curve curve. This value is 25."""

    @property
    def NbKnots(self) -> int:
        """
        					Returns the number of knots of this B-Spline curve.
        				"""

    @property
    def NbPoles(self) -> int:
        """Returns the number of poles of this B-Spline curve.
        				"""

    @property
    def StartPoint(self) -> object:
        """Returns the start point of this B-Spline curve."""

    def approximate(self, Points: object, DegMax: int = None, Continuity: str = None, Tolerance: float = None, DegMin: int = None, ParamType: str = None, Parameters: object = None, LengthWeight: float = None, CurvatureWeight: float = None, TorsionWeight: float = None):
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
        				"""

    def buildFromPoles(self, arg1: object, arg2: bool = None, arg3: int = None, arg4: bool = None, /):
        """
        					Builds a B-Spline by a list of poles.
        				"""

    def buildFromPolesMultsKnots(self, poles: object, mults: object = None, knots: object = None, periodic: bool = None, degree: int = None, weights: object = None):
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
        			"""

    @typing.overload
    def getCardinalSplineTangents(self, Points: object, Parameter: float): ...

    @typing.overload
    def getCardinalSplineTangents(self, Points: object, Parameters: object):
        """Compute the tangents for a Cardinal spline"""

    def getKnot(self, arg1: int, /):
        """Get a knot of the B-Spline curve."""

    def getKnots(self):
        """Get all knots of the B-Spline curve."""

    def getMultiplicities(self):
        """
        					Returns the multiplicities table M of the knots of this B-Spline curve.
        				"""

    def getMultiplicity(self, arg1: int, /):
        """Returns the multiplicity of the knot of index
        from the knots table of this B-Spline curve."""

    def getPole(self, arg1: int, /):
        """Get a pole of the B-Spline curve."""

    def getPoles(self):
        """Get all poles of the B-Spline curve."""

    def getPolesAndWeights(self):
        """Returns the table of poles and weights in homogeneous coordinates."""

    def getResolution(self, arg1: float, /):
        """Computes for this B-Spline curve the parametric tolerance (UTolerance)
        for a given 3D tolerance (Tolerance3D).
        If f(t) is the equation of this B-Spline curve, the parametric tolerance
        ensures that:
        |t1-t0| < UTolerance =""==> |f(t1)-f(t0)| < Tolerance3D"""

    def getWeight(self, arg1: int, /):
        """Get a weight of the B-Spline curve."""

    def getWeights(self):
        """Get all weights of the B-Spline curve."""

    def increaseDegree(self, arg1: int, /):
        """increase(Int=Degree)
        Increases the degree of this B-Spline curve to Degree.
        As a result, the poles, weights and multiplicities tables
        are modified; the knots table is not changed. Nothing is
        done if Degree is less than or equal to the current degree."""

    def increaseMultiplicity(self, int_start: int, int_end: int, int_mult: int = None, /):
        """
        				increaseMultiplicity(int index, int mult)
        				increaseMultiplicity(int start, int end, int mult)
        				Increases multiplicity of knots up to mult.

        				index: the index of a knot to modify (1-based)
        				start, end: index range of knots to modify.
        				If mult is lower or equal to the current multiplicity nothing is done. If mult is higher than the degree the degree is used.
        				"""

    def incrementMultiplicity(self, int_start: int, int_end: int, int_mult: int, /):
        """
        				incrementMultiplicity(int start, int end, int mult)
        				Raises multiplicity of knots by mult.

        				start, end: index range of knots to modify.
        				"""

    def insertKnot(self, u: float, mult: int = 1, tol: float = 0.0, /):
        """
        				insertKnot(u, mult = 1, tol = 0.0)
        				Inserts a knot value in the sequence of knots. If u is an existing knot the
        				multiplicity is increased by mult. """

    def insertKnots(self, list_of_floats: object, list_of_ints: object, tol: float = 0.0, bool_add: bool = True, /):
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
        				"""

    def interpolate(self, Points: object, PeriodicFlag: bool = None, Tolerance: float = None, InitialTangent: object = None, FinalTangent: object = None, Tangents: object = None, TangentFlags: object = None, Parameters: object = None):
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
        				"""

    def isClosed(self):
        """
        					Returns true if the distance between the start point and end point of
        					this B-Spline curve is less than or equal to gp::Resolution().
        				"""

    def isPeriodic(self):
        """Returns true if this BSpline curve is periodic."""

    def isRational(self):
        """
        					Returns true if this B-Spline curve is rational.
        					A B-Spline curve is rational if, at the time of construction,
        					the weight table has been initialized.
        				"""

    def join(self, arg1: Part.BSplineCurve2d, /):
        """
        					Build a new spline by joining this and a second spline.
        				"""

    def makeC1Continuous(self, arg1: float = None, /):
        """
        					makeC1Continuous(tol = 1e-6, ang_tol = 1e-7)
        					Reduces as far as possible the multiplicities of the knots of this BSpline
        					(keeping the geometry). It returns a new BSpline, which could still be C0.
        					tol is a geometrical tolerance.
        					The tol_ang is angular tolerance, in radians. It sets tolerable angle mismatch
        					of the tangents on the left and on the right to decide if the curve is G1 or
        					not at a given point.
        				"""

    def movePoint(self, U: float, P: object, Index1: int, Index2: int, /):
        """
        				movePoint(U, P, Index1, Index2)
        				Moves the point of parameter U of this B-Spline curve to P.
        Index1 and Index2 are the indexes in the table of poles of this B-Spline curve
        of the first and last poles designated to be moved.

        Returns: (FirstModifiedPole, LastModifiedPole). They are the indexes of the
        first and last poles which are effectively modified."""

    def removeKnot(self, Index: int, M: int, tol: float, /):
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
        				"""

    def segment(self, u1: float, u2: float, /):
        """
        					segment(u1,u2)
        					Modifies this B-Spline curve by segmenting it."""

    def setKnot(self, arg1: int, arg2: float, arg3: int = None, /):
        """Set a knot of the B-Spline curve."""

    def setKnots(self, arg1: object, /):
        """Set knots of the B-Spline curve."""

    def setNotPeriodic(self):
        """Changes this B-Spline curve into a non-periodic curve.
        If this curve is already non-periodic, it is not modified."""

    def setOrigin(self, arg1: int, /):
        """Assigns the knot of index Index in the knots table
        as the origin of this periodic B-Spline curve. As a consequence,
        the knots and poles tables are modified."""

    def setPeriodic(self):
        """Changes this B-Spline curve into a periodic curve."""

    def setPole(self, arg1: int, arg2: object, arg3: float = None, /):
        """Modifies this B-Spline curve by assigning P
        to the pole of index Index in the poles table."""

    def setWeight(self, arg1: int, arg2: float, /):
        """Set a weight of the B-Spline curve."""

    def toBezier(self):
        """
        					Build a list of Bezier splines.
        				"""

    def toBiArcs(self, tolerance: float, /):
        """
        					Build a list of arcs and lines to approximate the B-spline.
        					toBiArcs(tolerance) -> list.
        				"""


# BezierCurve2dPy.xml
class BezierCurve2d(Part.Curve2d):
    """
                    Describes a rational or non-rational Bezier curve in 2d space:
    				-- a non-rational Bezier curve is defined by a table of poles (also called control points)
    				-- a rational Bezier curve is defined by a table of poles with varying weights
    			"""

    @property
    def Degree(self) -> int:
        """Returns the polynomial degree of this Bezier curve,
        which is equal to the number of poles minus 1."""

    @property
    def EndPoint(self) -> object:
        """Returns the end point of this Bezier curve."""

    @property
    def MaxDegree(self) -> int:
        """Returns the value of the maximum polynomial degree of any
        Bezier curve curve. This value is 25."""

    @property
    def NbPoles(self) -> int:
        """Returns the number of poles of this Bezier curve.
        				"""

    @property
    def StartPoint(self) -> object:
        """Returns the start point of this Bezier curve."""

    def getPole(self, arg1: int, /):
        """Get a pole of the Bezier curve."""

    def getPoles(self):
        """Get all poles of the Bezier curve."""

    def getResolution(self, arg1: float, /):
        """Computes for this Bezier curve the parametric tolerance (UTolerance)
        for a given 3D tolerance (Tolerance3D).
        If f(t) is the equation of this Bezier curve, the parametric tolerance
        ensures that:
        |t1-t0| < UTolerance =""==> |f(t1)-f(t0)| < Tolerance3D"""

    def getWeight(self, arg1: int, /):
        """Get a weight of the Bezier curve."""

    def getWeights(self):
        """Get all weights of the Bezier curve."""

    def increase(self, Int: int, /):
        """increase(Int=Degree)
        Increases the degree of this Bezier curve to Degree.
        As a result, the poles and weights tables are modified."""

    def insertPoleAfter(self, arg1: int, arg2: object, arg3: float = None, /):
        """Inserts after the pole of index."""

    def insertPoleBefore(self, arg1: int, arg2: object, arg3: float = None, /):
        """Inserts before the pole of index."""

    def isClosed(self):
        """Returns true if the distance between the start point and end point of
        					this Bezier curve is less than or equal to gp::Resolution().
        				"""

    def isPeriodic(self):
        """Returns false."""

    def isRational(self):
        """Returns false if the weights of all the poles of this Bezier curve are equal."""

    def removePole(self, arg1: int, /):
        """Removes the pole of index Index from the table of poles of this Bezier curve.
        If this Bezier curve is rational, it can become non-rational."""

    def segment(self, arg1: float, arg2: float, /):
        """Modifies this Bezier curve by segmenting it."""

    def setPole(self, arg1: int, arg2: object, arg3: float = None, /):
        """Set a pole of the Bezier curve."""

    def setPoles(self, arg1: object, /):
        """Set the poles of the Bezier curve."""

    def setWeight(self, arg1: int, arg2: float, /):
        """Set a weight of the Bezier curve."""


# OffsetCurve2dPy.xml
class OffsetCurve2d(Part.Curve2d):
    def __init__(self, arg1: Part.Curve2d, arg2: float, /): ...

    @property
    def BasisCurve(self) -> object:
        """
        					Sets or gets the basic curve.
        				"""

    @property
    def OffsetValue(self) -> float:
        """
        					Sets or gets the offset value to offset the underlying curve.
        				"""


# Parabola2dPy.xml
class Parabola2d(Part.Conic2d):
    """Describes a parabola in 2D space"""

    def __init__(self):
        """Describes a parabola in 2D space"""

    @property
    def Focal(self) -> float:
        """The focal distance is the distance between
        the apex and the focus of the parabola."""

    @Focal.setter
    def Focal(self, value: float): ...

    @property
    def Focus(self) -> object:
        """The focus is on the positive side of the
        'X Axis' of the local coordinate system of the parabola."""

    @property
    def Parameter(self) -> float:
        """Compute the parameter of this parabola
        which is the distance between its focus
        and its directrix. This distance is twice the focal length.
        				"""


# Line2dPy.xml
class Line2d(Part.Curve2d):
    """Describes an infinite line in 2D space
    To create a line there are several ways:
    Part.Geom2d.Line2d()
        Creates a default line

    Part.Geom2d.Line2d(Line)
        Creates a copy of the given line

    Part.Geom2d.Line2d(Point,Dir)
        Creates a line that goes through two given points"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Line: Part.Line2d, /): ...

    @typing.overload
    def __init__(self, Point: object, Dir: object, /):
        """Describes an infinite line in 2D space
        To create a line there are several ways:
        Part.Geom2d.Line2d()
            Creates a default line

        Part.Geom2d.Line2d(Line)
            Creates a copy of the given line

        Part.Geom2d.Line2d(Point,Dir)
            Creates a line that goes through two given points"""

    @property
    def Direction(self) -> object:
        """Returns the direction of this line."""

    @Direction.setter
    def Direction(self, value: object): ...

    @property
    def Location(self) -> object:
        """Returns the location of this line."""

    @Location.setter
    def Location(self, value: object): ...


# MakePrismPy.xml
class MakePrism(FreeCAD.PyObjectBase):
    """Describes functions to build prism features."""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Sbase: Part.TopoShape, Pbase: Part.TopoShape, Skface: Part.TopoShape, Direction: FreeCAD.Vector, Fuse: int, Modify: bool):
        """Describes functions to build prism features."""

    def add(self, Edge: Part.TopoShape, Face: Part.TopoShape):
        """
        Indicates that the edge will slide on the face.
        Raises ConstructionError if the  face does not belong to the
        basis shape, or the edge to the prismed shape.
                    """

    def barycCurve(self):
        """
        Generates a curve along the center of mass of the primitive.
                    """

    def curves(self):
        """
        Returns the list of curves S parallel to the axis of the prism.
                    """

    def init(self, Sbase: Part.TopoShape, Pbase: Part.TopoShape, Skface: Part.TopoShape, Direction: FreeCAD.Vector, Fuse: int, Modify: bool):
        """
        Initializes this algorithm for building prisms along surfaces.
        A face Pbase is selected in the shape Sbase
        to serve as the basis for the prism. The orientation
        of the prism will be defined by the vector Direction.

        Fuse offers a choice between:
        -   removing matter with a Boolean cut using the setting 0
        -   adding matter with Boolean fusion using the setting 1.
        The sketch face Skface serves to determine
        the type of operation. If it is inside the basis
        shape, a local operation such as glueing can be performed.
                    """

    @typing.overload
    def perform(self, From: Part.TopoShape, Until: Part.TopoShape): ...

    @typing.overload
    def perform(self, Until: Part.TopoShape): ...

    @typing.overload
    def perform(self, Length: float): ...

    def performFromEnd(self, arg1: Part.TopoShape, /):
        """
        Realizes a semi-infinite prism, limited by the face Funtil.
                    """

    def performThruAll(self):
        """
        Builds an infinite prism. The infinite descendants will not be kept in the result.
                    """

    def performUntilEnd(self):
        """
        Realizes a semi-infinite prism, limited by the
        position of the prism base. All other faces extend infinitely.
                    """

    def performUntilHeight(self, arg1: Part.TopoShape, arg2: float, /):
        """
        Assigns both a limiting shape, Until from TopoDS_Shape
        and a height, Length at which to stop generation of the prism feature.
                    """

    def shape(self):
        """Returns a shape built by the shape construction algorithm."""


# UnifySameDomainPy.xml
class UnifySameDomain(FreeCAD.PyObjectBase):
    """This tool tries to unify faces and edges of the shape which lie on the same geometry."""

    def __init__(self, Shape: Part.TopoShape, UnifyEdges: bool = None, UnifyFaces: bool = None, ConcatBSplines: bool = None):
        """This tool tries to unify faces and edges of the shape which lie on the same geometry."""

    def allowInternalEdges(self, arg1: bool, /):
        """Sets the flag defining whether it is allowed to create
        internal edges inside merged faces in the case of non-manifold
        topology. Without this flag merging through multi connected edge
        is forbidden. Default value is false."""

    def build(self):
        """Performs unification and builds the resulting shape"""

    def initialize(self, Shape: Part.TopoShape, UnifyEdges: bool = None, UnifyFaces: bool = None, ConcatBSplines: bool = None):
        """Initializes with a shape and necessary flags"""

    def keepShape(self, arg1: Part.TopoShape, /):
        """Sets the shape for avoid merging of the faces/edges."""

    def keepShapes(self, arg1: object, /):
        """Sets the map of shapes for avoid merging of the faces/edges."""

    def setAngularTolerance(self, arg1: float, /):
        """Sets the angular tolerance"""

    def setLinearTolerance(self, arg1: float, /):
        """Sets the linear tolerance"""

    def setSafeInputMode(self, arg1: bool, /):
        """Sets the flag defining the behavior of the algorithm regarding
        modification of input shape.
        If this flag is equal to True then the input (original) shape can't be
        modified during modification process. Default value is true."""

    def shape(self):
        """Gives the resulting shape"""


# AppPartPy.cpp
def open(arg1: str, /):
    """open(string) -- Create a new document and load the file into the document."""


def insert(arg1: str, arg2: str, /):
    """insert(string,string) -- Insert the file into the given document."""


def export(arg1: object, arg2: str, /):
    """export(list,string) -- Export a list of objects into a single file."""


def read(arg1: str, /):
    """read(string) -- Load the file and return the shape."""


def show(arg1: Part.TopoShape, arg2: str = None, /):
    """show(shape,[string]) -- Add the shape to the active document or create one if no document exists."""


def getFacets(arg1: object, /):
    """getFacets(shape): simplified mesh generation"""


def makeCompound(arg1: object, /):
    """makeCompound(list) -- Create a compound out of a list of shapes."""


def makeShell(arg1: object, /):
    """makeShell(list) -- Create a shell out of a list of faces."""


def makeFace(arg1: object, arg2: str, /):
    """makeFace(list_of_shapes_or_compound, maker_class_name) -- Create a face (faces) using facemaker class.
    maker_class_name is a string like 'Part::FaceMakerSimple'."""


def makeFilledFace(arg1: object, arg2: Part.TopoShape = None, /):
    """makeFilledFace(list) -- Create a face out of a list of edges."""


def makeSolid(arg1: Part.TopoShape, /):
    """makeSolid(shape): Create a solid out of shells of shape. If shape is a compsolid, the overall volume solid is created."""


def makePlane(arg1: float, arg2: float, arg3: FreeCAD.Vector = None, arg4: FreeCAD.Vector = None, arg5: FreeCAD.Vector = None, /):
    """makePlane(length,width,[pnt,dirZ,dirX]) -- Make a plane
    By default pnt=Vector(0,0,0) and dirZ=Vector(0,0,1), dirX is ignored in this case"""


def makeBox(arg1: float, arg2: float, arg3: float, arg4: FreeCAD.Vector = None, arg5: FreeCAD.Vector = None, /):
    """makeBox(length,width,height,[pnt,dir]) -- Make a box located
    in pnt with the dimensions (length,width,height)
    By default pnt=Vector(0,0,0) and dir=Vector(0,0,1)"""


def makeWedge(arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: FreeCAD.Vector = None, arg12: FreeCAD.Vector = None, /):
    """makeWedge(xmin, ymin, zmin, z2min, x2min,
    xmax, ymax, zmax, z2max, x2max,[pnt,dir])
     -- Make a wedge located in pnt
    By default pnt=Vector(0,0,0) and dir=Vector(0,0,1)"""


def makeLine(arg1: object, arg2: object, /):
    """makeLine(startpnt,endpnt) -- Make a line between two points

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


def makePolygon(arg1: object, arg2: bool = None, /):
    """makePolygon(pntslist) -- Make a polygon from a list of points

    Args:
        pntslist (list(Vector)): list of Vectors representing the 
            points of the polygon.

    Returns:
        Wire: Part.Wire object. If the last point in the list is 
            not the same as the first point, the Wire will not be 
            closed and cannot be used to create a face.
    """


def makeCircle(arg1: float, arg2: FreeCAD.Vector = None, arg3: FreeCAD.Vector = None, arg4: float = None, arg5: float = None, /):
    """makeCircle(radius,[pnt,dir,angle1,angle2]) -- Make a circle with a given radius
    By default pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=0 and angle2=360"""


def makeSphere(arg1: float, arg2: FreeCAD.Vector = None, arg3: FreeCAD.Vector = None, arg4: float = None, arg5: float = None, arg6: float = None, /):
    """makeSphere(radius,[pnt, dir, angle1,angle2,angle3]) -- Make a sphere with a given radius
    By default pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=0, angle2=90 and angle3=360"""


def makeCylinder(arg1: float, arg2: float, arg3: FreeCAD.Vector = None, arg4: FreeCAD.Vector = None, arg5: float = None, /):
    """makeCylinder(radius,height,[pnt,dir,angle]) -- Make a cylinder with a given radius and height
    By default pnt=Vector(0,0,0),dir=Vector(0,0,1) and angle=360"""


def makeCone(arg1: float, arg2: float, arg3: float, arg4: FreeCAD.Vector = None, arg5: FreeCAD.Vector = None, arg6: float = None, /):
    """makeCone(radius1,radius2,height,[pnt,dir,angle]) -- Make a cone with given radii and height
    By default pnt=Vector(0,0,0), dir=Vector(0,0,1) and angle=360"""


def makeTorus(arg1: float, arg2: float, arg3: FreeCAD.Vector = None, arg4: FreeCAD.Vector = None, arg5: float = None, arg6: float = None, arg7: float = None, /):
    """makeTorus(radius1,radius2,[pnt,dir,angle1,angle2,angle]) -- Make a torus with a given radii and angles
    By default pnt=Vector(0,0,0),dir=Vector(0,0,1),angle1=0,angle1=360 and angle=360"""


def makeHelix(arg1: float, arg2: float, arg3: float, arg4: float = None, arg5: bool = None, arg6: bool = None, /):
    """makeHelix(pitch,height,radius,[angle]) -- Make a helix with a given pitch, height and radius
    By default a cylindrical surface is used to create the helix. If the fourth parameter is set
    (the apex given in degree) a conical surface is used instead"""


def makeLongHelix(arg1: float, arg2: float, arg3: float, arg4: float = None, arg5: bool = None, /):
    """makeLongHelix(pitch,height,radius,[angle],[hand]) -- Make a (multi-edge) helix with a given pitch, height and radius
    By default a cylindrical surface is used to create the helix. If the fourth parameter is set
    (the apex given in degree) a conical surface is used instead."""


def makeThread(arg1: float, arg2: float, arg3: float, arg4: float, /):
    """makeThread(pitch,depth,height,radius) -- Make a thread with a given pitch, depth, height and radius"""


@typing.overload
def makeRevolution(arg1: Part.Geometry, arg2: float = None, arg3: float = None, arg4: float = None, arg5: FreeCAD.Vector = None, arg6: FreeCAD.Vector = None, arg7: type = None, /): ...


@typing.overload
def makeRevolution(arg1: Part.TopoShape, arg2: float = None, arg3: float = None, arg4: float = None, arg5: FreeCAD.Vector = None, arg6: FreeCAD.Vector = None, arg7: type = None, /):
    """makeRevolution(Curve or Edge,[vmin,vmax,angle,pnt,dir,shapetype]) -- Make a revolved shape
    by rotating the curve or a portion of it around an axis given by (pnt,dir).
    By default vmin/vmax=bounds of the curve, angle=360, pnt=Vector(0,0,0),
    dir=Vector(0,0,1) and shapetype=Part.Solid"""


def makeRuledSurface(arg1: Part.TopoShape, arg2: Part.TopoShape, /):
    """makeRuledSurface(Edge|Wire,Edge|Wire) -- Make a ruled surface
    Create a ruled surface out of two edges or wires. If wires are used thenthese must have the same number of edges."""


def makeShellFromWires(arg1: object, /):
    """makeShellFromWires(Wires) -- Make a shell from wires.
    The wires must have the same number of edges."""


def makeTube(arg1: Part.TopoShape, arg2: float, arg3: str = None, arg4: int = None, arg5: int = None, /):
    """makeTube(edge,radius,[continuity,max degree,max segments]) -- Create a tube.
    continuity is a string which must be 'C0','C1','C2','C3','CN','G1' or 'G1',"""


def makeSweepSurface(arg1: Part.TopoShape, arg2: Part.TopoShape, arg3: float = None, arg4: int = None, /):
    """makeSweepSurface(edge(path),edge(profile),[float]) -- Create a profile along a path."""


@typing.overload
def makeLoft(arg1: object, /): ...


@typing.overload
def makeLoft(arg1: object, arg2: bool = None, arg3: bool = None, arg4: bool = None, arg5: int = None, /):
    """makeLoft(list of wires,[solid=False,ruled=False,closed=False,maxDegree=5]) -- Create a loft shape."""


@typing.overload
def makeWireString(arg1: object, arg2: str, arg3: str, arg4: float, arg5: float = None, /): ...


@typing.overload
def makeWireString(arg1: object, arg2: str, arg3: float, arg4: float = None, /):
    """makeWireString(string,fontdir,fontfile,height,[track]) -- Make list of wires in the form of a string's characters."""


def makeSplitShape(arg1: Part.TopoShape, arg2: object, arg3: bool = None, /):
    """makeSplitShape(shape, list of shape pairs,[check Interior=True]) -> two lists of shapes.
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


def exportUnits(arg1: str = None, /):
    """exportUnits([string=MM|M|INCH|FT|MI|KM|MIL|UM|CM|UIN]) -- Set units for exporting STEP/IGES files and returns the units."""


@typing.overload
def setStaticValue(arg1: str, arg2: str, /): ...


@typing.overload
def setStaticValue(arg1: str, arg2: object, /):
    """setStaticValue(string,string|int|float) -- Set a name to a value The value can be a string, int or float."""


def cast_to_shape(arg1: Part.TopoShape, /):
    """cast_to_shape(shape) -- Cast to the actual shape type"""


def getSortedClusters(arg1: object, /):
    """getSortedClusters(list of edges) -- Helper method to sort and cluster a variety of edges"""


def __sortEdges__(arg1: object, /):
    """__sortEdges__(list of edges) -- list of edges
    Helper method to sort an unsorted list of edges so that afterwards
    the start and end vertex of two consecutive edges are geometrically coincident.
    It returns a single list of edges and the algorithm stops after the first set of
    connected edges which means that the output list can be smaller than the input list.
    The sorted list can be used to create a Wire."""


def sortEdges(arg1: object, /):
    """sortEdges(list of edges) -- list of lists of edges
    It does basically the same as __sortEdges__ but sorts all input edges and thus returns
    a list of lists of edges"""


def __toPythonOCC__(arg1: Part.TopoShape, /):
    """__toPythonOCC__(shape) -- Helper method to convert an internal shape to pythonocc shape"""


def __fromPythonOCC__(arg1: object, /):
    """__fromPythonOCC__(occ) -- Helper method to convert a pythonocc shape to an internal shape"""


def clearShapeCache():
    """clearShapeCache() -- Clears internal shape cache"""


def splitSubname(arg1: str, /):
    """splitSubname(subname) -> list(sub,mapped,subElement)
    Split the given subname into a list

    sub: subname without any sub-element reference
    mapped: mapped element name, or '' if none
    subElement: old style element name, or '' if none"""


def joinSubname(arg1: str, arg2: str, arg3: str, /):
    """joinSubname(sub,mapped,subElement) -> subname
    """


def getShape(obj: FreeCAD.DocumentObject, subname: str = None, mat: FreeCAD.Matrix = None, needSubElement: object = None, transform: object = None, retType: int = None, noElementMap: object = None, refine: object = None):
    """getShape(obj,subname=None,mat=None,needSubElement=False,transform=True,retType=0):
    Obtain the the TopoShape of a given object with SubName reference

    * obj: the input object
    * subname: dot separated sub-object reference
    * mat: the current transformation matrix
    * needSubElement: if False, ignore the sub-element (e.g. Face1, Edge1) reference in 'subname'
    * transform: if False, then skip obj's transformation. Use this if mat already include obj's
                 transformation matrix
    * retType: 0: return TopoShape,
               1: return (shape,subObj,mat), where subObj is the object referenced in 'subname',
                  and 'mat' is the accumulated transformation matrix of that sub-object.
               2: same as 1, but make sure 'subObj' is resolved if it is a link.
    * refine: refine the returned shape"""


# AttacherTexts.cpp
def getModeStrings(arg1: str, arg2: int, /):
    """getModeStrings(attacher_type, mode_index) - gets mode user-friendly name and brief description."""


def getRefTypeUserFriendlyName(arg1: int, /):
    """getRefTypeUserFriendlyName(type_index) - gets user-friendly name of AttachEngine's shape type."""
