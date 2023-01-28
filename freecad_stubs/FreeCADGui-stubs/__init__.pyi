import typing

from FreeCADGui.TaskDialogPython import Control as ControlClass
import FreeCAD
import FreeCADGui
import FreeCADGui.Selection
import FreeCADTemplates
import pivy.coin
import qtpy.QtCore
import qtpy.QtGui
import qtpy.QtWidgets

_T = typing.TypeVar("_T")
Triple_t: typing.TypeAlias = tuple[_T, _T, _T]
Quadruple_t: typing.TypeAlias = tuple[_T, _T, _T, _T]

class ReturnGetObjectInfoDict(typing.TypedDict):
    x: float
    y: float
    z: float
    ParentObject: typing.Any
    SubName: str
    Document: str
    Object: str
    Component: str


class ReturnGetObjectsInfoDict(typing.TypedDict):
    x: float
    y: float
    z: float
    ParentObject: typing.Any
    SubName: str
    Document: str
    Object: str
    Component: str



# WorkbenchPy.xml
class WorkbenchC(FreeCAD.BaseClass):
    """This is the base class for workbenches"""

    MenuText: str = ''
    ToolTip: str = ''
    Icon: str = None  # path to the icon

    def Initialize(self):
        raise NotImplementedError

    def Activated(self): ...

    def Deactivated(self): ...

    def ContextMenu(self, recipient): ...

    def reloadActive(self): ...

    def GetClassName(self):
        return 'Gui::PythonWorkbench'

    def activate(self):
        """Activate this workbench"""

    def getToolbarItems(self) -> dict[typing.Any, list[str]]:
        """Show a dict of all toolbars and their commands"""

    def listCommandbars(self) -> list[str]:
        """Show a list of all command bars"""

    def listMenus(self) -> list[str]:
        """Show a list of all menus"""

    def listToolbars(self) -> list[str]:
        """Show a list of all toolbars"""

    def name(self) -> str:
        """Return the workbench name"""

    @staticmethod
    def reloadActive():
        """Reload the active workbench after changing menus or toolbars"""


# LinkViewPy.xml
class LinkView(FreeCAD.BaseClass):
    """Helper class to link to a view object"""

    def __init__(self):
        """Helper class to link to a view object"""

    @property
    def Count(self) -> int:
        """Set the element size to create an array of linked object"""

    @property
    def LinkedView(self) -> object | typing.Any:
        """The linked view object"""

    @property
    def Owner(self) -> object | typing.Any:
        """The owner view object of this link handle"""

    @property
    def RootNode(self) -> pivy.coin.SoSeparator:
        """A pivy node holding the cloned representation of the linked view object"""

    @property
    def SubNames(self) -> object | tuple[str, ...]:
        """The sub-object reference of the link"""

    @property
    def Visibilities(self) -> object | tuple[bool, ...]:
        """Get/set the child element visibility"""

    def getBoundBox(self, vobj=None, /) -> FreeCAD.BoundBox:
        """getBoundBox(vobj=None): get the bounding box."""

    def getChildren(self) -> tuple[typing.Any, ...]:
        """Get children view objects"""

    @typing.overload
    def getDetailPath(self, element, /): ...

    @typing.overload
    def getDetailPath(self, sub: str, path, /) -> pivy.coin.SoDetail:
        """
        getDetailPath(element): get the 3d path an detail of an element.

        Return a tuple(path,detail) for the coin3D SoPath and SoDetail of the element
                
        Possible exceptions: (TypeError).
        """

    def getElementPicked(self, obj, /) -> str:
        """
        getElementPicked(pickPoint): get the element under a 3d pick point. 
        Possible exceptions: (TypeError).
        """

    def reset(self):
        """Reset the link view and clear the links"""

    def setChildren(self, pyObj, pyVis: list = None, type: str = 0, /):
        """
        setChildren([obj...],vis=[],type=0)
        Group a list of children objects. Note, this mode of operation is incompatible
        with link array. Calling this function will deactivate link array. And calling
        setSize() will reset all linked children.

        vis: initial visibility status of the children

        type: children linking type,
           0: override transformation and visibility,
           1: override visibility,
           2: override none.
        """

    @typing.overload
    def setLink(self, pyObj, pySubName=None, /): ...

    @typing.overload
    def setLink(self, object, subname, /, *args):
        """
        setLink(object): Set the link

        setLink(object, subname): Set the link with a sub-object reference

        setLink(object, [subname,...]): Set the link with a list of sub object references

        object: The linked document object or its view object

        subname: a string or tuple/list of strings sub-name references to sub object
                 or sub elements (e.g. Face1, Edge2) belonging to the linked object.
                 The sub-name must end with a '.' if it is referencing an sub-object,
                 or else it is considered a sub-element reference.
                
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def setMaterial(self, pyObj, /): ...

    @typing.overload
    def setMaterial(self, Material, /, *args): ...

    @typing.overload
    def setMaterial(self, arg1, arg2, /):
        """
        setMaterial(Material): set the override material of the entire linked object

        setMaterial([Material,...]): set the materials for the elements of the link
                                     array/group.

        setMaterial({Int:Material,...}): set the material for the elements of the
                                         link array/group by index.

        If material is None, then the material is unset. If the material of an element
        is unset, it defaults to the override material of the linked object, if there
        is one
                
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def setTransform(self, pyObj, /): ...

    @typing.overload
    def setTransform(self, matrix, /, *args): ...

    @typing.overload
    def setTransform(self, arg1, arg2, /):
        """
        setTransform(matrix): set transformation of the linked object

        setTransform([matrix,...]): set transformation for the elements of the link
                                    array/group

        setTransform({index:matrix,...}): set transformation for elements of the link
                                          array/group by index
                
        Possible exceptions: (TypeError).
        """

    def setType(self, type: int, sublink: bool = True, /):
        """
        setType(type, sublink=True): set the link type.

        type=0:  override transformation and visibility
        type=1:  override visibility
        type=2:  no override
        type=-1: sub-object link with override visibility
        type=-2: sub-object link with override transformation and visibility

        sublink: auto delegate to the sub-object references in the link, if there is
                 one and only one.
        """


