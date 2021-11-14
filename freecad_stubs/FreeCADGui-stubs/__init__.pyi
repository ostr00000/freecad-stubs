import typing

from FreeCADGui.TaskDialogPython import Control as ControlClass
import FreeCAD
import FreeCADGui
import FreeCADGui.Selection
import FreeCADTemplates
import qtpy.QtCore
import qtpy.QtGui
import qtpy.QtWidgets

_T = typing.TypeVar("_T")
Triple_t: typing.TypeAlias = tuple[_T, _T, _T]
Quadruple_t: typing.TypeAlias = tuple[_T, _T, _T, _T]


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

    def getToolbarItems(self) -> dict[object, list[str]]:
        """Show a dict of all toolbars and their commands"""

    def listCommandbars(self) -> list[str]:
        """Show a list of all command bars"""

    def listMenus(self) -> list[str]:
        """Show a list of all menus"""

    def listToolbars(self) -> list[str]:
        """Show a list of all toolbars"""

    def name(self) -> str:
        """Return the workbench name"""


# LinkViewPy.xml
class LinkView(FreeCAD.BaseClass):
    """Helper class to link to a view object"""

    @property
    def Count(self) -> int:
        """Set the element size to create an array of linked object"""

    @property
    def LinkedView(self) -> object:
        """The linked view object"""

    @property
    def Owner(self) -> object:
        """The owner view object of this link handle"""

    @property
    def RootNode(self) -> object:
        """A pivy node holding the cloned representation of the linked view object"""

    @property
    def SubNames(self) -> object:
        """The sub-object reference of the link"""

    @property
    def Visibilities(self) -> object:
        """Get/set the child element visibility"""

    def getBoundBox(self, vobj, /):
        """getBoundBox(vobj=None): get the bounding box."""

    def getChildren(self) -> tuple[object]:
        """Get children view objects"""

    def getDetailPath(self, arg1: str, arg2, /):
        """
        getDetailPath(element): get the 3d path an detail of an element.

        Return a tuple(path,detail) for the coin3D SoPath and SoDetail of the element
        """

    def getElementPicked(self, pickPoint, /) -> str:
        """getElementPicked(pickPoint): get the element under a 3d pick point."""

    def reset(self):
        """Reset the link view and clear the links"""

    def setChildren(self, obj_, vis: list = None, type: str = 0, /):
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

    def setLink(self, object, subname=None, /):
        """
        setLink(object): Set the link

        setLink(object, subname): Set the link with a sub-object reference

        setLink(object, [subname,...]): Set the link with a list of sub object references

        object: The linked document object or its view object

        subname: a string or tuple/list of strings sub-name references to sub object
                 or sub elements (e.g. Face1, Edge2) belonging to the linked object.
                 The sub-name must end with a '.' if it is referencing an sub-object,
                 or else it is considered a sub-element reference.
        """

    def setMaterial(self, Material, /):
        """
        setMaterial(Material): set the override material of the entire linked object

        setMaterial([Material,...]): set the materials for the elements of the link
                                     array/group. 

        setMaterial({Int:Material,...}): set the material for the elements of the
                                         link array/group by index. 

        If material is None, then the material is unset. If the material of an element
        is unset, it defaults to the override material of the linked object, if there
        is one
        """

    def setTransform(self, matrix, /):
        """
        setTransform(matrix): set transformation of the linked object

        setTransform([matrix,...]): set transformation for the elements of the link
                                    array/group

        setTransform({index:matrix,...}): set transformation for elements of the link
                                          array/group by index
        """

    def setType(self, type: int, sublink=True, /):
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
    def Annotation(self) -> object:
        """A pivy Separator to add a custom scenegraph to this ViewProvider"""

    @Annotation.setter
    def Annotation(self, value: object): ...

    @property
    def CanRemoveChildrenFromRoot(self) -> bool:
        """Tells the tree view whether to remove the children item from root or not"""

    @property
    def DefaultMode(self) -> int:
        """Get/Set the default display mode in turns of coin node index"""

    @DefaultMode.setter
    def DefaultMode(self, value: int): ...

    @property
    def DropPrefix(self) -> str:
        """Subname referecing the sub-object for holding dropped object"""

    @property
    def IV(self) -> str:
        """Represents the whole ViewProvider as an Inventor string."""

    @property
    def Icon(self) -> object:
        """The icon of this ViewProvider"""

    @property
    def LinkVisibility(self) -> bool:
        """Get/set visibilities of all links to this view object"""

    @property
    def RootNode(self) -> object:
        """A pivy Separator with the root of this ViewProvider"""

    @RootNode.setter
    def RootNode(self, value: object): ...

    @property
    def SwitchNode(self) -> object:
        """A pivy SoSwitch for the display mode switch of this ViewProvider"""

    @SwitchNode.setter
    def SwitchNode(self, value: object): ...

    def addDisplayMode(self, arg1, arg2: str, /):
        """Add a new display mode to the view provider"""

    def addProperty(self, arg1: str, arg2: str = None, arg3: str = None, arg4: str = None, arg5: int = None, arg6: bool = None, arg7: bool = None, /) -> FreeCADGui.ViewProvider:
        """
        Add a generic property.
        addProperty(string, string)
        --
        The first argument specifies the type, the second the name of the property.
        """

    def canDragAndDropObject(self, obj: FreeCAD.DocumentObject, /) -> bool:
        """
        Check whether the child object can be removed from other parent and added here by drag and drop
        canDragAndDropObject(obj)
        """

    def canDragObject(self, obj=None, /) -> bool:
        """
        check whether the child object can be removed by dragging
        canDragObject(obj=None)
        """

    def canDropObject(self, arg1=None, arg2=None, arg3: str = None, arg4=None, /) -> bool:
        """
        check whether the child object can be added by dropping
        canDropObject(obj=None,owner=None,subname=None)
        """

    def claimChildren(self) -> list[FreeCAD.DocumentObject | None]:
        """Returns list of objects that are to be grouped in tree under this object."""

    def doubleClicked(self) -> bool:
        """Trigger double clicking the corresponding tree item of this view object"""

    def dragObject(self, obj: FreeCAD.DocumentObject, /):
        """
        remove a child object by dropping
        dragObject(obj)
        """

    def dropObject(self, arg1: FreeCAD.DocumentObject, arg2=None, arg3: str = None, arg4=None, /) -> str:
        """
        add a child object by dropping
        dropObject(obj,owner=None,subname=None)
        """

    def getBoundingBox(self, subname: str = None, transform=True, view=None, /):
        """
        obtain the bounding box of this view object
        getBoundingBox(subname=None, transform=True, view=None)
        --
        subname: the optional subname referring a sub-object
        transform: whether to apply the transformation matrix of this view provider
        view: the MDIView, default to active view
        """

    def getDetailPath(self, subname: str, path, append=True, /) -> bool | object:
        """
        return Coin detail and path of an subelement
        getDetailPath(subname,path,append=True)
        --
        subelement: dot separated string reference to the sub element
        pPath: output coin path leading to the returned element detail
        append: If true, path will be first appended with the root node and the mode
        switch node of this view provider.
        """

    def getElementColors(self, elementName: str = None, /) -> dict[str, tuple]:
        """getElementColors(elementName=None) -> dict(elementName:color)"""

    def getElementPicked(self, pickPoint, /) -> str:
        """
        return the picked subelement
        getElementPicked(pickPoint)
        """

    def hide(self):
        """Hide the object"""

    def isVisible(self) -> bool:
        """Check if the object is visible"""

    def listDisplayModes(self) -> list[str]:
        """Show a list of all display modes"""

    def partialRender(self, sub=None, clear=False, /) -> int:
        """
        render only part of the object
        partialRender(sub=None,clear=False)
        --
        sub: string or list of string refer to the subelement. If it is None then reset the partial rendering.
        clear: true to add, or false to remove the subelement(s) for rendering.
        """

    def removeProperty(self, string: str, /) -> bool:
        """
        Remove a generic property.
        removeProperty(string)
        --
        Note, you can only remove user-defined properties, not built-in ones.
        """

    def replaceObject(self, oldObj: FreeCAD.DocumentObject, newObj: FreeCAD.DocumentObject, /) -> int:
        """
        replace a child object
        replaceObject(oldObj, newObj) -> Int
        --
        Returns 1 if succeeded, 0 if not found, -1 if not supported
        """

    def setElementColors(self, colors, /):
        """
        setElementColors(colors): set element colors
        --
        colors: color dictionary of type elementName:(r,g,b,a)
        """

    @typing.overload
    def setTransformation(self, arg1: FreeCAD.Matrix, /): ...

    @typing.overload
    def setTransformation(self, arg1: FreeCAD.Placement, /):
        """Set a transformation on the Inventor node"""

    def show(self):
        """Show the object"""

    def signalChangeIcon(self):
        """Trigger icon changed signal"""

    def supportedProperties(self) -> list[str]:
        """A list of supported property types"""

    def toString(self) -> str:
        """Return a string representation of the Inventor node"""


