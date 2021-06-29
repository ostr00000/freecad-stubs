import typing

import FreeCAD
import Part


# ConstraintPy.xml
class Constraint(FreeCAD.Persistence):
    """With this object you can handle sketches"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: object, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: int, arg4: object, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: int, arg4: int, arg5: object, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: int, arg4: int, arg5: int, arg6: object, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: object, /):
        """With this object you can handle sketches"""

    @property
    def Driving(self) -> bool:
        """Driving Constraint"""

    @property
    def First(self) -> int:
        """First geometry index the Constraint refers to"""

    @First.setter
    def First(self, value: int): ...

    @property
    def FirstPos(self) -> int:
        """Position of first geometry index the Constraint refers to"""

    @property
    def InVirtualSpace(self) -> bool:
        """Constraint in virtual space"""

    @property
    def Name(self) -> str:
        """Name of the constraint"""

    @Name.setter
    def Name(self, value: str): ...

    @property
    def Second(self) -> int:
        """Second geometry index the Constraint refers to"""

    @Second.setter
    def Second(self, value: int): ...

    @property
    def SecondPos(self) -> int:
        """Position of second geometry index the Constraint refers to"""

    @property
    def Third(self) -> int:
        """Third geometry index the Constraint refers to"""

    @Third.setter
    def Third(self, value: int): ...

    @property
    def ThirdPos(self) -> int:
        """Position of third geometry index the Constraint refers to"""

    @property
    def Type(self) -> str:
        """Get the constraint type"""

    @property
    def Value(self) -> float:
        """Value of the Constraint"""


# SketchObjectSFPy.xml
class SketchObjectSF(Part.Part2DObject):
    """With this objects you can handle sketches"""


# SketchObjectPy.xml
class SketchObject(Part.Part2DObject):
    """With this objects you can handle sketches"""

    @property
    def AxisCount(self) -> int:
        """
                  Return the number of construction lines in the sketch which can be used as axes
                """

    @property
    def ConstraintCount(self) -> int:
        """Number of Constraints in this sketch"""

    @property
    def GeometryCount(self) -> int:
        """Number of geometric objects in this sketch"""

    @property
    def MissingLineEqualityConstraints(self) -> list:
        """
                        returns a list of (First FirstPos Second SecondPos) tuples with all the detected line segment equality constraints.
                    """

    @MissingLineEqualityConstraints.setter
    def MissingLineEqualityConstraints(self, value: list): ...

    @property
    def MissingPointOnPointConstraints(self) -> list:
        """
                        returns a list of (First FirstPos Second SecondPos Type) tuples with all the detected endpoint constraints.
                    """

    @MissingPointOnPointConstraints.setter
    def MissingPointOnPointConstraints(self, value: list): ...

    @property
    def MissingRadiusConstraints(self) -> list:
        """
                        returns a list of (First FirstPos Second SecondPos) tuples with all the detected radius constraints.
                    """

    @MissingRadiusConstraints.setter
    def MissingRadiusConstraints(self, value: list): ...

    @property
    def MissingVerticalHorizontalConstraints(self) -> list:
        """
                        returns a list of (First FirstPos Second SecondPos Type) tuples with all the detected vertical/horizontal constraints.
                    """

    @MissingVerticalHorizontalConstraints.setter
    def MissingVerticalHorizontalConstraints(self, value: list): ...

    @property
    def OpenVertices(self) -> list:
        """
                        returns a list of vertices positions.
                    """

    def DeleteUnusedInternalGeometry(self, arg1: int, /):
        """Deprecated -- use deleteUnusedInternalGeometry"""

    def ExposeInternalGeometry(self, arg1: int, /):
        """Deprecated -- use exposeInternalGeometry"""

    def addConstraint(self, arg1: object, /):
        """add a constraint to the sketch"""

    def addCopy(self, arg1: object, arg2: FreeCAD.Vector, arg3: bool = None, /):
        """add a copy of geometric objects to the sketch displaced by a vector3d"""

    def addExternal(self, arg1: str, arg2: str, /):
        """add a link to an external geometry to use it in a constraint"""

    @typing.overload
    def addGeometry(self, arg1: object, arg2: bool, /): ...

    @typing.overload
    def addGeometry(self, arg1: object, /):
        """add a geometric object to the sketch"""

    def addMove(self, arg1: object, arg2: FreeCAD.Vector, /):
        """Moves the geometric objects in the sketch displaced by a vector3d"""

    def addRectangularArray(self, arg1: object, arg2: FreeCAD.Vector, arg3: bool, arg4: int, arg5: int, arg6: bool = None, arg7: float = None, /):
        """add an array of size cols by rows where each element is a copy of the selected geometric objects displaced by a vector3d in the cols direction and by a vector perpendicular to it in the rows direction"""

    def addSymmetric(self, arg1: object, arg2: int, arg3: int = None, /):
        """add a symmetric geometric objects to the sketch with respect to a reference point or line"""

    def analyseMissingPointOnPointCoincident(self, arg1: float = None, /):
        """
                        Analyses the already detected Missing Point On Point Constraints to detect endpoint tagency/perpendicular.
                        The result may be retrieved or applied using the corresponding Get / Make methods.
                    """

    def autoRemoveRedundants(self, arg1: bool = None, /):
        """
                        Removes constraints currently detected as redundant by the solver. If the argument is True, then the geometry is updated after solving.
                    """

    def autoconstraint(self, arg1: float = None, arg2: float = None, arg3: bool = None, /):
        """
                        Automatic sketch constraining algorithm.
                    """

    def calculateAngleViaPoint(self, GeoId1: int, GeoId2: int, px: float, py: float, /):
        """
                  calculateAngleViaPoint(GeoId1, GeoId2, px, py) - calculates angle between
                  curves identified by GeoId1 and GeoId2 at point (x,y). The point must be
                  on intersection of the curves, otherwise the result may be useless (except
                  line-to-line, where (0,0) is OK). Returned value is in radians.
                """

    def calculateConstraintError(self, index: int, /):
        """
                  calculateConstraintError(index) - calculates the error function of the
                  constraint identified by its index and returns the signed error value.
                  The error value roughly corresponds to by how much the constraint is
                  violated. If the constraint internally has more than one error function,
                  the returned value is RMS of all errors (sign is lost in this case).
                """

    def carbonCopy(self, arg1: str, arg2: bool = None, /):
        """copy another sketch's geometry and constraints"""

    def changeConstraintsLocking(self, bLock: int, /):
        """
                  changeConstraintsLocking(bLock) - locks or unlocks all tangent and
                  perpendicular constraints. (Constraint locking prevents it from
                  flipping to another valid configuration, when e.g. external geometry
                  is updated from outside.) The sketch solve is not triggered by the
                  function, but the SketchObject is touched (a recompute will be
                  necessary). The geometry should not be affected by the function.

                  The bLock argument specifies, what to do. If true, all constraints
                  are unlocked and locked again. If false, all tangent and perp.
                  constraints are unlocked.
                """

    def convertToNURBS(self, arg1: int, /):
        """Approximates the given geometry with a B-Spline"""

    def delConstraint(self, arg1: int, /):
        """delete a constraint from the sketch"""

    def delConstraintOnPoint(self, arg1: int, arg2: int = None, /):
        """delete coincident constraints associated with a sketch point"""

    def delExternal(self, arg1: int, /):
        """delete a external geometry link from the sketch"""

    def delGeometry(self, arg1: int, /):
        """delete a geometric object from the sketch"""

    def deleteAllConstraints(self):
        """delete all the constraints from the sketch"""

    def deleteAllGeometry(self):
        """delete all the geometry objects and constraints from the sketch except external geometry"""

    def deleteUnusedInternalGeometry(self, arg1: int, /):
        """Deletes all unused (not further constrained) internal geometry"""

    def detectMissingEqualityConstraints(self, arg1: float = None, /):
        """
                        Detects Missing Equality Constraints. The Detect step just identifies possible missing constraints.
                        The result may be retrieved or applied using the corresponding Get / Make methods.
                    """

    def detectMissingPointOnPointConstraints(self, arg1: float = None, arg2: bool = None, /):
        """
                        Detects Missing Point On Point Constraints. The Detect step just identifies possible missing constraints.
                        The result may be retrieved or applied using the corresponding Get / Make methods.
                    """

    def detectMissingVerticalHorizontalConstraints(self, arg1: float = None, /):
        """
                        Detects Missing Horizontal/Vertical Constraints. The Detect step just identifies possible missing constraints.
                        The result may be retrieved or applied using the corresponding Get / Make methods.
                    """

    def exposeInternalGeometry(self, arg1: int, /):
        """Exposes all internal geometry of an object supporting internal geometry"""

    def extend(self, arg1: int, arg2: float, arg3: int, /):
        """extend a curve to new start and end positions"""

    @typing.overload
    def fillet(self, arg1: int, arg2: int, arg3: FreeCAD.Vector, arg4: FreeCAD.Vector, arg5: float, arg6: int = None, /): ...

    @typing.overload
    def fillet(self, arg1: int, arg2: int, arg3: float, arg4: int = None, /):
        """create fillet between two edges or at a point"""

    def getAxis(self, arg1: int, /):
        """
                  return an axis based on the corresponding construction line
                """

    @typing.overload
    def getDatum(self, arg1: int, /): ...

    @typing.overload
    def getDatum(self, arg1: str, /):
        """Get the value of a datum constraint"""

    def getDriving(self, arg1: int, /):
        """Get the Driving status of a datum constraint"""

    def getGeometryWithDependentParameters(self):
        """
                        getGeometryWithDependentParameters - returns a list of geoid posid pairs
                        with all the geometry element edges and vertices which the solver regards
                        as being dependent on other parameters.
                    """

    def getPoint(self, GeoIndex: int, PointPos: int, /):
        """
                  getPoint(GeoIndex,PointPos) - retrieve the vector of a point in the sketch
                """

    def getVirtualSpace(self, arg1: int, /):
        """Get the VirtualSpace status of a constraint"""

    def increaseBSplineDegree(self, arg1: int, arg2: int = None, /):
        """Increases the given BSpline Degree by a number of degrees"""

    def isPointOnCurve(self, arg1: int, arg2: float, arg3: float, /):
        """
                  isPointOnObject(GeoIdCurve, float x, float y) - tests if the point (x,y)
                  geometrically lies on a curve (e.g. ellipse). It treats lines as infinite,
                  arcs as full circles/ellipses/etc. Returns boolean value.
                """

    def makeMissingEquality(self, arg1: bool = None, /):
        """
                        Applies the detected / set Equality constraints. If the argument is True, then solving and redundant removal is done after each individual addition.
                    """

    def makeMissingPointOnPointCoincident(self, arg1: bool = None, /):
        """
                        Applies the detected / set Point On Point coincident constraints. If the argument is True, then solving and redundant removal is done after each individual addition.
                    """

    def makeMissingVerticalHorizontal(self, arg1: bool = None, /):
        """
                        Applies the detected / set Vertical/Horizontal constraints. If the argument is True, then solving and redundant removal is done after each individual addition.
                    """

    def modifyBSplineKnotMultiplicity(self, arg1: int, arg2: int, arg3: int = None, /):
        """Increases or reduces the given BSpline knot multiplicity"""

    def moveDatumsToEnd(self):
        """Moves all datum constraints to the end of the constraint list"""

    def movePoint(self, GeoIndex: int, PointPos: int, Vector: FreeCAD.Vector, relative: int = None, /):
        """
                  movePoint(GeoIndex,PointPos,Vector,[relative]) - move a given point (or curve)
                  to another location.
                  It moves the specified point (or curve) to the given location by adding some
                  temporary weak constraints and solve the sketch.
                  This method is mostly used to allow the user to drag some portions of the sketch
                  in real time by e.g. the mouse and it works only for underconstrained portions of
                  the sketch.
                  The argument 'relative', if present, states if the new location is given
                  relatively to the current one.
                """

    def renameConstraint(self, arg1: int, arg2: str, /):
        """Rename a constraint of the sketch"""

    def setConstruction(self, arg1: int, arg2: bool, /):
        """set construction mode of a geometry on or off"""

    @typing.overload
    def setDatum(self, arg1: int, arg2: FreeCAD.Quantity, /): ...

    @typing.overload
    def setDatum(self, arg1: int, arg2: float, /): ...

    @typing.overload
    def setDatum(self, arg1: str, arg2: FreeCAD.Quantity, /): ...

    @typing.overload
    def setDatum(self, arg1: str, arg2: float, /):
        """set the Datum of a Distance or Angle constraint"""

    def setDatumsDriving(self, arg1: bool, /):
        """set the Driving status of datum constraints"""

    def setDriving(self, arg1: int, arg2: bool, /):
        """set the Driving status of a datum constraint"""

    def setVirtualSpace(self, arg1: int, arg2: bool, /):
        """set the VirtualSpace status of a constraint"""

    def solve(self):
        """solve the actual set of geometry and constraints"""

    def toggleConstruction(self, arg1: int, /):
        """switch a geometry to a construction line"""

    def toggleDriving(self, arg1: int, /):
        """toggle the Driving status of a datum constraint"""

    def toggleVirtualSpace(self, arg1: int, /):
        """toggle the VirtualSpace status of a constraint"""

    def trim(self, arg1: int, arg2: FreeCAD.Vector, /):
        """trim a curve with a given id at a given reference point"""


