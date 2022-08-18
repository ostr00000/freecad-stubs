import io
import typing

import FreeCAD
import Part as PartModule
import Sketcher

StrIO_t: typing.TypeAlias = str | bytes | io.IOBase
DocAndStr_t: typing.TypeAlias = tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]
LinkSub_t: typing.TypeAlias = FreeCAD.DocumentObject | None | tuple[()] | DocAndStr_t
LinkList_t: typing.TypeAlias = None | FreeCAD.DocumentObject
SequenceDoc_t: typing.TypeAlias = tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]
LinkSubList_t: typing.TypeAlias = typing.Sequence[SequenceDoc_t | FreeCAD.DocumentObject]


# SketchGeometryExtensionPy.xml
class SketchGeometryExtension(PartModule.GeometryExtension):
    """
    This class can be imported.
    Describes a SketchGeometryExtension
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: int, /):
        """
        Describes a SketchGeometryExtension
        Possible exceptions: (TypeError).
        """

    @property
    def Blocked(self) -> bool:
        """Sets/returns whether the geometry is blocked or not."""

    @Blocked.setter
    def Blocked(self, value: bool): ...

    @property
    def Construction(self) -> bool:
        """Sets/returns this geometry as a construction one, which will not be part of a later built shape."""

    @Construction.setter
    def Construction(self, value: bool): ...

    @property
    def GeometryLayerId(self) -> int:
        """Returns the Id of the geometry Layer in which the geometry is located."""

    @GeometryLayerId.setter
    def GeometryLayerId(self, value: int): ...

    @property
    def Id(self) -> int:
        """Returns the Id of the SketchGeometryExtension."""

    @Id.setter
    def Id(self, value: int): ...

    @property
    def InternalType(self) -> str:
        """Returns the Id of the SketchGeometryExtension."""

    @InternalType.setter
    def InternalType(self, value: str): ...

    def setGeometryMode(self, arg1: str, arg2: bool = None, /):
        """
        Sets the given bit to true/false.
        Possible exceptions: (TypeError).
        """

    def testGeometryMode(self, arg1: str, /) -> bool:
        """
        Returns a boolean indicating whether the given bit is set.
        Possible exceptions: (TypeError).
        """


# ConstraintPy.xml
class Constraint(FreeCAD.Persistence):
    """
    This class can be imported.
    With this object you can handle sketches
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: int, arg4, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: int, arg4: int, arg5, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: int, arg4: int, arg5: int, arg6, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7, /):
        """
        With this object you can handle sketches
        Possible exceptions: (TypeError).
        """

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

    @FirstPos.setter
    def FirstPos(self, value: int): ...

    @property
    def InVirtualSpace(self) -> bool:
        """Constraint in virtual space"""

    @property
    def IsActive(self) -> bool:
        """Returns whether the constraint active (enforced) or not"""

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

    @SecondPos.setter
    def SecondPos(self, value: int): ...

    @property
    def Third(self) -> int:
        """Third geometry index the Constraint refers to"""

    @Third.setter
    def Third(self, value: int): ...

    @property
    def ThirdPos(self) -> int:
        """Position of third geometry index the Constraint refers to"""

    @ThirdPos.setter
    def ThirdPos(self, value: int): ...

    @property
    def Type(self) -> str:
        """Get the constraint type"""

    @property
    def Value(self) -> float:
        """Value of the Constraint"""


# SketchObjectSFPy.xml
class SketchObjectSF(PartModule.Part2DObject):
    """With this objects you can handle sketches"""

    @property
    def SketchFlatFile(self) -> str:
        """
        Property TypeId: App::PropertyFileIncluded.
        SketchFlat file (*.skf) which defines this sketch.
        """

    @SketchFlatFile.setter
    def SketchFlatFile(self, value: StrIO_t | tuple[StrIO_t, StrIO_t]): ...


