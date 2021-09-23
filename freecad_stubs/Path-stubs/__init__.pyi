import typing

import FreeCAD
import Part
import Path


# ToolPy.xml
class Tool(FreeCAD.Persistence):
    """
    This class can be imported.
    The Tool objects holds the properties of a CNC tool.
    optional attributes:
      name: a user-defined name for this tool
      tooltype: Drill, CenterDrill, CounterSink, CounterBore, Reamer, Tap, EndMill, SlotCutter, BallEndMill, ChamferMill, CornerRound, Engraver or Undefined
      material: HighSpeedSteel, HighCarbonToolSteel, Carbide, CastAlloy, Ceramics, Diamond, Sialon or Undefined
      diameter : the diameter of this tool
      lengthOffset
      flatRadius
      cornerRadius
      cuttingEdgeAngle
      cuttingEdgeHeight
    """

    @typing.overload
    def __init__(self, arg1: dict, /): ...

    @typing.overload
    def __init__(self, name: str = None, tooltype: str = None, material: str = None, diameter: object = None, lengthOffset: object = None, flatRadius: object = None, cornerRadius: object = None, cuttingEdgeAngle: object = None, cuttingEdgeHeight: object = None, version: int = None): ...

    @typing.overload
    def __init__(self, name: str = None, tooltype: str = None, material: str = None, diameter: object = None, lengthOffset: object = None, flatRadius: object = None, cornerRadius: object = None, cuttingEdgeAngle: object = None, cuttingEdgeHeight: object = None):
        """
        The Tool objects holds the properties of a CNC tool.
        optional attributes:
          name: a user-defined name for this tool
          tooltype: Drill, CenterDrill, CounterSink, CounterBore, Reamer, Tap, EndMill, SlotCutter, BallEndMill, ChamferMill, CornerRound, Engraver or Undefined
          material: HighSpeedSteel, HighCarbonToolSteel, Carbide, CastAlloy, Ceramics, Diamond, Sialon or Undefined
          diameter : the diameter of this tool
          lengthOffset
          flatRadius
          cornerRadius
          cuttingEdgeAngle
          cuttingEdgeHeight
        """

    @property
    def CornerRadius(self) -> float:
        """the corner radius of this tool in mm"""

    @CornerRadius.setter
    def CornerRadius(self, value: float): ...

    @property
    def CuttingEdgeAngle(self) -> float:
        """the cutting edge angle of this tool"""

    @CuttingEdgeAngle.setter
    def CuttingEdgeAngle(self, value: float): ...

    @property
    def CuttingEdgeHeight(self) -> float:
        """the cutting edge height of this tool in mm"""

    @CuttingEdgeHeight.setter
    def CuttingEdgeHeight(self, value: float): ...

    @property
    def Diameter(self) -> float:
        """the diameter of this tool in mm"""

    @Diameter.setter
    def Diameter(self, value: float): ...

    @property
    def FlatRadius(self) -> float:
        """the flat radius of this tool in mm"""

    @FlatRadius.setter
    def FlatRadius(self, value: float): ...

    @property
    def LengthOffset(self) -> float:
        """the length offset of this tool in mm"""

    @LengthOffset.setter
    def LengthOffset(self, value: float): ...

    @property
    def Material(self) -> str:
        """
        the material of this tool: Steel, Carbide, HighSpeedSteel,
        HighCarbonToolSteel CastAlloy, Ceramics, Diamond, Sialon or Undefined
        """

    @Material.setter
    def Material(self, value: str): ...

    @property
    def Name(self) -> str:
        """the name of this tool in mm"""

    @Name.setter
    def Name(self, value: str): ...

    @property
    def ToolType(self) -> str:
        """
        the type of this tool: Drill, CenterDrill, CounterSink, CounterBore, Reamer, Tap,
        EndMill, SlotCutter, BallEndMill, ChamferMill, CornerRound, Engraver or Undefined
        """

    @ToolType.setter
    def ToolType(self, value: str): ...

    def copy(self):
        """returns a copy of this tool"""

    def getToolMaterials(self):
        """returns all available tool materials"""

    def getToolTypes(self):
        """returns all available tool types"""

    def setFromTemplate(self, xmlString_dictionary: str, /):
        """setFromTemplate(xmlString|dictionary) ... fills receiver with values from the template string or dictionary"""

    def templateAttrs(self):
        """templateAttrs() ... returns a dictionary with all attributes"""


