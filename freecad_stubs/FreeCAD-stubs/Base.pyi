import sys
import typing

import FreeCAD


class ReturnGetFormatDict(typing.TypedDict):
    Precision: int
    NumberFormat: str
    Denominator: int



# VectorPy.xml
class Vector(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    Base.Vector class.

    This class represents a 3D float vector.
    Useful to represent points in the 3D space.

    The following constructors are supported:

    Vector(x=0, y=0, z=0)
    x : float
    y : float
    z : float

    Vector(vector)
    Copy constructor.
    vector : Base.Vector

    Vector(seq)
    Define from a sequence of float.
    seq : sequence of float.
    """

    @typing.overload
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, /): ...

    @typing.overload
    def __init__(self, object: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, object, /):
        """
        Base.Vector class.

        This class represents a 3D float vector.
        Useful to represent points in the 3D space.

        The following constructors are supported:

        Vector(x=0, y=0, z=0)
        x : float
        y : float
        z : float

        Vector(vector)
        Copy constructor.
        vector : Base.Vector

        Vector(seq)
        Define from a sequence of float.
        seq : sequence of float.
        Possible exceptions: (TypeError).
        """

    @property
    def Length(self) -> float:
        """Gets or sets the length of this vector."""

    @Length.setter
    def Length(self, value: float): ...

    @property
    def x(self) -> float:
        """Gets or sets the X component of this vector."""

    @x.setter
    def x(self, value: float): ...

    @property
    def y(self) -> float:
        """Gets or sets the Y component of this vector."""

    @y.setter
    def y(self, value: float): ...

    @property
    def z(self) -> float:
        """Gets or sets the Z component of this vector."""

    @z.setter
    def z(self, value: float): ...

    def __reduce__(self) -> tuple[typing.Any, tuple[float, float, float]]:
        """
        __reduce__() -> tuple

        Serialization of Vector objects.
        """

    def add(self, obj: FreeCAD.Vector, /) -> FreeCAD.Vector:
        """
        add(vector2) -> Base.Vector

        Returns the sum of this vector and `vector2`.

        vector2 : Base.Vector
        """

    def cross(self, obj: FreeCAD.Vector, /) -> FreeCAD.Vector:
        """
        cross(vector2) -> Base.Vector

        Returns the vector product (cross product) between this vector and `vector2`.

        vector2 : Base.Vector
        """

    def distanceToLine(self, base, line, /) -> float:
        """
        distanceToLine(base, dir) -> float

        Returns the distance between the point represented by this vector
        and a line defined by a base point represented by `base` and a
        direction `dir`.

        base : Base.Vector
        dir : Base.Vector
        Possible exceptions: (TypeError).
        """

    def distanceToLineSegment(self, base, line, /) -> FreeCAD.Vector:
        """
        distanceToLineSegment(point1, point2) -> Base.Vector

        Returns the vector between the point represented by this vector and the point
        on the line segment with the shortest distance. The line segment is defined by
        `point1` and `point2`.

        point1 : Base.Vector
        point2 : Base.Vector
        Possible exceptions: (TypeError).
        """

    def distanceToPlane(self, base, line, /) -> float:
        """
        distanceToPlane(base, normal) -> float

        Returns the distance between this vector and a plane defined by a
        base point represented by `base` and a normal defined by `normal`.

        base : Base.Vector
        normal : Base.Vector
        Possible exceptions: (TypeError).
        """

    def distanceToPoint(self, pnt: FreeCAD.Vector, /) -> float:
        """
        distanceToPoint(point2) -> float

        Returns the distance to another point represented by `point2`.
        .
        point : Base.Vector
        """

    def dot(self, obj: FreeCAD.Vector, /) -> float:
        """
        dot(vector2) -> float

        Returns the scalar product (dot product) between this vector and `vector2`.

        vector2 : Base.Vector
        """

    def getAngle(self, obj: FreeCAD.Vector, /) -> float:
        """
        getAngle(vector2) -> float

        Returns the angle in radians between this vector and `vector2`.

        vector2 : Base.Vector
        """

    def isEqual(self, obj: FreeCAD.Vector, tolerance: float = 0, /) -> bool:
        """
        isEqual(vector2, tol=0) -> bool

        Checks if the distance between the points represented by this vector
        and `vector2` is less or equal to the given tolerance.

        vector2 : Base.Vector
        tol : float
        """

    def isOnLineSegment(self, start, end, /) -> bool:
        """
        isOnLineSegment(vector1, vector2) -> bool

        Checks if this vector is on the line segment generated by `vector1` and `vector2`.

        vector1 : Base.Vector
        vector2 : Base.Vector
        Possible exceptions: (TypeError).
        """

    def multiply(self, factor: float, /) -> FreeCAD.Vector:
        """
        multiply(factor) -> Base.Vector

        Multiplies in-place each component of this vector by a single factor.
        Equivalent to scale(factor, factor, factor).

        factor : float
        """

    def negative(self) -> FreeCAD.Vector:
        """
        negative() -> Base.Vector

        Returns the negative (opposite) of this vector.
        """

    def normalize(self) -> FreeCAD.Vector:
        """
        normalize() -> Base.Vector

        Normalizes in-place this vector to the length of 1.0.
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def projectToLine(self, base, line, /) -> FreeCAD.Vector:
        """
        projectToLine(point, dir) -> Base.Vector

        Projects `point` on a line that goes through the origin with the direction `dir`.
        The result is the vector from `point` to the projected point.
        The operation is equivalent to dir_n.cross(dir_n.cross(point)), where `dir_n` is
        the vector `dir` normalized.
        The method modifies this vector instance according to result and does not
        depend on the vector itself.

        point : Base.Vector
        dir : Base.Vector
        Possible exceptions: (TypeError).
        """

    def projectToPlane(self, base, line, /) -> FreeCAD.Vector:
        """
        projectToPlane(base, normal) -> Base.Vector

        Projects in-place this vector on a plane defined by a base point
        represented by `base` and a normal defined by `normal`.

        base : Base.Vector
        normal : Base.Vector
        Possible exceptions: (TypeError).
        """

    def scale(self, factorX: float, factorY: float, factorZ: float, /) -> FreeCAD.Vector:
        """
        scale(x, y, z) -> Base.Vector

        Scales in-place this vector by the given factor in each component.

        x : float
            x-component factor scale.
        y : float
            y-component factor scale.
        z : float
            z-component factor scale.
        """

    def sub(self, obj: FreeCAD.Vector, /) -> FreeCAD.Vector:
        """
        sub(vector2) -> Base.Vector

        Returns the difference of this vector and `vector2`.

        vector2 : Base.Vector
        """

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Vector: ...

    def __radd__(self, other) -> Vector: ...

    def __sub__(self, other) -> Vector: ...

    def __rsub__(self, other) -> Vector: ...

    def __mul__(self, other): ...

    def __rmul__(self, other): ...

    def __mod__(self, other): ...

    def __rmod__(self, other): ...

    def __divmod__(self, other): ...

    def __rdivmod__(self, other): ...

    def __pow__(self, power, modulo=None): ...

    def __rpow__(self, power, modulo=None): ...

    def __neg__(self) -> Vector: ...

    def __pos__(self) -> Vector: ...

    def __abs__(self) -> Vector: ...

    def __bool__(self) -> bool: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rlshift__(self, other): ...

    def __rshift__(self, other): ...

    def __rrshift__(self, other): ...

    def __and__(self, other): ...

    def __rand__(self, other): ...

    def __xor__(self, other): ...

    def __rxor__(self, other): ...

    def __or__(self, other): ...

    def __ror__(self, other): ...

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...

    def __truediv__(self, other) -> Vector: ...

    def __rtruediv__(self, other) -> Vector: ...


# RotationPy.xml
class Rotation(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    Base.Rotation class.

    A Rotation using a quaternion.

    The following constructors are supported:

    Rotation()
    Empty constructor.

    Rotation(rotation)
    Copy constructor.

    Rotation(Axis, Radian)
    Rotation(Axis, Degree)
    Define from an axis and an angle (in radians or degrees according to the keyword).
    Axis : Base.Vector
    Radian : float
    Degree : float

    Rotation(vector_start, vector_end)
    Define from two vectors (rotation from/to vector).
    vector_start : Base.Vector
    vector_end : Base.Vector

    Rotation(angle1, angle2, angle3)
    Define from three floats (Euler angles) as yaw-pitch-roll in XY'Z'' convention.
    angle1 : float
    angle2 : float
    angle3 : float

    Rotation(seq, angle1, angle2, angle3)
    Define from one string and three floats (Euler angles) as Euler rotation
    of a given type. Call toEulerAngles() for supported sequence types.
    seq : str
    angle1 : float
    angle2 : float
    angle3 : float

    Rotation(x, y, z, w)
    Define from four floats (quaternion) where the quaternion is specified as:
    q = xi+yj+zk+w, i.e. the last parameter is the real part.
    x : float
    y : float
    z : float
    w : float

    Rotation(dir1, dir2, dir3, seq)
    Define from three vectors that define rotated axes directions plus an optional
    3-characher string of capital letters 'X', 'Y', 'Z' that sets the order of
    importance of the axes (e.g., 'ZXY' means z direction is followed strictly,
    x is used but corrected if necessary, y is ignored).
    dir1 : Base.Vector
    dir2 : Base.Vector
    dir3 : Base.Vector
    seq : str

    Rotation(matrix)
    Define from a matrix rotation in the 4D representation.
    matrix : Base.Matrix

    Rotation(*coef)
    Define from 16 or 9 elements which represent the rotation in the 4D matrix
    representation or in the 3D matrix representation, respectively.
    coef : sequence of float
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, a11: float = 1.0, a12: float = 0.0, a13: float = 0.0, a14: float = 0.0, a21: float = 0.0, a22: float = 1.0, a23: float = 0.0, a24: float = 0.0, a31: float = 0.0, a32: float = 0.0, a33: float = 1.0, a34: float = 0.0, a41: float = 0.0, a42: float = 0.0, a43: float = 0.0, a44: float = 1.0, /): ...

    @typing.overload
    def __init__(self, a11: float = 1.0, a12: float = 0.0, a13: float = 0.0, a21: float = 0.0, a22: float = 1.0, a23: float = 0.0, a31: float = 0.0, a32: float = 0.0, a33: float = 1.0, /): ...

    @typing.overload
    def __init__(self, o: FreeCAD.Rotation, /): ...

    @typing.overload
    def __init__(self, o: FreeCAD.Matrix, /): ...

    @typing.overload
    def __init__(self, v1: FreeCAD.Vector, v2: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, Axis: FreeCAD.Vector, Degree: float): ...

    @typing.overload
    def __init__(self, Axis: FreeCAD.Vector, Radian: float): ...

    @typing.overload
    def __init__(self, y: float, p: float, r: float, /): ...

    @typing.overload
    def __init__(self, v1: FreeCAD.Vector, v2: FreeCAD.Vector, v3: FreeCAD.Vector, priority: str = None, /): ...

    @typing.overload
    def __init__(self, q0: float, q1: float, q2: float, q3: float, /): ...

    @typing.overload
    def __init__(self, seq: str, a: float, b: float, c: float, /):
        """
        Base.Rotation class.

        A Rotation using a quaternion.

        The following constructors are supported:

        Rotation()
        Empty constructor.

        Rotation(rotation)
        Copy constructor.

        Rotation(Axis, Radian)
        Rotation(Axis, Degree)
        Define from an axis and an angle (in radians or degrees according to the keyword).
        Axis : Base.Vector
        Radian : float
        Degree : float

        Rotation(vector_start, vector_end)
        Define from two vectors (rotation from/to vector).
        vector_start : Base.Vector
        vector_end : Base.Vector

        Rotation(angle1, angle2, angle3)
        Define from three floats (Euler angles) as yaw-pitch-roll in XY'Z'' convention.
        angle1 : float
        angle2 : float
        angle3 : float

        Rotation(seq, angle1, angle2, angle3)
        Define from one string and three floats (Euler angles) as Euler rotation
        of a given type. Call toEulerAngles() for supported sequence types.
        seq : str
        angle1 : float
        angle2 : float
        angle3 : float

        Rotation(x, y, z, w)
        Define from four floats (quaternion) where the quaternion is specified as:
        q = xi+yj+zk+w, i.e. the last parameter is the real part.
        x : float
        y : float
        z : float
        w : float

        Rotation(dir1, dir2, dir3, seq)
        Define from three vectors that define rotated axes directions plus an optional
        3-characher string of capital letters 'X', 'Y', 'Z' that sets the order of
        importance of the axes (e.g., 'ZXY' means z direction is followed strictly,
        x is used but corrected if necessary, y is ignored).
        dir1 : Base.Vector
        dir2 : Base.Vector
        dir3 : Base.Vector
        seq : str

        Rotation(matrix)
        Define from a matrix rotation in the 4D representation.
        matrix : Base.Matrix

        Rotation(*coef)
        Define from 16 or 9 elements which represent the rotation in the 4D matrix
        representation or in the 3D matrix representation, respectively.
        coef : sequence of float
        Possible exceptions: (FreeCAD.Base.FreeCADError, TypeError).
        """

    @property
    def Angle(self) -> float:
        """The rotation angle of the quaternion."""

    @Angle.setter
    def Angle(self, value: float): ...

    @property
    def Axis(self) -> FreeCAD.Vector:
        """The rotation axis of the quaternion."""

    @Axis.setter
    def Axis(self, value: FreeCAD.Vector): ...

    @property
    def Q(self) -> tuple[float, float, float, float]:
        """The rotation elements (as quaternion)."""

    @Q.setter
    def Q(self, value: tuple[float, float, float, float]): ...

    @property
    def RawAxis(self) -> FreeCAD.Vector:
        """The rotation axis without normalization."""

    def getYawPitchRoll(self) -> tuple[float, float, float]:
        """
        getYawPitchRoll() -> tuple

        Get the Euler angles of this rotation as yaw-pitch-roll in XY'Z'' convention.
        The angles are given in degrees.
        """

    def invert(self):
        """
        invert() -> None

        Sets the rotation to its inverse.
        """

    def inverted(self) -> FreeCAD.Rotation:
        """
        inverted() -> Base.Rotation

        Returns the inverse of the rotation.
        """

    def isIdentity(self, tol: float = 0.0, /) -> bool:
        """
        isIdentity(tol=0) -> bool

        Returns True if the rotation equals the 4D identity matrix.
        tol : float
            Tolerance used to check for identity.
            If tol is negative or zero, no tolerance is used.
        """

    def isNull(self) -> bool:
        """
        isNull() -> bool

        Returns True if all values in the quaternion representation are zero.
        """

    def isSame(self, rot: FreeCAD.Rotation, tol: float = 0.0, /) -> bool:
        """
        isSame(rotation, tol=0) -> bool

        Checks if `rotation` perform the same transformation as this rotation.

        rotation : Base.Rotation
        tol : float
            Tolerance used to compare both rotations.
            If tol is negative or zero, no tolerance is used.
        """

    def multVec(self, obj: FreeCAD.Vector, /) -> FreeCAD.Vector:
        """
        multVec(vector) -> Base.Vector

        Compute the transformed vector using the rotation.

        vector : Base.Vector
            Vector to be transformed.
        """

    def multiply(self, rot: FreeCAD.Rotation, /) -> FreeCAD.Rotation:
        """
        multiply(rotation) -> Base.Rotation

        Right multiply this rotation with another rotation.

        rotation : Base.Rotation
            Rotation by which to multiply this rotation.
        """

    def setEulerAngles(self, seq: str, A: float, B: float, C: float, /):
        """
        setEulerAngles(seq, angle1, angle2, angle3) -> None

        Set the Euler angles in a given sequence for this rotation.
        The angles must be given in degrees.

        seq : str
            Euler sequence name. All possible values given by toEulerAngles().
        angle1 : float
        angle2 : float
        angle3 : float
        """

    def setYawPitchRoll(self, A: float, B: float, C: float, /):
        """
        setYawPitchRoll(angle1, angle2, angle3) -> None

        Set the Euler angles of this rotation as yaw-pitch-roll in XY'Z'' convention.

        angle1 : float
            Angle around yaw axis in degrees.
        angle2 : float
            Angle around pitch axis in degrees.
        angle3 : float
            Angle around roll axis in degrees.
        """

    def slerp(self, rot: FreeCAD.Rotation, t: float, /) -> FreeCAD.Rotation:
        """
        slerp(rotation2, t) -> Base.Rotation

        Spherical Linear Interpolation (SLERP) of this rotation and `rotation2`.

        t : float
            Parameter of the path. t=0 returns this rotation, t=1 returns `rotation2`.
        """

    def toEulerAngles(self, seq: str = None, /) -> list[str] | tuple[float, float, float]:
        """
        toEulerAngles(seq) -> list

        Get the Euler angles in a given sequence for this rotation.

        seq : str
            Euler sequence name. If not given, the function returns
            all possible values of `seq`. Optional.
        """

    def toMatrix(self) -> FreeCAD.Matrix:
        """
        toMatrix() -> Base.Matrix

        Convert the rotation to a 4D matrix representation.
        """

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Rotation: ...

    def __radd__(self, other) -> Rotation: ...

    def __sub__(self, other) -> Rotation: ...

    def __rsub__(self, other) -> Rotation: ...

    def __mul__(self, other): ...

    def __rmul__(self, other): ...

    def __mod__(self, other): ...

    def __rmod__(self, other): ...

    def __divmod__(self, other): ...

    def __rdivmod__(self, other): ...

    def __pow__(self, power, modulo=None): ...

    def __rpow__(self, power, modulo=None): ...

    def __neg__(self) -> Rotation: ...

    def __pos__(self) -> Rotation: ...

    def __abs__(self) -> Rotation: ...

    def __bool__(self) -> bool: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rlshift__(self, other): ...

    def __rshift__(self, other): ...

    def __rrshift__(self, other): ...

    def __and__(self, other): ...

    def __rand__(self, other): ...

    def __xor__(self, other): ...

    def __rxor__(self, other): ...

    def __or__(self, other): ...

    def __ror__(self, other): ...

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...

    def __truediv__(self, other) -> Rotation: ...

    def __rtruediv__(self, other) -> Rotation: ...


# PersistencePy.xml
class Persistence(FreeCAD.BaseClass):
    """
    Base.Persistence class.

    Class to dump and restore the content of an object.
    """

    @property
    def Content(self) -> str:
        """Content of the object in XML representation."""

    @property
    def MemSize(self) -> int:
        """Memory size of the object in bytes."""

    def dumpContent(self, Compression: int = 3):
        """
        dumpContent(Compression=3) -> bytearray

        Dumps the content of the object, both the XML representation and the additional
        data files required, into a byte representation.

        Compression : int
            Set the data compression level in the range [0,9]. Set to 0 for no compression.
        Possible exceptions: (NotImplementedError, IOError).
        """

    def restoreContent(self, buffer, /):
        """
        restoreContent(obj) -> None

        Restore the content of the object from a byte representation as stored by `dumpContent`.
        It could be restored from any Python object implementing the buffer protocol.

        obj : buffer
            Object with buffer protocol support.
        Possible exceptions: (TypeError, IOError).
        """


# PrecisionPy.xml
class Precision(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    This is the Precision class
    """

    @staticmethod
    def angular() -> float:
        """Returns the recommended precision value when checking the equality of two angles (given in radians)"""

    @staticmethod
    def approximation() -> float:
        """Returns the precision value in real space, frequently used by approximation algorithms"""

    @staticmethod
    def confusion() -> float:
        """Returns the recommended precision value when checking coincidence of two points in real space"""

    @staticmethod
    def infinite() -> float:
        """Returns a  big number that  can  be  considered as infinite"""

    @staticmethod
    def intersection() -> float:
        """Returns the precision value in real space, frequently used by intersection algorithms"""

    @staticmethod
    def isInfinite(v: float, /) -> bool:
        """Returns True if R may be considered as an infinite number"""

    @staticmethod
    def isNegativeInfinite(v: float, /) -> bool:
        """Returns True if R may  be considered as a negative infinite number"""

    @staticmethod
    def isPositiveInfinite(v: float, /) -> bool:
        """Returns True if R may  be considered as a positive infinite number"""

    @staticmethod
    @typing.overload
    def parametric(p: float, /) -> float: ...

    @staticmethod
    @typing.overload
    def parametric(p: float, t: float, /) -> float:
        """
        Convert a real space precision to a parametric space precision
        Possible exceptions: (ValueError).
        """

    @staticmethod
    def squareConfusion() -> float:
        """Returns square of confusion"""


# BoundBoxPy.xml
class BoundBox(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    Base.BoundBox class.

    This class represents a bounding box.
    A bounding box is a rectangular cuboid which is a way to describe outer
    boundaries and is obtained from a lot of 3D types.
    It is often used to check if a 3D entity lies in the range of another object.
    Checking for bounding interference first can save a lot of computing time!
    An invalid BoundBox is represented by inconsistent values at each direction:
    The maximum float value of the system at the minimum coordinates, and the
    opposite value at the maximum coordinates.

    The following constructors are supported:

    BoundBox()
    Empty constructor. Returns an invalid BoundBox.

    BoundBox(boundBox)
    Copy constructor.
    boundBox : Base.BoundBox

    BoundBox(xMin, yMin=0, zMin=0, xMax=0, yMax=0, zMax=0)
    Define from the minimum and maximum values at each direction.
    xMin : float
        Minimum value at x-coordinate.
    yMin : float
        Minimum value at y-coordinate.
    zMin : float
        Minimum value at z-coordinate.
    xMax : float
        Maximum value at x-coordinate.
    yMax : float
        Maximum value at y-coordinate.
    zMax : float
        Maximum value at z-coordinate.

    App.BoundBox(min, max)
    Define from two containers representing the minimum and maximum values of the
    coordinates in each direction.
    min : Base.Vector, tuple
        Minimum values of the coordinates.
    max : Base.Vector, tuple
        Maximum values of the coordinates.
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, xMin: float = 0.0, yMin: float = 0.0, zMin: float = 0.0, xMax: float = 0.0, yMax: float = 0.0, zMax: float = 0.0, /): ...

    @typing.overload
    def __init__(self, object1: FreeCAD.BoundBox, /): ...

    @typing.overload
    def __init__(self, object1: tuple, object2: tuple, /): ...

    @typing.overload
    def __init__(self, object1: FreeCAD.Vector, object2: FreeCAD.Vector, /):
        """
        Base.BoundBox class.

        This class represents a bounding box.
        A bounding box is a rectangular cuboid which is a way to describe outer
        boundaries and is obtained from a lot of 3D types.
        It is often used to check if a 3D entity lies in the range of another object.
        Checking for bounding interference first can save a lot of computing time!
        An invalid BoundBox is represented by inconsistent values at each direction:
        The maximum float value of the system at the minimum coordinates, and the
        opposite value at the maximum coordinates.

        The following constructors are supported:

        BoundBox()
        Empty constructor. Returns an invalid BoundBox.

        BoundBox(boundBox)
        Copy constructor.
        boundBox : Base.BoundBox

        BoundBox(xMin, yMin=0, zMin=0, xMax=0, yMax=0, zMax=0)
        Define from the minimum and maximum values at each direction.
        xMin : float
            Minimum value at x-coordinate.
        yMin : float
            Minimum value at y-coordinate.
        zMin : float
            Minimum value at z-coordinate.
        xMax : float
            Maximum value at x-coordinate.
        yMax : float
            Maximum value at y-coordinate.
        zMax : float
            Maximum value at z-coordinate.

        App.BoundBox(min, max)
        Define from two containers representing the minimum and maximum values of the
        coordinates in each direction.
        min : Base.Vector, tuple
            Minimum values of the coordinates.
        max : Base.Vector, tuple
            Maximum values of the coordinates.
        Possible exceptions: (TypeError).
        """

    @property
    def Center(self) -> FreeCAD.Vector:
        """Center point of the bounding box."""

    @property
    def DiagonalLength(self) -> float:
        """Diagonal length of the bounding box."""

    @property
    def XLength(self) -> float:
        """Length of the bounding box in x direction."""

    @property
    def XMax(self) -> float:
        """The maximum x boundary position."""

    @XMax.setter
    def XMax(self, value: float): ...

    @property
    def XMin(self) -> float:
        """The minimum x boundary position."""

    @XMin.setter
    def XMin(self, value: float): ...

    @property
    def YLength(self) -> float:
        """Length of the bounding box in y direction."""

    @property
    def YMax(self) -> float:
        """The maximum y boundary position."""

    @YMax.setter
    def YMax(self, value: float): ...

    @property
    def YMin(self) -> float:
        """The minimum y boundary position."""

    @YMin.setter
    def YMin(self, value: float): ...

    @property
    def ZLength(self) -> float:
        """Length of the bounding box in z direction."""

    @property
    def ZMax(self) -> float:
        """The maximum z boundary position."""

    @ZMax.setter
    def ZMax(self, value: float): ...

    @property
    def ZMin(self) -> float:
        """The minimum z boundary position."""

    @ZMin.setter
    def ZMin(self, value: float): ...

    @typing.overload
    def add(self, object: tuple, /): ...

    @typing.overload
    def add(self, object: FreeCAD.Vector, /): ...

    @typing.overload
    def add(self, object: FreeCAD.BoundBox, /): ...

    @typing.overload
    def add(self, x: float, y: float, z: float, /):
        """
        add(minMax) -> None
        add(x, y, z) -> None

        Increase the maximum values or decrease the minimum values of this BoundBox by
        replacing the current values with the given values, so the bounding box can grow
        but not shrink.

        minMax : Base.Vector, tuple
            Values to enlarge at each direction.
        x : float
            Value to enlarge at x-direction.
        y : float
            Value to enlarge at y-direction.
        z : float
            Value to enlarge at z-direction.
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def closestPoint(self, object: tuple, /) -> FreeCAD.Vector: ...

    @typing.overload
    def closestPoint(self, object: FreeCAD.Vector, /) -> FreeCAD.Vector: ...

    @typing.overload
    def closestPoint(self, x: float, y: float, z: float, /) -> FreeCAD.Vector:
        """
        closestPoint(point) -> Base.Vector
        closestPoint(x, y, z) -> Base.Vector

        Get the closest point of the bounding box to the given point.

        point : Base.Vector, tuple
            Coordinates of the given point.
        x : float
            X-coordinate of the given point.
        y : float
            Y-coordinate of the given point.
        z : float
            Z-coordinate of the given point.
        Possible exceptions: (TypeError).
        """

    def enlarge(self, s: float, /):
        """
        enlarge(variation) -> None

        Decrease the minimum values and increase the maximum values by the given value.
        A negative value shrinks the bounding box.

        variation : float
        """

    def getEdge(self, index: int, /) -> tuple[FreeCAD.Vector, FreeCAD.Vector]:
        """
        getEdge(index) -> tuple of Base.Vector

        Get the edge points of the given index.
        The index must be in the range of [0, 11].

        index : int
        """

    def getIntersectionPoint(self, object: FreeCAD.Vector, object2: FreeCAD.Vector, epsilon: float = 0.0001, /) -> FreeCAD.Vector:
        """
        getIntersectionPoint(base, dir, epsilon=0.0001) -> Base.Vector

        Calculate the intersection point of a line with the bounding box.
        The base point must lie inside the bounding box, if not an exception is thrown.

        base : Base.Vector
            Base point of the line.
        dir : Base.Vector
            Direction of the line.
        epsilon : float
            Bounding box size tolerance.
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def getPoint(self, index: int, /) -> FreeCAD.Vector:
        """
        getPoint(index) ->Base.Vector

        Get the point of the given index.
        The index must be in the range of [0, 7].

        index : int
        """

    @typing.overload
    def intersect(self, object: FreeCAD.BoundBox, /) -> bool: ...

    @typing.overload
    def intersect(self, object: FreeCAD.Vector, object2: FreeCAD.Vector, /) -> bool:
        """
        intersect(boundBox2) -> bool
        intersect(base, dir) -> bool

        Checks if the given object intersects with this bounding box. That can be
        another bounding box or a line specified by base and direction.

        boundBox2 : Base.BoundBox
        base : Base.Vector, tuple
        dir : Base.Vector, tuple
        Possible exceptions: (TypeError).
        """

    def intersected(self, object: FreeCAD.BoundBox, /) -> FreeCAD.BoundBox:
        """
        intersected(boundBox2) -> Base.BoundBox

        Returns the intersection of this and the given bounding box.

        boundBox2 : Base.BoundBox
        """

    def isCutPlane(self, object: FreeCAD.Vector, object2: FreeCAD.Vector, /) -> bool:
        """
        isCutPlane(base, normal) -> bool

        Check if the plane specified by base and normal intersects (cuts) this bounding
        box.

        base : Base.Vector
        normal : Base.Vector
        """

    @typing.overload
    def isInside(self, object: tuple, /) -> bool: ...

    @typing.overload
    def isInside(self, object: FreeCAD.Vector, /) -> bool: ...

    @typing.overload
    def isInside(self, object: FreeCAD.BoundBox, /) -> bool: ...

    @typing.overload
    def isInside(self, x: float, y: float, z: float, /) -> bool:
        """
        isInside(object) -> bool
        isInside(x, y, z) -> bool

        Check if a point or a bounding box is inside this bounding box.

        object : Base.Vector, Base.BoundBox
            Object to check if it is inside this bounding box.
        x : float
            X-coordinate of the point to check.
        y : float
            Y-coordinate of the point to check.
        z : float
            Z-coordinate of the point to check.
        Possible exceptions: (TypeError).
        """

    def isValid(self) -> bool:
        """
        isValid() -> bool

        Checks if the bounding box is valid.
        """

    @typing.overload
    def move(self, object: tuple, /): ...

    @typing.overload
    def move(self, object: FreeCAD.Vector, /): ...

    @typing.overload
    def move(self, x: float, y: float, z: float, /):
        """
        move(displacement) -> None
        move(x, y, z) -> None

        Move the bounding box by the given values.

        displacement : Base.Vector, tuple
            Displacement at each direction.
        x : float
            Displacement at x-direction.
        y : float
            Displacement at y-direction.
        z : float
            Displacement at z-direction.
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def scale(self, object: tuple, /): ...

    @typing.overload
    def scale(self, object: FreeCAD.Vector, /): ...

    @typing.overload
    def scale(self, x: float, y: float, z: float, /):
        """
        scale(factor) -> None
        scale(x, y, z) -> None

        Scale the bounding box by the given values.

        factor : Base.Vector, tuple
            Factor scale at each direction.
        x : float
            Scale at x-direction.
        y : float
            Scale at y-direction.
        z : float
            Scale at z-direction.
        Possible exceptions: (TypeError).
        """

    def setVoid(self):
        """
        setVoid() -> None

        Invalidate the bounding box.
        """

    def transformed(self, mat: FreeCAD.Matrix, /) -> FreeCAD.BoundBox:
        """
        transformed(matrix) -> Base.BoundBox

        Returns a new BoundBox containing the transformed rectangular cuboid
        represented by this BoundBox.

        matrix : Base.Matrix
            Transformation matrix.
        Possible exceptions: (FloatingPointError).
        """

    def united(self, object: FreeCAD.BoundBox, /) -> FreeCAD.BoundBox:
        """
        united(boundBox2) -> Base.BoundBox

        Returns the union of this and the given bounding box.

        boundBox2 : Base.BoundBox
        """


# PlacementPy.xml
class Placement(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    Base.Placement class.

    A Placement defines an orientation (rotation) and a position (base) in 3D space.
    It is used when no scaling or other distortion is needed.

    The following constructors are supported:

    Placement()
    Empty constructor.

    Placement(placement)
    Copy constructor.
    placement : Base.Placement

    Placement(matrix)
    Define from a 4D matrix consisting of rotation and translation.
    matrix : Base.Matrix

    Placement(base, rotation)
    Define from position and rotation.
    base : Base.Vector
    rotation : Base.Rotation

    Placement(base, rotation, center)
    Define from position and rotation with center.
    base : Base.Vector
    rotation : Base.Rotation
    center : Base.Vector

    Placement(base, axis, angle)
    define position and rotation.
    base : Base.Vector
    axis : Base.Vector
    angle : float
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, o: FreeCAD.Matrix, /): ...

    @typing.overload
    def __init__(self, o: FreeCAD.Placement, /): ...

    @typing.overload
    def __init__(self, o: FreeCAD.Vector, d: FreeCAD.Rotation, /): ...

    @typing.overload
    def __init__(self, o: FreeCAD.Vector, d: FreeCAD.Vector, angle: float, /): ...

    @typing.overload
    def __init__(self, o: FreeCAD.Vector, d: FreeCAD.Rotation, c: FreeCAD.Vector, /):
        """
        Base.Placement class.

        A Placement defines an orientation (rotation) and a position (base) in 3D space.
        It is used when no scaling or other distortion is needed.

        The following constructors are supported:

        Placement()
        Empty constructor.

        Placement(placement)
        Copy constructor.
        placement : Base.Placement

        Placement(matrix)
        Define from a 4D matrix consisting of rotation and translation.
        matrix : Base.Matrix

        Placement(base, rotation)
        Define from position and rotation.
        base : Base.Vector
        rotation : Base.Rotation

        Placement(base, rotation, center)
        Define from position and rotation with center.
        base : Base.Vector
        rotation : Base.Rotation
        center : Base.Vector

        Placement(base, axis, angle)
        define position and rotation.
        base : Base.Vector
        axis : Base.Vector
        angle : float
        Possible exceptions: (TypeError).
        """

    @property
    def Base(self) -> FreeCAD.Vector:
        """Vector to the Base Position of the Placement."""

    @Base.setter
    def Base(self, value: FreeCAD.Vector): ...

    @property
    def Matrix(self) -> FreeCAD.Matrix:
        """Set/get matrix representation of the placement."""

    @Matrix.setter
    def Matrix(self, value: FreeCAD.Matrix): ...

    @property
    def Rotation(self) -> FreeCAD.Rotation:
        """Orientation of the placement expressed as rotation."""

    @Rotation.setter
    def Rotation(self, value: FreeCAD.Rotation): ...

    def copy(self) -> FreeCAD.Placement:
        """
        copy() -> Base.Placement

        Returns a copy of this placement.
        """

    def inverse(self) -> FreeCAD.Placement:
        """
        inverse() -> Base.Placement

        Compute the inverse placement.
        """

    def isIdentity(self, tol: float = 0.0, /) -> bool:
        """
        isIdentity([tol=0.0]) -> bool

        Returns True if the placement has no displacement and no rotation.
        Matrix representation is the 4D identity matrix.
        tol : float
            Tolerance used to check for identity.
            If tol is negative or zero, no tolerance is used.
        """

    def isSame(self, plm: FreeCAD.Placement, tol: float = 0.0, /) -> bool:
        """
        isSame(Base.Placement, [tol=0.0]) -> bool

        Checks whether this and the given placement are the same.
        The default tolerance is set to 0.0
        """

    def move(self, vec: FreeCAD.Vector, /):
        """
        move(vector) -> None

        Move the placement along a vector.

        vector : Base.Vector
            Vector by which to move the placement.
        """

    def multVec(self, vec: FreeCAD.Vector, /) -> FreeCAD.Vector:
        """
        multVec(vector) -> Base.Vector

        Compute the transformed vector using the placement.

        vector : Base.Vector
            Vector to be transformed.
        """

    def multiply(self, plm: FreeCAD.Placement, /) -> FreeCAD.Placement:
        """
        multiply(placement) -> Base.Placement

        Right multiply this placement with another placement.
        Also available as `*` operator.

        placement : Base.Placement
            Placement by which to multiply this placement.
        """

    def pow(self, t: float, shorten: bool = True, /) -> FreeCAD.Placement:
        """
        pow(t, shorten=True) -> Base.Placement

        Raise this placement to real power using ScLERP interpolation.
        Also available as `**` operator.

        t : float
            Real power.
        shorten : bool
            If True, ensures rotation quaternion is net positive to make
            the path shorter.
        """

    @typing.overload
    def rotate(self, center: tuple[float, float, float], axis: tuple[float, float, float], angle: float, comp: bool = False): ...

    @typing.overload
    def rotate(self):
        """
        rotate(center, axis, angle, comp) -> None

        Rotate the current placement around center and axis with the given angle.
        This method is compatible with TopoShape.rotate() if the (optional) keyword
        argument comp is True (default=False).

        center : Base.Vector, sequence of float
            Rotation center.
        axis : Base.Vector, sequence of float
            Rotation axis.
        angle : float
            Rotation angle in degrees.
        comp : bool
            optional keyword only argument, if True (default=False),
        behave like TopoShape.rotate() (i.e. the resulting placements are interchangeable).
        """

    def sclerp(self, pyplm2: FreeCAD.Placement, t: float, shorten: bool = True, /) -> FreeCAD.Placement:
        """
        sclerp(placement2, t, shorten=True) -> Base.Placement

        Screw Linear Interpolation (ScLERP) between this placement and `placement2`.
        Interpolation is a continuous motion along a helical path parametrized by `t`
        made of equal transforms if discretized.
        If quaternions of rotations of the two placements differ in sign, the interpolation
        will take a long path.

        placement2 : Base.Placement
        t : float
            Parameter of helical path. t=0 returns this placement, t=1 returns
            `placement2`. t can also be outside of [0, 1] range for extrapolation.
        shorten : bool
            If True, the signs are harmonized before interpolation and the interpolation
            takes the shorter path.
        """

    def slerp(self, pyplm2: FreeCAD.Placement, t: float, /) -> FreeCAD.Placement:
        """
        slerp(placement2, t) -> Base.Placement

        Spherical Linear Interpolation (SLERP) between this placement and `placement2`.
        This function performs independent interpolation of rotation and movement.
        Result of such interpolation might be not what application expects, thus this tool
        might be considered for simple cases or for interpolating between small intervals.
        For more complex cases you better use the advanced sclerp() function.

        placement2 : Base.Placement
        t : float
            Parameter of the path. t=0 returns this placement, t=1 returns `placement2`.
        """

    def toMatrix(self) -> FreeCAD.Matrix:
        """
        toMatrix() -> Base.Matrix

        Compute the matrix representation of the placement.
        """

    @typing.overload
    def translate(self, vector, /): ...

    @typing.overload
    def translate(self):
        """
        translate(vector) -> None

        Alias to move(), to be compatible with TopoShape.translate().

        vector : Base.Vector
            Vector by which to move the placement.
        """

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Placement: ...

    def __radd__(self, other) -> Placement: ...

    def __sub__(self, other) -> Placement: ...

    def __rsub__(self, other) -> Placement: ...

    def __mul__(self, other): ...

    def __rmul__(self, other): ...

    def __mod__(self, other): ...

    def __rmod__(self, other): ...

    def __divmod__(self, other): ...

    def __rdivmod__(self, other): ...

    def __pow__(self, power, modulo=None): ...

    def __rpow__(self, power, modulo=None): ...

    def __neg__(self) -> Placement: ...

    def __pos__(self) -> Placement: ...

    def __abs__(self) -> Placement: ...

    def __bool__(self) -> bool: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rlshift__(self, other): ...

    def __rshift__(self, other): ...

    def __rrshift__(self, other): ...

    def __and__(self, other): ...

    def __rand__(self, other): ...

    def __xor__(self, other): ...

    def __rxor__(self, other): ...

    def __or__(self, other): ...

    def __ror__(self, other): ...

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...

    def __truediv__(self, other) -> Placement: ...

    def __rtruediv__(self, other) -> Placement: ...


# UnitPy.xml
class Unit(FreeCAD.PyObjectBase):
    """
    This class can be imported.

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
    def __init__(self, i1: int = 0, i2: int = 0, i3: int = 0, i4: int = 0, i5: int = 0, i6: int = 0, i7: int = 0, i8: int = 0, /): ...

    @typing.overload
    def __init__(self, object: FreeCAD.Quantity, /): ...

    @typing.overload
    def __init__(self, object: FreeCAD.Unit, /): ...

    @typing.overload
    def __init__(self, string: str, /):
        """
        Unit
         defines a unit type, calculate and compare.

         The following constructors are supported:
         Unit()                        -- empty constructor
         Unit(i1,i2,i3,i4,i5,i6,i7,i8) -- unit signature
         Unit(Quantity)                -- copy unit from Quantity
         Unit(Unit)                    -- copy constructor
         Unit(string)                  -- parse the string for units
        
        Possible exceptions: (ValueError, OverflowError, TypeError).
        """

    @property
    def Signature(self) -> tuple[int, int, int, int, int, int, int, int]:
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

    def __radd__(self, other) -> Unit: ...

    def __sub__(self, other) -> Unit: ...

    def __rsub__(self, other) -> Unit: ...

    def __mul__(self, other): ...

    def __rmul__(self, other): ...

    def __mod__(self, other): ...

    def __rmod__(self, other): ...

    def __divmod__(self, other): ...

    def __rdivmod__(self, other): ...

    def __pow__(self, power, modulo=None): ...

    def __rpow__(self, power, modulo=None): ...

    def __neg__(self) -> Unit: ...

    def __pos__(self) -> Unit: ...

    def __abs__(self) -> Unit: ...

    def __bool__(self) -> bool: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rlshift__(self, other): ...

    def __rshift__(self, other): ...

    def __rrshift__(self, other): ...

    def __and__(self, other): ...

    def __rand__(self, other): ...

    def __xor__(self, other): ...

    def __rxor__(self, other): ...

    def __or__(self, other): ...

    def __ror__(self, other): ...

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...

    def __truediv__(self, other) -> Unit: ...

    def __rtruediv__(self, other) -> Unit: ...


# QuantityPy.xml
class Quantity(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    Quantity
    defined by a value and a unit.

    The following constructors are supported:
    Quantity() -- empty constructor
    Quantity(Value) -- empty constructor
    Quantity(Value,Unit) -- empty constructor
    Quantity(Quantity) -- copy constructor
    Quantity(string) -- arbitrary mixture of numbers and chars defining a Quantity
    """

    @typing.overload
    def __init__(self, f: float = sys.float_info.max, object: FreeCAD.Unit = None, /): ...

    @typing.overload
    def __init__(self, f: float = sys.float_info.max, object: FreeCAD.Quantity = None, /): ...

    @typing.overload
    def __init__(self, f: float = sys.float_info.max, i1: int = 0, i2: int = 0, i3: int = 0, i4: int = 0, i5: int = 0, i6: int = 0, i7: int = 0, i8: int = 0, /): ...

    @typing.overload
    def __init__(self, f: float = sys.float_info.max, string: str = None, /): ...

    @typing.overload
    def __init__(self, object: FreeCAD.Quantity, /): ...

    @typing.overload
    def __init__(self, string: str, /):
        """
        Quantity
        defined by a value and a unit.

        The following constructors are supported:
        Quantity() -- empty constructor
        Quantity(Value) -- empty constructor
        Quantity(Value,Unit) -- empty constructor
        Quantity(Quantity) -- copy constructor
        Quantity(string) -- arbitrary mixture of numbers and chars defining a Quantity
        
        Possible exceptions: (TypeError, ValueError).
        """

    @property
    def Format(self) -> ReturnGetFormatDict:
        """Format of the Quantity"""

    @Format.setter
    def Format(self, value: dict): ...

    @property
    def Unit(self) -> FreeCAD.Unit:
        """Unit of the Quantity"""

    @Unit.setter
    def Unit(self, value: FreeCAD.Unit): ...

    @property
    def UserString(self) -> str:
        """Unit of the Quantity"""

    @property
    def Value(self) -> float:
        """Numeric Value of the Quantity (in internal system mm,kg,s)"""

    @Value.setter
    def Value(self, value: float): ...

    def __round__(self) -> FreeCAD.Quantity:
        """
        Return the Integral closest to x, rounding half toward even.
        When an argument is passed, work like built-in round(x, ndigits).
        """

    def getUserPreferred(self) -> tuple[str, float, str]:
        """returns a quantity with the translation factor and a string with the prevered unit"""

    @typing.overload
    def getValueAs(self, object: FreeCAD.Quantity, /) -> FreeCAD.Quantity: ...

    @typing.overload
    def getValueAs(self, object: FreeCAD.Unit, /) -> FreeCAD.Quantity: ...

    @typing.overload
    def getValueAs(self, f: float = sys.float_info.max, i1: int = 0, i2: int = 0, i3: int = 0, i4: int = 0, i5: int = 0, i6: int = 0, i7: int = 0, i8: int = 0, /) -> FreeCAD.Quantity: ...

    @typing.overload
    def getValueAs(self, string: str, /) -> FreeCAD.Quantity: ...

    @typing.overload
    def getValueAs(self, value: float, object: FreeCAD.Unit, /) -> FreeCAD.Quantity:
        """
        returns a floating point value as the provided unit

                  Following parameters are allowed:
                  getValueAs('m/s')  # unit string to parse
                  getValueAs(2.45,1) # translation value and unit signature
                  getValueAs(FreeCAD.Units.Pascal) # predefined standard units
                  getValueAs(Qantity('N/m^2')) # a quantity
                  getValueAs(Unit(0,1,0,0,0,0,0,0)) # a unit
        
        Possible exceptions: (TypeError, ValueError).
        """

    def toStr(self, prec: int = None, /) -> str:
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

    def __radd__(self, other) -> Quantity: ...

    def __sub__(self, other) -> Quantity: ...

    def __rsub__(self, other) -> Quantity: ...

    def __mul__(self, other): ...

    def __rmul__(self, other): ...

    def __mod__(self, other): ...

    def __rmod__(self, other): ...

    def __divmod__(self, other): ...

    def __rdivmod__(self, other): ...

    def __pow__(self, power, modulo=None): ...

    def __rpow__(self, power, modulo=None): ...

    def __neg__(self) -> Quantity: ...

    def __pos__(self) -> Quantity: ...

    def __abs__(self) -> Quantity: ...

    def __bool__(self) -> bool: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rlshift__(self, other): ...

    def __rshift__(self, other): ...

    def __rrshift__(self, other): ...

    def __and__(self, other): ...

    def __rand__(self, other): ...

    def __xor__(self, other): ...

    def __rxor__(self, other): ...

    def __or__(self, other): ...

    def __ror__(self, other): ...

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...

    def __truediv__(self, other) -> Quantity: ...

    def __rtruediv__(self, other) -> Quantity: ...


# BaseClassPy.xml
class BaseClass(FreeCAD.PyObjectBase):
    """This is the base class"""

    @property
    def Module(self) -> str:
        """Module in which this class is defined"""

    @property
    def TypeId(self) -> str:
        """Is the type of the FreeCAD object with module domain"""

    def getAllDerivedFrom(self) -> list[str]:
        """Returns all descendants"""

    def isDerivedFrom(self, name: str, /) -> bool:
        """Returns true if given type is a father"""


# MatrixPy.xml
class Matrix(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    Base.Matrix class.

    A 4x4 Matrix.
    In particular, this matrix can represent an affine transformation, that is,
    given a 3D vector `x`, apply the transformation y = M*x + b, where the matrix
    `M` is a linear map and the vector `b` is a translation.
    `y` can be obtained using a linear transformation represented by the 4x4 matrix
    `A` conformed by the augmented 3x4 matrix (M|b), augmented by row with
    (0,0,0,1), therefore: (y, 1) = A*(x, 1).

    The following constructors are supported:

    Matrix()
    Empty constructor.

    Matrix(matrix)
    Copy constructor.
    matrix : Base.Matrix.

    Matrix(*coef)
    Define from 16 coefficients of the 4x4 matrix.
    coef : sequence of float
        The sequence can have up to 16 elements which complete the matrix by rows.

    Matrix(vector1, vector2, vector3, vector4)
    Define from four 3D vectors which represent the columns of the 3x4 submatrix,
    useful to represent an affine transformation. The fourth row is made up by
    (0,0,0,1).
    vector1 : Base.Vector
    vector2 : Base.Vector
    vector3 : Base.Vector
    vector4 : Base.Vector
        Default to (0,0,0). Optional.
    """

    @typing.overload
    def __init__(self, a11: float = 1.0, a12: float = 0.0, a13: float = 0.0, a14: float = 0.0, a21: float = 0.0, a22: float = 1.0, a23: float = 0.0, a24: float = 0.0, a31: float = 0.0, a32: float = 0.0, a33: float = 1.0, a34: float = 0.0, a41: float = 0.0, a42: float = 0.0, a43: float = 0.0, a44: float = 1.0, /): ...

    @typing.overload
    def __init__(self, o: FreeCAD.Matrix, /): ...

    @typing.overload
    def __init__(self, o1: FreeCAD.Vector, o2: FreeCAD.Vector, o3: FreeCAD.Vector, o4: FreeCAD.Vector = None, /):
        """
        Base.Matrix class.

        A 4x4 Matrix.
        In particular, this matrix can represent an affine transformation, that is,
        given a 3D vector `x`, apply the transformation y = M*x + b, where the matrix
        `M` is a linear map and the vector `b` is a translation.
        `y` can be obtained using a linear transformation represented by the 4x4 matrix
        `A` conformed by the augmented 3x4 matrix (M|b), augmented by row with
        (0,0,0,1), therefore: (y, 1) = A*(x, 1).

        The following constructors are supported:

        Matrix()
        Empty constructor.

        Matrix(matrix)
        Copy constructor.
        matrix : Base.Matrix.

        Matrix(*coef)
        Define from 16 coefficients of the 4x4 matrix.
        coef : sequence of float
            The sequence can have up to 16 elements which complete the matrix by rows.

        Matrix(vector1, vector2, vector3, vector4)
        Define from four 3D vectors which represent the columns of the 3x4 submatrix,
        useful to represent an affine transformation. The fourth row is made up by
        (0,0,0,1).
        vector1 : Base.Vector
        vector2 : Base.Vector
        vector3 : Base.Vector
        vector4 : Base.Vector
            Default to (0,0,0). Optional.
        Possible exceptions: (TypeError).
        """

    @property
    def A(self) -> typing.Sequence:
        """The matrix elements."""

    @A.setter
    def A(self, value: typing.Sequence): ...

    @property
    def A11(self) -> float:
        """The (1,1) matrix element."""

    @A11.setter
    def A11(self, value: float): ...

    @property
    def A12(self) -> float:
        """The (1,2) matrix element."""

    @A12.setter
    def A12(self, value: float): ...

    @property
    def A13(self) -> float:
        """The (1,3) matrix element."""

    @A13.setter
    def A13(self, value: float): ...

    @property
    def A14(self) -> float:
        """The (1,4) matrix element."""

    @A14.setter
    def A14(self, value: float): ...

    @property
    def A21(self) -> float:
        """The (2,1) matrix element."""

    @A21.setter
    def A21(self, value: float): ...

    @property
    def A22(self) -> float:
        """The (2,2) matrix element."""

    @A22.setter
    def A22(self, value: float): ...

    @property
    def A23(self) -> float:
        """The (2,3) matrix element."""

    @A23.setter
    def A23(self, value: float): ...

    @property
    def A24(self) -> float:
        """The (2,4) matrix element."""

    @A24.setter
    def A24(self, value: float): ...

    @property
    def A31(self) -> float:
        """The (3,1) matrix element."""

    @A31.setter
    def A31(self, value: float): ...

    @property
    def A32(self) -> float:
        """The (3,2) matrix element."""

    @A32.setter
    def A32(self, value: float): ...

    @property
    def A33(self) -> float:
        """The (3,3) matrix element."""

    @A33.setter
    def A33(self, value: float): ...

    @property
    def A34(self) -> float:
        """The (3,4) matrix element."""

    @A34.setter
    def A34(self, value: float): ...

    @property
    def A41(self) -> float:
        """The (4,1) matrix element."""

    @A41.setter
    def A41(self, value: float): ...

    @property
    def A42(self) -> float:
        """The (4,2) matrix element."""

    @A42.setter
    def A42(self, value: float): ...

    @property
    def A43(self) -> float:
        """The (4,3) matrix element."""

    @A43.setter
    def A43(self, value: float): ...

    @property
    def A44(self) -> float:
        """The (4,4) matrix element."""

    @A44.setter
    def A44(self, value: float): ...

    def analyze(self) -> str:
        """
        analyze() -> str

        Analyzes the type of transformation.
        """

    def col(self, index: int, /) -> FreeCAD.Vector:
        """
        col(index) -> Base.Vector

        Return the vector of a column, that is, the vector generated by the three
        first elements of the specified column.

        index : int
            Required column index.
        Possible exceptions: (ValueError).
        """

    def determinant(self) -> float:
        """
        determinant() -> float

        Compute the determinant of the matrix.
        """

    def hasScale(self, tol: float = 0, /):
        """
        hasScale(tol=0) -> ScaleType

        Return an enum value of ScaleType. Possible values are:
        Uniform, NonUniformLeft, NonUniformRight, NoScaling or Other
        if it's not a scale matrix.

        tol : float
        """

    def inverse(self) -> FreeCAD.Matrix:
        """
        inverse() -> Base.Matrix

        Compute the inverse matrix, if possible.
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def invert(self):
        """
        invert() -> None

        Compute the inverse matrix in-place, if possible.
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def isNull(self) -> bool:
        """
        isNull() -> bool

        Check if this is the null matrix.
        """

    def isOrthogonal(self, eps: float = 1e-06, /) -> float:
        """
        isOrthogonal(tol=1e-6) -> float

        Checks if the matrix is orthogonal, i.e. M * M^T = k*I and returns
        the multiple of the identity matrix. If it's not orthogonal 0 is returned.

        tol : float
            Tolerance used to check orthogonality.
        """

    def isUnity(self) -> bool:
        """
        isUnity() -> bool

        Check if this is the unit matrix (4D identity matrix).
        """

    @typing.overload
    def move(self, pcVecObj: tuple, /): ...

    @typing.overload
    def move(self, pcVecObj: FreeCAD.Vector, /): ...

    @typing.overload
    def move(self, x: float, y: float, z: float, /):
        """
        move(vector) -> None
        move(x, y, z) -> None

        Move the matrix along a vector, equivalent to left multiply the matrix
        by a pure translation transformation.

        vector : Base.Vector, tuple
        x : float
            `x` translation.
        y : float
            `y` translation.
        z : float
            `z` translation.
        """

    def multVec(self, obj: FreeCAD.Vector, /) -> FreeCAD.Vector:
        """
        multVec(vector) -> Base.Vector

        Compute the transformed vector using the matrix.

        vector : Base.Vector
        """

    @typing.overload
    def multiply(self, o: FreeCAD.Matrix, /) -> FreeCAD.Matrix | FreeCAD.Vector: ...

    @typing.overload
    def multiply(self, o: FreeCAD.Vector, /) -> FreeCAD.Matrix | FreeCAD.Vector:
        """
        multiply(matrix) -> Base.Matrix
        multiply(vector) -> Base.Vector

        Right multiply the matrix by the given object.
        If the argument is a vector, this is augmented to the 4D vector (`vector`, 1).

        matrix : Base.Matrix
        vector : Base.Vector
        Possible exceptions: (TypeError).
        """

    def nullify(self):
        """
        nullify() -> None

        Make this the null matrix.
        """

    @typing.overload
    def rotateX(self, object: FreeCAD.Quantity, /): ...

    @typing.overload
    def rotateX(self, angle: float = 0, /):
        """
        rotateX(angle) -> None

        Rotate around X axis.

        angle : float
            Angle in radians.
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def rotateY(self, object: FreeCAD.Quantity, /): ...

    @typing.overload
    def rotateY(self, angle: float = 0, /):
        """
        rotateY(angle) -> None

        Rotate around Y axis.

        angle : float
            Angle in radians.
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def rotateZ(self, object: FreeCAD.Quantity, /): ...

    @typing.overload
    def rotateZ(self, angle: float = 0, /):
        """
        rotateZ(angle) -> None

        Rotate around Z axis.

        angle : float
            Angle in radians.
        Possible exceptions: (TypeError).
        """

    def row(self, index: int, /) -> FreeCAD.Vector:
        """
        row(index) -> Base.Vector

        Return the vector of a row, that is, the vector generated by the three
        first elements of the specified row.

        index : int
            Required row index.
        Possible exceptions: (ValueError).
        """

    @typing.overload
    def scale(self, x: float, /): ...

    @typing.overload
    def scale(self, pcVecObj: tuple, /): ...

    @typing.overload
    def scale(self, pcVecObj: FreeCAD.Vector, /): ...

    @typing.overload
    def scale(self, x: float, y: float, z: float, /):
        """
        scale(vector) -> None
        scale(x, y, z) -> None
        scale(factor) -> None

        Scale the first three rows of the matrix.

        vector : Base.Vector
        x : float
            First row factor scale.
        y : float
            Second row factor scale.
        z : float
            Third row factor scale.
        factor : float
            global factor scale.
        """

    def setCol(self, index: int, o: FreeCAD.Vector, /):
        """
        setCol(index, vector) -> None

        Set the vector of a column, that is, the three first elements of the specified
        column by index.

        index : int
            Required column index.
        vector : Base.Vector
        Possible exceptions: (ValueError).
        """

    def setRow(self, index: int, o: FreeCAD.Vector, /):
        """
        setRow(index, vector) -> None

        Set the vector of a row, that is, the three first elements of the specified
        row by index.

        index : int
            Required row index.
        vector : Base.Vector
        Possible exceptions: (ValueError).
        """

    def setTrace(self, o: FreeCAD.Vector, /):
        """
        setTrace(vector) -> None

        Set the diagonal of the 3x3 leading principal submatrix.

        vector : Base.Vector
        """

    def submatrix(self, dim: int, /) -> FreeCAD.Matrix:
        """
        submatrix(dim) -> Base.Matrix

        Get the leading principal submatrix of the given dimension.
        The (4 - `dim`) remaining dimensions are completed with the
        corresponding identity matrix.

        dim : int
            Dimension parameter must be in the range [1,4].
        Possible exceptions: (IndexError).
        """

    def trace(self) -> FreeCAD.Vector:
        """
        trace() -> Base.Vector

        Return the diagonal of the 3x3 leading principal submatrix as vector.
        """

    def transform(self, pcVecObj: FreeCAD.Vector, pcMatObj: FreeCAD.Matrix, /):
        """
        transform(vector, matrix2) -> None

        Transform the matrix around a given point.
        Equivalent to left multiply the matrix by T*M*T_inv, where M is `matrix2`, T the
        translation generated by `vector` and T_inv the inverse translation.
        For example, if `matrix2` is a rotation, the result is the transformation generated
        by the current matrix followed by a rotation around the point represented by `vector`.

        vector : Base.Vector
        matrix2 : Base.Matrix
        """

    def transpose(self):
        """
        transpose() -> None

        Transpose the matrix in-place.
        """

    def transposed(self) -> FreeCAD.Matrix:
        """
        transposed() -> Base.Matrix

        Returns a transposed copy of this matrix.
        """

    def unity(self):
        """
        unity() -> None

        Make this matrix to unity (4D identity matrix).
        """

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Matrix: ...

    def __radd__(self, other) -> Matrix: ...

    def __sub__(self, other) -> Matrix: ...

    def __rsub__(self, other) -> Matrix: ...

    def __mul__(self, other): ...

    def __rmul__(self, other): ...

    def __mod__(self, other): ...

    def __rmod__(self, other): ...

    def __divmod__(self, other): ...

    def __rdivmod__(self, other): ...

    def __pow__(self, power, modulo=None): ...

    def __rpow__(self, power, modulo=None): ...

    def __neg__(self) -> Matrix: ...

    def __pos__(self) -> Matrix: ...

    def __abs__(self) -> Matrix: ...

    def __bool__(self) -> bool: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rlshift__(self, other): ...

    def __rshift__(self, other): ...

    def __rrshift__(self, other): ...

    def __and__(self, other): ...

    def __rand__(self, other): ...

    def __xor__(self, other): ...

    def __rxor__(self, other): ...

    def __or__(self, other): ...

    def __ror__(self, other): ...

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...

    def __truediv__(self, other) -> Matrix: ...

    def __rtruediv__(self, other) -> Matrix: ...


# CoordinateSystemPy.xml
class CoordinateSystem(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    Base.CoordinateSystem class.

    An orthonormal right-handed coordinate system in 3D space.

    CoordinateSystem()
    Empty constructor.
    """

    def __init__(self):
        """
        Base.CoordinateSystem class.

        An orthonormal right-handed coordinate system in 3D space.

        CoordinateSystem()
        Empty constructor.
        """

    @property
    def Axis(self) -> FreeCAD.Axis:
        """Set or get axis."""

    @Axis.setter
    def Axis(self, value: FreeCAD.Axis): ...

    @property
    def Position(self) -> FreeCAD.Vector:
        """Set or get position."""

    @Position.setter
    def Position(self, value: FreeCAD.Vector): ...

    @property
    def XDirection(self) -> FreeCAD.Vector:
        """Set or get X-direction."""

    @XDirection.setter
    def XDirection(self, value: FreeCAD.Vector): ...

    @property
    def YDirection(self) -> FreeCAD.Vector:
        """Set or get Y-direction."""

    @YDirection.setter
    def YDirection(self, value: FreeCAD.Vector): ...

    @property
    def ZDirection(self) -> FreeCAD.Vector:
        """Set or get Z-direction."""

    @ZDirection.setter
    def ZDirection(self, value: FreeCAD.Vector): ...

    def displacement(self, cs: FreeCAD.CoordinateSystem, /) -> FreeCAD.Placement:
        """
        displacement(coordSystem2) -> Base.Placement

        Computes the placement from this to the passed coordinate system `coordSystem2`.

        coordSystem2 : Base.CoordinateSystem
        """

    @typing.overload
    def setAxes(self, axis: FreeCAD.Axis, xdir: FreeCAD.Vector, /): ...

    @typing.overload
    def setAxes(self, axis: FreeCAD.Vector, xdir: FreeCAD.Vector, /):
        """
        setAxes(axis, xDir) -> None

        Set axis or Z-direction, and X-direction.
        The X-direction is determined from the orthonormal compononent of `xDir`
        with respect to `axis` direction.

        axis : Base.Axis, Base.Vector
        xDir : Base.Vector
        Possible exceptions: (TypeError).
        """

    def setPlacement(self, plm: FreeCAD.Placement, /):
        """
        setPlacment(placement) -> None

        Set placement to the coordinate system.

        placement : Base.Placement
        """

    @typing.overload
    def transform(self, plm: FreeCAD.Placement, /): ...

    @typing.overload
    def transform(self, plm: FreeCAD.Rotation, /):
        """
        transform(trans) -> None

        Applies a transformation on this coordinate system.

        trans : Base.Rotation, Base.Placement
        Possible exceptions: (TypeError).
        """

    def transformTo(self, vec: FreeCAD.Vector, /) -> FreeCAD.Vector:
        """
        transformTo(vector) -> Base.Vector

        Computes the coordinates of the point in coordinates of this coordinate system.

        vector : Base.Vector
        """


# TypePy.xml
class TypeId(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    Base.BaseType class.

    This class is not intended to create instances of itself, but to get information
    from the different types and create instances of them.
    Regarding instantiation, this is possible in cases that inherit from the
    Base::BaseClass class and are not abstract classes.
    """

    @property
    def Key(self) -> int:
        """The key of the type id."""

    @property
    def Module(self) -> str:
        """Module in which this class is defined."""

    @property
    def Name(self) -> str:
        """The name of the type id."""

    def createInstance(self):
        """
        createInstance() -> object

        Creates an instance of this type id.
        """

    @staticmethod
    def createInstanceByName(name: str, load: bool = False, /) -> FreeCAD.BaseClass:
        """
        createInstanceByName(name, load=False) -> object

        Creates an instance of the named type id.

        name : str
        load : bool
            Load named type id module.
        """

    @staticmethod
    def fromKey(index: int, /) -> FreeCAD.TypeId:
        """
        fromKey(key) -> Base.BaseType

        Returns a type id object by key.

        key : int
        """

    @staticmethod
    def fromName(name: str, /) -> FreeCAD.TypeId:
        """
        fromName(name) -> Base.BaseType

        Returns a type object by name.

        name : str
        """

    def getAllDerived(self) -> list[FreeCAD.TypeId]:
        """
        getAllDerived() -> list

        Returns all descendants from this type id.
        """

    @staticmethod
    @typing.overload
    def getAllDerivedFrom(name: str, /) -> list[FreeCAD.TypeId]: ...

    @staticmethod
    @typing.overload
    def getAllDerivedFrom(t: FreeCAD.TypeId, /) -> list[FreeCAD.TypeId]:
        """
        getAllDerivedFrom(type) -> list

        Returns all descendants from the given type id.

        type : str, Base.BaseType
        Possible exceptions: (TypeError).
        """

    @staticmethod
    def getBadType() -> FreeCAD.TypeId:
        """
        getBadType() -> Base.BaseType

        Returns an invalid type id.
        """

    @staticmethod
    def getNumTypes() -> int:
        """
        getNumTypes() -> int

        Returns the number of type ids created so far.
        """

    def getParent(self) -> FreeCAD.TypeId:
        """
        getParent() -> Base.BaseType

        Returns the parent type id.
        """

    def isBad(self) -> bool:
        """
        isBad() -> bool

        Checks if the type id is invalid.
        """

    @typing.overload
    def isDerivedFrom(self, name: str, /) -> bool: ...

    @typing.overload
    def isDerivedFrom(self, t: FreeCAD.TypeId, /) -> bool:
        """
        isDerivedFrom(type) -> bool

        Returns true if given type id is a father of this type id.

        type : str, Base.BaseType
        Possible exceptions: (TypeError).
        """


# AxisPy.xml
class Axis(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    Base.Axis class.

    An Axis defines a direction and a position (base) in 3D space.

    The following constructors are supported:

    Axis()
    Empty constructor.

    Axis(axis)
    Copy constructor.
    axis : Base.Axis

    Axis(base, direction)
    Define from a position and a direction.
    base : Base.Vector
    direction : Base.Vector
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, o: FreeCAD.Axis, /): ...

    @typing.overload
    def __init__(self, o: FreeCAD.Vector, d: FreeCAD.Vector, /):
        """
        Base.Axis class.

        An Axis defines a direction and a position (base) in 3D space.

        The following constructors are supported:

        Axis()
        Empty constructor.

        Axis(axis)
        Copy constructor.
        axis : Base.Axis

        Axis(base, direction)
        Define from a position and a direction.
        base : Base.Vector
        direction : Base.Vector
        Possible exceptions: (TypeError).
        """

    @property
    def Base(self) -> FreeCAD.Vector:
        """Base position vector of the Axis."""

    @Base.setter
    def Base(self, value: FreeCAD.Vector): ...

    @property
    def Direction(self) -> FreeCAD.Vector:
        """Direction vector of the Axis."""

    @Direction.setter
    def Direction(self, value: FreeCAD.Vector): ...

    def copy(self) -> FreeCAD.Axis:
        """
        copy() -> Base.Axis

        Returns a copy of this Axis.
        """

    def move(self, vec: FreeCAD.Vector, /):
        """
        move(vector) -> None

        Move the axis base along the given vector.

        vector : Base.Vector
            Vector by which to move the axis.
        """

    def multiply(self, plm: FreeCAD.Placement, /) -> FreeCAD.Axis:
        """
        multiply(placement) -> Base.Axis

        Multiply this axis by a placement.

        placement : Base.Placement
            Placement by which to multiply the axis.
        """

    def reversed(self) -> FreeCAD.Axis:
        """
        reversed() -> Base.Axis

        Compute the reversed axis. This returns a new Base.Axis with
        the original direction reversed.
        """


# GeometryPyCXX.cpp
class Vector2d:
    """This class can be imported."""

    pass