# SketchObjectPy.xml
class SketchObject(PartModule.Part2DObject):
    """With this objects you can handle sketches"""

    @property
    def AxisCount(self) -> int:
        """Return the number of construction lines in the sketch which can be used as axes"""

    @property
    def ConstraintCount(self) -> int:
        """Number of Constraints in this sketch"""

    @property
    def GeometryCount(self) -> int:
        """Number of geometric objects in this sketch"""

    @property
    def GeometryFacadeList(self) -> list[Sketcher.GeometryFacade]:
        """Return a list of GeometryFacade objects corresponding to the PropertyGeometryList"""

    @GeometryFacadeList.setter
    def GeometryFacadeList(self, value: list): ...

    @property
    def MissingLineEqualityConstraints(self) -> list[tuple[int, int, int, int]]:
        """returns a list of (First FirstPos Second SecondPos) tuples with all the detected line segment equality constraints."""

    @MissingLineEqualityConstraints.setter
    def MissingLineEqualityConstraints(self, value: list): ...

    @property
    def MissingPointOnPointConstraints(self) -> list[tuple[int, int, int, int, int]]:
        """returns a list of (First FirstPos Second SecondPos Type) tuples with all the detected endpoint constraints."""

    @MissingPointOnPointConstraints.setter
    def MissingPointOnPointConstraints(self, value: list): ...

    @property
    def MissingRadiusConstraints(self) -> list[tuple[int, int, int, int]]:
        """returns a list of (First FirstPos Second SecondPos) tuples with all the detected radius constraints."""

    @MissingRadiusConstraints.setter
    def MissingRadiusConstraints(self, value: list): ...

    @property
    def MissingVerticalHorizontalConstraints(self) -> list[tuple[int, int, int, int, int]]:
        """returns a list of (First FirstPos Second SecondPos Type) tuples with all the detected vertical/horizontal constraints."""

    @MissingVerticalHorizontalConstraints.setter
    def MissingVerticalHorizontalConstraints(self, value: list): ...

    @property
    def OpenVertices(self) -> list[tuple[float, float, float]]:
        """returns a list of vertices positions."""

    @property
    def Constraints(self) -> list[Sketcher.Constraint]:
        """
        Property group: Sketch.
        Property TypeId: Sketcher::PropertyConstraintList.
        Sketch constraints.
        """

    @Constraints.setter
    def Constraints(self, value: typing.Iterable[Sketcher.Constraint] | dict[int, Sketcher.Constraint]): ...

    @property
    def ExternalGeometry(self) -> list[tuple[FreeCAD.DocumentObject, list[str]]]:
        """
        Property group: Sketch.
        Property TypeId: App::PropertyLinkSubList.
        Sketch external geometry.
        """

    @ExternalGeometry.setter
    def ExternalGeometry(self, value: LinkSub_t | LinkList_t | LinkSubList_t): ...

    @property
    def FullyConstrained(self) -> bool:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Hidden] Property won't appear in the editor.
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Sketch.
        Property TypeId: App::PropertyBool.
        Sketch is fully constrained.
        """

    @property
    def Geometry(self) -> list[PartModule.Geometry]:
        """
        Property group: Sketch.
        Property TypeId: Part::PropertyGeometryList.
        Sketch geometry.
        """

    @Geometry.setter
    def Geometry(self, value: typing.Iterable[PartModule.Geometry] | dict[int, PartModule.Geometry]): ...

    def DeleteUnusedInternalGeometry(self, arg1: int, /):
        """
        Deprecated -- use deleteUnusedInternalGeometry
        Possible exceptions: (ValueError).
        """

    def ExposeInternalGeometry(self, arg1: int, /):
        """
        Deprecated -- use exposeInternalGeometry
        Possible exceptions: (ValueError).
        """

    def addConstraint(self, arg1, /) -> int | tuple[int, ...]:
        """
        add a constraint to the sketch
        Possible exceptions: (TypeError, IndexError).
        """

    def addCopy(self, arg1, arg2: FreeCAD.Vector, arg3: bool = None, /) -> tuple[int, ...]:
        """
        add a copy of geometric objects to the sketch displaced by a vector3d
        Possible exceptions: (TypeError, ValueError).
        """

    def addExternal(self, arg1: str, arg2: str, /):
        """
        add a link to an external geometry to use it in a constraint
        Possible exceptions: (ValueError).
        """

    @typing.overload
    def addGeometry(self, arg1, arg2: bool, /) -> int | tuple[int, ...]: ...

    @typing.overload
    def addGeometry(self, arg1, /) -> int | tuple[int, ...]:
        """
        add a geometric object to the sketch
        Possible exceptions: (TypeError).
        """

    def addMove(self, arg1, arg2: FreeCAD.Vector, /):
        """
        Moves the geometric objects in the sketch displaced by a vector3d
        Possible exceptions: (TypeError).
        """

    def addRectangularArray(self, arg1, arg2: FreeCAD.Vector, arg3: bool, arg4: int, arg5: int, arg6: bool = None, arg7: float = None, /):
        """
        add an array of size cols by rows where each element is a copy of the selected geometric objects displaced by a vector3d in the cols direction and by a vector perpendicular to it in the rows direction
        Possible exceptions: (TypeError, ValueError).
        """

    def addSymmetric(self, arg1, arg2: int, arg3: int = None, /) -> tuple[int, ...]:
        """
        add a symmetric geometric objects to the sketch with respect to a reference point or line
        Possible exceptions: (TypeError).
        """

    def analyseMissingPointOnPointCoincident(self, arg1: float = None, /):
        """
        Analyses the already detected Missing Point On Point Constraints to detect endpoint tagency/perpendicular.
                        The result may be retrieved or applied using the corresponding Get / Make methods.
        """

    def autoRemoveRedundants(self, arg1: bool = None, /):
        """Removes constraints currently detected as redundant by the solver. If the argument is True, then the geometry is updated after solving."""

    def autoconstraint(self, arg1: float = None, arg2: float = None, arg3: bool = None, /):
        """
        Automatic sketch constraining algorithm.
            
        Possible exceptions: (ValueError).
        """

    def calculateAngleViaPoint(self, GeoId1: int, GeoId2: int, px: float, py: float, /) -> float:
        """
        calculateAngleViaPoint(GeoId1, GeoId2, px, py) - calculates angle between
                  curves identified by GeoId1 and GeoId2 at point (x,y). The point must be
                  on intersection of the curves, otherwise the result may be useless (except
                  line-to-line, where (0,0) is OK). Returned value is in radians.
        
        Possible exceptions: (ValueError).
        """

    def calculateConstraintError(self, index: int, /) -> float:
        """
        calculateConstraintError(index) - calculates the error function of the
                  constraint identified by its index and returns the signed error value.
                  The error value roughly corresponds to by how much the constraint is
                  violated. If the constraint internally has more than one error function,
                  the returned value is RMS of all errors (sign is lost in this case).
        
        Possible exceptions: (ValueError).
        """

    def carbonCopy(self, arg1: str, arg2: bool = None, /):
        """
        copy another sketch's geometry and constraints
        Possible exceptions: (ValueError).
        """

    def changeConstraintsLocking(self, bLock: int, /) -> int:
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
        """
        Approximates the given geometry with a B-Spline
        Possible exceptions: (ValueError).
        """

    def decreaseBSplineDegree(self, arg1: int, arg2: int = None, /) -> bool:
        """Decreases the given BSpline Degree by a number of degrees by approximating this curve"""

    def delConstraint(self, arg1: int, /):
        """
        delete a constraint from the sketch
        Possible exceptions: (ValueError).
        """

    def delConstraintOnPoint(self, arg1: int, arg2: int = None, /):
        """
        delete coincident constraints associated with a sketch point
        Possible exceptions: (ValueError).
        """

    def delExternal(self, arg1: int, /):
        """
        delete a external geometry link from the sketch
        Possible exceptions: (ValueError).
        """

    def delGeometries(self, arg1, /):
        """
        delete a list of geometric objects from the sketch, including any internal alignment geometry thereof
        Possible exceptions: (TypeError, ValueError).
        """

    def delGeometry(self, arg1: int, /):
        """
        delete a geometric object from the sketch
        Possible exceptions: (ValueError).
        """

    def deleteAllConstraints(self):
        """
        delete all the constraints from the sketch
        Possible exceptions: (ValueError).
        """

    def deleteAllGeometry(self):
        """
        delete all the geometry objects and constraints from the sketch except external geometry
        Possible exceptions: (ValueError).
        """

    def deleteUnusedInternalGeometry(self, arg1: int, /):
        """
        Deletes all unused (not further constrained) internal geometry
        Possible exceptions: (ValueError).
        """

    def detectMissingEqualityConstraints(self, arg1: float = None, /) -> int:
        """
        Detects Missing Equality Constraints. The Detect step just identifies possible missing constraints.
                        The result may be retrieved or applied using the corresponding Get / Make methods.
        """

    def detectMissingPointOnPointConstraints(self, arg1: float = None, arg2: bool = None, /) -> int:
        """
        Detects Missing Point On Point Constraints. The Detect step just identifies possible missing constraints.
                        The result may be retrieved or applied using the corresponding Get / Make methods.
        """

    def detectMissingVerticalHorizontalConstraints(self, arg1: float = None, /) -> int:
        """
        Detects Missing Horizontal/Vertical Constraints. The Detect step just identifies possible missing constraints.
                        The result may be retrieved or applied using the corresponding Get / Make methods.
        """

    def exposeInternalGeometry(self, arg1: int, /):
        """
        Exposes all internal geometry of an object supporting internal geometry
        Possible exceptions: (ValueError).
        """

    def extend(self, arg1: int, arg2: float, arg3: int, /):
        """
        extend a curve to new start and end positions
        Possible exceptions: (ValueError, TypeError).
        """

    @typing.overload
    def fillet(self, arg1: int, arg2: int, arg3: FreeCAD.Vector, arg4: FreeCAD.Vector, arg5: float, arg6: int = None, arg7: bool = None, /): ...

    @typing.overload
    def fillet(self, arg1: int, arg2: int, arg3: float, arg4: int = None, arg5: bool = None, /):
        """
        create fillet between two edges or at a point
        Possible exceptions: (ValueError, TypeError).
        """

    def getActive(self, arg1: int, /) -> bool:
        """
        Get the constraint status (enforced or not)
        Possible exceptions: (ValueError).
        """

    def getAxis(self, arg1: int, /) -> FreeCAD.Axis:
        """return an axis based on the corresponding construction line"""

    def getConstruction(self, arg1: int, /) -> bool:
        """
        returns the construction mode of a geometry
        Possible exceptions: (ValueError).
        """

    @typing.overload
    def getDatum(self, arg1: int, /) -> FreeCAD.Quantity: ...

    @typing.overload
    def getDatum(self, arg1: str, /) -> FreeCAD.Quantity:
        """
        Get the value of a datum constraint
        Possible exceptions: (IndexError, NameError, TypeError).
        """

    def getDriving(self, arg1: int, /) -> bool:
        """
        Get the Driving status of a datum constraint
        Possible exceptions: (ValueError).
        """

    def getGeoVertexIndex(self, index: int, /) -> tuple[int, int]:
        """(geoId, posId) = getGeoVertexIndex(index) - retrieve the GeoId and PosId of a point in the sketch"""

    def getGeometryId(self, arg1: int, /) -> int:
        """
        gets the GeometryId of the SketchGeometryExtension of the geometry with the provided GeoId
        Possible exceptions: (ValueError).
        """

    def getGeometryWithDependentParameters(self) -> list[tuple[int, int]]:
        """
        getGeometryWithDependentParameters - returns a list of geoid posid pairs
                        with all the geometry element edges and vertices which the solver regards
                        as being dependent on other parameters.
        """

    def getIndexByName(self, arg1: str, /) -> int:
        """
        Get the index of the constraint by name.
        If there is no such constraint an exception is raised.
        
        Possible exceptions: (ValueError, LookupError).
        """

    def getPoint(self, GeoIndex: int, PointPos: int, /) -> FreeCAD.Vector:
        """
        getPoint(GeoIndex,PointPos) - retrieve the vector of a point in the sketch
        
        Possible exceptions: (ValueError).
        """

    def getVirtualSpace(self, arg1: int, /) -> bool:
        """
        Get the VirtualSpace status of a constraint
        Possible exceptions: (ValueError).
        """

    def increaseBSplineDegree(self, arg1: int, arg2: int = None, /):
        """
        Increases the given BSpline Degree by a number of degrees
        Possible exceptions: (ValueError).
        """

    def insertBSplineKnot(self, arg1: int, arg2: float, arg3: int = None, /):
        """
        Inserts a knot into the BSpline at the given param with given multiplicity. If the knot already exists, this increases the knot multiplicity by the given multiplicity.
        Possible exceptions: (ValueError).
        """

    def isPointOnCurve(self, arg1: int, arg2: float, arg3: float, /) -> bool:
        """
        isPointOnObject(GeoIdCurve, float x, float y) - tests if the point (x,y)
                  geometrically lies on a curve (e.g. ellipse). It treats lines as infinite,
                  arcs as full circles/ellipses/etc. Returns boolean value.
        
        Possible exceptions: (ValueError).
        """

    def makeMissingEquality(self, arg1: bool = None, /):
        """Applies the detected / set Equality constraints. If the argument is True, then solving and redundant removal is done after each individual addition."""

    def makeMissingPointOnPointCoincident(self, arg1: bool = None, /):
        """Applies the detected / set Point On Point coincident constraints. If the argument is True, then solving and redundant removal is done after each individual addition."""

    def makeMissingVerticalHorizontal(self, arg1: bool = None, /):
        """Applies the detected / set Vertical/Horizontal constraints. If the argument is True, then solving and redundant removal is done after each individual addition."""

    def modifyBSplineKnotMultiplicity(self, arg1: int, arg2: int, arg3: int = None, /):
        """
        Increases or reduces the given BSpline knot multiplicity
        Possible exceptions: (ValueError).
        """

    def moveDatumsToEnd(self):
        """
        Moves all datum constraints to the end of the constraint list
        Possible exceptions: (ValueError).
        """

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
        
        Possible exceptions: (ValueError).
        """

    def removeAxesAlignment(self, arg1, /):
        """
        modifies constraints so that the shape is not forced to be aligned with axes.
        Possible exceptions: (TypeError).
        """

    def renameConstraint(self, arg1: int, arg2: str, /):
        """
        Rename a constraint of the sketch
        Possible exceptions: (IndexError, ValueError).
        """

    def setActive(self, arg1: int, arg2: bool, /):
        """
        sets the constraint on/off (enforced or not)
        Possible exceptions: (ValueError).
        """

    def setConstruction(self, arg1: int, arg2: bool, /):
        """
        set construction mode of a geometry on or off
        Possible exceptions: (ValueError).
        """

    @typing.overload
    def setDatum(self, arg1: int, arg2: FreeCAD.Quantity, /): ...

    @typing.overload
    def setDatum(self, arg1: int, arg2: float, /): ...

    @typing.overload
    def setDatum(self, arg1: str, arg2: FreeCAD.Quantity, /): ...

    @typing.overload
    def setDatum(self, arg1: str, arg2: float, /):
        """
        set the Datum of a Distance or Angle constraint
        Possible exceptions: (ValueError, TypeError).
        """

    def setDatumsDriving(self, arg1: bool, /):
        """
        set the Driving status of datum constraints
        Possible exceptions: (ValueError).
        """

    def setDriving(self, arg1: int, arg2: bool, /):
        """
        set the Driving status of a datum constraint
        Possible exceptions: (ValueError).
        """

    def setGeometryId(self, arg1: int, arg2: int, /):
        """
        sets the GeometryId of the SketchGeometryExtension of the geometry with the provided GeoId
        Possible exceptions: (ValueError).
        """

    def setVirtualSpace(self, arg1, arg2: bool, /):
        """
        set the VirtualSpace status of a constraint
        Possible exceptions: (TypeError, ValueError).
        """

    def solve(self) -> int:
        """solve the actual set of geometry and constraints"""

    def split(self, arg1: int, arg2: FreeCAD.Vector, /):
        """
        split a curve with a given id at a given reference point
        Possible exceptions: (ValueError).
        """

    def toggleActive(self, arg1: int, /):
        """
        toggle the active status of constraint (enforced or not)
        Possible exceptions: (ValueError).
        """

    def toggleConstruction(self, arg1: int, /):
        """
        switch a geometry to a construction line
        Possible exceptions: (ValueError).
        """

    def toggleDriving(self, arg1: int, /):
        """
        toggle the Driving status of a datum constraint
        Possible exceptions: (ValueError).
        """

    def toggleVirtualSpace(self, arg1: int, /):
        """
        toggle the VirtualSpace status of a constraint
        Possible exceptions: (ValueError).
        """

    def trim(self, arg1: int, arg2: FreeCAD.Vector, /):
        """
        trim a curve with a given id at a given reference point
        Possible exceptions: (ValueError).
        """


