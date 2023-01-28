import typing

import FreeCAD


# AppPartDesignPy.cpp
@typing.overload
def makeFilletArc(*args): ...


@typing.overload
def makeFilletArc(pM1: FreeCAD.Vector, pP: FreeCAD.Vector, pQ: FreeCAD.Vector, pN: FreeCAD.Vector, r2: float, ccw: int, /) -> tuple[FreeCAD.Vector, FreeCAD.Vector, FreeCAD.Vector]:
    """
    makeFilletArc(...) -- Fillet arc.
    Possible exceptions: (Exception, RuntimeError).
    """
