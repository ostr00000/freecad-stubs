import typing

from FreeCADGui.TaskDialogPython import Control as ControlClass
import FreeCAD
import FreeCADGui
import FreeCADGui.Selection
import FreeCADTemplates


# WorkbenchPy.xml
class Workbench(FreeCAD.BaseClass):
    """This is the base class for workbenches"""

    MenuText = ""
    ToolTip = ""

    def Initialize(self):
        raise NotImplementedError

    def ContextMenu(self, recipient): ...

    def appendToolbar(self, name, cmds): ...

    def removeToolbar(self, name): ...

    def appendCommandbar(self, name, cmds): ...

    def removeCommandbar(self, name): ...

    def appendMenu(self, name, cmds): ...

    def removeMenu(self, name): ...

    def appendContextMenu(self, name, cmds): ...

    def removeContextMenu(self, name): ...

    def GetClassName(self): ...

    def activate(self):
        """Activate this workbench"""

    def name(self):
        """Return the workbench name"""


# ViewProviderPy.xml
class ViewProvider(FreeCAD.ExtensionContainer):
    """This is the ViewProvider base class"""

    @property
    def Annotation(self) -> object:
        """A pivy Separator to add a custom scene graph to this ViewProvider"""

    @Annotation.setter
    def Annotation(self, value: object): ...

    @property
    def IV(self) -> str:
        """Represents the whole ViewProvider as an Inventor string."""

    @property
    def Icon(self) -> object:
        """The icon of this ViewProvider"""

    @property
    def RootNode(self) -> object:
        """A pivy Separator with the root of this ViewProvider"""

    @RootNode.setter
    def RootNode(self, value: object): ...

    def addDisplayMode(self, arg1: object, arg2: str, /):
        """Add a new display mode to the view provider"""

    def addProperty(self, arg1: str, arg2: str = None, arg3: str = None, arg4: str = None, arg5: int = None, arg6: bool = None, arg7: bool = None, /):
        """
                            addProperty(string, string) -- Add a generic property.
                            The first argument specifies the type, the second the
                            name of the property.
                        """

    def claimChildren(self):
        """Returns list of objects that are to be grouped in tree under this object."""

    def hide(self):
        """Hide the object"""

    def isVisible(self):
        """Check if the object is visible"""

    def listDisplayModes(self):
        """Show a list of all display modes"""

    def removeProperty(self, string: str, /):
        """
                            removeProperty(string) -- Remove a generic property.
                            Note, you can only remove user-defined properties but not built-in ones.
                        """

    @typing.overload
    def setTransformation(self, arg1: FreeCAD.Matrix, /): ...

    @typing.overload
    def setTransformation(self, arg1: FreeCAD.Placement, /):
        """Set a transformation on the Inventor node"""

    def show(self):
        """Show the object"""

    def supportedProperties(self):
        """A list of supported property types"""

    def toString(self):
        """Return a string representation of the Inventor node"""


# PythonWorkbenchPy.xml
class PythonBaseWorkbench(FreeCADGui.Workbench):
    """This class handles document objects in group"""

    def appendCommandbar(self, arg1: str, arg2: object, /):
        """Append a new command bar"""

    def appendContextMenu(self, arg1: object, arg2: object, /):
        """Append a new context menu item"""

    def appendMenu(self, arg1: object, arg2: object, /):
        """Append a new menu"""

    def appendToolbar(self, arg1: str, arg2: object, /):
        """Append a new toolbar"""

    def listCommandbars(self):
        """Show a list of all command bars"""

    def listMenus(self):
        """Show a list of all menus"""

    def listToolbars(self):
        """Show a list of all toolbars"""

    def removeCommandbar(self, arg1: str, /):
        """Remove a command bar"""

    def removeContextMenu(self, arg1: str, /):
        """Remove a context menu item"""

    def removeMenu(self, arg1: str, /):
        """Remove a menu"""

    def removeToolbar(self, arg1: str, /):
        """Remove a toolbar"""


