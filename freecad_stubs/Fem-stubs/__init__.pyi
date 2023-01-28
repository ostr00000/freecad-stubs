import typing

import Fem
import FreeCAD
import Part as PartModule

LinkList_t: typing.TypeAlias = None | FreeCAD.DocumentObject


# FemMeshPy.xml
class FemMesh(FreeCAD.ComplexGeoData):
    """
    This class can be imported.
    FemMesh class
    """

    def __init__(self, pcObj=None, /):
        """
        FemMesh class
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    @property
    def EdgeCount(self) -> int:
        """Number of edges in the Mesh."""

    @property
    def Edges(self) -> tuple[int, ...]:
        """Tuple of edge IDs"""

    @property
    def EdgesOnly(self) -> tuple[int, ...]:
        """Tuple of edge IDs which does not belong to any face (and thus not belong to any volume too)"""

    @property
    def FaceCount(self) -> int:
        """Number of Faces in the Mesh."""

    @property
    def Faces(self) -> tuple[int, ...]:
        """Tuple of face IDs"""

    @property
    def FacesOnly(self) -> tuple[int, ...]:
        """Tuple of face IDs which does not belong to any volume"""

    @property
    def GroupCount(self) -> int:
        """Number of Groups in the Mesh."""

    @property
    def Groups(self) -> tuple[int, ...]:
        """Tuple of Group IDs."""

    @property
    def HexaCount(self) -> int:
        """Number of Hexas in the Mesh."""

    @property
    def NodeCount(self) -> int:
        """Number of nodes in the Mesh."""

    @property
    def Nodes(self) -> dict[int, FreeCAD.Vector]:
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
    def Volume(self) -> FreeCAD.Quantity:
        """Volume of the mesh."""

    @property
    def VolumeCount(self) -> int:
        """Number of Volumes in the Mesh."""

    @property
    def Volumes(self) -> tuple[int, ...]:
        """Tuple of volume IDs"""

    @typing.overload
    def addEdge(self, n1: int, n2: int, /) -> int: ...

    @typing.overload
    def addEdge(self, obj: list, ElementId: int = -1, /) -> int:
        """
        Add an edge by setting two node indices.
        Possible exceptions: (FreeCAD.Base.FreeCADError, TypeError).
        """

    @typing.overload
    def addFace(self, n1: int, n2: int, n3: int, /) -> int: ...

    @typing.overload
    def addFace(self, obj: list, ElementId: int = -1, /) -> int:
        """
        Add a face by setting three node indices.
        Possible exceptions: (FreeCAD.Base.FreeCADError, TypeError).
        """

    def addGroup(self, Name: str, typeString: str, theId: int = -1, /) -> int:
        """
        Add a group to mesh with specific name and type
                            addGroup(name, typestring, [id])
                            name: string
                            typestring: "All", "Node", "Edge", "Face", "Volume", "0DElement", "Ball"
                            id: int
                            Optional id is used to force specific id for group, but does
                            not work, yet.
                
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """

    def addGroupElements(self, id: int, pList: list, /):
        """
        Add a tuple of ElementIDs to a given group ID
                            addGroupElements(groupid, list_of_elements)
                            groupid: int
                            list_of_elements: list of int
                            Notice that the elements have to be in the mesh.
                
        Possible exceptions: (TypeError, FreeCAD.Base.CADKernelError).
        """

    def addHypothesis(self, hyp, shp: PartModule.Shape = None, /):
        """
        Add hypothesis
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    @typing.overload
    def addNode(self, x: float, y: float, z: float, /) -> int: ...

    @typing.overload
    def addNode(self, x: float, y: float, z: float, i: int = -1, /) -> int:
        """
        Add a node by setting (x,y,z).
        Possible exceptions: (FreeCAD.Base.FreeCADError, TypeError).
        """

    def addQuad(self, n1: int, n2: int, n3: int, n4: int, /) -> int:
        """
        Add a quad by setting four node indices.
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    @typing.overload
    def addVolume(self, n1: int, n2: int, n3: int, n4: int, /) -> int: ...

    @typing.overload
    def addVolume(self, obj: list, ElementId: int = -1, /) -> int:
        """
        Add a volume by setting an arbitrary number of node indices.
        Possible exceptions: (FreeCAD.Base.FreeCADError, TypeError).
        """

    def compute(self):
        """
        Update the internal mesh structure
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def copy(self) -> Fem.FemMesh:
        """Make a copy of this FEM mesh."""

    def getEdgesByEdge(self, pW: PartModule.Edge, /) -> list[int]:
        """
        Return a list of edge IDs which belong to a TopoEdge
        Possible exceptions: (ValueError, FreeCAD.Base.CADKernelError).
        """

    def getElementNodes(self, id: int, /) -> tuple[int, ...]:
        """
        Return a tuple of node IDs to a given element ID
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """

    def getElementType(self, id: int, /) -> str:
        """
        Return the element type of a given ID
        Possible exceptions: (ValueError).
        """

    def getFacesByFace(self, pW: PartModule.Face, /) -> list[int]:
        """
        Return a list of face IDs which belong to a TopoFace
        Possible exceptions: (ValueError, FreeCAD.Base.CADKernelError).
        """

    def getGroupElementType(self, id: int, /) -> str:
        """
        Return a string of group element type to a given group ID
        Possible exceptions: (ValueError).
        """

    def getGroupElements(self, id: int, /) -> tuple[int, ...]:
        """
        Return a tuple of ElementIDs to a given group ID
        Possible exceptions: (ValueError).
        """

    def getGroupName(self, id: int, /) -> str:
        """
        Return a string of group name to a given group ID
        Possible exceptions: (ValueError).
        """

    def getIdByElementType(self, str: str, /) -> tuple[int, ...]:
        """Return a tuple of IDs to a given element type"""

    def getNodeById(self, id: int, /) -> FreeCAD.Vector:
        """
        Get the node position vector by a Node-ID
        Possible exceptions: (ValueError).
        """

    def getNodesByEdge(self, pW: PartModule.Edge, /) -> list[int]:
        """
        Return a list of node IDs which belong to a TopoEdge
        Possible exceptions: (ValueError, FreeCAD.Base.CADKernelError).
        """

    def getNodesByFace(self, pW: PartModule.Face, /) -> list[int]:
        """
        Return a list of node IDs which belong to a TopoFace
        Possible exceptions: (ValueError, FreeCAD.Base.CADKernelError).
        """

    def getNodesBySolid(self, pW: PartModule.Solid, /) -> list[int]:
        """
        Return a list of node IDs which belong to a TopoSolid
        Possible exceptions: (ValueError, FreeCAD.Base.CADKernelError).
        """

    def getNodesByVertex(self, pW: PartModule.Vertex, /) -> list[int]:
        """
        Return a list of node IDs which belong to a TopoVertex
        Possible exceptions: (ValueError, FreeCAD.Base.CADKernelError).
        """

    def getVolumesByFace(self, pW: PartModule.Face, /) -> list[tuple[int, int]]:
        """
        Return a dict of volume IDs and face IDs which belong to a TopoFace
        Possible exceptions: (ValueError, FreeCAD.Base.CADKernelError).
        """

    def getccxVolumesByFace(self, pW: PartModule.Face, /) -> list[tuple[int, int]]:
        """
        Return a dict of volume IDs and ccx face numbers which belong to a TopoFace
        Possible exceptions: (ValueError, FreeCAD.Base.CADKernelError).
        """

    def read(self, Name: str, /):
        """
        Read in a various FEM mesh file formats.
                            read(file.endingToExportTo)
                            supported formats: DAT, INP, MED, STL, UNV, VTK, Z88
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def removeGroup(self, theId: int, /) -> bool:
        """
        Remove a group with a given group ID
                            removeGroup(groupid)
                            groupid: int
                            Returns boolean.
        """

    def setShape(self, pcObj: PartModule.Shape, /):
        """
        Set the Part shape to mesh
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def setStandardHypotheses(self):
        """
        Set some standard hypotheses for the whole shape
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def setTransform(self, ptr: FreeCAD.Placement, /):
        """Use a Placement object to perform a translation or rotation"""

    def write(self, Name: str, /):
        """
        Write out various FEM mesh file formats.
                            write(file.endingToExportTo)
                            supported formats: BDF, DAT, INP, MED, STL, UNV, VTK, Z88
                
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def writeABAQUS(self, Name: str, elemParam: int, groupParam: bool, /):
        """
        Write out as ABAQUS inp
                            writeABAQUS(file, int elemParam, bool groupParam)
                            elemParam: 0 = all elements, 1 = highest elements only, 2 = FEM elements only (only edges not belonging to faces and faces not belonging to volumes)
                            groupParam: true = write group data, false = do not write group data
                
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """


