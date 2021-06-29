import typing

from FreeCAD.Base import *
import FreeCAD
import FreeCAD.Base
import FreeCAD.Console
import FreeCAD.UnitsApiPy as Units
import FreeCAD.__Translate__ as Qt
import FreeCADGui
import FreeCADTemplates


class PyObjectBase(object): ...


# MaterialPy.xml
class Material(FreeCAD.PyObjectBase):
    """This is the Material class"""

    def __init__(self, DiffuseColor: object = None, AmbientColor: object = None, SpecularColor: object = None, EmissiveColor: object = None, Shininess: object = None, Transparency: object = None):
        """This is the Material class"""

    @property
    def AmbientColor(self) -> tuple:
        """Ambient color"""

    @AmbientColor.setter
    def AmbientColor(self, value: tuple): ...

    @property
    def DiffuseColor(self) -> tuple:
        """Diffuse color"""

    @DiffuseColor.setter
    def DiffuseColor(self, value: tuple): ...

    @property
    def EmissiveColor(self) -> tuple:
        """Emissive color"""

    @EmissiveColor.setter
    def EmissiveColor(self, value: tuple): ...

    @property
    def Shininess(self) -> float:
        """Shininess"""

    @Shininess.setter
    def Shininess(self, value: float): ...

    @property
    def SpecularColor(self) -> tuple:
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
class DocumentObjectGroup(FreeCAD.DocumentObject):
    """This class handles document objects in group"""


# GeoFeaturePy.xml
class GeoFeature(FreeCAD.DocumentObject):
    """This class does the whole placement and position handling"""

    def getGlobalPlacement(self):
        """Returns the placement of the object in the global coordinate space, respecting all stacked relationships. 
                          Note: This function is not available during recompute, as there the placements of parents can change 
                          after the execution of this object, rendering the result wrong."""

    def getPropertyNameOfGeometry(self):
        """Returns the property name of the actual geometry or None.
        For example for a part object it returns the value Shape,
        for a mesh the value Mesh and so on.
        If an object has no such property then None is returned."""


# DocumentObjectPy.xml
class DocumentObject(FreeCAD.ExtensionContainer):
    """This is the father of all classes handled by the document"""

    @property
    def Label(self) -> str: ...

    @Label.setter
    def Label(self, value: str): ...

    @property
    def Proxy(self) -> FreeCADTemplates.ProxyPython: ...

    @Proxy.setter
    def Proxy(self, value: FreeCADTemplates.ProxyPython): ...

    @property
    def Document(self) -> object:
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
    def State(self) -> list[FreeCAD.DocumentObject]:
        """State of the object in the document"""

    @property
    def ViewObject(self) -> typing.Optional[FreeCADGui.ViewProviderDocumentObject]:
        """If the GUI is loaded the associated view provider is returned
        or None if the GUI is not up"""

    def addProperty(self, arg1: str, arg2: str = None, arg3: str = None, arg4: str = None, arg5: int = None, arg6: bool = None, arg7: bool = None, /):
        """
                            addProperty(string, string) -- Add a generic property.
                            The first argument specifies the type, the second the
                            name of the property.
                        """

    def enforceRecompute(self):
        """Mark the object for recompute"""

    def getParentGeoFeatureGroup(self):
        """Returns the GeoFeatureGroup, and hence the local coorinate system, the object 
                                  is in or None if it is not part of a group. Note that an object can only be 
                                  in a single group, hence only a single return value."""

    def getParentGroup(self):
        """Returns the group the object is in or None if it is not part of a group. 
                                  Note that an object can only be in a single group, hence only a single return 
                                  value."""

    def getPathsByOutList(self, arg1: FreeCAD.DocumentObject, /):
        """Get all paths from this object to another object following the OutList."""

    def purgeTouched(self):
        """Mark the object as unchanged"""

    def recompute(self):
        """Recomputes this object"""

    def removeProperty(self, string: str, /):
        """
                            removeProperty(string) -- Remove a generic property.
                            Note, you can only remove user-defined properties but not built-in ones.
                        """

    @typing.overload
    def setExpression(self, arg1: str, arg2: object, arg3: str = None, /): ...

    @typing.overload
    def setExpression(self): ...

    @typing.overload
    def setExpression(self, arg1: FreeCAD.DocumentObject, /):
        """Register an expression for a property"""

    def supportedProperties(self):
        """A list of supported property types"""

    def touch(self):
        """Mark the object as changed (touched)"""


