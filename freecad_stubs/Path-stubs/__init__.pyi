import typing

import FreeCAD
import Part
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
    def __init__(self, name: str = None, parameters: dict = None): ...

    @typing.overload
    def __init__(self, name: str = None, parameters: FreeCAD.Placement = None):
        """
        Command([name],[parameters]): Represents a basic Gcode command
        name (optional) is the name of the command, ex. G1
        parameters (optional) is a dictionary containing string:number 
        pairs, or a placement, or a vector
        Possible exceptions: (TypeError).
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

    def setFromGCode(self, arg1: str, /) -> None:
        """
        toGCode(): returns a GCode representation of the command
        Possible exceptions: (Exception).
        """

    def toGCode(self) -> str:
        """
        toGCode(): returns a GCode representation of the command
        Possible exceptions: (Exception).
        """

    def transform(self, Placement: FreeCAD.Placement, /) -> PathModule.Command:
        """
        transform(Placement): returns a copy of this command transformed by the given placement
        Possible exceptions: (Exception).
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

    def __init__(self, key=None, /):
        """
        FreeCAD python wrapper of libarea

        Path.Area(key=value ...)

        The constructor accepts the same parameters as setParams(...) to configure the object
        All arguments are optional.
        """

    @property
    def Sections(self) -> list[Part.Shape]:
        """List of sections in this area."""

    @property
    def Shapes(self) -> list[tuple[Part.Shape, int]]:
        """A list of tuple: [(shape,op), ...] containing the added shapes together with their operation code"""

    @property
    def Workplane(self) -> Part.Shape:
        """The current workplane. If no plane is set, it is derived from the added shapes."""

    @Workplane.setter
    def Workplane(self, value: Part.Shape): ...

    def add(self, shape) -> PathModule.Area:
        """Possible exceptions: (TypeError)."""

    def getParams(self) -> dict:
        """Get current algorithm parameters as a dictionary."""

    def getShape(self, index: int = -1, rebuild=False) -> Part.Shape:
        """
        getShape(index=-1,rebuild=False): Return the resulting shape


        * index (-1): the index of the section. -1 means all sections. No effect on planar shape.


        * rebuild: clean the internal cache and rebuild
        """

    def makeOffset(self, index: int = None) -> Part.Shape: ...

    def makePocket(self, index: int = None) -> Part.Shape: ...

    def makeSections(self, heights=None, plane: PartModule.Shape = None) -> list[PathModule.Area]:
        """Possible exceptions: (TypeError)."""

    def setParams(self) -> PathModule.Area: ...

    def setPlane(self, shape: PartModule.Shape, /) -> PathModule.Area:
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
    def __init__(self, commands: list = None, /): ...

    @typing.overload
    def __init__(self, commands: str = None, /):
        """
        Path([commands]): Represents a basic Gcode path
        commands (optional) is a list of Path commands
        Possible exceptions: (TypeError).
        """

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
    def addCommands(self, arg1: PathModule.Command, /) -> PathModule.Path: ...

    @typing.overload
    def addCommands(self, arg1: list, /) -> PathModule.Path:
        """adds a command or a list of commands at the end of the path"""

    def copy(self) -> PathModule.Path:
        """
        returns a copy of this path
        Possible exceptions: (Exception).
        """

    def deleteCommand(self, int: int = None, /) -> PathModule.Path:
        """
        deleteCommand([int]):
        deletes the command found at the given position or from the end of the path
        """

    def insertCommand(self, Command: PathModule.Command, int: int = None, /) -> PathModule.Path:
        """
        insertCommand(Command,[int]):
        adds a command at the given position or at the end of the path
        """

    def setFromGCode(self, arg1: str, /) -> None:
        """
        sets the contents of the path from a gcode string
        Possible exceptions: (Exception).
        """

    def toGCode(self) -> str:
        """
        returns a gcode string representing the path
        Possible exceptions: (Exception).
        """


# TooltablePy.xml
class Tooltable(FreeCAD.Persistence):
    """
    This class can be imported.
    The Tooltable object holds a table of CNC tools
    """

    @typing.overload
    def __init__(self, arg1: dict, /): ...

    @typing.overload
    def __init__(self, name: str = None, tooltype: str = None, material: str = None, diameter=None, lengthOffset=None, flatRadius=None, cornerRadius=None, cuttingEdgeAngle=None, cuttingEdgeHeight=None, version: int = None): ...

    @typing.overload
    def __init__(self, name: str = None, tooltype: str = None, material: str = None, diameter=None, lengthOffset=None, flatRadius=None, cornerRadius=None, cuttingEdgeAngle=None, cuttingEdgeHeight=None):
        """
        The Tooltable object holds a table of CNC tools
        Possible exceptions: (TypeError).
        """

    @property
    def Tools(self) -> dict:
        """the dictionary of tools of this table"""

    @Tools.setter
    def Tools(self, value: dict): ...

    @typing.overload
    def addTools(self, arg1: PathModule.Tool, /) -> None: ...

    @typing.overload
    def addTools(self, arg1: list, /) -> None:
        """adds a tool or a list of tools at the end of the table"""

    def copy(self) -> PathModule.Tool:
        """
        returns a copy of this tooltable
        Possible exceptions: (Exception).
        """

    def deleteTool(self, int: int = None, /) -> None:
        """
        deleteTool(int):
        deletes the tool found at the given position
        """

    def getTool(self, int: int, /) -> PathModule.Tool | None:
        """
        getTool(int):
        returns the tool found at the given position, or  None
        """

    def setFromTemplate(self, dict: str, /):
        """
        setFromTemplate(dict) ... restores receiver from given template attribute dictionary
        Possible exceptions: (TypeError).
        """

    def setTool(self, int: int, tool: PathModule.Tool, /) -> None:
        """
        setTool(int,tool):
        adds a tool at the given position
        """

    def templateAttrs(self) -> dict[str, int | str | float]:
        """
        templateAttrs() ... returns a dictionary representing the receivers attributes for a template
        Possible exceptions: (Exception).
        """


