import typing

import FreeCADGui

_T = typing.TypeVar("_T")
Quadruple_t: typing.TypeAlias = tuple[_T, _T, _T, _T]
Triple_t: typing.TypeAlias = tuple[_T, _T, _T]


# ViewProviderMeshPy.xml
class ViewProviderMesh(FreeCADGui.ViewProviderDocumentObject):
    """This is the ViewProvider base class"""

    @property
    def Coloring(self) -> bool:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyBool.
        Set coloring.
        """

    @Coloring.setter
    def Coloring(self, value: int | bool): ...

    @property
    def CreaseAngle(self) -> float:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyFloatConstraint.
        Set crease angle.
        """

    @CreaseAngle.setter
    def CreaseAngle(self, value: float | Quadruple_t[float]): ...

    @property
    def Lighting(self) -> int:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyEnumeration.

        Set if the illumination comes from two sides
         or one side in the 3D view.
        """

    @Lighting.setter
    def Lighting(self, value: typing.Literal['One side', 'Two side']): ...

    @property
    def LineColor(self) -> tuple[float, float, float, float]:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyColor.
        Set line color.
        """

    @LineColor.setter
    def LineColor(self, value: Triple_t[float] | Quadruple_t[float] | int): ...

    @property
    def LineTransparency(self) -> int:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyPercent.
        Set line transparency.
        """

    @LineTransparency.setter
    def LineTransparency(self, value: int): ...

    @property
    def LineWidth(self) -> float:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyFloatConstraint.
        Set line width.
        """

    @LineWidth.setter
    def LineWidth(self, value: float | Quadruple_t[float]): ...

    @property
    def OpenEdges(self) -> bool:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyBool.
        Set open edges.
        """

    @OpenEdges.setter
    def OpenEdges(self, value: int | bool): ...

    @property
    def PointSize(self) -> float:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyFloatConstraint.
        Set point size.
        """

    @PointSize.setter
    def PointSize(self, value: float | Quadruple_t[float]): ...

    def addSelection(self, obj, /):
        """Add list of facets to selection"""

    def clearSelection(self):
        """Clear the selection"""

    def highlightSegments(self, list, /):
        """
        Highlights the segments of a mesh with a given list of colors.
        The number of elements of this list must be equal to the number of mesh segments.
        """

    def invertSelection(self):
        """Invert the selection"""

    def removeSelection(self, obj, /):
        """Remove list of facets from selection"""

    def setSelection(self, obj, /):
        """Select list of facets"""


# AppMeshGui.cpp
def convertToSTL(inname: str, outname: str, /) -> bool:
    """
    Convert a scene into an STL.
    Possible exceptions: (Exception).
    """