# PartPy.xml
class Part(FreeCAD.GeoFeature):
    """This class handles document objects in Part"""


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

    def addObject(self, arg1: FreeCAD.DocumentObject, /):
        """Add an object to the group. Returns all objects that have been added."""

    def addObjects(self, arg1: object, /):
        """Adds multiple objects to the group. Expects a list and returns all objects that have been added."""

    def getObject(self, arg1: str, /):
        """Return the object with the given name"""

    def hasObject(self, obj: FreeCAD.DocumentObject, recursive: object = False, /):
        """hasObject(obj, recursive=false)
                        Checks if the group has a given object
                        @param obj        the object to check for.
                        @param recursive  if true check also if the obj is child of some sub group (default is false).
                    """

    def newObject(self, arg1: str, arg2: str = None, /):
        """Create and add an object with given type and name to the group"""

    def removeObject(self, arg1: FreeCAD.DocumentObject, /):
        """Remove an object from the group and returns all objects that have been removed."""

    def removeObjects(self, arg1: object, /):
        """Remove multiple objects from the group. Expects a list and returns all objects that have been removed."""

    def removeObjectsFromDocument(self):
        """Remove all child objects from the group and document"""

    def setObjects(self, arg1: object, /):
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

    def addExtension(self, arg1: str, arg2: object, /):
        """Adds an extension to the object. Requires the string identifier as well as the python object 
                          used to check for overridden functions (most likely self)"""

    def hasExtension(self, arg1: str, /):
        """Returns if this object has the specified extension"""


# DocumentPy.xml
class Document(FreeCAD.PropertyContainer):
    """This is a Document class"""

    @property
    def ActiveObject(self) -> object:
        """The active object of the document"""

    @property
    def DependencyGraph(self) -> str:
        """The dependency graph as GraphViz text"""

    @property
    def Name(self) -> str:
        """The internal name of the document"""

    @property
    def Objects(self) -> list:
        """The list of object handled by this document"""

    @property
    def RecomputesFrozen(self) -> bool:
        """Returns or sets if automatic recomputes for this document are disabled."""

    @property
    def RedoCount(self) -> int:
        """Number of possible Redos"""

    @property
    def RedoNames(self) -> list:
        """A List of Redo names"""

    @property
    def RootObjects(self) -> list:
        """The list of root object of this document"""

    @property
    def TopologicalSortedObjects(self) -> list:
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
    def UndoNames(self) -> list:
        """A list of Undo names"""

    @property
    def UndoRedoMemSize(self) -> int:
        """The size of the Undo stack in byte"""

    def abortTransaction(self):
        """Abort an Undo/Redo transaction (rollback)"""

    def addObject(self, arg1: str, arg2: str = None, arg3: object = None, arg4: object = None, /):
        """Add an object with given type and name to the document"""

    def clearUndos(self):
        """Clear the undo stack of the document"""

    def commitTransaction(self):
        """Commit an Undo/Redo transaction"""

    def copyObject(self, object: FreeCAD.DocumentObject, bool_with_dependencies: bool = False, bool_ignored_argument: bool = False, /):
        """copyObject(object, bool with_dependencies = False, bool ignored_argument = False)
                Copy an object from another document to this document. If with_dependencies is True, all objects this object depends on are copied too."""

    def exportGraphviz(self, arg1: str = None, /):
        """Export the dependencies of the objects as graph"""

    def findObjects(self, string_type_: str = None, string_name_: str = None, /):
        """findObjects([string (type)], [string (name)]) -> list
        Return a list of objects that match the specified type and name.
        Both parameters are optional."""

    def getObject(self, arg1: str, /):
        """Return the object with the given name"""

    def getObjectsByLabel(self, arg1: str, /):
        """Return the objects with the given label name.
        NOTE: It's possible that several objects have the same label name."""

    def getTempFileName(self, arg1: object, /):
        """Returns a file name with path in the temp directory of the document."""

    def load(self, arg1: str, /):
        """Load the document from the given path"""

    def mergeProject(self, arg1: str, /):
        """Merges this document with another project file"""

    def moveObject(self, arg1: str, /):
        """moveObject(object, bool with_dependencies = False)
                Transfers an object from another document to this document. If with_dependencies is True, all objects this object depends on are transferred too."""

    def openTransaction(self, arg1: object = None, /):
        """Open a new Undo/Redo transaction."""

    def recompute(self):
        """Recompute the document and returns the amount of recomputed features"""

    def redo(self):
        """Redo a previously undone transaction"""

    def removeObject(self, arg1: str, /):
        """Remove an object from the document"""

    def restore(self):
        """Restore the document from disk"""

    def save(self):
        """Save the document to disk"""

    def saveAs(self, arg1: str, /):
        """Save the document under a new name to disk"""

    def saveCopy(self, arg1: str, /):
        """Save a copy of the document under a new name to disk"""

    def supportedTypes(self):
        """A list of supported types of objects"""

    def undo(self):
        """Undo one transaction"""