# FemPostPipelinePy.xml
class FemPostPipeline(FreeCAD.GeoFeature):
    """The FemPostPipeline class."""

    @property
    def Filter(self) -> list[FreeCAD.DocumentObject | None]:
        """
        Property group: Pipeline.
        Property TypeId: App::PropertyLinkList.
        The filter used in this pipeline.
        """

    @Filter.setter
    def Filter(self, value: LinkList_t): ...

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
    def Mode(self) -> int:
        """
        Property group: Pipeline.
        Property TypeId: App::PropertyEnumeration.

        Selects the pipeline data transition mode.
        In serial, every filter gets the output of the previous one as input.
        In parallel, every filter gets the pipeline source as input.
        In custom, every filter keeps its input set by the user.
        """

    @Mode.setter
    def Mode(self, value: typing.Literal['Serial', 'Parallel', 'Custom']): ...

    def getLastPostObject(self) -> FreeCAD.DocumentObject:
        """Get the last post-processing object"""

    def holdsPostObject(self, py: FreeCAD.DocumentObject, /) -> bool:
        """
        Check if this pipeline holds a given post-processing object
        Possible exceptions: (TypeError).
        """

    def load(self, py: FreeCAD.DocumentObject, /):
        """
        Load a result object
        Possible exceptions: (TypeError).
        """

    def read(self, Name: str, /):
        """Read in vtk file"""

    def recomputeChildren(self):
        """Recomputes all children of the pipeline"""

    def scale(self, scale: float, /):
        """scale the points of a loaded vtk file"""


