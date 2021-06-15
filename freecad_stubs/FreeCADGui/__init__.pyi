import typing

import FreeCAD
import FreeCADGui
import FreeCADGui.Selection


# WorkbenchPy.xml
class Workbench(FreeCAD.BaseClass):
    """This is the base class for workbenches"""

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
    def Document(self) -> object:
        """Return the document the view provider is part of"""

    @property
    def Object(self) -> object:
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
    def ActiveObject(self) -> object:
        """The active object of the document"""

    @ActiveObject.setter
    def ActiveObject(self, value: object): ...

    @property
    def ActiveView(self) -> object:
        """The active view of the document"""

    @ActiveView.setter
    def ActiveView(self, value: object): ...

    @property
    def Document(self) -> object:
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
def subgraphFromObject(arg1: FreeCAD.DocumentObject, /):
    """subgraphFromObject(object) -> Node

    Return the Inventor subgraph to an object"""


def getSoDBVersion():
    """getSoDBVersion() -> String

    Return a text string containing the name
    of the Coin library and version information"""


# View3DPy.cpp
def message(arg1: str, /):
    """message()"""


def fitAll(arg1: float = None, /):
    """fitAll()"""


def viewBottom():
    """viewBottom()"""


def viewFront():
    """viewFront()"""


def viewLeft():
    """viewLeft()"""


def viewRear():
    """viewRear()"""


def viewRight():
    """viewRight()"""


def viewTop():
    """viewTop()"""


def viewAxometric():
    """viewAxonometric()"""


def viewAxonometric():
    """viewAxonometric()"""


def viewIsometric():
    """viewIsometric()"""


def viewDimetric():
    """viewDimetric()"""


def viewTrimetric():
    """viewTrimetric()"""


def viewDefaultOrientation(arg1: str = None, /):
    """viewDefaultOrientation()"""


def viewRotateLeft():
    """viewRotateLeft()"""


def viewRotateRight():
    """viewRotateRight()"""


def zoomIn():
    """zoomIn()"""


def zoomOut():
    """zoomOut()"""


def viewPosition(arg1: FreeCAD.Placement = None, arg2: int = None, arg3: int = None, /):
    """viewPosition()"""


def startAnimating(arg1: float, arg2: float, arg3: float, arg4: float, /):
    """startAnimating()"""


def stopAnimating():
    """stopAnimating()"""


def setAnimationEnabled(arg1: int, /):
    """setAnimationEnabled()"""


def isAnimationEnabled():
    """isAnimationEnabled()"""


def dump(arg1: str, /):
    """dump()"""


def dumpNode(arg1: object, /):
    """dumpNode(node)"""


@typing.overload
def setStereoType(arg1: int, /): ...


@typing.overload
def setStereoType(arg1: str, /):
    """setStereoType()"""


def getStereoType():
    """getStereoType()"""


def listStereoTypes():
    """listStereoTypes()"""


def saveImage(arg1: str, arg2: int = None, arg3: int = None, arg4: str = None, arg5: str = None, /):
    """saveImage()"""


def saveVectorGraphic(arg1: str, arg2: int = None, arg3: str = None, /):
    """saveVectorGraphic()"""


def getCamera():
    """getCamera()"""


def getCameraNode():
    """getCameraNode()"""


def getViewDirection():
    """getViewDirection() --> tuple of integers
    returns the direction vector the view is currently pointing at as tuple with xyz values
    """


def setViewDirection(arg1: object, /):
    """setViewDirection(tuple) --> None
    Sets the direction the view is pointing at. The direction must be given as tuple with
    three coordinates xyz"""


def setCamera(arg1: str, /):
    """setCamera()"""


def setCameraOrientation(arg1: object, arg2: bool = None, /):
    """setCameraOrientation()"""


def getCameraOrientation():
    """getCameraOrientation()"""


def getCameraType():
    """getCameraType()"""


@typing.overload
def setCameraType(arg1: int, /): ...


@typing.overload
def setCameraType(arg1: str, /):
    """setCameraType()"""


def listCameraTypes():
    """listCameraTypes()"""


