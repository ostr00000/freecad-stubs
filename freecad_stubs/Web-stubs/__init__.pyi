# AppWeb.cpp
def startServer(addr: str = '127.0.0.1', port: int = 0, /) -> tuple[str, int]:
    """
    startServer(address=127.0.0.1,port=0) -- Start a server.
    Possible exceptions: (Exception, OverflowError, RuntimeError).
    """


def waitForConnection(addr: str = '127.0.0.1', port: int = 0, timeout: int = 0, /) -> bool:
    """
    waitForConnection(address=127.0.0.1,port=0,timeout=0)
    Start a server, wait for connection and close server.
    Its use is disadvised in a the GUI version, since it will
    stop responding until the function returns.
    Possible exceptions: (Exception, OverflowError, RuntimeError).
    """


def registerServerFirewall(obj, /) -> None:
    """
    registerServerFirewall(callable(string)) -- Register a firewall.
    Possible exceptions: (Exception).
    """


# BrowserView.cpp
class BrowserView:
    """Python interface class to BrowserView"""

    def setHtml(self, HtmlCode: str, BaseUrl: str = None, /) -> None:
        """
        setHtml(str)
        Possible exceptions: (Exception).
        """

    def load(self, BaseUrl: str, /) -> None:
        """
        load(url)
        Possible exceptions: (Exception).
        """

    def stop(self) -> None:
        """
        stop()
        Possible exceptions: (Exception).
        """

    def url(self) -> str:
        """
        url()
        Possible exceptions: (Exception).
        """

    def cast_to_base(self):
        """cast_to_base() cast to MDIView class"""