# ViewProviderLinkPy.xml
class ViewProviderLink(FreeCADGui.ViewProviderDocumentObject):
    """This is the ViewProviderLink class"""

    @property
    def DraggingPlacement(self) -> object:
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

    def ignoreOverlayIcon(self, arg1: str, /) -> bool:
        """Ignore the overlay icon of an extension"""

    def setIgnoreOverlayIcon(self, arg1: bool, arg2: str, /):
        """Ignore the overlay icon of an extension"""


# CommandPy.xml
class Command(FreeCAD.PyObjectBase):
    """FreeCAD Python wrapper of Command functions"""

    @staticmethod
    def get(string: str, /) -> FreeCADGui.Command:
        """
        Get a given command by name or None if it doesn't exist.
        get(string) -> Command
        """

    def getAction(self) -> list[qtpy.QtCore.QObject]:
        """
        Return the associated QAction object.
        getAction() -> list of QAction
        """

    def getInfo(self) -> list[str]:
        """
        Return information about this command.
        getInfo() -> list of strings
        --
        Usage: menuText, tooltipText, whatsThisText, statustipText, pixmapText, shortcutText.
        """

    def getShortcut(self) -> str:
        """
        Returns string representing shortcut key accelerator for command.
        getShortcut() -> string
        """

    def isActive(self) -> bool:
        """
        Returns True if the command is active, False otherwise.
        isActive() -> bool
        """

    @staticmethod
    def listAll() -> list[str]:
        """
        Returns the name of all commands.
        listAll() -> list of strings
        """

    @staticmethod
    def listByShortcut(string: str, bool_bUseRegExp: int = False, /) -> list[str]:
        """
        Returns a list of all commands, filtered by shortcut.
        listByShortcut(string, bool bUseRegExp=False) -> list of strings
        --
        Shortcuts are converted to uppercase and spaces removed prior to comparison.
        """

    def resetShortcut(self) -> bool:
        """
        Resets shortcut for given command back to the default, returns bool True for success.
        resetShortcut() -> bool
        """

    def run(self, arg1: int = None, /):
        """
        Runs the given command.
        run() -> None
        """

    def setShortcut(self, string: str, /) -> bool:
        """
        Sets shortcut for given command, returns bool True for success.
        setShortcut(string) -> bool
        """

    @staticmethod
    def update():
        """
        Update active status of all commands.
        update() -> None
        """


