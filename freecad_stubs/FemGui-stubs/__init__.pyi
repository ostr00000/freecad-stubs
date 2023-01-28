import typing

import FreeCAD
import FreeCADGui

_T = typing.TypeVar("_T")
Triple_t: typing.TypeAlias = tuple[_T, _T, _T]
Quadruple_t: typing.TypeAlias = tuple[_T, _T, _T, _T]


# ViewProviderFemPostPipelinePy.xml
class ViewProviderFemPostPipeline(FreeCADGui.ViewProviderDocumentObject):
    """ViewProviderFemPostPipeline class"""

    def transformField(self, FieldName: str, FieldFactor: float, /):
        """Scales values of given result mesh field by given factor"""

    def updateColorBars(self):
        """Update coloring of pipeline and its childs"""


# ViewProviderFemMeshPy.xml
class ViewProviderFemMesh(FreeCADGui.ViewProviderDocumentObject):
    """ViewProviderFemMesh class"""

    @property
    def ElementColor(self) -> dict:
        """Postprocessing color of the elements. All faces of the element get the same color."""

    @ElementColor.setter
    def ElementColor(self, value: dict): ...

    @property
    def HighlightedNodes(self) -> list[int]:
        """List of nodes which get highlighted."""

    @HighlightedNodes.setter
    def HighlightedNodes(self, value: list): ...

    @property
    def NodeColor(self) -> dict:
        """Postprocessing color of the nodes. The faces between the nodes get interpolated."""

    @NodeColor.setter
    def NodeColor(self, value: dict): ...

    @property
    def NodeDisplacement(self) -> dict:
        """Postprocessing color of the nodes. The faces between the nodes get interpolated."""

    @NodeDisplacement.setter
    def NodeDisplacement(self, value: dict): ...

    @property
    def VisibleElementFaces(self) -> list:
        """List of elements and faces which are actually shown. These are all surface faces of the mesh."""

    @property
    def BackfaceCulling(self) -> bool:
        """Property TypeId: App::PropertyBool."""

    @BackfaceCulling.setter
    def BackfaceCulling(self, value: int | bool): ...

    @property
    def LineWidth(self) -> float:
        """Property TypeId: App::PropertyFloatConstraint."""

    @LineWidth.setter
    def LineWidth(self, value: float | Quadruple_t[float]): ...

    @property
    def MaxFacesShowInner(self) -> int:
        """Property TypeId: App::PropertyInteger."""

    @MaxFacesShowInner.setter
    def MaxFacesShowInner(self, value: int): ...

    @property
    def PointColor(self) -> tuple[float, float, float, float]:
        """Property TypeId: App::PropertyColor."""

    @PointColor.setter
    def PointColor(self, value: Triple_t[float] | Quadruple_t[float] | int): ...

    @property
    def PointSize(self) -> float:
        """Property TypeId: App::PropertyFloatConstraint."""

    @PointSize.setter
    def PointSize(self, value: float | Quadruple_t[float]): ...

    @property
    def ShowInner(self) -> bool:
        """Property TypeId: App::PropertyBool."""

    @ShowInner.setter
    def ShowInner(self, value: int | bool): ...

    def applyDisplacement(self, factor: float, /): ...

    def resetHighlightedNodes(self):
        """Reset highlighted nodes."""

    def resetNodeColor(self):
        """Reset color set by method setNodeColorByScalars."""

    def resetNodeDisplacement(self):
        """Reset displacements set by method setNodeDisplacementByVectors."""

    def setNodeColorByScalars(self, arg1: list, arg2: list, /):
        """
        Sets mesh node colors using element list and value list.
        Possible exceptions: (ValueError, TypeError).
        """

    def setNodeDisplacementByVectors(self, arg1: list, arg2: list, /):
        """Possible exceptions: (ValueError, TypeError)."""


# AppFemGuiPy.cpp
def setActiveAnalysis(object: FreeCAD.DocumentObject = None, /) -> None:
    """
    setActiveAnalysis(AnalysisObject) -- Set the Analysis object in work.
    Possible exceptions: (FreeCAD.Base.FreeCADError).
    """


def getActiveAnalysis() -> typing.Any | None:
    """
    getActiveAnalysis() -- Returns the Analysis object in work.
    Possible exceptions: (Exception).
    """


def open(Name: str, DocName: str = None, /) -> None:
    """
    open(string) -- Opens an Abaqus file in a text editor.
    Possible exceptions: (Exception).
    """


def insert(Name: str, DocName: str = None, /) -> None:
    """
    insert(string,string) -- Opens an Abaqus file in a text editor.
    Possible exceptions: (Exception).
    """
