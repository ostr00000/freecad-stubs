import typing

import FreeCAD


# Selection.cpp
def addSelection(object: FreeCAD.DocumentObject, string: str = None, float: float = None, float3: float = None, float4: float = None, /):
    """addSelection(object,[string,float,float,float]) -- Add an object to the selection
    where string is the sub-element name and the three floats represent a 3d point"""


def removeSelection(arg1: FreeCAD.DocumentObject, arg2: str = None, /):
    """removeSelection(object) -- Remove an object from the selection"""


def clearSelection(string: str = None, /):
    """clearSelection([string]) -- Clear the selection
    Clear the selection to the given document name. If no document is
    given the complete selection is cleared."""


def isSelected(arg1: FreeCAD.DocumentObject, arg2: str = None, /):
    """isSelected(object) -- Check if a given object is selected"""


def getPreselection():
    """getPreselection() -- Get preselected object"""


def clearPreselection():
    """clearPreselection() -- Clear the preselection"""


def countObjectsOfType(string: str, string1: str = None, /):
    """countObjectsOfType(string, [string]) -- Get the number of selected objects
    The first argument defines the object type e.g. "Part::Feature" and the
    second argumeht defines the document name. If no document name is given the
    currently active document is used"""


def getSelection(string: str = None, /):
    """getSelection([string]) -- Return a list of selected objects
    Return a list of selected objects for a given document name. If no
    document name is given the selection for the active document is returned."""


def getCompleteSelection():
    """getCompleteSelection() -- Return a list of selected objects of all documents."""


def getSelectionEx(string: str = None, /):
    """getSelectionEx([string]) -- Return a list of SelectionObjects
    Return a list of SelectionObjects for a given document name. If no
    document is given the selection of the active document is returned.
    The SelectionObjects contain a variety of information about the selection,
    e.g. sub-element names."""


def getSelectionObject(doc: str, obj: str, sub: str, arg: tuple = None, /):
    """getSelectionObject(doc,obj,sub,(x,y,z)) -- Return a SelectionObject"""


def addObserver(Object: object, /):
    """addObserver(Object) -- Install an observer
    """


def removeObserver(Object: object, /):
    """removeObserver(Object) -- Uninstall an observer
    """


@typing.overload
def addSelectionGate(String_Filter_Gate: str, /): ...


@typing.overload
def addSelectionGate(String_Filter_Gate: object, /): ...


@typing.overload
def addSelectionGate(filter: str, /): ...


@typing.overload
def addSelectionGate(filter: object, /): ...


@typing.overload
def addSelectionGate(Gate_: str, /): ...


@typing.overload
def addSelectionGate(Gate_: object, /):
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
