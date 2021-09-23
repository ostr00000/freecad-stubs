import typing

from FreeCAD.Base import *
import FreeCAD
import FreeCAD.Base
import FreeCAD.Console
import FreeCAD.Qt as Qt
import FreeCAD.UnitsApiPy as Units
import FreeCADGui
import FreeCADTemplates


class PyObjectBase(object): ...


# ParameterPy.cpp
class ParameterGrp:
    """Python interface class to set parameters"""

    def GetGroup(self, str: str, /):
        """GetGroup(str)"""

    def GetGroups(self):
        """GetGroups()"""

    def RemGroup(self, str: str, /):
        """RemGroup(str)"""

    def HasGroup(self, str: str, /):
        """HasGroup(str)"""

    def IsEmpty(self):
        """IsEmpty()"""

    def Clear(self):
        """Clear()"""

    def Attach(self, arg1: object, /):
        """Attach()"""

    def Detach(self, arg1: object, /):
        """Detach()"""

    def Notify(self, arg1: str, /):
        """Notify()"""

    def NotifyAll(self):
        """NotifyAll()"""

    def SetBool(self, arg1: str, arg2: int, /):
        """SetBool()"""

    def GetBool(self, arg1: str, arg2: int = None, /):
        """GetBool()"""

    def GetBools(self, arg1: str = None, /):
        """GetBools()"""

    def RemBool(self, arg1: str, /):
        """RemBool()"""

    def SetInt(self, arg1: str, arg2: int, /):
        """SetInt()"""

    def GetInt(self, arg1: str, arg2: int = None, /):
        """GetInt()"""

    def GetInts(self, arg1: str = None, /):
        """GetInts()"""

    def RemInt(self, arg1: str, /):
        """RemInt()"""

    def SetUnsigned(self, arg1: str, arg2: int, /):
        """SetUnsigned()"""

    def GetUnsigned(self, arg1: str, arg2: int = None, /):
        """GetUnsigned()"""

    def GetUnsigneds(self, arg1: str = None, /):
        """GetUnsigneds()"""

    def RemUnsigned(self, arg1: str, /):
        """RemUnsigned()"""

    def SetFloat(self, arg1: str, arg2: float, /):
        """SetFloat()"""

    def GetFloat(self, arg1: str, arg2: float = None, /):
        """GetFloat()"""

    def GetFloats(self, arg1: str = None, /):
        """GetFloats()"""

    def RemFloat(self, arg1: str, /):
        """RemFloat()"""

    def SetString(self, arg1: str, arg2: str, /):
        """SetString()"""

    def GetString(self, arg1: str, arg2: str = None, /):
        """GetString()"""

    def GetStrings(self, arg1: str = None, /):
        """GetStrings()"""

    def RemString(self, arg1: str, /):
        """RemString()"""

    def Import(self, arg1: str, /):
        """Import()"""

    def Insert(self, arg1: str, /):
        """Insert()"""

    def Export(self, arg1: str, /):
        """Export()"""

    def GetContents(self):
        """GetContents()"""


# Sequencer.cpp
class ProgressIndicator:
    """
    This class can be imported.
    Progress indicator
    """

    def start(self, string: str, int: int, /):
        """start(string,int)"""

    def next(self, arg1: int = None, /):
        """next()"""

    def stop(self):
        """stop()"""