# AppFemPy.cpp
def open(Name: str, /) -> None:
    """
    open(string) -- Create a new document and a Mesh::Import feature to load the file into the document.
    Possible exceptions: (Exception).
    """


def insert(Name: str, DocName: str = None, /) -> None:
    """
    insert(string|mesh,[string]) -- Load or insert a mesh into the given or active document.
    Possible exceptions: (Exception).
    """


def export(object, Name: str, /) -> None:
    """
    export(list,string) -- Export a list of objects into a single file.
    Possible exceptions: (Exception).
    """


def read(Name: str, /) -> Fem.FemMesh:
    """
    Read a mesh from a file and returns a Mesh object.
    Possible exceptions: (Exception).
    """


def readResult(fileName: str = None, objName: str = None, /) -> None:
    """
    Read a CFD or Mechanical result (auto detect) from a file (file format detected from file suffix)
    Possible exceptions: (Exception).
    """


def writeResult(fileName: str = None, pcObj: FreeCAD.DocumentObject = None, /) -> None:
    """
    write a CFD or FEM result (auto detect) to a file (file format detected from file suffix)
    Possible exceptions: (Exception).
    """


def show(pcObj: Fem.FemMesh, name: str = 'Mesh', /) -> None:
    """
    show(shape,[string]) -- Add the mesh to the active document or create one if no document exists.
    Possible exceptions: (Exception).
    """


# HypothesisPy.cpp
class StdMeshers_Arithmetic1D:
    """StdMeshers_Arithmetic1D"""

    def setLength(self) -> None:
        """setLength()"""

    @typing.overload
    def getLength(self): ...

    @typing.overload
    def getLength(self, start: int, /) -> float:
        """
        getLength()
        Possible exceptions: (Exception).
        """


class StdMeshers_AutomaticLength:
    """StdMeshers_AutomaticLength"""

    def setFineness(self) -> None:
        """setFineness()"""

    def getFineness(self) -> float:
        """
        getFineness()
        Possible exceptions: (Exception).
        """

    def getLength(self) -> float:
        """getLength()"""


class StdMeshers_NotConformAllowed:
    """StdMeshers_NotConformAllowed"""

    pass
class StdMeshers_MaxLength:
    """StdMeshers_MaxLength"""

    def setLength(self) -> None:
        """setLength()"""

    def getLength(self) -> float:
        """
        getLength()
        Possible exceptions: (Exception).
        """

    def havePreestimatedLength(self) -> bool:
        """
        havePreestimatedLength()
        Possible exceptions: (Exception).
        """

    def getPreestimatedLength(self) -> float:
        """
        getPreestimatedLength()
        Possible exceptions: (Exception).
        """

    def setPreestimatedLength(self) -> None:
        """setPreestimatedLength()"""

    def setUsePreestimatedLength(self) -> None:
        """setUsePreestimatedLength()"""

    def getUsePreestimatedLength(self) -> bool:
        """
        getUsePreestimatedLength()
        Possible exceptions: (Exception).
        """


class StdMeshers_LocalLength:
    """StdMeshers_LocalLength"""

    def setLength(self) -> None:
        """setLength()"""

    def getLength(self) -> float:
        """
        getLength()
        Possible exceptions: (Exception).
        """

    def setPrecision(self) -> None:
        """setPrecision()"""

    def getPrecision(self) -> float:
        """
        getPrecision()
        Possible exceptions: (Exception).
        """


