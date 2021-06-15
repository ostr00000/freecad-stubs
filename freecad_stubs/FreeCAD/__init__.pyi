import typing

import FreeCAD
import FreeCAD.Console
import FreeCAD.Translate as Qt
import FreeCAD.UnitsApiPy as Units
import FreeCADGui


class PyObjectBase(object): ...


# VectorPy.xml
class Vector(FreeCAD.PyObjectBase):
    """This class represents a 3D float vector"""

    @typing.overload
    def __init__(self, arg1: float = None, arg2: float = None, arg3: float = None, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, arg1: object, /):
        """This class represents a 3D float vector"""

    @property
    def Length(self) -> float:
        """Length([Float]) -> Float
        						  gets or sets the length of this vector
        				"""

    @Length.setter
    def Length(self, value: float): ...

    @property
    def x(self) -> float:
        """x([Float]) -> Float
        						  gets or sets the X component of this vector
        				"""

    @x.setter
    def x(self, value: float): ...

    @property
    def y(self) -> float:
        """y([Float]) -> Float
        						  gets or sets the Y component of this vector
        				"""

    @y.setter
    def y(self, value: float): ...

    @property
    def z(self) -> float:
        """z([Float]) -> Float
        						  gets or sets the Z component of this vector
        				"""

    @z.setter
    def z(self, value: float): ...

    def __reduce__(self):
        """__reduce__()
                              Serialization of Vector objects
                    """

    def add(self, Vector: FreeCAD.Vector, /):
        """add(Vector)
        					      returns the sum of this and another vector
        				"""

    def cross(self, Vector: FreeCAD.Vector, /):
        """cross(Vector)
        					      returns the cross product between this and another vector
        				"""

    def distanceToLine(self, Vector: object, Vector2: object, /):
        """distanceToLine(Vector,Vector)
        						  returns the distance between this vector and a line defined by
        						  a base point and a direction
        				"""

    def distanceToLineSegment(self, Vector: object, Vector2: object, /):
        """distanceToLineSegment(Vector,Vector)
        						  returns the distance between this vector and a line segment defined by
        						  a base point and a direction
        				"""

    def distanceToPlane(self, Vector: object, Vector2: object, /):
        """distanceToPlane(Vector,Vector)
        						  returns the distance between this vector and a plane defined by
        						  a base point and a normal
        				"""

    def distanceToPoint(self, Vector: FreeCAD.Vector, /):
        """
        					distanceToPoint(Vector)
        					returns the distance to another point
        				"""

    def dot(self, Vector: FreeCAD.Vector, /):
        """dot(Vector)
        						  returns the dot product of the this vector with another one
        				"""

    def getAngle(self, Vector: FreeCAD.Vector, /):
        """getAngle(Vector)
        					      returns the angle in radians between this and another vector
        				"""

    def isEqual(self, Vector: FreeCAD.Vector, tolerance: float, /):
        """isEqual(Vector, tolerance) -> Boolean
                                  If the distance to the given point is less or equal to the tolerance
                                  bith points are considered equal.
                        """

    def isOnLineSegment(self, Vector: object, Vector2: object, /):
        """isOnLineSegment(Vector, Vector)
        					      checks if Vector is on a line segment
        				"""

    def multiply(self, Float: float, /):
        """multiply(Float)
        					      multiplies (scales) this vector by a single factor
        				"""

    def negative(self):
        """negative()
        					      returns the negative (opposite) of this vector
        				"""

    def normalize(self):
        """normalize()
        						  normalizes the vector to the length of 1.0
        				"""

    def projectToLine(self, Vector_pnt: object, Vector_vec: object, /):
        """projectToLine(Vector pnt,Vector vec)
        						  Projects the point 'pnt' on a line that goes through the origin with the direction vector 'vec'.
        						  The result is the vector from point 'pnt' to the projected point.
        						  NOTE: The result does not depend on the vector instance 'self'.
        						  NOTE: This method modifies the vector instance 'self'.
        				"""

    def projectToPlane(self, Vector: object, Vector2: object, /):
        """projectToPlane(Vector,Vector)
        						  projects the vector on a plane defined by a base point and a normal
        				"""

    def scale(self, Float: float, Float2: float, Float3: float, /):
        """scale(Float,Float,Float)
        					      scales (multiplies) this vector by a factor
        			    """

    def sub(self, Vector: FreeCAD.Vector, /):
        """sub(Vector)
        					      returns the difference of this and another vector
        				"""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Vector: ...

    def __sub__(self, other) -> Vector: ...

    def __mul__(self, other) -> Vector: ...

    def __floordiv__(self, other): ...

    def __divmod__(self, other): ...

    def __pow__(self, power, modulo=None): ...

    def __neg__(self) -> Vector: ...

    def __pos__(self) -> Vector: ...

    def __abs__(self) -> Vector: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rshift__(self, other): ...

    def __and__(self, other): ...

    def __xor__(self, other): ...

    def __or__(self, other): ...

    def __int__(self): ...

    def __float__(self): ...


