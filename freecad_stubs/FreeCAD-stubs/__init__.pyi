import typing

from FreeCAD.Base import *
import FreeCAD
import FreeCAD.Base
import FreeCAD.Console
import FreeCAD.Qt as Qt
import FreeCAD.Units as Units
import FreeCADGui
import FreeCADTemplates

_T = typing.TypeVar("_T")
Triple_t: typing.TypeAlias = tuple[_T, _T, _T]
Quadruple_t: typing.TypeAlias = tuple[_T, _T, _T, _T]


class PyObjectBase(object): ...


# ParameterPy.cpp
class ParameterGrp:
    """Python interface class to set parameters"""

    def GetGroup(self, str: str, /) -> FreeCAD.ParameterGrp:
        """GetGroup(str)"""

    def RemGroup(self, str: str, /) -> None:
        """RemGroup(str)"""

    def HasGroup(self, str: str, /) -> bool:
        """HasGroup(str)"""

    def IsEmpty(self) -> bool:
        """IsEmpty()"""

    def Clear(self) -> None:
        """Clear()"""

    def Attach(self, arg1, /) -> None:
        """Attach()"""

    def Detach(self, arg1, /) -> None:
        """Detach()"""

    def Notify(self, arg1: str, /) -> None:
        """Notify()"""

    def NotifyAll(self) -> None:
        """NotifyAll()"""

    def SetBool(self, arg1: str, arg2: int, /) -> None:
        """SetBool()"""

    def GetBool(self, arg1: str, arg2: int = None, /) -> bool:
        """GetBool()"""

    def RemBool(self, arg1: str, /) -> None:
        """RemBool()"""

    def SetInt(self, arg1: str, arg2: int, /) -> None:
        """SetInt()"""

    def GetInt(self, arg1: str, arg2: int = None, /) -> int:
        """GetInt()"""

    def RemInt(self, arg1: str, /) -> None:
        """RemInt()"""

    def SetUnsigned(self, arg1: str, arg2: int, /) -> None:
        """SetUnsigned()"""

    def GetUnsigned(self, arg1: str, arg2: int = None, /) -> int:
        """GetUnsigned()"""

    def RemUnsigned(self, arg1: str, /) -> None:
        """RemUnsigned()"""

    def SetFloat(self, arg1: str, arg2: float, /) -> None:
        """SetFloat()"""

    def GetFloat(self, arg1: str, arg2: float = None, /) -> float:
        """GetFloat()"""

    def RemFloat(self, arg1: str, /) -> None:
        """RemFloat()"""

    def SetString(self, arg1: str, arg2: str, /) -> None:
        """SetString()"""

    def GetString(self, arg1: str, arg2: str = None, /) -> str:
        """GetString()"""

    def RemString(self, arg1: str, /) -> None:
        """RemString()"""

    def Import(self, arg1: str, /) -> None:
        """Import()"""

    def Insert(self, arg1: str, /) -> None:
        """Insert()"""

    def Export(self, arg1: str, /) -> None:
        """Export()"""

    def GetContents(self) -> object | None:
        """GetContents()"""