# MaterialPy.xml
class Material(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    This is the Material class
    """

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
    """
    This class can be imported.
    This class handles document objects in group
    """


# GeoFeaturePy.xml
class GeoFeature(FreeCAD.DocumentObject):
    """
    This class can be imported.
    This class does the whole placement and position handling
    """

    @property
    def Placement(self):
        """
        [Prop_NoRecompute] Modified property doesn't touch its container for recompute.
        Property TypeId: PropertyPlacement.
        """

    @Placement.setter
    def Placement(self, value): ...

    def getGlobalPlacement(self):
        """
        Returns the placement of the object in the global coordinate space, respecting all stacked relationships. 
                          Note: This function is not available during recompute, as there the placements of parents can change 
                          after the execution of this object, rendering the result wrong.
        """

    def getPropertyNameOfGeometry(self):
        """
        Returns the property name of the actual geometry or None.
        For example for a part object it returns the value Shape,
        for a mesh the value Mesh and so on.
        If an object has no such property then None is returned.
        """

    def getPropertyOfGeometry(self):
        """
        Returns the property of the actual geometry or None.
        For example for a part object it returns its Shape property,
        for a mesh its Mesh property and so on.
        If an object has no such property then None is returned.
        Unlike to getPropertyNameOfGeometry this function returns the geometry,
        not its name.
        """


# DocumentObjectPy.xml
class DocumentObject(FreeCAD.ExtensionContainer):
    """
    This class can be imported.
    This is the father of all classes handled by the document
    """

    @property
    def Proxy(self) -> FreeCADTemplates.ProxyPython: ...

    @Proxy.setter
    def Proxy(self, value: FreeCADTemplates.ProxyPython): ...

    @property
    def Document(self) -> FreeCAD.Document:
        """Return the document this object is part of"""

    @property
    def FullName(self) -> str:
        """Return the document name and internal name of this object"""

    @property
    def ID(self) -> int:
        """The unique identifier (among its document) of this object"""

    @property
    def InList(self) -> list[FreeCAD.DocumentObject]:
        """A list of all objects which link to this object."""

    @property
    def InListRecursive(self) -> list[FreeCAD.DocumentObject]:
        """A list of all objects which link to this object recursively."""

    @property
    def MustExecute(self) -> bool:
        """Check if the object must be recomputed"""

    @property
    def Name(self) -> str:
        """Return the internal name of this object"""

    @property
    def NoTouch(self) -> bool:
        """Enable/disable no touch on any property change"""

    @property
    def OldLabel(self) -> str:
        """Contains the old label before change"""

    @property
    def OutList(self) -> list[FreeCAD.DocumentObject]:
        """A list of all objects this object links to."""

    @property
    def OutListRecursive(self) -> list[FreeCAD.DocumentObject]:
        """A list of all objects this object links to recursively."""

    @property
    def Parents(self) -> list[tuple[FreeCAD.DocumentObject, str]]:
        """A List of tuple(parent,subname) holding all parents to this object"""

    @property
    def Removing(self) -> bool:
        """Indicate if the object is being removed"""

    @property
    def State(self) -> list[typing.Literal["Touched", "Invalid", "Recompute", "Recompute2", "Restore", "Expanded", "Partial", "Importing", "Up-to-date"]]:
        """State of the object in the document"""

    @property
    def ViewObject(self) -> typing.Optional[FreeCADGui.ViewProviderDocumentObject]:
        """
        If the GUI is loaded the associated view provider is returned
        or None if the GUI is not up
        """

    @property
    def ExpressionEngine(self):
        """
        [Prop_Hidden] Property won't appear in the editor.
        Property group: Base.
        Property TypeId: PropertyExpressionEngine.
        Property expressions.
        """

    @ExpressionEngine.setter
    def ExpressionEngine(self, value): ...

    @property
    def Label(self) -> str:
        """
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Base.
        Property TypeId: PropertyString.
        User name of the object (UTF8).
        """

    @Label.setter
    def Label(self, value: str): ...

    @property
    def Label2(self) -> str:
        """
        [Prop_Hidden] Property won't appear in the editor.
        Property group: Base.
        Property TypeId: PropertyString.
        User description of the object (UTF8).
        """

    @Label2.setter
    def Label2(self, value: str): ...

    @property
    def Visibility(self) -> int | bool:
        """Property TypeId: PropertyBool."""

    @Visibility.setter
    def Visibility(self, value: int | bool): ...

    def addProperty(self, arg1: str, arg2: str = None, arg3: str = None, arg4: str = None, arg5: int = None, arg6: bool = None, arg7: bool = None, /):
        """
        addProperty(string, string) -- Add a generic property.
                            The first argument specifies the type, the second the
                            name of the property.
        """

    def adjustRelativeLinks(self, parent: FreeCAD.DocumentObject, recursive: object = True, /):
        """adjustRelativeLinks(parent,recursive=True) -- auto correct potential cyclic dependencies"""

    def enforceRecompute(self):
        """Mark the object for recompute"""

    @classmethod
    def evalExpression(cls, arg1: str, /):
        """Evaluate an expression"""

    def getLinkedObject(self, recursive: object = True, matrix: object = None, transform: object = True, depth: int = 0):
        """
        getLinkedObject(recursive=True, matrix=None, transform=True, depth=0)
        Returns the linked object if there is one, or else return itself

        * recursive: whether to recursively resolve the links

        * transform: whether to transform the sub object using this object's placement

        * matrix: If not none, this specifies the initial transformation to be applied
        to the sub object. And cause the method to return a tuple (object, matrix)
        containing the accumulated transformation matrix

        * depth: current recursive depth
        """

    def getParentGeoFeatureGroup(self):
        """
        Returns the GeoFeatureGroup, and hence the local coordinate system, the object 
                                  is in or None if it is not part of a group. Note that an object can only be 
                                  in a single group, hence only a single return value.
        """

    def getParentGroup(self):
        """
        Returns the group the object is in or None if it is not part of a group. 
                                  Note that an object can only be in a single group, hence only a single return 
                                  value.
        """

    def getPathsByOutList(self, arg1: FreeCAD.DocumentObject, /):
        """Get all paths from this object to another object following the OutList."""

    def getStatusString(self):
        """
        Returns the status of the object as string.
        If the object is invalid its error description will be returned.
        If the object is valid but touched then 'Touched' will be returned,
        'Valid' otherwise.
        """

    def getSubObject(self, subname: object, retType: int = 0, matrix: object = None, transform: object = True, depth: int = 0):
        """
        getSubObject(subname, retType=0, matrix=None, transform=True, depth=0)

        * subname(string|list|tuple): dot separated string or sequence of strings
        referencing subobject.

        * retType: return type, 0=PyObject, 1=DocObject, 2=DocAndPyObject, 3=Placement

            PyObject: return a python binding object for the (sub)object referenced in
            each 'subname' The actual type of 'PyObject' is implementation dependent.
            For Part::Feature compatible objects, this will be of type TopoShapePy and
            pre-transformed by accumulated transformation matrix along the object path.  

            DocObject:  return the document object referenced in subname, if 'matrix' is
            None. Or, return a tuple (object, matrix) for each 'subname' and 'matrix' is
            the accumulated transformation matrix for the sub object.

            DocAndPyObject: return a tuple (object, matrix, pyobj) for each subname

            Placement: return a transformed placement of the sub-object

        * matrix: the initial transformation to be applied to the sub object.

        * transform: whether to transform the sub object using this object's placement

        * depth: current recursive depth
        """

    def getSubObjectList(self, subname: str, /):
        """
        getSubObjectList(subname)

        Return a list of objects referenced by a given subname including this object
        """

    def getSubObjects(self, reason: int = 0, /):
        """getSubObjects(reason=0): Return subname reference of all sub-objects"""

    def hasChildElement(self):
        """Return true to indicate the object having child elements"""

    def isElementVisible(self, element: str, /):
        """
        isElementVisible(element): Check if a child element is visible
        Return -1 if element visibility is not supported or element not found, 0 if invisible, or else 1
        """

    def isValid(self):
        """Returns True if the object is valid, False otherwise"""

    def purgeTouched(self):
        """Mark the object as unchanged"""

    def recompute(self, recursive: object = False, /):
        """recompute(recursive=False): Recomputes this object"""

    def removeProperty(self, string: str, /):
        """
        removeProperty(string) -- Remove a generic property.
                            Note, you can only remove user-defined properties but not built-in ones.
        """

    def resolve(self, subname: str, /):
        """
        resolve(subname) -- resolve the sub object

        Returns a tuple (subobj,parent,elementName,subElement), where 'subobj' is the
        last object referenced in 'subname', and 'parent' is the direct parent of
        'subobj', and 'elementName' is the name of the subobj, which can be used
        to call parent.isElementVisible/setElementVisible(). 'subElement' is the
        non-object sub-element name if any.
        """

    def resolveSubElement(self, subname: str, append: object = None, type: int = None, /):
        """
        resolveSubElement(subname,append,type) -- resolve both new and old style sub element

        subname: subname reference containing object hierarchy
        append: Whether to append object hierarchy prefix inside subname to returned element name
        type: 0: normal, 1: for import, 2: for export

        Return tuple(obj,newElementName,oldElementName)
        """

    def setElementVisible(self, element: str, visible: object = None, /):
        """
        setElementVisible(element,visible): Set the visibility of a child element
        Return -1 if element visibility is not supported, 0 if element not found, 1 if success
        """

    def setExpression(self, arg1: str, arg2: object, arg3: str = None, /):
        """Register an expression for a property"""

    def supportedProperties(self):
        """A list of supported property types"""

    def touch(self, arg1: str = None, /):
        """Mark the object as changed (touched)"""


# LinkBaseExtensionPy.xml
class LinkBaseExtension(FreeCAD.DocumentObjectExtension):
    """
    This class can be imported.
    Link extension base class
    """

    @property
    def LinkedChildren(self) -> list:
        """Return a flattened (in case grouped by plain group) list of linked children"""

    @property
    def _ChildCache(self):
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Hidden] Property won't appear in the editor.
        [Prop_NoPersist] Property won't be saved to file at all.
        Property group: Link.
        Property TypeId: PropertyLinkList.
        """

    @property
    def _LinkOwner(self) -> int:
        """
        [Prop_Hidden] Property won't appear in the editor.
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Link.
        Property TypeId: PropertyInteger.
        """

    @_LinkOwner.setter
    def _LinkOwner(self, value: int): ...

    @property
    def _LinkTouched(self) -> int | bool:
        """
        [Prop_Hidden] Property won't appear in the editor.
        [Prop_NoPersist] Property won't be saved to file at all.
        Property group: Link.
        Property TypeId: PropertyBool.
        """

    @_LinkTouched.setter
    def _LinkTouched(self, value: int | bool): ...

    def cacheChildLabel(self, enable: object = True, /):
        """
        cacheChildLabel(enable=True): enable/disable child label cache

        The cache is not updated on child label change for performance reason. You must
        call this function on any child label change
        """

    @typing.overload
    def configLinkProperty(self, key, arg): ...

    @typing.overload
    def configLinkProperty(self):
        """
        configLinkProperty(key=val,...): property configuration
        configLinkProperty(key,...): property configuration with default name

        This methode is here to implement what I called Property Design
        Pattern. The extension operates on a predefined set of properties,
        but it relies on the extended object to supply the actual property by
        calling this methode. You can choose a sub set of functionality of
        this extension by supplying only some of the supported properties. 

        The 'key' are names used to refer to properties supported by this
        extension, and 'val' is the actual name of the property of your
        object. You can obtain the key names and expected types using
        getLinkPropertyInfo().  You can use property of derived type when
        calling configLinkProperty().  Other types will cause exception to
        ben thrown. The actual properties supported may be different
        depending on the actual extension object underlying this python
        object.

        If 'val' is omitted, i.e. calling configLinkProperty(key,...), then
        it is assumed the the actually property name is the same as 'key'
        """

    def expandSubname(self, subname: str, /):
        """
        expandSubname(subname) -> string

        Return an expanded subname in case it references an object inside a linked plain group
        """

    def flattenSubname(self, subname: str, /):
        """
        flattenSubname(subname) -> string

        Return a flattened subname in case it references an object inside a linked plain group
        """

    def getLinkExtProperty(self, name: str, /):
        """getLinkExtProperty(name): return the property value by its predefined name"""

    def getLinkExtPropertyName(self, name: str, /):
        """getLinkExtPropertyName(name): lookup the property name by its predefined name"""

    @typing.overload
    def getLinkPropertyInfo(self): ...

    @typing.overload
    def getLinkPropertyInfo(self, index: int, /): ...

    @typing.overload
    def getLinkPropertyInfo(self, index: str, /): ...

    @typing.overload
    def getLinkPropertyInfo(self, name: int, /): ...

    @typing.overload
    def getLinkPropertyInfo(self, name: str, /):
        """
        getLinkPropertyInfo(): return a tuple of (name,type,doc) for all supported properties.

        getLinkPropertyInfo(index): return (name,type,doc) of a specific property

        getLinkPropertyInfo(name): return (type,doc) of a specific property
        """

    @typing.overload
    def setLink(self, obj, subName = None, subElements = None): ...

    @typing.overload
    def setLink(self, obj, arg): ...

    @typing.overload
    def setLink(self, arg, arg2):
        """
        setLink(obj,subName=None,subElements=None): Set link object.

        setLink([obj,...]),
        setLink([(obj,subName,subElements),...]),
        setLink({index:obj,...}),
        setLink({index:(obj,subName,subElements),...}): set link element of a link group.

        obj (DocumentObject): the object to link to. If this is None, then the link is cleared

        subName (String): Dot separated object path. 

        subElements (String|tuple(String)): non-object sub-elements, e.g. Face1, Edge2.
        """


# PartPy.xml
class Part(FreeCAD.GeoFeature):
    """
    This class can be imported.
    This class handles document objects in Part
    """

    @property
    def Color(self) -> tuple[float, float, float] | tuple[float, float, float, float] | int:
        """Property TypeId: App::PropertyColor."""

    @Color.setter
    def Color(self, value: tuple[float, float, float] | tuple[float, float, float, float] | int): ...

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
        """Property TypeId: PropertyString."""

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
    """
    This class can be imported.
    Base class for all document object extensions
    """


# GroupExtensionPy.xml
class GroupExtension(FreeCAD.DocumentObjectExtension):
    """
    This class can be imported.
    Extension class which allows grouping of document objects
    """

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
        """
        hasObject(obj, recursive=false)
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
    """
    This class can be imported.
    Base class for all extensions
    """


# GeoFeatureGroupExtensionPy.xml
class GeoFeatureGroupExtension(FreeCAD.GroupExtension):
    """
    This class can be imported.
    This class handles placeable group of document objects
    """


# OriginGroupExtensionPy.xml
class OriginGroupExtension(FreeCAD.GeoFeatureGroupExtension):
    """
    This class can be imported.
    This class handles placable group of document objects with an Origin
    """


# ExtensionContainerPy.xml
class ExtensionContainer(FreeCAD.PropertyContainer):
    """
    This class can be imported.
    Base class for all objects which can be extended
    """

    def addExtension(self, arg1: str, arg2: object = None, /):
        """Adds an extension to the object. Requires the string identifier for the python extension as argument"""

    def hasExtension(self, arg1: str, arg2: object = None, /):
        """Returns if this object has the specified extension"""


# DocumentPy.xml
class Document(FreeCAD.PropertyContainer):
    """
    This class can be imported.
    This is a Document class
    """

    @property
    def ActiveObject(self) -> typing.Optional[FreeCAD.DocumentObject]:
        """The active object of the document"""

    @property
    def DependencyGraph(self) -> str:
        """The dependency graph as GraphViz text"""

    @property
    def HasPendingTransaction(self) -> bool:
        """Check if there is a pending transaction"""

    @property
    def Importing(self) -> bool:
        """Indicate if the document is importing. Note the document will also report Restoring while importing"""

    @property
    def InList(self) -> list:
        """A list of all documents that link to this document."""

    @property
    def Name(self) -> str:
        """The internal name of the document"""

    @property
    def Objects(self) -> list:
        """The list of object handled by this document"""

    @property
    def OldLabel(self) -> str:
        """Contains the old label before change"""

    @property
    def OutList(self) -> list:
        """A list of all documents that this document links to."""

    @property
    def Partial(self) -> bool:
        """Indicate if the document is partially loaded"""

    @property
    def RecomputesFrozen(self) -> bool:
        """Returns or sets if automatic recomputes for this document are disabled."""

    @property
    def Recomputing(self) -> bool:
        """Indicate if the document is recomputing"""

    @property
    def RedoCount(self) -> int:
        """Number of possible Redos"""

    @property
    def RedoNames(self) -> list:
        """A List of Redo names"""

    @property
    def Restoring(self) -> bool:
        """Indicate if the document is restoring"""

    @property
    def RootObjects(self) -> list:
        """The list of root object of this document"""

    @property
    def Temporary(self) -> bool:
        """Check if this is a temporary document"""

    @property
    def TopologicalSortedObjects(self) -> list:
        """The list of object of this document in topological sorted order"""

    @property
    def Transacting(self) -> bool:
        """Indicate whether the document is undoing/redoing"""

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

    @property
    def Comment(self) -> str:
        """
        Property TypeId: PropertyString.
        Additional tag to save a comment.
        """

    @Comment.setter
    def Comment(self, value: str): ...

    @property
    def Company(self) -> str:
        """
        Property TypeId: PropertyString.
        Additional tag to save the name of the company.
        """

    @Company.setter
    def Company(self, value: str): ...

    @property
    def CreatedBy(self) -> str:
        """
        Property TypeId: PropertyString.
        The creator of the document.
        """

    @CreatedBy.setter
    def CreatedBy(self, value: str): ...

    @property
    def CreationDate(self) -> str:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        Property TypeId: PropertyString.
        Date of creation.
        """

    @property
    def FileName(self) -> str:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Transient] Property content won't be saved to file, but still saves name, type and status.
        Property TypeId: PropertyString.
        The path to the file where the document is saved to.
        """

    @property
    def Id(self) -> str:
        """
        Property TypeId: PropertyString.
        ID of the document.
        """

    @Id.setter
    def Id(self, value: str): ...

    @property
    def Label(self) -> str:
        """
        Property TypeId: PropertyString.
        The name of the document.
        """

    @Label.setter
    def Label(self, value: str): ...

    @property
    def LastModifiedBy(self) -> str:
        """Property TypeId: PropertyString."""

    @LastModifiedBy.setter
    def LastModifiedBy(self, value: str): ...

    @property
    def LastModifiedDate(self) -> str:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        Property TypeId: PropertyString.
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
    def ShowHidden(self) -> int | bool:
        """
        Property TypeId: PropertyBool.
        Whether to show hidden object items in the tree view.
        """

    @ShowHidden.setter
    def ShowHidden(self, value: int | bool): ...

    @property
    def Tip(self):
        """
        [Prop_Transient] Property content won't be saved to file, but still saves name, type and status.
        Property TypeId: PropertyLink.
        Link of the tip object of the document.
        """

    @Tip.setter
    def Tip(self, value): ...

    @property
    def TipName(self) -> str:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Hidden] Property won't appear in the editor.
        Property TypeId: PropertyString.
        Link of the tip object of the document.
        """

    @property
    def TransientDir(self) -> str:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Transient] Property content won't be saved to file, but still saves name, type and status.
        Property TypeId: PropertyString.
        Transient directory, where the files live while the document is open.
        """

    @property
    def Uid(self):
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        Property TypeId: PropertyUUID.
        UUID of the document.
        """

    def abortTransaction(self):
        """Abort an Undo/Redo transaction (rollback)"""

    def addObject(self, type: str, name: str = None, objProxy: object = None, viewProxy: object = None, attach: object = False, viewType: str = None):
        """
        addObject(type, name=None, objProxy=None, viewProxy=None, attach=False, viewType=None)

        Add an object to document

        type (String): the type of the document object to create.
        name (String): the optional name of the new object.
        objProxy (Object): the Python binding object to attach to the new document object.
        viewProxy (Object): the Python binding object to attach the view provider of this object.
        attach (Boolean): if True, then bind the document object first before adding to the document
                to allow Python code to override view provider type. Once bound, and before adding to
                the document, it will try to call Python binding object's attach(obj) method.
        viewType (String): override the view provider type directly, only effective when attach is False.
        """

    def clearUndos(self):
        """Clear the undo stack of the document"""

    def commitTransaction(self):
        """Commit an Undo/Redo transaction"""

    def copyObject(self, object: object, with_dependencies: object = False, return_all: object = False, /):
        """
        copyObject(object, with_dependencies=False, return_all=False)
        Copy an object or objects from another document to this document. 

        object: can either a single object or sequence of objects
        with_dependencies: if True, all internal dependent objects are copied too.
        return_all: if True, return all copied objects, or else return only the copied
                    object corresponding to the input objects.
        """

    def exportGraphviz(self, arg1: str = None, /):
        """Export the dependencies of the objects as graph"""

    def findObjects(self, Type: str = None, Name: str = None, Label: str = None):
        """
        findObjects([Type=string], [Name=string], [Label=string]) -> list
        Return a list of objects that match the specified type, name or label.
        Name and label support regular expressions. All parameters are optional.
        """

    def getDependentDocuments(self, sort: object = True, /):
        """
        getDependentDocuments(sort=True)

        Returns a list of documents that this document directly or indirectly links to including itself.

        sort: whether to topologically sort the return list
        """

    def getLinksTo(self, obj: object = None, options: int = 0, maxCount: int = 0, /):
        """
        getLinksTo(obj, options=0, maxCount=0): return objects linked to 'obj'

        options: 1: recursive, 2: check link array. Options can combine.
        maxCount: to limit the number of links returned
        """

    @typing.overload
    def getObject(self, arg1: str, /): ...

    @typing.overload
    def getObject(self, arg1: int, /):
        """Return the object with the given name"""

    def getObjectsByLabel(self, arg1: str, /):
        """
        Return the objects with the given label name.
        NOTE: It's possible that several objects have the same label name.
        """

    def getTempFileName(self, arg1: object, /):
        """Returns a file name with path in the temp directory of the document."""

    def importLinks(self, object_object_: object = None, /):
        """
        importLinks(object|[object...])

        Import any externally linked object given a list of objects in
        this document.  Any link type properties of the input objects
        will be automatically reassigned to the imported object

        If no object is given as input, it import all externally linked
        object of this document.
        """

    def load(self, arg1: str, /):
        """Load the document from the given path"""

    def mergeProject(self, arg1: str, /):
        """Merges this document with another project file"""

    def moveObject(self, arg1: str, /):
        """
        moveObject(object, bool with_dependencies = False)
        Transfers an object from another document to this document.
              
        object: can either a single object or sequence of objects
        with_dependencies: if True, all internal dependent objects are copied too.
        """

    def openTransaction(self, name: object = None, /):
        """
        openTransaction(name) - Open a new Undo/Redo transaction.

        This function no long creates a new transaction, but calls
        FreeCAD.setActiveTransaction(name) instead, which will auto creates a
        transaction with the given name when any change happed in any opened document.
        If more than one document is changed, all newly created transactions will have
        the same internal ID and will be undo/redo together.
        """

    def recompute(self, arg1: object = None, arg2: bool = None, arg3: bool = None, /):
        """recompute(objs=None): Recompute the document and returns the amount of recomputed features"""

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
    """
    This class can be imported.
    This is a Persistence class
    """

    @property
    def PropertiesList(self) -> list:
        """A list of all property names"""

    def dumpPropertyContent(self, Property: str, Compression: int = 1-9):
        """
        Dumps the content of the property, both the XML representation as well as the additional datafiles  
        required, into a byte representation. It will be returned as byte array.
        dumpPropertyContent(propertyname) -- returns a byte array with full content
        dumpPropertyContent(propertyname, [Compression=1-9]) -- Sets the data compression from 0 (no) to 9 (max)
        """

    def getDocumentationOfProperty(self, arg1: str, /):
        """Return the documentation string of the property of this class."""

    def getEditorMode(self, arg1: str, /):
        """
        Get the behaviour of the property in the property editor.
        It returns a list of strings with the current mode. If the list is empty there are no special restrictions.
        If the list contains 'ReadOnly' then the item appears in the property editor but is disabled.
        If the list contains 'Hidden' then the item even doesn't appear in the property editor.
        """

    def getEnumerationsOfProperty(self, arg1: str, /):
        """Return all enumeration strings of the property of this class or None if not a PropertyEnumeration."""

    def getGroupOfProperty(self, arg1: str, /):
        """Return the name of the group which the property belongs to in this class. The properties sorted in different named groups for convenience."""

    def getPropertyByName(self, name: str, checkOwner: int = 0, /):
        """
        getPropertyByName(name,checkOwner=0)

        Return the value of a named property. Note that the returned property may not
        always belong to this container (e.g. from a linked object).

        * name: name of the property
        * checkOwner:  0: just return the property
                       1: raise exception if not found or the property 
                          does not belong to this container
                       2: return a tuple(owner,property_value)
        """

    def getPropertyStatus(self, name: str = '', /):
        """
        getPropertyStatus(name=''): Get property status.

        name(String): property name. If name is empty, return a list of supported
        text names of the status.
        """

    def getPropertyTouchList(self, arg1: str, /):
        """Return a list of index of touched values for list type properties."""

    def getTypeIdOfProperty(self, arg1: str, /):
        """Returns the C++ class name of a named property."""

    def getTypeOfProperty(self, arg1: str, /):
        """Return the type of a named property. This can be (Hidden,ReadOnly,Output) or any combination."""

    def restorePropertyContent(self, propertyname: str, buffer: object, /):
        """
        Restore the content of given property from a byte representation as stored by "dumpContent".
        It could be restored from any python object implementing the buffer protocol.
        restorePropertyContent(propertyname, buffer) -- restores from the given byte array
        """

    @typing.overload
    def setEditorMode(self, arg1: str, arg2: int, /): ...

    @typing.overload
    def setEditorMode(self, arg1: str, arg2: object, /):
        """
        Set the behaviour of the property in the property editor.
        0 - default behaviour
        1 - item is ready-only
        2 - item is hidden
        """

    def setPropertyStatus(self, name: str, val: object, /):
        """
        setPropertyStatus(name,val): Set property status

        name(String): property name

        val(String|Int|[String|Int...]): text or integer value, or list/tuple of
        values. Call getPropertyStatus() to get a list of supported text value.
        If the text start with '-' or the integer value is negative, then the
        status is cleared.
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

    @property
    def Tag(self) -> int:
        """Geometry Tag"""

    def getFacesFromSubelement(self, arg1: str, arg2: int, /):
        """Return vertexes and faces from a sub-element"""


# ApplicationPy.cpp
def ParamGet(arg1: str, /):
    """Get parameters by path"""


def saveParameter(config: str = 'User parameter', /):
    """
    saveParameter(config='User parameter') -> None
    Save parameter set to file. The default set is 'User parameter'
    """


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


def changeImportModule(arg1: str, arg2: str, arg3: str, /):
    """Change the import module name of a registered filetype"""


def getImportType(arg1: str = None, /):
    """Get the name of the module that can import the filetype"""


def EndingAdd(arg1: str, arg2: str, /):
    """deprecated -- use addImportType"""


def EndingGet(arg1: str = None, /):
    """deprecated -- use getImportType"""


def addExportType(arg1: str, arg2: str, /):
    """Register filetype for export"""


def changeExportModule(arg1: str, arg2: str, arg3: str, /):
    """Change the export module name of a registered filetype"""


def getExportType(arg1: str = None, /):
    """Get the name of the module that can export the filetype"""


def getResourceDir():
    """Get the root directory of all resources"""


def getUserAppDataDir():
    """Get the root directory of user settings"""


def getUserMacroDir(bool: bool = False, /):
    """
    getUserMacroDir(bool=False) -> stringGet the directory of the user's macro directory
    If parameter is False (the default) it returns the standard path in theuser's home directory, otherwise it returns the user-defined path.
    """


def getHelpDir():
    """Get the directory of the documentation"""


def getHomePath():
    """Get the home path, i.e. the parent directory of the executable"""


def loadFile(arg1: str, arg2: str = None, arg3: str = None, /):
    """
    loadFile(string=filename,[string=module]) -> None

    Loads an arbitrary file by delegating to the given Python module:
    * If no module is given it will be determined by the file extension.
    * If more than one module can load a file the first one will be taken.
    * If no module exists to load the file an exception will be raised.
    """


def open(name: str, hidden: object = None):
    """See openDocument(string)"""


def openDocument(name: str, hidden: object = False):
    """
    openDocument(filepath,hidden=False) -> object
    Create a document and load the project file into the document.

    filepath: file path to an existing file. If the file doesn't exist
              or the file cannot be loaded an I/O exception is thrown.
              In this case the document is kept alive.
    hidden: whether to hide document 3D view.
    """


def newDocument(name: str = None, label: str = None, hidden: object = False, temp: object = False):
    """
    newDocument(name, label=None, hidden=False, temp=False) -> object
    Create a new document with a given name.

    name: unique document name which is checked automatically.
    label: optional user changeable label for the document.
    hidden: whether to hide document 3D view.
    temp: mark the document as temporary so that it will not be saved
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