# RotationPy.xml
class Rotation(FreeCAD.PyObjectBase):
    """
    				A Rotation using a quaternion.
    				The Rotation object can be created by:
    				-- an empty parameter list
    				-- a Rotation object
    				-- a Vector (axis) and a float (angle)
    				-- two Vectors (rotation from/to vector)
    				-- three floats (Euler angles) as yaw-pitch-roll in XY'Z'' convention
    				-- four floats (Quaternion) where the quaternion is specified as:
    				   q=xi+yj+zk+w, i.e. the last parameter is the real part
    				-- three vectors that define rotated axes directions + an optional
    				   3-characher string of capital letters 'X', 'Y', 'Z' that sets the
    				   order of importance of the axes (e.g., 'ZXY' means z direction is
    				   followed strictly, x is used but corrected if necessary, y is ignored).
    			"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Rotation, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: float, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Matrix, /): ...

    @typing.overload
    def __init__(self, arg1: float, arg2: float, arg3: float, arg4: float, /): ...

    @typing.overload
    def __init__(self, arg1: float, arg2: float, arg3: float, /): ...

    @typing.overload
    def __init__(self, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float, /): ...

    @typing.overload
    def __init__(self, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, arg3: FreeCAD.Vector, arg4: str = None, /):
        """
        				A Rotation using a quaternion.
        				The Rotation object can be created by:
        				-- an empty parameter list
        				-- a Rotation object
        				-- a Vector (axis) and a float (angle)
        				-- two Vectors (rotation from/to vector)
        				-- three floats (Euler angles) as yaw-pitch-roll in XY'Z'' convention
        				-- four floats (Quaternion) where the quaternion is specified as:
        				   q=xi+yj+zk+w, i.e. the last parameter is the real part
        				-- three vectors that define rotated axes directions + an optional
        				   3-characher string of capital letters 'X', 'Y', 'Z' that sets the
        				   order of importance of the axes (e.g., 'ZXY' means z direction is
        				   followed strictly, x is used but corrected if necessary, y is ignored).
        			"""

    @property
    def Angle(self) -> float:
        """The rotation angle of the quaternion"""

    @Angle.setter
    def Angle(self, value: float): ...

    @property
    def Axis(self) -> object:
        """The rotation axis of the quaternion"""

    @Axis.setter
    def Axis(self, value: object): ...

    @property
    def Q(self) -> tuple:
        """The rotation elements (as quaternion)"""

    @Q.setter
    def Q(self, value: tuple): ...

    @property
    def RawAxis(self) -> object:
        """The rotation axis without normalization"""

    def invert(self):
        """
                            invert() -> None
                            Sets the rotation to its inverse
        				"""

    def inverted(self):
        """
                            inverted() -> Rotation
                            Returns the inverse of the rotation
                        """

    def isIdentity(self):
        """
                            isIdentity() -> Bool
                            returns True if the rotation equals the unity matrix
                        """

    def isNull(self):
        """
        					isNull() -> Bool
                            returns True if all Q values are zero
        				"""

    def isSame(self, Rotation: FreeCAD.Rotation, tolerance: float = 0, /):
        """
                            isSame(Rotation, [tolerance=0])
                            Checks if the two quaternions perform the same rotation.
                            Optionally, a tolerance value greater than zero can be passed.
                        """

    def multVec(self, Vector: FreeCAD.Vector, /):
        """
        					multVec(Vector) -> Vector
        					Compute the transformed vector using the rotation
        				"""

    def multiply(self, Rotation: FreeCAD.Rotation, /):
        """
        					multiply(Rotation)
        					Multiply this quaternion with another quaternion
        				"""

    def slerp(self, Rotation: FreeCAD.Rotation, Float: float, /):
        """
        					slerp(Rotation, Float) -> Rotation
        					Spherical linear interpolation of this and a given rotation. The float must be in the range of 0 and 1
        				"""

    def toEuler(self):
        """
        					toEuler(Vector) -> list
        					Get the Euler angles of this rotation
        					as yaw-pitch-roll in XY'Z'' convention
        				"""

    def toMatrix(self):
        """
        					toMatrix()
        					convert the rotation to a matrix representation
        				"""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Rotation: ...

    def __sub__(self, other) -> Rotation: ...

    def __mul__(self, other) -> Rotation: ...

    def __floordiv__(self, other): ...

    def __divmod__(self, other): ...

    def __pow__(self, power, modulo=None): ...

    def __neg__(self) -> Rotation: ...

    def __pos__(self) -> Rotation: ...

    def __abs__(self) -> Rotation: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rshift__(self, other): ...

    def __and__(self, other): ...

    def __xor__(self, other): ...

    def __or__(self, other): ...

    def __int__(self): ...

    def __float__(self): ...


# PersistencePy.xml
class Persistence(FreeCAD.BaseClass):
    """This is a persistence class"""

    @property
    def Content(self) -> str:
        """Content of the object in XML representation"""

    @property
    def MemSize(self) -> int:
        """Memory size of the object in byte"""

    @typing.overload
    def dumpContent(self, Compression: int = None): ...

    @typing.overload
    def dumpContent(self, Compression: int = 1-9):
        """Dumps the content of the object, both the XML representation as well as the additional datafiles  
        required, into a byte representation. It will be returned as byte array.
        dumpContent() -- returns a byte array with full content
        dumpContent(Compression=1-9) -- Sets the data compression from 0 (no) to 9 (max)
                        """

    def restoreContent(self, buffer: object, /):
        """Restore the content of the object from a byte representation as stored by \"dumpContent\".
        It could be restored from any python object implementing the buffer protocol.
        restoreContent(buffer) -- restores from the given byte array
                        """


# BoundBoxPy.xml
class BoundBox(FreeCAD.PyObjectBase):
    """Bound box class
    A bounding box is an orthographic cube which is a way to describe outer boundaries.
    You get a bounding box from a lot of 3D types. It is often used to check if a 3D
    entity lies in the range of another object. Checking for bounding interference first
    can save a lot of computing time!

    Constructor:
    App.BoundBox([Xmin,Ymin,Zmin,Xmax,Ymax,Zmax])
    App.BoundBox(Tuple, Tuple)
    App.BoundBox(Vector, Vector)
    App.BoundBox(BoundBox)
    	  """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: float, arg2: float = None, arg3: float = None, arg4: float = None, arg5: float = None, arg6: float = None, /): ...

    @typing.overload
    def __init__(self, arg1: tuple, arg2: tuple, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.BoundBox, /):
        """Bound box class
        A bounding box is an orthographic cube which is a way to describe outer boundaries.
        You get a bounding box from a lot of 3D types. It is often used to check if a 3D
        entity lies in the range of another object. Checking for bounding interference first
        can save a lot of computing time!

        Constructor:
        App.BoundBox([Xmin,Ymin,Zmin,Xmax,Ymax,Zmax])
        App.BoundBox(Tuple, Tuple)
        App.BoundBox(Vector, Vector)
        App.BoundBox(BoundBox)
        	  """

    @property
    def Center(self) -> object:
        """Center point of the bounding box"""

    @property
    def DiagonalLength(self) -> float:
        """Diagonal length of the BoundBox"""

    @property
    def XLength(self) -> float:
        """Length of the BoundBox in x direction"""

    @property
    def XMax(self) -> float:
        """The maximum x boundary position"""

    @XMax.setter
    def XMax(self, value: float): ...

    @property
    def XMin(self) -> float:
        """The minimum x boundary position"""

    @XMin.setter
    def XMin(self, value: float): ...

    @property
    def YLength(self) -> float:
        """Length of the BoundBox in y direction"""

    @property
    def YMax(self) -> float:
        """The maximum y boundary position"""

    @YMax.setter
    def YMax(self, value: float): ...

    @property
    def YMin(self) -> float:
        """The minimum y boundary position"""

    @YMin.setter
    def YMin(self, value: float): ...

    @property
    def ZLength(self) -> float:
        """Length of the BoundBox in z direction"""

    @property
    def ZMax(self) -> float:
        """The maximum z boundary position"""

    @ZMax.setter
    def ZMax(self, value: float): ...

    @property
    def ZMin(self) -> float:
        """The minimum z boundary position"""

    @ZMin.setter
    def ZMin(self, value: float): ...

    @typing.overload
    def add(self, BoundBox: tuple, /): ...

    @typing.overload
    def add(self, BoundBox: FreeCAD.Vector, /): ...

    @typing.overload
    def add(self, BoundBox: FreeCAD.BoundBox, /):
        """method add(BoundBox)
        Add (enlarge) the given BoundBox"""

    @typing.overload
    def closestPoint(self, Vector: tuple, /): ...

    @typing.overload
    def closestPoint(self, Vector: FreeCAD.Vector, /):
        """method closestPoint(Vector)
        Get the closest point of the bounding box to the given point
                """

    def enlarge(self, Float: float, /):
        """method enlarge(Float)
        Enlarge the BoundBox by the given value in each direction.
        A negative value shrinks the box."""

    def getEdge(self, Int: int, /):
        """method getEdge(Int)
        Get the edge points of the given index. The index must be in the range of [0,11]
                """

    def getIntersectionPoint(self, Vector_Base: FreeCAD.Vector, Vector_Dir: FreeCAD.Vector, float_epsilon: float = 0.0001, /):
        """method Vector getIntersectionPoint(Vector Base, Vector Dir, [float epsilon=0.0001])
        Calculate the intersection point of a line with the BoundBox
        The Base point must lie inside the bounding box, if not an
        exception is thrown.
        			  """

    def getPoint(self, Int: int, /):
        """method getPoint(Int)
        Get the point of the given index. The index must be in the range of [0,7]
                """

    def intersect(self, BoundBox_Vector_Base: FreeCAD.Vector, Vector_Dir: FreeCAD.Vector, /):
        """method intersect(BoundBox|Vector Base, Vector Dir)
        Checks if the given object intersects with the BoundBox. That can be:
        - Another BoundBox
        - A line, specified by Base and Dir
        		"""

    def intersected(self, BoundBox: FreeCAD.BoundBox, /):
        """method intersected(BoundBox)
        Returns the intersection of this and the given bounding box.
        		"""

    def isCutPlane(self, Vector_Base: FreeCAD.Vector, Vector_Normal: FreeCAD.Vector, /):
        """method bool isCutPlane(Vector Base, Vector Normal)
        Check if the plane specified by Base and Normal intersects (cuts) the BoundBox"""

    @typing.overload
    def isInside(self, Vector_Base_BoundBox_box: tuple, /): ...

    @typing.overload
    def isInside(self, Vector_Base_BoundBox_box: FreeCAD.Vector, /): ...

    @typing.overload
    def isInside(self, Vector_Base_BoundBox_box: FreeCAD.BoundBox, /):
        """
        					method bool isInside(Vector Base|BoundBox box)
        Check if the point or bounding box is inside this bounding box
        				"""

    def isValid(self):
        """method isValid()
        Checks if the bounding box is valid"""

    @typing.overload
    def move(self, Vector: tuple, /): ...

    @typing.overload
    def move(self, Vector: FreeCAD.Vector, /):
        """ method move(Vector)
        Move the BoundBox by the given vector
        			  """

    def scale(self, x: float, y: float, z: float, /):
        """ method scale(x,y,z)
        Scale the BoundBox by the given values in x, y and z
        			  """

    def setVoid(self):
        """method setVoid()
        Invalidate the bounding box"""

    def transformed(self, Matrix: FreeCAD.Matrix, /):
        """ method transformed(Matrix)
        Return a new bounding box with the transformed corner of this bounding box
        			  """

    def united(self, BoundBox: FreeCAD.BoundBox, /):
        """method united(BoundBox)
        Returns the union of this and the given bounding box.
        		"""


# PlacementPy.xml
class Placement(FreeCAD.PyObjectBase):
    """Placement
    A placement defines an orientation (rotation) and a position (base) in 3D space.
    It is used when no scaling or other distortion is needed.

    The following constructors are supported:
    Placement() -- empty constructor
    Placement(Placement) -- copy constructor
    Placement(Matrix) -- 4D matrix consisting of rotation and translation
    Placement(Base, Rotation) -- define position and rotation
    Placement(Base, Rotation,Center) -- define position and rotation with center
    Placement(Base, Axis, Angle) -- define position and rotation
    		"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Matrix, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Placement, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, arg3: float, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Rotation, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Rotation, arg3: FreeCAD.Vector, /):
        """Placement
        A placement defines an orientation (rotation) and a position (base) in 3D space.
        It is used when no scaling or other distortion is needed.

        The following constructors are supported:
        Placement() -- empty constructor
        Placement(Placement) -- copy constructor
        Placement(Matrix) -- 4D matrix consisting of rotation and translation
        Placement(Base, Rotation) -- define position and rotation
        Placement(Base, Rotation,Center) -- define position and rotation with center
        Placement(Base, Axis, Angle) -- define position and rotation
        		"""

    @property
    def Base(self) -> object:
        """Vector to the Base Position of the Placement"""

    @Base.setter
    def Base(self, value: object): ...

    @property
    def Matrix(self) -> object:
        """Set/get matrix representation of this placement"""

    @Matrix.setter
    def Matrix(self, value: object): ...

    @property
    def Rotation(self) -> object:
        """Orientation of the placement expressed as rotation"""

    @Rotation.setter
    def Rotation(self, value: object): ...

    def copy(self):
        """
                            copy()
                            Returns a copy of this Placement
                        """

    def inverse(self):
        """
        					inverse() -> Placement
        					compute the inverse placement
        				"""

    def isIdentity(self):
        """
                            isIdentity() -> Bool
        					returns True if the placement has no displacement and no rotation
        				"""

    def move(self, Vector: FreeCAD.Vector, /):
        """
        					move(Vector) 
        					Move the placement along the vector
        				"""

    def multVec(self, arg1: FreeCAD.Vector, /):
        """
        					multVector(Vector) -> Vector
        					Compute the transformed vector using the placement
        				"""

    def multiply(self, Placement: FreeCAD.Placement, /):
        """
        					multiply(Placement)
        					Multiply this placement with another placement
        				"""

    def pow(self, t: float, shorten: bool = True, /):
        """
        					pow(t, shorten = true): raise this placement to real power using ScLERP interpolation.
                            If 'shorten' is true, ensures rotation quaternion is net positive, to make the path shorter.
                            Also available as ** operator.
        				"""

    def rotate(self, center: object, axis: object, degree: float, /):
        """
                        rotate(center,axis,degree) - rotate the current placement around center and axis with degree
                        This method is compatible with TopoShape.rotate()
                    """

    def sclerp(self, placement2: FreeCAD.Placement, t: float, shorten: bool = True, /):
        """
                            sclerp(placement2, t, shorten = True): interpolate between self and placement2.
                            Interpolation is a continuous motion along a helical path, made of equal transforms if discretized.
                            t = 0.0 - return self. t = 1.0 - return placement2. t can also be outside of 0..1 range, for extrapolation.
                            If quaternions of rotations of the two placements differ in sign, the interpolation will 
                             take a long path. If 'shorten' is true, the signs are harmonized before interpolation, and the 
                             interpolation takes the shorter path.
        				"""

    def slerp(self, arg1: FreeCAD.Placement, arg2: float, /):
        """
        					slerp(placement2, t, shorten = True): interpolate between self and placement2.
                            This function performs independent interpolation of rotation and movement.
                            Result of such interpolation might be not what application expects, thus this
                            tool might be considered for simple cases or for interpolating between small intervals.
                    
                            For more complex cases you better use the advanced sclerp() function.
        				"""

    def toMatrix(self):
        """
        					toMatrix()
        					convert the placement to a matrix representation
        				"""

    @typing.overload
    def translate(self, Vector): ...

    @typing.overload
    def translate(self, arg):
        """
        					translate(Vector) 
        					alias to move(), to be compatible with TopoShape.translate()
        				"""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Placement: ...

    def __sub__(self, other) -> Placement: ...

    def __mul__(self, other) -> Placement: ...

    def __floordiv__(self, other): ...

    def __divmod__(self, other): ...

    def __pow__(self, power, modulo=None): ...

    def __neg__(self) -> Placement: ...

    def __pos__(self) -> Placement: ...

    def __abs__(self) -> Placement: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rshift__(self, other): ...

    def __and__(self, other): ...

    def __xor__(self, other): ...

    def __or__(self, other): ...

    def __int__(self): ...

    def __float__(self): ...


