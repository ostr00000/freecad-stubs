import FreeCAD


# MDIViewPagePy.xml
class MDIViewPage(FreeCAD.PyObjectBase):
    """MDIViewPage object"""

    def getPage(self):
        """returns the page being displayed"""


# AppTechDrawGuiPy.cpp
def export(arg1: object, arg2: str, /):
    """TechDraw hook for FC Gui exporter."""


def exportPageAsPdf(DrawPageObject: object, FilePath: str, /):
    """exportPageAsPdf(DrawPageObject,FilePath) -- print page as Pdf to file."""


def exportPageAsSvg(DrawPageObject: object, FilePath: str, /):
    """exportPageAsSvg(DrawPageObject,FilePath) -- print page as Svg to file."""


def copyActiveViewToSvgFile(arg1: object, arg2: str, arg3: float = None, arg4: float = None, arg5: object = None, arg6: object = None, arg7: float = None, arg8: float = None, arg9: int = None, /):
    """copyActiveViewToSvgFile(DrawPageObject,FilePath) -- copy ActiveView to Svg file."""


def addQGIToView(View: object, QGraphicsItem: object, /):
    """addQGIToView(View, QGraphicsItem) -- insert graphics item into view's graphic."""
