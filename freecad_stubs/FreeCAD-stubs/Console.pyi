# Console.cpp
def PrintMessage(output, /) -> None:
    """PrintMessage(string) -- Print a message to the output"""


def PrintLog(output, /) -> None:
    """PrintLog(string) -- Print a log message to the output"""


def PrintError(output, /) -> None:
    """PrintError(string) -- Print an error message to the output"""


def PrintWarning(output, /) -> None:
    """PrintWarning -- Print a warning to the output"""


def SetStatus(pstr1: str, pstr2: str, Bool: int, /) -> None:
    """Set the status for either Log, Msg, Wrn or Error for an observer"""


def GetStatus(pstr1: str, pstr2: str, /) -> int | None:
    """Get the status for either Log, Msg, Wrn or Error for an observer"""
