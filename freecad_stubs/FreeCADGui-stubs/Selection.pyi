import typing

import FreeCAD
import FreeCADGui


# Selection.cpp
@typing.overload
def addSelection(arg0: str, arg1: str, arg2: str = None, arg3: float = None, arg4: float = None, arg5: float = None, arg6: bool = None, /): ...


@typing.overload
def addSelection(arg0: FreeCAD.DocumentObject, arg1: str = None, arg2: float = None, arg3: float = None, arg4: float = None, arg5: bool = None, /): ...


@typing.overload
def addSelection(arg0: FreeCAD.DocumentObject, arg1, arg2: bool = None, /):
    """
    addSelection(object,[string,float,float,float]) -- Add an object to the selection
    where string is the sub-element name and the three floats represent a 3d point
    """


def updateSelection(show, object: FreeCAD.DocumentObject, string: str = None, /):
    """
    updateSelection(show,object,[string]) -- update an object in the selection
    where string is the sub-element name and the three floats represent a 3d point
    """


@typing.overload
def removeSelection(arg0: str, arg1: str, arg2: str = None, /): ...


@typing.overload
def removeSelection(arg0: FreeCAD.DocumentObject, arg1: str = None, /):
    """removeSelection(object) -- Remove an object from the selection"""


def clearSelection(docName: str = '', clearPreSelect: bool = True, /):
    """
    clearSelection(docName='',clearPreSelect=True) -- Clear the selection
    Clear the selection to the given document name. If no document is
    given the complete selection is cleared.
    """


def isSelected(arg0: FreeCAD.DocumentObject, arg1: str = None, arg2=None, /) -> bool:
    """isSelected(object,resolve=True) -- Check if a given object is selected"""


def setPreselection(obj: FreeCAD.DocumentObject, subname: str = None, x: float = None, y: float = None, z: float = None, tp: int = None):
    """setPreselection() -- Set preselected object"""


def getPreselection() -> FreeCADGui.SelectionObject:
    """getPreselection() -- Get preselected object"""


def clearPreselection():
    """clearPreselection() -- Clear the preselection"""


def countObjectsOfType(string: str, string1: str = None, resolve: int = 1, /) -> int:
    """
    countObjectsOfType(string, [string],[resolve=1]) -- Get the number of selected objects
    The first argument defines the object type e.g. "Part::Feature" and the
    second argumeht defines the document name. If no document name is given the
    currently active document is used
    """


def getSelection(docName: str = '', resolve: int = 1, single=False, /) -> list[FreeCAD.DocumentObject]:
    """
    getSelection(docName='',resolve=1,single=False) -- Return a list of selected objects

    docName - document name. Empty string means the active document, and '*' means all document
    resolve - whether to resolve the subname references.
              0: do not resolve, 1: resolve, 2: resolve with element map
    single - only return if there is only one selection
    """


def getPickedList(docName: str = '', /) -> list[FreeCADGui.SelectionObject]:
    """
    getPickedList(docName='') -- Return a list of objects under the last mouse click

    docName - document name. Empty string means the active document, and '*' means all document
    """


def enablePickedList(boolean=None, /):
    """enablePickedList(boolean) -- Enable/disable pick list"""


def getCompleteSelection(resolve: int = 1, /) -> list:
    """getCompleteSelection(resolve=1) -- Return a list of selected objects of all documents."""


def getSelectionEx(docName: str = '', resolve: int = 1, single=False, /) -> list[FreeCADGui.SelectionObject]:
    """
    getSelectionEx(docName='',resolve=1, single=False) -- Return a list of SelectionObjects

    docName - document name. Empty string means the active document, and '*' means all document
    resolve - whether to resolve the subname references.
              0: do not resolve, 1: resolve, 2: resolve with element map
    single - only return if there is only one selection

    The SelectionObjects contain a variety of information about the selection, e.g. sub-element names.
    """


def getSelectionObject(doc: str, obj: str, sub: str, arg3: tuple = None, /) -> FreeCADGui.SelectionObject:
    """getSelectionObject(doc,obj,sub,(x,y,z)) -- Return a SelectionObject"""


def addObserver(Object, resolve: int = 1, /):
    """addObserver(Object, resolve=1) -- Install an observer"""


def removeObserver(Object, /):
    """removeObserver(Object) -- Uninstall an observer"""


@typing.overload
def addSelectionGate(String_Filter_Gate: str, resolve: int = 1, /): ...


@typing.overload
def addSelectionGate(String_Filter_Gate, resolve: int = 1, /):
    """
    addSelectionGate(String|Filter|Gate, resolve=1) -- activate the selection gate.
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
    Gui.Selection.addSelectionGate(Gate())
    """


def removeSelectionGate():
    """removeSelectionGate() -- remove the active selection gate"""


def setVisible(visible=None, /):
    """
    setVisible(visible=None) -- set visibility of all selection items
    If 'visible' is None, then toggle visibility
    """


def pushSelStack(clearForward=True, overwrite=False, /):
    """
    pushSelStack(clearForward=True, overwrite=False) -- push current selection to stack

    clearForward: whether to clear the forward selection stack.
    overwrite: overwrite the top back selection stack with current selection.
    """


def hasSelection(docName: str = '', resolve=False, /) -> bool:
    """hasSelection(docName='', resolve=False) -- check if there is any selection"""


def hasSubSelection(docName: str = '', subElement: bool = False, /) -> bool:
    """hasSubSelection(docName='',subElement=False) -- check if there is any selection with subname"""


def getSelectionFromStack(docName: str = '', resolve: int = 1, index: int = 0, /) -> list:
    """
    getSelectionFromStack(docName='',resolve=1,index=0) -- Return a list of SelectionObjects from selection stack

    docName - document name. Empty string means the active document, and '*' means all document
    resolve - whether to resolve the subname references.
              0: do not resolve, 1: resolve, 2: resolve with element map
    index - select stack index, 0 is the last pushed selection, positive index to trace further back,
              and negative for forward stack item
    """