# SketchPy.xml
class Sketch(FreeCAD.Persistence):
    """
    This class can be imported.
    With this objects you can handle constraint sketches
    """

    def __init__(self):
        """With this objects you can handle constraint sketches"""

    @property
    def Conflicts(self) -> tuple[int, ...]:
        """Tuple of conflicting constraints"""

    @property
    def Constraint(self) -> int:
        """0: exactly constraint, -1 under-constraint, 1 over-constraint"""

    @property
    def Geometries(self) -> tuple:
        """Tuple of all geometric elements in this sketch"""

    @property
    def Redundancies(self) -> tuple[int, ...]:
        """Tuple of redundant constraints"""

    @property
    def Shape(self) -> PartModule.Shape:
        """Resulting shape from the sketch geometry"""

    def addConstraint(self, arg1, /) -> tuple[int, ...] | int:
        """
        add an constraint object to the sketch
        Possible exceptions: (TypeError).
        """

    def addGeometry(self, arg1, /) -> int | tuple[int, ...]:
        """
        add a geometric object to the sketch
        Possible exceptions: (TypeError).
        """

    def clear(self):
        """clear the sketch"""

    def movePoint(self, GeoIndex: int, PointPos: int, Vector: FreeCAD.Vector, relative: int = None, /) -> int:
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

    def solve(self) -> int:
        """solve the actual set of geometry and constraints"""


