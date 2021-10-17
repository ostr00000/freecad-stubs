import typing

import Assembly
import FreeCAD

DocAndStr_t: typing.TypeAlias = tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]
LinkSub_t: typing.TypeAlias = FreeCAD.DocumentObject | None | tuple[()] | DocAndStr_t
LinkList_t: typing.TypeAlias = None | FreeCAD.DocumentObject


# PartRefPy.xml
class PartRef(Assembly.Item):
    """Base class of all objects in Assembly"""

    @property
    def Annotation(self): ...

    @Annotation.setter
    def Annotation(self, value): ...

    @property
    def Model(self): ...

    @Model.setter
    def Model(self, value): ...


# ConstraintPy.xml
class Constraint(FreeCAD.DocumentObject):
    """Base class of all objects in Assembly"""

    @property
    def First(self) -> tuple[FreeCAD.DocumentObject, list[str]] | None:
        """Property TypeId: App::PropertyLinkSub."""

    @First.setter
    def First(self, value: LinkSub_t): ...

    @property
    def Orientation(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @Orientation.setter
    def Orientation(self, value: typing.Literal['Parallel', 'Equal', 'Opposite', 'Perpendicular']): ...

    @property
    def Second(self) -> tuple[FreeCAD.DocumentObject, list[str]] | None:
        """Property TypeId: App::PropertyLinkSub."""

    @Second.setter
    def Second(self, value: LinkSub_t): ...

    @property
    def SolutionSpace(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @SolutionSpace.setter
    def SolutionSpace(self, value: typing.Literal['Bidirectional', 'PositivDirectional', 'NegativeDirectional']): ...

    @property
    def Type(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @Type.setter
    def Type(self, value: typing.Literal['Fix', 'Distance', 'Orientation', 'Angle', 'Align', 'Coincident', 'None']): ...

    @property
    def Value(self) -> float:
        """Property TypeId: App::PropertyFloat."""

    @Value.setter
    def Value(self, value: float): ...


# ConstraintGroupPy.xml
class ConstraintGroup(FreeCAD.DocumentObject):
    """Base class of all objects in Assembly"""

    @property
    def Constraints(self) -> list[FreeCAD.DocumentObject | None]:
        """Property TypeId: App::PropertyLinkList."""

    @Constraints.setter
    def Constraints(self, value: LinkList_t): ...


# ProductRefPy.xml
class ProductRef(Assembly.Item):
    """Base class of all objects in Assembly"""

    @property
    def Item(self) -> FreeCAD.DocumentObject | None:
        """Property TypeId: App::PropertyLink."""

    @Item.setter
    def Item(self, value: FreeCAD.DocumentObject | None): ...


# ItemPy.xml
class Item(FreeCAD.DocumentObject):
    """Base class of all objects in Assembly"""

    @property
    def Meta(self) -> dict[str, str]:
        """
        Property TypeId: App::PropertyMap.
        Map with additional meta information.
        """

    @Meta.setter
    def Meta(self, value: dict[str, str]): ...


# AppAssemblyGuiPy.cpp
def setActiveAssembly(AssemblyObject: Assembly.Item = None, /):
    """setActiveAssembly(AssemblyObject) -- Set the Assembly object in work."""


def getActiveAssembly():
    """getActiveAssembly() -- Returns the Assembly object in work."""


def clearActiveAssembly():
    """clearActiveAssembly() -- Removes the current active Assembly as object in work"""