# PythonWorkbenchPy.xml
class PythonWorkbench(FreeCADGui.Workbench):
    """This class handles document objects in group"""

    def appendCommandbar(self, arg1: str, arg2, /):
        """Append a new command bar"""

    def appendContextMenu(self, arg1, arg2, /):
        """Append a new context menu item"""

    def appendMenu(self, arg1, arg2, /):
        """Append a new menu"""

    def appendToolbar(self, arg1: str, arg2, /):
        """Append a new toolbar"""

    def removeCommandbar(self, arg1: str, /):
        """Remove a command bar"""

    def removeContextMenu(self, arg1: str, /):
        """Remove a context menu item"""

    def removeMenu(self, arg1: str, /):
        """Remove a menu"""

    def removeToolbar(self, arg1: str, /):
        """Remove a toolbar"""


# AxisOriginPy.xml
class AxisOrigin(FreeCAD.BaseClass):
    """Class for creating a Coin3D representation of a coordinate system"""

    @property
    def AxisLength(self) -> float:
        """Get/set the axis length"""

    @property
    def Labels(self) -> dict:
        """
        Get/set axis component names as a dictionary. Available keys are,
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
        """Get/set the axis line width for rendering"""

    @property
    def Node(self) -> object:
        """Get the Coin3D node"""

    @property
    def Plane(self) -> tuple:
        """Get/set axis plane size and distance to axis line"""

    @property
    def PointSize(self) -> float:
        """Get/set the origin point size for rendering"""

    @property
    def Scale(self) -> float:
        """Get/set auto scaling factor, 0 to disable"""

    def getDetailPath(self, subname: str, path, /) -> bool | object:
        """
        getDetailPath(subname,path): return Coin detail and path of an subelement

        subelement: dot separated string reference to the sub element
        pPath: output coin path leading to the returned element detail
        """

    def getElementPicked(self, pickPoint, /) -> str:
        """getElementPicked(pickPoint): return the picked subelement"""


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
    def TreeRank(self) -> int:
        """
        [Prop_Hidden] Property won't appear in the editor.
        [Prop_NoPersist] Property won't be saved to file at all.
        Property group: Display Options.
        Property TypeId: App::PropertyInteger.
        Tree view item ordering key.
        """

    @TreeRank.setter
    def TreeRank(self, value: int): ...

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

    def isObjectTypeOf(self, type: str, /) -> bool:
        """
        Test for a certain father class.
        isObjectTypeOf(type) -> Bool
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
    def EditMode(self) -> int:
        """Current edit mode. Only meaningful when there is a current object in edit"""

    @property
    def EditingTransform(self) -> object:
        """The editing transformation matrix"""

    @property
    def InEditInfo(self) -> object:
        """A tuple(obj,subname,subElement,editMode) of editing object reference, or None if no object is in edit"""

    @property
    def Modified(self) -> bool:
        """Returns True if the document is marked as modified, and False otherwise"""

    @property
    def Transacting(self) -> bool:
        """Indicate whether the document is undoing/redoing"""

    def activeObject(self) -> FreeCADGui.ViewProvider:
        """deprecated -- use ActiveObject"""

    def activeView(self) -> FreeCADGui.MDIView:
        """deprecated -- use ActiveView"""

    def addAnnotation(self, AnnoName: str, FileName: str, ModName: str = None, /):
        """
        Add an Inventor object
        addAnnotation(AnnoName,FileName,[ModName]) -> None
        """

    def getInEdit(self) -> FreeCADGui.ViewProvider:
        """
        Returns the current object in edit mode or None if there is no such object
        getInEdit() -> Object or None
        """

    def getObject(self, Name: str, /) -> FreeCADGui.ViewProvider:
        """
        Return the object with the given name
        getObject(Name) -> Object or None
        """

    def hide(self, arg1: str, /):
        """
        Hide the object
        hide() -> None
        """

    def mdiViewsOfType(self, type: str, /) -> list[FreeCADGui.MDIView]:
        """
        Return a list if mdi views of a given type
        mdiViewsOfType(type) -> list of MDIView
        """

    def mergeProject(self, filename: str, /):
        """
        Merges this document with another project file
        mergeProject(filename) -> None
        """

    def resetEdit(self):
        """
        Reset (end) the current editing.
        resetEdit() -> None
        """

    def scrollToTreeItem(self, ViewObject: FreeCADGui.ViewProviderDocumentObject, /):
        """
        scroll the tree view to the item of a view object
        scrollToTreeItem(ViewObject) -> None
        """

    def sendMsgToViews(self, msg: str, /):
        """
        Send a message to all views of the document
        sendMsgToViews(msg) -> None
        """

    @typing.overload
    def setEdit(self, String_Name_ViewProvider_DocumentObject_: str, mod: int = None, subname: str = None, /) -> bool: ...

    @typing.overload
    def setEdit(self, String_Name_ViewProvider_DocumentObject_, mod: int = None, subname: str = None, /) -> bool:
        """
        Set the given object in edit mode.
        setEdit([String:Name|ViewProvider|DocumentObject]|,mod,subname=None) -> Bool
        """

    def setPos(self, arg1: str, arg2: FreeCAD.Matrix, /):
        """
        Set the position
        setPos(matrix) -> None
        """

    def show(self, arg1: str, /):
        """
        Show the object
        show() -> None
        """

    def toggleInSceneGraph(self, ViewObject: FreeCADGui.ViewProvider, /):
        """
        Add or remove view object from scene graph of all views depending on its canAddToSceneGraph()
        toggleInSceneGraph(ViewObject) -> None
        """

    def toggleTreeItem(self, arg1: FreeCAD.DocumentObject, arg2: int = None, arg3: str = None, /):
        """
        Change TreeItem of a document object.
        toggleTreeItem(DocObject,[flag=0]) -> None
        --
        flag can be 0:Toggle, 1:Collaps, 2:Expand
        """

    def update(self):
        """
        Update the view representations of all objects
        update() -> None
        """


