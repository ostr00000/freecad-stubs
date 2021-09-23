# AppWeb.cpp
def startServer(address: str = None, port: int = 0, /):
    """startServer(address=127.0.0.1,port=0) -- Start a server."""


def waitForConnection(address: str = None, port: int = 0, timeout: int = 0, /):
    """
    waitForConnection(address=127.0.0.1,port=0,timeout=0)
    Start a server, wait for connection and close server.
    Its use is disadvised in a the GUI version, since it will
    stop responding until the function returns.
    """


def registerServerFirewall(callable_string_: object, /):
    """registerServerFirewall(callable(string)) -- Register a firewall."""


# BrowserView.cpp
class BrowserView:
    """Python interface class to BrowserView"""

    def setHtml(self, arg1: str, arg2: str = None, /):
        """setHtml(str)"""