def getCursorPos():
    """getCursorPos() -> tuple of integers

    Return the current cursor position relative to the coordinate system of the
    viewport region.
    """


def getObjectInfo(arg1: object, arg2: float = None, /):
    """getObjectInfo(tuple(int,int), [pick_radius]) -> dictionary or None

    Return a dictionary with the name of document, object and component. The
    dictionary also contains the coordinates of the appropriate 3d point of
    the underlying geometry in the scenegraph.
    If no geometry was found 'None' is returned, instead.
    """


def getObjectsInfo(arg1: object, arg2: float = None, /):
    """getObjectsInfo(tuple(int,int), [pick_radius]) -> dictionary or None

    Does the same as getObjectInfo() but returns a list of dictionaries or None.
    """


def getSize():
    """getSize()"""


def getPoint(arg1: int, arg2: int, /):
    """getPoint(pixel coords (as integer)) -> 3D vector

    Return the according 3D point on the focal plane to the given 2D point (in
    pixel coordinates).
    """


@typing.overload
def getPointOnScreen(arg1: FreeCAD.Vector, /): ...


@typing.overload
def getPointOnScreen(arg1: float, arg2: float, arg3: float, /):
    """getPointOnScreen(3D vector) -> pixel coords (as integer)

    Return the projected 3D point (in pixel coordinates).
    """


def addEventCallback(arg1: str, arg2: object, /):
    """addEventCallback()"""


def removeEventCallback(arg1: str, arg2: object, /):
    """removeEventCallback()"""


def setAnnotation(arg1: str, arg2: str, /):
    """setAnnotation()"""


def removeAnnotation(arg1: str, /):
    """removeAnnotation()"""


def getSceneGraph():
    """getSceneGraph()"""


def getViewer():
    """getViewer()"""


def addEventCallbackPivy(arg1: object, arg2: object, arg3: int = None, /):
    """addEventCallbackPivy()"""


def removeEventCallbackPivy(arg1: object, arg2: object, arg3: int = None, /):
    """removeEventCallbackPivy()"""


def addEventCallbackSWIG(arg1: object, arg2: object, arg3: int = None, /):
    """Deprecated -- use addEventCallbackPivy()"""


def removeEventCallbackSWIG(arg1: object, arg2: object, arg3: int = None, /):
    """Deprecated -- use removeEventCallbackPivy()"""


def setNavigationType(arg1: str, /):
    """setNavigationType()"""


def setAxisCross(arg1: int, /):
    """switch the big axis-cross on and off"""


def hasAxisCross():
    """check if the big axis-cross is on or off()"""


def addDraggerCallback(arg1: object, arg2: str, arg3: object, /):
    """addDraggerCallback(SoDragger, String CallbackType, function)
    Add a DraggerCalback function to the coin node
    Possibles types :
    'addFinishCallback','addStartCallback','addMotionCallback','addValueChangedCallback'
    """


def removeDraggerCallback(arg1: object, arg2: str, arg3: object, /):
    """removeDraggerCallback(SoDragger, String CallbackType, function)
    Remove the DraggerCalback function from the coin node
    Possibles types :
    'addFinishCallback','addStartCallback','addMotionCallback','addValueChangedCallback'
    """


def setActiveObject(arg1: str, arg2: FreeCAD.DocumentObject, /):
    """setActiveObject(name,object)
    add or set a new active object"""


def getActiveObject(arg1: str, /):
    """getActiveObject(name)
    returns the active object for the given type"""


def getViewProvidersOfType(arg1: str, /):
    """getViewProvidersOfType(name)
    returns a list of view providers for the given type"""


def redraw():
    """redraw(): renders the scene on screen (useful for animations)"""


def boxZoom(XMin: int, YMin: int, XMax: int, YMax: int):
    """boxZoom()"""


# WidgetFactory.cpp
def value(arg1: str, arg2: str, /):
    """&PyResource::value"""


def setValue(arg1: str, arg2: str, arg3: object, /):
    """&PyResource::setValue"""


# SplitView3DInventor.cpp
def fitAll():
    """fitAll()"""


