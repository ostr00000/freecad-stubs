import typing

import Assembly
import FreeCAD


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
    def First(self) -> FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None:
        """Property TypeId: App::PropertyLinkSub."""

    @First.setter
    def First(self, value: FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None): ...

    @property
    def Orientation(self) -> typing.Literal['Parallel', 'Equal', 'Opposite', 'Perpendicular']:
        """Property TypeId: App::PropertyEnumeration."""

    @Orientation.setter
    def Orientation(self, value: typing.Literal['Parallel', 'Equal', 'Opposite', 'Perpendicular']): ...

    @property
    def Second(self) -> FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None:
        """Property TypeId: App::PropertyLinkSub."""

    @Second.setter
    def Second(self, value: FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]] | list[FreeCAD.DocumentObject | str | typing.Sequence[str]] | None): ...

    @property
    def SolutionSpace(self) -> typing.Literal['Bidirectional', 'PositivDirectional', 'NegativeDirectional']:
        """Property TypeId: App::PropertyEnumeration."""

    @SolutionSpace.setter
    def SolutionSpace(self, value: typing.Literal['Bidirectional', 'PositivDirectional', 'NegativeDirectional']): ...

    @property
    def Type(self) -> typing.Literal['Fix', 'Distance', 'Orientation', 'Angle', 'Align', 'Coincident', 'None']:
        """Property TypeId: App::PropertyEnumeration."""

    @Type.setter
    def Type(self, value: typing.Literal['Fix', 'Distance', 'Orientation', 'Angle', 'Align', 'Coincident', 'None']): ...

    @property
    def Value(self) -> float | int:
        """Property TypeId: App::PropertyFloat."""

    @Value.setter
    def Value(self, value: float | int): ...


# ConstraintGroupPy.xml
class ConstraintGroup(FreeCAD.DocumentObject):
    """Base class of all objects in Assembly"""

    @property
    def Constraints(self) -> dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]:
        """Property TypeId: App::PropertyLinkList."""

    @Constraints.setter
    def Constraints(self, value: dict[int, FreeCAD.DocumentObject | None] | typing.Iterable[FreeCAD.DocumentObject | None] | typing.Sequence[FreeCAD.DocumentObject | None]): ...


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
