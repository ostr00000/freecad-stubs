import FreeCAD
import Points


# PointsPy.xml
class Points(FreeCAD.ComplexGeoData):
    """
    This class can be imported.
    Points() -- Create an empty points object.

    This class allows one to manipulate the Points object by adding new points, deleting facets, importing from an STL file,
    transforming and much more.
    """

    def __init__(self, arg1: object = None, /):
        """
        Points() -- Create an empty points object.

        This class allows one to manipulate the Points object by adding new points, deleting facets, importing from an STL file,
        transforming and much more.
        """

    @property
    def CountPoints(self) -> int:
        """Return the number of vertices of the points object."""

    @property
    def Points(self) -> list:
        """
        A collection of points
        With this attribute it is possible to get access to the points of the object

        for p in pnt.Points:
        	print p
        """

    def addPoints(self, arg1: object, /):
        """add one or more (list of) points to the object"""

    def copy(self):
        """Create a copy of this points object"""

    def fromSegment(self, arg1: object, /):
        """Get a new point object from a given segment"""

    def fromValid(self):
        """Get a new point object from points with valid coordinates (i.e. that are not NaN)"""

    def read(self, arg1: str, /):
        """Read in a points object from file."""

    def write(self, arg1: str, /):
        """Write the points object into file."""

    def writeInventor(self):
        """Write the points in OpenInventor format to a string."""


# AppPointsPy.cpp
def open(arg1: str, /): ...


def insert(arg1: str, arg2: str, /): ...


def export(arg1: object, arg2: str, /): ...


def show(points: Points.Points, string: str = None, /):
    """show(points,[string]) -- Add the points to the active document or create one if no document exists."""