class StdMeshers_MaxElementArea:
    """StdMeshers_MaxElementArea"""

    def setMaxArea(self) -> None:
        """setMaxArea()"""

    def getMaxArea(self) -> float:
        """
        getMaxArea()
        Possible exceptions: (Exception).
        """


class StdMeshers_QuadranglePreference:
    """StdMeshers_QuadranglePreference"""

    pass
class StdMeshers_Quadrangle_2D:
    """StdMeshers_Quadrangle_2D"""

    pass
class StdMeshers_Regular_1D:
    """StdMeshers_Regular_1D"""

    pass
class StdMeshers_UseExisting_1D:
    """StdMeshers_UseExisting_1D"""

    pass
class StdMeshers_UseExisting_2D:
    """StdMeshers_UseExisting_2D"""

    pass
class StdMeshers_CompositeSegment_1D:
    """StdMeshers_CompositeSegment_1D"""

    pass
class StdMeshers_Deflection1D:
    """StdMeshers_Deflection1D"""

    def setDeflection(self) -> None:
        """setDeflection()"""


class StdMeshers_Hexa_3D:
    """StdMeshers_Hexa_3D"""

    pass
class StdMeshers_TrianglePreference:
    """StdMeshers_TrianglePreference"""

    pass
class StdMeshers_StartEndLength:
    """StdMeshers_StartEndLength"""

    def setLength(self) -> None:
        """setLength()"""

    def getLength(self) -> float:
        """getLength()"""


class StdMeshers_SegmentLengthAroundVertex:
    """StdMeshers_SegmentLengthAroundVertex"""

    def setLength(self) -> None:
        """setLength()"""

    def getLength(self) -> float:
        """
        getLength()
        Possible exceptions: (Exception).
        """


class StdMeshers_SegmentAroundVertex_0D:
    """StdMeshers_SegmentAroundVertex_0D"""

    pass
class StdMeshers_RadialPrism_3D:
    """StdMeshers_RadialPrism_3D"""

    pass
class StdMeshers_QuadraticMesh:
    """StdMeshers_QuadraticMesh"""

    pass
class StdMeshers_ProjectionSource3D:
    """StdMeshers_ProjectionSource3D"""

    pass
class StdMeshers_ProjectionSource2D:
    """StdMeshers_ProjectionSource2D"""

    pass
class StdMeshers_ProjectionSource1D:
    """StdMeshers_ProjectionSource1D"""

    pass
class StdMeshers_Projection_3D:
    """StdMeshers_Projection_3D"""

    pass
class StdMeshers_Projection_2D:
    """StdMeshers_Projection_2D"""

    pass
class StdMeshers_Projection_1D:
    """StdMeshers_Projection_1D"""

    pass
class StdMeshers_Prism_3D:
    """StdMeshers_Prism_3D"""

    pass
class StdMeshers_NumberOfSegments:
    """StdMeshers_NumberOfSegments"""

    def setNumberOfSegments(self) -> None:
        """setNumberOfSegments()"""

    def getNumberOfSegments(self) -> int:
        """
        getNumberOfSegments()
        Possible exceptions: (Exception).
        """


class StdMeshers_NumberOfLayers:
    """StdMeshers_NumberOfLayers"""

    def setNumberOfLayers(self) -> None:
        """setNumberOfLayers()"""

    def getNumberOfLayers(self) -> int:
        """
        getNumberOfLayers()
        Possible exceptions: (Exception).
        """


class StdMeshers_MEFISTO_2D:
    """StdMeshers_MEFISTO_2D"""

    pass
class StdMeshers_MaxElementVolume:
    """StdMeshers_MaxElementVolume"""

    def setMaxVolume(self) -> None:
        """setMaxVolume()"""

    def getMaxVolume(self) -> float:
        """
        getMaxVolume()
        Possible exceptions: (Exception).
        """


class StdMeshers_LengthFromEdges:
    """StdMeshers_LengthFromEdges"""

    def setMode(self) -> None:
        """setMode()"""

    def getMode(self) -> int:
        """
        getMode()
        Possible exceptions: (Exception).
        """


class StdMeshers_LayerDistribution:
    """StdMeshers_LayerDistribution"""

    def setLayerDistribution(self) -> None:
        """
        setLayerDistribution()
        Possible exceptions: (Exception).
        """

    def getLayerDistribution(self) -> None:
        """
        getLayerDistribution()
        Possible exceptions: (Exception).
        """