def setActiveDocument(arg1: str, /):
    """
    setActiveDocement(string) -> None

    Set the active document by its name.
    """


def getDocument(string: str, /):
    """
    getDocument(string) -> object

    Get a document by its name or raise an exception
    if there is no document with the given name.
    """


def listDocuments(sort: object = False, /):
    """
    listDocuments(sort=False) -> list

    Return a list of names of all documents, optionally sort in dependency order.
    """


def addDocumentObserver(arg1: object, /):
    """
    addDocumentObserver() -> None

    Add an observer to get notified about changes on documents.
    """


def removeDocumentObserver(arg1: object, /):
    """
    removeDocumentObserver() -> None

    Remove an added document observer.
    """


def setLogLevel(tag: str, level: object, /):
    """
    setLogLevel(tag, level) -- Set the log level for a string tag.
    'level' can either be string 'Log', 'Msg', 'Wrn', 'Error', or an integer value
    """


def getLogLevel(tag: str, /):
    """getLogLevel(tag) -- Get the log level of a string tag"""


def checkLinkDepth(depth: int, /):
    """checkLinkDepth(depth) -- check link recursion depth"""


def getLinksTo(obj: object = None, options: int = 0, maxCount: int = 0, /):
    """
    getLinksTo(obj,options=0,maxCount=0) -- return the objects linked to 'obj'

    options: 1: recursive, 2: check link array. Options can combine.
    maxCount: to limit the number of links returned
    """