# ExternalGeometryFacadePy.xml
class ExternalGeometryFacade(FreeCAD.BaseClass):
    """
    This class can be imported.
    Describes a GeometryFacade
    """

    def __init__(self, arg1: PartModule.Geometry, /):
        """
        Describes a GeometryFacade
        Possible exceptions: (TypeError).
        """

    @property
    def Blocked(self) -> bool:
        """Sets/returns whether the geometry is blocked or not."""

    @Blocked.setter
    def Blocked(self, value: bool): ...

    @property
    def Construction(self) -> bool:
        """Sets/returns this geometry as a construction one, which will not be part of a later built shape."""

    @Construction.setter
    def Construction(self, value: bool): ...

    @property
    def Geometry(self) -> object:
        """Returns the underlying geometry object."""

    @Geometry.setter
    def Geometry(self, value: object): ...

    @property
    def GeometryLayerId(self) -> int:
        """Returns the Id of the geometry Layer in which the geometry is located."""

    @GeometryLayerId.setter
    def GeometryLayerId(self, value: int): ...

    @property
    def Id(self) -> int:
        """Sets/returns the Internal Alignment Type of the Geometry."""

    @Id.setter
    def Id(self, value: int): ...

    @property
    def InternalType(self) -> str:
        """Sets/returns the Internal Alignment Type of the Geometry."""

    @InternalType.setter
    def InternalType(self, value: str): ...

    @property
    def Ref(self) -> str:
        """Returns the reference string of this external geometry."""

    @Ref.setter
    def Ref(self, value: str): ...

    @property
    def Tag(self) -> str:
        """Gives the tag of the geometry as string."""

    def deleteExtensionOfName(self, arg1: str, /):
        """
        Deletes all extensions of the indicated name.
        Possible exceptions: (Part.OCCError).
        """

    def deleteExtensionOfType(self, arg1: str, /):
        """
        Deletes all extensions of the indicated type.
        Possible exceptions: (Part.OCCError).
        """

    def getExtensionOfName(self, arg1: str, /):
        """
        Gets the first geometry extension of the name indicated by the string.
        Possible exceptions: (Part.OCCError).
        """

    def getExtensionOfType(self, arg1: str, /):
        """
        Gets the first geometry extension of the type indicated by the string.
        Possible exceptions: (Part.OCCError).
        """

    def getExtensions(self) -> list:
        """
        Returns a list with information about the geometry extensions.
        Possible exceptions: (Part.OCCError).
        """

    def hasExtensionOfName(self, arg1: str, /) -> bool:
        """
        Returns a boolean indicating whether a geometry extension with the name indicated as a string exists.
        Possible exceptions: (Part.OCCError).
        """

    def hasExtensionOfType(self, arg1: str, /) -> bool:
        """
        Returns a boolean indicating whether a geometry extension of the type indicated as a string exists.
        Possible exceptions: (Part.OCCError).
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

    def setExtension(self, arg1: PartModule.GeometryExtension, /):
        """
        Sets a geometry extension of the indicated type.
        Possible exceptions: (Part.OCCError).
        """

    def setFlag(self, arg1: str, arg2: bool = None, /) -> bool:
        """
        Sets the given bit to true/false.
        Possible exceptions: (TypeError).
        """

    def testFlag(self, arg1: str, /) -> bool:
        """
        Returns a boolean indicating whether the given bit is set.
        Possible exceptions: (TypeError).
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