# MDIViewPy.cpp
class MDIViewPy:
    """Python binding class for the MDI view class"""

    def message(self, arg1: str, /) -> bool:
        """deprecated: use sendMessage"""

    def sendMessage(self, str: str, /) -> bool:
        """sendMessage(str)"""

    def supportMessage(self, str: str, /) -> bool:
        """supportMessage(str)"""

    def fitAll(self) -> None:
        """fitAll()"""

    def setActiveObject(self, name: str, object=None, subname: str = None, /) -> None:
        """
        setActiveObject(name,object,subname=None)
        add or set a new active object
        """

    def getActiveObject(self, name: str, resolve=True, /) -> None | FreeCAD.DocumentObject | tuple:
        """
        getActiveObject(name,resolve=True)
        returns the active object for the given type
        """


# Application.cpp
def subgraphFromObject(object: FreeCAD.DocumentObject, /) -> object | None:
    """
    subgraphFromObject(object) -> Node

    Return the Inventor subgraph to an object
    """


def exportSubgraph(Node, File_or_Buffer, Format: str = 'VRML', /) -> None:
    """
    exportSubgraph(Node, File or Buffer, [Format='VRML']) -> None

    Exports the sub-graph in the requested formatThe format string can be VRML or IV
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

    def message(self, arg1: str, /) -> None:
        """message()"""

    def fitAll(self, arg1: float = None, /) -> None:
        """fitAll()"""

    def viewBottom(self) -> None:
        """viewBottom()"""

    def viewFront(self) -> None:
        """viewFront()"""

    def viewLeft(self) -> None:
        """viewLeft()"""

    def viewRear(self) -> None:
        """viewRear()"""

    def viewRight(self) -> None:
        """viewRight()"""

    def viewTop(self) -> None:
        """viewTop()"""

    def viewAxometric(self) -> None:
        """viewAxonometric()"""

    def viewAxonometric(self) -> None:
        """viewAxonometric()"""

    def viewIsometric(self) -> None:
        """viewIsometric()"""

    def viewDimetric(self) -> None:
        """viewDimetric()"""

    def viewTrimetric(self) -> None:
        """viewTrimetric()"""

    def viewDefaultOrientation(self, ori_str: str = '', scale: float = -1.0, /) -> None:
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
        """

    def viewRotateLeft(self) -> None:
        """viewRotateLeft()"""

    def viewRotateRight(self) -> None:
        """viewRotateRight()"""

    def zoomIn(self) -> None:
        """zoomIn()"""

    def zoomOut(self) -> None:
        """zoomOut()"""

    def viewPosition(self, arg1: FreeCAD.Placement = None, arg2: int = None, arg3: int = None, /) -> None | FreeCAD.Placement:
        """viewPosition()"""

    def startAnimating(self, arg1: float, arg2: float, arg3: float, arg4: float, /) -> None:
        """startAnimating()"""

    def stopAnimating(self) -> None:
        """stopAnimating()"""

    def setAnimationEnabled(self, arg1: int, /) -> None:
        """setAnimationEnabled()"""

    def isAnimationEnabled(self) -> bool:
        """isAnimationEnabled()"""

    def setPopupMenuEnabled(self, arg1: int, /) -> None:
        """setPopupMenuEnabled()"""

    def isPopupMenuEnabled(self) -> bool:
        """isPopupMenuEnabled()"""

    def dump(self, filename: str, onlyVisible=False, /) -> None:
        """dump(filename, [onlyVisible=False])"""

    def dumpNode(self, node, /) -> str:
        """dumpNode(node)"""

    @typing.overload
    def setStereoType(self, arg1: int, /) -> None: ...

    @typing.overload
    def setStereoType(self, arg1: str, /) -> None:
        """setStereoType()"""

    def getStereoType(self) -> str:
        """getStereoType()"""

    def listStereoTypes(self) -> list:
        """listStereoTypes()"""

    def saveImage(self, arg1: str, arg2: int = None, arg3: int = None, arg4: str = None, arg5: str = None, arg6: int = None, /) -> None:
        """saveImage()"""

    def saveVectorGraphic(self, arg1: str, arg2: int = None, arg3: str = None, /) -> None:
        """saveVectorGraphic()"""

    def getCamera(self) -> str:
        """getCamera()"""

    def getCameraNode(self):
        """getCameraNode()"""

    def getViewDirection(self) -> FreeCAD.Vector:
        """
        getViewDirection() --> tuple of integers
        returns the direction vector the view is currently pointing at as tuple with xyz values
        """

    def setViewDirection(self, tuple, /) -> None:
        """
        setViewDirection(tuple) --> None
        Sets the direction the view is pointing at. The direction must be given as tuple with
        three coordinates xyz
        """

    def setCamera(self, arg1: str, /) -> None:
        """setCamera()"""

    def setCameraOrientation(self, arg1, arg2: bool = None, /) -> None:
        """setCameraOrientation()"""

    def getCameraOrientation(self) -> FreeCAD.Rotation:
        """getCameraOrientation()"""

    def getCameraType(self) -> str:
        """getCameraType()"""

    @typing.overload
    def setCameraType(self, arg1: int, /) -> None: ...

    @typing.overload
    def setCameraType(self, arg1: str, /) -> None:
        """setCameraType()"""

    def listCameraTypes(self) -> list:
        """listCameraTypes()"""

    def getCursorPos(self) -> tuple[int, int]:
        """
        getCursorPos() -> tuple of integers

        Return the current cursor position relative to the coordinate system of the
        viewport region.
        """

    def getObjectInfo(self, tuple_int_int_, pick_radius: float = None, /) -> None:
        """
        getObjectInfo(tuple(int,int), [pick_radius]) -> dictionary or None

        Return a dictionary with the name of document, object and component. The
        dictionary also contains the coordinates of the appropriate 3d point of
        the underlying geometry in the scenegraph.
        If no geometry was found 'None' is returned, instead.
        """

    def getObjectsInfo(self, tuple_int_int_, pick_radius: float = None, /) -> None:
        """
        getObjectsInfo(tuple(int,int), [pick_radius]) -> dictionary or None

        Does the same as getObjectInfo() but returns a list of dictionaries or None.
        """

    def getSize(self) -> tuple[int, int]:
        """getSize()"""

    def getPoint(self, arg1: int, arg2: int, /) -> FreeCAD.Vector:
        """
        getPoint(pixel coords (as integer)) -> 3D vector

        Return the according 3D point on the focal plane to the given 2D point (in
        pixel coordinates).
        """

    def getPointOnScreen(self, arg1: FreeCAD.Vector, /) -> tuple[int, int]:
        """
        getPointOnScreen(3D vector) -> pixel coords (as integer)

        Return the projected 3D point (in pixel coordinates).
        """

    def addEventCallback(self, arg1: str, arg2, /) -> typing.Callable:
        """addEventCallback()"""

    def removeEventCallback(self, arg1: str, arg2, /) -> None:
        """removeEventCallback()"""

    def setAnnotation(self, arg1: str, arg2: str, /) -> None:
        """setAnnotation()"""

    def removeAnnotation(self, arg1: str, /) -> None:
        """removeAnnotation()"""

    def getSceneGraph(self):
        """getSceneGraph()"""

    def getViewer(self) -> FreeCADGui.View3DInventorViewerPy:
        """getViewer()"""

    def addEventCallbackPivy(self, arg1, arg2, arg3: int = None, /) -> typing.Callable:
        """addEventCallbackPivy()"""

    def removeEventCallbackPivy(self, arg1, arg2, arg3: int = None, /) -> typing.Callable:
        """removeEventCallbackPivy()"""

    def addEventCallbackSWIG(self, arg1, arg2, arg3: int = None, /) -> typing.Callable:
        """Deprecated -- use addEventCallbackPivy()"""

    def removeEventCallbackSWIG(self, arg1, arg2, arg3: int = None, /) -> typing.Callable:
        """Deprecated -- use removeEventCallbackPivy()"""

    def listNavigationTypes(self):
        """listNavigationTypes()"""

    def getNavigationType(self):
        """getNavigationType()"""

    def setNavigationType(self, arg1: str, /) -> None:
        """setNavigationType()"""

    def setAxisCross(self, arg1: int, /) -> None:
        """switch the big axis-cross on and off"""

    def hasAxisCross(self) -> bool:
        """check if the big axis-cross is on or off()"""

    def addDraggerCallback(self, SoDragger, String_CallbackType: str, function, /) -> typing.Callable:
        """
        addDraggerCallback(SoDragger, String CallbackType, function)
        Add a DraggerCalback function to the coin node
        Possibles types :
        'addFinishCallback','addStartCallback','addMotionCallback','addValueChangedCallback'
        """

    def removeDraggerCallback(self, SoDragger, String_CallbackType: str, function, /) -> typing.Callable:
        """
        removeDraggerCallback(SoDragger, String CallbackType, function)
        Remove the DraggerCalback function from the coin node
        Possibles types :
        'addFinishCallback','addStartCallback','addMotionCallback','addValueChangedCallback'
        """

    def setActiveObject(self, name: str, object=None, subname: str = None, /) -> None:
        """
        setActiveObject(name,object,subname=None)
        add or set a new active object
        """

    def getActiveObject(self, name: str, resolve=True, /) -> None | FreeCAD.DocumentObject | tuple:
        """
        getActiveObject(name,resolve=True)
        returns the active object for the given type
        """

    def getViewProvidersOfType(self, name: str, /) -> list[FreeCADGui.ViewProvider]:
        """
        getViewProvidersOfType(name)
        returns a list of view providers for the given type
        """

    def redraw(self) -> None:
        """redraw(): renders the scene on screen (useful for animations)"""

    def setName(self, str: str, /) -> None:
        """
        setName(str): sets a name to this viewer
        The name sets the widget's windowTitle and appears on the viewer tab
        """

    def hasClippingPlane(self) -> bool:
        """hasClippingPlane(): check whether this clipping plane is active"""

    def graphicsView(self) -> qtpy.QtWidgets.QGraphicsView:
        """graphicsView(): Access this view as QGraphicsView"""

    def boxZoom(self, XMin: int, YMin: int, XMax: int, YMax: int) -> None:
        """boxZoom()"""

    def toggleClippingPlane(self, toggle: int = None, beforeEditing=None, noManip=None, pla: FreeCAD.Placement = None) -> None:
        """
        toggleClippingPlane(toggle=-1, beforeEditing=False, noManip=True, pla=App.Placement()
        Toggle a global clipping plane

        toggle: -1 toggle, 1 show, 0 hide
        beforeEditing: whether to insert the clipping node before or after editing root node
        noManip: whether to create a manipulator
        pla: clipping plane placement
        """