# ViewProviderPy.xml
class ViewProvider(FreeCAD.ExtensionContainer):
    """This is the ViewProvider base class"""

    @property
    def Annotation(self) -> pivy.coin.SoSeparator:
        """A pivy Separator to add a custom scenegraph to this ViewProvider."""

    @Annotation.setter
    def Annotation(self, value: pivy.coin.SoSeparator): ...

    @property
    def CanRemoveChildrenFromRoot(self) -> bool:
        """Tells the tree view whether to remove the children item from root or not."""

    @property
    def DefaultMode(self) -> int:
        """Get/Set the default display mode in turns of coin node index."""

    @DefaultMode.setter
    def DefaultMode(self, value: int): ...

    @property
    def DropPrefix(self) -> str:
        """Subname referecing the sub-object for holding dropped object."""

    @property
    def IV(self) -> str:
        """Represents the whole ViewProvider as an Inventor string."""

    @property
    def Icon(self) -> qtpy.QtGui.QIcon:
        """The icon of this ViewProvider."""

    @property
    def LinkVisibility(self) -> bool:
        """Get/set visibilities of all links to this view object."""

    @property
    def RootNode(self) -> pivy.coin.SoSeparator:
        """A pivy Separator with the root of this ViewProvider."""

    @RootNode.setter
    def RootNode(self, value: pivy.coin.SoSeparator): ...

    @property
    def SwitchNode(self) -> pivy.coin.SoSwitch:
        """A pivy SoSwitch for the display mode switch of this ViewProvider."""

    @SwitchNode.setter
    def SwitchNode(self, value: pivy.coin.SoSwitch): ...

    def addDisplayMode(self, obj, mode: str, /):
        """
        addDisplayMode(obj, mode) -> None

        Add a new display mode to the view provider.

        obj : coin.SoNode
            Display mode.
        mode : str
            Name of the display mode.
        Possible exceptions: (RuntimeError).
        """

    def addProperty(self, sType: str, sName: str = None, sGroup: str = None, sDoc: str = None, attr: int = 0, ro: bool = False, hd: bool = False, /) -> FreeCADGui.ViewProvider:
        """
        addProperty(type, name, group, doc, attr=0, ro=False, hd=False) -> ViewProvider

        Add a generic property.

        type : str
            Property type.
        name : str
            Property name. Optional.
        group : str
            Property group. Optional.
        attr : int
            Property attributes.
        ro : bool
            Read only property.
        hd : bool
            Hidden property.
        Possible exceptions: (RuntimeError, TypeError).
        """

    def canDragAndDropObject(self, obj: FreeCAD.DocumentObject, /) -> bool:
        """
        canDragAndDropObject(obj) -> bool

        Check whether the child object can be removed from
        other parent and added here by drag and drop.

        obj : App.DocumentObject
            Object to be dragged and dropped.
        """

    def canDragObject(self, obj=None, /) -> bool:
        """
        canDragObject(obj=None) -> bool

        Check whether the child object can be removed by dragging.
        If 'obj' is not given, check without filter by any particular object.

        obj : App.DocumentObject
            Object to be dragged.
        """

    def canDropObject(self, obj=None, owner=None, subname: str = None, elem=None) -> bool:
        """
        canDropObject(obj=None, owner=None, subname, elem=None) -> bool

        Check whether the child object can be added by dropping.
        If 'obj' is not given, check without filter by any particular object.

        obj : App.DocumentObject
            Object to be dropped.
        owner : App.DocumentObject
            Parent object of the dropping object.
        subname : str
            Subname reference to the dropping object. Optional.
        elem : sequence of str
            Non-objects subelements selected when the object is
            being dropped.
        Possible exceptions: (ValueError, TypeError).
        """

    def claimChildren(self) -> list[FreeCAD.DocumentObject | None]:
        """
        claimChildren() -> list

        Returns list of objects that are to be grouped in tree under this object.
        """

    def doubleClicked(self) -> bool:
        """
        doubleClicked() -> bool

        Trigger double clicking the corresponding tree item of this view object.
        """

    def dragObject(self, obj: FreeCAD.DocumentObject, /):
        """
        dragObject(obj) -> None

        Remove a child object by dropping.

        obj : App.DocumentObject
            Object to be dragged.
        """

    def dropObject(self, obj: FreeCAD.DocumentObject, owner=None, subname: str = None, elem=None) -> str:
        """
        dropObject(obj, owner=None, subname, elem=None) -> str

        Add a child object by dropping.

        obj : App.DocumentObject
            Object to be dropped.
        owner : App.DocumentObject
            Parent object of the dropping object.
        subname : str
            Subname reference to the dropping object. Optional.
        elem : sequence of str
            Non-objects subelements selected when the object is
            being dropped.
        Possible exceptions: (TypeError).
        """

    def getBoundingBox(self, subname: str = None, transform: bool = True, pyView=None, /) -> FreeCAD.BoundBox:
        """
        getBoundingBox(subName, transform=True, view) -> Base.BoundBox

        Obtain the bounding box of this view object.

        subName : str
            Name referring a sub-object. Optional.
        transform: bool
            Whether to apply the transformation matrix of this view provider.
        view: View3DInventorPy
            Default to active view. Optional.
        """

    def getDetailPath(self, sub: str, path, append: bool = True, /) -> pivy.coin.SoDetail:
        """
        getDetailPath(subelement, path, append=True) -> coin.SoDetail or None

        Return Coin detail and path of an subelement.

        subname: str
            Dot separated string reference to the sub element.
        pPath: coin.SoPath
            Output coin path leading to the returned element detail.
        append: bool
            If True, path will be first appended with the root node and the mode
            switch node of this view provider.
        """

    def getElementColors(self, element: str = None, /) -> dict[str, tuple[float, float, float, float]]:
        """
        getElementColors(elementName) -> dict

        Get a dictionary of the form {elementName : (r,g,b,a)}.
        If no element name is given a dictionary with all the elements is returned.

        elementName : str
            Name of the element. Optional.
        """

    def getElementPicked(self, obj, /) -> str:
        """
        getElementPicked(pickPoint) -> str

        Return the picked subelement.

        pickPoint : coin.SoPickedPoint
        """

    def hide(self):
        """
        show() -> None

        Hide the object.
        """

    def isVisible(self) -> bool:
        """
        isVisible() -> bool

        Check if the object is visible.
        """

    def listDisplayModes(self) -> list[str]:
        """
        listDisplayModes() -> list

        Show a list of all display modes.
        """

    def partialRender(self, value=None, clear: bool = False, /) -> int:
        """
        partialRender(sub=None, clear=False) -> int

        Render only part of the object.

        sub: None, str, sequence of str
            Refer to the subelement. If it is None then reset the partial rendering.
        clear: bool
            True to add, or False to remove the subelement(s) for rendering.
        """

    def removeProperty(self, sName: str, /) -> bool:
        """
        removeProperty(name) -> bool

        Remove a generic property.
        Only user-defined properties can be removed, not built-in ones.

        name : str
            Property name.
        Possible exceptions: (RuntimeError).
        """

    def replaceObject(self, oldObj: FreeCAD.DocumentObject, newObj: FreeCAD.DocumentObject, /) -> int:
        """
        replaceObject(oldObj, newObj) -> int

        Replace a child object.
        Returns 1 if succeeded, 0 if not found, -1 if not supported.

        oldObj : App.DocumentObject
            Old object.
        newObj : App.DocumentObject
            New object.
        """

    def setElementColors(self, pyObj, /):
        """
        setElementColors(colors) -> None

        Set element colors.

        colors: dict
            Color dictionary of the form {elementName:(r,g,b,a)}.
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def setTransformation(self, p: FreeCAD.Matrix, /): ...

    @typing.overload
    def setTransformation(self, p: FreeCAD.Placement, /):
        """
        setTransformation(trans) -> None

        Set a transformation on the Inventor node.

        trans : Base.Placement, Base.Matrix
        Possible exceptions: (TypeError).
        """

    def show(self):
        """
        show() -> None

        Show the object.
        """

    def signalChangeIcon(self):
        """
        signalChangeIcon() -> None

        Trigger icon changed signal.
        """

    def supportedProperties(self) -> list[str]:
        """
        supportedProperties() -> list

        A list of supported property types.
        """

    def toString(self) -> str:
        """
        toString() -> str

        Return a string representation of the Inventor node.
        """


# ViewProviderLinkPy.xml
class ViewProviderLink(FreeCADGui.ViewProviderDocumentObject):
    """This is the ViewProviderLink class"""

    @property
    def DraggingPlacement(self) -> FreeCAD.Placement:
        """Get/set dragger placement during dragging"""

    @property
    def LinkView(self) -> object:
        """Get the associated LinkView object"""

    @property
    def UseCenterballDragger(self) -> bool:
        """Get/set dragger type"""

    @property
    def ChildViewProvider(self) -> object:
        """Property TypeId: App::PropertyPersistentObject."""

    @ChildViewProvider.setter
    def ChildViewProvider(self, value: str): ...

    @property
    def DrawStyle(self) -> int:
        """
        Property group: Link.
        Property TypeId: App::PropertyEnumeration.
        """

    @DrawStyle.setter
    def DrawStyle(self, value: typing.Literal['None', 'Solid', 'Dashed', 'Dotted', 'Dashdot']): ...

    @property
    def LineWidth(self) -> float:
        """
        Property group: Link.
        Property TypeId: App::PropertyFloatConstraint.
        """

    @LineWidth.setter
    def LineWidth(self, value: float | Quadruple_t[float]): ...

    @property
    def MaterialList(self) -> list[tuple[FreeCAD.Material, ...]]:
        """Property TypeId: App::PropertyMaterialList."""

    @MaterialList.setter
    def MaterialList(self, value: typing.Iterable[FreeCAD.Material] | dict[int, FreeCAD.Material]): ...

    @property
    def OverrideColorList(self) -> list[tuple[float, float, float, float]]:
        """Property TypeId: App::PropertyColorList."""

    @OverrideColorList.setter
    def OverrideColorList(self, value: typing.Iterable[Triple_t[float] | Quadruple_t[float] | int] | dict[int, Triple_t[float] | Quadruple_t[float] | int]): ...

    @property
    def OverrideMaterial(self) -> bool:
        """
        Property group: Link.
        Property TypeId: App::PropertyBool.
        Override linked object's material.
        """

    @OverrideMaterial.setter
    def OverrideMaterial(self, value: int | bool): ...

    @property
    def OverrideMaterialList(self) -> tuple[bool, ...]:
        """Property TypeId: App::PropertyBoolList."""

    @OverrideMaterialList.setter
    def OverrideMaterialList(self, value: typing.Iterable[int | bool] | dict[int, int | bool]): ...

    @property
    def PointSize(self) -> float:
        """
        Property group: Link.
        Property TypeId: App::PropertyFloatConstraint.
        """

    @PointSize.setter
    def PointSize(self, value: float | Quadruple_t[float]): ...

    @property
    def Selectable(self) -> bool:
        """
        Property group: Link.
        Property TypeId: App::PropertyBool.
        """

    @Selectable.setter
    def Selectable(self, value: int | bool): ...

    @property
    def ShapeMaterial(self) -> FreeCAD.Material:
        """
        Property group: Link.
        Property TypeId: App::PropertyMaterial.
        """

    @ShapeMaterial.setter
    def ShapeMaterial(self, value: FreeCAD.Material): ...


# ViewProviderExtensionPy.xml
class ViewProviderExtension(FreeCAD.Extension):
    """Base class for all view provider extensions"""

    def ignoreOverlayIcon(self, name: str = None, /) -> bool:
        """
        Ignore the overlay icon of an extension
        Possible exceptions: (NameError).
        """

    def setIgnoreOverlayIcon(self, ignore: bool, name: str = None, /):
        """
        Ignore the overlay icon of an extension
        Possible exceptions: (NameError).
        """


# CommandPy.xml
class Command(FreeCAD.PyObjectBase):
    """FreeCAD Python wrapper of Command functions"""

    @staticmethod
    def createCustomCommand(macroFile: str, menuText: str = None, toolTip: str = None, whatsThis: str = None, statusTip: str = None, pixmap: str = None, shortcut: str = None) -> str:
        """
        createCustomCommand(macroFile, menuText, toolTip, whatsThis, statusTip, pixmap, shortcut) -> str

        Create a custom command for a macro. Returns name of the created command.

        macroFile : str
            Macro file.
        menuText : str
            Menu text. Optional.
        toolTip : str
            Tool tip text. Optional.
        whatsThis : str
            `What's this?` text. Optional.
        statusTip : str
            Status tip text. Optional.
        pixmap : str
            Pixmap name. Optional.
        shortcut : str
            Shortcut key sequence. Optional.
        """

    @staticmethod
    def findCustomCommand(macroScriptName: str = None, /) -> typing.Any | str:
        """
        findCustomCommand(name) -> str or None

        Given the name of a macro, return the name of the custom command for that macro
        or None if there is no command matching that macro script name.

        name : str
            Macro name.
        """

    @staticmethod
    def get(pName: str, /) -> FreeCADGui.Command:
        """
        get(name) -> Gui.Command or None

        Get a given command by name or None if it doesn't exist.

        name : str
            Command name.
        """

    def getAction(self) -> list[qtpy.QtCore.QObject]:
        """
        getAction() -> list of QAction

        Return the associated QAction object.
        """

    def getInfo(self) -> dict[str, str]:
        """
        getInfo() -> dict

        Return information about this command.
        """

    def getShortcut(self) -> str:
        """
        getShortcut() -> str

        Returns string representing shortcut key accelerator for command.
        """

    def isActive(self) -> bool:
        """
        isActive() -> bool

        Returns True if the command is active, False otherwise.
        """

    @staticmethod
    def listAll() -> list[str]:
        """
        listAll() -> list of str

        Returns the name of all commands.
        """

    @staticmethod
    def listByShortcut(string: str, bIsRegularExp: bool = False, /) -> list[str]:
        """
        listByShortcut(string, useRegExp=False) -> list of str

        Returns a list of all commands, filtered by shortcut.
        Shortcuts are converted to uppercase and spaces removed
        prior to comparison.

        string :  str
            Shortcut to be searched.
        useRegExp : bool
            Filter using regular expression.
        Possible exceptions: (RuntimeError).
        """

    @staticmethod
    def removeCustomCommand(actionName: str = None, /) -> bool:
        """
        removeCustomCommand(name) -> bool

        Remove the custom command if it exists.
        Given the name of a custom command, this removes that command.
        It is not an error to remove a non-existent command, the function
        simply does nothing in that case.
        Returns True if something was removed, or False if not.

        name : str
            Command name.
        """

    def resetShortcut(self) -> bool:
        """
        resetShortcut() -> bool

        Resets shortcut for given command back to the default, returns True for success.
        """

    def run(self, item: int = 0, /):
        """
        run(item=0) -> None

        Runs the given command.

        item : int
            Item to be run.
        """

    def setShortcut(self, pShortcut: str, /) -> bool:
        """
        setShortcut(string) -> bool

        Sets shortcut for given command, returns True for success.

        string : str
            Shortcut to be set.
        """

    @staticmethod
    def update():
        """
        update() -> None

        Update active status of all commands.
        """


# PythonWorkbenchPy.xml
class PythonWorkbench(FreeCADGui.WorkbenchC):
    """This is the class for Python workbenches"""

    def AppendCommandbar(self):
        """deprecated -- use appendCommandBar"""

    def AppendContextMenu(self):
        """deprecated -- use appendContextMenu"""

    def AppendMenu(self):
        """deprecated -- use appendMenu"""

    def AppendToolbar(self):
        """deprecated -- use appendToolbar"""

    def ListCommandbars(self):
        """deprecated -- use listCommandBars"""

    def ListMenus(self):
        """deprecated -- use listMenus"""

    def ListToolbars(self):
        """deprecated -- use listToolbars"""

    def RemoveCommandbar(self):
        """deprecated -- use removeCommandBar"""

    def RemoveContextMenu(self):
        """deprecated -- use removeContextMenu"""

    def RemoveMenu(self):
        """deprecated -- use removeMenu"""

    def RemoveToolbar(self):
        """deprecated -- use removeToolbar"""

    def appendCommandbar(self, psToolBar: str, pObject, /):
        """
        Append a new command bar
        Possible exceptions: (AssertionError).
        """

    def appendContextMenu(self, pPath, pItems, /):
        """
        Append a new context menu item
        Possible exceptions: (AssertionError).
        """

    def appendMenu(self, pPath, pItems, /):
        """
        Append a new menu
        Possible exceptions: (AssertionError).
        """

    def appendToolbar(self, psToolBar: str, pObject, /):
        """
        Append a new toolbar
        Possible exceptions: (AssertionError).
        """

    def removeCommandbar(self, psToolBar: str, /):
        """Remove a command bar"""

    def removeContextMenu(self, psMenu: str, /):
        """Remove a context menu item"""

    def removeMenu(self, psMenu: str, /):
        """Remove a menu"""

    def removeToolbar(self, psToolBar: str, /):
        """Remove a toolbar"""


# AxisOriginPy.xml
class AxisOrigin(FreeCAD.BaseClass):
    """
    Gui.AxisOrigin class.

    Class for creating a Coin3D representation of a coordinate system.
    """

    def __init__(self):
        """
        Gui.AxisOrigin class.

        Class for creating a Coin3D representation of a coordinate system.
        """

    @property
    def AxisLength(self) -> float:
        """Get/set the axis length."""

    @property
    def Labels(self) -> dict[str, str]:
        """
        Get/set axis component names as a dictionary.
        Available keys are:
        'O': origin
        'X': x axis
        'Y': y axis
        'Z': z axis
        'XY': xy plane
        'XZ': xz plane
        'YZ': yz plane
        """

    @property
    def LineWidth(self) -> float:
        """Get/set the axis line width for rendering."""

    @property
    def Node(self) -> pivy.coin.SoGroup:
        """Get the Coin3D node."""

    @property
    def Plane(self) -> tuple[float, float]:
        """Get/set axis plane size and distance to axis line."""

    @property
    def PointSize(self) -> float:
        """Get/set the origin point size for rendering."""

    @property
    def Scale(self) -> float:
        """Get/set auto scaling factor, 0 to disable."""

    def getDetailPath(self, sub: str, path, /) -> pivy.coin.SoDetail:
        """
        getDetailPath(subname, path) -> coin.SoDetail or None

        Returns Coin detail of a subelement.
        Note: Not fully implemented. Currently only returns None.

        subname : str
            String reference to the subelement.
        path: coin.SoPath
            Output Coin path leading to the returned element detail.
        Possible exceptions: (TypeError).
        """

    def getElementPicked(self, obj, /) -> str:
        """
        getElementPicked(pickedPoint) -> str

        Returns the picked element name.

        pickedPoint : coin.SoPickedPoint
        Possible exceptions: (TypeError).
        """


# ViewProviderDocumentObjectPy.xml
class ViewProviderDocumentObject(FreeCADGui.ViewProvider):
    """This is the ViewProvider base class"""

    @property
    def Proxy(self) -> FreeCADTemplates.ViewProviderPython: ...

    @Proxy.setter
    def Proxy(self, value: FreeCADTemplates.ViewProviderPython): ...

    @property
    def Document(self) -> FreeCADGui.Document:
        """Return the document the view provider is part of"""

    @property
    def ForceUpdate(self) -> bool:
        """Reference count to force update visual"""

    @property
    def Object(self) -> FreeCAD.DocumentObject:
        """Set/Get the associated data object"""

    @property
    def DisplayMode(self) -> int:
        """
        Property group: Display Options.
        Property TypeId: App::PropertyEnumeration.
        Set the display mode.
        """

    @DisplayMode.setter
    def DisplayMode(self, value): ...

    @property
    def OnTopWhenSelected(self) -> int:
        """
        Property group: Selection.
        Property TypeId: App::PropertyEnumeration.

        Enabled: Display the object on top of any other object when selected
        Object: On top only if the whole object is selected
        Element: On top only if some sub-element of the object is selected.
        """

    @OnTopWhenSelected.setter
    def OnTopWhenSelected(self, value: typing.Literal['Disabled', 'Enabled', 'Object', 'Element']): ...

    @property
    def SelectionStyle(self) -> int:
        """
        Property group: Selection.
        Property TypeId: App::PropertyEnumeration.
        Set the object selection style.
        """

    @SelectionStyle.setter
    def SelectionStyle(self, value: typing.Literal['Shape', 'BoundBox']): ...

    @property
    def ShowInTree(self) -> bool:
        """
        Property group: Display Options.
        Property TypeId: App::PropertyBool.
        Show the object in the tree view.
        """

    @ShowInTree.setter
    def ShowInTree(self, value: int | bool): ...

    @property
    def Visibility(self) -> bool:
        """
        Property group: Display Options.
        Property TypeId: App::PropertyBool.
        Show the object in the 3d view.
        """

    @Visibility.setter
    def Visibility(self, value: int | bool): ...

    def update(self):
        """Update the view representation of the object"""


# SelectionObjectPy.xml
class SelectionObject(FreeCAD.BaseClass):
    """This class represents selections made by the user. It holds information about the object, document and sub-element of the selection."""

    @property
    def Document(self) -> FreeCADGui.Document:
        """Document of the selected object"""

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
    def Object(self) -> FreeCAD.DocumentObject:
        """Selected object"""

    @property
    def ObjectName(self) -> str:
        """Name of the selected object"""

    @property
    def PickedPoints(self) -> tuple[FreeCAD.Vector, ...]:
        """Picked points for selection"""

    @property
    def SubElementNames(self) -> tuple[str, ...]:
        """Name of the selected sub-element if any"""

    @property
    def SubObjects(self) -> tuple[typing.Any, ...]:
        """Selected sub-element, if any"""

    @property
    def TypeName(self) -> str:
        """Type name of the selected object"""

    def isObjectTypeOf(self, type: str, /) -> bool:
        """
        Test for a certain father class.
        isObjectTypeOf(type) -> Bool

        Possible exceptions: (TypeError).
        """

    def remove(self):
        """
        Remove this selection item from the selection.
        remove() -> None
        --
        This object becomes invalid.
        """


# DocumentPy.xml
class Document(FreeCAD.Persistence):
    """This is a Document class"""

    @property
    def ActiveObject(self) -> FreeCADGui.ViewProvider | None:
        """The active object of the document."""

    @ActiveObject.setter
    def ActiveObject(self, value: FreeCADGui.ViewProvider | None): ...

    @property
    def ActiveView(self) -> FreeCADGui.MDIViewPy | FreeCADGui.View3DInventorPy | None:
        """The active view of the document."""

    @ActiveView.setter
    def ActiveView(self, value: FreeCADGui.MDIViewPy | FreeCADGui.View3DInventorPy | None): ...

    @property
    def Document(self) -> FreeCAD.Document:
        """The related App document to this Gui document."""

    @property
    def EditMode(self) -> int:
        """Current edit mode. Only meaningful when there is a current object in edit."""

    @property
    def EditingTransform(self) -> FreeCAD.Matrix:
        """The editing transformation matrix."""

    @property
    def InEditInfo(self) -> tuple[typing.Any, str, str, int] | None:
        """A tuple(obj,subname,subElement,editMode) of editing object reference, or None if no object is in edit."""

    @property
    def Modified(self) -> bool:
        """Returns True if the document is marked as modified, and False otherwise."""

    @property
    def Transacting(self) -> bool:
        """Indicate whether the document is undoing/redoing."""

    def activeObject(self) -> FreeCADGui.ViewProvider:
        """
        activeObject() -> object or None

        The active object of the document. Deprecated, use ActiveObject.
        """

    def activeView(self) -> FreeCADGui.MDIViewPy:
        """
        activeView() -> object or None

        The active view of the document. Deprecated, use ActiveView.
        """

    def addAnnotation(self, psAnnoName: str, psFileName: str, psModName: str = None, /):
        """
        addAnnotation(annoName, fileName, modName) -> None

        Add an Inventor object from a file.

        annoName : str
            Annotation name.
        fileName : str
            File name.
        modName : str
            Display mode name. Optional.
        """

    def getInEdit(self) -> FreeCADGui.ViewProvider:
        """
        getInEdit() -> Gui.ViewProviderDocumentObject or None

        Returns the current object in edit mode or None if there is no such object.
        """

    def getObject(self, sName: str, /) -> FreeCADGui.ViewProvider:
        """
        getObject(objName) -> object or None

        Return the object with the given name. If no one exists, return None.

        ObjName : str
            Object name.
        """

    def hide(self, psFeatStr: str, /):
        """
        hide(objName) -> None

        Hide an object.

        objName : str
            Name of the `Gui.ViewProvider` to hide.
        """

    def mdiViewsOfType(self, sType: str, /) -> list:
        """
        mdiViewsOfType(type) -> list of MDIView

        Return a list of mdi views of a given type.

        type : str
            Type name.
        """

    def mergeProject(self, filename: str, /):
        """
        mergeProject(fileName) -> None

        Merges this document with another project file.

        fileName : str
            File name.
        """

    def resetEdit(self):
        """
        resetEdit() -> None

        End the current editing.
        """

    def save(self) -> bool:
        """
        save() -> bool

        Attempts to save the document
        """

    def saveAs(self) -> bool:
        """
        saveAs() -> bool

        Attempts to save the document under a new name
        """

    def scrollToTreeItem(self, view: FreeCADGui.ViewProviderDocumentObject, /):
        """
        scrollToTreeItem(obj) -> None

        Scroll the tree view to the item of a view object.

        obj : Gui.ViewProviderDocumentObject
        """

    def sendMsgToViews(self, msg: str, /):
        """
        sendMsgToViews(msg) -> None

        Send a message to all views of the document.

        msg : str
        """

    @typing.overload
    def setEdit(self, psFeatStr: str, mod: int = 0, subname: str = None, /) -> bool: ...

    @typing.overload
    def setEdit(self, pyObj, mod: int = 0, subname: str = None, /) -> bool:
        """
        setEdit(obj, mod=0, subName) -> bool

        Set an object in edit mode.

        obj : str, App.DocumentObject, Gui.ViewPrivider
            Object to set in edit mode.
        mod : int
            Edit mode.
        subName : str
            Subelement name. Optional.
        Possible exceptions: (TypeError, ValueError).
        """

    def setPos(self, psFeatStr: str, pcMatObj: FreeCAD.Matrix, /):
        """
        setPos(objName, matrix) -> None

        Set the position of an object.

        objName : str
            Name of the `Gui.ViewProvider`.

        matrix : Base.Matrix
            Transformation to apply on the object.
        """

    def show(self, psFeatStr: str, /):
        """
        show(objName) -> None

        Show an object.

        objName : str
            Name of the `Gui.ViewProvider` to show.
        """

    def toggleInSceneGraph(self, view: FreeCADGui.ViewProvider, /):
        """
        toggleInSceneGraph(obj) -> None

        Add or remove view object from scene graph of all views depending
        on its canAddToSceneGraph().

        obj : Gui.ViewProvider
        """

    def toggleTreeItem(self, object: FreeCAD.DocumentObject, mod: int = 0, subname: str = None, /):
        """
        toggleTreeItem(obj, mod=0, subName) -> None

        Change TreeItem of a document object.

        obj : App.DocumentObject
        mod : int
            Item mode.
            0: Toggle, 1: Collapse, 2: Expand, 3: Expand path.
        subName : str
            Subelement name. Optional.
        Possible exceptions: (ValueError).
        """

    def update(self):
        """
        update() -> None

        Update the view representations of all objects.
        """


# MDIViewPy.cpp
class MDIViewPy(qtpy.QtWidgets.QMainWindow):
    """Python binding class for the MDI view class"""

    def printView(self) -> None:
        """
        printView()
        Possible exceptions: (Exception).
        """

    def printPdf(self) -> None:
        """
        printPdf()
        Possible exceptions: (Exception).
        """

    def printPreview(self) -> None:
        """
        printPreview()
        Possible exceptions: (Exception).
        """

    def undoActions(self) -> list[str]:
        """
        undoActions()
        Possible exceptions: (Exception).
        """

    def redoActions(self) -> list[str]:
        """
        redoActions()
        Possible exceptions: (Exception).
        """

    def message(self, psMsgStr: str, /) -> bool:
        """
        deprecated: use sendMessage
        Possible exceptions: (Exception, RuntimeError).
        """

    def sendMessage(self, psMsgStr: str, /) -> bool:
        """
        sendMessage(str)
        Possible exceptions: (Exception, RuntimeError).
        """

    def supportMessage(self, psMsgStr: str, /) -> bool:
        """
        supportMessage(str)
        Possible exceptions: (Exception, RuntimeError).
        """

    def fitAll(self) -> None:
        """
        fitAll()
        Possible exceptions: (Exception, RuntimeError).
        """

    def setActiveObject(self, name: str, docObject=None, subname: str = None, /) -> None:
        """
        setActiveObject(name,object,subname=None)
        add or set a new active object
        Possible exceptions: (Exception).
        """

    def getActiveObject(self, name: str, resolve: bool = True, /) -> FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, FreeCAD.DocumentObject, str] | None:
        """
        getActiveObject(name,resolve=True)
        returns the active object for the given type
        Possible exceptions: (Exception).
        """

    def cast_to_base(self) -> FreeCADGui.MDIViewPy:
        """cast_to_base() cast to MDIView class"""


# Application.cpp
def subgraphFromObject(o: FreeCAD.DocumentObject, /) -> typing.Any | None:
    """
    subgraphFromObject(object) -> Node

    Return the Inventor subgraph to an object
    Possible exceptions: (RuntimeError).
    """


def exportSubgraph(proxy, output, format: str = 'VRML', /) -> None:
    """
    exportSubgraph(Node, File or Buffer, [Format='VRML']) -> None

    Exports the sub-graph in the requested formatThe format string can be VRML or IV
    Possible exceptions: (RuntimeError).
    """


def getSoDBVersion() -> str:
    """
    getSoDBVersion() -> String

    Return a text string containing the name
    of the Coin library and version information
    """


# View3DPy.cpp
class View3DInventorPy:
    """Python binding class for the Inventor viewer class"""

    def fitAll(self, factor: float = 1.0, /) -> None:
        """
        fitAll()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewBottom(self) -> None:
        """
        viewBottom()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewFront(self) -> None:
        """
        viewFront()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewLeft(self) -> None:
        """
        viewLeft()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewRear(self) -> None:
        """
        viewRear()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewRight(self) -> None:
        """
        viewRight()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewTop(self) -> None:
        """
        viewTop()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewAxometric(self) -> None:
        """
        viewAxonometric()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewAxonometric(self) -> None:
        """
        viewAxonometric()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewIsometric(self) -> None:
        """
        viewIsometric()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewDimetric(self) -> None:
        """
        viewDimetric()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewTrimetric(self) -> None:
        """
        viewTrimetric()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewDefaultOrientation(self, view: str = '', scale: float = -1.0, /) -> None:
        """
        viewDefaultOrientation(ori_str = '', scale = -1.0): sets camera rotation to a predefined one, 
        and camera position and zoom to show certain amount of model space. 
        ori_string can be 'Top', 'Bottom', 'Front', 'Rear', 'Left', 'Right', 
        'Isometric', 'Dimetric', 'Trimetric', 'Custom'. If empty, the value is 
        fetched from Parameters.
        scale sets distance from camera to origin, and height of the screen in 
        model space, so that a sphere of diameter <scale> fits the height of the
        viewport. If zero, scaling is not done. If negative, the value is 
        fetched from Parameters.
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewRotateLeft(self) -> None:
        """
        viewRotateLeft()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewRotateRight(self) -> None:
        """
        viewRotateRight()
        Possible exceptions: (Exception, RuntimeError).
        """

    def zoomIn(self) -> None:
        """
        zoomIn()
        Possible exceptions: (Exception, RuntimeError).
        """

    def zoomOut(self) -> None:
        """
        zoomOut()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewPosition(self, p: FreeCAD.Placement = None, steps: int = 20, ms: int = 30, /) -> FreeCAD.Placement | None:
        """
        viewPosition()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def startAnimating(self): ...

    @typing.overload
    def startAnimating(self, x: float, y: float, z: float, velocity: float, /) -> None:
        """
        startAnimating()
        Possible exceptions: (Exception).
        """

    def stopAnimating(self) -> None:
        """
        stopAnimating()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def setAnimationEnabled(self): ...

    @typing.overload
    def setAnimationEnabled(self, ok: int, /) -> None:
        """
        setAnimationEnabled()
        Possible exceptions: (Exception).
        """

    def isAnimationEnabled(self) -> bool:
        """
        isAnimationEnabled()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def setPopupMenuEnabled(self): ...

    @typing.overload
    def setPopupMenuEnabled(self, ok: int, /) -> None:
        """
        setPopupMenuEnabled()
        Possible exceptions: (Exception).
        """

    def isPopupMenuEnabled(self) -> bool:
        """
        isPopupMenuEnabled()
        Possible exceptions: (Exception).
        """

    def dump(self, filename: str, onlyVisible: bool = False, /) -> None:
        """
        dump(filename, [onlyVisible=False])
        Possible exceptions: (Exception, RuntimeError).
        """

    def dumpNode(self, object, /) -> str:
        """
        dumpNode(node)
        Possible exceptions: (Exception, RuntimeError).
        """

    @typing.overload
    def setStereoType(self, stereomode: int = -1, /) -> None: ...

    @typing.overload
    def setStereoType(self, modename: str, /) -> None:
        """
        setStereoType()
        Possible exceptions: (Exception, NameError, IndexError, RuntimeError).
        """

    def getStereoType(self) -> str:
        """
        getStereoType()
        Possible exceptions: (Exception, ValueError, RuntimeError).
        """

    def listStereoTypes(self) -> list:
        """
        listStereoTypes()
        Possible exceptions: (Exception, RuntimeError).
        """

    @typing.overload
    def saveImage(self): ...

    @typing.overload
    def saveImage(self, cFileName: str, w: int = -1, h: int = -1, cColor: str = 'Current', cComment: str = '$MIBA', s: int = None, /) -> None:
        """
        saveImage()
        Possible exceptions: (Exception, RuntimeError).
        """

    @typing.overload
    def saveVectorGraphic(self): ...

    @typing.overload
    def saveVectorGraphic(self, filename: str, ps: int = 4, name: str = 'white', /) -> None:
        """
        saveVectorGraphic()
        Possible exceptions: (Exception, RuntimeError).
        """

    def getCamera(self) -> str:
        """
        getCamera()
        Possible exceptions: (Exception, RuntimeError).
        """

    def getCameraNode(self):
        """
        getCameraNode()
        Possible exceptions: (Exception, RuntimeError).
        """

    def getViewDirection(self) -> FreeCAD.Vector:
        """
        getViewDirection() --> tuple of floats
        returns the direction vector the view is currently pointing at as tuple with xyz values

        Possible exceptions: (Exception, RuntimeError).
        """

    def setViewDirection(self, object, /) -> None:
        """
        setViewDirection(tuple) --> None
        Sets the direction the view is pointing at. The direction must be given as tuple with
        three coordinates xyz
        Possible exceptions: (Exception, ValueError, RuntimeError).
        """

    @typing.overload
    def setCamera(self): ...

    @typing.overload
    def setCamera(self, buffer: str, /) -> None:
        """
        setCamera()
        Possible exceptions: (Exception, RuntimeError).
        """

    @typing.overload
    def setCameraOrientation(self): ...

    @typing.overload
    def setCameraOrientation(self, o, m: bool = False, /) -> None:
        """
        setCameraOrientation()
        Possible exceptions: (Exception, ValueError, RuntimeError).
        """

    def getCameraOrientation(self) -> FreeCAD.Rotation:
        """
        getCameraOrientation()
        Possible exceptions: (Exception).
        """

    def getCameraType(self) -> str:
        """
        getCameraType()
        Possible exceptions: (Exception, RuntimeError, TypeError).
        """

    @typing.overload
    def setCameraType(self, cameratype: int = -1, /) -> None: ...

    @typing.overload
    def setCameraType(self, modename: str, /) -> None:
        """
        setCameraType()
        Possible exceptions: (Exception, NameError, IndexError).
        """

    def listCameraTypes(self) -> list:
        """
        listCameraTypes()
        Possible exceptions: (Exception, RuntimeError).
        """

    def getCursorPos(self) -> tuple[int, int]:
        """
        getCursorPos() -> tuple of integers

        Return the current cursor position relative to the coordinate system of the
        viewport region.

        Possible exceptions: (Exception).
        """

    def getObjectInfo(self, object, r: float = None, /) -> ReturnGetObjectInfoDict | None:
        """
        getObjectInfo(tuple(int,int), [pick_radius]) -> dictionary or None

        Return a dictionary with the name of document, object and component. The
        dictionary also contains the coordinates of the appropriate 3d point of
        the underlying geometry in the scenegraph.
        If no geometry was found 'None' is returned, instead.

        Possible exceptions: (Exception).
        """

    def getObjectsInfo(self, object, r: float = None, /) -> ReturnGetObjectsInfoDict | list[ReturnGetObjectsInfoDict] | None:
        """
        getObjectsInfo(tuple(int,int), [pick_radius]) -> dictionary or None

        Does the same as getObjectInfo() but returns a list of dictionaries or None.

        Possible exceptions: (Exception).
        """

    def getSize(self) -> tuple[int, int]:
        """
        getSize()
        Possible exceptions: (Exception).
        """

    def getPoint(self, x: int, y: int, /) -> FreeCAD.Vector:
        """
        Same as getPointOnFocalPlane
        Possible exceptions: (RuntimeError).
        """

    @typing.overload
    def getPointOnFocalPlane(self, pixel_coords_as_integer_, /): ...

    @typing.overload
    def getPointOnFocalPlane(self, x: int, y: int, /) -> FreeCAD.Vector:
        """
        getPointOnFocalPlane(pixel coords (as integer)) -> 3D vector

        Return the according 3D point on the focal plane to the given 2D point (in
        pixel coordinates).

        Possible exceptions: (RuntimeError).
        """

    @typing.overload
    def getPointOnScreen(self, v: FreeCAD.Vector, /) -> tuple[int, int]: ...

    @typing.overload
    def getPointOnScreen(self, vx: float, vy: float, vz: float, /) -> tuple[int, int]:
        """
        getPointOnScreen(3D vector) -> pixel coords (as integer)

        Return the projected 3D point (in pixel coordinates).

        Possible exceptions: (TypeError, RuntimeError).
        """

    @typing.overload
    def projectPointToLine(self, pixel_coords_as_integer_, /): ...

    @typing.overload
    def projectPointToLine(self, x: int, y: int, /) -> tuple[FreeCAD.Vector, FreeCAD.Vector]:
        """
        projectPointToLine(pixel coords (as integer)) -> line defined by two points

        Return the projecting 3D line to the given 2D point
        Possible exceptions: (RuntimeError).
        """

    @typing.overload
    def addEventCallback(self): ...

    @typing.overload
    def addEventCallback(self, eventtype: str, method, /) -> typing.Callable:
        """
        addEventCallback()
        Possible exceptions: (Exception, TypeError).
        """

    @typing.overload
    def removeEventCallback(self): ...

    @typing.overload
    def removeEventCallback(self, eventtype: str, method, /) -> None:
        """
        removeEventCallback()
        Possible exceptions: (Exception, RuntimeError, TypeError).
        """

    @typing.overload
    def setAnnotation(self): ...

    @typing.overload
    def setAnnotation(self, psAnnoName: str, psBuffer: str, /) -> None:
        """
        setAnnotation()
        Possible exceptions: (Exception, RuntimeError).
        """

    @typing.overload
    def removeAnnotation(self): ...

    @typing.overload
    def removeAnnotation(self, psAnnoName: str, /) -> None:
        """
        removeAnnotation()
        Possible exceptions: (Exception, KeyError).
        """

    def getSceneGraph(self) -> pivy.coin.SoSeparator:
        """
        getSceneGraph()
        Possible exceptions: (Exception, RuntimeError).
        """

    def getViewer(self) -> FreeCADGui.View3DInventorViewerPy:
        """
        getViewer()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def addEventCallbackPivy(self): ...

    @typing.overload
    def addEventCallbackPivy(self, proxy, method, ex: int = 1, /) -> typing.Callable:
        """
        addEventCallbackPivy()
        Possible exceptions: (Exception, RuntimeError, TypeError).
        """

    @typing.overload
    def removeEventCallbackPivy(self): ...

    @typing.overload
    def removeEventCallbackPivy(self, proxy, method, ex: int = 1, /) -> typing.Callable:
        """
        removeEventCallbackPivy()
        Possible exceptions: (Exception, RuntimeError, TypeError).
        """

    def addEventCallbackSWIG(self, proxy, method, ex: int = 1, /) -> typing.Callable:
        """
        Deprecated -- use addEventCallbackPivy()
        Possible exceptions: (Exception, RuntimeError, TypeError).
        """

    def removeEventCallbackSWIG(self, proxy, method, ex: int = 1, /) -> typing.Callable:
        """
        Deprecated -- use removeEventCallbackPivy()
        Possible exceptions: (Exception, RuntimeError, TypeError).
        """

    def listNavigationTypes(self) -> list[str]:
        """listNavigationTypes()"""

    def getNavigationType(self) -> str:
        """getNavigationType()"""

    @typing.overload
    def setNavigationType(self): ...

    @typing.overload
    def setNavigationType(self, style: str, /) -> None:
        """
        setNavigationType()
        Possible exceptions: (Exception).
        """

    def setAxisCross(self, ok: int, /) -> None:
        """
        switch the big axis-cross on and off
        Possible exceptions: (Exception).
        """

    def hasAxisCross(self) -> bool:
        """
        check if the big axis-cross is on or off()
        Possible exceptions: (Exception).
        """

    def addDraggerCallback(self, dragger, type: str, method, /) -> typing.Callable:
        """
        addDraggerCallback(SoDragger, String CallbackType, function)
        Add a DraggerCalback function to the coin node
        Possibles types :
        'addFinishCallback','addStartCallback','addMotionCallback','addValueChangedCallback'

        Possible exceptions: (Exception, TypeError).
        """

    def removeDraggerCallback(self, dragger, type: str, method, /) -> typing.Callable:
        """
        removeDraggerCallback(SoDragger, String CallbackType, function)
        Remove the DraggerCalback function from the coin node
        Possibles types :
        'addFinishCallback','addStartCallback','addMotionCallback','addValueChangedCallback'

        Possible exceptions: (Exception, TypeError).
        """

    def setActiveObject(self, name: str, docObject=None, subname: str = None, /) -> None:
        """
        setActiveObject(name,object,subname=None)
        add or set a new active object
        Possible exceptions: (Exception).
        """

    def getActiveObject(self, name: str, resolve: bool = True, /) -> FreeCAD.DocumentObject | tuple[FreeCAD.DocumentObject, FreeCAD.DocumentObject, str] | None:
        """
        getActiveObject(name,resolve=True)
        returns the active object for the given type
        Possible exceptions: (Exception).
        """

    def getViewProvidersOfType(self, name: str, /) -> list:
        """
        getViewProvidersOfType(name)
        returns a list of view providers for the given type
        Possible exceptions: (Exception).
        """

    def redraw(self) -> None:
        """
        redraw(): renders the scene on screen (useful for animations)
        Possible exceptions: (Exception).
        """

    def setName(self, buffer: str, /) -> None:
        """
        setName(str): sets a name to this viewer
        The name sets the widget's windowTitle and appears on the viewer tab
        Possible exceptions: (Exception, RuntimeError).
        """

    def hasClippingPlane(self) -> bool:
        """
        hasClippingPlane(): check whether this clipping plane is active
        Possible exceptions: (Exception).
        """

    def graphicsView(self) -> qtpy.QtWidgets.QGraphicsView:
        """
        graphicsView(): Access this view as QGraphicsView
        Possible exceptions: (Exception).
        """

    def setCornerCrossVisible(self, ok: int, /) -> None:
        """
        setCornerCrossVisible(bool): Defines corner axis cross visibility
        Possible exceptions: (Exception).
        """

    def isCornerCrossVisible(self) -> bool:
        """
        isCornerCrossVisible(): Returns current corner axis cross visibility
        Possible exceptions: (Exception).
        """

    def setCornerCrossSize(self, size: int = 0, /) -> None:
        """
        setCornerCrossSize(int): Defines corner axis cross size
        Possible exceptions: (Exception).
        """

    def getCornerCrossSize(self) -> int:
        """
        getCornerCrossSize(): Returns current corner axis cross size
        Possible exceptions: (Exception).
        """

    def cast_to_base(self):
        """cast_to_base() cast to MDIView class"""

    @typing.overload
    def boxZoom(self): ...

    @typing.overload
    def boxZoom(self, XMin: int, YMin: int, XMax: int, YMax: int) -> None:
        """
        boxZoom()
        Possible exceptions: (Exception).
        """

    def toggleClippingPlane(self, toggle: int = -1, beforeEditing: bool = False, noManip: bool = True, pla: FreeCAD.Placement = None) -> None:
        """
        toggleClippingPlane(toggle=-1, beforeEditing=False, noManip=True, pla=App.Placement()
        Toggle a global clipping plane

        toggle: -1 toggle, 1 show, 0 hide
        beforeEditing: whether to insert the clipping node before or after editing root node
        noManip: whether to create a manipulator
        pla: clipping plane placement
        Possible exceptions: (Exception).
        """


