# Console.cpp
def PrintMessage(arg1: object, /):
    """PrintMessage(string) -- Print a message to the output"""


def PrintLog(arg1: object, /):
    """PrintLog(string) -- Print a log message to the output"""


def PrintError(arg1: object, /):
    """PrintError(string) -- Print an error message to the output"""


def PrintWarning(arg1: object, /):
    """PrintWarning -- Print a warning to the output"""


def SetStatus(arg1: str, arg2: str, arg3: int, /):
    """Set the status for either Log, Msg, Wrn, or Error for an observer"""


def GetStatus(arg1: str, arg2: str, /):
    """Get the status for either Log, Msg, Wrn, or Error for an observer"""
