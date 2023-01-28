import FreeCAD
import Points as PointsModule


# PointsPy.xml
class Points(FreeCAD.ComplexGeoData):
    """
    This class can be imported.
    Points() -- Create an empty points object.

    This class allows one to manipulate the Points object by adding new points, deleting facets, importing from an STL file,
    transforming and much more.
    """

    def __init__(self, pcObj=None, /):
        """
        Points() -- Create an empty points object.

        This class allows one to manipulate the Points object by adding new points, deleting facets, importing from an STL file,
        transforming and much more.

      
        Possible exceptions: (TypeError).
        """

    @property
    def CountPoints(self) -> int:
        """Return the number of vertices of the points object."""

    @property
    def Points(self) -> list[FreeCAD.Vector]:
        """
        A collection of points
        With this attribute it is possible to get access to the points of the object

        for p in pnt.Points:
        	print p
        """

    def addPoints(self, obj, /):
        """
        add one or more (list of) points to the object
        Possible exceptions: (TypeError).
        """

    def copy(self) -> PointsModule.Points:
        """Create a copy of this points object"""

    def fromSegment(self, obj, /) -> PointsModule.Points:
        """
        Get a new point object from a given segment
        Possible exceptions: (TypeError).
        """

    def fromValid(self) -> PointsModule.Points:
        """
        Get a new point object from points with valid coordinates (i.e. that are not NaN)
        Possible exceptions: (TypeError).
        """

    def read(self, Name: str, /):
        """Read in a points object from file."""

    def write(self, Name: str, /):
        """Write the points object into file."""

    def writeInventor(self) -> str:
        """Write the points in OpenInventor format to a string."""


# AppPointsPy.cpp
def open(Name: str, /) -> None:
    """Possible exceptions: (Exception, RuntimeError)."""


def insert(Name: str, DocName: str, /) -> None:
    """Possible exceptions: (Exception, RuntimeError)."""


def export(object, Name: str, /) -> None:
    """Possible exceptions: (Exception, RuntimeError)."""


def show(pcObj: PointsModule.Points, name: str = 'Points', /) -> None:
    """
    show(points,[string]) -- Add the points to the active document or create one if no document exists.
    Possible exceptions: (Exception, RuntimeError).
    """
