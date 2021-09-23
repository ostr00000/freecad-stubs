import typing

import Fem
import FreeCAD
import Part


# FemMeshPy.xml
class FemMesh(FreeCAD.ComplexGeoData):
    """
    This class can be imported.
    FemMesh class
    """

    def __init__(self, arg1: object = None, /):
        """FemMesh class"""

    @property
    def EdgeCount(self) -> int:
        """Number of edges in the Mesh."""

    @property
    def Edges(self) -> tuple:
        """Tuple of edge IDs"""

    @property
    def EdgesOnly(self) -> tuple:
        """Tuple of edge IDs which does not belong to any face (and thus not belong to any volume too)"""

    @property
    def FaceCount(self) -> int:
        """Number of Faces in the Mesh."""

    @property
    def Faces(self) -> tuple:
        """Tuple of face IDs"""

    @property
    def FacesOnly(self) -> tuple:
        """Tuple of face IDs which does not belong to any volume"""

    @property
    def GroupCount(self) -> int:
        """Number of Groups in the Mesh."""

    @property
    def Groups(self) -> tuple:
        """Tuple of Group IDs."""

    @property
    def HexaCount(self) -> int:
        """Number of Hexas in the Mesh."""

    @property
    def NodeCount(self) -> int:
        """Number of nodes in the Mesh."""

    @property
    def Nodes(self) -> dict:
        """Dictionary of Nodes by ID (int ID:Vector())"""

    @property
    def PolygonCount(self) -> int:
        """Number of Quadrangles in the Mesh."""

    @property
    def PolyhedronCount(self) -> int:
        """Number of Polyhedrons in the Mesh."""

    @property
    def PrismCount(self) -> int:
        """Number of Prisms in the Mesh."""

    @property
    def PyramidCount(self) -> int:
        """Number of Pyramids in the Mesh."""

    @property
    def QuadrangleCount(self) -> int:
        """Number of Quadrangles in the Mesh."""

    @property
    def SubMeshCount(self) -> int:
        """Number of SubMeshs in the Mesh."""

    @property
    def TetraCount(self) -> int:
        """Number of Tetras in the Mesh."""

    @property
    def TriangleCount(self) -> int:
        """Number of Triangles in the Mesh."""

    @property
    def Volume(self) -> object:
        """Volume of the mesh."""

    @property
    def VolumeCount(self) -> int:
        """Number of Volumes in the Mesh."""

    @property
    def Volumes(self) -> tuple:
        """Tuple of volume IDs"""

    @typing.overload
    def addEdge(self, arg1: int, arg2: int, /): ...

    @typing.overload
    def addEdge(self, arg1: list, arg2: int = None, /):
        """Add an edge by setting two node indices."""

    @typing.overload
    def addFace(self, arg1: int, arg2: int, arg3: int, /): ...

    @typing.overload
    def addFace(self, arg1: list, arg2: int = None, /):
        """Add a face by setting three node indices."""

    def addGroup(self, name: str, typestring: str, id: int = None, /):
        """
        Add a group to mesh with specific name and type
                            addGroup(name, typestring, [id])
                            name: string
                            typestring: "All", "Node", "Edge", "Face", "Volume", "0DElement", "Ball"
                            id: int
                            Optional id is used to force specific id for group, but does
                            not work, yet.
        """

    def addGroupElements(self, groupid: int, list_of_elements: list, /):
        """
        Add a tuple of ElementIDs to a given group ID
                            addGroupElements(groupid, list_of_elements)
                            groupid: int
                            list_of_elements: list of int
                            Notice that the elements have to be in the mesh.
        """

    def addHypothesis(self, arg1: object, arg2: Part.Shape = None, /):
        """Add hypothesis"""

    @typing.overload
    def addNode(self, arg1: float, arg2: float, arg3: float, /): ...

    @typing.overload
    def addNode(self, arg1: float, arg2: float, arg3: float, arg4: int, /):
        """Add a node by setting (x,y,z)."""

    def addQuad(self, arg1: int, arg2: int, arg3: int, arg4: int, /):
        """Add a quad by setting four node indices."""

    @typing.overload
    def addVolume(self, arg1: int, arg2: int, arg3: int, arg4: int, /): ...

    @typing.overload
    def addVolume(self, arg1: list, arg2: int = None, /):
        """Add a volume by setting an arbitrary number of node indices."""

    def compute(self):
        """Update the internal mesh structure"""

    def copy(self):
        """Make a copy of this FEM mesh."""

    def getEdgesByEdge(self, arg1: Part.Edge, /):
        """Return a list of edge IDs which belong to a TopoEdge"""

    def getElementNodes(self, arg1: int, /):
        """Return a tuple of node IDs to a given element ID"""

    def getElementType(self, arg1: int, /):
        """Return the element type of a given ID"""

    def getFacesByFace(self, arg1: Part.Face, /):
        """Return a list of face IDs which belong to a TopoFace"""

    def getGroupElementType(self, arg1: int, /):
        """Return a string of group element type to a given group ID"""

    def getGroupElements(self, arg1: int, /):
        """Return a tuple of ElementIDs to a given group ID"""

    def getGroupName(self, arg1: int, /):
        """Return a string of group name to a given group ID"""

    def getIdByElementType(self, arg1: str, /):
        """Return a tuple of IDs to a given element type"""

    def getNodeById(self, arg1: int, /):
        """Get the node position vector by a Node-ID"""

    def getNodesByEdge(self, arg1: Part.Edge, /):
        """Return a list of node IDs which belong to a TopoEdge"""

    def getNodesByFace(self, arg1: Part.Face, /):
        """Return a list of node IDs which belong to a TopoFace"""

    def getNodesBySolid(self, arg1: Part.Solid, /):
        """Return a list of node IDs which belong to a TopoSolid"""

    def getNodesByVertex(self, arg1: Part.Vertex, /):
        """Return a list of node IDs which belong to a TopoVertex"""

    def getVolumesByFace(self, arg1: Part.Face, /):
        """Return a dict of volume IDs and face IDs which belong to a TopoFace"""

    def getccxVolumesByFace(self, arg1: Part.Face, /):
        """Return a dict of volume IDs and ccx face numbers which belong to a TopoFace"""

    def read(self, file_endingToExportTo: str, /):
        """
        Read in a various FEM mesh file formats.
                            read(file.endingToExportTo)
                            supported formats: DAT, INP, MED, STL, UNV, VTK, Z88
        """

    def removeGroup(self, groupid: int, /):
        """
        Remove a group with a given group ID
                            removeGroup(groupid)
                            groupid: int
                            Returns boolean.
        """

    def setShape(self, arg1: Part.Shape, /):
        """Set the Part shape to mesh"""

    def setStandardHypotheses(self):
        """Set some standard hypotheses for the whole shape"""

    def setTransform(self, arg1: FreeCAD.Placement, /):
        """Use a Placement object to perform a translation or rotation"""

    def write(self, file_endingToExportTo: str, /):
        """
        Write out various FEM mesh file formats.
                            write(file.endingToExportTo)
                            supported formats: BDF, DAT, INP, MED, STL, UNV, VTK, Z88
        """

    def writeABAQUS(self, file: str, int_elemParam: int, bool_groupParam: bool, /):
        """
        Write out as ABAQUS inp
                            writeABAQUS(file, int elemParam, bool groupParam)
                            elemParam: 0 = all elements, 1 = highest elements only, 2 = FEM elements only (only edges not belonging to faces and faces not belonging to volumes)
                            groupParam: true = write group data, false = do not write group data
        """