# VoronoiEdgePy.xml
class VoronoiEdge(FreeCAD.BaseClass):
    """
    This class can be imported.
    Edge of a Voronoi diagram
    """

    def __init__(self):
        """Edge of a Voronoi diagram"""

    @property
    def Cell(self) -> object:
        """cell the edge belongs to"""

    @property
    def Color(self) -> int:
        """Assigned color of the receiver."""

    @Color.setter
    def Color(self, value: int): ...

    @property
    def Index(self) -> int:
        """Internal id of the element."""

    @property
    def Next(self) -> object:
        """CCW next edge within voronoi cell"""

    @property
    def Prev(self) -> object:
        """CCW previous edge within voronoi cell"""

    @property
    def RotNext(self) -> object:
        """Rotated CCW next edge within voronoi cell"""

    @property
    def RotPrev(self) -> object:
        """Rotated CCW previous edge within voronoi cell"""

    @property
    def Twin(self) -> object:
        """Twin edge"""

    @property
    def Vertices(self) -> list:
        """Begin and End voronoi vertex"""

    def toShape(self, arg1: float = None, arg2: float = None, arg3: bool = None, /):
        """Returns a shape for the edge"""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...


# VoronoiCellPy.xml
class VoronoiCell(FreeCAD.BaseClass):
    """
    This class can be imported.
    Cell of a Voronoi diagram
    """

    def __init__(self):
        """Cell of a Voronoi diagram"""

    @property
    def Color(self) -> int:
        """Assigned color of the receiver."""

    @Color.setter
    def Color(self, value: int): ...

    @property
    def IncidentEdge(self) -> object:
        """Incident edge of the cell - if exists"""

    @property
    def Index(self) -> int:
        """Internal id of the element."""

    @property
    def SourceCategory(self) -> int:
        """Returns the index of the cell's source"""

    @property
    def SourceIndex(self) -> int:
        """Returns the index of the cell's source"""

    def getSource(self, arg1: float = None, /):
        """Returns the Source for the cell"""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...


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

    def setFromGCode(self, arg1: str, /):
        """setFromGCode(): sets the path from the contents of the given GCode string"""

    def toGCode(self):
        """toGCode(): returns a GCode representation of the command"""

    def transform(self, Placement: FreeCAD.Placement, /):
        """transform(Placement): returns a copy of this command transformed by the given placement"""


