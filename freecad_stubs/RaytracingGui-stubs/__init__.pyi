# AppRaytracingGuiPy.cpp
def open(Name: str, DocName: str = None, /) -> None:
    """
    open(string) -- Create a new text document and load the file into the document.
    Possible exceptions: (Exception, RuntimeError).
    """


def insert(Name: str, DocName: str = None, /) -> None:
    """
    insert(string,string) -- Create a new text document and load the file into the document.
    Possible exceptions: (Exception, RuntimeError).
    """


def povViewCamera() -> str:
    """
    string povViewCamera() -- returns the povray camera definition of the active 3D view.
    Possible exceptions: (Exception, RuntimeError).
    """


def luxViewCamera() -> str:
    """
    string luxViewCamera() -- returns the luxrender camera definition of the active 3D view.
    Possible exceptions: (Exception, RuntimeError).
    """