# ViewProviderDocumentObjectPy.xml
class ViewProviderDocumentObject(FreeCADGui.ViewProvider):
    """This is the ViewProvider base class"""

    @property
    def Proxy(self) -> FreeCADTemplates.ViewProxyPython: ...

    @Proxy.setter
    def Proxy(self, value: FreeCADTemplates.ViewProxyPython): ...

    @property
    def Document(self) -> FreeCADGui.Document:
        """Return the document the view provider is part of"""

    @property
    def Object(self) -> FreeCAD.DocumentObject:
        """Return the associated data object"""

    def update(self):
        """Update the view representation of the object"""


# SelectionObjectPy.xml
class SelectionObject(FreeCAD.BaseClass):
    """This class represents selections made by the user. It holds information about the object, document and sub-element of the selection."""

    @property
    def Document(self) -> object:
        """Selected document"""

    @property
    def DocumentName(self) -> str:
        """Name of the document of the selected object"""

    @property
    def FullName(self) -> str:
        """Name of the selected object"""

    @property
    def HasSubObjects(self) -> bool:
        """Selected sub-element, if any"""

    @property
    def Object(self) -> object:
        """Selected object"""

    @property
    def ObjectName(self) -> str:
        """Name of the selected object"""

    @property
    def PickedPoints(self) -> tuple:
        """Picked points for selection"""

    @property
    def SubElementNames(self) -> tuple:
        """Name of the selected sub-element if any"""

    @property
    def SubObjects(self) -> tuple:
        """Selected sub-element, if any"""

    @property
    def TypeName(self) -> str:
        """Type name of the selected object"""

    def isObjectTypeOf(self, arg1: str, /):
        """Test for a certain father class."""

    def remove(self):
        """Remove this selection item from the selection. This object becomes invalid."""


# DocumentPy.xml
class Document(FreeCAD.Persistence):
    """This is a Document class"""

    @property
    def ActiveObject(self) -> typing.Optional[FreeCAD.DocumentObject]:
        """The active object of the document"""

    @ActiveObject.setter
    def ActiveObject(self, value: typing.Optional[FreeCAD.DocumentObject]): ...

    @property
    def ActiveView(self) -> FreeCADGui.View3DInventorPy:
        """The active view of the document"""

    @ActiveView.setter
    def ActiveView(self, value: FreeCADGui.View3DInventorPy): ...

    @property
    def Document(self) -> FreeCAD.Document:
        """The related App document to this Gui document"""

    @property
    def Modified(self) -> bool:
        """Returns True if the document is marked as modified, and False otherwise"""

    def activeObject(self):
        """deprecated -- use ActiveObject"""

    def activeView(self):
        """deprecated -- use ActiveView"""

    def addAnnotation(self, arg1: str, arg2: str, arg3: str = None, /):
        """Add an Inventor object"""

    def getInEdit(self):
        """
                  getInEdit()
                  Returns the current object in edit mode or None if there is no such object
                """

    def getObject(self, arg1: str, /):
        """Return the object with the given name"""

    def hide(self, arg1: str, /):
        """Hide the object"""

    def mdiViewsOfType(self, arg1: str, /):
        """Return a list if mdi views of a given type"""

    def mergeProject(self, arg1: str, /):
        """Merges this document with another project file"""

    def resetEdit(self):
        """
                  Reset (end) the current editing.
                """

    def scrollToTreeItem(self, ViewObject: FreeCADGui.ViewProviderDocumentObject, /):
        """scrollToTreeItem(ViewObject) - scroll the tree view to the item of a view object"""

    def sendMsgToViews(self, arg1: str, /):
        """Send a message to all views of the document"""

    @typing.overload
    def setEdit(self, String_Name_ViewProvider_DocumentObject_: str, mod: int = None, /): ...

    @typing.overload
    def setEdit(self, String_Name_ViewProvider_DocumentObject_: FreeCAD.DocumentObject, mod: int = None, /): ...

    @typing.overload
    def setEdit(self, String_Name_ViewProvider_DocumentObject_: FreeCADGui.ViewProvider, mod: int = None, /):
        """
                  setEdit([String:Name|ViewProvider|DocumentObject]|,mod)
                  Set the given object in edit mode.
                """

    def setPos(self, arg1: str, arg2: FreeCAD.Matrix, /):
        """Set the position"""

    def show(self, arg1: str, /):
        """Show the object"""

    def toggleTreeItem(self, DocObject: FreeCAD.DocumentObject, int: int = 0, /):
        """toggleTreeItem(DocObject,int=0) - change TreeItem of a document object 0:Toggle,1:Collaps,2:Expand"""

    def update(self):
        """Update the view representations of all objects"""


