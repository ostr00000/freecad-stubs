import typing

import FreeCAD


# AppPartDesignPy.cpp
@typing.overload
def makeFilletArc(*args): ...


@typing.overload
def makeFilletArc(arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, arg3: FreeCAD.Vector, arg4: FreeCAD.Vector, arg5: float, arg6: int, /) -> tuple[FreeCAD.Vector, FreeCAD.Vector, FreeCAD.Vector]:
    """
    makeFilletArc(...) -- Fillet arc.
    Possible exceptions: (Exception, RuntimeError).
    """