# UnitPy.xml
class Unit(FreeCAD.PyObjectBase):
    """
     Unit
     defines a unit type, calculate and compare.

     The following constructors are supported:
     Unit()                        -- empty constructor
     Unit(i1,i2,i3,i4,i5,i6,i7,i8) -- unit signature
     Unit(Quantity)                -- copy unit from Quantity
     Unit(Unit)                    -- copy constructor
     Unit(string)                  -- parse the string for units
            """

    @typing.overload
    def __init__(self, arg1: FreeCAD.Quantity, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Unit, /): ...

    @typing.overload
    def __init__(self, arg1: str, /): ...

    @typing.overload
    def __init__(self, arg1: int = None, arg2: int = None, arg3: int = None, arg4: int = None, arg5: int = None, arg6: int = None, arg7: int = None, arg8: int = None, /):
        """
         Unit
         defines a unit type, calculate and compare.

         The following constructors are supported:
         Unit()                        -- empty constructor
         Unit(i1,i2,i3,i4,i5,i6,i7,i8) -- unit signature
         Unit(Quantity)                -- copy unit from Quantity
         Unit(Unit)                    -- copy constructor
         Unit(string)                  -- parse the string for units
                """

    @property
    def Signature(self) -> tuple:
        """Returns the signature."""

    @property
    def Type(self) -> str:
        """holds the unit type as a string, e.g. 'Area'."""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Unit: ...

    def __sub__(self, other) -> Unit: ...

    def __mul__(self, other) -> Unit: ...

    def __floordiv__(self, other): ...

    def __divmod__(self, other): ...

    def __pow__(self, power, modulo=None): ...

    def __neg__(self) -> Unit: ...

    def __pos__(self) -> Unit: ...

    def __abs__(self) -> Unit: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rshift__(self, other): ...

    def __and__(self, other): ...

    def __xor__(self, other): ...

    def __or__(self, other): ...

    def __int__(self): ...

    def __float__(self): ...


# QuantityPy.xml
class Quantity(FreeCAD.PyObjectBase):
    """Quantity
    defined by a value and a unit.

    The following constructors are supported:
    Quantity() -- empty constructor
    Quantity(Value) -- empty constructor
    Quantity(Value,Unit) -- empty constructor
    Quantity(Quantity) -- copy constructor
    Quantity(string) -- arbitrary mixture of numbers and chars defining a Quantity
    		"""

    @typing.overload
    def __init__(self, arg1: FreeCAD.Quantity, /): ...

    @typing.overload
    def __init__(self, arg1: float, arg2: FreeCAD.Unit, /): ...

    @typing.overload
    def __init__(self, arg1: float, arg2: FreeCAD.Quantity, /): ...

    @typing.overload
    def __init__(self, arg1: float = None, arg2: int = None, arg3: int = None, arg4: int = None, arg5: int = None, arg6: int = None, arg7: int = None, arg8: int = None, arg9: int = None, /): ...

    @typing.overload
    def __init__(self, arg1: str, /):
        """Quantity
        defined by a value and a unit.

        The following constructors are supported:
        Quantity() -- empty constructor
        Quantity(Value) -- empty constructor
        Quantity(Value,Unit) -- empty constructor
        Quantity(Quantity) -- copy constructor
        Quantity(string) -- arbitrary mixture of numbers and chars defining a Quantity
        		"""

    @property
    def Format(self) -> dict:
        """Format of the Quantity"""

    @Format.setter
    def Format(self, value: dict): ...

    @property
    def Unit(self) -> object:
        """Unit of the Quantity"""

    @Unit.setter
    def Unit(self, value: object): ...

    @property
    def UserString(self) -> str:
        """Unit of the Quantity"""

    @property
    def Value(self) -> float:
        """Numeric Value of the Quantity (in internal system mm,kg,s)"""

    @Value.setter
    def Value(self, value: float): ...

    @typing.overload
    def getValueAs(self, arg: FreeCAD.Quantity, /): ...

    @typing.overload
    def getValueAs(self, arg: FreeCAD.Unit, /): ...

    @typing.overload
    def getValueAs(self, arg: str, /): ...

    @typing.overload
    def getValueAs(self, arg: float, arg2: FreeCAD.Unit, /): ...

    @typing.overload
    def getValueAs(self, FreeCAD_Units_Pascal: FreeCAD.Quantity, /): ...

    @typing.overload
    def getValueAs(self, FreeCAD_Units_Pascal: FreeCAD.Unit, /): ...

    @typing.overload
    def getValueAs(self, FreeCAD_Units_Pascal: str, /): ...

    @typing.overload
    def getValueAs(self, Qantity_N_m_2_: FreeCAD.Quantity, /): ...

    @typing.overload
    def getValueAs(self, Qantity_N_m_2_: FreeCAD.Unit, /): ...

    @typing.overload
    def getValueAs(self, Qantity_N_m_2_: str, /): ...

    @typing.overload
    def getValueAs(self, Unit_0_1_0_0_0_0_0_0_: FreeCAD.Quantity, /): ...

    @typing.overload
    def getValueAs(self, Unit_0_1_0_0_0_0_0_0_: FreeCAD.Unit, /): ...

    @typing.overload
    def getValueAs(self, Unit_0_1_0_0_0_0_0_0_: str, /):
        """
                  returns a floating point value as the provided unit

                  Following parameters are allowed:
                  getValueAs('m/s')  # unit string to parse
                  getValueAs(2.45,1) # translatrion value and unit signature
                  getValueAs(FreeCAD.Units.Pascal) # predefined standard units 
                  getValueAs(Qantity('N/m^2')) # a quantity
                  getValueAs(Unit(0,1,0,0,0,0,0,0)) # a unit
                """

    def toStr(self, decimals: int = None, /):
        """
                  toStr([decimals])
                  returns a string representation rounded to number of decimals. If no decimals are specified then
                  the internal precision is used
                """

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Quantity: ...

    def __sub__(self, other) -> Quantity: ...

    def __mul__(self, other) -> Quantity: ...

    def __floordiv__(self, other): ...

    def __divmod__(self, other): ...

    def __pow__(self, power, modulo=None): ...

    def __neg__(self) -> Quantity: ...

    def __pos__(self) -> Quantity: ...

    def __abs__(self) -> Quantity: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rshift__(self, other): ...

    def __and__(self, other): ...

    def __xor__(self, other): ...

    def __or__(self, other): ...

    def __int__(self): ...

    def __float__(self): ...


# BaseClassPy.xml
class BaseClass(FreeCAD.PyObjectBase):
    """This is the base class"""

    @property
    def Module(self) -> str:
        """Module in which this class is defined"""

    @property
    def TypeId(self) -> str:
        """Is the type of the FreeCAD object with module domain"""

    def getAllDerivedFrom(self):
        """Returns all descendants"""

    def isDerivedFrom(self, arg1: str, /):
        """Returns true if given type is a father"""