# Application.cpp
def subgraphFromObject(object: FreeCAD.DocumentObject, /):
    """subgraphFromObject(object) -> Node

    Return the Inventor subgraph to an object"""


def getSoDBVersion():
    """getSoDBVersion() -> String

    Return a text string containing the name
    of the Coin library and version information"""


# View3DPy.cpp
class View3DInventorPy:
    """Python binding class for the Inventor viewer class"""

    def message(self, arg1: str, /):
        """message()"""

    def fitAll(self, arg1: float = None, /):
        """fitAll()"""

    def viewBottom(self):
        """viewBottom()"""

    def viewFront(self):
        """viewFront()"""

    def viewLeft(self):
        """viewLeft()"""

    def viewRear(self):
        """viewRear()"""

    def viewRight(self):
        """viewRight()"""

    def viewTop(self):
        """viewTop()"""

    def viewAxometric(self):
        """viewAxonometric()"""

    def viewAxonometric(self):
        """viewAxonometric()"""

    def viewIsometric(self):
        """viewIsometric()"""

    def viewDimetric(self):
        """viewDimetric()"""

    def viewTrimetric(self):
        """viewTrimetric()"""

    def viewDefaultOrientation(self, arg1: str = None, /):
        """viewDefaultOrientation()"""

    def viewRotateLeft(self):
        """viewRotateLeft()"""

    def viewRotateRight(self):
        """viewRotateRight()"""

    def zoomIn(self):
        """zoomIn()"""

    def zoomOut(self):
        """zoomOut()"""

    def viewPosition(self, arg1: FreeCAD.Placement = None, arg2: int = None, arg3: int = None, /):
        """viewPosition()"""

    def startAnimating(self, arg1: float, arg2: float, arg3: float, arg4: float, /):
        """startAnimating()"""

    def stopAnimating(self):
        """stopAnimating()"""

    def setAnimationEnabled(self, arg1: int, /):
        """setAnimationEnabled()"""

    def isAnimationEnabled(self):
        """isAnimationEnabled()"""

    def dump(self, arg1: str, /):
        """dump()"""

    def dumpNode(self, node: object, /):
        """dumpNode(node)"""

    @typing.overload
    def setStereoType(self, arg1: int, /): ...

    @typing.overload
    def setStereoType(self, arg1: str, /):
        """setStereoType()"""

    def getStereoType(self):
        """getStereoType()"""

    def listStereoTypes(self):
        """listStereoTypes()"""

    def saveImage(self, arg1: str, arg2: int = None, arg3: int = None, arg4: str = None, arg5: str = None, /):
        """saveImage()"""

    def saveVectorGraphic(self, arg1: str, arg2: int = None, arg3: str = None, /):
        """saveVectorGraphic()"""

    def getCamera(self):
        """getCamera()"""

    def getCameraNode(self):
        """getCameraNode()"""

    def getViewDirection(self):
        """getViewDirection() --> tuple of integers
        returns the direction vector the view is currently pointing at as tuple with xyz values
        """

    def setViewDirection(self, tuple: object, /):
        """setViewDirection(tuple) --> None
        Sets the direction the view is pointing at. The direction must be given as tuple with
        three coordinates xyz"""

    def setCamera(self, arg1: str, /):
        """setCamera()"""

    def setCameraOrientation(self, arg1: object, arg2: bool = None, /):
        """setCameraOrientation()"""

    def getCameraOrientation(self):
        """getCameraOrientation()"""

    def getCameraType(self):
        """getCameraType()"""

    @typing.overload
    def setCameraType(self, arg1: int, /): ...

    @typing.overload
    def setCameraType(self, arg1: str, /):
        """setCameraType()"""

    def listCameraTypes(self):
        """listCameraTypes()"""

    def getCursorPos(self):
        """getCursorPos() -> tuple of integers

        Return the current cursor position relative to the coordinate system of the
        viewport region.
        """

    def getObjectInfo(self, tuple_int_int_: object, pick_radius: float = None, /):
        """getObjectInfo(tuple(int,int), [pick_radius]) -> dictionary or None

        Return a dictionary with the name of document, object and component. The
        dictionary also contains the coordinates of the appropriate 3d point of
        the underlying geometry in the scenegraph.
        If no geometry was found 'None' is returned, instead.
        """

    def getObjectsInfo(self, tuple_int_int_: object, pick_radius: float = None, /):
        """getObjectsInfo(tuple(int,int), [pick_radius]) -> dictionary or None

        Does the same as getObjectInfo() but returns a list of dictionaries or None.
        """

    def getSize(self):
        """getSize()"""

    def getPoint(self, arg1: int, arg2: int, /):
        """getPoint(pixel coords (as integer)) -> 3D vector

        Return the according 3D point on the focal plane to the given 2D point (in
        pixel coordinates).
        """

    def getPointOnScreen(self, arg: FreeCAD.Vector, /):
        """getPointOnScreen(3D vector) -> pixel coords (as integer)

        Return the projected 3D point (in pixel coordinates).
        """

    def addEventCallback(self, arg1: str, arg2: object, /):
        """addEventCallback()"""

    def removeEventCallback(self, arg1: str, arg2: object, /):
        """removeEventCallback()"""

    def setAnnotation(self, arg1: str, arg2: str, /):
        """setAnnotation()"""

    def removeAnnotation(self, arg1: str, /):
        """removeAnnotation()"""

    def getSceneGraph(self):
        """getSceneGraph()"""

    def getViewer(self):
        """getViewer()"""

    def addEventCallbackPivy(self, arg1: object, arg2: object, arg3: int = None, /):
        """addEventCallbackPivy()"""

    def removeEventCallbackPivy(self, arg1: object, arg2: object, arg3: int = None, /):
        """removeEventCallbackPivy()"""

    def addEventCallbackSWIG(self, arg1: object, arg2: object, arg3: int = None, /):
        """Deprecated -- use addEventCallbackPivy()"""

    def removeEventCallbackSWIG(self, arg1: object, arg2: object, arg3: int = None, /):
        """Deprecated -- use removeEventCallbackPivy()"""

    def listNavigationTypes(self):
        """listNavigationTypes()"""

    def getNavigationType(self):
        """getNavigationType()"""

    def setNavigationType(self, arg1: str, /):
        """setNavigationType()"""

    def setAxisCross(self, arg1: int, /):
        """switch the big axis-cross on and off"""

    def hasAxisCross(self):
        """check if the big axis-cross is on or off()"""

    def addDraggerCallback(self, SoDragger: object, String_CallbackType: str, function: object, /):
        """addDraggerCallback(SoDragger, String CallbackType, function)
        Add a DraggerCalback function to the coin node
        Possibles types :
        'addFinishCallback','addStartCallback','addMotionCallback','addValueChangedCallback'
        """

    def removeDraggerCallback(self, SoDragger: object, String_CallbackType: str, function: object, /):
        """removeDraggerCallback(SoDragger, String CallbackType, function)
        Remove the DraggerCalback function from the coin node
        Possibles types :
        'addFinishCallback','addStartCallback','addMotionCallback','addValueChangedCallback'
        """

    def setActiveObject(self, name: str, object: FreeCAD.DocumentObject, /):
        """setActiveObject(name,object)
        add or set a new active object"""

    def getActiveObject(self, name: str, /):
        """getActiveObject(name)
        returns the active object for the given type"""

    def getViewProvidersOfType(self, name: str, /):
        """getViewProvidersOfType(name)
        returns a list of view providers for the given type"""

    def redraw(self):
        """redraw(): renders the scene on screen (useful for animations)"""

    def boxZoom(self, XMin: int, YMin: int, XMax: int, YMax: int):
        """boxZoom()"""