# SketchPy.xml
class Sketch(FreeCAD.Persistence):
    """With this objects you can handle constraint sketches"""

    @property
    def Conflicts(self) -> tuple:
        """Tuple of conflicting constraints"""

    @property
    def Constraint(self) -> int:
        """0: exactly constraint, -1 under-constraint, 1 over-constraint"""

    @property
    def Geometries(self) -> tuple:
        """Tuple of all geometric elements in this sketch"""

    @property
    def Redundancies(self) -> tuple:
        """Tuple of redundant constraints"""

    @property
    def Shape(self) -> object:
        """Resulting shape from the sketch geometry"""

    def addConstraint(self, arg1: object, /):
        """add an constraint object to the sketch"""

    def addGeometry(self, arg1: object, /):
        """add a geometric object to the sketch"""

    def clear(self):
        """clear the sketch"""

    def movePoint(self, GeoIndex: int, PointPos: int, Vector: FreeCAD.Vector, relative: int = None, /):
        """
                  movePoint(GeoIndex,PointPos,Vector,[relative]) - move a given point (or curve)
                  to another location.
                  It moves the specified point (or curve) to the given location by adding some
                  temporary weak constraints and solve the sketch.
                  This method is mostly used to allow the user to drag some portions of the sketch
                  in real time by e.g. the mouse and it works only for underconstrained portions of
                  the sketch.
                  The argument 'relative', if present, states if the new location is given
                  relatively to the current one.
                """

    def solve(self):
        """solve the actual set of geometry and constraints"""


# AppSketcherPy.cpp
def open(arg1: str, /): ...


def insert(arg1: str, arg2: str, /): ...
