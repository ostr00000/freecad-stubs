import FreeCAD
import Part


# UnifySameDomainPy.xml
class UnifySameDomain(FreeCAD.PyObjectBase):
    """This tool tries to unify faces and edges of the shape which lie on the same geometry."""

    def __init__(self, Shape: Part.Shape, UnifyEdges: bool = None, UnifyFaces: bool = None, ConcatBSplines: bool = None):
        """This tool tries to unify faces and edges of the shape which lie on the same geometry."""

    def allowInternalEdges(self, arg1: bool, /):
        """
        Sets the flag defining whether it is allowed to create
        internal edges inside merged faces in the case of non-manifold
        topology. Without this flag merging through multi connected edge
        is forbidden. Default value is false.
        """

    def build(self):
        """Performs unification and builds the resulting shape"""

    def initialize(self, Shape: Part.Shape, UnifyEdges: bool = None, UnifyFaces: bool = None, ConcatBSplines: bool = None):
        """Initializes with a shape and necessary flags"""

    def keepShape(self, arg1: Part.Shape, /):
        """Sets the shape for avoid merging of the faces/edges."""

    def keepShapes(self, arg1: object, /):
        """Sets the map of shapes for avoid merging of the faces/edges."""

    def setAngularTolerance(self, arg1: float, /):
        """Sets the angular tolerance"""

    def setLinearTolerance(self, arg1: float, /):
        """Sets the linear tolerance"""

    def setSafeInputMode(self, arg1: bool, /):
        """
        Sets the flag defining the behavior of the algorithm regarding
        modification of input shape.
        If this flag is equal to True then the input (original) shape can't be
        modified during modification process. Default value is true.
        """

    def shape(self):
        """Gives the resulting shape"""
