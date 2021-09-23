import typing

import FreeCAD
import Mesh


# FacetPy.xml
class Facet(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    Facet in mesh
    This is a facet in a MeshObject. You can get it by e.g. iterating a
    mesh. The facet has a connection to its mesh and allows therefore
    topological operations. It is also possible to create an unbounded facet e.g. to create
    a mesh. In this case the topological operations will fail. The same is
    when you cut the bound to the mesh by calling unbound().
    """

    def __init__(self):
        """
        Facet in mesh
        This is a facet in a MeshObject. You can get it by e.g. iterating a
        mesh. The facet has a connection to its mesh and allows therefore
        topological operations. It is also possible to create an unbounded facet e.g. to create
        a mesh. In this case the topological operations will fail. The same is
        when you cut the bound to the mesh by calling unbound().
        """

    @property
    def Area(self) -> float:
        """The area of the facet"""

    @property
    def AspectRatio(self) -> float:
        """The aspect ratio of the facet computed by longest edge and its height"""

    @property
    def AspectRatio2(self) -> float:
        """The aspect ratio of the facet computed by radius of circum-circle and in-circle"""

    @property
    def Bound(self) -> bool:
        """Bound state of the facet"""

    @property
    def CircumCircle(self) -> tuple:
        """The center and radius of the circum-circle"""

    @property
    def InCircle(self) -> tuple:
        """The center and radius of the in-circle"""

    @property
    def Index(self) -> int:
        """The index of this facet in the MeshObject"""

    @property
    def NeighbourIndices(self) -> tuple:
        """The index tuple of neighbour facets of the mesh this facet is adjacent with"""

    @property
    def Normal(self) -> object:
        """Normal vector of the facet."""

    @property
    def PointIndices(self) -> tuple:
        """The index tuple of point vertices of the mesh this facet is built of"""

    @property
    def Points(self) -> list:
        """A list of points of the facet"""

    @property
    def Roundness(self) -> float:
        """The roundness of the facet"""

    def intersect(self, Facet: Mesh.Facet, /):
        """
        intersect(Facet) -> list 
        Get a list of intersection points with another triangle.
        """

    def isDeformed(self, arg1: float, arg2: float, /):
        """
        isDegenerated(MinAngle, MaxAngle) -> boolean
        Returns true if the facet is deformed, otherwise false.
        A triangle is considered deformed if an angle is less than MinAngle
        or higher than MaxAngle.
        The two angles are given in radian.
        """

    def isDegenerated(self, float: float = None, /):
        """
        isDegenerated([float]) -> boolean
        Returns true if the facet is degenerated, otherwise false.
        """

    def unbound(self):
        """
        method unbound()
        Cut the connection to a MeshObject. The facet becomes
        free and is more or less a simple facet.
        After calling unbound() no topological operation will
        work!
        """


# MeshPointPy.xml
class MeshPoint(FreeCAD.PyObjectBase):
    """
    This class can be imported.
     Point in mesh
    This is a point in a MeshObject. You can get it by e.g. iterating a
    mesh. The point has a connection to its mesh and allows therefore 
    topological operations. It is also possible to create an unbounded mesh point e.g. to create
    a mesh. In this case the topological operations will fail. The same is
    when you cut the bound to the mesh by calling unbound().
    """

    def __init__(self, arg1: float = None, arg2: float = None, arg3: float = None, /):
        """
        Point in mesh
        This is a point in a MeshObject. You can get it by e.g. iterating a
        mesh. The point has a connection to its mesh and allows therefore 
        topological operations. It is also possible to create an unbounded mesh point e.g. to create
        a mesh. In this case the topological operations will fail. The same is
        when you cut the bound to the mesh by calling unbound().
        """

    @property
    def Bound(self) -> bool:
        """Bound state of the point"""

    @property
    def Index(self) -> int:
        """The index of this point in the MeshObject"""

    @property
    def Normal(self) -> object:
        """Normal vector of the point computed by the surrounding mesh."""

    @property
    def Vector(self) -> object:
        """Vector of the point."""

    @property
    def x(self) -> float:
        """
        The X component of the point.
        Setting this value also affects the mesh if this point is connected to it.
        """

    @x.setter
    def x(self, value: float): ...

    @property
    def y(self) -> float:
        """
        The Y component of the point.
        Setting this value also affects the mesh if this point is connected to it.
        """

    @y.setter
    def y(self, value: float): ...

    @property
    def z(self) -> float:
        """
        The Z component of the point.
        Setting this value also affects the mesh if this point is connected to it.
        """

    @z.setter
    def z(self, value: float): ...

    def move(self, Vector: FreeCAD.Vector, /):
        """
        method move(Vector)
        This method moves the point in the mesh along the 
        given vector. This affects the geometry of the mesh.
        Be aware that after moving point(s) the mesh can 
        have self intersections!
        """

    def unbound(self):
        """
        method unbound()
        Cut the connection to a MeshObject. The point becomes
        free and is more or less a simple vector/point.
        After calling unbound() no topological operation will
        work!
        """


# MeshFeaturePy.xml
class Feature(FreeCAD.GeoFeature):
    """
    This class can be imported.
    The Mesh::Feature class handles meshes.
    The Mesh.MeshFeature() function is for internal use only and cannot be used to create instances of this class.
    Therefore you must have a reference to a document, e.g. 'd' then you can create an instance with
    d.addObject("Mesh::Feature").
    """

    def __init__(self):
        """
        The Mesh::Feature class handles meshes.
        The Mesh.MeshFeature() function is for internal use only and cannot be used to create instances of this class.
        Therefore you must have a reference to a document, e.g. 'd' then you can create an instance with
        d.addObject("Mesh::Feature").
        """

    @property
    def Mesh(self):
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: PropertyMeshKernel.
        The mesh kernel.
        """

    @Mesh.setter
    def Mesh(self, value): ...

    def fixDegenerations(self, arg1: float = None, /):
        """Remove degenerated facets"""

    def fixIndices(self):
        """Repair any invalid indices"""

    def fixSelfIntersections(self):
        """Repair self-intersections"""

    def harmonizeNormals(self):
        """Adjust wrong oriented facets"""

    def removeDuplicatedFacets(self):
        """Remove duplicated facets"""

    def removeDuplicatedPoints(self):
        """Remove duplicated points"""

    def removeFoldsOnSurface(self):
        """Remove folds on surfaces"""

    def removeInvalidPoints(self):
        """Remove points with invalid coordinates (NaN)"""

    def removeNonManifoldPoints(self):
        """Remove non-manifold points"""

    def removeNonManifolds(self):
        """Remove non-manifolds"""

    def smooth(self, arg1: int = None, arg2: float = None, /):
        """Smooth the mesh data"""


# MeshPy.xml
class Mesh(FreeCAD.ComplexGeoData):
    """
    This class can be imported.
    Mesh() -- Create an empty mesh object.

    This class allows one to manipulate the mesh object by adding new facets, deleting facets, importing from an STL file,
    transforming the mesh and much more.
    For a complete overview of what can be done see also the documentation of mesh.
    A mesh object cannot be added to an existing document directly. Therefore the document must create an object
    with a property class that supports meshes.
    Example:
      m = Mesh.Mesh()
      ... # Manipulate the mesh
      d = FreeCAD.activeDocument() # Get a reference to the actie document
      f = d.addObject("Mesh::Feature", "Mesh") # Create a mesh feature
      f.Mesh = m # Assign the mesh object to the internal property
      d.recompute()
    """

    def __init__(self, arg1: object = None, /):
        """
        Mesh() -- Create an empty mesh object.

        This class allows one to manipulate the mesh object by adding new facets, deleting facets, importing from an STL file,
        transforming the mesh and much more.
        For a complete overview of what can be done see also the documentation of mesh.
        A mesh object cannot be added to an existing document directly. Therefore the document must create an object
        with a property class that supports meshes.
        Example:
          m = Mesh.Mesh()
          ... # Manipulate the mesh
          d = FreeCAD.activeDocument() # Get a reference to the actie document
          f = d.addObject("Mesh::Feature", "Mesh") # Create a mesh feature
          f.Mesh = m # Assign the mesh object to the internal property
          d.recompute()
        """

    @property
    def Area(self) -> float:
        """Return the area of the mesh object."""

    @property
    def CountEdges(self) -> int:
        """Return the number of edges of the mesh object."""

    @property
    def CountFacets(self) -> int:
        """Return the number of facets of the mesh object."""

    @property
    def CountPoints(self) -> int:
        """Return the number of vertices of the mesh object."""

    @property
    def Facets(self) -> list:
        """
        A collection of facets
        With this attribute it is possible to get access to the facets of the mesh
        for p in mesh.Facets:
        	print p
        """

    @property
    def Points(self) -> list:
        """
        A collection of the mesh points
        With this attribute it is possible to get access to the points of the mesh
        for p in mesh.Points:
        	print p.x, p.y, p.z
        """

    @property
    def Topology(self) -> tuple:
        """Return the points and face indices as tuple."""

    @property
    def Volume(self) -> float:
        """Return the volume of the mesh object."""

    @typing.overload
    def addFacet(self, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, /): ...

    @typing.overload
    def addFacet(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, arg3: FreeCAD.Vector, /): ...

    @typing.overload
    def addFacet(self, arg1: Mesh.Facet, /):
        """Add a facet to the mesh"""

    @typing.overload
    def addFacets(self, arg1: list, /): ...

    @typing.overload
    def addFacets(self, arg1: tuple, arg2: bool = None, /):
        """Add a list of facets to the mesh"""

    def addMesh(self, arg1: Mesh.Mesh, /):
        """Combine this mesh with another mesh."""

    def clear(self):
        """Clear the mesh"""

    def coarsen(self):
        """Coarse the mesh"""

    def collapseEdge(self, arg1: int, arg2: int, /):
        """Remove an edge and both facets that share this edge"""

    def collapseFacet(self, arg1: int, /):
        """Remove a facet"""

    def collapseFacets(self, arg1: object, /):
        """Remove a list of facets"""

    def copy(self):
        """Create a copy of this mesh"""

    def countComponents(self):
        """Get the number of topologic independent areas"""

    def countNonUniformOrientedFacets(self):
        """Get the number of wrong oriented facets"""

    def countSegments(self):
        """Get the number of segments which may also be 0"""

    def crossSections(self, arg1: object, arg2: float = None, arg3: bool = None, /):
        """Get cross-sections of the mesh through several planes"""

    def cut(self, list: object, int: int, /):
        """
        Cuts the mesh with a given closed polygon
        cut(list, int) -> None
        The argument list is an array of points, a polygon
        The argument int is the mode: 0=inner, 1=outer
        """

    @typing.overload
    def decimate(self, tolerance_Float_: float, reduction_Float_: float, /): ...

    @typing.overload
    def decimate(self, arg: float, arg2: float, /):
        """
        Decimate the mesh
        					decimate(tolerance(Float), reduction(Float))
        					tolerance: maximum error
        					reduction: reduction factor must be in the range [0.0,1.0]
        					Example:
        					mesh.decimate(0.5, 0.1) # reduction by up to 10 percent
        					mesh.decimate(0.5, 0.9) # reduction by up to 90 percent
        """

    def difference(self, arg1: Mesh.Mesh, /):
        """Difference of this and the given mesh object."""

    def fillupHoles(self, arg1: int, arg2: int = None, arg3: float = None, /):
        """Fillup holes"""

    def fixCaps(self, arg1: float = None, arg2: float = None, /):
        """Repair caps by swapping the edge"""

    def fixDeformations(self, arg1: float, arg2: float = None, /):
        """Repair deformed facets"""

    def fixDegenerations(self, arg1: float = None, /):
        """Remove degenerated facets"""

    def fixIndices(self):
        """Repair any invalid indices"""

    def fixSelfIntersections(self):
        """Repair self-intersections"""

    def flipNormals(self):
        """Flip the mesh normals"""

    def foraminate(self, arg1: object, arg2: object, /):
        """Get a list of facet indices and intersection points"""

    def getCurvaturePerVertex(self):
        """
        getCurvaturePerVertex() -> list
        The items in the list contains minimum and maximum curvature with their directions
        """

    def getEigenSystem(self):
        """Get Eigen base of the mesh"""

    def getFacetSelection(self):
        """Get a list of the indices of selected facets"""

    def getInternalFacets(self):
        """Builds a list of facet indices with triangles that are inside a volume mesh"""

    def getNonUniformOrientedFacets(self):
        """Get a tuple of wrong oriented facets"""

    def getPlanarSegments(self, dev: float, min_faces: int = 0, /):
        """
        getPlanarSegments(dev,[min faces=0]) -> list
        Get all planes of the mesh as segment.
        In the worst case each triangle can be regarded as single
        plane if none of its neighbors are coplanar.
        """

    def getPointNormals(self):
        """
        getPointNormals()
        					Get the normals of the points.
        """

    def getPointSelection(self):
        """Get a list of the indices of selected points"""

    def getSegment(self, arg1: int, /):
        """Get a list of facet indices that describes a segment"""

    def getSegmentsByCurvature(self, list: object, /):
        """
        getSegmentsByCurvature(list) -> list
        The argument list gives a list if tuples where it defines the preferred maximum curvature,
        the preferred minimum curvature, the tolerances and the number of minimum faces for the segment.
        Example:
        c=(1.0, 0.0, 0.1, 0.1, 500) # search for a cylinder with radius 1.0
        p=(0.0, 0.0, 0.1, 0.1, 500) # search for a plane
        mesh.getSegmentsByCurvature([c,p])
        """

    def getSegmentsOfType(self, type: str, dev: float, min_faces: int = 0, /):
        """
        getSegmentsOfType(type, dev,[min faces=0]) -> list
        Get all segments of type.
        Type can be Plane, Cylinder or Sphere
        """

    def getSelfIntersections(self):
        """Returns a tuple of indices of intersecting triangles"""

    def getSeparateComponents(self):
        """
        Returns a list containing the different
        components (separated areas) of the mesh as separate meshes

        import Mesh
        for c in mesh.getSeparatecomponents():
        	Mesh.show(c)
        """

    def harmonizeNormals(self):
        """Adjust wrong oriented facets"""

    def hasCorruptedFacets(self):
        """Check if the mesh has corrupted facets"""

    def hasFacetsOutOfRange(self):
        """Check if the mesh has facet indices that are out of range"""

    def hasInvalidNeighbourhood(self):
        """Check if the mesh has invalid neighbourhood indices"""

    def hasInvalidPoints(self):
        """Check if the mesh has points with invalid coordinates (NaN)"""

    def hasNonManifolds(self):
        """Check if the mesh has non-manifolds"""

    def hasNonUniformOrientedFacets(self):
        """Check if the mesh has facets with inconsistent orientation"""

    def hasPointsOutOfRange(self):
        """Check if the mesh has point indices that are out of range"""

    def hasSelfIntersections(self):
        """Check if the mesh intersects itself"""

    def inner(self, arg1: Mesh.Mesh, /):
        """Get the part inside of the intersection"""

    def insertVertex(self, arg1: int, arg2: FreeCAD.Vector, /):
        """Insert a vertex into a facet"""

    def intersect(self, arg1: Mesh.Mesh, /):
        """Intersection of this and the given mesh object."""

    def isSolid(self):
        """Check if the mesh is a solid"""

    def mergeFacets(self):
        """Merge facets to optimize topology"""

    def meshFromSegment(self, arg1: object, /):
        """Create a mesh from segment"""

    @typing.overload
    def nearestFacetOnRay(self, tuple: object, tuple2: object, /): ...

    @typing.overload
    def nearestFacetOnRay(self, tuple: float, tuple2: int = None, /):
        """
        nearestFacetOnRay(tuple, tuple) -> dict
        Get the index and intersection point of the nearest facet to a ray.
        The first parameter is a tuple of three floats the base point of the ray,
        the second parameter is ut uple of three floats for the direction.
        The result is a dictionary with an index and the intersection point or
        an empty dictionary if there is no intersection.
        """

    def offset(self, arg1: float, /):
        """Move the point along their normals"""

    def offsetSpecial(self, arg1: float, arg2: float, arg3: float, /):
        """Move the point along their normals"""

    def optimizeEdges(self):
        """Optimize the edges to get nicer facets"""

    def optimizeTopology(self, arg1: float = None, /):
        """Optimize the edges to get nicer facets"""

    def outer(self, arg1: Mesh.Mesh, /):
        """Get the part outside the intersection"""

    def printInfo(self):
        """Get detailed information about the mesh"""

    @typing.overload
    def read(self, Filename: str): ...

    @typing.overload
    def read(self, Stream: object, Format: str):
        """
        Read in a mesh object from file.
        mesh.read(Filename='mymesh.stl')
        mesh.read(Stream=file,Format='STL')
        """

    def rebuildNeighbourHood(self):
        """Repairs the neighbourhood which might be broken"""

    def refine(self):
        """Refine the mesh"""

    def removeComponents(self, arg1: int, /):
        """Remove components with less or equal to number of given facets"""

    def removeDuplicatedFacets(self):
        """Remove duplicated facets"""

    def removeDuplicatedPoints(self):
        """Remove duplicated points"""

    def removeFacets(self, arg1: object, /):
        """Remove a list of facet indices from the mesh"""

    def removeFoldsOnSurface(self):
        """Remove folds on surfaces"""

    def removeFullBoundaryFacets(self):
        """Remove facets whose all three points are on the boundary"""

    def removeInvalidPoints(self):
        """Remove points with invalid coordinates (NaN)"""

    def removeNeedles(self, arg1: float, /):
        """Remove all edges that are smaller than a given length"""

    def removeNonManifoldPoints(self):
        """Remove non-manifold points"""

    def removeNonManifolds(self):
        """Remove non-manifolds"""

    def rotate(self, arg1: float, arg2: float, arg3: float, /):
        """Apply a rotation to the mesh"""

    def section(self, Mesh: Mesh.Mesh, ConnectLines: bool = True, MinDist: float = 0.0001):
        """
        Get the section curves of this and the given mesh object.
        lines = mesh.section(mesh2, [ConnectLines=True, MinDist=0.0001])
        """

    def setPoint(self, int: int, Vector: FreeCAD.Vector, /):
        """
        setPoint(int, Vector)
        					Sets the point at index.
        """

    def smooth(self, Method: str = None, Iteration: int = None, Lambda: float = None, Micro: float = None):
        """
        Smooth the mesh
        smooth([iteration=1,maxError=FLT_MAX])
        """

    def snapVertex(self, arg1: int, arg2: FreeCAD.Vector, /):
        """Insert a new facet at the border"""

    def splitEdge(self, arg1: int, arg2: int, arg3: FreeCAD.Vector, /):
        """Split edge"""

    def splitEdges(self):
        """Split all edges"""

    def splitFacet(self, arg1: int, arg2: FreeCAD.Vector, arg3: FreeCAD.Vector, /):
        """Split facet"""

    def swapEdge(self, arg1: int, arg2: int, /):
        """Swap the common edge with the neighbour"""

    def transform(self, arg1: FreeCAD.Matrix, /):
        """Apply a transformation to the mesh"""

    def transformToEigen(self):
        """Transform the mesh to its eigenbase"""

    def translate(self, arg1: float, arg2: float, arg3: float, /):
        """Apply a translation to the mesh"""

    def trim(self, list: object, int: int, /):
        """
        Trims the mesh with a given closed polygon
        trim(list, int) -> None
        The argument list is an array of points, a polygon
        The argument int is the mode: 0=inner, 1=outer
        """

    def unite(self, arg1: Mesh.Mesh, /):
        """Union of this and the given mesh object."""

    @typing.overload
    def write(self, Filename: str, Format: str = 'STL', Name: str = 'Object name', Material: object = None): ...

    @typing.overload
    def write(self, Stream: object, Format: str, Name: str = 'Object name', Material: object = None):
        """
        Write the mesh object into file.
        mesh.write(Filename='mymesh.stl',[Format='STL',Name='Object name',Material=colors])
        mesh.write(Stream=file,Format='STL',[Name='Object name',Material=colors])
        """

    def writeInventor(self, arg1: float = None, /):
        """Write the mesh in OpenInventor format to a string."""


# AppMeshPy.cpp
def read(arg1: str, /):
    """Read a mesh from a file and returns a Mesh object."""


def open(string: str, /):
    """
    open(string)
    Create a new document and a Mesh feature to load the file into
    the document.
    """


def insert(string_mesh: str, string: str = None, /):
    """
    insert(string|mesh,[string])
    Load or insert a mesh into the given or active document.
    """


def show(shape: Mesh.Mesh, string: str = None, /):
    """show(shape,[string]) -- Add the mesh to the active document or create one if no document exists."""


def createBox(arg1: float = None, arg2: float = None, arg3: float = None, arg4: float = None, /):
    """Create a solid mesh box"""


def createPlane(arg1: float = None, arg2: float = None, arg3: float = None, /):
    """Create a mesh XY plane normal +Z"""


def createSphere(arg1: float = None, arg2: int = None, /):
    """Create a tessellated sphere"""


def createEllipsoid(arg1: float = None, arg2: float = None, arg3: int = None, /):
    """Create a tessellated ellipsoid"""


def createCylinder(arg1: float = None, arg2: float = None, arg3: int = None, arg4: float = None, arg5: int = None, /):
    """Create a tessellated cylinder"""


def createCone(arg1: float = None, arg2: float = None, arg3: float = None, arg4: int = None, arg5: float = None, arg6: int = None, /):
    """Create a tessellated cone"""


def createTorus(arg1: float = None, arg2: float = None, arg3: int = None, /):
    """Create a tessellated torus"""


def calculateEigenTransform(seq_Base_Vector_: object, /):
    """
    calculateEigenTransform(seq(Base.Vector))
    Calculates the eigen Transformation from a list of points.
    calculate the point's local coordinate system with the center
    of gravity as origin. The local coordinate system is computed
    this way that u has minimum and w has maximum expansion.
    The local coordinate system is right-handed.
    """


def polynomialFit(seq_Base_Vector_: object, /):
    """polynomialFit(seq(Base.Vector)) -- Calculates a polynomial fit."""


def minimumVolumeOrientedBox(seq_Base_Vector_: object, /):
    """
    minimumVolumeOrientedBox(seq(Base.Vector)) -- Calculates the minimum
    volume oriented box containing all points. The return value is a
    tuple of seven items:
        center, u, v, w directions and the lengths of the three vectors.
    """


def export(objectList: object, filename: str, tolerance: float = 0.1, exportAmfCompressed: bool = True):
    """
    export(objects, filename, [tolerance=0.1, exportAmfCompressed=True])
    Export a list of objects into a single file identified by filename.
    tolerance is in mm and specifies the maximum acceptable deviation
    between the specified objects and the exported mesh.
    exportAmfCompressed specifies whether exported AMF files should be
    compressed.
    """
