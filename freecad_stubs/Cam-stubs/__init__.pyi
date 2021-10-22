import Mesh as MeshModule
import Part


# AppCamPy.cpp
def open(string: str, /):
    """open(string) -- Not implemented for this Module so far."""


def insert(string: str, string1: str, /):
    """insert(string, string) -- Not implemented for this Module so far."""


def read(arg0: str, /):
    """1"""


def createTestBSPLINE() -> Part.Shape:
    """Creates a TopoShape with a test BSPLINE"""


def createTestApproximate() -> Part.Shape:
    """1"""


def offset(arg0: Part.Shape, arg1: float, /) -> Part.Shape:
    """1"""


def tesselateShape(arg0: Part.Shape, arg1: float, /):
    """1"""


def tess_shape(arg0: Part.Shape, arg1: float, /) -> MeshModule.Mesh:
    """1"""


def createPlane(arg0: float, /) -> Part.Shape:
    """1"""


def best_fit_test(arg0: Part.Shape, /) -> MeshModule.Mesh:
    """1"""


def best_fit_complete(arg0: MeshModule.Mesh, arg1: Part.Shape, /):
    """1"""


def best_fit_coarse(arg0: Part.Shape, /):
    """1"""


def createBox(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, /) -> Part.Shape:
    """1"""


def spring_back(arg0: MeshModule.Mesh, arg1: Part.Shape, /) -> MeshModule.Mesh:
    """1"""


def useMesh(MeshObject: MeshModule.Mesh, /):
    """useMesh(MeshObject) -- Shows the usage of Mesh objects from the Mesh Module."""


def openDYNA(arg0: str, /):
    """Open up a DYNA file, triangulate it, and returns a mesh"""
