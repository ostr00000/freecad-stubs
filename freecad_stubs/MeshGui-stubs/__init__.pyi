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
        """Property TypeId: App::PropertyBool."""

    @Coloring.setter
    def Coloring(self, value: int | bool): ...

    @property
    def CreaseAngle(self) -> float:
        """Property TypeId: App::PropertyFloatConstraint."""

    @CreaseAngle.setter
    def CreaseAngle(self, value: float | Quadruple_t[float]): ...

    @property
    def Lighting(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @Lighting.setter
    def Lighting(self, value: typing.Literal['One side', 'Two side']): ...

    @property
    def LineColor(self) -> tuple[float, float, float, float]:
        """Property TypeId: App::PropertyColor."""

    @LineColor.setter
    def LineColor(self, value: Triple_t[float] | Quadruple_t[float] | int): ...

    @property
    def LineTransparency(self) -> int:
        """Property TypeId: App::PropertyPercent."""

    @LineTransparency.setter
    def LineTransparency(self, value: int): ...

    @property
    def LineWidth(self) -> float:
        """Property TypeId: App::PropertyFloatConstraint."""

    @LineWidth.setter
    def LineWidth(self, value: float | Quadruple_t[float]): ...

    @property
    def OpenEdges(self) -> bool:
        """Property TypeId: App::PropertyBool."""

    @OpenEdges.setter
    def OpenEdges(self, value: int | bool): ...

    @property
    def PointSize(self) -> float:
        """Property TypeId: App::PropertyFloatConstraint."""

    @PointSize.setter
    def PointSize(self, value: float | Quadruple_t[float]): ...

    def addSelection(self, arg1, /):
        """Add list of facets to selection"""

    def clearSelection(self):
        """Clear the selection"""

    def invertSelection(self):
        """Invert the selection"""

    def removeSelection(self, arg1, /):
        """Remove list of facets from selection"""

    def setSelection(self, arg1, /):
        """Select list of facets"""