# MatrixPy.xml
class Matrix(FreeCAD.PyObjectBase):
    """A 4x4 Matrix"""

    @typing.overload
    def __init__(self, arg1: float = None, arg2: float = None, arg3: float = None, arg4: float = None, arg5: float = None, arg6: float = None, arg7: float = None, arg8: float = None, arg9: float = None, arg10: float = None, arg11: float = None, arg12: float = None, arg13: float = None, arg14: float = None, arg15: float = None, arg16: float = None, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Matrix, /):
        """A 4x4 Matrix"""

    @property
    def A(self) -> typing.Sequence:
        """The matrix elements"""

    @A.setter
    def A(self, value: typing.Sequence): ...

    @property
    def A11(self) -> float:
        """The matrix elements"""

    @A11.setter
    def A11(self, value: float): ...

    @property
    def A12(self) -> float:
        """The matrix elements"""

    @A12.setter
    def A12(self, value: float): ...

    @property
    def A13(self) -> float:
        """The matrix elements"""

    @A13.setter
    def A13(self, value: float): ...

    @property
    def A14(self) -> float:
        """The matrix elements"""

    @A14.setter
    def A14(self, value: float): ...

    @property
    def A21(self) -> float:
        """The matrix elements"""

    @A21.setter
    def A21(self, value: float): ...

    @property
    def A22(self) -> float:
        """The matrix elements"""

    @A22.setter
    def A22(self, value: float): ...

    @property
    def A23(self) -> float:
        """The matrix elements"""

    @A23.setter
    def A23(self, value: float): ...

    @property
    def A24(self) -> float:
        """The matrix elements"""

    @A24.setter
    def A24(self, value: float): ...

    @property
    def A31(self) -> float:
        """The matrix elements"""

    @A31.setter
    def A31(self, value: float): ...

    @property
    def A32(self) -> float:
        """The matrix elements"""

    @A32.setter
    def A32(self, value: float): ...

    @property
    def A33(self) -> float:
        """The matrix elements"""

    @A33.setter
    def A33(self, value: float): ...

    @property
    def A34(self) -> float:
        """The matrix elements"""

    @A34.setter
    def A34(self, value: float): ...

    @property
    def A41(self) -> float:
        """The matrix elements"""

    @A41.setter
    def A41(self, value: float): ...

    @property
    def A42(self) -> float:
        """The matrix elements"""

    @A42.setter
    def A42(self, value: float): ...

    @property
    def A43(self) -> float:
        """The matrix elements"""

    @A43.setter
    def A43(self, value: float): ...

    @property
    def A44(self) -> float:
        """The matrix elements"""

    @A44.setter
    def A44(self, value: float): ...

    def analyze(self):
        """
        analyze() -> string
        Analyzes the type of transformation.
                """

    def determinant(self):
        """
        determinant() -> Float
        Compute the determinant of the matrix
                """

    def hasScale(self, tol: float = None, /):
        """
        hasScale(tol=None)
        Return 0 is no scale factor, 1 for uniform scaling, -1 for non-uniform scaling.
                """

    def inverse(self):
        """
        inverse() -> Matrix
        Compute the inverse matrix, if possible
                """

    def invert(self):
        """
        invert() -> None
        Compute the inverse matrix, if possible
                """

    def isOrthogonal(self, Float: float = None, /):
        """
        isOrthogonal([Float]) -> Float
        Checks if the matrix is orthogonal, i.e. M * M^T = k*I and returns
        the multiple of the identity matrix. If it's not orthogonal 0 is returned.
        As argument you can set a tolerance which by default is 1.0e-6.
                """

    @typing.overload
    def move(self, Vector: tuple, /): ...

    @typing.overload
    def move(self, Vector: FreeCAD.Vector, /):
        """
        move(Vector)
        Move the matrix along the vector
                """

    def multVec(self, Vector: FreeCAD.Vector, /):
        """
        multVec(Vector) -> Vector
        Compute the transformed vector using the matrix
                """

    @typing.overload
    def multiply(self, Matrix_Vector: FreeCAD.Matrix, /): ...

    @typing.overload
    def multiply(self, Matrix_Vector: FreeCAD.Vector, /):
        """
        multiply(Matrix|Vector)
        Multiply a matrix or vector with this matrix
                """

    @typing.overload
    def rotateX(self, float: FreeCAD.Quantity, /): ...

    @typing.overload
    def rotateX(self, float: float, /):
        """rotateX(float) - rotate around X"""

    @typing.overload
    def rotateY(self, float: FreeCAD.Quantity, /): ...

    @typing.overload
    def rotateY(self, float: float, /):
        """rotateY(float) - rotate around Y"""

    @typing.overload
    def rotateZ(self, float: FreeCAD.Quantity, /): ...

    @typing.overload
    def rotateZ(self, float: float, /):
        """rotateZ(float) - rotate around Z"""

    @typing.overload
    def scale(self, Vector: tuple, /): ...

    @typing.overload
    def scale(self, Vector: FreeCAD.Vector, /):
        """
        scale(Vector)
        Scale the matrix with the vector
                """

    def submatrix(self, int: int, /):
        """
        submatrix(int) -> Matrix
        Get the sub-matrix. The parameter must be in the range [1,4].
                """

    def transform(self, Vector: FreeCAD.Vector, Matrix: FreeCAD.Matrix, /):
        """transform(Vector,Matrix) - return the dot product of the two vectors"""

    def transpose(self):
        """
        transpose() -> None
        Transpose the matrix. 
                """

    def transposed(self):
        """
        transposed() -> Matrix
        Returns a transposed copy of this matrix.
                """

    def unity(self):
        """unity() - make this matrix to unity"""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Matrix: ...

    def __sub__(self, other) -> Matrix: ...

    def __mul__(self, other) -> Matrix: ...

    def __floordiv__(self, other): ...

    def __divmod__(self, other): ...

    def __pow__(self, power, modulo=None): ...

    def __neg__(self) -> Matrix: ...

    def __pos__(self) -> Matrix: ...

    def __abs__(self) -> Matrix: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rshift__(self, other): ...

    def __and__(self, other): ...

    def __xor__(self, other): ...

    def __or__(self, other): ...

    def __int__(self): ...

    def __float__(self): ...


# CoordinateSystemPy.xml
class CoordinateSystem(FreeCAD.PyObjectBase):
    @property
    def Axis(self) -> object:
        """Set or get axis"""

    @Axis.setter
    def Axis(self, value: object): ...

    @property
    def Position(self) -> object:
        """Set or get position"""

    @Position.setter
    def Position(self, value: object): ...

    @property
    def XDirection(self) -> object:
        """Set or get x direction"""

    @XDirection.setter
    def XDirection(self, value: object): ...

    @property
    def YDirection(self) -> object:
        """Set or get y direction"""

    @YDirection.setter
    def YDirection(self, value: object): ...

    @property
    def ZDirection(self) -> object:
        """Set or get z direction"""

    @ZDirection.setter
    def ZDirection(self, value: object): ...

    def displacement(self, CoordinateSystem: FreeCAD.CoordinateSystem, /):
        """displacement(CoordinateSystem)
        Computes the placement from this to the passed coordinate system"""

    @typing.overload
    def setAxes(self, Axis_or_Vector_z: FreeCAD.Axis, Vector_x: FreeCAD.Vector, /): ...

    @typing.overload
    def setAxes(self, Axis_or_Vector_z: FreeCAD.Vector, Vector_x: FreeCAD.Vector, /):
        """setAxes(Axis or Vector z, Vector x)
        Set axis or z direction and x direction"""

    def setPlacement(self, arg1: FreeCAD.Placement, /):
        """setPlacment(Placement)
        Set placement to the coordinate system.
                """

    @typing.overload
    def transform(self, Rotation_or_Placement: FreeCAD.Placement, /): ...

    @typing.overload
    def transform(self, Rotation_or_Placement: FreeCAD.Rotation, /):
        """transform(Rotation or Placement)
        Applies the rotation or placement on this coordinate system
                """

    def transformTo(self, Vector: FreeCAD.Vector, /):
        """transformTo(Vector)
        Computes the coordinates of the point in coordinates of this system
                """


# TypePy.xml
class BaseType(FreeCAD.PyObjectBase):
    """This is the Type class"""

    @property
    def Key(self) -> int:
        """The key of the type id"""

    @property
    def Module(self) -> str:
        """Module in which this class is defined"""

    @property
    def Name(self) -> str:
        """The name of the type id"""

    def createInstance(self):
        """Creates an instance of this type"""

    @staticmethod
    def createInstanceByName(arg0: str, arg1: bool = None, /):
        """Creates an instance of the named type"""

    @staticmethod
    def fromKey(arg0: int, /):
        """Returns a type object by key"""

    @staticmethod
    def fromName(arg0: str, /):
        """Returns a type object by name"""

    def getAllDerived(self):
        """Returns all descendants"""

    @staticmethod
    @typing.overload
    def getAllDerivedFrom(arg0: str, /): ...

    @staticmethod
    @typing.overload
    def getAllDerivedFrom(arg0: FreeCAD.BaseType, /):
        """Returns all descendants"""

    @staticmethod
    def getBadType():
        """Returns an invalid type id"""

    @staticmethod
    def getNumTypes():
        """Returns the number of type ids"""

    def getParent(self):
        """Returns the parent type id"""

    def isBad(self):
        """Checks if the type id is invalid"""

    @typing.overload
    def isDerivedFrom(self, arg1: str, /): ...

    @typing.overload
    def isDerivedFrom(self, arg1: FreeCAD.BaseType, /):
        """Returns true if given type is a father"""