# WidgetFactory.cpp
class PyResource:
    """PyResource"""

    def value(self, psName: str, psProperty: str, /) -> list | str | float | bool | int | None:
        """Possible exceptions: (Exception)."""

    def setValue(self, psName: str, psProperty: str, psValue, /) -> None:
        """Possible exceptions: (Exception, TypeError)."""

    def show(self) -> None: ...

    def connect(self): ...


# MainWindowPy.cpp
class MainWindowPy(qtpy.QtWidgets.QMainWindow):
    """Python binding class for the MainWindow class"""

    def getWindows(self) -> list:
        """
        getWindows()
        Possible exceptions: (Exception).
        """

    def getWindowsOfType(self, t: FreeCAD.TypeId, /) -> list:
        """
        getWindowsOfType(typeid)
        Possible exceptions: (Exception).
        """

    def setActiveWindow(self, MDIView, /) -> None:
        """setActiveWindow(MDIView)"""

    def getActiveWindow(self) -> MDIViewPy | None:
        """
        getActiveWindow()
        Possible exceptions: (Exception).
        """

    def addWindow(self, obj, /) -> typing.Any | None:
        """
        addWindow(MDIView)
        Possible exceptions: (Exception).
        """

    def removeWindow(self, obj, /) -> None:
        """
        removeWindow(MDIView)
        Possible exceptions: (Exception).
        """


