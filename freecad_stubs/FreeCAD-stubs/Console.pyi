# Console.cpp
def PrintMessage(obj, /):
    """
    PrintMessage(obj) -> None

    Print a message to the output.

    obj : object
        The string representation is printed.
    """


def PrintLog(obj, /):
    """
    PrintLog(obj) -> None

    Print a log message to the output.

    obj : object
        The string representation is printed.
    """


def PrintError(obj, /):
    """
    PrintError(obj) -> None

    Print an error message to the output.

    obj : object
        The string representation is printed.
    """


def PrintWarning(obj, /):
    """
    PrintWarning(obj) -> None

    Print a warning message to the output.

    obj : object
        The string representation is printed.
    """


def SetStatus(pstr1: str, pstr2: str, pyStatus: bool, /):
    """
    SetStatus(observer, type, status) -> None

    Set the status for either 'Log', 'Msg', 'Wrn' or 'Error' for an observer.

    observer : str
        Logging interface name.
    type : str
        Message type.
    status : bool
    """


def GetStatus(pstr1: str, pstr2: str, /) -> bool:
    """
    GetStatus(observer, type) -> bool or None

    Get the status for either 'Log', 'Msg', 'Wrn' or 'Error' for an observer.
    Returns None if the specified observer doesn't exist.

    observer : str
        Logging interface name.
    type : str
        Message type.
    """


def GetObservers() -> list[str]:
    """
    GetObservers() -> list of str

    Get the names of the current logging interfaces.
    """
