import FreeCAD
import TechDraw


# MDIViewPagePy.xml
class MDIViewPage(FreeCAD.PyObjectBase):
    """MDIViewPage object"""

    def getPage(self) -> TechDraw.DrawPage:
        """returns the page being displayed"""


# AppTechDrawGuiPy.cpp
def export(arg1, arg2: str, /) -> None:
    """TechDraw hook for FC Gui exporter."""


def exportPageAsPdf(DrawPageObject, FilePath: str, /) -> None:
    """exportPageAsPdf(DrawPageObject,FilePath) -- print page as Pdf to file."""


def exportPageAsSvg(DrawPageObject, FilePath: str, /) -> None:
    """exportPageAsSvg(DrawPageObject,FilePath) -- print page as Svg to file."""


def copyActiveViewToSvgFile(arg1, arg2: str, arg3: float = None, arg4: float = None, arg5=None, arg6=None, arg7: float = None, arg8: float = None, arg9: int = None, /) -> float:
    """copyActiveViewToSvgFile(DrawPageObject,FilePath) -- copy ActiveView to Svg file."""


def addQGIToView(View, QGraphicsItem, /) -> None:
    """addQGIToView(View, QGraphicsItem) -- insert graphics item into view's graphic."""
