import typing

import FreeCAD
import Part as PartModule
import Path as PathModule


# AppPathPy.cpp
def write(pObj, Name: str, /) -> None:
    """
    write(object,filename): Exports a given path object to a GCode file
    Possible exceptions: (Exception, RuntimeError).
    """


def read(Name: str, DocName: str = None, /) -> None:
    """
    read(filename,[document]): Imports a GCode file into the given document
    Possible exceptions: (Exception, RuntimeError).
    """


def show(pcObj: PathModule.Path, name: str = 'Path', /) -> None:
    """
    show(path,[string]): Add the path to the active document or create one if no document exists
    Possible exceptions: (Exception, ReferenceError, RuntimeError).
    """


def fromShape(pcObj, /) -> PathModule.Path:
    """
    fromShape(Shape): Returns a Path object from a Part Shape (deprecated - use fromShapes() instead)
    Possible exceptions: (Exception, TypeError, RuntimeError).
    """


def fromShapes(shapes, start: FreeCAD.Vector = None, return_end: bool = None) -> PathModule.Path | tuple[PathModule.Path, FreeCAD.Vector]:
    """
    fromShapes(shapes, start=Vector(), return_end=False" PARAM_PY_ARGS_DOC(ARG,AREA_PARAMS_PATH) ")

    Returns a Path object from a list of shapes

    * shapes: input list of shapes.

    * start (Vector()): feed start position, and also serves as a hint of path entry.

    * return_end (False): if True, returns tuple (path, endPosition).
    "
                  PARAM_PY_DOC(ARG, AREA_PARAMS_PATH)
    Possible exceptions: (Exception, TypeError).
    """


@typing.overload
def sortWires(shapes, /, start=None, arg2=None): ...


@typing.overload
def sortWires(shapes, start: FreeCAD.Vector = None) -> tuple[list[PartModule.Shape], FreeCAD.Vector, int]:
    """
    sortWires(shapes, start=Vector(), "
                  PARAM_PY_ARGS_DOC(ARG,AREA_PARAMS_ARC_PLANE)
                  PARAM_PY_ARGS_DOC(ARG,AREA_PARAMS_SORT) ")

    Returns (wires,end), where 'wires' is sorted across Z value and with optimized travel distance,
    and 'end' is the ending position of the whole wires. If arc_plane==1, it returns (wires,end,arc_plane),
    where arc_plane is the found plane if any, or unchanged.

    * shapes: input shape list

    * start (Vector()): optional start position.
    "
                  PARAM_PY_DOC(ARG, AREA_PARAMS_ARC_PLANE)
                  PARAM_PY_DOC(ARG, AREA_PARAMS_SORT)
    Possible exceptions: (Exception, TypeError).
    """