# SoFCOffscreenRenderer.cpp
class SoQtOffscreenRenderer:
    """Python interface for SoQtOffscreenRenderer"""

    def setViewportRegion(self, w: int, h: int, /) -> None:
        """
        setViewportRegion(int, int)
        Possible exceptions: (Exception).
        """

    def getViewportRegion(self) -> tuple[int, int]:
        """
        getViewportRegion() -> tuple
        Possible exceptions: (Exception).
        """

    def setBackgroundColor(self, r: float, g: float, b: float, a: float = 1.0, /) -> None:
        """
        setBackgroundColor(float, float, float, [float])
        Possible exceptions: (Exception).
        """

    def getBackgroundColor(self) -> tuple[float, float, float, float]:
        """
        getBackgroundColor() -> tuple
        Possible exceptions: (Exception).
        """

    def setNumPasses(self, num: int, /) -> None:
        """
        setNumPasses(int)
        Possible exceptions: (Exception).
        """

    def getNumPasses(self) -> int:
        """
        getNumPasses() -> int
        Possible exceptions: (Exception).
        """

    def setInternalTextureFormat(self, format: int, /) -> None:
        """
        setInternalTextureFormat(int)
        Possible exceptions: (Exception).
        """

    def getInternalTextureFormat(self) -> int:
        """
        getInternalTextureFormat() -> int
        Possible exceptions: (Exception).
        """

    def render(self, proxy, /) -> bool:
        """
        render(node)
        Possible exceptions: (Exception).
        """

    def writeToImage(self, filename: str, /) -> None:
        """
        writeToImage(string)
        Possible exceptions: (Exception).
        """

    def getWriteImageFiletypeInfo(self) -> tuple[str, ...]:
        """
        getWriteImageFiletypeInfo() -> tuple
        Possible exceptions: (Exception).
        """