# AreaPy.xml
class Area(FreeCAD.BaseClass):
    """
    This class can be imported.
    FreeCAD python wrapper of libarea

    Path.Area(key=value ...)

    The constructor accepts the same parameters as setParams(...) to configure the object
    All arguments are optional.
    """

    def __init__(self, key):
        """
        FreeCAD python wrapper of libarea

        Path.Area(key=value ...)

        The constructor accepts the same parameters as setParams(...) to configure the object
        All arguments are optional.
        """

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
        """
        getShape(index=-1,rebuild=False): Return the resulting shape


        * index (-1): the index of the section. -1 means all sections. No effect on planar shape.


        * rebuild: clean the internal cache and rebuild
        """

    def makeOffset(self, index: int = None): ...

    def makePocket(self, index: int = None): ...

    def makeSections(self, heights: object = None, plane: Part.Shape = None): ...

    def setParams(self): ...

    def setPlane(self, shape: Part.Shape, /):
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
        """

    @property
    def BoundBox(self) -> FreeCAD.BoundBox:
        """the extent of this path"""

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
        """
        deleteCommand([int]):
        deletes the command found at the given position or from the end of the path
        """

    def getCycleTime(self, arg1: float, arg2: float, arg3: float, arg4: float, /):
        """return the cycle time estimation for this path in s"""

    def insertCommand(self, Command: Path.Command, int: int = None, /):
        """
        insertCommand(Command,[int]):
        adds a command at the given position or at the end of the path
        """

    def setFromGCode(self, arg1: str, /):
        """sets the contents of the path from a gcode string"""

    def toGCode(self):
        """returns a gcode string representing the path"""


# TooltablePy.xml
class Tooltable(FreeCAD.Persistence):
    """
    This class can be imported.
    The Tooltable object holds a table of CNC tools
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: dict, /): ...

    @typing.overload
    def __init__(self, arg1: list, /):
        """The Tooltable object holds a table of CNC tools"""

    @property
    def Name(self) -> str:
        """the name of this tool table"""

    @Name.setter
    def Name(self, value: str): ...

    @property
    def Tools(self) -> dict:
        """the dictionary of tools of this table"""

    @Tools.setter
    def Tools(self, value: dict): ...

    @property
    def Version(self) -> int:
        """the version of this tooltable"""

    @Version.setter
    def Version(self, value: int): ...

    @typing.overload
    def addTools(self, arg1: Path.Tool, /): ...

    @typing.overload
    def addTools(self, arg1: list, /):
        """adds a tool or a list of tools at the end of the table"""

    def copy(self):
        """returns a copy of this tooltable"""

    def deleteTool(self, int: int = None, /):
        """
        deleteTool(int):
        deletes the tool found at the given position
        """

    def getTool(self, int: int, /):
        """
        getTool(int):
        returns the tool found at the given position, or  None
        """

    def setFromTemplate(self, dict: dict, /):
        """setFromTemplate(dict) ... restores receiver from given template attribute dictionary"""

    def setTool(self, int: int, tool: Path.Tool, /):
        """
        setTool(int,tool):
        adds a tool at the given position
        """

    def templateAttrs(self):
        """templateAttrs() ... returns a dictionary representing the receivers attributes for a template"""


# VoronoiPy.xml
class Voronoi(FreeCAD.BaseClass):
    """
    This class can be imported.
    Voronoi([segments]): Create voronoi for given collection of line segments
    """

    def __init__(self, segments: float = None, /):
        """Voronoi([segments]): Create voronoi for given collection of line segments"""

    @property
    def Cells(self) -> list:
        """List of all cells of the voronoi diagram"""

    @property
    def Edges(self) -> list:
        """List of all edges of the voronoi diagram"""

    @property
    def Vertices(self) -> list:
        """List of all vertices of the voronoi diagram"""

    def addPoint(self, vector_vector2d: object, /):
        """addPoint(vector|vector2d) add given point to input collection"""

    def addSegment(self, vector_vector2d: object, vector_vector2d2: object, /):
        """addSegment(vector|vector2d, vector|vector2d) add given segment to input collection"""

    def colorColinear(self, arg1: int, arg2: float = None, /):
        """assign given color to all edges sourced by two segments almost in line with each other (optional angle in degrees)"""

    def colorExterior(self, arg1: int, arg2: object = None, /):
        """assign given color to all exterior edges and vertices"""

    def colorTwins(self, arg1: int, /):
        """assign given color to all twins of edges (which one is considered a twin is arbitrary)"""

    def construct(self):
        """constructs the voronoi diagram from the input collections"""

    def getPoints(self, arg1: float = None, /):
        """Get list of all input points."""

    def getSegments(self, arg1: float = None, /):
        """Get list of all input segments."""

    def numCells(self):
        """Return number of cells"""

    def numEdges(self):
        """Return number of edges"""

    def numPoints(self):
        """Return number of input points"""

    def numSegments(self):
        """Return number of input segments"""

    def numVertices(self):
        """Return number of vertices"""

    def resetColor(self, arg1: int, /):
        """assign color 0 to all elements with the given color"""


