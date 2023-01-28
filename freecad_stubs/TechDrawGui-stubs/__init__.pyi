import TechDraw


# AppTechDrawGuiPy.cpp
def export(object, Name: str, /) -> None:
    """
    TechDraw hook for FC Gui exporter.
    Possible exceptions: (Exception, TypeError).
    """


def exportPageAsPdf(pageObj, name: str, /) -> None:
    """
    exportPageAsPdf(DrawPageObject, FilePath) -- print page as Pdf to file.
    Possible exceptions: (TypeError, Exception).
    """


def exportPageAsSvg(pageObj, name: str, /) -> None:
    """
    exportPageAsSvg(DrawPageObject, FilePath) -- print page as Svg to file.
    Possible exceptions: (TypeError, Exception).
    """


def addQGIToView(viewPy: TechDraw.DrawView = None, qgiPy=None, /) -> None:
    """
    addQGIToView(View, QGraphicsItem) -- insert graphics item into view's graphic.
    Possible exceptions: (TypeError, RuntimeError, Exception).
    """


def addQGObjToView(viewPy: TechDraw.DrawView = None, qgiPy=None, /) -> None:
    """
    addQGObjToView(View, QGraphicsObject) -- insert graphics object into view's graphic. Use for QGraphicsItems that have QGraphicsObject as base class.
    Possible exceptions: (TypeError, RuntimeError, Exception).
    """