# AxisPy.xml
class Axis(FreeCAD.PyObjectBase):
    """Axis
    An defines a direction and a position (base) in 3D space.

    The following constructors are supported:
    Axis() -- empty constructor
    Axis(Axis) -- copy constructor
    Axis(Base, Direction) -- define position and direction
    		"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Axis, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: object, /):
        """Axis
        An defines a direction and a position (base) in 3D space.

        The following constructors are supported:
        Axis() -- empty constructor
        Axis(Axis) -- copy constructor
        Axis(Base, Direction) -- define position and direction
        		"""

    @property
    def Base(self) -> object:
        """Vector to the Base position of the Axis"""

    @Base.setter
    def Base(self, value: object): ...

    @property
    def Direction(self) -> object:
        """Direction vector of the Axis"""

    @Direction.setter
    def Direction(self, value: object): ...

    def copy(self):
        """
                            copy()
                            Returns a copy of this Axis
                        """

    def move(self, Vector: FreeCAD.Vector, /):
        """
        					move(Vector)
        					Move the axis base along the vector
        				"""

    def multiply(self, Placement: FreeCAD.Placement, /):
        """
        					multiply(Placement)
        					Multiply this axis with a placement
        				"""

    def reversed(self):
        """
        					reversed() -> Axis
        					compute the reversed axis
        				"""


# ParameterPy.cpp
def GetGroup(arg1: str, /):
    """GetGroup(str)"""


def GetGroups():
    """GetGroups()"""


def RemGroup(arg1: str, /):
    """RemGroup(str)"""


def HasGroup(arg1: str, /):
    """HasGroup(str)"""


def IsEmpty():
    """IsEmpty()"""


def Clear():
    """Clear()"""


def Attach(arg1: object, /):
    """Attach()"""


def Detach(arg1: object, /):
    """Detach()"""


def Notify(arg1: str, /):
    """Notify()"""


def NotifyAll():
    """NotifyAll()"""


def SetBool(arg1: str, arg2: int, /):
    """SetBool()"""


def GetBool(arg1: str, arg2: int = None, /):
    """GetBool()"""


def GetBools(arg1: str = None, /):
    """GetBools()"""


def RemBool(arg1: str, /):
    """RemBool()"""


def SetInt(arg1: str, arg2: int, /):
    """SetInt()"""


def GetInt(arg1: str, arg2: int = None, /):
    """GetInt()"""


def GetInts(arg1: str = None, /):
    """GetInts()"""


def RemInt(arg1: str, /):
    """RemInt()"""


def SetUnsigned(arg1: str, arg2: int, /):
    """SetUnsigned()"""


def GetUnsigned(arg1: str, arg2: int = None, /):
    """GetUnsigned()"""


def GetUnsigneds(arg1: str = None, /):
    """GetUnsigneds()"""


def RemUnsigned(arg1: str, /):
    """RemUnsigned()"""


def SetFloat(arg1: str, arg2: float, /):
    """SetFloat()"""


def GetFloat(arg1: str, arg2: float = None, /):
    """GetFloat()"""


def GetFloats(arg1: str = None, /):
    """GetFloats()"""


def RemFloat(arg1: str, /):
    """RemFloat()"""


def SetString(arg1: str, arg2: str, /):
    """SetString()"""


def GetString(arg1: str, arg2: str = None, /):
    """GetString()"""


def GetStrings(arg1: str = None, /):
    """GetStrings()"""


def RemString(arg1: str, /):
    """RemString()"""


def Import(arg1: str, /):
    """Import()"""


def Insert(arg1: str, /):
    """Insert()"""


def Export(arg1: str, /):
    """Export()"""


def GetContents():
    """GetContents()"""


# Sequencer.cpp
def start(arg1: str, arg2: int, /):
    """start(string,int)"""


def next(arg1: int = None, /):
    """next()"""


def stop():
    """stop()"""


# MaterialPy.xml
class Material(FreeCAD.PyObjectBase):
    """This is the Material class"""

    def __init__(self, DiffuseColor: object = None, AmbientColor: object = None, SpecularColor: object = None, EmissiveColor: object = None, Shininess: object = None, Transparency: object = None):
        """This is the Material class"""

    @property
    def AmbientColor(self) -> tuple:
        """Ambient color"""

    @AmbientColor.setter
    def AmbientColor(self, value: tuple): ...

    @property
    def DiffuseColor(self) -> tuple:
        """Diffuse color"""

    @DiffuseColor.setter
    def DiffuseColor(self, value: tuple): ...

    @property
    def EmissiveColor(self) -> tuple:
        """Emissive color"""

    @EmissiveColor.setter
    def EmissiveColor(self, value: tuple): ...

    @property
    def Shininess(self) -> float:
        """Shininess"""

    @Shininess.setter
    def Shininess(self, value: float): ...

    @property
    def SpecularColor(self) -> tuple:
        """Specular color"""

    @SpecularColor.setter
    def SpecularColor(self, value: tuple): ...

    @property
    def Transparency(self) -> float:
        """Transparency"""

    @Transparency.setter
    def Transparency(self, value: float): ...

    def set(self, arg1: str, /):
        """
        Set(string) -- Set the material.

        The material must be one of the following values:
        Brass, Bronze, Copper, Gold, Pewter, Plaster, Plastic, Silver, Steel, Stone, Shiny plastic,
        Satin, Metalized, Neon GNC, Chrome, Aluminium, Obsidian, Neon PHC, Jade, Ruby or Emerald.
        			"""


# DocumentObjectGroupPy.xml
class DocumentObjectGroup(FreeCAD.DocumentObject):
    """This class handles document objects in group"""


# GeoFeaturePy.xml
class GeoFeature(FreeCAD.DocumentObject):
    """This class does the whole placement and position handling"""

    def getGlobalPlacement(self):
        """Returns the placement of the object in the global coordinate space, respecting all stacked relationships. 
                          Note: This function is not available during recompute, as there the placements of parents can change 
                          after the execution of this object, rendering the result wrong."""

    def getPropertyNameOfGeometry(self):
        """Returns the property name of the actual geometry or None.
        For example for a part object it returns the value Shape,
        for a mesh the value Mesh and so on.
        If an object has no such property then None is returned."""

    def getPropertyOfGeometry(self):
        """Returns the property of the actual geometry or None.
        For example for a part object it returns its Shape property,
        for a mesh its Mesh property and so on.
        If an object has no such property then None is returned.
        Unlike to getPropertyNameOfGeometry this function returns the geometry,
        not its name.
        """


# DocumentObjectPy.xml
class DocumentObject(FreeCAD.ExtensionContainer):
    """This is the father of all classes handled by the document"""

    @property
    def Label(self) -> str: ...

    @Label.setter
    def Label(self, value: str): ...

    @property
    def Proxy(self) -> object: ...

    @Proxy.setter
    def Proxy(self, value: object): ...

    @property
    def Document(self) -> object:
        """Return the document this object is part of"""

    @property
    def FullName(self) -> str:
        """Return the document name and internal name of this object"""

    @property
    def ID(self) -> int:
        """The unique identifier (among its document) of this object"""

    @property
    def InList(self) -> list:
        """A list of all objects which link to this object."""

    @property
    def InListRecursive(self) -> list:
        """A list of all objects which link to this object recursively."""

    @property
    def MustExecute(self) -> bool:
        """Check if the object must be recomputed"""

    @property
    def Name(self) -> str:
        """Return the internal name of this object"""

    @property
    def NoTouch(self) -> bool:
        """Enable/disable no touch on any property change"""

    @property
    def OldLabel(self) -> str:
        """Contains the old label before change"""

    @property
    def OutList(self) -> list:
        """A list of all objects this object links to."""

    @property
    def OutListRecursive(self) -> list:
        """A list of all objects this object links to recursively."""

    @property
    def Parents(self) -> list:
        """A List of tuple(parent,subname) holding all parents to this object"""

    @property
    def Removing(self) -> bool:
        """Indicate if the object is being removed"""

    @property
    def State(self) -> list:
        """State of the object in the document"""

    @property
    def ViewObject(self) -> object:
        """If the GUI is loaded the associated view provider is returned
        or None if the GUI is not up"""

    def addProperty(self, arg1: str, arg2: str = None, arg3: str = None, arg4: str = None, arg5: int = None, arg6: bool = None, arg7: bool = None, /):
        """
                            addProperty(string, string) -- Add a generic property.
                            The first argument specifies the type, the second the
                            name of the property.
                        """

    def adjustRelativeLinks(self, parent: FreeCAD.DocumentObject, recursive: object = True, /):
        """adjustRelativeLinks(parent,recursive=True) -- auto correct potential cyclic dependencies"""

    def enforceRecompute(self):
        """Mark the object for recompute"""

    def evalExpression(self, arg1: str, /):
        """Evaluate an expression"""

    def getLinkedObject(self, recursive: object = True, matrix: object = None, transform: object = True, depth: int = 0):
        """
        getLinkedObject(recursive=True, matrix=None, transform=True, depth=0)
        Returns the linked object if there is one, or else return itself

        * recursive: whether to recursively resolve the links

        * transform: whether to transform the sub object using this object's placement

        * matrix: If not none, this specifies the initial transformation to be applied
        to the sub object. And cause the method to return a tuple (object, matrix)
        containing the accumulated transformation matrix

        * depth: current recursive depth
                        """

    def getParentGeoFeatureGroup(self):
        """Returns the GeoFeatureGroup, and hence the local coordinate system, the object 
                                  is in or None if it is not part of a group. Note that an object can only be 
                                  in a single group, hence only a single return value."""

    def getParentGroup(self):
        """Returns the group the object is in or None if it is not part of a group. 
                                  Note that an object can only be in a single group, hence only a single return 
                                  value."""

    def getPathsByOutList(self, arg1: FreeCAD.DocumentObject, /):
        """Get all paths from this object to another object following the OutList."""

    def getStatusString(self):
        """Returns the status of the object as string.
        If the object is invalid its error description will be returned.
        If the object is valid but touched then 'Touched' will be returned,
        'Valid' otherwise.
        """

    def getSubObject(self, subname: object, retType: int = 0, matrix: object = None, transform: object = True, depth: int = 0):
        """
        getSubObject(subname, retType=0, matrix=None, transform=True, depth=0)

        * subname(string|list|tuple): dot separated string or sequence of strings
        referencing subobject.

        * retType: return type, 0=PyObject, 1=DocObject, 2=DocAndPyObject, 3=Placement

            PyObject: return a python binding object for the (sub)object referenced in
            each 'subname' The actual type of 'PyObject' is implementation dependent.
            For Part::Feature compatible objects, this will be of type TopoShapePy and
            pre-transformed by accumulated transformation matrix along the object path.  

            DocObject:  return the document object referenced in subname, if 'matrix' is
            None. Or, return a tuple (object, matrix) for each 'subname' and 'matrix' is
            the accumulated transformation matrix for the sub object.

            DocAndPyObject: return a tuple (object, matrix, pyobj) for each subname

            Placement: return a transformed placement of the sub-object

        * matrix: the initial transformation to be applied to the sub object.

        * transform: whether to transform the sub object using this object's placement

        * depth: current recursive depth
                        """

    def getSubObjectList(self, subname: str, /):
        """
        getSubObjectList(subname)

        Return a list of objects referenced by a given subname including this object
                        """

    def getSubObjects(self, reason: int = 0, /):
        """getSubObjects(reason=0): Return subname reference of all sub-objects"""

    def hasChildElement(self):
        """Return true to indicate the object having child elements"""

    def isElementVisible(self, element: str, /):
        """
        isElementVisible(element): Check if a child element is visible
        Return -1 if element visibility is not supported or element not found, 0 if invisible, or else 1
                        """

    def isValid(self):
        """Returns True if the object is valid, False otherwise"""

    def purgeTouched(self):
        """Mark the object as unchanged"""

    def recompute(self, recursive: object = False, /):
        """recompute(recursive=False): Recomputes this object"""

    def removeProperty(self, string: str, /):
        """
                            removeProperty(string) -- Remove a generic property.
                            Note, you can only remove user-defined properties but not built-in ones.
                        """

    def resolve(self, subname: str, /):
        """
        resolve(subname) -- resolve the sub object

        Returns a tuple (subobj,parent,elementName,subElement), where 'subobj' is the
        last object referenced in 'subname', and 'parent' is the direct parent of
        'subobj', and 'elementName' is the name of the subobj, which can be used
        to call parent.isElementVisible/setElementVisible(). 'subElement' is the
        non-object sub-element name if any.
                        """

    def resolveSubElement(self, subname: str, append: object = None, type: int = None, /):
        """
        resolveSubElement(subname,append,type) -- resolve both new and old style sub element

        subname: subname reference containing object hierarchy
        append: Whether to append object hierarchy prefix inside subname to returned element name
        type: 0: normal, 1: for import, 2: for export

        Return tuple(obj,newElementName,oldElementName)
                        """

    def setElementVisible(self, element: str, visible: object = None, /):
        """
        setElementVisible(element,visible): Set the visibility of a child element
        Return -1 if element visibility is not supported, 0 if element not found, 1 if success
                        """

    @typing.overload
    def setExpression(self, arg1: str, arg2: object, arg3: str = None, /): ...

    @typing.overload
    def setExpression(self, arg1: str, /): ...

    @typing.overload
    def setExpression(self, arg1: object = None, /): ...

    @typing.overload
    def setExpression(self): ...

    @typing.overload
    def setExpression(self): ...

    @typing.overload
    def setExpression(self, arg1: str, /): ...

    @typing.overload
    def setExpression(self, arg1: int = None, /): ...

    @typing.overload
    def setExpression(self, arg1: str, /): ...

    @typing.overload
    def setExpression(self, arg1: str, arg2: object = None, /): ...

    @typing.overload
    def setExpression(self): ...

    @typing.overload
    def setExpression(self): ...

    @typing.overload
    def setExpression(self): ...

    @typing.overload
    def setExpression(self, arg1: FreeCAD.DocumentObject, /): ...

    @typing.overload
    def setExpression(self, arg1: str, /): ...

    @typing.overload
    def setExpression(self, arg1: str, arg2: object = None, arg3: int = None, /): ...

    @typing.overload
    def setExpression(self, arg1: FreeCAD.DocumentObject, arg2: object = None, /): ...

    @typing.overload
    def setExpression(self, subname: object, retType: int = None, matrix: object = None, transform: object = None, depth: int = None): ...

    @typing.overload
    def setExpression(self, recursive: object = None, matrix: object = None, transform: object = None, depth: int = None):
        """Register an expression for a property"""

    def supportedProperties(self):
        """A list of supported property types"""

    def touch(self, arg1: str = None, /):
        """Mark the object as changed (touched)"""


# LinkBaseExtensionPy.xml
class LinkBaseExtension(FreeCAD.DocumentObjectExtension):
    """Link extension base class"""

    @property
    def LinkedChildren(self) -> list:
        """Return a flattened (in case grouped by plain group) list of linked children"""

    def cacheChildLabel(self, enable: object = True, /):
        """
        cacheChildLabel(enable=True): enable/disable child label cache

        The cache is not updated on child label change for performance reason. You must
        call this function on any child label change
                """

    @typing.overload
    def configLinkProperty(self, key, arg): ...

    @typing.overload
    def configLinkProperty(self, key, arg): ...

    @typing.overload
    def configLinkProperty(self, arg): ...

    @typing.overload
    def configLinkProperty(self, key, arg):
        """
        configLinkProperty(key=val,...): property configuration
        configLinkProperty(key,...): property configuration with default name

        This methode is here to implement what I called Property Design
        Pattern. The extension operates on a predefined set of properties,
        but it relies on the extended object to supply the actual property by
        calling this methode. You can choose a sub set of functionality of
        this extension by supplying only some of the supported properties. 

        The 'key' are names used to refer to properties supported by this
        extension, and 'val' is the actual name of the property of your
        object. You can obtain the key names and expected types using
        getLinkPropertyInfo().  You can use property of derived type when
        calling configLinkProperty().  Other types will cause exception to
        ben thrown. The actual properties supported may be different
        depending on the actual extension object underlying this python
        object.

        If 'val' is omitted, i.e. calling configLinkProperty(key,...), then
        it is assumed the the actually property name is the same as 'key'
                """

    def expandSubname(self, subname: str, /):
        """
        expandSubname(subname) -> string

        Return an expanded subname in case it references an object inside a linked plain group
                """

    def flattenSubname(self, subname: str, /):
        """
        flattenSubname(subname) -> string

        Return a flattened subname in case it references an object inside a linked plain group
                """

    def getLinkExtProperty(self, name: str, /):
        """getLinkExtProperty(name): return the property value by its predefined name """

    def getLinkExtPropertyName(self, name: str, /):
        """getLinkExtPropertyName(name): lookup the property name by its predefined name """

    @typing.overload
    def getLinkPropertyInfo(self, arg: int, /): ...

    @typing.overload
    def getLinkPropertyInfo(self, arg: str, /): ...

    @typing.overload
    def getLinkPropertyInfo(self, index: int, /): ...

    @typing.overload
    def getLinkPropertyInfo(self, index: str, /): ...

    @typing.overload
    def getLinkPropertyInfo(self, name: int, /): ...

    @typing.overload
    def getLinkPropertyInfo(self, name: str, /):
        """
        getLinkPropertyInfo(): return a tuple of (name,type,doc) for all supported properties.

        getLinkPropertyInfo(index): return (name,type,doc) of a specific property

        getLinkPropertyInfo(name): return (type,doc) of a specific property
                """

    @typing.overload
    def setLink(self, obj, subName = None, subElements = None): ...

    @typing.overload
    def setLink(self, obj, arg): ...

    @typing.overload
    def setLink(self, arg, arg2): ...

    @typing.overload
    def setLink(self, arg, arg2): ...

    @typing.overload
    def setLink(self, arg, arg2):
        """
        setLink(obj,subName=None,subElements=None): Set link object.

        setLink([obj,...]),
        setLink([(obj,subName,subElements),...]),
        setLink({index:obj,...}),
        setLink({index:(obj,subName,subElements),...}): set link element of a link group.

        obj (DocumentObject): the object to link to. If this is None, then the link is cleared

        subName (String): Dot separated object path. 

        subElements (String|tuple(String)): non-object sub-elements, e.g. Face1, Edge2.
                """


# PartPy.xml
class Part(FreeCAD.GeoFeature):
    """This class handles document objects in Part"""


# DocumentObjectExtensionPy.xml
class DocumentObjectExtension(FreeCAD.Extension):
    """Base class for all document object extensions"""


# GroupExtensionPy.xml
class GroupExtension(FreeCAD.DocumentObjectExtension):
    """Extension class which allows grouping of document objects"""

    @property
    def Group(self) -> list[DocumentObject]: ...

    @Group.setter
    def Group(self, value: list[DocumentObject]): ...

    def addObject(self, arg1: FreeCAD.DocumentObject, /):
        """Add an object to the group. Returns all objects that have been added."""

    def addObjects(self, arg1: object, /):
        """Adds multiple objects to the group. Expects a list and returns all objects that have been added."""

    def getObject(self, arg1: str, /):
        """Return the object with the given name"""

    def hasObject(self, obj: FreeCAD.DocumentObject, recursive: object = False, /):
        """hasObject(obj, recursive=false)
                        Checks if the group has a given object
                        @param obj        the object to check for.
                        @param recursive  if true check also if the obj is child of some sub group (default is false).
                    """

    def newObject(self, arg1: str, arg2: str = None, /):
        """Create and add an object with given type and name to the group"""

    def removeObject(self, arg1: FreeCAD.DocumentObject, /):
        """Remove an object from the group and returns all objects that have been removed."""

    def removeObjects(self, arg1: object, /):
        """Remove multiple objects from the group. Expects a list and returns all objects that have been removed."""

    def removeObjectsFromDocument(self):
        """Remove all child objects from the group and document"""

    def setObjects(self, arg1: object, /):
        """Sets the objects of the group. Expects a list and returns all objects that are now in the group."""


# ExtensionPy.xml
class Extension(FreeCAD.PyObjectBase):
    """Base class for all extensions"""


# GeoFeatureGroupExtensionPy.xml
class GeoFeatureGroupExtension(FreeCAD.GroupExtension):
    """This class handles placeable group of document objects"""


# OriginGroupExtensionPy.xml
class OriginGroupExtension(FreeCAD.GeoFeatureGroupExtension):
    """This class handles placable group of document objects with an Origin"""


# ExtensionContainerPy.xml
class ExtensionContainer(FreeCAD.PropertyContainer):
    """Base class for all objects which can be extended"""

    def addExtension(self, arg1: str, arg2: object = None, /):
        """Adds an extension to the object. Requires the string identifier for the python extension as argument"""

    def hasExtension(self, arg1: str, arg2: object = None, /):
        """Returns if this object has the specified extension"""


# DocumentPy.xml
class Document(FreeCAD.PropertyContainer):
    """This is a Document class"""

    @property
    def ActiveObject(self) -> object:
        """The active object of the document"""

    @property
    def DependencyGraph(self) -> str:
        """The dependency graph as GraphViz text"""

    @property
    def HasPendingTransaction(self) -> bool:
        """Check if there is a pending transaction"""

    @property
    def Importing(self) -> bool:
        """Indicate if the document is importing. Note the document will also report Restoring while importing"""

    @property
    def InList(self) -> list:
        """A list of all documents that link to this document."""

    @property
    def Name(self) -> str:
        """The internal name of the document"""

    @property
    def Objects(self) -> list:
        """The list of object handled by this document"""

    @property
    def OldLabel(self) -> str:
        """Contains the old label before change"""

    @property
    def OutList(self) -> list:
        """A list of all documents that this document links to."""

    @property
    def Partial(self) -> bool:
        """Indicate if the document is partially loaded"""

    @property
    def RecomputesFrozen(self) -> bool:
        """Returns or sets if automatic recomputes for this document are disabled."""

    @property
    def Recomputing(self) -> bool:
        """Indicate if the document is recomputing"""

    @property
    def RedoCount(self) -> int:
        """Number of possible Redos"""

    @property
    def RedoNames(self) -> list:
        """A List of Redo names"""

    @property
    def Restoring(self) -> bool:
        """Indicate if the document is restoring"""

    @property
    def RootObjects(self) -> list:
        """The list of root object of this document"""

    @property
    def Temporary(self) -> bool:
        """Check if this is a temporary document"""

    @property
    def TopologicalSortedObjects(self) -> list:
        """The list of object of this document in topological sorted order"""

    @property
    def Transacting(self) -> bool:
        """Indicate whether the document is undoing/redoing"""

    @property
    def UndoCount(self) -> int:
        """Number of possible Undos"""

    @property
    def UndoMode(self) -> int:
        """The Undo mode of the Document (0 = no Undo, 1 = Undo/Redo)"""

    @UndoMode.setter
    def UndoMode(self, value: int): ...

    @property
    def UndoNames(self) -> list:
        """A list of Undo names"""

    @property
    def UndoRedoMemSize(self) -> int:
        """The size of the Undo stack in byte"""

    def abortTransaction(self):
        """Abort an Undo/Redo transaction (rollback)"""

    def addObject(self, type: str, name: str = None, objProxy: object = None, viewProxy: object = None, attach: object = False, viewType: str = None):
        """addObject(type, name=None, objProxy=None, viewProxy=None, attach=False, viewType=None)

        Add an object to document

        type (String): the type of the document object to create.
        name (String): the optional name of the new object.
        objProxy (Object): the Python binding object to attach to the new document object.
        viewProxy (Object): the Python binding object to attach the view provider of this object.
        attach (Boolean): if True, then bind the document object first before adding to the document
                to allow Python code to override view provider type. Once bound, and before adding to
                the document, it will try to call Python binding object's attach(obj) method.
        viewType (String): override the view provider type directly, only effective when attach is False."""

    def clearUndos(self):
        """Clear the undo stack of the document"""

    def commitTransaction(self):
        """Commit an Undo/Redo transaction"""

    def copyObject(self, object: object, with_dependencies: object = False, return_all: object = False, /):
        """
        copyObject(object, with_dependencies=False, return_all=False)
        Copy an object or objects from another document to this document. 

        object: can either a single object or sequence of objects
        with_dependencies: if True, all internal dependent objects are copied too.
        return_all: if True, return all copied objects, or else return only the copied
                    object corresponding to the input objects.
                  """

    def exportGraphviz(self, arg1: str = None, /):
        """Export the dependencies of the objects as graph"""

    def findObjects(self, Type: str = None, Name: str = None, Label: str = None):
        """findObjects([Type=string], [Name=string], [Label=string]) -> list
        Return a list of objects that match the specified type, name or label.
        Name and label support regular expressions. All parameters are optional."""

    def getDependentDocuments(self, sort: object = True, /):
        """
        getDependentDocuments(sort=True)

        Returns a list of documents that this document directly or indirectly links to including itself.

        sort: whether to topologically sort the return list
                      """

    def getLinksTo(self, obj: object = None, options: int = 0, maxCount: int = 0, /):
        """
        getLinksTo(obj, options=0, maxCount=0): return objects linked to 'obj'

        options: 1: recursive, 2: check link array. Options can combine.
        maxCount: to limit the number of links returned
                    """

    @typing.overload
    def getObject(self, arg1: str, /): ...

    @typing.overload
    def getObject(self, arg1: int, /):
        """Return the object with the given name"""

    def getObjectsByLabel(self, arg1: str, /):
        """Return the objects with the given label name.
        NOTE: It's possible that several objects have the same label name."""

    def getTempFileName(self, arg1: object, /):
        """Returns a file name with path in the temp directory of the document."""

    def importLinks(self, object_object_: object = None, /):
        """
        importLinks(object|[object...])

        Import any externally linked object given a list of objects in
        this document.  Any link type properties of the input objects
        will be automatically reassigned to the imported object

        If no object is given as input, it import all externally linked
        object of this document.
                  """

    def load(self, arg1: str, /):
        """Load the document from the given path"""

    def mergeProject(self, arg1: str, /):
        """Merges this document with another project file"""

    def moveObject(self, arg1: str, /):
        """
        moveObject(object, bool with_dependencies = False)
        Transfers an object from another document to this document.
              
        object: can either a single object or sequence of objects
        with_dependencies: if True, all internal dependent objects are copied too.
                """

    def openTransaction(self, name: object = None, /):
        """openTransaction(name) - Open a new Undo/Redo transaction.

        This function no long creates a new transaction, but calls
        FreeCAD.setActiveTransaction(name) instead, which will auto creates a
        transaction with the given name when any change happed in any opened document.
        If more than one document is changed, all newly created transactions will have
        the same internal ID and will be undo/redo together.
                  """

    def recompute(self, arg1: object = None, arg2: bool = None, arg3: bool = None, /):
        """recompute(objs=None): Recompute the document and returns the amount of recomputed features"""

    def redo(self):
        """Redo a previously undone transaction"""

    def removeObject(self, arg1: str, /):
        """Remove an object from the document"""

    def restore(self):
        """Restore the document from disk"""

    def save(self):
        """Save the document to disk"""

    def saveAs(self, arg1: str, /):
        """Save the document under a new name to disk"""

    def saveCopy(self, arg1: str, /):
        """Save a copy of the document under a new name to disk"""

    def supportedTypes(self):
        """A list of supported types of objects"""

    def undo(self):
        """Undo one transaction"""