# FeatureAreaPy.xml
class FeatureArea(FreeCAD.DocumentObject):
    """This class handles Path Area features"""

    @property
    def WorkPlane(self) -> object:
        """The current workplane. If no plane is set, it is derived from the added shapes."""

    @WorkPlane.setter
    def WorkPlane(self, value: object): ...

    @property
    def Sources(self) -> dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]:
        """Property TypeId: App::PropertyLinkList."""

    @Sources.setter
    def Sources(self, value: dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]): ...

    @property
    def WorkPlane(self):
        """Property TypeId: Part::PropertyPartShape."""

    @WorkPlane.setter
    def WorkPlane(self, value): ...

    def getArea(self):
        """Return a copy of the encapsulated Python Area object."""

    def setParams(self):
        """
        setParams(key=value...): Convenient function to configure this feature.

        Same usage as Path.Area.setParams(). This function stores the parameters in the properties.
        """


# VoronoiVertexPy.xml
class VoronoiVertex(FreeCAD.BaseClass):
    """
    This class can be imported.
    Vertex of a Voronoi diagram
    """

    def __init__(self):
        """Vertex of a Voronoi diagram"""

    @property
    def Color(self) -> int:
        """Assigned color of the receiver."""

    @Color.setter
    def Color(self, value: int): ...

    @property
    def IncidentEdge(self) -> object:
        """Y position"""

    @property
    def Index(self) -> int:
        """Internal id of the element."""

    @property
    def X(self) -> float:
        """X position"""

    @property
    def Y(self) -> float:
        """Y position"""

    def toPoint(self, arg1: float = None, /):
        """Returns a Vector - or None if not possible"""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...


# FeaturePathCompoundPy.xml
class FeaturePathCompound(FreeCAD.DocumentObject):
    """This class handles Path Compound features"""

    def addObject(self, arg1: FreeCAD.DocumentObject, /):
        """Add an object to the group"""

    def removeObject(self, arg1: FreeCAD.DocumentObject, /):
        """Remove an object from the group"""


# AppPathPy.cpp
def write(object: object, filename: str, /):
    """write(object,filename): Exports a given path object to a GCode file"""


def read(filename: str, document: str = None, /):
    """read(filename,[document]): Imports a GCode file into the given document"""


def show(path: Path.Path, string: str = None, /):
    """show(path,[string]): Add the path to the active document or create one if no document exists"""


def fromShape(Shape: object, /):
    """fromShape(Shape): Returns a Path object from a Part Shape (deprecated - use fromShapes() instead)"""


def fromShapes(shapes: object, start: FreeCAD.Vector = None, return_end: object = None):
    """
    fromShapes(shapes, start=Vector(), return_end=False" PARAM_PY_ARGS_DOC(ARG,AREA_PARAMS_PATH) ")

    Returns a Path object from a list of shapes

    * shapes: input list of shapes.

    * start (Vector()): feed start position, and also serves as a hint of path entry.

    * return_end (False): if True, returns tuple (path, endPosition).
    "
                PARAM_PY_DOC(ARG, AREA_PARAMS_PATH)
    """


def sortWires(shapes: object, start: FreeCAD.Vector = None):
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
def setDefaultParams():
    """
    setDefaultParams(key=value...):
    Static method to set the default parameters of all following Path.Area, plus the following
    additional parameters.
    """


def getDefaultParams():
    """getDefaultParams(): Static method to return the current default parameters."""


def abort(aborting: object = None): ...


def getParamsDesc(as_string: object = False):
    """
    getParamsDesc(as_string=False): Returns a list of supported parameters and their descriptions.

    * as_string: if False, then return a dictionary of documents of all supported parameters.
    """