# PropertyContainerPy.xml
class PropertyContainer(FreeCAD.Persistence):
    """This is a Persistence class"""

    @property
    def PropertiesList(self) -> list:
        """A list of all property names"""

    def dumpPropertyContent(self, Property: str, Compression: int = 1-9):
        """Dumps the content of the property, both the XML representation as well as the additional datafiles  
        required, into a byte representation. It will be returned as byte array.
        dumpPropertyContent(propertyname) -- returns a byte array with full content
        dumpPropertyContent(propertyname, [Compression=1-9]) -- Sets the data compression from 0 (no) to 9 (max)
                        """

    def getDocumentationOfProperty(self, arg1: str, /):
        """Return the documentation string of the property of this class."""

    def getEditorMode(self, arg1: str, /):
        """Get the behaviour of the property in the property editor.
        It returns a list of strings with the current mode. If the list is empty there are no special restrictions.
        If the list contains 'ReadOnly' then the item appears in the property editor but is disabled.
        If the list contains 'Hidden' then the item even doesn't appear in the property editor.
                        """

    def getGroupOfProperty(self, arg1: str, /):
        """Return the name of the group which the property belongs to in this class. The properties sorted in different named groups for convenience."""

    def getPropertyByName(self, arg1: str, /):
        """Return the value of a named property."""

    def getTypeIdOfProperty(self, arg1: str, /):
        """Returns the C++ class name of a named property."""

    def getTypeOfProperty(self, arg1: str, /):
        """Return the type of a named property. This can be (Hidden,ReadOnly,Output) or any combination. """

    def restorePropertyContent(self, propertyname: str, buffer: object, /):
        """Restore the content of given property from a byte representation as stored by "dumpContent".
        It could be restored from any python object implementing the buffer protocol.
        restorePropertyContent(propertyname, buffer) -- restores from the given byte array
                        """

    @typing.overload
    def setEditorMode(self, arg1: str, arg2: int, /): ...

    @typing.overload
    def setEditorMode(self, arg1: str, arg2: object, /):
        """Set the behaviour of the property in the property editor.
        0 - default behaviour
        1 - item is ready-only
        2 - item is hidden
                        """


