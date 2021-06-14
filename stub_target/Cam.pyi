import Mesh
import Part


# AppCamPy.cpp
def open(arg1: str, /):
    """open(string) -- Not implemented for this Module so far."""


def insert(arg1: str, arg2: str, /):
    """insert(string, string) -- Not implemented for this Module so far."""


def read(arg1: str, /):
    """1"""


def createTestBSPLINE():
    """Creates a TopoShape with a test BSPLINE"""


def createTestApproximate():
    """1"""


def offset(arg1: Part.TopoShape, arg2: float, /):
    """1"""


def tesselateShape(arg1: Part.TopoShape, arg2: float, /):
    """1"""


def tess_shape(arg1: Part.TopoShape, arg2: float, /):
    """1"""


def createPlane(arg1: float, /):
    """1"""


def best_fit_test(arg1: Part.TopoShape, /):
    """1"""


def best_fit_complete(arg1: Mesh.MeshObject, arg2: Part.TopoShape, /):
    """1"""


def best_fit_coarse(arg1: Part.TopoShape, /):
    """1"""


def createBox(arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, /):
    """1"""


def spring_back(arg1: Mesh.MeshObject, arg2: Part.TopoShape, /):
    """1"""


def useMesh(arg1: Mesh.MeshObject, /):
    """useMesh(MeshObject) -- Shows the usage of Mesh objects from the Mesh Module."""


def openDYNA(arg1: str, /):
    """Open up a DYNA file, triangulate it, and returns a mesh"""