# FeatureAreaPy.xml
class FeatureArea(FreeCAD.DocumentObject):
    """This class handles Path Area features"""

    @property
    def WorkPlane(self) -> Part.Shape:
        """The current workplane. If no plane is set, it is derived from the added shapes."""

    @WorkPlane.setter
    def WorkPlane(self, value: Part.Shape): ...

    @property
    def Sources(self) -> list[FreeCAD.DocumentObject | None]:
        """Property TypeId: App::PropertyLinkList."""

    @Sources.setter
    def Sources(self, value: LinkList_t): ...

    @property
    def WorkPlane(self) -> Part.Shape:
        """Property TypeId: Part::PropertyPartShape."""

    @WorkPlane.setter
    def WorkPlane(self, value: Part.Shape): ...

    def getArea(self) -> PathModule.Area:
        """Return a copy of the encapsulated Python Area object."""

    def setParams(self) -> None:
        """
        setParams(key=value...): Convenient function to configure this feature.

        Same usage as Path.Area.setParams(). This function stores the parameters in the properties.
        """


# FeaturePathCompoundPy.xml
class FeaturePathCompound(FreeCAD.DocumentObject):
    """This class handles Path Compound features"""

    def addObject(self, arg1: FreeCAD.DocumentObject, /):
        """
        Add an object to the group
        Possible exceptions: (FreeCAD.FreeCADError).
        """

    def removeObject(self, arg1: FreeCAD.DocumentObject, /):
        """
        Remove an object from the group
        Possible exceptions: (FreeCAD.FreeCADError).
        """


# AppPathPy.cpp
def write(object, filename: str, /) -> None:
    """write(object,filename): Exports a given path object to a GCode file"""


def read(filename: str, document: str = None, /) -> None:
    """read(filename,[document]): Imports a GCode file into the given document"""


def show(path: PathModule.Path, string: str = None, /) -> None:
    """show(path,[string]): Add the path to the active document or create one if no document exists"""


def fromShape(Shape, /) -> PathModule.Path:
    """fromShape(Shape): Returns a Path object from a Part Shape (deprecated - use fromShapes() instead)"""


def fromShapes(shapes, start: FreeCAD.Vector = None, return_end=None) -> PathModule.Path | tuple[PathModule.Path, FreeCAD.Vector]:
    """
    fromShapes(shapes, start=Vector(), return_end=False" PARAM_PY_ARGS_DOC(ARG,AREA_PARAMS_PATH) ")

    Returns a Path object from a list of shapes

    * shapes: input list of shapes.

    * start (Vector()): feed start position, and also serves as a hint of path entry.

    * return_end (False): if True, returns tuple (path, endPosition).
    "
                PARAM_PY_DOC(ARG, AREA_PARAMS_PATH)
    """


def sortWires(shapes, start: FreeCAD.Vector = None) -> tuple[list, FreeCAD.Vector, int, int]:
    """
    sortWires(shapes, start=Vector(), "  
                PARAM_PY_ARGS_DOC(ARG,AREA_PARAMS_ARC_PLANE)
                PARAM_PY_ARGS_DOC(ARG,AREA_PARAMS_SORT) ")

    Returns (wires,end), where 'wires' is sorted across Z value and with optimized travel distance,
    and 'end' is the ending position of the whole wires. If arc_plane==1, it returns (wires,end,arc_plane),
    where arc_plane is the found plane if any, or unchanged.

    * shapes: input shape list

    * start (Vector()): optional start position.
    "
                PARAM_PY_DOC(ARG, AREA_PARAMS_ARC_PLANE)
                PARAM_PY_DOC(ARG, AREA_PARAMS_SORT)
    """


# AreaPyImp.cpp
def setDefaultParams() -> None:
    """
    setDefaultParams(key=value...):
    Static method to set the default parameters of all following Path.Area, plus the following
    additional parameters.
    """


def getDefaultParams() -> dict:
    """getDefaultParams(): Static method to return the current default parameters."""


def abort(aborting=None) -> None: ...


def getParamsDesc(as_string=False) -> str | dict:
    """
    getParamsDesc(as_string=False): Returns a list of supported parameters and their descriptions.

    * as_string: if False, then return a dictionary of documents of all supported parameters.
    """