# FemPostPipelinePy.xml
class FemPostPipeline(FreeCAD.GeoFeature):
    """The FemPostPipeline class."""

    @property
    def Filter(self) -> dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]:
        """
        Property group: Pipeline.
        Property TypeId: App::PropertyLinkList.
        The filter used in this pipeline.
        """

    @Filter.setter
    def Filter(self, value: dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]): ...

    @property
    def Functions(self) -> FreeCAD.DocumentObject | None:
        """
        [Prop_Hidden] Property won't appear in the editor.
        Property group: Pipeline.
        Property TypeId: App::PropertyLink.
        The function provider which groups all pipeline functions.
        """

    @Functions.setter
    def Functions(self, value: FreeCAD.DocumentObject | None): ...

    @property
    def Mode(self) -> typing.Literal['Serial', 'Parallel']:
        """
        Property group: Pipeline.
        Property TypeId: App::PropertyEnumeration.
        Selects the pipeline data transition mode. In serial, every filtergets the output of the previous one as input. In parallel, everyfilter gets the pipeline source as input.
        """

    @Mode.setter
    def Mode(self, value: typing.Literal['Serial', 'Parallel']): ...

    def getLastPostObject(self):
        """Get the last post-processing object"""

    def holdsPostObject(self, arg1: FreeCAD.DocumentObject, /):
        """Check if this pipeline holds a given post-processing object"""

    def load(self, arg1: FreeCAD.DocumentObject, /):
        """Load a result object"""

    def read(self, arg1: str, /):
        """Read in vtk file"""