# UiLoader.cpp
class UiLoader:
    """UiLoader to create widgets"""

    @typing.overload
    def load(self, string, /, QWidget_parent=None) -> qtpy.QtWidgets.QWidget | None: ...

    @typing.overload
    def load(self, QIODevice, /, QWidget_parent=None) -> qtpy.QtWidgets.QWidget | None:
        """
        load(string, QWidget parent=None) -> QWidget
        load(QIODevice, QWidget parent=None) -> QWidget
        Possible exceptions: (RuntimeError, TypeError).
        """

    def createWidget(self):
        """createWidget()"""


# PythonConsolePy.cpp
class PythonStdout:
    """Redirection of stdout to FreeCAD's Python console window"""

    def isatty(self) -> bool:
        """isatty()"""

    @typing.overload
    def write(self): ...

    @typing.overload
    def write(self, output: str, /) -> None:
        """
        write()
        Possible exceptions: (TypeError).
        """

    def flush(self) -> None:
        """flush()"""


class PythonStderr:
    """Redirection of stdout to FreeCAD's Python console window"""

    def isatty(self) -> bool:
        """isatty()"""

    @typing.overload
    def write(self): ...

    @typing.overload
    def write(self, output: str, /) -> None:
        """
        write()
        Possible exceptions: (TypeError).
        """

    def flush(self) -> None:
        """flush()"""