# WidgetFactory.cpp
class UiLoader:
    """UiLoader to create widgets"""

    @typing.overload
    def load(self, string, QWidget_parent = None): ...

    @typing.overload
    def load(self, QIODevice, QWidget_parent = None):
        """load(string, QWidget parent=None) -> QWidget
        load(QIODevice, QWidget parent=None) -> QWidget"""

    def createWidget(self):
        """createWidget()"""


class PyResource:
    """PyResource"""

    def value(self, arg1: str, arg2: str, /): ...

    def setValue(self, arg1: str, arg2: str, arg3: object, /): ...


# PythonConsolePy.cpp
class PythonStdout:
    """Redirection of stdout to FreeCAD's Python console window"""

    def isatty(self):
        """isatty()"""

    def write(self):
        """write()"""

    def flush(self):
        """flush()"""


class PythonStderr:
    """Redirection of stdout to FreeCAD's Python console window"""

    def isatty(self):
        """isatty()"""

    def write(self):
        """write()"""

    def flush(self):
        """flush()"""


class OutputStdout:
    """Redirection of stdout to FreeCAD's output window"""

    def isatty(self):
        """isatty()"""

    def write(self):
        """write()"""

    def flush(self):
        """flush()"""


class OutputStderr:
    """Redirection of stdout to FreeCAD's output window"""

    def isatty(self):
        """isatty()"""

    def write(self):
        """write()"""

    def flush(self):
        """flush()"""