# AppFemPy.cpp
def open(string: str, /):
    """open(string) -- Create a new document and a Mesh::Import feature to load the file into the document."""


def insert(string_mesh: str, string: str = None, /):
    """insert(string|mesh,[string]) -- Load or insert a mesh into the given or active document."""


def export(list: object, string: str, /):
    """export(list,string) -- Export a list of objects into a single file."""


def read(arg1: str, /):
    """Read a mesh from a file and returns a Mesh object."""


def readResult(arg1: str, arg2: str = None, /):
    """Read a CFD or Mechanical result (auto detect) from a file (file format detected from file suffix)"""


def writeResult(arg1: str, arg2: FreeCAD.DocumentObject = None, /):
    """write a CFD or FEM result (auto detect) to a file (file format detected from file suffix)"""


def show(shape: Fem.FemMesh, string: str = None, /):
    """show(shape,[string]) -- Add the mesh to the active document or create one if no document exists."""


# HypothesisPy.cpp
class StdMeshers_Arithmetic1D:
    """StdMeshers_Arithmetic1D"""

    def setLength(self):
        """setLength()"""

    def getLength(self, arg1: int, /):
        """getLength()"""


class StdMeshers_AutomaticLength:
    """StdMeshers_AutomaticLength"""

    def setFineness(self):
        """setFineness()"""

    def getFineness(self):
        """getFineness()"""

    def getLength(self):
        """getLength()"""


class StdMeshers_MaxLength:
    """StdMeshers_MaxLength"""

    def setLength(self):
        """setLength()"""

    def getLength(self):
        """getLength()"""

    def havePreestimatedLength(self):
        """havePreestimatedLength()"""

    def getPreestimatedLength(self):
        """getPreestimatedLength()"""

    def setPreestimatedLength(self):
        """setPreestimatedLength()"""

    def setUsePreestimatedLength(self):
        """setUsePreestimatedLength()"""

    def getUsePreestimatedLength(self):
        """getUsePreestimatedLength()"""


class StdMeshers_LocalLength:
    """StdMeshers_LocalLength"""

    def setLength(self):
        """setLength()"""

    def getLength(self):
        """getLength()"""

    def setPrecision(self):
        """setPrecision()"""

    def getPrecision(self):
        """getPrecision()"""


class StdMeshers_MaxElementArea:
    """StdMeshers_MaxElementArea"""

    def setMaxArea(self):
        """setMaxArea()"""

    def getMaxArea(self):
        """getMaxArea()"""


class StdMeshers_Deflection1D:
    """StdMeshers_Deflection1D"""

    def setDeflection(self):
        """setDeflection()"""


class StdMeshers_StartEndLength:
    """StdMeshers_StartEndLength"""

    def setLength(self):
        """setLength()"""

    def getLength(self):
        """getLength()"""


class StdMeshers_SegmentLengthAroundVertex:
    """StdMeshers_SegmentLengthAroundVertex"""

    def setLength(self):
        """setLength()"""

    def getLength(self):
        """getLength()"""


class StdMeshers_NumberOfSegments:
    """StdMeshers_NumberOfSegments"""

    def setNumberOfSegments(self):
        """setNumberOfSegments()"""

    def getNumberOfSegments(self):
        """getNumberOfSegments()"""


class StdMeshers_NumberOfLayers:
    """StdMeshers_NumberOfLayers"""

    def setNumberOfLayers(self):
        """setNumberOfLayers()"""

    def getNumberOfLayers(self):
        """getNumberOfLayers()"""


class StdMeshers_MaxElementVolume:
    """StdMeshers_MaxElementVolume"""

    def setMaxVolume(self):
        """setMaxVolume()"""

    def getMaxVolume(self):
        """getMaxVolume()"""


class StdMeshers_LengthFromEdges:
    """StdMeshers_LengthFromEdges"""

    def setMode(self):
        """setMode()"""

    def getMode(self):
        """getMode()"""


class StdMeshers_LayerDistribution:
    """StdMeshers_LayerDistribution"""

    def setLayerDistribution(self):
        """setLayerDistribution()"""

    def getLayerDistribution(self):
        """getLayerDistribution()"""