# MaterialPy.xml
class Material(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    This is the Material class
    """

    def __init__(self, DiffuseColor=None, AmbientColor=None, SpecularColor=None, EmissiveColor=None, Shininess=None, Transparency=None):
        """This is the Material class"""

    @property
    def AmbientColor(self) -> tuple[float, float, float, float]:
        """Ambient color"""

    @AmbientColor.setter
    def AmbientColor(self, value: tuple): ...

    @property
    def DiffuseColor(self) -> tuple[float, float, float, float]:
        """Diffuse color"""

    @DiffuseColor.setter
    def DiffuseColor(self, value: tuple): ...

    @property
    def EmissiveColor(self) -> tuple[float, float, float, float]:
        """Emissive color"""

    @EmissiveColor.setter
    def EmissiveColor(self, value: tuple): ...

    @property
    def Shininess(self) -> float:
        """Shininess"""

    @Shininess.setter
    def Shininess(self, value: float): ...

    @property
    def SpecularColor(self) -> tuple[float, float, float, float]:
        """Specular color"""

    @SpecularColor.setter
    def SpecularColor(self, value: tuple): ...

    @property
    def Transparency(self) -> float:
        """Transparency"""

    @Transparency.setter
    def Transparency(self, value: float): ...

    def set(self, arg1: str, /):
        """
        Set(string) -- Set the material.

        The material must be one of the following values:
        Brass, Bronze, Copper, Gold, Pewter, Plaster, Plastic, Silver, Steel, Stone, Shiny plastic,
        Satin, Metalized, Neon GNC, Chrome, Aluminium, Obsidian, Neon PHC, Jade, Ruby or Emerald.
        """


# DocumentObjectGroupPy.xml
class DocumentObjectGroup(FreeCAD.DocumentObject, FreeCAD.GroupExtension):
    """This class handles document objects in group"""


# GeoFeaturePy.xml
class GeoFeature(FreeCAD.DocumentObject):
    """This class does the whole placement and position handling"""

    @property
    def Placement(self) -> FreeCAD.Placement:
        """Property TypeId: App::PropertyPlacement."""

    @Placement.setter
    def Placement(self, value: FreeCAD.Matrix | FreeCAD.Placement): ...

    def getGlobalPlacement(self) -> FreeCAD.Placement:
        """
        Returns the placement of the object in the global coordinate space, respecting all stacked relationships. 
                          Note: This function is not available during recompute, as there the placements of parents can change 
                          after the execution of this object, rendering the result wrong.
        Possible exceptions: (RuntimeError).
        """

    def getPropertyNameOfGeometry(self) -> str | None:
        """
        Returns the property name of the actual geometry or None.
        For example for a part object it returns the value Shape,
        for a mesh the value Mesh and so on.
        If an object has no such property then None is returned.
        """


# DocumentObjectPy.xml
class DocumentObject(FreeCAD.ExtensionContainer):
    """This is the father of all classes handled by the document"""

    @property
    def Proxy(self) -> FreeCADTemplates.ProxyPython: ...

    @Proxy.setter
    def Proxy(self, value: FreeCADTemplates.ProxyPython): ...

    @property
    def Document(self) -> FreeCAD.Document:
        """Return the document this object is part of"""

    @property
    def InList(self) -> list[FreeCAD.DocumentObject]:
        """A list of all objects which link to this object."""

    @property
    def InListRecursive(self) -> list[FreeCAD.DocumentObject]:
        """A list of all objects which link to this object recursively."""

    @property
    def Name(self) -> str:
        """Return the internal name of this object"""

    @property
    def OutList(self) -> list[FreeCAD.DocumentObject]:
        """A list of all objects this object links to."""

    @property
    def OutListRecursive(self) -> list[FreeCAD.DocumentObject]:
        """A list of all objects this object links to recursively."""

    @property
    def State(self) -> list[typing.Literal["Touched", "Invalid", "Recompute", "Recompute2", "Restore", "Expanded", "Partial", "Importing", "Up-to-date"]]:
        """State of the object in the document"""

    @property
    def ViewObject(self) -> FreeCADGui.ViewProviderDocumentObject | None:
        """
        If the GUI is loaded the associated view provider is returned
        or None if the GUI is not up
        """

    @property
    def ExpressionEngine(self) -> list[tuple[str, str]]:
        """
        [Prop_Hidden] Property won't appear in the editor.
        Property group: Base.
        Property TypeId: App::PropertyExpressionEngine.
        Property expressions.
        """

    @property
    def Label(self) -> str:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Base.
        Property TypeId: App::PropertyString.
        User name of the object (UTF8).
        """

    @Label.setter
    def Label(self, value: str): ...

    def addProperty(self, arg1: str, arg2: str = None, arg3: str = None, arg4: str = None, arg5: int = None, arg6: bool = None, arg7: bool = None, /) -> FreeCAD.DocumentObject:
        """
        addProperty(string, string) -- Add a generic property.
                            The first argument specifies the type, the second the
                            name of the property.
                
        Possible exceptions: (RuntimeError, Exception).
        """

    def getParentGeoFeatureGroup(self) -> object | None:
        """
        Returns the GeoFeatureGroup, and hence the local coorinate system, the object 
                                  is in or None if it is not part of a group. Note that an object can only be 
                                  in a single group, hence only a single return value.
        Possible exceptions: (RuntimeError).
        """

    def getParentGroup(self) -> FreeCAD.DocumentObjectGroup | None:
        """
        Returns the group the object is in or None if it is not part of a group. 
                                  Note that an object can only be in a single group, hence only a single return 
                                  value.
        Possible exceptions: (RuntimeError).
        """

    def getPathsByOutList(self, arg1: FreeCAD.DocumentObject, /) -> list[list]:
        """
        Get all paths from this object to another object following the OutList.
        Possible exceptions: (RuntimeError).
        """

    def purgeTouched(self):
        """Mark the object as unchanged"""

    def recompute(self) -> bool:
        """
        Recomputes this object
        Possible exceptions: (RuntimeError).
        """

    def removeProperty(self, string: str, /) -> bool:
        """
        removeProperty(string) -- Remove a generic property.
                            Note, you can only remove user-defined properties but not built-in ones.
                
        Possible exceptions: (RuntimeError).
        """

    def setExpression(self, arg1: str, arg2, arg3: str = None, /):
        """
        Register an expression for a property
        Possible exceptions: (TypeError).
        """

    def supportedProperties(self) -> list[str]:
        """A list of supported property types"""

    def touch(self):
        """Mark the object as changed (touched)"""


# PartPy.xml
class Part(FreeCAD.DocumentObject):
    """This class handles document objects in Part"""

    @property
    def Color(self) -> tuple[float, float, float, float]:
        """Property TypeId: App::PropertyColor."""

    @Color.setter
    def Color(self, value: Triple_t[float] | Quadruple_t[float] | int): ...

    @property
    def Id(self) -> str:
        """
        Property TypeId: App::PropertyString.
        ID (Part-Number) of the Item.
        """

    @Id.setter
    def Id(self, value: str): ...

    @property
    def License(self) -> str:
        """
        Property TypeId: App::PropertyString.
        License string of the Item.
        """

    @License.setter
    def License(self, value: str): ...

    @property
    def LicenseURL(self) -> str:
        """
        Property TypeId: App::PropertyString.
        URL to the license text/contract.
        """

    @LicenseURL.setter
    def LicenseURL(self, value: str): ...

    @property
    def Material(self) -> dict[str, str]:
        """
        Property TypeId: App::PropertyMap.
        Map with material properties.
        """

    @Material.setter
    def Material(self, value: dict[str, str]): ...

    @property
    def Meta(self) -> dict[str, str]:
        """
        Property TypeId: App::PropertyMap.
        Map with additional meta information.
        """

    @Meta.setter
    def Meta(self, value: dict[str, str]): ...

    @property
    def Type(self) -> str:
        """Property TypeId: App::PropertyString."""

    @Type.setter
    def Type(self, value: str): ...

    @property
    def Uid(self) -> str:
        """
        Property TypeId: App::PropertyUUID.
        UUID of the Item.
        """

    @Uid.setter
    def Uid(self, value: str): ...


# DocumentObjectExtensionPy.xml
class DocumentObjectExtension(FreeCAD.Extension):
    """Base class for all document object extensions"""


# GroupExtensionPy.xml
class GroupExtension(FreeCAD.DocumentObjectExtension):
    """Extension class which allows grouping of document objects"""

    @property
    def Group(self) -> list[DocumentObject]: ...

    @Group.setter
    def Group(self, value: list[DocumentObject]): ...

    def addObject(self, arg1: FreeCAD.DocumentObject, /) -> list[FreeCAD.DocumentObject]:
        """
        Add an object to the group. Returns all objects that have been added.
        Possible exceptions: (FreeCAD.FreeCADError).
        """

    def addObjects(self, arg1, /) -> list[FreeCAD.DocumentObject]:
        """Adds multiple objects to the group. Expects a list and returns all objects that have been added."""

    def getObject(self, arg1: str, /) -> FreeCAD.DocumentObject:
        """Return the object with the given name"""

    def hasObject(self, obj: FreeCAD.DocumentObject, recursive=False, /) -> bool:
        """
        hasObject(obj, recursive=false)
                        Checks if the group has a given object
                        @param obj        the object to check for.
                        @param recursive  if true check also if the obj is child of some sub group (default is false).
            
        Possible exceptions: (FreeCAD.FreeCADError, ValueError).
        """

    def newObject(self, arg1: str, arg2: str = None, /) -> FreeCAD.DocumentObject:
        """Create and add an object with given type and name to the group"""

    def removeObject(self, arg1: FreeCAD.DocumentObject, /) -> list[FreeCAD.DocumentObject]:
        """
        Remove an object from the group and returns all objects that have been removed.
        Possible exceptions: (FreeCAD.FreeCADError).
        """

    def removeObjects(self, arg1, /) -> list[FreeCAD.DocumentObject]:
        """Remove multiple objects from the group. Expects a list and returns all objects that have been removed."""

    def removeObjectsFromDocument(self):
        """Remove all child objects from the group and document"""

    def setObjects(self, arg1, /) -> list[FreeCAD.DocumentObject]:
        """Sets the objects of the group. Expects a list and returns all objects that are now in the group."""


# ExtensionPy.xml
class Extension(FreeCAD.PyObjectBase):
    """Base class for all extensions"""


# GeoFeatureGroupExtensionPy.xml
class GeoFeatureGroupExtension(FreeCAD.GroupExtension):
    """This class handles placeable group of document objects"""


# OriginGroupExtensionPy.xml
class OriginGroupExtension(FreeCAD.GeoFeatureGroupExtension):
    """This class handles placable group of document objects with an Origin"""


# ExtensionContainerPy.xml
class ExtensionContainer(FreeCAD.PropertyContainer):
    """Base class for all objects which can be extended"""

    def addExtension(self, arg1: str, arg2, /):
        """
        Adds an extension to the object. Requires the string identifier as well as the python object 
                          used to check for overridden functions (most likely self)
        Possible exceptions: (Exception).
        """

    def hasExtension(self, arg1: str, /) -> bool:
        """
        Returns if this object has the specified extension
        Possible exceptions: (Exception).
        """


# DocumentPy.xml
class Document(FreeCAD.PropertyContainer):
    """This is a Document class"""

    @property
    def ActiveObject(self) -> FreeCAD.DocumentObject | None:
        """The active object of the document"""

    @property
    def DependencyGraph(self) -> str:
        """The dependency graph as GraphViz text"""

    @property
    def Name(self) -> str:
        """The internal name of the document"""

    @property
    def Objects(self) -> list[FreeCAD.DocumentObject]:
        """The list of object handled by this document"""

    @property
    def RecomputesFrozen(self) -> bool:
        """Returns or sets if automatic recomputes for this document are disabled."""

    @property
    def RedoCount(self) -> int:
        """Number of possible Redos"""

    @property
    def RedoNames(self) -> list[str]:
        """A List of Redo names"""

    @property
    def RootObjects(self) -> list[FreeCAD.DocumentObject]:
        """The list of root object of this document"""

    @property
    def TopologicalSortedObjects(self) -> list[FreeCAD.DocumentObject]:
        """The list of object of this document in topological sorted order"""

    @property
    def UndoCount(self) -> int:
        """Number of possible Undos"""

    @property
    def UndoMode(self) -> int:
        """The Undo mode of the Document (0 = no Undo, 1 = Undo/Redo)"""

    @UndoMode.setter
    def UndoMode(self, value: int): ...

    @property
    def UndoNames(self) -> list[str]:
        """A list of Undo names"""

    @property
    def UndoRedoMemSize(self) -> int:
        """The size of the Undo stack in byte"""

    @property
    def Comment(self) -> str:
        """
        Property TypeId: App::PropertyString.
        Additional tag to save a comment.
        """

    @Comment.setter
    def Comment(self, value: str): ...

    @property
    def Company(self) -> str:
        """
        Property TypeId: App::PropertyString.
        Additional tag to save the name of the company.
        """

    @Company.setter
    def Company(self, value: str): ...

    @property
    def CreatedBy(self) -> str:
        """
        Property TypeId: App::PropertyString.
        The creator of the document.
        """

    @CreatedBy.setter
    def CreatedBy(self, value: str): ...

    @property
    def CreationDate(self) -> str:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        Property TypeId: App::PropertyString.
        Date of creation.
        """

    @property
    def FileName(self) -> str:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Transient] Property content won't be saved to file, but still saves name, type and status.
        Property TypeId: App::PropertyString.
        The path to the file where the document is saved to.
        """

    @property
    def Id(self) -> str:
        """
        Property TypeId: App::PropertyString.
        ID of the document.
        """

    @Id.setter
    def Id(self, value: str): ...

    @property
    def Label(self) -> str:
        """
        Property TypeId: App::PropertyString.
        The name of the document.
        """

    @Label.setter
    def Label(self, value: str): ...

    @property
    def LastModifiedBy(self) -> str:
        """Property TypeId: App::PropertyString."""

    @LastModifiedBy.setter
    def LastModifiedBy(self, value: str): ...

    @property
    def LastModifiedDate(self) -> str:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        Property TypeId: App::PropertyString.
        Date of last modification.
        """

    @property
    def License(self) -> str:
        """
        Property TypeId: App::PropertyString.
        License string of the Item.
        """

    @License.setter
    def License(self, value: str): ...

    @property
    def License(self) -> str:
        """
        Property TypeId: App::PropertyString.
        License string of the Item.
        """

    @License.setter
    def License(self, value: str): ...

    @property
    def LicenseURL(self) -> str:
        """
        Property TypeId: App::PropertyString.
        URL to the license text/contract.
        """

    @LicenseURL.setter
    def LicenseURL(self, value: str): ...

    @property
    def LicenseURL(self) -> str:
        """
        Property TypeId: App::PropertyString.
        URL to the license text/contract.
        """

    @LicenseURL.setter
    def LicenseURL(self, value: str): ...

    @property
    def Material(self) -> dict[str, str]:
        """
        Property TypeId: App::PropertyMap.
        Map with material properties.
        """

    @Material.setter
    def Material(self, value: dict[str, str]): ...

    @property
    def Meta(self) -> dict[str, str]:
        """
        Property TypeId: App::PropertyMap.
        Map with additional meta information.
        """

    @Meta.setter
    def Meta(self, value: dict[str, str]): ...

    @property
    def Tip(self) -> FreeCAD.DocumentObject | None:
        """
        [Prop_Transient] Property content won't be saved to file, but still saves name, type and status.
        Property TypeId: App::PropertyLink.
        Link of the tip object of the document.
        """

    @Tip.setter
    def Tip(self, value: FreeCAD.DocumentObject | None): ...

    @property
    def TipName(self) -> str:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Hidden] Property won't appear in the editor.
        Property TypeId: App::PropertyString.
        Link of the tip object of the document.
        """

    @property
    def TransientDir(self) -> str:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Transient] Property content won't be saved to file, but still saves name, type and status.
        Property TypeId: App::PropertyString.
        Transient directory, where the files live while the document is open.
        """

    @property
    def Uid(self) -> str:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        Property TypeId: App::PropertyUUID.
        UUID of the document.
        """

    def abortTransaction(self):
        """Abort an Undo/Redo transaction (rollback)"""

    def addObject(self, arg1: str, arg2: str = None, arg3=None, arg4=None, /) -> FreeCAD.DocumentObject:
        """
        Add an object with given type and name to the document
        Possible exceptions: (Exception).
        """

    def clearUndos(self):
        """Clear the undo stack of the document"""

    def commitTransaction(self):
        """Commit an Undo/Redo transaction"""

    def copyObject(self, object: FreeCAD.DocumentObject, bool_with_dependencies: bool = False, bool_ignored_argument: bool = False, /) -> FreeCAD.DocumentObject:
        """
        copyObject(object, bool with_dependencies = False, bool ignored_argument = False)
                Copy an object from another document to this document. If with_dependencies is True, all objects this object depends on are copied too.
        Possible exceptions: (Exception).
        """

    def exportGraphviz(self, arg1: str = None, /) -> str:
        """Export the dependencies of the objects as graph"""

    def findObjects(self, string_type_: str = None, string_name_: str = None, /) -> list[FreeCAD.DocumentObject]:
        """
        findObjects([string (type)], [string (name)]) -> list
        Return a list of objects that match the specified type and name.
        Both parameters are optional.
        Possible exceptions: (RuntimeError).
        """

    def getObject(self, arg1: str, /) -> FreeCAD.DocumentObject:
        """Return the object with the given name"""

    def getObjectsByLabel(self, arg1: str, /) -> list[FreeCAD.DocumentObject]:
        """
        Return the objects with the given label name.
        NOTE: It's possible that several objects have the same label name.
        """

    def getTempFileName(self, arg1, /) -> str:
        """
        Returns a file name with path in the temp directory of the document.
        Possible exceptions: (TypeError).
        """

    def load(self, arg1: str, /):
        """Load the document from the given path"""

    def mergeProject(self, arg1: str, /):
        """Merges this document with another project file"""

    def moveObject(self, arg1: str, /):
        """
        moveObject(object, bool with_dependencies = False)
                Transfers an object from another document to this document. If with_dependencies is True, all objects this object depends on are transferred too.
        Possible exceptions: (Exception).
        """

    def openTransaction(self, arg1=None, /):
        """
        Open a new Undo/Redo transaction.
        Possible exceptions: (TypeError).
        """

    def recompute(self) -> int:
        """
        Recompute the document and returns the amount of recomputed features
        Possible exceptions: (RuntimeError).
        """

    def redo(self):
        """Redo a previosly undid transaction"""

    def removeObject(self, arg1: str, /):
        """
        Remove an object from the document
        Possible exceptions: (Exception).
        """

    def restore(self):
        """Restore the document from disk"""

    def save(self):
        """
        Save the document to disk
        Possible exceptions: (ValueError, IOError, RuntimeError).
        """

    def saveAs(self, arg1: str, /):
        """
        Save the document under a new name to disk
        Possible exceptions: (ValueError, IOError, RuntimeError).
        """

    def saveCopy(self, arg1: str, /):
        """Save a copy of the document under a new name to disk"""

    def supportedTypes(self) -> list[str]:
        """A list of supported types of objects"""

    def undo(self):
        """Undo one transaction"""