# ExternalGeometryExtensionPy.xml
class ExternalGeometryExtension(PartModule.GeometryExtension):
    """
    This class can be imported.
    Describes a ExternalGeometryExtension
    """

    def __init__(self):
        """
        Describes a ExternalGeometryExtension
        Possible exceptions: (TypeError).
        """

    @property
    def Ref(self) -> str:
        """returns the reference string of this external geometry."""

    @Ref.setter
    def Ref(self, value: str): ...

    def setFlag(self, arg1: str, arg2: bool = None, /):
        """
        sets the given bit to true/false.
        Possible exceptions: (TypeError).
        """

    def testFlag(self, arg1: str, /) -> bool:
        """
        returns a boolean indicating whether the given bit is set.
        Possible exceptions: (TypeError).
        """


# GeometryFacadePy.xml
class GeometryFacade(FreeCAD.BaseClass):
    """
    This class can be imported.
    Describes a GeometryFacade
    """

    def __init__(self, arg1: PartModule.Geometry, /):
        """
        Describes a GeometryFacade
        Possible exceptions: (TypeError).
        """

    @property
    def Blocked(self) -> bool:
        """Sets/returns whether the geometry is blocked or not."""

    @Blocked.setter
    def Blocked(self, value: bool): ...

    @property
    def Construction(self) -> bool:
        """Sets/returns this geometry as a construction one, which will not be part of a later built shape."""

    @Construction.setter
    def Construction(self, value: bool): ...

    @property
    def Geometry(self) -> object:
        """Returns the underlying geometry object."""

    @Geometry.setter
    def Geometry(self, value: object): ...

    @property
    def GeometryLayerId(self) -> int:
        """Returns the Id of the geometry Layer in which the geometry is located."""

    @GeometryLayerId.setter
    def GeometryLayerId(self, value: int): ...

    @property
    def Id(self) -> int:
        """Sets/returns the Id of the SketchGeometryExtension."""

    @Id.setter
    def Id(self, value: int): ...

    @property
    def InternalType(self) -> str:
        """Sets/returns the Internal Alignment Type of the Geometry."""

    @InternalType.setter
    def InternalType(self, value: str): ...

    @property
    def Tag(self) -> str:
        """Gives the tag of the geometry as string."""

    def deleteExtensionOfName(self, arg1: str, /):
        """
        Deletes all extensions of the indicated name.
        Possible exceptions: (Part.OCCError).
        """

    def deleteExtensionOfType(self, arg1: str, /):
        """
        Deletes all extensions of the indicated type.
        Possible exceptions: (Part.OCCError).
        """

    def getExtensionOfName(self, arg1: str, /):
        """
        Gets the first geometry extension of the name indicated by the string.
        Possible exceptions: (Part.OCCError).
        """

    def getExtensionOfType(self, arg1: str, /):
        """
        Gets the first geometry extension of the type indicated by the string.
        Possible exceptions: (Part.OCCError).
        """

    def getExtensions(self) -> list:
        """
        Returns a list with information about the geometry extensions.
        Possible exceptions: (Part.OCCError).
        """

    def hasExtensionOfName(self, arg1: str, /) -> bool:
        """
        Returns a boolean indicating whether a geometry extension with the name indicated as a string exists.
        Possible exceptions: (Part.OCCError).
        """

    def hasExtensionOfType(self, arg1: str, /) -> bool:
        """
        Returns a boolean indicating whether a geometry extension of the type indicated as a string exists.
        Possible exceptions: (Part.OCCError).
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

    def setExtension(self, arg1: PartModule.GeometryExtension, /):
        """
        Sets a geometry extension of the indicated type.
        Possible exceptions: (Part.OCCError).
        """

    def setGeometryMode(self, arg1: str, arg2: bool = None, /):
        """
        Sets the given bit to true/false.
        Possible exceptions: (TypeError).
        """

    def testGeometryMode(self, arg1: str, /) -> bool:
        """
        Returns a boolean indicating whether the given bit is set.
        Possible exceptions: (TypeError).
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


# AppSketcherPy.cpp
def open(arg1: str, /):
    """Possible exceptions: (Exception, RuntimeError)."""


def insert(arg1: str, arg2: str, /) -> None:
    """Possible exceptions: (Exception, RuntimeError)."""