# PropertyContainerPy.xml
class PropertyContainer(FreeCAD.Persistence):
    """This is a Persistence class"""

    @property
    def PropertiesList(self) -> list:
        """A list of all property names"""

    def dumpPropertyContent(self, Property: str, Compression: int = 1-9):
        """Dumps the content of the property, both the XML representation as well as the additional datafiles  
        required, into a byte representation. It will be returned as byte array.
        dumpPropertyContent(propertyname) -- returns a byte array with full content
        dumpPropertyContent(propertyname, [Compression=1-9]) -- Sets the data compression from 0 (no) to 9 (max)
                        """

    def getDocumentationOfProperty(self, arg1: str, /):
        """Return the documentation string of the property of this class."""

    def getEditorMode(self, arg1: str, /):
        """Get the behaviour of the property in the property editor.
        It returns a list of strings with the current mode. If the list is empty there are no special restrictions.
        If the list contains 'ReadOnly' then the item appears in the property editor but is disabled.
        If the list contains 'Hidden' then the item even doesn't appear in the property editor.
                        """

    def getEnumerationsOfProperty(self, arg1: str, /):
        """Return all enumeration strings of the property of this class or None if not a PropertyEnumeration."""

    def getGroupOfProperty(self, arg1: str, /):
        """Return the name of the group which the property belongs to in this class. The properties sorted in different named groups for convenience."""

    def getPropertyByName(self, name: str, checkOwner: int = 0, /):
        """
        getPropertyByName(name,checkOwner=0)

        Return the value of a named property. Note that the returned property may not
        always belong to this container (e.g. from a linked object).

        * name: name of the property
        * checkOwner:  0: just return the property
                       1: raise exception if not found or the property 
                          does not belong to this container
                       2: return a tuple(owner,property_value)
                """

    def getPropertyStatus(self, name: str = '', /):
        """
        getPropertyStatus(name=''): Get property status.

        name(String): property name. If name is empty, return a list of supported
        text names of the status.
                        """

    def getPropertyTouchList(self, arg1: str, /):
        """Return a list of index of touched values for list type properties."""

    def getTypeIdOfProperty(self, arg1: str, /):
        """Returns the C++ class name of a named property."""

    def getTypeOfProperty(self, arg1: str, /):
        """Return the type of a named property. This can be (Hidden,ReadOnly,Output) or any combination. """

    def restorePropertyContent(self, propertyname: str, buffer: object, /):
        """Restore the content of given property from a byte representation as stored by \"dumpContent\".
        It could be restored from any python object implementing the buffer protocol.
        restorePropertyContent(propertyname, buffer) -- restores from the given byte array
                        """

    @typing.overload
    def setEditorMode(self, arg1: str, arg2: int, /): ...

    @typing.overload
    def setEditorMode(self, arg1: str, arg2: object, /):
        """Set the behaviour of the property in the property editor.
        0 - default behaviour
        1 - item is ready-only
        2 - item is hidden
                        """

    def setPropertyStatus(self, name: str, val: object, /):
        """
        setPropertyStatus(name,val): Set property status

        name(String): property name

        val(String|Int|[String|Int...]): text or integer value, or list/tuple of
        values. Call getPropertyStatus() to get a list of supported text value.
        If the text start with '-' or the integer value is negative, then the
        status is cleared.
                        """


