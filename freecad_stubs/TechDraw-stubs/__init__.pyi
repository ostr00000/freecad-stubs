import io
import typing

import FreeCAD
import Part as PartModule
import TechDraw

DocAndStr_t: typing.TypeAlias = tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]
LinkSub_t: typing.TypeAlias = FreeCAD.DocumentObject | None | tuple[()] | DocAndStr_t
StrIO_t: typing.TypeAlias = str | bytes | io.IOBase
_T = typing.TypeVar("_T")
Quadruple_t: typing.TypeAlias = tuple[_T, _T, _T, _T]
Triple_t: typing.TypeAlias = tuple[_T, _T, _T]
LinkList_t: typing.TypeAlias = None | FreeCAD.DocumentObject
SequenceDoc_t: typing.TypeAlias = tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]
LinkSubList_t: typing.TypeAlias = typing.Sequence[SequenceDoc_t | FreeCAD.DocumentObject]
SequenceNone_t: typing.TypeAlias = tuple[None, typing.Any]
PropX_t: typing.TypeAlias = None | FreeCAD.DocumentObject | SequenceNone_t | SequenceDoc_t

class ReturnGetFormatDict(typing.TypedDict):
    style: int
    weight: float
    color: tuple
    visible: bool



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
    def PatIncluded(self) -> str:
        """
        Property group: GeomHatch.
        Property TypeId: App::PropertyFileIncluded.
        Embedded Pat hatch file. System use only.
        """

    @PatIncluded.setter
    def PatIncluded(self, value: StrIO_t | tuple[StrIO_t, StrIO_t]): ...

    @property
    def PatternOffset(self) -> FreeCAD.Vector:
        """
        Property group: GeomHatch.
        Property TypeId: App::PropertyVector.
        Pattern offset.
        """

    @PatternOffset.setter
    def PatternOffset(self, value: FreeCAD.Vector | Triple_t[float]): ...

    @property
    def PatternRotation(self) -> float:
        """
        Property group: GeomHatch.
        Property TypeId: App::PropertyFloat.
        Pattern rotation in degrees anticlockwise.
        """

    @PatternRotation.setter
    def PatternRotation(self, value: float): ...

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


