# AppWeb.cpp
def startServer(address: str = None, port: int = 0, /):
    """startServer(address=127.0.0.1,port=0) -- Start a server."""


def waitForConnection(address: str = None, port: int = 0, timeout: int = 0, /):
    """waitForConnection(address=127.0.0.1,port=0,timeout=0)
    Start a server, wait for connection and close server.
    Its use is disadvised in a the GUI version, since it will
    stop responding until the function returns."""


def registerServerFirewall(callable_string_: object, /):
    """registerServerFirewall(callable(string)) -- Register a firewall."""


# AppWebGui.cpp
def openBrowser(arg1: str, /):
    """&Module::openBrowser"""


def openBrowserHTML(arg1: str, arg2: str, arg3: str = None, /):
    """&Module::openBrowserHTML"""


def openBrowserWindow(arg1: str = None, /):
    """&Module::openBrowserWindow"""


def open(string: str, /):
    """open(string)
    Load a local (X)HTML file."""


def insert(string: str, /):
    """insert(string)
    Load a local (X)HTML file."""


# BrowserView.cpp
def setHtml(arg1: str, arg2: str = None, /):
    """setHtml(str)"""