class PythonStdin:
    """Redirection of stdin to FreeCAD to open an input dialog"""

    def readline(self):
        """readline()"""


# SplitView3DInventor.cpp
class AbstractSplitViewPy:
    """Python binding class for the Inventor viewer class"""

    def fitAll(self):
        """fitAll()"""

    def viewBottom(self):
        """viewBottom()"""

    def viewFront(self):
        """viewFront()"""

    def viewLeft(self):
        """viewLeft()"""

    def viewRear(self):
        """viewRear()"""

    def viewRight(self):
        """viewRight()"""

    def viewTop(self):
        """viewTop()"""

    def viewAxometric(self):
        """viewAxometric()"""

    def viewIsometric(self):
        """viewIsometric()"""

    def getViewer(self, index: int, /):
        """getViewer(index)"""

    def close(self):
        """close()"""


# SelectionFilter.cpp
class SelectionFilter:
    """Filter for certain selection
    Example strings are:
    "SELECT Part::Feature SUBELEMENT Edge",
    "SELECT Part::Feature", 
    "SELECT Part::Feature COUNT 1..5"
    """

    def match(self):
        """Check if the current selection matches the filter"""

    def result(self):
        """If match() returns True then with result() you get a list of the matching objects"""

    def test(self, Feature: FreeCAD.DocumentObject, SubName: str = '', /):
        """test(Feature, SubName='')
        Test if a given object is described in the filter.
        If SubName is not empty the sub-element gets also tested."""

    def setFilter(self, arg1: str, /):
        """Set a new selection filter"""


# PythonDebugger.cpp
class PythonDebugStdout:
    """Redirection of stdout to FreeCAD's Python debugger window"""

    def write(self, arg1: str, /):
        """write to stdout"""


class PythonDebugStderr:
    """Redirection of stderr to FreeCAD's Python debugger window"""

    def write(self, arg1: str, /):
        """write to stderr"""


# ApplicationPy.cpp
def activateWorkbench(string: str, /):
    """activateWorkbench(string) -> None

    Activate the workbench by name"""


def addWorkbench(arg1: object, /):
    """addWorkbench(string, object) -> None

    Add a workbench under a defined name."""