# PropertyContainerPy.xml
class PropertyContainer(FreeCAD.Persistence):
    """This is a Persistence class"""

    @property
    def PropertiesList(self) -> list[str]:
        """A list of all property names"""

    def getDocumentationOfProperty(self, arg1: str, /) -> str:
        """Return the documentation string of the property of this class."""

    def getEditorMode(self, arg1: str, /) -> list[str]:
        """
        Get the behaviour of the property in the property editor.
        It returns a list of strings with the current mode. If the list is empty there are no special restrictions.
        If the list contains 'ReadOnly' then the item appears in the property editor but is disabled.
        If the list contains 'Hidden' then the item even doesn't appear in the property editor.
        """

    def getGroupOfProperty(self, arg1: str, /) -> str:
        """Return the name of the group which the property belongs to in this class. The properties sorted in different named groups for convenience."""

    def getPropertyByName(self, arg1: str, /) -> FreeCAD.Property:
        """Return the value of a named property."""

    def getTypeIdOfProperty(self, arg1: str, /) -> str:
        """Returns the C++ class name of a named property."""

    def getTypeOfProperty(self, arg1: str, /) -> list[str]:
        """Return the type of a named property. This can be (Hidden,ReadOnly,Output) or any combination."""

    @typing.overload
    def setEditorMode(self, arg1: str, arg2: int, /): ...

    @typing.overload
    def setEditorMode(self, arg1: str, arg2, /):
        """
        Set the behaviour of the property in the property editor.
        0 - default behaviour
        1 - item is ready-only
        2 - item is hidden
                
        Possible exceptions: (TypeError).
        """


