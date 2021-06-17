# Console.cpp
def PrintMessage(string: object, /):
    """PrintMessage(string) -- Print a message to the output"""


def PrintLog(string: object, /):
    """PrintLog(string) -- Print a log message to the output"""


def PrintError(string: object, /):
    """PrintError(string) -- Print an error message to the output"""


def PrintWarning(arg1: object, /):
    """PrintWarning -- Print a warning to the output"""


def SetStatus(arg1: str, arg2: str, arg3: int, /):
    """Set the status for either Log, Msg, Wrn or Error for an observer"""


def GetStatus(arg1: str, arg2: str, /):
    """Get the status for either Log, Msg, Wrn or Error for an observer"""
