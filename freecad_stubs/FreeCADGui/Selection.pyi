import typing

import FreeCAD


# Selection.cpp
@typing.overload
def addSelection(arg1: FreeCAD.DocumentObject, arg2: str = None, arg3: float = None, arg4: float = None, arg5: float = None, /): ...


@typing.overload
def addSelection(arg1: FreeCAD.DocumentObject, arg2: object, /):
    """addSelection(object,[string,float,float,float]) -- Add an object to the selection
    where string is the sub-element name and the three floats represent a 3d point"""


def removeSelection(arg1: FreeCAD.DocumentObject, arg2: str = None, /):
    """removeSelection(object) -- Remove an object from the selection"""


def clearSelection(arg1: str = None, /):
    """clearSelection([string]) -- Clear the selection
    Clear the selection to the given document name. If no document is
    given the complete selection is cleared."""


def isSelected(arg1: FreeCAD.DocumentObject, arg2: str = None, /):
    """isSelected(object) -- Check if a given object is selected"""


def getPreselection():
    """getPreselection() -- Get preselected object"""


def clearPreselection():
    """clearPreselection() -- Clear the preselection"""


def countObjectsOfType(arg1: str, arg2: str = None, /):
    """countObjectsOfType(string, [string]) -- Get the number of selected objects
    The first argument defines the object type e.g. \"Part::Feature\" and the
    second argumeht defines the document name. If no document name is given the
    currently active document is used"""


def getSelection(arg1: str = None, /):
    """getSelection([string]) -- Return a list of selected objects
    Return a list of selected objects for a given document name. If no
    document name is given the selection for the active document is returned."""


def getCompleteSelection():
    """getCompleteSelection() -- Return a list of selected objects of all documents."""


def getSelectionEx(arg1: str = None, /):
    """getSelectionEx([string]) -- Return a list of SelectionObjects
    Return a list of SelectionObjects for a given document name. If no
    document is given the selection of the active document is returned.
    The SelectionObjects contain a variety of information about the selection,
    e.g. sub-element names."""


def getSelectionObject(arg1: str, arg2: str, arg3: str, arg4: tuple = None, /):
    """getSelectionObject(doc,obj,sub,(x,y,z)) -- Return a SelectionObject"""


def addObserver(arg1: object, /):
    """addObserver(Object) -- Install an observer
    """


def removeObserver(arg1: object, /):
    """removeObserver(Object) -- Uninstall an observer
    """


@typing.overload
def addSelectionGate(arg1: str, /): ...


@typing.overload
def addSelectionGate(arg1: object, /): ...


@typing.overload
def addSelectionGate(arg1: object, /):
    """addSelectionGate(String|Filter|Gate) -- activate the selection gate.
    The selection gate will prohibit all selections which do not match
    the given selection filter string.
     Examples strings are:
    'SELECT Part::Feature SUBELEMENT Edge',
    'SELECT Robot::RobotObject'

    You can also set an instance of SelectionFilter:
    filter = Gui.Selection.Filter('SELECT Part::Feature SUBELEMENT Edge')
    Gui.Selection.addSelectionGate(filter)

    And the most flexible approach is to write your own selection gate class
    that implements the method 'allow'
    class Gate:
      def allow(self,doc,obj,sub):
        return (sub[0:4] == 'Face')
    Gui.Selection.addSelectionGate(Gate())"""


def removeSelectionGate():
    """removeSelectionGate() -- remove the active selection gate
    """
