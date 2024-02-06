import typing

import Part as PartModule


# AppPartPy.cpp
def sameParameter(shape: PartModule.Shape, enforce: bool, prec: float = 0.0, /) -> bool:
    """
    sameParameter(shape, enforce, prec=0.0)
    Possible exceptions: (Exception).
    """


def encodeRegularity(shape: PartModule.Shape, tolang: float = 1e-10, /) -> None:
    """
    encodeRegularity(shape, tolerance = 1e-10)

    Possible exceptions: (Exception).
    """


@typing.overload
def removeSmallEdges(shape, tolerance, ReShapeContext, /): ...


@typing.overload
def removeSmallEdges(shape: PartModule.Shape, tol: float, /) -> PartModule.Shape:
    """
    removeSmallEdges(shape, tolerance, ReShapeContext)
    Removes edges which are less than given tolerance from shape
    Possible exceptions: (Exception).
    """


@typing.overload
def fixVertexPosition(shape, tolerance, ReShapeContext, /): ...


@typing.overload
def fixVertexPosition(shape: PartModule.Shape, tol: float, /) -> bool:
    """
    fixVertexPosition(shape, tolerance, ReShapeContext)
    Fix position of the vertices having tolerance more tnan specified one
    Possible exceptions: (Exception).
    """


def leastEdgeSize(shape: PartModule.Shape, /) -> float:
    """
    leastEdgeSize(shape)
    Calculate size of least edge
    Possible exceptions: (Exception).
    """