# WidgetFactory.cpp
class PyResource:
    """PyResource"""

    def value(self, arg1: str, arg2: str, /) -> None: ...

    def setValue(self, arg1: str, arg2: str, arg3, /) -> None: ...


# UiLoader.cpp
class UiLoader:
    """UiLoader to create widgets"""

    @typing.overload
    def load(self, string, QWidget_parent=None, /): ...

    @typing.overload
    def load(self, QIODevice, QWidget_parent=None, /):
        """
        load(string, QWidget parent=None) -> QWidget
        load(QIODevice, QWidget parent=None) -> QWidget
        """

    def createWidget(self):
        """createWidget()"""


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

    def fitAll(self) -> None:
        """fitAll()"""

    def viewBottom(self) -> None:
        """viewBottom()"""

    def viewFront(self) -> None:
        """viewFront()"""

    def viewLeft(self) -> None:
        """viewLeft()"""

    def viewRear(self) -> None:
        """viewRear()"""

    def viewRight(self) -> None:
        """viewRight()"""

    def viewTop(self) -> None:
        """viewTop()"""

    def viewAxometric(self) -> None:
        """viewAxometric()"""

    def viewIsometric(self) -> None:
        """viewIsometric()"""

    def getViewer(self, index: int, /) -> FreeCADGui.View3DInventorViewer:
        """getViewer(index)"""

    def close(self) -> None:
        """close()"""


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
        """Check if the current selection matches the filter"""

    def result(self):
        """If match() returns True then with result() you get a list of the matching objects"""

    def test(self, Feature: FreeCAD.DocumentObject, SubName: str = '', /) -> bool:
        """
        test(Feature, SubName='')
        Test if a given object is described in the filter.
        If SubName is not empty the sub-element gets also tested.
        """

    def setFilter(self, arg1: str, /) -> None:
        """Set a new selection filter"""