class OutputStdout:
    """Redirection of stdout to FreeCAD's report view"""

    def isatty(self) -> bool:
        """isatty()"""

    @typing.overload
    def write(self): ...

    @typing.overload
    def write(self, output: str, /) -> None:
        """
        write()
        Possible exceptions: (TypeError).
        """

    def flush(self) -> None:
        """flush()"""


class OutputStderr:
    """Redirection of stdout to FreeCAD's report view"""

    def isatty(self) -> bool:
        """isatty()"""

    @typing.overload
    def write(self): ...

    @typing.overload
    def write(self, output: str, /) -> None:
        """
        write()
        Possible exceptions: (TypeError).
        """

    def flush(self) -> None:
        """flush()"""


class PythonStdin:
    """Redirection of stdin to FreeCAD to open an input dialog"""

    def readline(self) -> str:
        """readline()"""


# SplitView3DInventor.cpp
class AbstractSplitViewPy:
    """Python binding class for the Inventor viewer class"""

    def fitAll(self) -> None:
        """
        fitAll()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewBottom(self) -> None:
        """
        viewBottom()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewFront(self) -> None:
        """
        viewFront()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewLeft(self) -> None:
        """
        viewLeft()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewRear(self) -> None:
        """
        viewRear()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewRight(self) -> None:
        """
        viewRight()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewTop(self) -> None:
        """
        viewTop()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewAxometric(self) -> None:
        """
        viewAxometric()
        Possible exceptions: (Exception, RuntimeError).
        """

    def viewIsometric(self) -> None:
        """
        viewIsometric()
        Possible exceptions: (Exception, RuntimeError).
        """

    def getViewer(self, viewIndex: int, /) -> FreeCADGui.View3DInventorViewerPy:
        """
        getViewer(index)
        Possible exceptions: (Exception, IndexError, RuntimeError).
        """

    def close(self) -> None:
        """
        close()
        Possible exceptions: (Exception).
        """

    def cast_to_base(self):
        """cast_to_base() cast to MDIView class"""


# SelectionFilter.cpp
class SelectionFilter:
    """
    Filter for certain selection
    Example strings are:
    "SELECT Part::Feature SUBELEMENT Edge",
    "SELECT Part::Feature", 
    "SELECT Part::Feature COUNT 1..5"
    """

    def match(self) -> bool:
        """
        Check if the current selection matches the filter
        Possible exceptions: (Exception).
        """

    def result(self) -> list[tuple[FreeCADGui.SelectionObject, ...]]:
        """If match() returns True then with result() you get a list of the matching objects"""

    def test(self, pcObj: FreeCAD.DocumentObject, text: str = '', /) -> bool:
        """
        test(Feature, SubName='')
        Test if a given object is described in the filter.
        If SubName is not empty the sub-element gets also tested.
        Possible exceptions: (Exception).
        """

    def setFilter(self, text: str = None, /) -> None:
        """
        Set a new selection filter
        Possible exceptions: (Exception, SyntaxError).
        """


# PythonDebugger.cpp
class PythonDebugStdout:
    """Redirection of stdout to FreeCAD's Python debugger window"""

    def write(self, msg: str, /) -> None:
        """
        write to stdout
        Possible exceptions: (Exception).
        """

    def flush(self) -> None:
        """flush the output"""