def viewBottom():
    """viewBottom()"""


def viewFront():
    """viewFront()"""


def viewLeft():
    """viewLeft()"""


def viewRear():
    """viewRear()"""


def viewRight():
    """viewRight()"""


def viewTop():
    """viewTop()"""


def viewAxometric():
    """viewAxometric()"""


def viewIsometric():
    """viewIsometric()"""


def getViewer(arg1: int, /):
    """getViewer(index)"""


def close():
    """close()"""


# SelectionFilter.cpp
def match():
    """Check if the current selection matches the filter"""


def test(arg1: FreeCAD.DocumentObject, arg2: str = None, /):
    """test(Feature, SubName='')
    Test if a given object is described in the filter.
    If SubName is not empty the sub-element gets also tested."""


def setFilter(arg1: str, /):
    """Set a new selection filter"""


# PythonDebugger.cpp
@typing.overload
def write(arg1: str, /): ...


@typing.overload
def write(arg1: str, /):
    """write to stdout"""


# ApplicationPy.cpp
def activateWorkbench(arg1: str, /):
    """activateWorkbench(string) -> None

    Activate the workbench by name"""


def addWorkbench(arg1: object, /):
    """addWorkbench(string, object) -> None

    Add a workbench under a defined name."""


def removeWorkbench(arg1: str, /):
    """removeWorkbench(string) -> None

    Remove the workbench with name"""


def getWorkbench(arg1: str, /):
    """getWorkbench(string) -> object

    Get the workbench by its name"""


def listWorkbenches():
    """listWorkbenches() -> list

    Show a list of all workbenches"""


def activeWorkbench():
    """activeWorkbench() -> object

    Return the active workbench object"""


def addResourcePath(arg1: str, /):
    """addResourcePath(string) -> None

    Add a new path to the system where to find resource files
    like icons or localization files"""


def addLanguagePath(arg1: str, /):
    """addLanguagePath(string) -> None

    Add a new path to the system where to find language files"""


def addIconPath(arg1: str, /):
    """addIconPath(string) -> None

    Add a new path to the system where to find icon files"""


