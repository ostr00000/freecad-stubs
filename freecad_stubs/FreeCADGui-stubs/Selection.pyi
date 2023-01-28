import typing

import FreeCAD
import FreeCADGui


# Selection.cpp
@typing.overload
def addSelection(docname: str, objname: str, subname: str = None, x: float = 0, y: float = 0, z: float = 0, clearPreselect: bool = True, /): ...


@typing.overload
def addSelection(docname: str, objname: str, subname: str = 0, x: float = 0, y: float = 0, z: float = 0, clearPreselect: bool = True, /): ...


@typing.overload
def addSelection(object: FreeCAD.DocumentObject, subname: str = None, x: float = 0, y: float = 0, z: float = 0, clearPreselect: bool = True, /): ...


@typing.overload
def addSelection(docname: str, objname: str, subname: str = True, x: float = 0, y: float = 0, z: float = 0, clearPreselect: bool = True, /): ...


@typing.overload
def addSelection(object: FreeCAD.DocumentObject, sequence, clearPreselect: bool = True, /):
    """
    addSelection(docName, objName, subName, x=0, y=0, z=0, clear=True) -> None
    addSelection(obj, subName, x=0, y=0, z=0, clear=True) -> None
    addSelection(obj, subNames, clear=True) -> None

    Add an object to the selection.

    docName : str
        Name of the `App.Document`.
    objName : str
        Name of the `App.DocumentObject` to add.
    obj : App.DocumentObject
        Object to add.
    subName : str
        Subelement name.
    x : float
        Coordinate `x` of the point to pick.
    y : float
        Coordinate `y` of the point to pick.
    z : float
        Coordinate `z` of the point to pick.
    subNames : list of str
        List of subelement names.
    clear : bool
        Clear preselection.
    Possible exceptions: (FreeCAD.Base.FreeCADError, ValueError).
    """


def updateSelection(show: bool, object: FreeCAD.DocumentObject, subname: str = None, /):
    """
    updateSelection(show, obj, subName) -> None

    Update an object in the selection.

    show : bool
        Show or hide the selection.
    obj : App.DocumentObject
        Object to update.
    subName : str
        Name of the subelement to update.
    Possible exceptions: (FreeCAD.Base.FreeCADError).
    """


@typing.overload
def removeSelection(docname: str, objname: str, subname: str = None, /): ...


@typing.overload
def removeSelection(object: FreeCAD.DocumentObject, subname: str = None, /):
    """
    removeSelection(obj, subName) -> None
    removeSelection(docName, objName, subName) -> None

    Remove an object from the selection.

    docName : str
        Name of the `App.Document`.
    objName : str
        Name of the `App.DocumentObject` to remove.
    obj : App.DocumentObject
        Object to remove.
    subName : str
        Name of the subelement to remove.
    Possible exceptions: (FreeCAD.Base.FreeCADError).
    """


@typing.overload
def clearSelection(documentName: str = None, clearPreSelect: bool = True, /): ...


@typing.overload
def clearSelection(clearPreSelect: bool = True, /): ...


@typing.overload
def clearSelection(documentName: str = True, clearPreSelect: bool = True, /):
    """
    clearSelection(docName, clearPreSelect=True) -> None
    clearSelection(clearPreSelect=True) -> None

    Clear the selection in the given document. If no document is
    given the complete selection is cleared.

    docName : str
        Name of the `App.Document`.
    clearPreSelect : bool
        Clear preselection.
    """


def isSelected(object: FreeCAD.DocumentObject, subname: str = None, resolve: int = 1, /) -> bool:
    """
    isSelected(obj, subName, resolve=ResolveMode.OldStyleElement) -> bool

    Check if a given object is selected.

    obj : App.DocumentObject
        Object to check.
    subName : str
        Name of the subelement.
    resolve : int
        Resolve subelement reference.
    """


def setPreselection(obj: FreeCAD.DocumentObject, subname: str = None, x: float = 0, y: float = 0, z: float = 0, tp: int = 1):
    """
    setPreselection(obj, subName, x=0, y=0, z=0, type=1) -> None

    Set preselected object.

    obj : App.DocumentObject
        Object to preselect.
    subName : str
        Subelement name.
    x : float
        Coordinate `x` of the point to preselect.
    y : float
        Coordinate `y` of the point to preselect.
    z : float
        Coordinate `z` of the point to preselect.
    type : int
    Possible exceptions: (FreeCAD.Base.FreeCADError, ValueError).
    """


def getPreselection() -> FreeCADGui.SelectionObject:
    """
    getPreselection() -> Gui.SelectionObject

    Get preselected object.
    """


def clearPreselection():
    """
    clearPreselection() -> None

    Clear the preselection.
    """


def countObjectsOfType(objecttype: str, document: str = None, resolve: int = 1, /) -> int:
    """
    countObjectsOfType(type, docName, resolve=ResolveMode.OldStyleElement) -> int

    Get the number of selected objects. If no document name is given the
    active document is used and '*' means all documents.

    type : str
        Object type id name.
    docName : str
        Name of the `App.Document`.
    resolve : int
    """


def getSelection(documentName: str = None, resolve: int = 1, single: bool = False, /) -> list:
    """
    getSelection(docName, resolve=ResolveMode.OldStyleElement, single=False) -> list

    Return a list of selected objects. If no document name is given
    the active document is used and '*' means all documents.

    docName : str
        Name of the `App.Document`.
    resolve : int
        Resolve the subname references.
        0: do not resolve, 1: resolve, 2: resolve with element map.
    single : bool
        Only return if there is only one selection.
    """


