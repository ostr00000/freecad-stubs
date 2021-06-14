import FreeCAD


# StepShapePy.xml
class StepShape(FreeCAD.PyObjectBase):
    """StepShape in Import
    This class gives a interface to retrieve TopoShapes out of an loaded STEP file of any kind. 
    		"""

    def __init__(self, arg1: str, /):
        """StepShape in Import
        This class gives a interface to retrieve TopoShapes out of an loaded STEP file of any kind. 
        		"""

    def read(self, arg):
        """method read()
        Read a STEP file into memory and make it accessible
        			  """


# AppImportPy.cpp
def open(arg1: str, arg2: str = None, /):
    """open(string) -- Open the file and create a new document."""


def insert(arg1: str, arg2: str = None, /):
    """insert(string,string) -- Insert the file into the given document."""


def export(arg1: object, arg2: str, /):
    """export(list,string) -- Export a list of objects into a single file."""


# AppImportGuiPy.cpp
def insert(arg1: str, arg2: str = None, /):
    """insert(string,string) -- Insert the file into the given document."""


def export(arg1: object, arg2: str, /):
    """export(list,string) -- Export a list of objects into a single file."""


def ocaf(arg1: str, /):
    """ocaf(string) -- Browse the ocaf structure."""