# PythonDebugger.cpp
class PythonDebugStdout:
    """Redirection of stdout to FreeCAD's Python debugger window"""

    def write(self, arg1: str, /) -> None:
        """write to stdout"""


class PythonDebugStderr:
    """Redirection of stderr to FreeCAD's Python debugger window"""

    def write(self, arg1: str, /) -> None:
        """write to stderr"""


class PythonDebugExcept:
    """Custom exception handler"""

    pass
# ApplicationPy.cpp
def activateWorkbench(string: str, /) -> bool:
    """
    activateWorkbench(string) -> None

    Activate the workbench by name
    """


def addWorkbench(arg0, /) -> None:
    """
    addWorkbench(string, object) -> None

    Add a workbench under a defined name.
    """


def removeWorkbench(string: str, /) -> None:
    """
    removeWorkbench(string) -> None

    Remove the workbench with name
    """


def getWorkbench(string: str, /):
    """
    getWorkbench(string) -> object

    Get the workbench by its name
    """


def listWorkbenches():
    """
    listWorkbenches() -> list

    Show a list of all workbenches
    """


def activeWorkbench():
    """
    activeWorkbench() -> object

    Return the active workbench object
    """


def addResourcePath(string: str, /) -> None:
    """
    addResourcePath(string) -> None

    Add a new path to the system where to find resource files
    like icons or localization files
    """


def addLanguagePath(string: str, /) -> None:
    """
    addLanguagePath(string) -> None

    Add a new path to the system where to find language files
    """


def addIconPath(string: str, /) -> None:
    """
    addIconPath(string) -> None

    Add a new path to the system where to find icon files
    """