# ComplexGeoDataPy.xml
class ComplexGeoData(FreeCAD.Persistence):
    """Father of all complex geometric data types"""

    @property
    def BoundBox(self) -> object:
        """Get the BoundBox of the object"""

    @property
    def Matrix(self) -> object:
        """Get the current transformation of the object as matrix"""

    @Matrix.setter
    def Matrix(self, value: object): ...

    @property
    def Placement(self) -> object:
        """Get the current transformation of the object as placement"""

    @Placement.setter
    def Placement(self, value: object): ...

    @property
    def Tag(self) -> int:
        """Geometry Tag"""

    def getFacesFromSubelement(self, arg1: str, arg2: int, /):
        """Return vertexes and faces from a sub-element"""


# ApplicationPy.cpp
def ParamGet(arg1: str, /):
    """Get parameters by path"""


def saveParameter(arg1: str = None, /):
    """saveParameter(config='User parameter') -> None
    Save parameter set to file. The default set is 'User parameter'"""


def Version():
    """Print the version to the output."""


def ConfigGet(arg1: str, /):
    """ConfigGet(string) -- Get the value for the given key."""


def ConfigSet(arg1: str, arg2: str, /):
    """ConfigSet(string, string) -- Set the given key to the given value."""


def ConfigDump():
    """Dump the configuration to the output."""


