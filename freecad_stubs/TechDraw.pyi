import typing

import FreeCAD
import TechDraw


# DrawGeomHatchPy.xml
class DrawGeomHatch(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing GeomHatch areas"""


# DrawLeaderLinePy.xml
class DrawLeaderLine(TechDraw.DrawView):
    """Feature for adding leaders to Technical Drawings"""


# DrawViewAnnotationPy.xml
class DrawViewAnnotation(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing Annotation Views"""


# DrawViewClipPy.xml
class DrawViewClip(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing Clip Views"""

    def addView(self, DrawView: FreeCAD.DocumentObject, /):
        """addView(DrawView) - Add a View to this ClipView"""

    def getChildViewNames(self):
        """getChildViewNames() - get a list of the DrawViews in this ClipView"""

    def removeView(self, DrawView: FreeCAD.DocumentObject, /):
        """removeView(DrawView) - Remove specified View to this ClipView"""


# DrawViewSymbolPy.xml
class DrawViewSymbol(TechDraw.DrawView):
    """Feature for creating and manipulating Drawing SVG Symbol Views"""

    def dumpSymbol(self, fileSpec: str, /):
        """dumpSymbol(fileSpec) - dump the contents of Symbol to a file"""


# DrawViewCollectionPy.xml
class DrawViewCollection(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing View Collections"""

    def addView(self, DrawView_object: FreeCAD.DocumentObject, /):
        """addView(DrawView object) - Add a new View to this Group. Returns count of views."""

    def removeView(self, DrawView_object: FreeCAD.DocumentObject, /):
        """removeView(DrawView object) - Remove specified Viewfrom this Group. Returns count of views in Group."""


# CosmeticExtensionPy.xml
class CosmeticExtension(FreeCAD.DocumentObjectExtension):
    """This object represents cosmetic features for a DrawViewPart."""


# DrawViewDimExtentPy.xml
class DrawViewDimExtent(TechDraw.DrawViewDimension):
    """Feature for creating and manipulating Technical Drawing DimExtents"""

    def tbd(self):
        """tbd() - returns tbd."""


# DrawRichAnnoPy.xml
class DrawRichAnno(TechDraw.DrawView):
    """Feature for adding rich annotation blocks to Technical Drawings"""


# DrawTilePy.xml
class DrawTile(FreeCAD.DocumentObject):
    """Feature for adding tiles to leader lines"""


# DrawViewDimensionPy.xml
class DrawViewDimension(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing Dimensions"""

    def getAnglePoints(self):
        """getAnglePoints() - returns list of points for angle Dimension"""

    def getArcPoints(self):
        """getArcPoints() - returns list of points for circle/arc Dimension"""

    def getArrowPositions(self):
        """getArrowPositions() - returns list of locations or Dimension Arrowheads. Locations are in unscaled coordinates of parent View """

    def getLinearPoints(self):
        """getLinearPoints() - returns list of points for linear Dimension"""

    def getRawValue(self):
        """getRawValue() - returns Dimension value in mm."""

    def getText(self):
        """getText() - returns Dimension text."""


# CosmeticVertexPy.xml
class CosmeticVertex(FreeCAD.PyObjectBase):
    """CosmeticVertex specifies an extra (cosmetic) vertex in Views"""

    @property
    def Color(self) -> object:
        """set/return the vertex's colour using a tuple (rgba)."""

    @Color.setter
    def Color(self, value: object): ...

    @property
    def Point(self) -> object:
        """Gives the position of this CosmeticVertex as vector."""

    @property
    def Show(self) -> bool:
        """Show/hide the vertex."""

    @property
    def Size(self) -> object:
        """set/return the vertex's radius in mm."""

    @Size.setter
    def Size(self, value: object): ...

    @property
    def Style(self) -> object:
        """set/return the vertex's style as integer."""

    @Style.setter
    def Style(self, value: object): ...

    @property
    def Tag(self) -> str:
        """Gives the tag of the CosmeticVertex as string."""

    def clone(self):
        """Create a clone of this CosmeticVertex"""

    def copy(self):
        """Create a copy of this CosmeticVertex"""


# DrawViewPy.xml
class DrawView(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Views"""


# DrawSVGTemplatePy.xml
class DrawSVGTemplate(TechDraw.DrawTemplate):
    """Feature for creating and manipulating Technical Drawing SVG Templates"""

    def getEditFieldContent(self, EditFieldName: str, /):
        """getEditFieldContent(EditFieldName) - returns the content of a specific Editable Text Field"""

    def setEditFieldContent(self, EditFieldName: str, NewContent: str, /):
        """setEditFieldContent(EditFieldName, NewContent) - sets a specific Editable Text Field to a new value"""


# DrawWeldSymbolPy.xml
class DrawWeldSymbol(TechDraw.DrawView):
    """Feature for adding welding tiles to leader lines"""


# DrawProjGroupPy.xml
class DrawProjGroup(TechDraw.DrawViewCollection):
    """Feature for creating and manipulating Technical Drawing Projection Groups"""

    def addProjection(self, string_projectionType: str, /):
        """addProjection(string projectionType) - Add a new Projection Item to this Group. Returns DocObj."""

    def getItemByLabel(self, string_projectionType: str, /):
        """getItemByLabel(string projectionType) - return specified Projection Item"""

    def getXYPosition(self, string_projectionType: str, /):
        """getXYPosition(string projectionType) - return the AutoDistribute position for specified Projection Item"""

    def purgeProjections(self):
        """purgeProjections() - Remove all Projection Items from this Group. Returns int number of views in Group (0)."""

    def removeProjection(self, string_projectionType: str, /):
        """removeProjection(string projectionType) - Remove specified Projection Item from this Group. Returns int number of views in Group."""


# DrawParametricTemplatePy.xml
class DrawParametricTemplate(TechDraw.DrawTemplate):
    """Feature for creating and manipulating Technical Drawing Templates"""

    @property
    def GeometryCount(self) -> int:
        """Number of geometry in template"""

    def drawLine(self, arg1: float, arg2: float, arg3: float, arg4: float, /):
        """Draw a line"""


# DrawViewPartPy.xml
class DrawViewPart(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing Part Views"""

    def clearCenterLines(self):
        """clearCenterLines() - remove all CenterLines from the View. Returns None."""

    def clearCosmeticEdges(self):
        """clearCosmeticEdges() - remove all CosmeticLines from the View. Returns None."""

    def clearCosmeticVertices(self):
        """clearCosmeticVertices() - remove all CosmeticVertices from the View. Returns None."""

    def clearGeomFormats(self):
        """clearGeomFormats() - remove all GeomFormats from the View. Returns None."""

    def formatGeometricEdge(self, index: int, style: int, weight: float, color: object, visible: int, /):
        """formatGeometricEdge(index, style, weight, color, visible). Returns None."""

    def getCenterLine(self, id: str, /):
        """cl = getCenterLine(id) - returns CenterLine with unique id."""

    def getCenterLineBySelection(self, name: str, /):
        """cl = getCenterLineBySelection(name) - returns CenterLine by name (Edge25).  Used in selections"""

    def getCosmeticEdge(self, id: str, /):
        """ce = getCosmeticEdge(id) - returns CosmeticEdge with unique id."""

    def getCosmeticEdgeBySelection(self, name: str, /):
        """ce = getCosmeticEdgeBySelection(name) - returns CosmeticEdge by name (Edge25).  Used in selections"""

    def getCosmeticVertex(self, id: str, /):
        """cv = getCosmeticVertex(id) - returns CosmeticVertex with unique id."""

    def getCosmeticVertexBySelection(self, name: str, /):
        """cv = getCosmeticVertexBySelection(name) - returns CosmeticVertex with name (Vertex6).  Used in selections."""

    def getEdgeByIndex(self, edgeIndex: int, /):
        """getEdgeByIndex(edgeIndex). Returns Part.TopoShape."""

    def getEdgeBySelection(self, edgeName: str, /):
        """getEdgeBySelection(edgeName). Returns Part.TopoShape."""

    def getHiddenEdges(self):
        """getHiddenEdges() - get the hidden edges in the View as Part::TopoShapeEdges"""

    def getVertexByIndex(self, vertexIndex: int, /):
        """getVertexByIndex(vertexIndex). Returns Part.TopoShape."""

    def getVertexBySelection(self, vertexName: str, /):
        """getVertexBySelection(vertexName). Returns Part.TopoShape."""

    def getVisibleEdges(self):
        """getVisibleEdges() - get the visible edges in the View as Part::TopoShapeEdges"""

    def makeCenterLine(self, subNames: object, mode: int, /):
        """makeCenterLine(subNames, mode) - draw a center line on this viewPart. SubNames is a list of n Faces, 2 Edges or 2 Vertices (ex [Face1,Face2,Face3]. Returns unique tag of added CenterLine."""

    def makeCosmeticCircle(self, arg1: FreeCAD.Vector, arg2: float, arg3: int = None, arg4: float = None, arg5: object = None, /):
        """tag = makeCosmeticCircle(center, radius) - add a CosmeticEdge at center with radius radius(View coordinates). Returns tag of new CosmeticEdge."""

    def makeCosmeticCircleArc(self, arg1: FreeCAD.Vector, arg2: float, arg3: float, arg4: float, arg5: int = None, arg6: float = None, arg7: object = None, /):
        """tag = makeCosmeticCircleArc(center, radius, start, end) - add a CosmeticEdge at center with radius radius(View coordinates) from start angle to end angle. Returns tag of new CosmeticEdge."""

    def makeCosmeticLine(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, arg3: int = None, arg4: float = None, arg5: object = None, /):
        """tag = makeCosmeticLine(p1, p2) - add a CosmeticEdge from p1 to p2(View coordinates). Returns tag of new CosmeticEdge."""

    def makeCosmeticLine3D(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, arg3: int = None, arg4: float = None, arg5: object = None, /):
        """tag = makeCosmeticLine3D(p1, p2) - add a CosmeticEdge from p1 to p2(3D coordinates). Returns tag of new CosmeticEdge."""

    def makeCosmeticVertex(self, p1: FreeCAD.Vector, /):
        """id = makeCosmeticVertex(p1) - add a CosmeticVertex at p1 (View coordinates). Returns unique id vertex."""

    def makeCosmeticVertex3d(self, p1: FreeCAD.Vector, /):
        """id = makeCosmeticVertex3d(p1) - add a CosmeticVertex at p1 (3d model coordinates). Returns unique id vertex."""

    def removeCenterLine(self, cl: str, /):
        """removeCenterLine(cl) - remove CenterLine cl from View. Returns None."""

    def removeCosmeticEdge(self, ce: str, /):
        """removeCosmeticEdge(ce) - remove CosmeticEdge ce from View. Returns None."""

    @typing.overload
    def removeCosmeticVertex(self, cv: str, /): ...

    @typing.overload
    def removeCosmeticVertex(self, cv: TechDraw.CosmeticVertex, /): ...

    @typing.overload
    def removeCosmeticVertex(self, cv: object, /):
        """removeCosmeticVertex(cv) - remove CosmeticVertex from View. Returns None."""

    def replaceCenterLine(self, cl):
        """replaceCenterLine(cl) - replacls CenterLine cl in View. Returns True/False."""

    def replaceCosmeticEdge(self, ce):
        """replaceCosmeticEdge(ce) - replaces CosmeticEdge ce in View. Returns True/False."""

    def replaceCosmeticVertex(self, cv):
        """rc = replaceCosmeticVertex(cv) - replaces CosmeticVertex in View. Returns True/False."""

    def requestPaint(self):
        """requestPaint(). Redraw the graphic for this View."""


# DrawTemplatePy.xml
class DrawTemplate(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Templates"""


# CenterLinePy.xml
class CenterLine(FreeCAD.PyObjectBase):
    """CenterLine specifies additional mark up edges in a View"""

    @property
    def Edges(self) -> object:
        """The names of source edges for this CenterLine."""

    @property
    def Extension(self) -> float:
        """The additional length to be added to this CenterLine."""

    @property
    def Faces(self) -> object:
        """The names of source Faces for this CenterLine."""

    @property
    def Flip(self) -> bool:
        """Reverse the order of points for 2 point CenterLine."""

    @property
    def Format(self) -> object:
        """The appearance attributes (style, color, weight, visible) for this CenterLine."""

    @property
    def HorizShift(self) -> float:
        """The left/right offset for this CenterLine."""

    @property
    def Mode(self) -> int:
        """0 - vert/ 1 - horiz/ 2 - aligned."""

    @property
    def Points(self) -> object:
        """The names of source Points for this CenterLine."""

    @property
    def Rotation(self) -> FreeCAD.Rotation:
        """The rotation of the Centerline in degrees."""

    @property
    def Tag(self) -> str:
        """Gives the tag of the CenterLine as string."""

    @property
    def Type(self) -> int:
        """0 - face, 1 - 2 line, 2 - 2 point."""

    @property
    def VertShift(self) -> float:
        """The up/down offset for this CenterLine."""

    def clone(self):
        """Create a clone of this centerline"""

    def copy(self):
        """Create a copy of this centerline"""


# DrawTileWeldPy.xml
class DrawTileWeld(TechDraw.DrawTile):
    """Feature for adding welding tiles to leader lines"""


# DrawPagePy.xml
class DrawPage(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Pages"""

    def addView(self, DrawView: FreeCAD.DocumentObject, /):
        """addView(DrawView) - Add a View to this Page"""

    def getAllViews(self):
        """getAllViews() - returns a list of all the views on page including Views inside Collections"""

    def removeView(self, DrawView: FreeCAD.DocumentObject, /):
        """removeView(DrawView) - Remove a View to this Page"""


# DrawHatchPy.xml
class DrawHatch(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Hatch areas"""


# DrawProjGroupItemPy.xml
class DrawProjGroupItem(TechDraw.DrawViewPart):
    """Feature for creating and manipulating component Views Technical Drawing Projection Groups"""

    def autoPosition(self):
        """autoPosition() - Move to AutoDistribute/Unlocked position on Page. Returns none."""


# CosmeticEdgePy.xml
class CosmeticEdge(FreeCAD.PyObjectBase):
    """CosmeticEdge specifies an extra (cosmetic) edge in Views"""

    @property
    def Center(self) -> object:
        """Gives the position of center point of this CosmeticEdge as vector."""

    @property
    def End(self) -> object:
        """Gives the position of one end of this CosmeticEdge as vector."""

    @property
    def Format(self) -> object:
        """The appearance attributes (style, weight, color, visible) for this CosmeticEdge."""

    @property
    def Radius(self) -> object:
        """Gives the radius of CosmeticEdge in mm."""

    @property
    def Start(self) -> object:
        """Gives the position of one end of this CosmeticEdge as vector."""

    @property
    def Tag(self) -> str:
        """Gives the tag of the CosmeticEdge as string."""

    def clone(self):
        """Create a clone of this CosmeticEdge"""

    def copy(self):
        """Create a copy of this CosmeticEdge"""


# GeomFormatPy.xml
class GeomFormat(FreeCAD.PyObjectBase):
    """GeomFormat specifies appearance parameters for TechDraw Geometry objects"""

    @property
    def Tag(self) -> str:
        """Gives the tag of the GeomFormat as string."""

    def clone(self):
        """Create a clone of this geomformat"""

    def copy(self):
        """Create a copy of this geomformat"""


# AppTechDrawPy.cpp
def edgeWalker(edgePile: list, inclBiggest: object = None, /):
    """[wires] = edgeWalker(edgePile,inclBiggest) -- Planar graph traversal finds wires in edge pile."""


def findOuterWire(edgeList: list, /):
    """wire = findOuterWire(edgeList) -- Planar graph traversal finds OuterWire in edge pile."""


def findShapeOutline(shape: object, scale: float, direction: object, /):
    """wire = findShapeOutline(shape,scale,direction) -- Project shape in direction and find outer wire of result."""


def viewPartAsDxf(DrawViewPart: object, /):
    """string = viewPartAsDxf(DrawViewPart) -- Return the edges of a DrawViewPart in Dxf format."""


def viewPartAsSvg(DrawViewPart: object, /):
    """string = viewPartAsSvg(DrawViewPart) -- Return the edges of a DrawViewPart in Svg format."""


def writeDXFView(arg1: object, arg2: str, arg3: object = None, /):
    """writeDXFView(view,filename): Exports a DrawViewPart to a DXF file."""


def writeDXFPage(page: object, filename: str, /):
    """writeDXFPage(page,filename): Exports a DrawPage to a DXF file."""


def findCentroid(shape: object, direction: object, /):
    """vector = findCentroid(shape,direction): finds geometric centroid of shape looking in direction."""


def makeExtentDim(DrawViewPart: object, edges: list, direction: int, /):
    """makeExtentDim(DrawViewPart, [edges], direction) -- draw horizontal or vertical extent dimension for edges (or all of DrawViewPart if edge list is empty. direction:  0 - Horizontal, 1 - Vertical."""


def makeDistanceDim(DrawViewPart: object, dimType: object, fromPoint: object, toPoint: object, /):
    """makeDistanceDim(DrawViewPart, dimType, fromPoint, toPoint) -- draw a Length dimension between fromPoint to toPoint.  FromPoint and toPoint are unscaled 2d View points. dimType is one of ['Distance', 'DistanceX', 'DistanceY'."""


def makeDistanceDim3d(arg1: object, arg2: object, arg3: object, arg4: object, /):
    """makeDistanceDim(DrawViewPart, dimType, 3dFromPoint, 3dToPoint) -- draw a Length dimension between fromPoint to toPoint.  FromPoint and toPoint are unscaled 3d model points. dimType is one of ['Distance', 'DistanceX', 'DistanceY'."""


def makeGeomHatch(face: object, patScale: float = None, patName: str = None, patFile: str = None, /):
    """makeGeomHatch(face, [patScale], [patName], [patFile]) -- draw a geom hatch on a given face, using optionally the given scale (default 1) and a given pattern name (ex. Diamond) and .pat file (the default pattern name and/or .pat files set in preferences are used if none are given). Returns a Part compound shape."""


# MDIViewPagePy.xml
class MDIViewPage(FreeCAD.PyObjectBase):
    """MDIViewPage object"""

    def getPage(self):
        """returns the page being displayed"""