# ComplexGeoDataPy.xml
class ComplexGeoData(FreeCAD.Persistence):
    """Father of all complex geometric data types"""

    @property
    def BoundBox(self) -> FreeCAD.BoundBox:
        """Get the BoundBox of the object"""

    @property
    def Matrix(self) -> FreeCAD.Matrix:
        """Get the current transformation of the object as matrix"""

    @Matrix.setter
    def Matrix(self, value: FreeCAD.Matrix): ...

    @property
    def Placement(self) -> FreeCAD.Placement:
        """Get the current transformation of the object as placement"""

    @Placement.setter
    def Placement(self, value: FreeCAD.Placement): ...

    def getFacesFromSubelement(self, arg1: str, arg2: int, /) -> tuple[list[FreeCAD.Vector], list[tuple[int, int, int]]]:
        """
        Return vertexes and faces from a sub-element
        Possible exceptions: (RuntimeError).
        """


# ApplicationPy.cpp
def ParamGet(arg0: str, /):
    """Get parameters by path"""


def saveParameter(config: str = 'User parameter', /) -> None:
    """
    saveParameter(config='User parameter') -> None
    Save parameter set to file. The default set is 'User parameter'
    """


def Version() -> list[str]:
    """Print the version to the output."""


def ConfigGet(string: str, /) -> str:
    """ConfigGet(string) -- Get the value for the given key."""