def removeWorkbench(string: str, /):
    """removeWorkbench(string) -> None

    Remove the workbench with name"""


def getWorkbench(string: str, /):
    """getWorkbench(string) -> object

    Get the workbench by its name"""


def listWorkbenches():
    """listWorkbenches() -> list

    Show a list of all workbenches"""


def activeWorkbench():
    """activeWorkbench() -> object

    Return the active workbench object"""


def addResourcePath(string: str, /):
    """addResourcePath(string) -> None

    Add a new path to the system where to find resource files
    like icons or localization files"""


def addLanguagePath(string: str, /):
    """addLanguagePath(string) -> None

    Add a new path to the system where to find language files"""


def addIconPath(string: str, /):
    """addIconPath(string) -> None

    Add a new path to the system where to find icon files"""


def addIcon(string: str, string_or_list: str, /):
    """addIcon(string, string or list) -> None

    Add an icon as file name or in XPM format to the system"""


def getMainWindow():
    """getMainWindow() -> QMainWindow

    Return the main window instance"""


def updateGui():
    """updateGui() -> None

    Update the main window and all its windows"""


def updateLocale():
    """updateLocale() -> None

    Update the localization"""


def getLocale():
    """getLocale() -> string

    Returns the locale currently used by FreeCAD"""


def setLocale(arg1: str, /):
    """getLocale(string) -> None

    Sets the locale used by FreeCAD. You can set it by
    top-level domain (e.g. "de") or the language name (e.g. "German")"""


def supportedLocales():
    """supportedLocales() -> dict

    Returns a dict of all supported languages/top-level domains"""


def createDialog(string: str, /):
    """createDialog(string) -- Open a UI file"""


@typing.overload
def addPreferencePage(string: str, string1: str, /): ...


@typing.overload
def addPreferencePage(string: type, string1: str, /): ...


@typing.overload
def addPreferencePage(string: typing.Type, string1: str, /): ...


@typing.overload
def addPreferencePage(string: str, string1: int = None, /): ...


@typing.overload
def addPreferencePage(string: str = None, string1: int = None, /): ...


@typing.overload
def addPreferencePage(string: int = None, string1: str = None, /):
    """addPreferencePage(string,string) -- Add a UI form to the
    preferences dialog. The first argument specifies the file nameand the second specifies the group name"""


def addCommand(arg1: str, arg2: object, arg3: str = None, /):
    """addCommand(string, object) -> None

    Add a command object"""


def runCommand(arg1: str, arg2: int = None, /):
    """runCommand(string) -> None

    Run command with name"""


def listCommands():
    """listCommands() -> list of strings

    Returns a list of all commands known to FreeCAD."""


def SendMsgToActiveView(arg1: str, arg2: bool = None, /):
    """deprecated -- use class View"""


def hide(arg1: str, /):
    """deprecated"""


def show(arg1: str, /):
    """deprecated"""


def hideObject(object: FreeCAD.DocumentObject, /):
    """hideObject(object) -> None

    Hide the view provider to the given object"""


def showObject(object: FreeCAD.DocumentObject, /):
    """showObject(object) -> None

    Show the view provider to the given object"""


def open(arg1: str, /):
    """Open a macro, Inventor or VRML file"""


def insert(arg1: str, arg2: str = None, /):
    """Open a macro, Inventor or VRML file"""


def export(arg1: object, arg2: str, /):
    """save scene to Inventor or VRML file"""


def activeDocument():
    """activeDocument() -> object or None

    Return the active document or None if no one exists"""


@typing.overload
def setActiveDocument(string_or_App_Document: str, /): ...


@typing.overload
def setActiveDocument(string_or_App_Document: FreeCAD.Document, /):
    """setActiveDocument(string or App.Document) -> None

    Activate the specified document"""


def activeView():
    """activeView() -> object or None

    Return the active view of the active document or None if no one exists"""


def activateView(arg1: str, arg2: bool, /):
    """activateView(type)

    Activate a view of the given type of the active document"""


@typing.overload
def getDocument(string: str, /): ...


