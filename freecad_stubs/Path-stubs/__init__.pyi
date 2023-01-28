import typing

import FreeCAD
import Part as PartModule
import Path as PathModule

LinkList_t: typing.TypeAlias = None | FreeCAD.DocumentObject


# CommandPy.xml
class Command(FreeCAD.Persistence):
    """
    This class can be imported.
    Command([name],[parameters]): Represents a basic Gcode command
    name (optional) is the name of the command, ex. G1
    parameters (optional) is a dictionary containing string:number
    pairs, or a placement, or a vector
    """

    @typing.overload
    def __init__(self, name: str = '', parameters: dict = None): ...

    @typing.overload
    def __init__(self, name: str = '', parameters: FreeCAD.Placement = None):
        """
        Command([name],[parameters]): Represents a basic Gcode command
        name (optional) is the name of the command, ex. G1
        parameters (optional) is a dictionary containing string:number
        pairs, or a placement, or a vector
        Possible exceptions: (ValueError, TypeError).
        """

    @property
    def Name(self) -> str:
        """The name of the command"""

    @Name.setter
    def Name(self, value: str): ...

    @property
    def Parameters(self) -> dict:
        """The parameters of the command"""

    @Parameters.setter
    def Parameters(self, value: dict): ...

    @property
    def Placement(self) -> FreeCAD.Placement:
        """The coordinates of the endpoint of the command"""

    @Placement.setter
    def Placement(self, value: FreeCAD.Placement): ...

    def setFromGCode(self, pstr: str = None, /) -> None:
        """
        setFromGCode(): sets the path from the contents of the given GCode string
        Possible exceptions: (TypeError, ValueError).
        """

    def toGCode(self) -> str:
        """
        toGCode(): returns a GCode representation of the command
        Possible exceptions: (TypeError).
        """

    def transform(self, placement: FreeCAD.Placement, /) -> PathModule.Command:
        """
        transform(Placement): returns a copy of this command transformed by the given placement
        Possible exceptions: (TypeError).
        """


# AreaPy.xml
class Area(FreeCAD.BaseClass):
    """
    This class can be imported.
    FreeCAD python wrapper of libarea

    Path.Area(key=value ...)

    The constructor accepts the same parameters as setParams(...) to configure the object
    All arguments are optional.
    """

    def __init__(self, key=None):
        """
        FreeCAD python wrapper of libarea

        Path.Area(key=value ...)

        The constructor accepts the same parameters as setParams(...) to configure the object
        All arguments are optional.
        """

    @property
    def Sections(self) -> list[PartModule.Shape]:
        """List of sections in this area."""

    @property
    def Shapes(self) -> list[tuple[PartModule.Shape, int]]:
        """A list of tuple: [(shape,op), ...] containing the added shapes together with their operation code"""

    @property
    def Workplane(self) -> PartModule.Shape:
        """The current workplane. If no plane is set, it is derived from the added shapes."""

    @Workplane.setter
    def Workplane(self, value: PartModule.Shape): ...

    def abort(self): ...

    def add(self, shape) -> PathModule.Area:
        """Possible exceptions: (TypeError)."""

    def getDefaultParams(self): ...

    def getParams(self) -> dict:
        """Get current algorithm parameters as a dictionary."""

    def getParamsDesc(self): ...

    def getShape(self, index: int = -1, rebuild: bool = False) -> PartModule.Shape:
        """
        getShape(index=-1,rebuild=False): Return the resulting shape


        * index (-1): the index of the section. -1 means all sections. No effect on planar shape.


        * rebuild: clean the internal cache and rebuild
        """

    def makeOffset(self, index: int = -1) -> PartModule.Shape: ...

    def makePocket(self, index: int = -1) -> PartModule.Shape: ...

    def makeSections(self, heights=None, plane: PartModule.Shape = None) -> list[PathModule.Area]:
        """Possible exceptions: (TypeError)."""

    def setDefaultParams(self): ...

    def setParams(self) -> PathModule.Area: ...

    def setPlane(self, pcObj: PartModule.Shape, /) -> PathModule.Area:
        """
        setPlane(shape): Set the working plane.

        The supplied shape does not need to be planar. Area will try to find planar
        sub-shape (face, wire or edge). If more than one planar sub-shape is found, it
        will prefer the top plane parallel to XY0 plane. If no working plane are set,
        Area will try to find a working plane from the added children shape using the
        same algorithm
        """


