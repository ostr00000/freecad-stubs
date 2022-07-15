import TechDraw


# AppTechDrawGuiPy.cpp
def export(arg1, arg2: str, /) -> None:
    """
    TechDraw hook for FC Gui exporter.
    Possible exceptions: (Exception, TypeError).
    """


def exportPageAsPdf(DrawPageObject, FilePath: str, /) -> None:
    """
    exportPageAsPdf(DrawPageObject,FilePath) -- print page as Pdf to file.
    Possible exceptions: (TypeError, Exception).
    """


def exportPageAsSvg(DrawPageObject, FilePath: str, /) -> None:
    """
    exportPageAsSvg(DrawPageObject,FilePath) -- print page as Svg to file.
    Possible exceptions: (TypeError, Exception).
    """


def copyActiveViewToSvgFile(arg1, arg2: str, arg3: float = None, arg4: float = None, arg5=None, arg6=None, arg7: float = None, arg8: float = None, arg9: int = None, /) -> float:
    """
    copyActiveViewToSvgFile(DrawPageObject,FilePath) -- copy ActiveView to Svg file.
    Possible exceptions: (TypeError, Exception).
    """


def addQGIToView(View: TechDraw.DrawView, QGraphicsItem, /) -> None:
    """
    addQGIToView(View, QGraphicsItem) -- insert graphics item into view's graphic.
    Possible exceptions: (TypeError, RuntimeError, Exception).
    """


def addQGObjToView(View: TechDraw.DrawView, QGraphicsObject, /) -> None:
    """
    addQGObjToView(View, QGraphicsObject) -- insert graphics object into view's graphic. Use for QGraphicsItems that have QGraphicsObject as base class.
    Possible exceptions: (TypeError, RuntimeError, Exception).
    """
