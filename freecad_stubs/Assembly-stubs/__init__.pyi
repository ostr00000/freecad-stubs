import Assembly
import FreeCAD


# PartRefPy.xml
class PartRef(Assembly.Item):
    """Base class of all objects in Assembly"""


# ConstraintPy.xml
class Constraint(FreeCAD.DocumentObject):
    """Base class of all objects in Assembly"""


# ConstraintGroupPy.xml
class ConstraintGroup(FreeCAD.DocumentObject):
    """Base class of all objects in Assembly"""


# ProductRefPy.xml
class ProductRef(Assembly.Item):
    """Base class of all objects in Assembly"""


# ItemPy.xml
class Item(FreeCAD.DocumentObject):
    """Base class of all objects in Assembly"""


# AppAssemblyGuiPy.cpp
def setActiveAssembly(AssemblyObject: Assembly.Item = None, /):
    """setActiveAssembly(AssemblyObject) -- Set the Assembly object in work."""


def getActiveAssembly():
    """getActiveAssembly() -- Returns the Assembly object in work."""


def clearActiveAssembly():
    """clearActiveAssembly() -- Removes the current active Assembly as object in work"""