def getPickedList(documentName: str = None, /) -> list:
    """
    getPickedList(docName) -> list of Gui.SelectionObject

    Return a list of SelectionObjects generated by the last mouse click.
    If no document name is given the active document is used and '*'
    means all documents.

    docName : str
        Name of the `App.Document`.
    """


def enablePickedList(enable: bool = True, /):
    """
    enablePickedList(enable=True) -> None

    Enable/disable pick list.

    enable : bool
    """


def getCompleteSelection(resolve: int = 1, /) -> list[FreeCADGui.SelectionObject]:
    """
    getCompleteSelection(resolve=ResolveMode.OldStyleElement) -> list

    Return a list of selected objects across all documents.

    resolve : int
    """


def getSelectionEx(documentName: str = None, resolve: int = 1, single: bool = False, /) -> list:
    """
    getSelectionEx(docName, resolve=ResolveMode.OldStyleElement, single=False) -> list of Gui.SelectionObject

    Return a list of SelectionObjects. If no document name is given the
    active document is used and '*' means all documents.
    The SelectionObjects contain a variety of information about the selection,
    e.g. subelement names.

    docName : str
        Name of the `App.Document`.
    resolve : int
        Resolve the subname references.
        0: do not resolve, 1: resolve, 2: resolve with element map.
    single : bool
        Only return if there is only one selection.
    """


def getSelectionObject(docName: str, objName: str, subName: str, tuple: tuple = None, /) -> FreeCADGui.SelectionObject:
    """
    getSelectionObject(docName, objName, subName, point) -> Gui.SelectionObject

    Return a SelectionObject.

    docName : str
        Name of the `App.Document`.
    objName : str
        Name of the `App.DocumentObject` to select.
    subName : str
        Subelement name.
    point : tuple
        Coordinates of the point to pick.
    """


def addObserver(o, resolve: int = 1, /):
    """
    addObserver(object, resolve=ResolveMode.OldStyleElement) -> None

    Install an observer.

    object : object
        Python object instance.
    resolve : int
    """


def removeObserver(o, /):
    """
    removeObserver(object) -> None

    Uninstall an observer.

    object : object
        Python object instance.
    """


@typing.overload
def addSelectionGate(filter: str, resolve: int = 1, /): ...


@typing.overload
def addSelectionGate(filterPy, resolve: int = 1, /): ...


@typing.overload
def addSelectionGate(gate, resolve: int = 1, /):
    """
    addSelectionGate(filter, resolve=ResolveMode.OldStyleElement) -> None

    Activate the selection gate.
    The selection gate will prohibit all selections that do not match
    the given selection criteria.

    filter : str, SelectionFilter, object
    resolve : int

    Examples strings are:
    Gui.Selection.addSelectionGate('SELECT Part::Feature SUBELEMENT Edge')
    Gui.Selection.addSelectionGate('SELECT Robot::RobotObject')

    An instance of SelectionFilter can also be set:
    filter = Gui.Selection.Filter('SELECT Part::Feature SUBELEMENT Edge')
    Gui.Selection.addSelectionGate(filter)

    The most flexible approach is to write a selection gate class that
    implements the method 'allow':
    class Gate:
        def allow(self,doc,obj,sub):
            return (sub[0:4] == 'Face')
    Gui.Selection.addSelectionGate(Gate())
    Possible exceptions: (ValueError).
    """


def removeSelectionGate():
    """
    removeSelectionGate() -> None

    Remove the active selection gate.
    """


def setVisible(visible=None, /):
    """
    setVisible(visible=None) -> None

    Set visibility of all selection items.

    visible : bool, None
        If None, then toggle visibility.
    """


def pushSelStack(clear: bool = True, overwrite: bool = False, /):
    """
    pushSelStack(clearForward=True, overwrite=False) -> None

    Push current selection to stack.

    clearForward : bool
        Clear the forward selection stack.
    overwrite : bool
        Overwrite the top back selection stack with current selection.
    """


@typing.overload
def hasSelection(docName, /, resolve=None): ...


@typing.overload
def hasSelection(doc: str = None, /) -> bool:
    """
    hasSelection(docName, resolve=ResolveMode.NoResolve) -> bool

    Check if there is any selection. If no document name is given,
    checks selections in all documents.

    docName : str
        Name of the `App.Document`.
    resolve : int
    """


def hasSubSelection(doc: str = None, subElement: bool = False, /) -> bool:
    """
    hasSubSelection(docName, subElement=False) -> bool

    Check if there is any selection with subname. If no document name
    is given the active document is used and '*' means all documents.

    docName : str
        Name of the `App.Document`.
    subElement : bool
    """


def getSelectionFromStack(documentName: str = None, resolve: int = 1, index: int = 0, /) -> list:
    """
    getSelectionFromStack(docName, resolve=ResolveMode.OldStyleElement, index=0) -> list of Gui.SelectionObject

    Return SelectionObjects from selection stack. If no document name is given
    the active document is used and '*' means all documents.

    docName : str
        Name of the `App.Document`.
    resolve : int
        Resolve the subname references.
        0: do not resolve, 1: resolve, 2: resolve with element map.
    index : int
        Select stack index.
        0: last pushed selection, > 0: trace back, < 0: trace forward.
    """
