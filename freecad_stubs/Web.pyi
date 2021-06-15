# AppWeb.cpp
def startServer(arg1: str = None, arg2: int = None, /):
    """startServer(address=127.0.0.1,port=0) -- Start a server."""


def waitForConnection(arg1: str = None, arg2: int = None, arg3: int = None, /):
    """waitForConnection(address=127.0.0.1,port=0,timeout=0)
    Start a server, wait for connection and close server.
    Its use is disadvised in a the GUI version, since it will
    stop responding until the function returns."""


def registerServerFirewall(arg1: object, /):
    """registerServerFirewall(callable(string)) -- Register a firewall."""


# AppWebGui.cpp
def openBrowser(arg1: str, /):
    """&Module::openBrowser"""


def openBrowserHTML(arg1: str, arg2: str, arg3: str = None, /):
    """&Module::openBrowserHTML"""


def openBrowserWindow(arg1: str = None, /):
    """&Module::openBrowserWindow"""


def open(arg1: str, /):
    """open(string)
    Load a local (X)HTML file."""


def insert(arg1: str, /):
    """insert(string)
    Load a local (X)HTML file."""


# BrowserView.cpp
def setHtml(arg1: str, arg2: str = None, /):
    """setHtml(str)"""