def ConfigSet(string: str, string1: str, /) -> None:
    """ConfigSet(string, string) -- Set the given key to the given value."""


def ConfigDump() -> dict[str, str]:
    """Dump the configuration to the output."""


def addImportType(arg0: str, arg1: str, /):
    """Register filetype for import"""


def getImportType(arg0: str = None, /) -> list[str] | dict[object, str | list[str] | None]:
    """Get the name of the module that can import the filetype"""


def EndingAdd(arg0: str, arg1: str, /):
    """deprecated -- use addImportType"""


def EndingGet(arg0: str = None, /) -> list[str] | dict[object, str | list[str] | None]:
    """deprecated -- use getImportType"""


def addExportType(arg0: str, arg1: str, /):
    """Register filetype for export"""


def getExportType(arg0: str = None, /) -> list[str] | dict[object, str | list[str] | None]:
    """Get the name of the module that can export the filetype"""


def getResourceDir() -> str:
    """Get the root directory of all resources"""


def getUserAppDataDir() -> str:
    """Get the root directory of user settings"""


def getUserMacroDir() -> str:
    """Get the directory of the user's macro directory"""


def getHelpDir() -> str:
    """Get the directory of the documentation"""


def getHomePath() -> str:
    """Get the home path, i.e. the parent directory of the executable"""