# PathPy.xml
class Path(FreeCAD.Persistence):
    """
    This class can be imported.
    Path([commands]): Represents a basic Gcode path
    commands (optional) is a list of Path commands
    """

    @typing.overload
    def __init__(self, pcObj: list = None, /): ...

    @typing.overload
    def __init__(self, gcode: str = None, /):
        """
        Path([commands]): Represents a basic Gcode path
        commands (optional) is a list of Path commands
        Possible exceptions: (TypeError).
        """

    @property
    def BoundBox(self) -> FreeCAD.BoundBox:
        """the extent of this path"""

    @property
    def Center(self) -> FreeCAD.Vector:
        """the center position for all rotational parameters"""

    @Center.setter
    def Center(self, value: FreeCAD.Vector): ...

    @property
    def Commands(self) -> list[PathModule.Command]:
        """the list of commands of this path"""

    @Commands.setter
    def Commands(self, value: list): ...

    @property
    def Length(self) -> float:
        """the total length of this path in mm"""

    @property
    def Size(self) -> int:
        """the number of commands in this path"""

    @typing.overload
    def addCommands(self, o: PathModule.Command, /) -> PathModule.Path: ...

    @typing.overload
    def addCommands(self, o: list, /) -> PathModule.Path:
        """adds a command or a list of commands at the end of the path"""

    def copy(self) -> PathModule.Path:
        """
        returns a copy of this path
        Possible exceptions: (TypeError).
        """

    def deleteCommand(self, pos: int = -1, /) -> PathModule.Path:
        """
        deleteCommand([int]):
        deletes the command found at the given position or from the end of the path
        """

    def getCycleTime(self, hFeed: float, vFeed: float, hRapid: float, vRapid: float, /) -> float:
        """return the cycle time estimation for this path in s"""

    def insertCommand(self, o: PathModule.Command, pos: int = -1, /) -> PathModule.Path:
        """
        insertCommand(Command,[int]):
        adds a command at the given position or at the end of the path
        """

    def setFromGCode(self, pstr: str = None, /) -> None:
        """
        sets the contents of the path from a gcode string
        Possible exceptions: (TypeError).
        """

    def toGCode(self) -> str:
        """
        returns a gcode string representing the path
        Possible exceptions: (TypeError).
        """


# FeatureAreaPy.xml
class FeatureArea(FreeCAD.DocumentObject):
    """This class handles Path Area features"""

    @property
    def WorkPlane(self) -> PartModule.Shape:
        """The current workplane. If no plane is set, it is derived from the added shapes."""

    @WorkPlane.setter
    def WorkPlane(self, value: PartModule.Shape): ...

    @property
    def Sources(self) -> list[FreeCAD.DocumentObject | None]:
        """Property TypeId: App::PropertyLinkList."""

    @Sources.setter
    def Sources(self, value: LinkList_t): ...

    @property
    def WorkPlane(self) -> PartModule.Shape:
        """Property TypeId: Part::PropertyPartShape."""

    @WorkPlane.setter
    def WorkPlane(self, value: PartModule.Shape): ...

    def getArea(self) -> PathModule.Area:
        """Return a copy of the encapsulated Python Area object."""

    @typing.overload
    def setParams(self, key=None): ...

    @typing.overload
    def setParams(self) -> None:
        """
        setParams(key=value...): Convenient function to configure this feature.

        Same usage as Path.Area.setParams(). This function stores the parameters in the properties.
        """


# FeaturePathCompoundPy.xml
class FeaturePathCompound(FreeCAD.DocumentObject):
    """This class handles Path Compound features"""

    def addObject(self, object: FreeCAD.DocumentObject, /):
        """
        Add an object to the group
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def removeObject(self, object: FreeCAD.DocumentObject, /):
        """
        Remove an object from the group
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """


# AreaPyImp.cpp
@typing.overload
def setDefaultParams(key=None): ...


@typing.overload
def setDefaultParams() -> None:
    """
    setDefaultParams(key=value...):
    Static method to set the default parameters of all following Path.Area, plus the following
    additional parameters.

    Possible exceptions: (ValueError).
    """


def getDefaultParams() -> dict:
    """getDefaultParams(): Static method to return the current default parameters."""


def abort(aborting: bool = True): ...


def getParamsDesc(as_string: bool = False) -> str | dict:
    """
    getParamsDesc(as_string=False): Returns a list of supported parameters and their descriptions.

    * as_string: if False, then return a dictionary of documents of all supported parameters.
    """
