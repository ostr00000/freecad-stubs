import typing

import FreeCAD
import Part


# MakePrismPy.xml
class MakePrism(FreeCAD.PyObjectBase):
    """Describes functions to build prism features."""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Sbase: Part.Shape, Pbase: Part.Shape, Skface: Part.Face, Direction: FreeCAD.Vector, Fuse: int, Modify: bool):
        """Describes functions to build prism features."""

    def add(self, Edge: Part.Edge, Face: Part.Face):
        """
        Indicates that the edge will slide on the face.
        Raises ConstructionError if the  face does not belong to the
        basis shape, or the edge to the prismed shape.
        """

    def barycCurve(self):
        """Generates a curve along the center of mass of the primitive."""

    def curves(self):
        """Returns the list of curves S parallel to the axis of the prism."""

    def init(self, Sbase: Part.Shape, Pbase: Part.Shape, Skface: Part.Face, Direction: FreeCAD.Vector, Fuse: int, Modify: bool):
        """
        Initializes this algorithm for building prisms along surfaces.
        A face Pbase is selected in the shape Sbase
        to serve as the basis for the prism. The orientation
        of the prism will be defined by the vector Direction.

        Fuse offers a choice between:
        -   removing matter with a Boolean cut using the setting 0
        -   adding matter with Boolean fusion using the setting 1.
        The sketch face Skface serves to determine
        the type of operation. If it is inside the basis
        shape, a local operation such as glueing can be performed.
        """

    @typing.overload
    def perform(self, From: Part.Shape, Until: Part.Shape): ...

    @typing.overload
    def perform(self, Until: Part.Shape): ...

    @typing.overload
    def perform(self, Length: float): ...

    def performFromEnd(self, arg1: Part.Shape, /):
        """Realizes a semi-infinite prism, limited by the face Funtil."""

    def performThruAll(self):
        """Builds an infinite prism. The infinite descendants will not be kept in the result."""

    def performUntilEnd(self):
        """
        Realizes a semi-infinite prism, limited by the
        position of the prism base. All other faces extend infinitely.
        """

    def performUntilHeight(self, arg1: Part.Shape, arg2: float, /):
        """
        Assigns both a limiting shape, Until from TopoDS_Shape
        and a height, Length at which to stop generation of the prism feature.
        """

    def shape(self):
        """Returns a shape built by the shape construction algorithm."""
