import sys
import typing

import FreeCAD
import Path.Voronoi


# VoronoiEdgePy.xml
class Edge(FreeCAD.BaseClass):
    """Edge of a Voronoi diagram"""

    def __init__(self):
        """
        Edge of a Voronoi diagram
        Possible exceptions: (RuntimeError).
        """

    @property
    def Cell(self) -> Path.Voronoi.Cell:
        """cell the edge belongs to"""

    @property
    def Color(self) -> int:
        """Assigned color of the receiver."""

    @Color.setter
    def Color(self, value: int): ...

    @property
    def Index(self) -> int:
        """Internal id of the element."""

    @property
    def Next(self) -> Path.Voronoi.Edge:
        """CCW next edge within voronoi cell"""

    @property
    def Prev(self) -> Path.Voronoi.Edge:
        """CCW previous edge within voronoi cell"""

    @property
    def RotNext(self) -> Path.Voronoi.Edge:
        """Rotated CCW next edge within voronoi cell"""

    @property
    def RotPrev(self) -> Path.Voronoi.Edge:
        """Rotated CCW previous edge within voronoi cell"""

    @property
    def Twin(self) -> Path.Voronoi.Edge:
        """Twin edge"""

    @property
    def Vertices(self) -> list[Path.Voronoi.Vertex | None]:
        """Begin and End voronoi vertex"""

    def getDistances(self) -> list:
        """Returns the distance of the vertices to the input source"""

    def getSegmentAngle(self) -> float | None:
        """Returns the angle (in degree) of the segments if the edge was formed by two segments"""

    def isBorderline(self) -> bool:
        """Returns true if the point is on the segment"""

    def isCurved(self) -> bool:
        """Returns true if edge is curved"""

    def isFinite(self) -> bool:
        """Returns true if both vertices are finite"""

    def isInfinite(self) -> bool:
        """Returns true if the end vertex is infinite"""

    def isLinear(self) -> bool:
        """Returns true if edge is straight"""

    def isPrimary(self) -> bool:
        """Returns false if edge goes through endpoint of the segment site"""

    def isSecondary(self) -> bool:
        """Returns true if edge goes through endpoint of the segment site"""

    def toShape(self, z0: float = 0.0, z1: float = sys.float_info.max, dbg: bool = 0, /) -> typing.Any | Path.Voronoi.Edge | None:
        """
        Returns a shape for the edge
        Possible exceptions: (RuntimeError).
        """

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...


# VoronoiCellPy.xml
class Cell(FreeCAD.BaseClass):
    """Cell of a Voronoi diagram"""

    def __init__(self):
        """
        Cell of a Voronoi diagram
        Possible exceptions: (RuntimeError).
        """

    @property
    def Color(self) -> int:
        """Assigned color of the receiver."""

    @Color.setter
    def Color(self, value: int): ...

    @property
    def IncidentEdge(self) -> Path.Voronoi.Edge:
        """Incident edge of the cell - if exists"""

    @property
    def Index(self) -> int:
        """Internal id of the element."""

    @property
    def SourceCategory(self) -> int:
        """Returns the cell's category as an integer"""

    @property
    def SourceCategoryName(self) -> str:
        """Returns the cell's category as a string"""

    @property
    def SourceIndex(self) -> int:
        """Returns the index of the cell's source"""

    def containsPoint(self) -> bool:
        """Returns true if the cell contains a point site"""

    def containsSegment(self) -> bool:
        """Returns true if the cell contains a segment site"""

    def getSource(self, z: float = 0, /) -> FreeCAD.Vector | list[FreeCAD.Vector]:
        """
        Returns the Source for the cell
        Possible exceptions: (TypeError).
        """

    def isDegenerate(self) -> bool:
        """Returns true if the cell doesn't have an incident edge"""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...


# VoronoiPy.xml
class Diagram(FreeCAD.BaseClass):
    """Voronoi([segments]): Create voronoi for given collection of line segments"""

    def __init__(self, scale: float = None, /):
        """
        Voronoi([segments]): Create voronoi for given collection of line segments
        Possible exceptions: (RuntimeError).
        """

    @property
    def Cells(self) -> list[Path.Voronoi.Cell]:
        """List of all cells of the voronoi diagram"""

    @property
    def Edges(self) -> list[Path.Voronoi.Edge]:
        """List of all edges of the voronoi diagram"""

    @property
    def Vertices(self) -> list[Path.Voronoi.Vertex]:
        """List of all vertices of the voronoi diagram"""

    def addPoint(self, obj, /) -> None:
        """addPoint(vector|vector2d) add given point to input collection"""

    def addSegment(self, objBegin, objEnd, /) -> None:
        """addSegment(vector|vector2d, vector|vector2d) add given segment to input collection"""

    def colorColinear(self, color: int, degree: float = 10.0, /) -> None:
        """
        assign given color to all edges sourced by two segments almost in line with each other (optional angle in degrees)
        Possible exceptions: (RuntimeError).
        """

    def colorExterior(self, color: int, callback=None, /) -> None:
        """
        assign given color to all exterior edges and vertices
        Possible exceptions: (RuntimeError).
        """

    def colorTwins(self, color: int, /) -> None:
        """
        assign given color to all twins of edges (which one is considered a twin is arbitrary)
        Possible exceptions: (RuntimeError).
        """

    def construct(self) -> None:
        """
        constructs the voronoi diagram from the input collections
        Possible exceptions: (RuntimeError).
        """

    def getPoints(self, z: float = 0, /) -> list[FreeCAD.Vector]:
        """
        Get list of all input points.
        Possible exceptions: (RuntimeError).
        """

    def getSegments(self, z: float = 0, /) -> list[tuple[FreeCAD.Vector, FreeCAD.Vector]]:
        """
        Get list of all input segments.
        Possible exceptions: (RuntimeError).
        """

    def numCells(self) -> int:
        """
        Return number of cells
        Possible exceptions: (RuntimeError).
        """

    def numEdges(self) -> int:
        """
        Return number of edges
        Possible exceptions: (RuntimeError).
        """

    def numPoints(self) -> int:
        """
        Return number of input points
        Possible exceptions: (RuntimeError).
        """

    def numSegments(self) -> int:
        """
        Return number of input segments
        Possible exceptions: (RuntimeError).
        """

    def numVertices(self) -> int:
        """
        Return number of vertices
        Possible exceptions: (RuntimeError).
        """

    def resetColor(self, color: int, /) -> None:
        """
        assign color 0 to all elements with the given color
        Possible exceptions: (RuntimeError).
        """


# VoronoiVertexPy.xml
class Vertex(FreeCAD.BaseClass):
    """Vertex of a Voronoi diagram"""

    def __init__(self):
        """
        Vertex of a Voronoi diagram
        Possible exceptions: (RuntimeError).
        """

    @property
    def Color(self) -> int:
        """Assigned color of the receiver."""

    @Color.setter
    def Color(self, value: int): ...

    @property
    def IncidentEdge(self) -> Path.Voronoi.Edge:
        """Y position"""

    @property
    def Index(self) -> int:
        """Internal id of the element."""

    @property
    def X(self) -> float:
        """X position"""

    @property
    def Y(self) -> float:
        """Y position"""

    def toPoint(self, z: float = 0.0, /) -> FreeCAD.Vector | None:
        """
        Returns a Vector - or None if not possible
        Possible exceptions: (RuntimeError).
        """

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...
