import FreeCAD


# AppSandbox.cpp
def DocumentProtector(Document: FreeCAD.Document, /):
    """DocumentProtector(Document)"""


def DocumentObjectProtector(DocumentObject: FreeCAD.DocumentObject, /):
    """DocumentObjectProtector(DocumentObject)"""


# DocumentProtectorPy.cpp
class DocumentProtectorPy:
    """Python binding class for the document protector class"""

    @staticmethod
    def addObject(type: str, name: str = None, /):
        """addObject(type,name)"""

    @staticmethod
    def recompute():
        """recompute()"""


class DocumentObjectProtectorPy:
    """Python binding class for the document object protector class"""

    @staticmethod
    def purgeTouched():
        """purgeTouched()"""
