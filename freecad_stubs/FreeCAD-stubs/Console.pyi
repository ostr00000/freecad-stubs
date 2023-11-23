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


def PrintDeveloperError(obj, /):
    """
    PrintDeveloperError(obj) -> None

    Print an error message intended only for Developers to the output.

    obj : object
        The string representation is printed.
    """


def PrintUserError(obj, /):
    """
    PrintUserError(obj) -> None

    Print an error message intended only for the User to the output.

    obj : object
        The string representation is printed.
    """


def PrintTranslatedUserError(obj, /):
    """
    PrintTranslatedUserError(obj) -> None

    Print an already translated error message intended only for the User to the output.

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


def PrintDeveloperWarning(obj, /):
    """
    PrintDeveloperWarning(obj) -> None

    Print an warning message intended only for Developers to the output.

    obj : object
        The string representation is printed.
    """


def PrintUserWarning(obj, /):
    """
    PrintUserWarning(obj) -> None

    Print a warning message intended only for the User to the output.

    obj : object
        The string representation is printed.
    """


def PrintTranslatedUserWarning(obj, /):
    """
    PrintTranslatedUserWarning(obj) -> None

    Print an already translated warning message intended only for the User to the output.

    obj : object
        The string representation is printed.
    """


def PrintCritical(obj, /):
    """
    PrintCritical(obj) -> None

    Print a critical message to the output.

    obj : object
        The string representation is printed.
    """


def PrintNotification(obj, /):
    """
    PrintNotification(obj) -> None

    Print a user notification to the output.

    obj : object
        The string representation is printed.
    """


def PrintTranslatedNotification(obj, /):
    """
    PrintTranslatedNotification(obj) -> None

    Print an already translated notification to the output.

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
