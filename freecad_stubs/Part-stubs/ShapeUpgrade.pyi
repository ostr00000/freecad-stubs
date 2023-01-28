import FreeCAD
import Part as PartModule


# UnifySameDomainPy.xml
class UnifySameDomain(FreeCAD.PyObjectBase):
    """This tool tries to unify faces and edges of the shape which lie on the same geometry."""

    def __init__(self, Shape: PartModule.Shape, UnifyEdges: bool = True, UnifyFaces: bool = True, ConcatBSplines: bool = False):
        """
        This tool tries to unify faces and edges of the shape which lie on the same geometry.
        Possible exceptions: (RuntimeError).
        """

    def allowInternalEdges(self, allow: bool, /):
        """
        Sets the flag defining whether it is allowed to create
        internal edges inside merged faces in the case of non-manifold
        topology. Without this flag merging through multi connected edge
        is forbidden. Default value is false.
        Possible exceptions: (RuntimeError).
        """

    def build(self):
        """
        Performs unification and builds the resulting shape
        Possible exceptions: (RuntimeError).
        """

    def initialize(self, Shape: PartModule.Shape, UnifyEdges: bool = True, UnifyFaces: bool = True, ConcatBSplines: bool = False):
        """
        Initializes with a shape and necessary flags
        Possible exceptions: (RuntimeError).
        """

    def keepShape(self, shape: PartModule.Shape, /):
        """
        Sets the shape for avoid merging of the faces/edges.
        Possible exceptions: (RuntimeError).
        """

    def keepShapes(self, obj, /):
        """
        Sets the map of shapes for avoid merging of the faces/edges.
        Possible exceptions: (RuntimeError).
        """

    def setAngularTolerance(self, angTol: float, /):
        """
        Sets the angular tolerance
        Possible exceptions: (RuntimeError).
        """

    def setLinearTolerance(self, linTol: float, /):
        """
        Sets the linear tolerance
        Possible exceptions: (RuntimeError).
        """

    def setSafeInputMode(self, mode: bool, /):
        """
        Sets the flag defining the behavior of the algorithm regarding
        modification of input shape.
        If this flag is equal to True then the input (original) shape can't be
        modified during modification process. Default value is true.
        Possible exceptions: (RuntimeError).
        """

    def shape(self) -> PartModule.Shape:
        """
        Gives the resulting shape
        Possible exceptions: (RuntimeError).
        """
