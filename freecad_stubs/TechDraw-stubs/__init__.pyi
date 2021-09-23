import typing

import FreeCAD
import TechDraw


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
    def PatIncluded(self):
        """
        Property group: GeomHatch.
        Property TypeId: App::PropertyFileIncluded.
        Embedded Pat hatch file. System use only.
        """

    @PatIncluded.setter
    def PatIncluded(self, value): ...

    @property
    def ScalePattern(self) -> float | tuple[float, float, float, float] | tuple[float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float]]:
        """
        Property group: GeomHatch.
        Property TypeId: App::PropertyFloatConstraint.
        GeomHatch pattern size adjustment.
        """

    @ScalePattern.setter
    def ScalePattern(self, value: float | tuple[float, float, float, float] | tuple[float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float]]): ...

    @property
    def Source(self) -> FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None:
        """
        Property group: GeomHatch.
        Property TypeId: App::PropertyLinkSub.
        The View + Face to be crosshatched.
        """

    @Source.setter
    def Source(self, value: FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None): ...


# DrawLeaderLinePy.xml
class DrawLeaderLine(TechDraw.DrawView):
    """Feature for adding leaders to Technical Drawings"""

    @property
    def AutoHorizontal(self) -> int | bool:
        """
        Property group: Leader.
        Property TypeId: App::PropertyBool.
        Forces last line segment to be horizontal.
        """

    @AutoHorizontal.setter
    def AutoHorizontal(self, value: int | bool): ...

    @property
    def EndSymbol(self):
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
    def Scalable(self) -> int | bool:
        """
        Property group: Leader.
        Property TypeId: App::PropertyBool.
        Scale line with LeaderParent.
        """

    @Scalable.setter
    def Scalable(self, value: int | bool): ...

    @property
    def StartSymbol(self):
        """Property TypeId: App::PropertyEnumeration."""

    @StartSymbol.setter
    def StartSymbol(self, value): ...

    @property
    def WayPoints(self) -> dict[int, FreeCAD.Vector | tuple[float | int, float | int, float | int]] | typing.Iterable[FreeCAD.Vector | tuple[float | int, float | int, float | int]] | typing.Sequence[FreeCAD.Vector | tuple[float | int, float | int, float | int]]:
        """
        Property group: Leader.
        Property TypeId: App::PropertyVectorList.
        Intermediate points for Leader line.
        """

    @WayPoints.setter
    def WayPoints(self, value: dict[int, FreeCAD.Vector | tuple[float | int, float | int, float | int]] | typing.Iterable[FreeCAD.Vector | tuple[float | int, float | int, float | int]] | typing.Sequence[FreeCAD.Vector | tuple[float | int, float | int, float | int]]): ...


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
    def LineSpace(self) -> int | tuple[int, int, int, int]:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyPercent.
        Line spacing in %. 100 means the height of a line.
        """

    @LineSpace.setter
    def LineSpace(self, value: int | tuple[int, int, int, int]): ...

    @property
    def MaxWidth(self) -> str | float | FreeCAD.Quantity:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyLength.

        Maximum width of the annotation block.
         -1 means no maximum width.
        .
        """

    @MaxWidth.setter
    def MaxWidth(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def Text(self) -> dict[int, str | bytes] | typing.Iterable[str | bytes] | typing.Sequence[str | bytes]:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyStringList.
        Annotation text.
        """

    @Text.setter
    def Text(self, value: dict[int, str | bytes] | typing.Iterable[str | bytes] | typing.Sequence[str | bytes]): ...

    @property
    def TextColor(self) -> tuple[float, float, float] | tuple[float, float, float, float] | int:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyColor.
        Text color.
        """

    @TextColor.setter
    def TextColor(self, value: tuple[float, float, float] | tuple[float, float, float, float] | int): ...

    @property
    def TextSize(self) -> str | float | FreeCAD.Quantity:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyLength.
        Text size.
        """

    @TextSize.setter
    def TextSize(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def TextStyle(self) -> typing.Literal['Normal', '\n                                      "Bold', '\n                                      "Italic', '\n                                      "Bold-Italic']:
        """
        Property group: Annotation.
        Property TypeId: App::PropertyEnumeration.
        Text style.
        """

    @TextStyle.setter
    def TextStyle(self, value: typing.Literal['Normal', '\n                                      "Bold', '\n                                      "Italic', '\n                                      "Bold-Italic']): ...


# DrawViewClipPy.xml
class DrawViewClip(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing Clip Views"""

    @property
    def Height(self) -> str | float | FreeCAD.Quantity:
        """
        Property group: Clip Group.
        Property TypeId: App::PropertyLength.
        The height of the view area of this clip.
        """

    @Height.setter
    def Height(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def ShowFrame(self) -> int | bool:
        """
        Property group: Clip Group.
        Property TypeId: App::PropertyBool.
        Specifies if the clip frame appears on the page or not.
        """

    @ShowFrame.setter
    def ShowFrame(self, value: int | bool): ...

    @property
    def Views(self) -> dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]:
        """
        Property group: Clip Group.
        Property TypeId: App::PropertyLinkList.
        The Views in this Clip group.
        """

    @Views.setter
    def Views(self, value: dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]): ...

    @property
    def Width(self) -> str | float | FreeCAD.Quantity:
        """
        Property group: Clip Group.
        Property TypeId: App::PropertyLength.
        The width of the view area of this clip.
        """

    @Width.setter
    def Width(self, value: str | float | FreeCAD.Quantity): ...

    def addView(self, DrawView: FreeCAD.DocumentObject, /):
        """addView(DrawView) - Add a View to this ClipView"""

    def getChildViewNames(self):
        """getChildViewNames() - get a list of the DrawViews in this ClipView"""

    def removeView(self, DrawView: FreeCAD.DocumentObject, /):
        """removeView(DrawView) - Remove specified View to this ClipView"""