class PythonDebugStderr:
    """Redirection of stderr to FreeCAD's Python debugger window"""

    def write(self, msg: str, /) -> None:
        """
        write to stderr
        Possible exceptions: (Exception).
        """


class PythonDebugExcept:
    """Custom exception handler"""

    def fc_excepthook(self) -> None:
        """
        Custom exception handler
        Possible exceptions: (Exception).
        """


# ApplicationPy.cpp
def activateWorkbench(psKey: str, /) -> bool:
    """
    activateWorkbench(name) -> bool

    Activate workbench by its name. Return False if the workbench is
    already active.

    name : str
        Name of the workbench to activate.
    Possible exceptions: (Exception, RuntimeError, FreeCAD.Base.FreeCADError).
    """


def addWorkbench(pcObject, /):
    """
    addWorkbench(workbench) -> None

    Add a workbench.

    workbench : Workbench, Workbench type
        Instance of a Workbench subclass or subclass of the
        Workbench class.
    Possible exceptions: (TypeError).
    """


def removeWorkbench(psKey: str, /):
    """
    removeWorkbench(name) -> None

    Remove a workbench.

    name : str
        Name of the workbench to remove.
    """


def getWorkbench(psKey: str, /):
    """
    getWorkbench(name) -> Workbench

    Get the workbench by its name.

    name : str
        Name of the workbench to return.
    """


def listWorkbenches():
    """
    listWorkbenches() -> dict

    Get a dictionary with all workbenches.
    """


def activeWorkbench():
    """
    activeWorkbench() -> Workbench

    Return the active workbench object.
    Possible exceptions: (AssertionError).
    """


def addResourcePath(filePath: str, /):
    """
    addResourcePath(path) -> None

    Add a new path to the system where to find resource files
    like icons or localization files.

    path : str, bytes, bytearray
        Path to resource files.
    """


def addLanguagePath(filePath: str, /):
    """
    addLanguagePath(path) -> None

    Add a new path to the system where to find language files.

    path : str, bytes, bytearray
        Path to language files.
    """


def addIconPath(filePath: str, /):
    """
    addIconPath(path) -> None

    Add a new path to the system where to find icon files.

    path : str, bytes, bytearray
        Path to icon files.
    """


def addIcon(iconName: str, content: str, format: str = 'XPM', /):
    """
    addIcon(name, content, format='XPM') -> None

    Add an icon to the system.

    name : str
        Name of the icon.
    content : str, bytes-like
        Content of the icon.
    format : str
        Format of the icon.
    Possible exceptions: (AssertionError, FreeCAD.Base.FreeCADError).
    """


def getIcon(iconName: str, /) -> qtpy.QtGui.QIcon:
    """
    getIcon(name) -> QIcon or None

    Get an icon in the system. If the pixmap is null, return None.

    name : str
        Name of the icon.
    """


def isIconCached(iconName: str, /) -> bool:
    """
    isIconCached(name) -> Bool

    Check if an icon with the given name is cached.

    name : str
        Name of the icon.
    """


def getMainWindow() -> FreeCADGui.MainWindowPy:
    """
    getMainWindow() -> QMainWindow

    Return the main window instance.
    """


def updateGui():
    """
    updateGui() -> None

    Update the main window and all its windows.
    """


def updateLocale():
    """
    updateLocale() -> None

    Update the localization.
    """


def getLocale() -> str:
    """
    getLocale() -> str

    Returns the locale currently used by FreeCAD.
    """


def setLocale(name: str, /):
    """
    setLocale(name) -> None

    Sets the locale used by FreeCAD. Can be set by top-level
    domain (e.g. "de") or the language name (e.g. "German").

    name : str
        Locale name.
    """


def supportedLocales() -> dict[str, str]:
    """
    supportedLocales() -> dict

    Returns a dict of all supported locales. The keys are the language
    names and the values the top-level domains.
    """


def createDialog(fn: str = None, /):
    """
    createDialog(path) -> PyResource

    Open a UI file.

    path : str
        UI file path.
    Possible exceptions: (AssertionError).
    """


@typing.overload
def addPreferencePage(fn: str, grp: str, /): ...


@typing.overload
def addPreferencePage(dlg: type, grp: str, /):
    """
    addPreferencePage(path, group) -> None
    addPreferencePage(dialog, group) -> None

    Add a UI form to the preferences dialog in the specified group.

    path : str
        UI file path.
    group : str
        Group name.
    dialog : type
        Preference page.
    Possible exceptions: (RuntimeError).
    """


def addCommand(pName: str, pcCmdObj, pSource: str = None, /):
    """
    addCommand(name, cmd, activation) -> None

    Add a command object.

    name : str
        Name of the command.
    cmd : object
        Command instance.
    activation : str
        Activation sequence. Optional.
    Possible exceptions: (Exception, ImportError, FreeCAD.Base.FreeCADError).
    """


def runCommand(pName: str, item: int = 0, /):
    """
    runCommand(name, index=0) -> None

    Run command by its name.

    name : str
        Name of the command.
    index : int
        Index of the child command.
    """


def SendMsgToActiveView(psCommandStr: str, suppress: bool = False, /) -> str:
    """
    SendMsgToActiveView(name, suppress=False) -> str or None

    Send message to the active view. Deprecated, use class View.

    name : str
        Name of the view command.
    suppress : bool
        If the sent message fail, suppress warning message.
    """


def sendMsgToFocusView(psCommandStr: str, suppress: bool = False, /) -> str:
    """
    sendMsgToFocusView(name, suppress=False) -> str or None

    Send message to the focused view.

    name : str
        Name of the view command.
    suppress : bool
        If send message fail, suppress warning message.
    """


def hide(psFeatStr: str, /):
    """
    hide(name) -> None

    Hide the given feature. Deprecated.

    name : str
        Feature name.
    """


def show(psFeatStr: str, /):
    """
    show(name) -> None

    Show the given feature. Deprecated.

    name : str
        Feature name.
    """


def hideObject(object: FreeCAD.DocumentObject, /):
    """
    hideObject(obj) -> None

    Hide the view provider of the given object.

    obj : App.DocumentObject
    """


def showObject(object: FreeCAD.DocumentObject, /):
    """
    showObject(obj) -> None

    Show the view provider of the given object.

    obj : App.DocumentObject
    """


def open(Name: str, /):
    """
    open(fileName) -> None

    Open a macro, Inventor or VRML file.

    fileName : str, bytes, bytearray
        File name.
    """


def insert(Name: str, DocName: str = None, /):
    """
    insert(fileName, docName) -> None

    Insert a macro, Inventor or VRML file. If no document name
    is given the active document is used.

    fileName : str, bytes, bytearray
        File name.
    docName : str
        Document name.
    """


def export(object, Name: str, /):
    """
    export(objs, fileName) -> None

    Save scene to Inventor or VRML file.

    objs : sequence of App.DocumentObject
        Sequence of objects to save.
    fileName : str, bytes, bytearray
        File name.
    """


def activeDocument() -> FreeCADGui.Document:
    """
    activeDocument() -> Gui.Document or None

    Return the active document. If no one exists, return None.
    """


@typing.overload
def setActiveDocument(pstr: str = None, /): ...


@typing.overload
def setActiveDocument(doc: FreeCAD.Document, /):
    """
    setActiveDocument(doc) -> None

    Activate the specified document.

    doc : str, App.Document
        Document to activate.
    Possible exceptions: (TypeError).
    """


def activeView(typeName: str = None, /) -> FreeCADGui.MDIViewPy:
    """
    activeView(typeName) -> object or None

    Return the active view of the active document. If no one
    exists, return None.

    typeName : str
        Type name.
    """


def activateView(typeStr: str, create: bool = False, /):
    """
    activateView(typeName, create=False) -> None

    Activate a view of the given type in the active document.
    If a view of this type doesn't exist and create is True, a
    new view of this type is created.

    type : str
        Type name.
    create : bool
    """


def editDocument() -> FreeCADGui.Document:
    """
    editDocument() -> Gui.Document or None

    Return the current editing document. If no one exists,
    return None.
    """


@typing.overload
def getDocument(pstr: str = None, /) -> FreeCADGui.Document: ...


