import typing

import FreeCAD
import Part
import Path


# CommandPy.xml
class Command(FreeCAD.Persistence):
    """Command([name],[parameters]): Represents a basic Gcode command
    name (optional) is the name of the command, ex. G1
    parameters (optional) is a dictionary containing string:number 
    pairs, or a placement, or a vector"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: str, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Placement, /): ...

    @typing.overload
    def __init__(self, name: str = None, parameters: dict = None): ...

    @typing.overload
    def __init__(self, name: str = None, parameters: FreeCAD.Placement = None):
        """Command([name],[parameters]): Represents a basic Gcode command
        name (optional) is the name of the command, ex. G1
        parameters (optional) is a dictionary containing string:number 
        pairs, or a placement, or a vector"""

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
    def Placement(self) -> object:
        """The coordinates of the endpoint of the command"""

    @Placement.setter
    def Placement(self, value: object): ...

    def setFromGCode(self, arg1: str, /):
        """toGCode(): returns a GCode representation of the command"""

    def toGCode(self):
        """toGCode(): returns a GCode representation of the command"""

    def transform(self, Placement: FreeCAD.Placement, /):
        """transform(Placement): returns a copy of this command transformed by the given placement"""


# AreaPy.xml
class Area(FreeCAD.BaseClass):
    """FreeCAD python wrapper of libarea\n
    Path.Area(key=value ...)\n
    The constructor accepts the same parameters as setParams(...) to configure the object
    All arguments are optional."""

    @property
    def Sections(self) -> list:
        """List of sections in this area."""

    @property
    def Shapes(self) -> list:
        """A list of tuple: [(shape,op), ...] containing the added shapes together with their operation code"""

    @property
    def Workplane(self) -> object:
        """The current workplane. If no plane is set, it is derived from the added shapes."""

    @Workplane.setter
    def Workplane(self, value: object): ...

    def add(self, shape: object): ...

    def getParams(self):
        """Get current algorithm parameters as a dictionary."""

    def getShape(self, index: int = -1, rebuild: object = False):
        """getShape(index=-1,rebuild=False): Return the resulting shape\n
        \n* index (-1): the index of the section. -1 means all sections. No effect on planar shape.\n
        \n* rebuild: clean the internal cache and rebuild"""

    def makeOffset(self, index: int = None): ...

    def makePocket(self, index: int = None): ...

    def makeSections(self, heights: object = None, plane: Part.TopoShape = None): ...

    def setParams(self): ...

    def setPlane(self, shape: Part.TopoShape, /):
        """setPlane(shape): Set the working plane.\n
        The supplied shape does not need to be planar. Area will try to find planar
        sub-shape (face, wire or edge). If more than one planar sub-shape is found, it
        will prefer the top plane parallel to XY0 plane. If no working plane are set,
        Area will try to find a working plane from the added children shape using the
        same algorithm"""


# PathPy.xml
class Toolpath(FreeCAD.Persistence):
    """Path([commands]): Represents a basic Gcode path
    commands (optional) is a list of Path commands"""

    @typing.overload
    def __init__(self, arg1: list = None, /): ...

    @typing.overload
    def __init__(self, arg1: str = None, /):
        """Path([commands]): Represents a basic Gcode path
        commands (optional) is a list of Path commands"""

    @property
    def Center(self) -> object:
        """the center position for all rotational parameters"""

    @Center.setter
    def Center(self, value: object): ...

    @property
    def Commands(self) -> list:
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
    def addCommands(self, arg1: Path.Command, /): ...

    @typing.overload
    def addCommands(self, arg1: list, /):
        """adds a command or a list of commands at the end of the path"""

    def copy(self):
        """returns a copy of this path"""

    def deleteCommand(self, int: int = None, /):
        """deleteCommand([int]):
        deletes the command found at the given position or from the end of the path"""

    def insertCommand(self, Command: Path.Command, int: int = None, /):
        """insertCommand(Command,[int]):
        adds a command at the given position or at the end of the path"""

    def setFromGCode(self, arg1: str, /):
        """sets the contents of the path from a gcode string"""

    def toGCode(self):
        """returns a gcode string representing the path"""


# TooltablePy.xml
class Tooltable(FreeCAD.Persistence):
    """The Tooltable object holds a table of CNC tools"""

    @typing.overload
    def __init__(self, arg1: dict, /): ...

    @typing.overload
    def __init__(self, name: str = None, tooltype: str = None, material: str = None, diameter: object = None, lengthOffset: object = None, flatRadius: object = None, cornerRadius: object = None, cuttingEdgeAngle: object = None, cuttingEdgeHeight: object = None, version: int = None): ...

    @typing.overload
    def __init__(self, name: str = None, tooltype: str = None, material: str = None, diameter: object = None, lengthOffset: object = None, flatRadius: object = None, cornerRadius: object = None, cuttingEdgeAngle: object = None, cuttingEdgeHeight: object = None):
        """The Tooltable object holds a table of CNC tools"""

    @property
    def Tools(self) -> dict:
        """the dictionary of tools of this table"""

    @Tools.setter
    def Tools(self, value: dict): ...

    @typing.overload
    def addTools(self, arg1: Path.Tool, /): ...

    @typing.overload
    def addTools(self, arg1: list, /):
        """adds a tool or a list of tools at the end of the table"""

    def copy(self):
        """returns a copy of this tooltable"""

    def deleteTool(self, int: int = None, /):
        """deleteTool(int):
        deletes the tool found at the given position"""

    def getTool(self, int: int, /):
        """getTool(int):
        returns the tool found at the given position, or  None"""

    def setFromTemplate(self, dict: str, /):
        """setFromTemplate(dict) ... restores receiver from given template attribute dictionary"""

    def setTool(self, int: int, tool: Path.Tool, /):
        """setTool(int,tool):
        adds a tool at the given position"""

    def templateAttrs(self):
        """templateAttrs() ... returns a dictionary representing the receivers attributes for a template"""


# FeatureAreaPy.xml
class FeatureArea(FreeCAD.DocumentObject):
    """This class handles Path Area features"""

    @property
    def WorkPlane(self) -> object:
        """The current workplane. If no plane is set, it is derived from the added shapes."""

    @WorkPlane.setter
    def WorkPlane(self, value: object): ...

    def getArea(self):
        """Return a copy of the encapsulated Python Area object."""

    def setParams(self):
        """setParams(key=value...): Convenient function to configure this feature.\n
        Same usage as Path.Area.setParams(). This function stores the parameters in the properties."""


# FeaturePathCompoundPy.xml
class FeaturePathCompound(FreeCAD.DocumentObject):
    """This class handles Path Compound features"""

    def addObject(self, arg1: FreeCAD.DocumentObject, /):
        """Add an object to the group"""

    def removeObject(self, arg1: FreeCAD.DocumentObject, /):
        """Remove an object from the group"""


# AppPathPy.cpp
def write(arg1: object, arg2: str, /):
    """write(object,filename): Exports a given path object to a GCode file"""


def read(arg1: str, arg2: str = None, /):
    """read(filename,[document]): Imports a GCode file into the given document"""


def show(arg1: Path.Toolpath, arg2: str = None, /):
    """show(path,[string]): Add the path to the active document or create one if no document exists"""


def fromShape(arg1: object, /):
    """fromShape(Shape): Returns a Path object from a Part Shape (deprecated - use fromShapes() instead)"""


def fromShapes(shapes: object, start: FreeCAD.Vector = None, return_end: object = None):
    """fromShapes(shapes, start=Vector(), return_end=False" PARAM_PY_ARGS_DOC(ARG,AREA_PARAMS_PATH) ")

    Returns a Path object from a list of shapes

    * shapes: input list of shapes.

    * start (Vector()): feed start position, and also serves as a hint of path entry.

    * return_end (False): if True, returns tuple (path, endPosition).
    "
                PARAM_PY_DOC(ARG, AREA_PARAMS_PATH)"""


def sortWires(shapes: object, start: FreeCAD.Vector = None):
    """sortWires(shapes, start=Vector(), "  
                PARAM_PY_ARGS_DOC(ARG,AREA_PARAMS_ARC_PLANE)
                PARAM_PY_ARGS_DOC(ARG,AREA_PARAMS_SORT) ")

    Returns (wires,end), where 'wires' is sorted across Z value and with optimized travel distance,
    and 'end' is the ending position of the whole wires. If arc_plane==1, it returns (wires,end,arc_plane),
    where arc_plane is the found plane if any, or unchanged.

    * shapes: input shape list

    * start (Vector()): optional start position.
    "
                PARAM_PY_DOC(ARG, AREA_PARAMS_ARC_PLANE)
                PARAM_PY_DOC(ARG, AREA_PARAMS_SORT)"""


# AreaPyImp.cpp
def setDefaultParams():
    """setDefaultParams(key=value...):
    Static method to set the default parameters of all following Path.Area, plus the following
    additional parameters.
    """


def getDefaultParams():
    """getDefaultParams(): Static method to return the current default parameters."""


def abort(aborting: object = None): ...


def getParamsDesc(as_string: object = None):
    """getParamsDesc(as_string=False): Returns a list of supported parameters and their descriptions.

    * as_string: if False, then return a dictionary of documents of all supported parameters."""


# AppPathGuiPy.cpp
def open(arg1: str, /):
    """open(filename): Opens a GCode file as a new document"""


def insert(arg1: str, arg2: str = None, /):
    """insert(filename,docname): Imports a given GCode file into the given document"""


def export(arg1: object, arg2: str, /):
    """export(objectslist,filename): Exports a given list of Path objects to a GCode file"""
