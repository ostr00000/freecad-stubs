import typing

import FreeCADGui


# ViewProviderMeshPy.xml
class ViewProviderMesh(FreeCADGui.ViewProviderDocumentObject):
    """This is the ViewProvider base class"""

    @property
    def Coloring(self) -> int | bool:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyBool.
        Set coloring.
        """

    @Coloring.setter
    def Coloring(self, value: int | bool): ...

    @property
    def CreaseAngle(self) -> float | tuple[float, float, float, float] | tuple[float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float]]:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyFloatConstraint.
        Set crease angle.
        """

    @CreaseAngle.setter
    def CreaseAngle(self, value: float | tuple[float, float, float, float] | tuple[float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float]]): ...

    @property
    def Lighting(self) -> typing.Literal['One side', 'Two side']:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyEnumeration.
        Set if the illumination comes from two sides
         or one side in the 3D view.
        """

    @Lighting.setter
    def Lighting(self, value: typing.Literal['One side', 'Two side']): ...

    @property
    def LineColor(self) -> tuple[float, float, float] | tuple[float, float, float, float] | int:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyColor.
        Set line color.
        """

    @LineColor.setter
    def LineColor(self, value: tuple[float, float, float] | tuple[float, float, float, float] | int): ...

    @property
    def LineTransparency(self) -> int | tuple[int, int, int, int]:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyPercent.
        Set line transparency.
        """

    @LineTransparency.setter
    def LineTransparency(self, value: int | tuple[int, int, int, int]): ...

    @property
    def LineWidth(self) -> float | tuple[float, float, float, float] | tuple[float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float]]:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyFloatConstraint.
        Set line width.
        """

    @LineWidth.setter
    def LineWidth(self, value: float | tuple[float, float, float, float] | tuple[float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float]]): ...

    @property
    def OpenEdges(self) -> int | bool:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyBool.
        Set open edges.
        """

    @OpenEdges.setter
    def OpenEdges(self, value: int | bool): ...

    @property
    def PointSize(self) -> float | tuple[float, float, float, float] | tuple[float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float]]:
        """
        Property group: Object Style.
        Property TypeId: App::PropertyFloatConstraint.
        Set point size.
        """

    @PointSize.setter
    def PointSize(self, value: float | tuple[float, float, float, float] | tuple[float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float], float | tuple[float, float, float, float]]): ...

    def addSelection(self, arg1: object, /):
        """Add list of facets to selection"""

    def clearSelection(self):
        """Clear the selection"""

    def highlightSegments(self, arg1: object, /):
        """Highlights the segments of a mesh with a given list of colors.
        The number of elements of this list must be equal to the number of mesh segments.
                        """

    def invertSelection(self):
        """Invert the selection"""

    def removeSelection(self, arg1: object, /):
        """Remove list of facets from selection"""

    def setSelection(self, arg1: object, /):
        """Select list of facets"""


# AppMeshGui.cpp
def convertToSTL(arg1: str, arg2: str, /):
    """Convert a scene into an STL."""
