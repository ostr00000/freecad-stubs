import io
import typing

import FreeCAD
import Part as PartModule
import TechDraw

DocAndStr_t: typing.TypeAlias = tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]
LinkSub_t: typing.TypeAlias = FreeCAD.DocumentObject | None | tuple[()] | DocAndStr_t
_T = typing.TypeVar("_T")
Quadruple_t: typing.TypeAlias = tuple[_T, _T, _T, _T]
LinkList_t: typing.TypeAlias = None | FreeCAD.DocumentObject
SequenceDoc_t: typing.TypeAlias = tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]
LinkSubList_t: typing.TypeAlias = typing.Sequence[SequenceDoc_t | FreeCAD.DocumentObject]
StrIO_t: typing.TypeAlias = str | bytes | io.IOBase
Triple_t: typing.TypeAlias = tuple[_T, _T, _T]


# DrawGeomHatchPy.xml
class DrawGeomHatch(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing GeomHatch areas"""

    @property
    def FilePattern(self) -> str:
        """
        Property group: GeomHatch.
        Property TypeId: App::PropertyFile.
        The crosshatch pattern file for this area.
        """

    @FilePattern.setter
    def FilePattern(self, value: str): ...

    @property
    def NamePattern(self) -> str:
        """
        Property group: GeomHatch.
        Property TypeId: App::PropertyString.
        The name of the pattern.
        """

    @NamePattern.setter
    def NamePattern(self, value: str): ...

    @property
    def ScalePattern(self) -> float:
        """
        Property group: GeomHatch.
        Property TypeId: App::PropertyFloatConstraint.
        GeomHatch pattern size adjustment.
        """

    @ScalePattern.setter
    def ScalePattern(self, value: float | Quadruple_t[float]): ...

    @property
    def Source(self) -> tuple[FreeCAD.DocumentObject, list[str]] | None:
        """
        Property group: GeomHatch.
        Property TypeId: App::PropertyLinkSub.
        The View + Face to be crosshatched.
        """

    @Source.setter
    def Source(self, value: LinkSub_t): ...


# DrawViewClipPy.xml
class DrawViewClip(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing Clip Views"""

    @property
    def Height(self) -> FreeCAD.Quantity:
        """
        Property group: Clip Group.
        Property TypeId: App::PropertyLength.
        The height of the view area of this clip.
        """

    @Height.setter
    def Height(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def ShowFrame(self) -> bool:
        """
        Property group: Clip Group.
        Property TypeId: App::PropertyBool.
        Specifies if the clip frame appears on the page or not.
        """

    @ShowFrame.setter
    def ShowFrame(self, value: int | bool): ...

    @property
    def ShowLabels(self) -> bool:
        """
        Property group: Clip Group.
        Property TypeId: App::PropertyBool.
        Specifies if View labels appear within the clip area.
        """

    @ShowLabels.setter
    def ShowLabels(self, value: int | bool): ...

    @property
    def Views(self) -> list[FreeCAD.DocumentObject | None]:
        """
        Property group: Clip Group.
        Property TypeId: App::PropertyLinkList.
        The Views in this Clip group.
        """

    @Views.setter
    def Views(self, value: LinkList_t): ...

    @property
    def Width(self) -> FreeCAD.Quantity:
        """
        Property group: Clip Group.
        Property TypeId: App::PropertyLength.
        The width of the view area of this clip.
        """

    @Width.setter
    def Width(self, value: str | float | FreeCAD.Quantity): ...

    def addView(self, DrawView: FreeCAD.DocumentObject, /):
        """addView(DrawView) - Add a View to this ClipView"""

    def getChildViewNames(self) -> list:
        """getChildViewNames() - get a list of the DrawViews in this ClipView"""

    def removeView(self, DrawView: FreeCAD.DocumentObject, /):
        """removeView(DrawView) - Remove specified View to this ClipView"""


# DrawViewSymbolPy.xml
class DrawViewSymbol(TechDraw.DrawView):
    """Feature for creating and manipulating Drawing SVG Symbol Views"""

    @property
    def EditableTexts(self) -> list[str]:
        """
        Property group: Drawing view.
        Property TypeId: App::PropertyStringList.
        Substitution values for the editable strings in this symbol.
        """

    @EditableTexts.setter
    def EditableTexts(self, value: typing.Iterable[str] | dict[int, str]): ...

    @property
    def Symbol(self) -> str:
        """
        [Prop_Hidden] Property won't appear in the editor.
        Property group: Drawing view.
        Property TypeId: App::PropertyString.
        The SVG code defining this symbol.
        """

    @Symbol.setter
    def Symbol(self, value: str): ...

    def dumpSymbol(self, fileSpec: str, /):
        """
        dumpSymbol(fileSpec) - dump the contents of Symbol to a file
        Possible exceptions: (TypeError, Exception).
        """


# DrawViewCollectionPy.xml
class DrawViewCollection(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing View Collections"""

    @property
    def Views(self) -> list[FreeCAD.DocumentObject | None]:
        """
        Property group: Drawing view.
        Property TypeId: App::PropertyLinkList.
        Attached Views.
        """

    @Views.setter
    def Views(self, value: LinkList_t): ...

    def addView(self, DrawView_object: FreeCAD.DocumentObject, /) -> int:
        """
        addView(DrawView object) - Add a new View to this Group. Returns count of views.
        Possible exceptions: (TypeError).
        """

    def removeView(self, DrawView_object: FreeCAD.DocumentObject, /) -> int:
        """
        removeView(DrawView object) - Remove specified Viewfrom this Group. Returns count of views in Group.
        Possible exceptions: (TypeError).
        """


# DrawViewDimensionPy.xml
class DrawViewDimension(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing Dimensions"""

    @property
    def FormatSpec(self) -> str:
        """
        Property group: Format.
        Property TypeId: App::PropertyString.
        Dimension Format.
        """

    @FormatSpec.setter
    def FormatSpec(self, value: str): ...

    @property
    def MeasureType(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @MeasureType.setter
    def MeasureType(self, value: typing.Literal['True', 'Projected']): ...

    @property
    def References2D(self) -> list[tuple[FreeCAD.DocumentObject, list[str]]]:
        """
        Property TypeId: App::PropertyLinkSubList.
        Projected Geometry References.
        """

    @References2D.setter
    def References2D(self, value: LinkSub_t | LinkList_t | LinkSubList_t): ...

    @property
    def References3D(self) -> list[tuple[FreeCAD.DocumentObject, list[str]]]:
        """
        Property TypeId: App::PropertyLinkSubList.
        3D Geometry References.
        """

    @References3D.setter
    def References3D(self, value: LinkSub_t | LinkList_t | LinkSubList_t): ...

    @property
    def Type(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @Type.setter
    def Type(self, value: typing.Literal['Distance', 'DistanceX', 'DistanceY', 'DistanceZ', 'Radius', 'Diameter', 'Angle']): ...


# DrawViewPy.xml
class DrawView(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Views"""

    @property
    def Caption(self) -> str:
        """
        Property group: Base.
        Property TypeId: App::PropertyString.
        Short text about the view.
        """

    @Caption.setter
    def Caption(self, value: str): ...

    @property
    def LockPosition(self) -> bool:
        """
        Property group: Base.
        Property TypeId: App::PropertyBool.
        Prevent View from moving in Gui.
        """

    @LockPosition.setter
    def LockPosition(self, value: int | bool): ...

    @property
    def Rotation(self) -> float:
        """
        Property group: Base.
        Property TypeId: App::PropertyFloat.
        Rotation of the view on the page in degrees counterclockwise.
        """

    @Rotation.setter
    def Rotation(self, value: float): ...

    @property
    def Scale(self) -> float:
        """
        Property group: Base.
        Property TypeId: App::PropertyFloatConstraint.
        Scale factor of the view.
        """

    @Scale.setter
    def Scale(self, value: float | Quadruple_t[float]): ...

    @property
    def ScaleType(self) -> int:
        """
        Property group: Base.
        Property TypeId: App::PropertyEnumeration.
        Scale Type.
        """

    @ScaleType.setter
    def ScaleType(self, value: typing.Literal['Page', 'Automatic', 'Custom']): ...

    @property
    def X(self) -> float:
        """
        Property group: Base.
        Property TypeId: App::PropertyFloat.
        X position of the view on the page in modelling units (mm).
        """

    @X.setter
    def X(self, value: float): ...

    @property
    def Y(self) -> float:
        """
        Property group: Base.
        Property TypeId: App::PropertyFloat.
        Y position of the view on the page in modelling units (mm).
        """

    @Y.setter
    def Y(self, value: float): ...


# DrawSVGTemplatePy.xml
class DrawSVGTemplate(TechDraw.DrawTemplate):
    """Feature for creating and manipulating Technical Drawing SVG Templates"""

    @property
    def PageResult(self) -> str:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Template.
        Property TypeId: App::PropertyFileIncluded.
        Current SVG code for template.
        """

    @PageResult.setter
    def PageResult(self, value: StrIO_t | tuple[StrIO_t, StrIO_t]): ...

    @property
    def Template(self) -> str:
        """
        [Prop_Transient] Property content won't be saved to file, but still saves name, type and status.
        Property group: Template.
        Property TypeId: App::PropertyFile.
        Template for the page.
        """

    @Template.setter
    def Template(self, value: str): ...

    def getEditFieldContent(self, EditFieldName: str, /) -> str:
        """getEditFieldContent(EditFieldName) - returns the content of a specific Editable Text Field"""

    def setEditFieldContent(self, EditFieldName: str, NewContent: str, /) -> bool:
        """setEditFieldContent(EditFieldName, NewContent) - sets a specific Editable Text Field to a new value"""


# DrawProjGroupPy.xml
class DrawProjGroup(TechDraw.DrawViewCollection):
    """Feature for creating and manipulating Technical Drawing Projection Groups"""

    @property
    def Anchor(self) -> FreeCAD.DocumentObject | None:
        """
        Property group: Base.
        Property TypeId: App::PropertyLink.
        The root view to align projections with.
        """

    @Anchor.setter
    def Anchor(self, value: FreeCAD.DocumentObject | None): ...

    @property
    def AutoDistribute(self) -> bool:
        """
        Property group: Distribute.
        Property TypeId: App::PropertyBool.
        Distribute Views Automatically or Manually.
        """

    @AutoDistribute.setter
    def AutoDistribute(self, value: int | bool): ...

    @property
    def CubeDirs(self) -> list[FreeCAD.Vector]:
        """
        Property group: Distribute.
        Property TypeId: App::PropertyVectorList.
        Current view directions.
        """

    @CubeDirs.setter
    def CubeDirs(self, value: typing.Iterable[FreeCAD.Vector | Triple_t[float]] | dict[int, FreeCAD.Vector | Triple_t[float]]): ...

    @property
    def CubeRotations(self) -> list[FreeCAD.Vector]:
        """
        Property group: Distribute.
        Property TypeId: App::PropertyVectorList.
        Current rotations.
        """

    @CubeRotations.setter
    def CubeRotations(self, value: typing.Iterable[FreeCAD.Vector | Triple_t[float]] | dict[int, FreeCAD.Vector | Triple_t[float]]): ...

    @property
    def ProjectionType(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @ProjectionType.setter
    def ProjectionType(self, value: typing.Literal['Default', 'First Angle', 'Third Angle']): ...

    @property
    def Source(self) -> list[FreeCAD.DocumentObject | None]:
        """
        Property group: Base.
        Property TypeId: App::PropertyLinkList.
        Shape to view.
        """

    @Source.setter
    def Source(self, value: LinkList_t): ...

    @property
    def spacingX(self) -> float:
        """
        Property group: Distribute.
        Property TypeId: App::PropertyFloat.
        Horizontal spacing between views.
        """

    @spacingX.setter
    def spacingX(self, value: float): ...

    @property
    def spacingY(self) -> float:
        """
        Property group: Distribute.
        Property TypeId: App::PropertyFloat.
        Vertical spacing between views.
        """

    @spacingY.setter
    def spacingY(self, value: float): ...

    def addProjection(self, string_projectionType: str, /) -> TechDraw.DrawProjGroupItem:
        """
        addProjection(string projectionType) - Add a new Projection Item to this Group. Returns DocObj.
        Possible exceptions: (Exception, TypeError).
        """

    def getItemByLabel(self, string_projectionType: str, /) -> TechDraw.DrawProjGroupItem:
        """
        getItemByLabel(string projectionType) - return specified Projection Item
        Possible exceptions: (Exception, TypeError).
        """

    def getXYPosition(self, string_projectionType: str, /) -> FreeCAD.Vector:
        """
        getXYPosition(string projectionType) - return the AutoDistribute position for specified Projection Item
        Possible exceptions: (Exception).
        """

    def purgeProjections(self):
        """purgeProjections() - Remove all Projection Items from this Group. Returns int number of views in Group (0)."""

    def removeProjection(self, string_projectionType: str, /) -> int:
        """
        removeProjection(string projectionType) - Remove specified Projection Item from this Group. Returns int number of views in Group.
        Possible exceptions: (Exception).
        """


# DrawParametricTemplatePy.xml
class DrawParametricTemplate(TechDraw.DrawTemplate):
    """Feature for creating and manipulating Technical Drawing Templates"""

    @property
    def GeometryCount(self) -> int:
        """Number of geometry in template"""

    @property
    def Template(self) -> str:
        """
        Property group: Page.
        Property TypeId: App::PropertyFile.
        Template script.
        """

    @Template.setter
    def Template(self, value: str): ...

    def drawLine(self, arg1: float, arg2: float, arg3: float, arg4: float, /):
        """Draw a line"""


# DrawViewPartPy.xml
class DrawViewPart(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing Part Views"""

    @property
    def CoarseView(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Coarse View on/off.
        """

    @CoarseView.setter
    def CoarseView(self, value: int | bool): ...

    @property
    def Direction(self) -> FreeCAD.Vector:
        """
        Property group: Projection.
        Property TypeId: App::PropertyVector.
        Projection direction. The direction you are looking from.
        """

    @Direction.setter
    def Direction(self, value: FreeCAD.Vector | Triple_t[float]): ...

    @property
    def Focus(self) -> FreeCAD.Quantity:
        """
        Property group: Projection.
        Property TypeId: App::PropertyDistance.
        Perspective view focus distance.
        """

    @Focus.setter
    def Focus(self, value: str | float | FreeCAD.Quantity | FreeCAD.Unit): ...

    @property
    def HardHidden(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Hidden Hard lines on/off.
        """

    @HardHidden.setter
    def HardHidden(self, value: int | bool): ...

    @property
    def IsoCount(self) -> int:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyInteger.
        Number of isoparameters.
        """

    @IsoCount.setter
    def IsoCount(self, value: int): ...

    @property
    def IsoHidden(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Hidden Iso u,v lines on/off.
        """

    @IsoHidden.setter
    def IsoHidden(self, value: int | bool): ...

    @property
    def IsoVisible(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Visible Iso u,v lines on/off.
        """

    @IsoVisible.setter
    def IsoVisible(self, value: int | bool): ...

    @property
    def Perspective(self) -> bool:
        """
        Property group: Projection.
        Property TypeId: App::PropertyBool.
        Perspective(true) or Orthographic(false) projection.
        """

    @Perspective.setter
    def Perspective(self, value: int | bool): ...

    @property
    def SeamHidden(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Hidden Seam lines on/off.
        """

    @SeamHidden.setter
    def SeamHidden(self, value: int | bool): ...

    @property
    def SeamVisible(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Visible Seam lines on/off.
        """

    @SeamVisible.setter
    def SeamVisible(self, value: int | bool): ...

    @property
    def SmoothHidden(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Hidden Smooth lines on/off.
        """

    @SmoothHidden.setter
    def SmoothHidden(self, value: int | bool): ...

    @property
    def SmoothVisible(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Visible Smooth lines on/off.
        """

    @SmoothVisible.setter
    def SmoothVisible(self, value: int | bool): ...

    @property
    def Source(self) -> list[FreeCAD.DocumentObject | None]:
        """
        Property group: Projection.
        Property TypeId: App::PropertyLinkList.
        3D Shape to view.
        """

    @Source.setter
    def Source(self, value: LinkList_t): ...


# DrawTemplatePy.xml
class DrawTemplate(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Templates"""

    @property
    def EditableTexts(self) -> dict[str, str]:
        """
        Property group: Page Properties.
        Property TypeId: App::PropertyMap.
        Editable strings in the template.
        """

    @EditableTexts.setter
    def EditableTexts(self, value: dict[str, str]): ...

    @property
    def Height(self) -> FreeCAD.Quantity:
        """
        Property group: Page Properties.
        Property TypeId: App::PropertyLength.
        Height of page.
        """

    @Height.setter
    def Height(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def Orientation(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @Orientation.setter
    def Orientation(self, value: typing.Literal['Portrait', 'Landscape']): ...

    @property
    def Width(self) -> FreeCAD.Quantity:
        """
        Property group: Page Properties.
        Property TypeId: App::PropertyLength.
        Width of page.
        """

    @Width.setter
    def Width(self, value: str | float | FreeCAD.Quantity): ...


# DrawPagePy.xml
class DrawPage(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Pages"""

    @property
    def KeepUpdated(self) -> bool:
        """
        Property group: Page.
        Property TypeId: App::PropertyBool.
        Keep page in sync with model.
        """

    @KeepUpdated.setter
    def KeepUpdated(self, value: int | bool): ...

    @property
    def ProjectionType(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @ProjectionType.setter
    def ProjectionType(self, value: typing.Literal['First Angle', 'Third Angle']): ...

    @property
    def ProjectionType(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @ProjectionType.setter
    def ProjectionType(self, value: typing.Literal['First Angle', 'Third Angle']): ...

    @property
    def Scale(self) -> float:
        """
        Property group: Page.
        Property TypeId: App::PropertyFloatConstraint.
        Scale factor for this Page.
        """

    @Scale.setter
    def Scale(self, value: float | Quadruple_t[float]): ...

    @property
    def Template(self) -> FreeCAD.DocumentObject | None:
        """
        Property group: Page.
        Property TypeId: App::PropertyLink.
        Attached Template.
        """

    @Template.setter
    def Template(self, value: FreeCAD.DocumentObject | None): ...

    @property
    def Views(self) -> list[FreeCAD.DocumentObject | None]:
        """
        Property group: Page.
        Property TypeId: App::PropertyLinkList.
        Attached Views.
        """

    @Views.setter
    def Views(self, value: LinkList_t): ...

    def addView(self, DrawView: FreeCAD.DocumentObject, /) -> int:
        """
        addView(DrawView) - Add a View to this Page
        Possible exceptions: (TypeError).
        """

    def removeView(self, DrawView: FreeCAD.DocumentObject, /) -> int:
        """
        removeView(DrawView) - Remove a View to this Page
        Possible exceptions: (TypeError).
        """


# DrawHatchPy.xml
class DrawHatch(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Hatch areas"""

    @property
    def DirProjection(self) -> FreeCAD.Vector:
        """
        Property group: Hatch.
        Property TypeId: App::PropertyVector.
        Projection direction when Hatch was defined.
        """

    @DirProjection.setter
    def DirProjection(self, value: FreeCAD.Vector | Triple_t[float]): ...

    @property
    def HatchPattern(self) -> str:
        """
        Property group: Hatch.
        Property TypeId: App::PropertyFile.
        The hatch pattern file for this area.
        """

    @HatchPattern.setter
    def HatchPattern(self, value: str): ...

    @property
    def Source(self) -> tuple[FreeCAD.DocumentObject, list[str]] | None:
        """
        Property group: Hatch.
        Property TypeId: App::PropertyLinkSub.
        The View + Face to be hatched.
        """

    @Source.setter
    def Source(self, value: LinkSub_t): ...


# DrawProjGroupItemPy.xml
class DrawProjGroupItem(TechDraw.DrawViewPart):
    """Feature for creating and manipulating component Views Technical Drawing Projection Groups"""

    @property
    def RotationVector(self) -> FreeCAD.Vector:
        """
        Property group: Base.
        Property TypeId: App::PropertyVector.
        Controls rotation of item in view. .
        """

    @RotationVector.setter
    def RotationVector(self, value: FreeCAD.Vector | Triple_t[float]): ...

    @property
    def Type(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @Type.setter
    def Type(self, value: typing.Literal['Front', 'Left', 'Right', 'Rear', 'Top', 'Bottom', 'FrontTopLeft', 'FrontTopRight', 'FrontBottomLeft', 'FrontBottomRight']): ...

    def autoPosition(self):
        """autoPosition() - Move to AutoDistribute/Unlocked position on Page. Returns none."""


# AppTechDrawPy.cpp
def edgeWalker(edgePile: list, inclBiggest=None, /) -> list | None:
    """[wires] = edgeWalker(edgePile,inclBiggest) -- Planar graph traversal finds wires in edge pile."""


def findOuterWire(edgeList: list, /) -> PartModule.Wire | None:
    """wire = findOuterWire(edgeList) -- Planar graph traversal finds OuterWire in edge pile."""


def findShapeOutline(shape, scale: float, direction, /) -> PartModule.Wire | None:
    """wire = findShapeOutline(shape,scale,direction) -- Project shape in direction and find outer wire of result."""


def viewPartAsDxf(DrawViewPart, /) -> str:
    """string = viewPartAsDxf(DrawViewPart) -- Return the edges of a DrawViewPart in Dxf format."""


def viewPartAsSvg(DrawViewPart, /) -> str:
    """string = viewPartAsSvg(DrawViewPart) -- Return the edges of a DrawViewPart in Svg format."""
