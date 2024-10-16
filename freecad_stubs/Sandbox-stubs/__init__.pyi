import FreeCAD
import Sandbox


# AppSandbox.cpp
def DocumentProtector(o: FreeCAD.Document, /) -> Sandbox.DocumentProtectorPy:
    """
    DocumentProtector(Document)
    Possible exceptions: (Exception).
    """


def DocumentObjectProtector(o: FreeCAD.DocumentObject, /) -> Sandbox.DocumentObjectProtectorPy:
    """
    DocumentObjectProtector(DocumentObject)
    Possible exceptions: (Exception).
    """


# DocumentProtectorPy.cpp
class DocumentProtectorPy:
    """Python binding class for the document protector class"""

    def addObject(self, type: str, name: str = 0, /) -> Sandbox.DocumentObjectProtectorPy:
        """
        addObject(type,name)
        Possible exceptions: (Exception, RuntimeError).
        """

    def recompute(self) -> None:
        """
        recompute()
        Possible exceptions: (Exception).
        """


class DocumentObjectProtectorPy:
    """Python binding class for the document object protector class"""

    def purgeTouched(self) -> None:
        """purgeTouched()"""