# ComplexGeoDataPy.xml
class ComplexGeoData(FreeCAD.Persistence):
    """Father of all complex geometric data types"""

    @property
    def BoundBox(self) -> object:
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

    def getFacesFromSubelement(self, arg1: str, arg2: int, /):
        """Return vertexes and faces from a sub-element"""


# ApplicationPy.cpp
def ParamGet(arg1: str, /):
    """Get parameters by path"""


def saveParameter(config: str = 'User parameter', /):
    """saveParameter(config='User parameter') -> None
    Save parameter set to file. The default set is 'User parameter'"""


def Version():
    """Print the version to the output."""


def ConfigGet(string: str, /):
    """ConfigGet(string) -- Get the value for the given key."""


def ConfigSet(string: str, string1: str, /):
    """ConfigSet(string, string) -- Set the given key to the given value."""


def ConfigDump():
    """Dump the configuration to the output."""


def addImportType(arg1: str, arg2: str, /):
    """Register filetype for import"""


def getImportType(arg1: str = None, /):
    """Get the name of the module that can import the filetype"""


def EndingAdd(arg1: str, arg2: str, /):
    """deprecated -- use addImportType"""


def EndingGet(arg1: str = None, /):
    """deprecated -- use getImportType"""


def addExportType(arg1: str, arg2: str, /):
    """Register filetype for export"""


def getExportType(arg1: str = None, /):
    """Get the name of the module that can export the filetype"""


def getResourceDir():
    """Get the root directory of all resources"""


def getUserAppDataDir():
    """Get the root directory of user settings"""


def getUserMacroDir(bool: bool = False, /):
    """getUserMacroDir(bool=False) -> stringGet the directory of the user's macro directory
    If parameter is False (the default) it returns the standard path in theuser's home directory, otherwise it returns the user-defined path."""


def getHelpDir():
    """Get the directory of the documentation"""


def getHomePath():
    """Get the home path, i.e. the parent directory of the executable"""


def loadFile(arg1: str, arg2: str = None, arg3: str = None, /):
    """loadFile(string=filename,[string=module]) -> None

    Loads an arbitrary file by delegating to the given Python module:
    * If no module is given it will be determined by the file extension.
    * If more than one module can load a file the first one one will be taken.
    * If no module exists to load the file an exception will be raised."""


def open(arg1: str, /):
    """See openDocument(string)"""


def openDocument(string: str, /):
    """openDocument(string) -> object

    Create a document and load the project file into the document.
    The string argument must point to an existing file. If the file doesn't exist
    or the file cannot be loaded an I/O exception is thrown. In this case the
    document is kept alive."""


def newDocument(arg1: str = None, arg2: str = None, /):
    """newDocument([string]) -> object

    Create a new document with a given name.
    The document name must be unique which
    is checked automatically."""


def closeDocument(string: str, /):
    """closeDocument(string) -> None

    Close the document with a given name."""


def activeDocument():
    """activeDocument() -> object or None

    Return the active document or None if there is no one."""


def setActiveDocument(arg1: str, /):
    """setActiveDocement(string) -> None

    Set the active document by its name."""


def getDocument(string: str, /):
    """getDocument(string) -> object

    Get a document by its name or raise an exception
    if there is no document with the given name."""


def listDocuments():
    """listDocuments() -> list

    Return a list of names of all documents."""


def addDocumentObserver(arg1: object, /):
    """addDocumentObserver() -> None

    Add an observer to get notified about changes on documents."""


def removeDocumentObserver(arg1: object, /):
    """removeDocumentObserver() -> None

    Remove an added document observer."""


def setLogLevel(tag: str, level: object, /):
    """setLogLevel(tag, level) -- Set the log level for a string tag.
    'level' can either be string 'Log', 'Msg', 'Wrn', 'Error', or an integer value"""


def getLogLevel(tag: str, /):
    """getLogLevel(tag) -- Get the log level of a string tag"""


GuiUp: typing.Literal[0, 1]
Gui = FreeCADGui
ActiveDocument: Document