# DrawViewSymbolPy.xml
class DrawViewSymbol(TechDraw.DrawView):
    """Feature for creating and manipulating Drawing SVG Symbol Views"""

    @property
    def EditableTexts(self) -> dict[int, str | bytes] | typing.Iterable[str | bytes] | typing.Sequence[str | bytes]:
        """
        Property group: Drawing view.
        Property TypeId: App::PropertyStringList.
        Substitution values for the editable strings in this symbol.
        """

    @EditableTexts.setter
    def EditableTexts(self, value: dict[int, str | bytes] | typing.Iterable[str | bytes] | typing.Sequence[str | bytes]): ...

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
        """dumpSymbol(fileSpec) - dump the contents of Symbol to a file"""


# DrawViewCollectionPy.xml
class DrawViewCollection(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing View Collections"""

    @property
    def Views(self) -> dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]:
        """
        Property group: Collection.
        Property TypeId: App::PropertyLinkList.
        Collection Views.
        """

    @Views.setter
    def Views(self, value: dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]): ...

    def addView(self, DrawView_object: FreeCAD.DocumentObject, /):
        """addView(DrawView object) - Add a new View to this Group. Returns count of views."""

    def removeView(self, DrawView_object: FreeCAD.DocumentObject, /):
        """removeView(DrawView object) - Remove specified Viewfrom this Group. Returns count of views in Group."""


# CosmeticExtensionPy.xml
class CosmeticExtension(FreeCAD.DocumentObjectExtension):
    """This object represents cosmetic features for a DrawViewPart."""

    @property
    def CenterLines(self):
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Cosmetics.
        Property TypeId: TechDraw::PropertyCenterLineList.
        Geometry format Save/Restore.
        """

    @CenterLines.setter
    def CenterLines(self, value): ...

    @property
    def CosmeticEdges(self):
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Cosmetics.
        Property TypeId: TechDraw::PropertyCosmeticEdgeList.
        CosmeticEdge Save/Restore.
        """

    @CosmeticEdges.setter
    def CosmeticEdges(self, value): ...

    @property
    def CosmeticVertexes(self):
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Cosmetics.
        Property TypeId: TechDraw::PropertyCosmeticVertexList.
        CosmeticVertex Save/Restore.
        """

    @CosmeticVertexes.setter
    def CosmeticVertexes(self, value): ...

    @property
    def GeomFormats(self):
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Cosmetics.
        Property TypeId: TechDraw::PropertyGeomFormatList.
        Geometry format Save/Restore.
        """

    @GeomFormats.setter
    def GeomFormats(self, value): ...


# DrawViewDimExtentPy.xml
class DrawViewDimExtent(TechDraw.DrawViewDimension):
    """Feature for creating and manipulating Technical Drawing DimExtents"""

    @property
    def CosmeticTags(self) -> dict[int, str | bytes] | typing.Iterable[str | bytes] | typing.Sequence[str | bytes]:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyStringList.
        Id of cosmetic endpoints.
        """

    @CosmeticTags.setter
    def CosmeticTags(self, value: dict[int, str | bytes] | typing.Iterable[str | bytes] | typing.Sequence[str | bytes]): ...

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
    def Source(self) -> dict[int, FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Iterable[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Sequence[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None]:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyLinkSubList.
        View (Edges) to dimension.
        """

    @Source.setter
    def Source(self, value: dict[int, FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Iterable[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Sequence[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None]): ...

    @property
    def Source3d(self) -> dict[int, FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Iterable[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Sequence[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None]:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyLinkSubList.
        View (Edges) to dimension.
        """

    @Source3d.setter
    def Source3d(self, value: dict[int, FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Iterable[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Sequence[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None]): ...

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
    def MaxWidth(self) -> float | int:
        """
        Property group: Text Block.
        Property TypeId: App::PropertyFloat.
        Width limit before auto wrap.
        """

    @MaxWidth.setter
    def MaxWidth(self, value: float | int): ...

    @property
    def ShowFrame(self) -> int | bool:
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
    def TileRow(self) -> int | tuple[int, int, int, int]:
        """
        Property group: Tile.
        Property TypeId: App::PropertyIntegerConstraint.

        Row in parent object
         0 for arrow side, -1 for other side
        .
        """

    @TileRow.setter
    def TileRow(self, value: int | tuple[int, int, int, int]): ...


# DrawViewDimensionPy.xml
class DrawViewDimension(TechDraw.DrawView):
    """Feature for creating and manipulating Technical Drawing Dimensions"""

    @property
    def Arbitrary(self) -> int | bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Format.
        Property TypeId: App::PropertyBool.
        Value overridden by user.
        """

    @Arbitrary.setter
    def Arbitrary(self, value: int | bool): ...

    @property
    def ArbitraryTolerances(self) -> int | bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Format.
        Property TypeId: App::PropertyBool.
        Tolerance values overridden by user.
        """

    @ArbitraryTolerances.setter
    def ArbitraryTolerances(self, value: int | bool): ...

    @property
    def EqualTolerance(self) -> int | bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyBool.
        If over- and undertolerance are equal.
        """

    @EqualTolerance.setter
    def EqualTolerance(self, value: int | bool): ...

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
    def Inverted(self) -> int | bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyBool.
        The dimensional value is displayed inverted.
        """

    @Inverted.setter
    def Inverted(self, value: int | bool): ...

    @property
    def MeasureType(self) -> typing.Literal['True', '\n                                                    "Projected']:
        """Property TypeId: App::PropertyEnumeration."""

    @MeasureType.setter
    def MeasureType(self, value: typing.Literal['True', '\n                                                    "Projected']): ...

    @property
    def OverTolerance(self):
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: FormatSpec.

        Overtolerance value
        If 'Equal Tolerance' is true this is also
        the negated value for 'Under Tolerance'
        .
        """

    @OverTolerance.setter
    def OverTolerance(self, value): ...

    @property
    def References2D(self) -> dict[int, FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Iterable[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Sequence[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None]:
        """
        Property TypeId: App::PropertyLinkSubList.
        Projected Geometry References.
        """

    @References2D.setter
    def References2D(self, value: dict[int, FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Iterable[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Sequence[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None]): ...

    @property
    def References3D(self) -> dict[int, FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Iterable[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Sequence[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None]:
        """
        Property TypeId: App::PropertyLinkSubList.
        3D Geometry References.
        """

    @References3D.setter
    def References3D(self, value: dict[int, FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Iterable[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Sequence[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None]): ...

    @property
    def TheoreticalExact(self) -> int | bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: App::PropertyBool.
        If theoretical exact (basic) dimension.
        """

    @TheoreticalExact.setter
    def TheoreticalExact(self, value: int | bool): ...

    @property
    def Type(self):
        """Property TypeId: Measure."""

    @Type.setter
    def Type(self, value): ...

    @property
    def UnderTolerance(self):
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property TypeId: FormatSpec.

        Undertolerance value
        If 'Equal Tolerance' is true it will be replaced
        by negative value of 'Over Tolerance'
        .
        """

    @UnderTolerance.setter
    def UnderTolerance(self, value): ...

    def getAnglePoints(self):
        """getAnglePoints() - returns list of points for angle Dimension"""

    def getArcPoints(self):
        """getArcPoints() - returns list of points for circle/arc Dimension"""

    def getArrowPositions(self):
        """getArrowPositions() - returns list of locations or Dimension Arrowheads. Locations are in unscaled coordinates of parent View"""

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
    def LockPosition(self) -> int | bool:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Base.
        Property TypeId: App::PropertyBool.
        Lock View position to parent Page or Group.
        """

    @LockPosition.setter
    def LockPosition(self, value: int | bool): ...

    @property
    def Rotation(self) -> str | float | FreeCAD.Quantity:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Base.
        Property TypeId: App::PropertyAngle.
        Rotation in degrees counterclockwise.
        """

    @Rotation.setter
    def Rotation(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def Scale(self) -> float | tuple[float, float, float, float] | tuple[float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float]]:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Base.
        Property TypeId: App::PropertyFloatConstraint.
        Scale factor of the view. Scale factors like 1:100 can be written as =1/100.
        """

    @Scale.setter
    def Scale(self, value: float | tuple[float, float, float, float] | tuple[float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float]]): ...

    @property
    def ScaleType(self) -> typing.Literal['Page', '\n                                         "Automatic', '\n                                         "Custom']:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Base.
        Property TypeId: App::PropertyEnumeration.
        Scale Type.
        """

    @ScaleType.setter
    def ScaleType(self, value: typing.Literal['Page', '\n                                         "Automatic', '\n                                         "Custom']): ...

    @property
    def X(self) -> str | float | FreeCAD.Quantity | FreeCAD.Unit:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        [Prop_NoRecompute] Modified property doesn't touch its container for recompute.
        Property group: Base.
        Property TypeId: App::PropertyDistance.
        X position.
        """

    @X.setter
    def X(self, value: str | float | FreeCAD.Quantity | FreeCAD.Unit): ...

    @property
    def Y(self) -> str | float | FreeCAD.Quantity | FreeCAD.Unit:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        [Prop_NoRecompute] Modified property doesn't touch its container for recompute.
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
    def PageResult(self):
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Template.
        Property TypeId: App::PropertyFileIncluded.
        Current SVG code for template.
        """

    @PageResult.setter
    def PageResult(self, value): ...

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

    def getEditFieldContent(self, EditFieldName: str, /):
        """getEditFieldContent(EditFieldName) - returns the content of a specific Editable Text Field"""

    def setEditFieldContent(self, EditFieldName: str, NewContent: str, /):
        """setEditFieldContent(EditFieldName, NewContent) - sets a specific Editable Text Field to a new value"""


# DrawWeldSymbolPy.xml
class DrawWeldSymbol(TechDraw.DrawView):
    """Feature for adding welding tiles to leader lines"""

    @property
    def AllAround(self) -> int | bool:
        """
        Property group: Weld Symbol.
        Property TypeId: App::PropertyBool.
        All Around Symbol on/off.
        """

    @AllAround.setter
    def AllAround(self, value: int | bool): ...

    @property
    def AlternatingWeld(self) -> int | bool:
        """
        Property group: Weld Symbol.
        Property TypeId: App::PropertyBool.
        Alternating Weld true/false.
        """

    @AlternatingWeld.setter
    def AlternatingWeld(self, value: int | bool): ...

    @property
    def FieldWeld(self) -> int | bool:
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
    def AutoDistribute(self) -> int | bool:
        """
        Property group: Distribute.
        Property TypeId: App::PropertyBool.
        Distribute views automatically or manually.
        """

    @AutoDistribute.setter
    def AutoDistribute(self, value: int | bool): ...

    @property
    def ProjectionType(self) -> typing.Literal['First Angle', '\n                                                    "Third Angle', '\n                                                    "Default']:
        """
        Property group: Base.
        Property TypeId: App::PropertyEnumeration.
        First or Third angle projection.
        """

    @ProjectionType.setter
    def ProjectionType(self, value: typing.Literal['First Angle', '\n                                                    "Third Angle', '\n                                                    "Default']): ...

    @property
    def Source(self) -> dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]:
        """
        Property group: Base.
        Property TypeId: App::PropertyLinkList.
        Shape to view.
        """

    @Source.setter
    def Source(self, value: dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]): ...

    @property
    def XSource(self) -> dict[int, FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Iterable[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Sequence[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None]:
        """
        Property group: Base.
        Property TypeId: App::PropertyXLinkList.
        External 3D Shape to view.
        """

    @XSource.setter
    def XSource(self, value: dict[int, FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Iterable[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Sequence[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None]): ...

    @property
    def spacingX(self) -> str | float | FreeCAD.Quantity:
        """
        Property group: Distribute.
        Property TypeId: App::PropertyLength.

        If AutoDistribute is on, this is the horizontal 
        spacing between the borders of views 
        (if label width is not wider than the object)
        .
        """

    @spacingX.setter
    def spacingX(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def spacingY(self) -> str | float | FreeCAD.Quantity:
        """
        Property group: Distribute.
        Property TypeId: App::PropertyLength.

        If AutoDistribute is on, this is the vertical 
        spacing between the borders of views
        .
        """

    @spacingY.setter
    def spacingY(self, value: str | float | FreeCAD.Quantity): ...

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
    def CoarseView(self) -> int | bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Coarse View on/off.
        """

    @CoarseView.setter
    def CoarseView(self, value: int | bool): ...

    @property
    def Direction(self) -> FreeCAD.Vector | tuple[float | int, float | int, float | int]:
        """
        Property group: Projection.
        Property TypeId: App::PropertyVector.
        Projection Plane normal. The direction you are looking from.
        """

    @Direction.setter
    def Direction(self, value: FreeCAD.Vector | tuple[float | int, float | int, float | int]): ...

    @property
    def Focus(self) -> str | float | FreeCAD.Quantity | FreeCAD.Unit:
        """
        Property group: Projection.
        Property TypeId: App::PropertyDistance.
        Perspective view focus distance.
        """

    @Focus.setter
    def Focus(self, value: str | float | FreeCAD.Quantity | FreeCAD.Unit): ...

    @property
    def HardHidden(self) -> int | bool:
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
    def IsoHidden(self) -> int | bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Show Hidden Iso u,v lines.
        """

    @IsoHidden.setter
    def IsoHidden(self, value: int | bool): ...

    @property
    def IsoVisible(self) -> int | bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Show Visible Iso u,v lines.
        """

    @IsoVisible.setter
    def IsoVisible(self, value: int | bool): ...

    @property
    def Perspective(self) -> int | bool:
        """
        Property group: Projection.
        Property TypeId: App::PropertyBool.
        Perspective(true) or Orthographic(false) projection.
        """

    @Perspective.setter
    def Perspective(self, value: int | bool): ...

    @property
    def SeamHidden(self) -> int | bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Show Hidden Seam lines.
        """

    @SeamHidden.setter
    def SeamHidden(self, value: int | bool): ...

    @property
    def SeamVisible(self) -> int | bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Show Visible Seam lines.
        """

    @SeamVisible.setter
    def SeamVisible(self, value: int | bool): ...

    @property
    def SmoothHidden(self) -> int | bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Show Hidden Smooth lines.
        """

    @SmoothHidden.setter
    def SmoothHidden(self, value: int | bool): ...

    @property
    def SmoothVisible(self) -> int | bool:
        """
        Property group: HLR Parameters.
        Property TypeId: App::PropertyBool.
        Show Visible Smooth lines.
        """

    @SmoothVisible.setter
    def SmoothVisible(self, value: int | bool): ...

    @property
    def Source(self) -> dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]:
        """
        Property group: Projection.
        Property TypeId: App::PropertyLinkList.
        3D Shape to view.
        """

    @Source.setter
    def Source(self, value: dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]): ...

    @property
    def XDirection(self) -> FreeCAD.Vector | tuple[float | int, float | int, float | int]:
        """
        Property group: Projection.
        Property TypeId: App::PropertyVector.
        Projection Plane X Axis in R3. Rotates/Mirrors View.
        """

    @XDirection.setter
    def XDirection(self, value: FreeCAD.Vector | tuple[float | int, float | int, float | int]): ...

    @property
    def XSource(self) -> dict[int, FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Iterable[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Sequence[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None]:
        """
        Property group: Projection.
        Property TypeId: App::PropertyXLinkList.
        External 3D Shape to view.
        """

    @XSource.setter
    def XSource(self, value: dict[int, FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Iterable[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None] | typing.Sequence[FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None]): ...

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
    def Height(self) -> str | float | FreeCAD.Quantity:
        """
        Property group: Page Properties.
        Property TypeId: App::PropertyLength.
        Height of page.
        """

    @Height.setter
    def Height(self, value: str | float | FreeCAD.Quantity): ...

    @property
    def Orientation(self) -> typing.Literal['Portrait', '\n                                                  "Landscape']:
        """Property TypeId: App::PropertyEnumeration."""

    @Orientation.setter
    def Orientation(self, value: typing.Literal['Portrait', '\n                                                  "Landscape']): ...

    @property
    def Width(self) -> str | float | FreeCAD.Quantity:
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
    def SymbolIncluded(self):
        """
        Property group: TileWeld.
        Property TypeId: App::PropertyFileIncluded.
        Embedded Symbol. System use only.
        """

    @SymbolIncluded.setter
    def SymbolIncluded(self, value): ...


# DrawPagePy.xml
class DrawPage(FreeCAD.DocumentObject):
    """Feature for creating and manipulating Technical Drawing Pages"""

    @property
    def KeepUpdated(self) -> int | bool:
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
    def ProjectionType(self) -> typing.Literal[' "First Angle', '\n                                                "Third Angle']:
        """Property TypeId: App::PropertyEnumeration."""

    @ProjectionType.setter
    def ProjectionType(self, value: typing.Literal[' "First Angle', '\n                                                "Third Angle']): ...

    @property
    def Scale(self) -> float | tuple[float, float, float, float] | tuple[float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float]]:
        """
        Property group: Page.
        Property TypeId: App::PropertyFloatConstraint.
        Scale factor for this Page.
        """

    @Scale.setter
    def Scale(self, value: float | tuple[float, float, float, float] | tuple[float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float]]): ...

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
    def Views(self) -> dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]:
        """
        Property group: Page.
        Property TypeId: App::PropertyLinkList.
        Attached Views.
        """

    @Views.setter
    def Views(self, value: dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]): ...

    def addView(self, DrawView: FreeCAD.DocumentObject, /):
        """addView(DrawView) - Add a View to this Page"""

    def getAllViews(self):
        """getAllViews() - returns a list of all the views on page including Views inside Collections"""

    def removeView(self, DrawView: FreeCAD.DocumentObject, /):
        """removeView(DrawView) - Remove a View to this Page"""


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
    def Source(self) -> FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None:
        """
        Property group: Hatch.
        Property TypeId: App::PropertyLinkSub.
        The View + Face to be hatched.
        """

    @Source.setter
    def Source(self, value: FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None): ...

    @property
    def SvgIncluded(self):
        """
        Property group: Hatch.
        Property TypeId: App::PropertyFileIncluded.
        Embedded SVG hatch file. System use only.
        """

    @SvgIncluded.setter
    def SvgIncluded(self, value): ...


# DrawProjGroupItemPy.xml
class DrawProjGroupItem(TechDraw.DrawViewPart):
    """Feature for creating and manipulating component Views Technical Drawing Projection Groups"""

    @property
    def RotationVector(self) -> FreeCAD.Vector | tuple[float | int, float | int, float | int]:
        """
        Property group: Base.
        Property TypeId: App::PropertyVector.
        Deprecated. Use XDirection.
        """

    @RotationVector.setter
    def RotationVector(self, value: FreeCAD.Vector | tuple[float | int, float | int, float | int]): ...

    @property
    def Type(self) -> typing.Literal['Front', '\n                                             "Left', '\n                                             "Right', '\n                                             "Rear', '\n                                             "Top', '\n                                             "Bottom', '\n                                             "FrontTopLeft', '\n                                             "FrontTopRight', '\n                                             "FrontBottomLeft', '\n                                             "FrontBottomRight']:
        """Property TypeId: App::PropertyEnumeration."""

    @Type.setter
    def Type(self, value: typing.Literal['Front', '\n                                             "Left', '\n                                             "Right', '\n                                             "Rear', '\n                                             "Top', '\n                                             "Bottom', '\n                                             "FrontTopLeft', '\n                                             "FrontTopRight', '\n                                             "FrontBottomLeft', '\n                                             "FrontBottomRight']): ...

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