@typing.overload
def getDocument(doc: FreeCAD.Document, /) -> FreeCADGui.Document:
    """
    getDocument(doc) -> Gui.Document

    Get a document.

    doc : str, App.Document
        `App.Document` name or `App.Document` object.
    Possible exceptions: (TypeError).
    """


def doCommand(sCmd: str = None, /):
    """
    doCommand(cmd) -> None

    Prints the given string in the python console and runs it.

    cmd : str
    """


def doCommandGui(sCmd: str = None, /):
    """
    doCommandGui(cmd) -> None

    Prints the given string in the python console and runs it
    but doesn't record it in macros.

    cmd : str
    """


def addModule(pstr: str, /):
    """
    addModule(mod) -> None

    Prints the given module import only once in the macro recording.

    mod : str
    Possible exceptions: (ImportError).
    """


def showDownloads():
    """
    showDownloads() -> None

    Show the downloads manager window.
    """


def showPreferences(pstr: str = None, idx: int = 0, /):
    """
    showPreferences(grp, index=0) -> None

    Show the preferences window.

    grp: str
        Group to show.
    index : int
        Page index.
    """


def createViewer(views: int = 1, title: str = None, /) -> typing.Any | FreeCADGui.AbstractSplitViewPy:
    """
    createViewer(views=1, name) -> View3DInventorPy or AbstractSplitViewPy

    Show and returns a viewer.

    views : int
        If > 1 a `AbstractSplitViewPy` object is returned.
    name : str
        Viewer title.
    """


def getMarkerIndex(pstr: str, defSize: int = 9, /) -> int:
    """
    getMarkerIndex(marker, size=9) -> int

    Get marker index according to marker name and size.

    marker : str
        Marker style name.
    size : int
        Marker size.
    """


def addDocumentObserver(o, /):
    """
    addDocumentObserver(obj) -> None

    Add an observer to get notifications about changes on documents.

    obj : object
    """


def removeDocumentObserver(o, /):
    """
    removeDocumentObserver(obj) -> None

    Remove an added document observer.

    obj : object
    """


def listUserEditModes() -> list[str]:
    """
    listUserEditModes() -> list

    List available user edit modes.
    """


def getUserEditMode() -> str:
    """
    getUserEditMode() -> str

    Get current user edit mode.
    """


def setUserEditMode(mode: str = '', /) -> bool:
    """
    setUserEditMode(mode) -> bool

    Set user edit mode. Returns True if exists, False otherwise.

    mode : str
    """


def reload(name: str, /):
    """
    reload(name) -> App.Document or None

    Reload a partial opened document. If the document is not open,
    return None.

    name : str
        `App.Document` name.
    """


def loadFile(path: str, mod: str = '', /):
    """
    loadFile(fileName, module) -> None

    Loads an arbitrary file by delegating to the given Python module.
    If no module is given it will be determined by the file extension.
    If more than one module can load a file the first one will be taken.
    If no module exists to load the file an exception will be raised.

    fileName : str
    module : str
    """


def coinRemoveAllChildren(pynode, /):
    """
    coinRemoveAllChildren(node) -> None

    Remove all children from a group node.

    node : object
    """


# ExpressionBindingPy.cpp
class ExpressionBinding:
    """Python interface class for ExpressionBinding"""

    def bind(self, py: FreeCAD.DocumentObject, str: str, /) -> None:
        """
        Bind with an expression
        Possible exceptions: (Exception, RuntimeError).
        """

    def isBound(self) -> bool:
        """
        Check if already bound with an expression
        Possible exceptions: (Exception).
        """

    def apply(self, str: str, /) -> bool:
        """
        apply
        Possible exceptions: (Exception).
        """

    def hasExpression(self) -> bool:
        """
        hasExpression
        Possible exceptions: (Exception).
        """

    def autoApply(self) -> bool:
        """
        autoApply
        Possible exceptions: (Exception).
        """

    def setAutoApply(self, b: bool, /) -> None:
        """
        setAutoApply
        Possible exceptions: (Exception).
        """


# View3DViewerPy.cpp
class View3DInventorViewerPy:
    """Python binding class for the 3D viewer class"""

    def getSoRenderManager(self) -> pivy.coin.SoRenderManager:
        """
        getSoRenderManager() -> SoRenderManager
        Returns the render manager which is used to handle everything related to
        rendering the scene graph. It can be used to get full control over the
        render process

        Possible exceptions: (Exception, RuntimeError).
        """

    def getSoEventManager(self) -> pivy.coin.SoEventManager:
        """
        getSoEventManager() -> SoEventManager
        Returns the event manager which is used to handle everything event related in
        the viewer. It can be used to change the event processing. This must however be
        done very carefully to not change the user interaction in an unpredictable manner.

        Possible exceptions: (Exception, RuntimeError).
        """

    def getSceneGraph(self) -> pivy.coin.SoSeparator:
        """
        getSceneGraph() -> SoNode
        Possible exceptions: (Exception, RuntimeError).
        """

    def setSceneGraph(self, proxy, /) -> None:
        """
        setSceneGraph(SoNode)
        Possible exceptions: (Exception, RuntimeError).
        """

    def seekToPoint(self, object, /) -> None:
        """
        seekToPoint(tuple) -> None
        Initiate a seek action towards the 3D intersection of the scene and the
        ray from the screen coordinate's point and in the same direction as the
        camera is pointing. If the tuple has two entries it is interpreted as the
        screen coordinates xy and the intersection point with the scene is
        calculated. If three entries are given it is interpreted as the intersection
        point xyz and the seek is done towards this point
        Possible exceptions: (Exception).
        """

    def setFocalDistance(self, distance: float, /) -> None:
        """
        setFocalDistance(float) -> None

        Possible exceptions: (Exception, RuntimeError).
        """

    def getFocalDistance(self) -> float:
        """
        getFocalDistance() -> float

        Possible exceptions: (Exception, RuntimeError).
        """

    def getPoint(self, x: int, y: int, /) -> FreeCAD.Vector:
        """
        Same as getPointOnFocalPlane
        Possible exceptions: (RuntimeError).
        """

    def getPointOnFocalPlane(self, x: int, y: int, /) -> FreeCAD.Vector:
        """
        getPointOnFocalPlane(x, y) -> Base::Vector(x,y,z)
        Possible exceptions: (RuntimeError).
        """

    def getPickRadius(self) -> float:
        """
        getPickRadius(): returns radius of confusion in pixels for picking objects on screen (selection).
        Possible exceptions: (Exception).
        """

    def setPickRadius(self, r: float = 0.0, /) -> None:
        """
        setPickRadius(new_radius): sets radius of confusion in pixels for picking objects on screen (selection).
        Possible exceptions: (Exception, RuntimeError).
        """

    def setupEditingRoot(self, pynode=None, pymat: FreeCAD.Matrix = None, /) -> None:
        """
        setupEditingRoot(matrix=None): setup the editing ViewProvider's root node.
        All child coin nodes of the current editing ViewProvider will be transferred to
        an internal editing node of this viewer, with a new transformation node specified
        by 'matrix'. All ViewProviderLink to the editing ViewProvider will be temporary
        hidden. Call resetEditingRoot() to restore everything back to normal
        Possible exceptions: (Exception, RuntimeError).
        """

    def resetEditingRoot(self, updateLinks: bool = True, /) -> None:
        """
        resetEditingRoot(updateLinks=True): restore the editing ViewProvider's root node
        Possible exceptions: (Exception, RuntimeError).
        """

    def setBackgroundColor(self, r: float, g: float, b: float = 0.0, /) -> None:
        """
        setBackgroundColor(r,g,b): sets the background color of the current viewer.
        Possible exceptions: (Exception, RuntimeError).
        """

    def setRedirectToSceneGraph(self, m: bool = False, /) -> None:
        """
        setRedirectToSceneGraph(bool): enables or disables to redirect events directly to the scene graph.
        Possible exceptions: (Exception).
        """

    def isRedirectedToSceneGraph(self) -> bool:
        """
        isRedirectedToSceneGraph() -> bool: check whether event redirection is enabled.
        Possible exceptions: (Exception).
        """

    def setEnabledNaviCube(self, m: bool = False, /) -> None:
        """
        setEnabledNaviCube(bool): enables or disables the navi cube of the viewer.
        Possible exceptions: (Exception).
        """

    def isEnabledNaviCube(self) -> bool:
        """
        isEnabledNaviCube() -> bool: check whether the navi cube is enabled.
        Possible exceptions: (Exception).
        """

    def setNaviCubeCorner(self, pos: int, /) -> None:
        """
        setNaviCubeCorner(int): sets the corner where to show the navi cube:
        0=top left, 1=top right, 2=bottom left, 3=bottom right
        Possible exceptions: (Exception, IndexError).
        """


# FreeCADGuiPy.cpp
def showMainWindow(inThread: bool = False, /) -> None:
    """
    showMainWindow() -- Show the main window
    If no main window does exist one gets created
    Possible exceptions: (RuntimeError).
    """


def exec_loop() -> None:
    """
    exec_loop() -- Starts the event loop
    Note: this will block the call until the event loop has terminated
    Possible exceptions: (RuntimeError).
    """


def setupWithoutGUI() -> None:
    """
    setupWithoutGUI() -- Uses this module without starting
    an event loop or showing up any GUI
    """


@typing.overload
def embedToWindow(): ...


@typing.overload
def embedToWindow(pointer: str, /) -> None:
    """
    embedToWindow() -- Embeds the main window into another window

    Possible exceptions: (FreeCAD.Base.FreeCADError, NotImplementedError).
    """


Workbench = FreeCADGui.PythonWorkbench  # noqa
ActiveDocument: FreeCADGui.Document | None
Control = ControlClass()  # hack to show this module in current module hints
