import typing

import FreeCAD
import Part as PartModule
import Surface


# BlendCurvePy.xml
class BlendCurve(FreeCAD.PyObjectBase):
    """
    This class can be imported.

    				Create a BlendCurve that interpolate 2 BlendPoints.
    				curve = BlendCurve(BlendPoint1, BlendPoint2)
    """

    def __init__(self, b1: Surface.BlendPoint, b2: Surface.BlendPoint, /):
        """
        Create a BlendCurve that interpolate 2 BlendPoints.
        				curve = BlendCurve(BlendPoint1, BlendPoint2)
        """

    def compute(self) -> PartModule.BezierCurve:
        """Return the BezierCurve that interpolate the input BlendPoints."""

    def setSize(self, i: int, size: float, relative: bool, /):
        """
        Set the tangent size of the blendpoint at given index.
        					If relative is true, the size is considered relative to the distance between the two blendpoints.
        					myBlendCurve.setSize(idx, size, relative)
				
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """


# BlendPointPy.xml
class BlendPoint(FreeCAD.PyObjectBase):
    """
    This class can be imported.

    				Create BlendPoint from a point and some derivatives.
    				myBlendPoint = BlendPoint([Point, D1, D2, ..., DN])
    				BlendPoint can also be constructed from an edge
    				myBlendPoint = BlendPoint(Edge, parameter = float, continuity = int)
    """

    @typing.overload
    def __init__(self, plist, /): ...

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, pcObj: PartModule.Shape, param: float, cont: int, /):
        """
        Create BlendPoint from a point and some derivatives.
        				myBlendPoint = BlendPoint([Point, D1, D2, ..., DN])
        				BlendPoint can also be constructed from an edge
        				myBlendPoint = BlendPoint(Edge, parameter = float, continuity = int)
			
        Possible exceptions: (RuntimeError, TypeError).
        """

    @property
    def Vectors(self) -> list[FreeCAD.Vector]:
        """The list of vectors of this BlendPoint."""

    def getSize(self) -> float:
        """
        Return BlendPoint first derivative length.
				
        Possible exceptions: (RuntimeError).
        """

    def setSize(self, size: float, /):
        """
        Resizes the BlendPoint vectors,
        					by setting the length of the first derivative.
        					theBlendPoint.setSize(new_size)
				
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """

    @typing.overload
    def setvectors(self, Point, D1, D2, /, *args, DN=None): ...

    @typing.overload
    def setvectors(self, plist, /):
        """
        Set the vectors of BlendPoint.
        					BlendPoint.setvectors([Point, D1, D2, ..., DN])
				
        Possible exceptions: (TypeError).
        """
