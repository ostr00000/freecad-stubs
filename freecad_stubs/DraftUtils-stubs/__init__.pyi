# AppDraftUtilsPy.cpp
def readDXF(Name: str, DocName: str = None, IgnoreErrors: int = True, /) -> None:
    """
    readDXF(filename,[document,ignore_errors]): Imports a DXF file into the given document. ignore_errors is True by default.
    Possible exceptions: (Exception, RuntimeError).
    """
