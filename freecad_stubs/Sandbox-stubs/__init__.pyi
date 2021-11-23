import FreeCAD
import Sandbox


# AppSandbox.cpp
def DocumentProtector(Document: FreeCAD.Document, /) -> Sandbox.DocumentProtector:
    """DocumentProtector(Document)"""


def DocumentObjectProtector(DocumentObject: FreeCAD.DocumentObject, /) -> Sandbox.DocumentObjectProtector:
    """DocumentObjectProtector(DocumentObject)"""


# DocumentProtectorPy.cpp
class DocumentProtectorPy:
    """Python binding class for the document protector class"""

    def addObject(self, type: str, name: str = None, /):
        """addObject(type,name)"""

    def recompute(self) -> None:
        """recompute()"""


class DocumentObjectProtectorPy:
    """Python binding class for the document object protector class"""

    def purgeTouched(self):
        """purgeTouched()"""
