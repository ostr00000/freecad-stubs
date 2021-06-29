import FreeCAD
import TechDraw


# DrawGeomHatchPy.xml
class DrawGeomHatch(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing GeomHatch areas"""


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


# DrawViewDimensionPy.xml
class DrawViewDimension(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing Dimensions"""


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


# DrawTemplatePy.xml
class DrawTemplate(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Templates"""


# DrawPagePy.xml
class DrawPage(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Pages"""

    def addView(self, DrawView: FreeCAD.DocumentObject, /):
        """addView(DrawView) - Add a View to this Page"""

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