@typing.overload
def getDocument(string: FreeCAD.Document, /):
    """getDocument(string) -> object

    Get a document by its name"""


def doCommand(string: str, /):
    """doCommand(string) -> None

    Prints the given string in the python console and runs it"""


def doCommandGui(string: str, /):
    """doCommandGui(string) -> None

    Prints the given string in the python console and runs it but doesn't record it in macros"""


def addModule(string: str, /):
    """addModule(string) -> None

    Prints the given module import only once in the macro recording"""


def showDownloads():
    """showDownloads() -> None

    Shows the downloads manager window"""


def showPreferences(string: str = None, int: int = None, /):
    """showPreferences([string,int]) -> None

    Shows the preferences window. If string and int are provided, the given page index in the given group is shown."""


def createViewer(arg1: int = None, arg2: str = None, /):
    """createViewer([int]) -> View3DInventor/SplitView3DInventor

    shows and returns a viewer. If the integer argument is given and > 1: -> splitViewer"""


def getMarkerIndex(arg1: str = None, arg2: int = None, /):
    """Get marker index according to marker size setting"""


def addDocumentObserver(arg1: object, /):
    """addDocumentObserver() -> None

    Add an observer to get notified about changes on documents."""


def removeDocumentObserver(arg1: object, /):
    """removeDocumentObserver() -> None

    Remove an added document observer."""


# View3DViewerPy.cpp
class View3DInventorViewerPy:
    """Python binding class for the 3D viewer class"""

    def getSoRenderManager(self):
        """getSoRenderManager() -> SoRenderManager
        Returns the render manager which is used to handle everything related to
        rendering the scene graph. It can be used to get full control over the
        render process
        """

    def getSoEventManager(self):
        """getSoEventManager() -> SoEventManager
        Returns the event manager which is used to handle everything event related in
        the viewer. It can be used to change the event processing. This must however be
        done very carefully to not change the user interaction in an unpredictable manner.
        """

    def getSceneGraph(self):
        """getSceneGraph() -> SoNode"""

    def setSceneGraph(self, SoNode: object, /):
        """setSceneGraph(SoNode)"""

    def seekToPoint(self, tuple: object, /):
        """seekToPoint(tuple) -> None
        Initiate a seek action towards the 3D intersection of the scene and the
        ray from the screen coordinate's point and in the same direction as the
        camera is pointing. If the tuple has two entries it is interpreted as the
        screen coordinates xy and the intersection point with the scene is
        calculated. If three entries are given it is interpreted as the intersection
        point xyz and the seek is done towards this point"""

    def setFocalDistance(self, float: float, /):
        """setFocalDistance(float) -> None
        """

    def getFocalDistance(self):
        """getFocalDistance() -> float
        """

    def getPoint(self, x: int, y: int, /):
        """getPoint(x, y) -> Base::Vector(x,y,z)"""

    def getPickRadius(self):
        """getPickRadius(): returns radius of confusion in pixels for picking objects on screen (selection)."""

    def setPickRadius(self, new_radius: float, /):
        """setPickRadius(new_radius): sets radius of confusion in pixels for picking objects on screen (selection)."""

    def setRedirectToSceneGraph(self, bool: bool, /):
        """setRedirectToSceneGraph(bool): enables or disables to redirect events directly to the scene graph."""

    def isRedirectedToSceneGraph(self):
        """isRedirectedToSceneGraph() -> bool: check whether event redirection is enabled."""

    def setEnabledNaviCube(self, bool: bool, /):
        """setEnabledNaviCube(bool): enables or disables the navi cube of the viewer."""

    def isEnabledNaviCube(self):
        """isEnabledNaviCube() -> bool: check whether the navi cube is enabled."""

    def setNaviCubeCorner(self, int: int, /):
        """setNaviCubeCorner(int): sets the corner where to show the navi cube:
        0=top left, 1=top right, 2=bottom left, 3=bottom right"""


Workbench: FreeCADGui.Workbench
ActiveDocument: Document
Control = ControlClass()  # hack to show this module in current module hints