def addIcon(arg1: str, arg2: str, /):
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
    top-level domain (e.g. \"de\") or the language name (e.g. \"German\")"""


def supportedLocales():
    """supportedLocales() -> dict

    Returns a dict of all supported languages/top-level domains"""


def createDialog(arg1: str, /):
    """createDialog(string) -- Open a UI file"""


@typing.overload
def addPreferencePage(arg1: str, arg2: str, /): ...


@typing.overload
def addPreferencePage(arg1: type, arg2: str, /): ...


@typing.overload
def addPreferencePage(arg1: typing.Type, arg2: str, /): ...


@typing.overload
def addPreferencePage(arg1: type, arg2: str, /): ...


@typing.overload
def addPreferencePage(arg1: str, /): ...


@typing.overload
def addPreferencePage(arg1: object, /): ...


@typing.overload
def addPreferencePage(arg1: str, /): ...


@typing.overload
def addPreferencePage(arg1: str, /): ...


@typing.overload
def addPreferencePage(): ...


@typing.overload
def addPreferencePage(): ...


@typing.overload
def addPreferencePage(arg1: str, /): ...


@typing.overload
def addPreferencePage(arg1: str, /): ...


@typing.overload
def addPreferencePage(arg1: str, /): ...


@typing.overload
def addPreferencePage(arg1: str, arg2: str, /): ...


@typing.overload
def addPreferencePage(arg1: str, arg2: object, arg3: str = None, /): ...


@typing.overload
def addPreferencePage(arg1: str, arg2: int = None, /): ...


@typing.overload
def addPreferencePage(): ...


@typing.overload
def addPreferencePage(arg1: str, /): ...


@typing.overload
def addPreferencePage(arg1: str, /): ...


@typing.overload
def addPreferencePage(arg1: str, /): ...


@typing.overload
def addPreferencePage(): ...


@typing.overload
def addPreferencePage(arg1: str = None, arg2: int = None, /): ...


@typing.overload
def addPreferencePage(arg1: int = None, arg2: str = None, /): ...


@typing.overload
def addPreferencePage(arg1: str = None, arg2: int = None, /): ...


@typing.overload
def addPreferencePage(arg1: object, /): ...


@typing.overload
def addPreferencePage(arg1: object, /):
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


def hideObject(arg1: FreeCAD.DocumentObject, /):
    """hideObject(object) -> None

    Hide the view provider to the given object"""


def showObject(arg1: FreeCAD.DocumentObject, /):
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
def setActiveDocument(arg1: str, /): ...


@typing.overload
def setActiveDocument(arg1: FreeCAD.Document, /):
    """setActiveDocument(string or App.Document) -> None

    Activate the specified document"""


def activeView():
    """activeView() -> object or None

    Return the active view of the active document or None if no one exists"""


def activateView(arg1: str, arg2: bool, /):
    """activateView(type)

    Activate a view of the given type of the active document"""


@typing.overload
def getDocument(arg1: str, /): ...


@typing.overload
def getDocument(arg1: FreeCAD.Document, /):
    """getDocument(string) -> object

    Get a document by its name"""


def doCommand(arg1: str, /):
    """doCommand(string) -> None

    Prints the given string in the python console and runs it"""


def doCommandGui(arg1: str, /):
    """doCommandGui(string) -> None

    Prints the given string in the python console and runs it but doesn't record it in macros"""


def addModule(arg1: str, /):
    """addModule(string) -> None

    Prints the given module import only once in the macro recording"""


def showDownloads():
    """showDownloads() -> None

    Shows the downloads manager window"""


def showPreferences(arg1: str = None, arg2: int = None, /):
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
def getSoRenderManager():
    """getSoRenderManager() -> SoRenderManager
    Returns the render manager which is used to handle everything related to
    rendering the scene graph. It can be used to get full control over the
    render process
    """


def getSoEventManager():
    """getSoEventManager() -> SoEventManager
    Returns the event manager which is used to handle everything event related in
    the viewer. It can be used to change the event processing. This must however be
    done very carefully to not change the user interaction in an unpredictable manner.
    """


def getSceneGraph():
    """getSceneGraph() -> SoNode"""


def setSceneGraph(arg1: object, /):
    """setSceneGraph(SoNode)"""


def seekToPoint(arg1: object, /):
    """seekToPoint(tuple) -> None
    Initiate a seek action towards the 3D intersection of the scene and the
    ray from the screen coordinate's point and in the same direction as the
    camera is pointing. If the tuple has two entries it is interpreted as the
    screen coordinates xy and the intersection point with the scene is
    calculated. If three entries are given it is interpreted as the intersection
    point xyz and the seek is done towards this point"""


def setFocalDistance(arg1: float, /):
    """setFocalDistance(float) -> None
    """


def getFocalDistance():
    """getFocalDistance() -> float
    """


def getPoint(arg1: int, arg2: int, /):
    """getPoint(x, y) -> Base::Vector(x,y,z)"""


def getPickRadius():
    """getPickRadius(): returns radius of confusion in pixels for picking objects on screen (selection)."""


def setPickRadius(arg1: float, /):
    """setPickRadius(new_radius): sets radius of confusion in pixels for picking objects on screen (selection)."""


def setRedirectToSceneGraph(arg1: bool, /):
    """setRedirectToSceneGraph(bool): enables or disables to redirect events directly to the scene graph."""


def isRedirectedToSceneGraph():
    """isRedirectedToSceneGraph() -> bool: check whether event redirection is enabled."""


def setEnabledNaviCube(arg1: bool, /):
    """setEnabledNaviCube(bool): enables or disables the navi cube of the viewer."""


def isEnabledNaviCube():
    """isEnabledNaviCube() -> bool: check whether the navi cube is enabled."""


def setNaviCubeCorner(arg1: int, /):
    """setNaviCubeCorner(int): sets the corner where to show the navi cube:
    0=top left, 1=top right, 2=bottom left, 3=bottom right"""


Workbench: FreeCADGui.Workbench
ActiveDocument: Document