def loadFile(arg0: str, arg1: str = None, arg2: str = None, /):
    """
    loadFile(string=filename,[string=module]) -> None

    Loads an arbitrary file by delegating to the given Python module:
    * If no module is given it will be determined by the file extension.
    * If more than one module can load a file the first one one will be taken.
    * If no module exists to load the file an exception will be raised.
    """


def open(arg0: str, /):
    """See openDocument(string)"""


def openDocument(string: str, /):
    """
    openDocument(string) -> object

    Create a document and load the project file into the document.
    The string argument must point to an existing file. If the file doesn't exist
    or the file cannot be loaded an I/O exception is thrown. In this case the
    document is kept alive.
    """


def newDocument(arg0: str = None, arg1: str = None, /) -> FreeCAD.Document:
    """
    newDocument([string]) -> object

    Create a new document with a given name.
    The document name must be unique which
    is checked automatically.
    """


def closeDocument(string: str, /):
    """
    closeDocument(string) -> None

    Close the document with a given name.
    """


def activeDocument() -> FreeCAD.Document:
    """
    activeDocument() -> object or None

    Return the active document or None if there is no one.
    """


def setActiveDocument(arg0: str, /):
    """
    setActiveDocement(string) -> None

    Set the active document by its name.
    """


def getDocument(string: str, /) -> FreeCADGui.Document:
    """
    getDocument(string) -> object

    Get a document by its name or raise an exception
    if there is no document with the given name.
    """


def listDocuments() -> dict[str, object]:
    """
    listDocuments() -> list

    Return a list of names of all documents.
    """


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


def setLogLevel(tag: str, level, /) -> None:
    """
    setLogLevel(tag, level) -- Set the log level for a string tag.
    'level' can either be string 'Log', 'Msg', 'Wrn', 'Error', or an integer value
    """


def getLogLevel(tag: str, /) -> int:
    """getLogLevel(tag) -- Get the log level of a string tag"""



App = FreeCAD
Log = FreeCAD.Console.PrintLog
Msg = FreeCAD.Console.PrintMessage
Err = FreeCAD.Console.PrintError
Wrn = FreeCAD.Console.PrintWarning
# be careful with following variables -
# some of them are set in FreeCADGui (GuiUp after InitApplications),
# so may not exist when accessible until FreeCADGuiInit is initialized - use `getattr`
GuiUp: typing.Literal[0, 1]
Gui = FreeCADGui
ActiveDocument: FreeCAD.Document