# DrawLeaderLinePy.xml
class DrawLeaderLine(TechDraw.DrawView):
    """Feature for adding leaders to Technical Drawings"""

    @property
    def AutoHorizontal(self) -> bool:
        """
        Property group: Leader.
        Property TypeId: App::PropertyBool.
        Forces last line segment to be horizontal.
        """

    @AutoHorizontal.setter
    def AutoHorizontal(self, value: int | bool): ...

    @property
    def EndSymbol(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @EndSymbol.setter
    def EndSymbol(self, value): ...

    @property
    def LeaderParent(self) -> FreeCAD.DocumentObject | None:
        """
        Property group: Leader.
        Property TypeId: App::PropertyLink.
        View to which this leader is attached.
        """

    @LeaderParent.setter
    def LeaderParent(self, value: FreeCAD.DocumentObject | None): ...

    @property
    def Scalable(self) -> bool:
        """
        Property group: Leader.
        Property TypeId: App::PropertyBool.
        Scale line with LeaderParent.
        """

    @Scalable.setter
    def Scalable(self, value: int | bool): ...

    @property
    def StartSymbol(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @StartSymbol.setter
    def StartSymbol(self, value): ...

    @property
    def WayPoints(self) -> list[FreeCAD.Vector]:
        """
        Property group: Leader.
        Property TypeId: App::PropertyVectorList.
        Intermediate points for Leader line.
        """

    @WayPoints.setter
    def WayPoints(self, value: typing.Iterable[FreeCAD.Vector | Triple_t[float]] | dict[int, FreeCAD.Vector | Triple_t[float]]): ...


# DrawViewAnnotationPy.xml
class DrawViewAnnotation(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing Annotation Views"""

    @property
    def Font(self) -> str:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyFont.
        Font name.
        """

    @Font.setter
    def Font(self, value: str): ...

    @property
    def LineSpace(self) -> int:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyPercent.
        Line spacing in %. 100 means the height of a line.
        """

    @LineSpace.setter
    def LineSpace(self, value: int): ...

    @property
    def MaxWidth(self) -> FreeCAD.Quantity:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyLength.

        Maximum width of the annotation block.
         -1 means no maximum width.
        """

    @MaxWidth.setter
    def MaxWidth(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def Text(self) -> list[str]:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyStringList.
        Annotation text.
        """

    @Text.setter
    def Text(self, value: typing.Iterable[str] | dict[int, str]): ...

    @property
    def TextColor(self) -> tuple[float, float, float, float]:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyColor.
        Text color.
        """

    @TextColor.setter
    def TextColor(self, value: Triple_t[float] | Quadruple_t[float] | int): ...

    @property
    def TextSize(self) -> FreeCAD.Quantity:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyLength.
        Text size.
        """

    @TextSize.setter
    def TextSize(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def TextStyle(self) -> int:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyEnumeration.
        Text style.
        """

    @TextStyle.setter
    def TextStyle(self, value: typing.Literal['Normal', 'Bold', 'Italic', 'Bold-Italic']): ...


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

    def addView(self, pcDocObj: TechDraw.DrawView, /):
        """addView(DrawView) - Add a View to this ClipView"""

    def getChildViewNames(self) -> list[str]:
        """getChildViewNames() - get a list of the DrawViews in this ClipView"""

    def removeView(self, pcDocObj: TechDraw.DrawView, /):
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
        Property group: Drawing view.
        Property TypeId: App::PropertyString.
        The SVG code defining this symbol.
        """

    @Symbol.setter
    def Symbol(self, value: str): ...

    def dumpSymbol(self, fileSpec: str, /):
        """
        dumpSymbol(fileSpec) - dump the contents of Symbol to a file
        Possible exceptions: (RuntimeError).
        """


# DrawViewCollectionPy.xml
class DrawViewCollection(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing View Collections"""

    @property
    def Views(self) -> list[FreeCAD.DocumentObject | None]:
        """
        Property group: Collection.
        Property TypeId: App::PropertyLinkList.
        Collection Views.
        """

    @Views.setter
    def Views(self, value: LinkList_t): ...

    def addView(self, pcDocObj: TechDraw.DrawView, /) -> int:
        """addView(DrawView object) - Add a new View to this Group. Returns count of views."""

    def removeView(self, pcDocObj: TechDraw.DrawView, /) -> int:
        """removeView(DrawView object) - Remove specified Viewfrom this Group. Returns count of views in Group."""


# CosmeticExtensionPy.xml
class CosmeticExtension(FreeCAD.DocumentObjectExtension):
    """This object represents cosmetic features for a DrawViewPart."""

    @property
    def CenterLines(self) -> list[TechDraw.CenterLine]:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Cosmetics.
        Property TypeId: TechDraw::PropertyCenterLineList.
        Geometry format Save/Restore.
        """

    @CenterLines.setter
    def CenterLines(self, value: typing.Iterable[TechDraw.CenterLine] | dict[int, TechDraw.CenterLine]): ...

    @property
    def CosmeticEdges(self) -> list[TechDraw.CosmeticEdge]:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Cosmetics.
        Property TypeId: TechDraw::PropertyCosmeticEdgeList.
        CosmeticEdge Save/Restore.
        """

    @CosmeticEdges.setter
    def CosmeticEdges(self, value: typing.Iterable[TechDraw.CosmeticEdge] | dict[int, TechDraw.CosmeticEdge]): ...

    @property
    def CosmeticVertexes(self) -> list[TechDraw.CosmeticVertex]:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Cosmetics.
        Property TypeId: TechDraw::PropertyCosmeticVertexList.
        CosmeticVertex Save/Restore.
        """

    @CosmeticVertexes.setter
    def CosmeticVertexes(self, value: typing.Iterable[TechDraw.CosmeticVertex] | dict[int, TechDraw.CosmeticVertex]): ...

    @property
    def GeomFormats(self) -> list[TechDraw.GeomFormat]:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Cosmetics.
        Property TypeId: TechDraw::PropertyGeomFormatList.
        Geometry format Save/Restore.
        """

    @GeomFormats.setter
    def GeomFormats(self, value: typing.Iterable[TechDraw.GeomFormat] | dict[int, TechDraw.GeomFormat]): ...


# DrawViewDimExtentPy.xml
class DrawViewDimExtent(TechDraw.DrawViewDimension):
    """Feature for creating and manipulating Technical Drawing DimExtents"""

    @property
    def CosmeticTags(self) -> list[str]:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyStringList.
        Id of cosmetic endpoints.
        """

    @CosmeticTags.setter
    def CosmeticTags(self, value: typing.Iterable[str] | dict[int, str]): ...

    @property
    def DirExtent(self) -> int:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyInteger.
        Horizontal / Vertical.
        """

    @DirExtent.setter
    def DirExtent(self, value: int): ...

    @property
    def Source(self) -> list[tuple[FreeCAD.DocumentObject, list[str]]]:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyLinkSubList.
        View containing the  dimension.
        """

    @Source.setter
    def Source(self, value: LinkSub_t | LinkList_t | LinkSubList_t): ...

    @property
    def Source3d(self) -> list[tuple[FreeCAD.DocumentObject, list[str]]]:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyLinkSubList.
        3d geometry to be dimensioned.
        """

    @Source3d.setter
    def Source3d(self, value: LinkSub_t | LinkList_t | LinkSubList_t): ...

    def tbd(self):
        """tbd() - returns tbd."""


# DrawRichAnnoPy.xml
class DrawRichAnno(TechDraw.DrawView):
    """Feature for adding rich annotation blocks to Technical Drawings"""

    @property
    def AnnoParent(self) -> FreeCAD.DocumentObject | None:
        """
        Property group: Text Block.
        Property TypeId: App::PropertyLink.
        Object to which this annontation is attached.
        """

    @AnnoParent.setter
    def AnnoParent(self, value: FreeCAD.DocumentObject | None): ...

    @property
    def AnnoText(self) -> str:
        """
        Property group: Text Block.
        Property TypeId: App::PropertyString.
        Annotation text.
        """

    @AnnoText.setter
    def AnnoText(self, value: str): ...

    @property
    def MaxWidth(self) -> float:
        """
        Property group: Text Block.
        Property TypeId: App::PropertyFloat.
        Width limit before auto wrap.
        """

    @MaxWidth.setter
    def MaxWidth(self, value: float): ...

    @property
    def ShowFrame(self) -> bool:
        """
        Property group: Text Block.
        Property TypeId: App::PropertyBool.
        Outline rectangle on/off.
        """

    @ShowFrame.setter
    def ShowFrame(self, value: int | bool): ...


# DrawTilePy.xml
class DrawTile(FreeCAD.DocumentObject):
    """Feature for adding tiles to leader lines"""

    @property
    def TileColumn(self) -> int:
        """
        Property group: Tile.
        Property TypeId: App::PropertyInteger.
        Column in parent object.
        """

    @TileColumn.setter
    def TileColumn(self, value: int): ...

    @property
    def TileParent(self) -> FreeCAD.DocumentObject | None:
        """
        Property group: Tile.
        Property TypeId: App::PropertyLink.
        Object to which this tile is attached.
        """

    @TileParent.setter
    def TileParent(self, value: FreeCAD.DocumentObject | None): ...

    @property
    def TileRow(self) -> int:
        """
        Property group: Tile.
        Property TypeId: App::PropertyIntegerConstraint.

        Row in parent object
         0 for arrow side, -1 for other side.
        """

    @TileRow.setter
    def TileRow(self, value: int | Quadruple_t[int]): ...


# DrawViewDimensionPy.xml
class DrawViewDimension(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing Dimensions"""

    @property
    def AngleOverride(self) -> bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Override.
        Property TypeId: App::PropertyBool.
        User specified angles.
        """

    @AngleOverride.setter
    def AngleOverride(self, value: int | bool): ...

    @property
    def Arbitrary(self) -> bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Format.
        Property TypeId: App::PropertyBool.
        Value overridden by user.
        """

    @Arbitrary.setter
    def Arbitrary(self, value: int | bool): ...

    @property
    def ArbitraryTolerances(self) -> bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Format.
        Property TypeId: App::PropertyBool.
        Tolerance values overridden by user.
        """

    @ArbitraryTolerances.setter
    def ArbitraryTolerances(self, value: int | bool): ...

    @property
    def EqualTolerance(self) -> bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyBool.
        If over- and undertolerance are equal.
        """

    @EqualTolerance.setter
    def EqualTolerance(self, value: int | bool): ...

    @property
    def ExtensionAngle(self) -> FreeCAD.Quantity:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Override.
        Property TypeId: App::PropertyAngle.
        Extension line angle.
        """

    @ExtensionAngle.setter
    def ExtensionAngle(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def FormatSpec(self) -> str:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Format.
        Property TypeId: App::PropertyString.
        Dimension format.
        """

    @FormatSpec.setter
    def FormatSpec(self, value: str): ...

    @property
    def FormatSpecOverTolerance(self) -> str:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Format.
        Property TypeId: App::PropertyString.
        Dimension overtolerance format.
        """

    @FormatSpecOverTolerance.setter
    def FormatSpecOverTolerance(self, value: str): ...

    @property
    def FormatSpecUnderTolerance(self) -> str:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Format.
        Property TypeId: App::PropertyString.
        Dimension undertolerance format.
        """

    @FormatSpecUnderTolerance.setter
    def FormatSpecUnderTolerance(self, value: str): ...

    @property
    def Inverted(self) -> bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyBool.
        The dimensional value is displayed inverted.
        """

    @Inverted.setter
    def Inverted(self, value: int | bool): ...

    @property
    def LineAngle(self) -> FreeCAD.Quantity:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Override.
        Property TypeId: App::PropertyAngle.
        Dimension line angle.
        """

    @LineAngle.setter
    def LineAngle(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def MeasureType(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @MeasureType.setter
    def MeasureType(self, value: typing.Literal['True', 'Projected']): ...

    @property
    def OverTolerance(self) -> FreeCAD.Quantity:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyQuantityConstraint.

        Overtolerance value
        If 'Equal Tolerance' is true this is also
        the negated value for 'Under Tolerance'.
        """

    @OverTolerance.setter
    def OverTolerance(self, value: str | float | FreeCAD.Quantity): ...

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
    def TheoreticalExact(self) -> bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyBool.
        If theoretical exact (basic) dimension.
        """

    @TheoreticalExact.setter
    def TheoreticalExact(self, value: int | bool): ...

    @property
    def Type(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @Type.setter
    def Type(self, value: typing.Literal['Distance', 'DistanceX', 'DistanceY', 'DistanceZ', 'Radius', 'Diameter', 'Angle', 'Angle3Pt']): ...

    @property
    def UnderTolerance(self) -> FreeCAD.Quantity:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyQuantityConstraint.

        Undertolerance value
        If 'Equal Tolerance' is true it will be replaced
        by negative value of 'Over Tolerance'.
        """

    @UnderTolerance.setter
    def UnderTolerance(self, value: str | float | FreeCAD.Quantity): ...

    def getAnglePoints(self) -> list[FreeCAD.Vector]:
        """getAnglePoints() - returns list of points for angle Dimension"""

    def getArcPoints(self) -> list[FreeCAD.Vector]:
        """getArcPoints() - returns list of points for circle/arc Dimension"""

    def getArrowPositions(self) -> list[FreeCAD.Vector]:
        """getArrowPositions() - returns list of locations or Dimension Arrowheads. Locations are in unscaled coordinates of parent View"""

    def getLinearPoints(self) -> list[FreeCAD.Vector]:
        """getLinearPoints() - returns list of points for linear Dimension"""

    def getRawValue(self) -> float:
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
    def Point(self) -> FreeCAD.Vector:
        """Gives the position of this CosmeticVertex as vector."""

    @property
    def Show(self) -> bool:
        """Show/hide the vertex."""

    @property
    def Size(self) -> float:
        """set/return the vertex's radius in mm."""

    @Size.setter
    def Size(self, value: float): ...

    @property
    def Style(self) -> int:
        """set/return the vertex's style as integer."""

    @Style.setter
    def Style(self, value: int): ...

    @property
    def Tag(self) -> str:
        """Gives the tag of the CosmeticVertex as string."""

    def clone(self):
        """
        Create a clone of this CosmeticVertex
        Possible exceptions: (TypeError).
        """

    def copy(self):
        """
        Create a copy of this CosmeticVertex
        Possible exceptions: (TypeError).
        """


# DrawViewPy.xml
class DrawView(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Views"""

    @property
    def Caption(self) -> str:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Base.
        Property TypeId: App::PropertyString.
        Short text about the view.
        """

    @Caption.setter
    def Caption(self, value: str): ...

    @property
    def LockPosition(self) -> bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Base.
        Property TypeId: App::PropertyBool.
        Lock View position to parent Page or Group.
        """

    @LockPosition.setter
    def LockPosition(self, value: int | bool): ...

    @property
    def Rotation(self) -> FreeCAD.Quantity:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Base.
        Property TypeId: App::PropertyAngle.
        Rotation in degrees counterclockwise.
        """

    @Rotation.setter
    def Rotation(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def Scale(self) -> float:
        """
        Property group: Base.
        Property TypeId: App::PropertyFloatConstraint.
        Scale factor of the view. Scale factors like 1:100 can be written as =1/100.
        """

    @Scale.setter
    def Scale(self, value: float | Quadruple_t[float]): ...

    @property
    def ScaleType(self) -> int:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Base.
        Property TypeId: App::PropertyEnumeration.
        Scale Type.
        """

    @ScaleType.setter
    def ScaleType(self, value: typing.Literal['Page', 'Automatic', 'Custom']): ...

    @property
    def X(self) -> FreeCAD.Quantity:
        """
        Property group: Base.
        Property TypeId: App::PropertyDistance.
        X position.
        """

    @X.setter
    def X(self, value: str | float | FreeCAD.Quantity | FreeCAD.Unit): ...

    @property
    def Y(self) -> FreeCAD.Quantity:
        """
        Property group: Base.
        Property TypeId: App::PropertyDistance.
        Y position.
        """

    @Y.setter
    def Y(self, value: str | float | FreeCAD.Quantity | FreeCAD.Unit): ...


# DrawSVGTemplatePy.xml
class DrawSVGTemplate(TechDraw.DrawTemplate):
    """Feature for creating and manipulating Technical Drawing SVG Templates"""

    @property
    def PageResult(self) -> str:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Template.
        Property TypeId: App::PropertyFileIncluded.
        Embedded SVG code for template. For system use.
        """

    @PageResult.setter
    def PageResult(self, value: StrIO_t | tuple[StrIO_t, StrIO_t]): ...

    @property
    def Template(self) -> str:
        """
        Property group: Template.
        Property TypeId: App::PropertyFile.
        Template file name.
        """

    @Template.setter
    def Template(self, value: str): ...

    def getEditFieldContent(self, fieldName: str, /) -> str:
        """getEditFieldContent(EditFieldName) - returns the content of a specific Editable Text Field"""

    def setEditFieldContent(self, fieldName: str, newContent: str, /):
        """setEditFieldContent(EditFieldName, NewContent) - sets a specific Editable Text Field to a new value"""


# DrawWeldSymbolPy.xml
class DrawWeldSymbol(TechDraw.DrawView):
    """Feature for adding welding tiles to leader lines"""

    @property
    def AllAround(self) -> bool:
        """
        Property group: Weld Symbol.
        Property TypeId: App::PropertyBool.
        All Around Symbol on/off.
        """

    @AllAround.setter
    def AllAround(self, value: int | bool): ...

    @property
    def AlternatingWeld(self) -> bool:
        """
        Property group: Weld Symbol.
        Property TypeId: App::PropertyBool.
        Alternating Weld true/false.
        """

    @AlternatingWeld.setter
    def AlternatingWeld(self, value: int | bool): ...

    @property
    def FieldWeld(self) -> bool:
        """
        Property group: Weld Symbol.
        Property TypeId: App::PropertyBool.
        Field Weld Symbol on/off.
        """

    @FieldWeld.setter
    def FieldWeld(self, value: int | bool): ...

    @property
    def Leader(self) -> FreeCAD.DocumentObject | None:
        """
        Property group: Weld Symbol.
        Property TypeId: App::PropertyLink.
        Parent Leader.
        """

    @Leader.setter
    def Leader(self, value: FreeCAD.DocumentObject | None): ...

    @property
    def TailText(self) -> str:
        """
        Property group: Weld Symbol.
        Property TypeId: App::PropertyString.
        Text at tail of symbol.
        """

    @TailText.setter
    def TailText(self, value: str): ...


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
        Distribute views automatically or manually.
        """

    @AutoDistribute.setter
    def AutoDistribute(self, value: int | bool): ...

    @property
    def ProjectionType(self) -> int:
        """
        Property group: Base.
        Property TypeId: App::PropertyEnumeration.
        First or Third angle projection.
        """

    @ProjectionType.setter
    def ProjectionType(self, value: typing.Literal['First Angle', 'Third Angle', 'Default']): ...

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
    def XSource(self) -> list[tuple[FreeCAD.DocumentObject, list[str]]] | list[FreeCAD.DocumentObject]:
        """
        Property group: Base.
        Property TypeId: App::PropertyXLinkList.
        External 3D Shape to view.
        """

    @XSource.setter
    def XSource(self, value: typing.Iterable[PropX_t] | dict[int, PropX_t]): ...

    @property
    def spacingX(self) -> FreeCAD.Quantity:
        """
        Property group: Distribute.
        Property TypeId: App::PropertyLength.

        If AutoDistribute is on, this is the horizontal 
        spacing between the borders of views 
        (if label width is not wider than the object).
        """

    @spacingX.setter
    def spacingX(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def spacingY(self) -> FreeCAD.Quantity:
        """
        Property group: Distribute.
        Property TypeId: App::PropertyLength.

        If AutoDistribute is on, this is the vertical 
        spacing between the borders of views.
        """

    @spacingY.setter
    def spacingY(self, value: str | float | FreeCAD.Quantity): ...

    def addProjection(self, projType: str, /) -> TechDraw.DrawProjGroupItem:
        """
        addProjection(string projectionType) - Add a new Projection Item to this Group. Returns DocObj.
        Possible exceptions: (Exception, TypeError).
        """

    def getItemByLabel(self, projType: str, /) -> TechDraw.DrawProjGroupItem:
        """
        getItemByLabel(string projectionType) - return specified Projection Item
        Possible exceptions: (Exception, TypeError).
        """

    def getXYPosition(self, projType: str, /) -> FreeCAD.Vector:
        """
        getXYPosition(string projectionType) - return the AutoDistribute position for specified Projection Item
        Possible exceptions: (Exception).
        """

    def purgeProjections(self) -> int:
        """purgeProjections() - Remove all Projection Items from this Group. Returns int number of views in Group (0)."""

    def removeProjection(self, projType: str, /) -> int:
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

    def drawLine(self, x1: float, y1: float, x2: float, y2: float, /):
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
    def Direction(self):
        """
        Property group: Projection.
        Property TypeId: TechDraw::.
        Projection Plane normal. The direction you are looking from.
        """

    @Direction.setter
    def Direction(self, value): ...

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
        Show Hidden Hard lines.
        """

    @HardHidden.setter
    def HardHidden(self, value: int | bool): ...

    @property
    def IsoCount(self) -> int:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyInteger.
        Number of iso parameters lines.
        """

    @IsoCount.setter
    def IsoCount(self, value: int): ...

    @property
    def IsoHidden(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Show Hidden Iso u, v lines.
        """

    @IsoHidden.setter
    def IsoHidden(self, value: int | bool): ...

    @property
    def IsoVisible(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Show Visible Iso u, v lines.
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
        Show Hidden Seam lines.
        """

    @SeamHidden.setter
    def SeamHidden(self, value: int | bool): ...

    @property
    def SeamVisible(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Show Visible Seam lines.
        """

    @SeamVisible.setter
    def SeamVisible(self, value: int | bool): ...

    @property
    def SmoothHidden(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Show Hidden Smooth lines.
        """

    @SmoothHidden.setter
    def SmoothHidden(self, value: int | bool): ...

    @property
    def SmoothVisible(self) -> bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Show Visible Smooth lines.
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

    @property
    def XDirection(self) -> FreeCAD.Vector:
        """
        Property group: Projection.
        Property TypeId: App::PropertyVector.
        Projection Plane X Axis in R3. Rotates/Mirrors View.
        """

    @XDirection.setter
    def XDirection(self, value: FreeCAD.Vector | Triple_t[float]): ...

    @property
    def XSource(self) -> list[tuple[FreeCAD.DocumentObject, list[str]]] | list[FreeCAD.DocumentObject]:
        """
        Property group: Projection.
        Property TypeId: App::PropertyXLinkList.
        External 3D Shape to view.
        """

    @XSource.setter
    def XSource(self, value: typing.Iterable[PropX_t] | dict[int, PropX_t]): ...

    def clearCenterLines(self):
        """clearCenterLines() - remove all CenterLines from the View. Returns None."""

    def clearCosmeticEdges(self):
        """clearCosmeticEdges() - remove all CosmeticLines from the View. Returns None."""

    def clearCosmeticVertices(self):
        """clearCosmeticVertices() - remove all CosmeticVertices from the View. Returns None."""

    def clearGeomFormats(self):
        """clearGeomFormats() - remove all GeomFormats from the View. Returns None."""

    def formatGeometricEdge(self, idx: int = -1, style: int = None, weight: float = 0.5, pColor=None, visible: int = 1, /):
        """formatGeometricEdge(index, style, weight, color, visible). Returns None."""

    def getCenterLine(self, tag: str, /) -> TechDraw.CenterLine:
        """cl = getCenterLine(id) - returns CenterLine with unique id."""

    def getCenterLineBySelection(self, tag: str, /) -> TechDraw.CenterLine:
        """cl = getCenterLineBySelection(name) - returns CenterLine by name (Edge25).  Used in selections"""

    def getCosmeticEdge(self, tag: str, /) -> TechDraw.CosmeticEdge:
        """ce = getCosmeticEdge(id) - returns CosmeticEdge with unique id."""

    def getCosmeticEdgeBySelection(self, name: str, /) -> TechDraw.CosmeticEdge:
        """ce = getCosmeticEdgeBySelection(name) - returns CosmeticEdge by name (Edge25).  Used in selections"""

    def getCosmeticVertex(self, id: str, /) -> TechDraw.CosmeticVertex:
        """cv = getCosmeticVertex(id) - returns CosmeticVertex with unique id."""

    def getCosmeticVertexBySelection(self, selName: str, /) -> TechDraw.CosmeticVertex:
        """cv = getCosmeticVertexBySelection(name) - returns CosmeticVertex with name (Vertex6).  Used in selections."""

    def getEdgeByIndex(self, edgeIndex: int = 0, /) -> PartModule.Edge:
        """
        getEdgeByIndex(edgeIndex). Returns Part.TopoShape.
        Possible exceptions: (ValueError).
        """

    def getEdgeBySelection(self, selName: str, /) -> PartModule.Edge:
        """
        getEdgeBySelection(edgeName). Returns Part.TopoShape.
        Possible exceptions: (ValueError).
        """

    def getHiddenEdges(self) -> list[PartModule.Edge]:
        """getHiddenEdges() - get the hidden edges in the View as Part::TopoShapeEdges"""

    def getVertexByIndex(self, vertexIndex: int = 0, /) -> PartModule.Vertex:
        """
        getVertexByIndex(vertexIndex). Returns Part.TopoShape.
        Possible exceptions: (ValueError).
        """

    def getVertexBySelection(self, selName: str, /) -> PartModule.Vertex:
        """
        getVertexBySelection(vertexName). Returns Part.TopoShape.
        Possible exceptions: (ValueError).
        """

    def getVisibleEdges(self) -> list[PartModule.Edge]:
        """getVisibleEdges() - get the visible edges in the View as Part::TopoShapeEdges"""

    def makeCenterLine(self, pSubs: list, mode: int = 0, /) -> str:
        """
        makeCenterLine(subNames, mode) - draw a center line on this viewPart. SubNames is a list of n Faces, 2 Edges or 2 Vertices (ex [Face1,Face2,Face3]. Returns unique tag of added CenterLine.
        Possible exceptions: (TypeError, RuntimeError).
        """

    def makeCosmeticCircle(self, pPnt1: FreeCAD.Vector = None, radius: float = 5.0, style: int = None, weight: float = None, pColor: tuple = None, /) -> str:
        """
        tag = makeCosmeticCircle(center, radius) - add a CosmeticEdge at center with radius radius(View coordinates). Returns tag of new CosmeticEdge.
        Possible exceptions: (RuntimeError).
        """

    def makeCosmeticCircleArc(self, pPnt1: FreeCAD.Vector = None, radius: float = 5.0, angle1: float = 0.0, angle2: float = 360.0, style: int = None, weight: float = None, pColor: tuple = None, /) -> str:
        """
        tag = makeCosmeticCircleArc(center, radius, start, end) - add a CosmeticEdge at center with radius radius(View coordinates) from start angle to end angle. Returns tag of new CosmeticEdge.
        Possible exceptions: (RuntimeError).
        """

    def makeCosmeticLine(self, pPnt1: FreeCAD.Vector = None, pPnt2: FreeCAD.Vector = None, style: int = None, weight: float = None, pColor: tuple = None, /) -> str:
        """
        tag = makeCosmeticLine(p1, p2) - add a CosmeticEdge from p1 to p2(View coordinates). Returns tag of new CosmeticEdge.
        Possible exceptions: (RuntimeError).
        """

    def makeCosmeticLine3D(self, pPnt1: FreeCAD.Vector = None, pPnt2: FreeCAD.Vector = None, style: int = None, weight: float = None, pColor: tuple = None, /) -> str:
        """
        tag = makeCosmeticLine3D(p1, p2) - add a CosmeticEdge from p1 to p2(3D coordinates). Returns tag of new CosmeticEdge.
        Possible exceptions: (RuntimeError).
        """

    def makeCosmeticVertex(self, pPnt1: FreeCAD.Vector = None, /) -> str:
        """id = makeCosmeticVertex(p1) - add a CosmeticVertex at p1 (View coordinates). Returns unique id vertex."""

    def makeCosmeticVertex3d(self, pPnt1: FreeCAD.Vector = None, /) -> str:
        """id = makeCosmeticVertex3d(p1) - add a CosmeticVertex at p1 (3d model coordinates). Returns unique id vertex."""

    def projectPoint(self, pPoint: FreeCAD.Vector = None, pInvert: bool = False, /) -> FreeCAD.Vector:
        """
        projectPoint(vector3d point, [bool invert]). Returns the projection of point in the
                projection coordinate system of this DrawViewPart. Optionally inverts the Y coordinate of the
                result.
        """

    def removeCenterLine(self, tag: str, /):
        """removeCenterLine(cl) - remove CenterLine cl from View. Returns None."""

    def removeCosmeticEdge(self, tag: str, /):
        """removeCosmeticEdge(ce) - remove CosmeticEdge ce from View. Returns None."""

    @typing.overload
    def removeCosmeticVertex(self, tag: str, /): ...

    @typing.overload
    def removeCosmeticVertex(self, pCVToDelete: TechDraw.CosmeticVertex = None, /): ...

    @typing.overload
    def removeCosmeticVertex(self, pDelList=None, /):
        """
        removeCosmeticVertex(cv) - remove CosmeticVertex from View. Returns None.
        Possible exceptions: (TypeError).
        """

    def requestPaint(self):
        """requestPaint(). Redraw the graphic for this View."""


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


# CenterLinePy.xml
class CenterLine(FreeCAD.PyObjectBase):
    """CenterLine specifies additional mark up edges in a View"""

    @property
    def Edges(self) -> list:
        """The names of source edges for this CenterLine."""

    @property
    def Extension(self) -> float:
        """The additional length to be added to this CenterLine."""

    @property
    def Faces(self) -> list:
        """The names of source Faces for this CenterLine."""

    @property
    def Flip(self) -> bool:
        """Reverse the order of points for 2 point CenterLine."""

    @property
    def Format(self) -> ReturnGetFormatDict:
        """The appearance attributes (style, color, weight, visible) for this CenterLine."""

    @property
    def HorizShift(self) -> float:
        """The left/right offset for this CenterLine."""

    @property
    def Mode(self) -> int:
        """0 - vert/ 1 - horiz/ 2 - aligned."""

    @property
    def Points(self) -> list:
        """The names of source Points for this CenterLine."""

    @property
    def Rotation(self) -> float:
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
        """
        Create a clone of this centerline
        Possible exceptions: (RuntimeError).
        """

    def copy(self):
        """
        Create a copy of this centerline
        Possible exceptions: (RuntimeError).
        """


# DrawTileWeldPy.xml
class DrawTileWeld(TechDraw.DrawTile):
    """Feature for adding welding tiles to leader lines"""

    @property
    def CenterText(self) -> str:
        """
        Property group: TileWeld.
        Property TypeId: App::PropertyString.
        Text above/below symbol.
        """

    @CenterText.setter
    def CenterText(self, value: str): ...

    @property
    def LeftText(self) -> str:
        """
        Property group: TileWeld.
        Property TypeId: App::PropertyString.
        Text before symbol.
        """

    @LeftText.setter
    def LeftText(self, value: str): ...

    @property
    def RightText(self) -> str:
        """
        Property group: TileWeld.
        Property TypeId: App::PropertyString.
        Text after symbol.
        """

    @RightText.setter
    def RightText(self, value: str): ...

    @property
    def SymbolFile(self) -> str:
        """
        Property group: TileWeld.
        Property TypeId: App::PropertyFile.
        Symbol File.
        """

    @SymbolFile.setter
    def SymbolFile(self, value: str): ...

    @property
    def SymbolIncluded(self) -> str:
        """
        Property group: TileWeld.
        Property TypeId: App::PropertyFileIncluded.
        Embedded Symbol. System use only.
        """

    @SymbolIncluded.setter
    def SymbolIncluded(self, value: StrIO_t | tuple[StrIO_t, StrIO_t]): ...


# DrawPagePy.xml
class DrawPage(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Pages"""

    @property
    def PageHeight(self) -> float:
        """Returns the height of this page"""

    @property
    def PageOrientation(self) -> str:
        """Returns the orientation of this page"""

    @property
    def PageWidth(self) -> float:
        """Returns the width of this page"""

    @property
    def KeepUpdated(self) -> bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Page.
        Property TypeId: App::PropertyBool.
        Keep page in sync with model.
        """

    @KeepUpdated.setter
    def KeepUpdated(self, value: int | bool): ...

    @property
    def NextBalloonIndex(self) -> int:
        """
        Property group: Page.
        Property TypeId: App::PropertyInteger.
        Auto-numbering for Balloons.
        """

    @NextBalloonIndex.setter
    def NextBalloonIndex(self, value: int): ...

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

    def addView(self, pcDocObj: TechDraw.DrawView, /) -> int:
        """addView(DrawView) - Add a View to this Page"""

    def getAllViews(self) -> list[TechDraw.DrawProjGroupItem | TechDraw.DrawViewPart | TechDraw.DrawViewAnnotation | TechDraw.DrawView]:
        """getAllViews() - returns a list of all the views on page including Views inside Collections"""

    def removeView(self, pcDocObj: TechDraw.DrawView, /) -> int:
        """removeView(DrawView) - Remove a View to this Page"""

    def requestPaint(self):
        """Ask the Gui to redraw this page"""


# DrawHatchPy.xml
class DrawHatch(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Hatch areas"""

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

    @property
    def SvgIncluded(self) -> str:
        """
        Property group: Hatch.
        Property TypeId: App::PropertyFileIncluded.
        Embedded SVG hatch file. System use only.
        """

    @SvgIncluded.setter
    def SvgIncluded(self, value: StrIO_t | tuple[StrIO_t, StrIO_t]): ...


# DrawProjGroupItemPy.xml
class DrawProjGroupItem(TechDraw.DrawViewPart):
    """Feature for creating and manipulating component Views Technical Drawing Projection Groups"""

    @property
    def RotationVector(self) -> FreeCAD.Vector:
        """
        Property group: Base.
        Property TypeId: App::PropertyVector.
        Deprecated. Use XDirection.
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


# CosmeticEdgePy.xml
class CosmeticEdge(FreeCAD.PyObjectBase):
    """CosmeticEdge specifies an extra (cosmetic) edge in Views"""

    @property
    def Center(self) -> FreeCAD.Vector:
        """Gives the position of center point of this CosmeticEdge as vector."""

    @property
    def End(self) -> FreeCAD.Vector:
        """Gives the position of one end of this CosmeticEdge as vector."""

    @property
    def Format(self) -> ReturnGetFormatDict:
        """The appearance attributes (style, weight, color, visible) for this CosmeticEdge."""

    @property
    def Radius(self) -> float:
        """Gives the radius of CosmeticEdge in mm."""

    @property
    def Start(self) -> FreeCAD.Vector:
        """Gives the position of one end of this CosmeticEdge as vector."""

    @property
    def Tag(self) -> str:
        """Gives the tag of the CosmeticEdge as string."""

    def clone(self):
        """
        Create a clone of this CosmeticEdge
        Possible exceptions: (RuntimeError).
        """

    def copy(self):
        """
        Create a copy of this CosmeticEdge
        Possible exceptions: (RuntimeError).
        """


# GeomFormatPy.xml
class GeomFormat(FreeCAD.PyObjectBase):
    """GeomFormat specifies appearance parameters for TechDraw Geometry objects"""

    @property
    def Tag(self) -> str:
        """Gives the tag of the GeomFormat as string."""

    def clone(self):
        """
        Create a clone of this geomformat
        Possible exceptions: (RuntimeError).
        """

    def copy(self):
        """
        Create a copy of this geomformat
        Possible exceptions: (RuntimeError).
        """


# AppTechDrawPy.cpp
def edgeWalker(pcObj: list = None, inclBig=True, /) -> list[PartModule.Wire] | None:
    """
    [wires] = edgeWalker(edgePile, inclBiggest) -- Planar graph traversal finds wires in edge pile.
    Possible exceptions: (TypeError, Part.OCCError, Exception).
    """


def findOuterWire(pcObj: list = None, /) -> PartModule.Wire | None:
    """
    wire = findOuterWire(edgeList) -- Planar graph traversal finds OuterWire in edge pile.
    Possible exceptions: (TypeError, Part.OCCError, Exception).
    """


def findShapeOutline(pcObjShape, scale: float, pcObjDir, /) -> PartModule.Wire | None:
    """
    wire = findShapeOutline(shape, scale, direction) -- Project shape in direction and find outer wire of result.
    Possible exceptions: (TypeError, Part.OCCError, Exception).
    """


def viewPartAsDxf(viewObj, /) -> str:
    """
    string = viewPartAsDxf(DrawViewPart) -- Return the edges of a DrawViewPart in Dxf format.
    Possible exceptions: (TypeError, Exception).
    """


def viewPartAsSvg(viewObj, /) -> str:
    """
    string = viewPartAsSvg(DrawViewPart) -- Return the edges of a DrawViewPart in Svg format.
    Possible exceptions: (TypeError, Exception).
    """


def writeDXFView(viewObj, name: str, alignObj=True, /) -> None:
    """
    writeDXFView(view, filename): Exports a DrawViewPart to a DXF file.
    Possible exceptions: (TypeError, RuntimeError).
    """


def writeDXFPage(pageObj, name: str, /) -> None:
    """
    writeDXFPage(page, filename): Exports a DrawPage to a DXF file.
    Possible exceptions: (TypeError, RuntimeError).
    """


def findCentroid(pcObjShape, pcObjDir, /) -> FreeCAD.Vector | None:
    """
    vector = findCentroid(shape, direction): finds geometric centroid of shape looking in direction.
    Possible exceptions: (TypeError).
    """


def makeExtentDim(pDvp, pEdgeList: list, direction: int = 0, /) -> None:
    """
    makeExtentDim(DrawViewPart, [edges], direction) -- draw horizontal or vertical extent dimension for edges (or all of DrawViewPart if edge list is empty. direction:  0 - Horizontal, 1 - Vertical.
    Possible exceptions: (TypeError, Part.OCCError).
    """


def makeDistanceDim(pDvp, pDimType, pFrom, pTo, /) -> TechDraw.DrawViewDimension:
    """
    makeDistanceDim(DrawViewPart, dimType, fromPoint, toPoint) -- draw a Length dimension between fromPoint to toPoint.  FromPoint and toPoint are unscaled 2d View points. dimType is one of ['Distance', 'DistanceX', 'DistanceY'.
    Possible exceptions: (TypeError).
    """


def makeDistanceDim3d(pDvp, pDimType, pFrom, pTo, /) -> None:
    """
    makeDistanceDim(DrawViewPart, dimType, 3dFromPoint, 3dToPoint) -- draw a Length dimension between fromPoint to toPoint.  FromPoint and toPoint are unscaled 3d model points. dimType is one of ['Distance', 'DistanceX', 'DistanceY'.
    Possible exceptions: (TypeError).
    """


def makeGeomHatch(pFace, scale: float = 1.0, pPatName: str = '', pPatFile: str = '', /) -> PartModule.Compound | None:
    """
    makeGeomHatch(face, [patScale], [patName], [patFile]) -- draw a geom hatch on a given face, using optionally the given scale (default 1) and a given pattern name (ex. Diamond) and .pat file (the default pattern name and/or .pat files set in preferences are used if none are given). Returns a Part compound shape.
    Possible exceptions: (TypeError, Exception).
    """


@typing.overload
def project(TopoShape_, App_Vector_Direction, string_type, /): ...


@typing.overload
def project(pcObjShape: PartModule.Shape, pcObjDir: FreeCAD.Vector = None, /) -> list[PartModule.Shape]:
    """
    [visiblyG0, visiblyG1, hiddenG0, hiddenG1] = project(TopoShape[, App.Vector Direction, string type])
     -- Project a shape and return the visible/invisible parts of it.
    Possible exceptions: (Exception).
    """


@typing.overload
def projectEx(TopoShape_, App_Vector_Direction, string_type, /): ...


@typing.overload
def projectEx(pcObjShape: PartModule.Shape, pcObjDir: FreeCAD.Vector = None, /) -> list[PartModule.Shape]:
    """
    [V, V1, VN, VO, VI, H,H1, HN, HO, HI] = projectEx(TopoShape[, App.Vector Direction, string type])
     -- Project a shape and return the all parts of it.
    Possible exceptions: (Exception).
    """


def projectToDXF(pcObjShape: PartModule.Shape, pcObjDir: FreeCAD.Vector = None, type: str = None, scale: float = 1.0, tol: float = 0.1, /) -> str:
    """
    string = projectToDXF(TopoShape[, App.Vector Direction, string type])
     -- Project a shape and return the DXF representation as string.
    Possible exceptions: (Exception).
    """


def removeSvgTags(svgcode: str, /) -> str:
    """
    string = removeSvgTags(string) -- Removes the opening and closing svg tags
    and other metatags from a svg code, making it embeddable
    Possible exceptions: (Exception).
    """


def projectToSVG(topoShape: PartModule.Shape = None, direction: FreeCAD.Vector = None, type: str = None, tolerance: float = 0.1, vStyle=None, v0Style=None, v1Style=None, hStyle=None, h0Style=None, h1Style=None) -> str:
    """
    string = projectToSVG(TopoShape[, App.Vector direction, string type, float tolerance, dict vStyle, dict v0Style, dict v1Style, dict hStyle, dict h0Style, dict h1Style])
     -- Project a shape and return the SVG representation as string.
    Possible exceptions: (Exception).
    """


# MDIViewPage.cpp
class MDIViewPagePy:
    """Python binding class for the MDI view page class"""

    def getPage(self) -> TechDraw.DrawPage:
        """
        getPage() returns the page being displayed
        Possible exceptions: (Exception).
        """

    def cast_to_base(self):
        """cast_to_base() cast to MDIView class"""
