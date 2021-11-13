import WebGui


# AppWebGui.cpp
def openBrowser(arg1: str, /) -> None: ...


def openBrowserHTML(arg1: str, arg2: str, arg3: str = None, arg4: str = None, /) -> None: ...


def openBrowserWindow(arg1: str = None, /) -> WebGui.BrowserView: ...


def open(arg1: str, /) -> None:
    """
    open(htmlcode,baseurl,[title,iconpath])
    Load a local (X)HTML file.
    """


def insert(string: str, /) -> None:
    """
    insert(string)
    Load a local (X)HTML file.
    """
