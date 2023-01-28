import typing

import WebGui


# AppWebGui.cpp
def openBrowser(url: str, /) -> None:
    """Possible exceptions: (Exception)."""


def openBrowserHTML(HtmlCode: str, BaseUrl: str, TabName: str = None, IconPath: str = None, /) -> None:
    """Possible exceptions: (Exception)."""


def openBrowserWindow(TabName: str = None, /) -> WebGui.BrowserView:
    """Possible exceptions: (Exception)."""


@typing.overload
def open(htmlcode, baseurl, title, iconpath, /): ...


@typing.overload
def open(url: str, /) -> None:
    """
    open(htmlcode,baseurl,[title,iconpath])
    Load a local (X)HTML file.
    Possible exceptions: (Exception).
    """


def insert(url: str, /) -> None:
    """
    insert(string)
    Load a local (X)HTML file.
    Possible exceptions: (Exception).
    """