def addIcon(arg0: str, arg1: str, arg2: str = None, /) -> None:
    """
    addIcon(string, string or list) -> None

    Add an icon as file name or in XPM format to the system
    """


def getIcon(string: str, /) -> qtpy.QtGui.QIcon:
    """
    getIcon(string) -> QIcon

    Get an icon in the system
    """


def isIconCached(String: str, /) -> bool:
    """
    isIconCached(String) -> Bool

    Check if an icon with the given name is cached
    """


def getMainWindow() -> qtpy.QtWidgets.QMainWindow:
    """
    getMainWindow() -> QMainWindow

    Return the main window instance
    """


def updateGui() -> None:
    """
    updateGui() -> None

    Update the main window and all its windows
    """


def updateLocale() -> None:
    """
    updateLocale() -> None

    Update the localization
    """


def getLocale() -> str:
    """
    getLocale() -> string

    Returns the locale currently used by FreeCAD
    """


def setLocale(arg0: str, /) -> None:
    """
    getLocale(string) -> None

    Sets the locale used by FreeCAD. You can set it by
    top-level domain (e.g. "de") or the language name (e.g. "German")
    """


def supportedLocales() -> dict[str, str]:
    """
    supportedLocales() -> dict

    Returns a dict of all supported languages/top-level domains
    """


def createDialog(string: str, /):
    """createDialog(string) -- Open a UI file"""


@typing.overload
def addPreferencePage(string: str, string1: str, /) -> None: ...


@typing.overload
def addPreferencePage(string: type, string1: str, /) -> None:
    """
    addPreferencePage(string,string) -- Add a UI form to the
    preferences dialog. The first argument specifies the file nameand the second specifies the group name
    """


def addCommand(arg0: str, arg1, arg2: str = None, /) -> None:
    """
    addCommand(string, object) -> None

    Add a command object
    """


def runCommand(arg0: str, arg1: int = None, /) -> None:
    """
    runCommand(string) -> None

    Run command with name
    """


def SendMsgToActiveView(arg0: str, arg1: bool = None, /) -> str | None:
    """deprecated -- use class View"""


def sendMsgToFocusView(arg0: str, arg1: bool = None, /) -> str | None:
    """send message to the focused view"""


def hide(arg0: str, /):
    """deprecated"""


def show(arg0: str, /):
    """deprecated"""


def hideObject(object: FreeCAD.DocumentObject, /):
    """
    hideObject(object) -> None

    Hide the view provider to the given object
    """


def showObject(object: FreeCAD.DocumentObject, /):
    """
    showObject(object) -> None

    Show the view provider to the given object
    """


def open(arg0: str, /):
    """Open a macro, Inventor or VRML file"""


def insert(arg0: str, arg1: str = None, /):
    """Open a macro, Inventor or VRML file"""


def export(arg0, arg1: str, /):
    """save scene to Inventor or VRML file"""


def activeDocument() -> FreeCADGui.Document:
    """
    activeDocument() -> object or None

    Return the active document or None if no one exists
    """


@typing.overload
def setActiveDocument(string_or_App_Document: str, /): ...


@typing.overload
def setActiveDocument(string_or_App_Document: FreeCAD.Document, /):
    """
    setActiveDocument(string or App.Document) -> None

    Activate the specified document
    """


def activeView(typename: str = None, /) -> FreeCADGui.MDIView:
    """
    activeView(typename=None) -> object or None

    Return the active view of the active document or None if no one exists
    """


def activateView(arg0: str, arg1: bool, /):
    """
    activateView(type)

    Activate a view of the given type of the active document
    """


def editDocument() -> FreeCADGui.Document:
    """
    editDocument() -> object or None

    Return the current editing document or None if no one exists
    """


@typing.overload
def getDocument(string: str, /) -> FreeCADGui.Document: ...


@typing.overload
def getDocument(string: FreeCAD.Document, /) -> FreeCADGui.Document:
    """
    getDocument(string) -> object

    Get a document by its name
    """


def doCommand(string: str, /):
    """
    doCommand(string) -> None

    Prints the given string in the python console and runs it
    """


def doCommandGui(string: str, /):
    """
    doCommandGui(string) -> None

    Prints the given string in the python console and runs it but doesn't record it in macros
    """


def addModule(string: str, /) -> None:
    """
    addModule(string) -> None

    Prints the given module import only once in the macro recording
    """


def showDownloads() -> None:
    """
    showDownloads() -> None

    Shows the downloads manager window
    """


def showPreferences(string: str = None, int: int = None, /) -> None:
    """
    showPreferences([string,int]) -> None

    Shows the preferences window. If string and int are provided, the given page index in the given group is shown.
    """


def createViewer(arg0: int = None, arg1: str = None, /) -> object | FreeCADGui.AbstractSplitViewPy | None:
    """
    createViewer([int]) -> View3DInventor/SplitView3DInventor

    shows and returns a viewer. If the integer argument is given and > 1: -> splitViewer
    """


def getMarkerIndex(arg0: str = None, arg1: int = None, /) -> int:
    """Get marker index according to marker size setting"""


def addDocumentObserver(arg0, /):
    """
    addDocumentObserver() -> None

    Add an observer to get notified about changes on documents.
    """