def getDependentObjects(arg1: object, arg2: int = None, /):
    """
    getDependentObjects(obj|[obj,...], options=0)
    Return a list of dependent objects including the given objects.

    options: can have the following bit flags,
             1: to sort the list in topological order.
             2: to exclude dependency of Link type object.
    """


def setActiveTransaction(name: str, persist: object = False, /):
    """
    setActiveTransaction(name, persist=False) -- setup active transaction with the given name

    name: the transaction name
    persist(False): by default, if the calling code is inside any invocation of a command, it
                    will be auto closed once all commands within the current stack exists. To
                    disable auto closing, set persist=True
    Returns the transaction ID for the active transaction. An application-wide
    active transaction causes any document changes to open a transaction with
    the given name and ID.
    """


def getActiveTransaction():
    """getActiveTransaction() -> (name,id) return the current active transaction name and ID"""


def closeActiveTransaction(arg1: object = None, arg2: int = None, /):
    """closeActiveTransaction(abort=False) -- commit or abort current active transaction"""


def isRestoring():
    """isRestoring() -> Bool -- Test if the application is opening some document"""


def checkAbort():
    """
    checkAbort() -- check for user abort in length operation.

    This only works if there is an active sequencer (or ProgressIndicator in Python).
    There is an active sequencer during document restore and recomputation. User may
    abort the operation by pressing the ESC key. Once detected, this function will
    trigger a BaseExceptionFreeCADAbort exception.
    """



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