def addImportType(arg1: str, arg2: str, /):
    """Register filetype for import"""


def changeImportModule(arg1: str, arg2: str, arg3: str, /):
    """Change the import module name of a registered filetype"""


def getImportType(arg1: str = None, /):
    """Get the name of the module that can import the filetype"""


def EndingAdd(arg1: str, arg2: str, /):
    """deprecated -- use addImportType"""


def EndingGet(arg1: str = None, /):
    """deprecated -- use getImportType"""


def addExportType(arg1: str, arg2: str, /):
    """Register filetype for export"""


def changeExportModule(arg1: str, arg2: str, arg3: str, /):
    """Change the export module name of a registered filetype"""


def getExportType(arg1: str = None, /):
    """Get the name of the module that can export the filetype"""


def getResourceDir():
    """Get the root directory of all resources"""


def getUserAppDataDir():
    """Get the root directory of user settings"""


def getUserMacroDir(arg1: bool = None, /):
    """getUserMacroDir(bool=False) -> stringGet the directory of the user's macro directory
    If parameter is False (the default) it returns the standard path in theuser's home directory, otherwise it returns the user-defined path."""


def getHelpDir():
    """Get the directory of the documentation"""


def getHomePath():
    """Get the home path, i.e. the parent directory of the executable"""


def loadFile(arg1: str, arg2: str = None, arg3: str = None, /):
    """loadFile(string=filename,[string=module]) -> None

    Loads an arbitrary file by delegating to the given Python module:
    * If no module is given it will be determined by the file extension.
    * If more than one module can load a file the first one will be taken.
    * If no module exists to load the file an exception will be raised."""


def open(name: str, hidden: object = None):
    """See openDocument(string)"""


def openDocument(name: str, hidden: object = None):
    """openDocument(filepath,hidden=False) -> object
    Create a document and load the project file into the document.

    filepath: file path to an existing file. If the file doesn't exist
              or the file cannot be loaded an I/O exception is thrown.
              In this case the document is kept alive.
    hidden: whether to hide document 3D view."""


def newDocument(name: str = None, label: str = None, hidden: object = None, temp: object = None):
    """newDocument(name, label=None, hidden=False, temp=False) -> object
    Create a new document with a given name.

    name: unique document name which is checked automatically.
    label: optional user changeable label for the document.
    hidden: whether to hide document 3D view.
    temp: mark the document as temporary so that it will not be saved"""


def closeDocument(arg1: str, /):
    """closeDocument(string) -> None

    Close the document with a given name."""


def activeDocument():
    """activeDocument() -> object or None

    Return the active document or None if there is no one."""


def setActiveDocument(arg1: str, /):
    """setActiveDocement(string) -> None

    Set the active document by its name."""


def getDocument(arg1: str, /):
    """getDocument(string) -> object

    Get a document by its name or raise an exception
    if there is no document with the given name."""


def listDocuments(arg1: object = None, /):
    """listDocuments(sort=False) -> list

    Return a list of names of all documents, optionally sort in dependency order."""


def addDocumentObserver(arg1: object, /):
    """addDocumentObserver() -> None

    Add an observer to get notified about changes on documents."""


def removeDocumentObserver(arg1: object, /):
    """removeDocumentObserver() -> None

    Remove an added document observer."""


@typing.overload
def setLogLevel(arg1: str, arg2: object, /): ...


@typing.overload
def setLogLevel(arg1: str, /): ...


@typing.overload
def setLogLevel(arg1: int, /): ...


@typing.overload
def setLogLevel(arg1: object = None, arg2: int = None, arg3: int = None, /): ...


@typing.overload
def setLogLevel(arg1: object, arg2: int = None, /): ...


@typing.overload
def setLogLevel(arg1: str, arg2: object = None, /): ...


@typing.overload
def setLogLevel(): ...


@typing.overload
def setLogLevel(arg1: object = None, arg2: int = None, /): ...


@typing.overload
def setLogLevel():
    """setLogLevel(tag, level) -- Set the log level for a string tag.
    'level' can either be string 'Log', 'Msg', 'Wrn', 'Error', or an integer value"""


def getLogLevel(arg1: str, /):
    """getLogLevel(tag) -- Get the log level of a string tag"""


def checkLinkDepth(arg1: int, /):
    """checkLinkDepth(depth) -- check link recursion depth"""


def getLinksTo(arg1: object = None, arg2: int = None, arg3: int = None, /):
    """getLinksTo(obj,options=0,maxCount=0) -- return the objects linked to 'obj'

    options: 1: recursive, 2: check link array. Options can combine.
    maxCount: to limit the number of links returned
    """


def getDependentObjects(arg1: object, arg2: int = None, /):
    """getDependentObjects(obj|[obj,...], options=0)
    Return a list of dependent objects including the given objects.

    options: can have the following bit flags,
             1: to sort the list in topological order.
             2: to exclude dependency of Link type object."""


def setActiveTransaction(arg1: str, arg2: object = None, /):
    """setActiveTransaction(name, persist=False) -- setup active transaction with the given name

    name: the transaction name
    persist(False): by default, if the calling code is inside any invocation of a command, it
                    will be auto closed once all commands within the current stack exists. To
                    disable auto closing, set persist=True
    Returns the transaction ID for the active transaction. An application-wide
    active transaction causes any document changes to open a transaction with
    the given name and ID."""


def getActiveTransaction():
    """getActiveTransaction() -> (name,id) return the current active transaction name and ID"""


def closeActiveTransaction(arg1: object = None, arg2: int = None, /):
    """closeActiveTransaction(abort=False) -- commit or abort current active transaction"""


def isRestoring():
    """isRestoring() -> Bool -- Test if the application is opening some document"""


def checkAbort():
    """checkAbort() -- check for user abort in length operation.

    This only works if there is an active sequencer (or ProgressIndicator in Python).
    There is an active sequencer during document restore and recomputation. User may
    abort the operation by pressing the ESC key. Once detected, this function will
    trigger a BaseExceptionFreeCADAbort exception."""


GuiUp: typing.Literal[0, 1]
Gui = FreeCADGui
ActiveDocument: Document