def removeDocumentObserver(arg0, /):
    """
    removeDocumentObserver() -> None

    Remove an added document observer.
    """


def listUserEditModes() -> list[str]:
    """
    listUserEditModes() -> list

    List available user edit modes
    """


def getUserEditMode() -> str:
    """
    getUserEditMode() -> string

    Get current user edit mode
    """


def setUserEditMode(string: str, /) -> bool:
    """
    setUserEditMode(string=mode) -> Bool

    Set user edit mode to 'mode', returns True if exists, false otherwise
    """


def reload(name: str, /):
    """
    reload(name) -> doc

    Reload a partial opened document
    """


def loadFile(string: str, string1: str = None, /):
    """
    loadFile(string=filename,[string=module]) -> None

    Loads an arbitrary file by delegating to the given Python module:
    * If no module is given it will be determined by the file extension.
    * If more than one module can load a file the first one will be taken.
    * If no module exists to load the file an exception will be raised.
    """


def coinRemoveAllChildren(arg0, /):
    """Remove all children from a group node"""


# ExpressionBindingPy.cpp
class ExpressionBinding:
    """Python interface class for ExpressionBinding"""

    def bind(self, arg1: FreeCAD.DocumentObject, arg2: str, /) -> None:
        """Bind with an expression"""

    def isBound(self) -> bool:
        """Check if already bound with an expression"""

    def apply(self, arg1: str, /) -> bool:
        """apply"""

    def hasExpression(self) -> bool:
        """hasExpression"""

    def autoApply(self) -> bool:
        """autoApply"""

    def setAutoApply(self, arg1: bool, /) -> None:
        """setAutoApply"""


# View3DViewerPy.cpp
class View3DInventorViewerPy:
    """Python binding class for the 3D viewer class"""

    def getSoRenderManager(self):
        """
        getSoRenderManager() -> SoRenderManager
        Returns the render manager which is used to handle everything related to
        rendering the scene graph. It can be used to get full control over the
        render process
        """

    def getSoEventManager(self):
        """
        getSoEventManager() -> SoEventManager
        Returns the event manager which is used to handle everything event related in
        the viewer. It can be used to change the event processing. This must however be
        done very carefully to not change the user interaction in an unpredictable manner.
        """

    def getSceneGraph(self):
        """getSceneGraph() -> SoNode"""

    def setSceneGraph(self, SoNode, /) -> None:
        """setSceneGraph(SoNode)"""

    def seekToPoint(self, tuple, /) -> None:
        """
        seekToPoint(tuple) -> None
        Initiate a seek action towards the 3D intersection of the scene and the
        ray from the screen coordinate's point and in the same direction as the
        camera is pointing. If the tuple has two entries it is interpreted as the
        screen coordinates xy and the intersection point with the scene is
        calculated. If three entries are given it is interpreted as the intersection
        point xyz and the seek is done towards this point
        """

    def setFocalDistance(self, float: float, /) -> None:
        """setFocalDistance(float) -> None"""

    def getFocalDistance(self) -> float:
        """getFocalDistance() -> float"""

    def getPoint(self, x: int, y: int, /) -> FreeCAD.Vector:
        """getPoint(x, y) -> Base::Vector(x,y,z)"""

    def getPickRadius(self) -> float:
        """getPickRadius(): returns radius of confusion in pixels for picking objects on screen (selection)."""

    def setPickRadius(self, new_radius: float, /) -> None:
        """setPickRadius(new_radius): sets radius of confusion in pixels for picking objects on screen (selection)."""

    def setupEditingRoot(self, arg1=None, arg2: FreeCAD.Matrix = None, /) -> None:
        """
        setupEditingRoot(matrix=None): setup the editing ViewProvider's root node.
        All child coin nodes of the current editing ViewProvider will be transferred to
        an internal editing node of this viewer, with a new transformation node specified
        by 'matrix'. All ViewProviderLink to the editing ViewProvider will be temporary
        hidden. Call resetEditingRoot() to restore everything back to normal
        """

    def resetEditingRoot(self, updateLinks=True, /) -> None:
        """resetEditingRoot(updateLinks=True): restore the editing ViewProvider's root node"""

    def setBackgroundColor(self, r: float, g: float, b: float, /) -> None:
        """setBackgroundColor(r,g,b): sets the background color of the current viewer."""

    def setRedirectToSceneGraph(self, bool: bool, /) -> None:
        """setRedirectToSceneGraph(bool): enables or disables to redirect events directly to the scene graph."""

    def isRedirectedToSceneGraph(self) -> bool:
        """isRedirectedToSceneGraph() -> bool: check whether event redirection is enabled."""

    def setEnabledNaviCube(self, bool: bool, /) -> None:
        """setEnabledNaviCube(bool): enables or disables the navi cube of the viewer."""

    def isEnabledNaviCube(self) -> bool:
        """isEnabledNaviCube() -> bool: check whether the navi cube is enabled."""

    def setNaviCubeCorner(self, int: int, /) -> None:
        """
        setNaviCubeCorner(int): sets the corner where to show the navi cube:
        0=top left, 1=top right, 2=bottom left, 3=bottom right
        """


Workbench: FreeCADGui.Workbench
ActiveDocument: FreeCADGui.Document
Control = ControlClass()  # hack to show this module in current module hints
