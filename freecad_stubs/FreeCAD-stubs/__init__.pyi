import typing

from FreeCAD.Base import *
import FreeCAD
import FreeCAD.Base
import FreeCAD.Console
import FreeCAD.Qt as Qt
import FreeCAD.Units as Units
import FreeCADGui
import FreeCADTemplates
import Mesh as MeshModule
import Part as PartModule
import Points as PointsModule

_T = typing.TypeVar("_T")
Triple_t: typing.TypeAlias = tuple[_T, _T, _T]
Quadruple_t: typing.TypeAlias = tuple[_T, _T, _T, _T]

class ReturnGetAuthorDict(typing.TypedDict):
    name: str
    email: str


class ReturnGetLicenseDict(typing.TypedDict):
    name: str
    file: str


class ReturnGetMaintainerDict(typing.TypedDict):
    name: str
    email: str


class ReturnGetUrlsDict(typing.TypedDict):
    location: str
    type: str
    branch: str


class ReturnGetGenericMetadataDict(typing.TypedDict):
    contents: str
    attributes: dict[typing.Any, str]



class PyObjectBase(object): ...


# ParameterPy.cpp
class ParameterGrp:
    """Python interface class to set parameters"""

    def GetGroup(self, pstr: str, /) -> FreeCAD.ParameterGrp:
        """
        GetGroup(str)
        Possible exceptions: (Exception, RuntimeError).
        """

    def GetGroupName(self) -> str:
        """
        GetGroupName()
        Possible exceptions: (Exception).
        """

    def GetGroups(self) -> list[str]:
        """
        GetGroups()
        Possible exceptions: (Exception).
        """

    def RemGroup(self, pstr: str, /) -> None:
        """
        RemGroup(str)
        Possible exceptions: (Exception).
        """

    def HasGroup(self, pstr: str, /) -> bool:
        """
        HasGroup(str)
        Possible exceptions: (Exception).
        """

    def Manager(self) -> FreeCAD.ParameterGrp | None:
        """
        Manager()
        Possible exceptions: (Exception).
        """

    def Parent(self) -> FreeCAD.ParameterGrp | None:
        """
        Parent()
        Possible exceptions: (Exception).
        """

    def IsEmpty(self) -> bool:
        """
        IsEmpty()
        Possible exceptions: (Exception).
        """

    def Clear(self) -> None:
        """
        Clear()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def Attach(self): ...

    @typing.overload
    def Attach(self, obj, /) -> None:
        """
        Attach()
        Possible exceptions: (Exception, TypeError, RuntimeError).
        """

    def AttachManager(self, obj, /) -> None:
        """
        AttachManager(observer) -- attach parameter manager for notification

        This method attaches a user defined observer to the manager (i.e. the root)
        of the current parameter group to receive notification of all its parameters
        and those from its sub-groups

        The method expects the observer to have a callable attribute as shown below
               slotParamChanged(param, tp, name, value)
        where 'param' is the parameter group causing the change, 'tp' is the type of
        the parameter, 'name' is the name of the parameter, and 'value' is the current
        value.

        The possible value of type are, 'FCBool', 'FCInt', 'FCUint', 'FCFloat', 'FCText',
        and 'FCParamGroup'. The notification is triggered when value is changed, in which
        case 'value' contains the new value in text form, or, when the parameter is removed,
        in which case 'value' is empty.

        For 'FCParamGroup' type, the observer will be notified in the following events.
        * Group creation: both 'name' and 'value' contain the name of the new group
        * Group removal: both 'name' and 'value' are empty
        * Group rename: 'name' is the new name, and 'value' is the old name
        Possible exceptions: (Exception, RuntimeError, TypeError).
        """

    @typing.overload
    def Detach(self): ...

    @typing.overload
    def Detach(self, obj, /) -> None:
        """
        Detach()
        Possible exceptions: (Exception, TypeError).
        """

    @typing.overload
    def Notify(self): ...

    @typing.overload
    def Notify(self, pstr: str, /) -> None:
        """
        Notify()
        Possible exceptions: (Exception).
        """

    def NotifyAll(self) -> None:
        """
        NotifyAll()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def SetBool(self): ...

    @typing.overload
    def SetBool(self, pstr: str, Bool: int, /) -> None:
        """
        SetBool()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def GetBool(self): ...

    @typing.overload
    def GetBool(self, pstr: str, Bool: int = 0, /) -> bool:
        """
        GetBool()
        Possible exceptions: (Exception).
        """

    def GetBools(self, filter: str = None, /) -> list[str]:
        """
        GetBools()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def RemBool(self): ...

    @typing.overload
    def RemBool(self, pstr: str, /) -> None:
        """
        RemBool()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def SetInt(self): ...

    @typing.overload
    def SetInt(self, pstr: str, Int: int, /) -> None:
        """
        SetInt()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def GetInt(self): ...

    @typing.overload
    def GetInt(self, pstr: str, Int: int = 0, /) -> int:
        """
        GetInt()
        Possible exceptions: (Exception).
        """

    def GetInts(self, filter: str = None, /) -> list[str]:
        """
        GetInts()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def RemInt(self): ...

    @typing.overload
    def RemInt(self, pstr: str, /) -> None:
        """
        RemInt()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def SetUnsigned(self): ...

    @typing.overload
    def SetUnsigned(self, pstr: str, UInt: int, /) -> None:
        """
        SetUnsigned()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def GetUnsigned(self): ...

    @typing.overload
    def GetUnsigned(self, pstr: str, UInt: int = 0, /) -> int:
        """
        GetUnsigned()
        Possible exceptions: (Exception).
        """

    def GetUnsigneds(self, filter: str = None, /) -> list[str]:
        """
        GetUnsigneds()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def RemUnsigned(self): ...

    @typing.overload
    def RemUnsigned(self, pstr: str, /) -> None:
        """
        RemUnsigned()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def SetFloat(self): ...

    @typing.overload
    def SetFloat(self, pstr: str, Float: float, /) -> None:
        """
        SetFloat()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def GetFloat(self): ...

    @typing.overload
    def GetFloat(self, pstr: str, Float: float = 0.0, /) -> float:
        """
        GetFloat()
        Possible exceptions: (Exception).
        """

    def GetFloats(self, filter: str = None, /) -> list[str]:
        """
        GetFloats()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def RemFloat(self): ...

    @typing.overload
    def RemFloat(self, pstr: str, /) -> None:
        """
        RemFloat()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def SetString(self): ...

    @typing.overload
    def SetString(self, pstr: str, str: str, /) -> None:
        """
        SetString()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def GetString(self): ...

    @typing.overload
    def GetString(self, pstr: str, str: str = '', /) -> str:
        """
        GetString()
        Possible exceptions: (Exception).
        """

    def GetStrings(self, filter: str = None, /) -> list[str]:
        """
        GetStrings()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def RemString(self): ...

    @typing.overload
    def RemString(self, pstr: str, /) -> None:
        """
        RemString()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def Import(self): ...

    @typing.overload
    def Import(self, pstr: str, /) -> None:
        """
        Import()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def Insert(self): ...

    @typing.overload
    def Insert(self, pstr: str, /) -> None:
        """
        Insert()
        Possible exceptions: (Exception).
        """

    @typing.overload
    def Export(self): ...

    @typing.overload
    def Export(self, pstr: str, /) -> None:
        """
        Export()
        Possible exceptions: (Exception).
        """

    def GetContents(self) -> list[tuple[str, str, str] | tuple[str, str, int] | tuple[str, str, float] | tuple[str, str, bool]] | None:
        """
        GetContents()
        Possible exceptions: (Exception).
        """


# ProgressIndicatorPy.cpp
class ProgressIndicator:
    """
    This class can be imported.
    Progress indicator
    """

    def start(self, text: str, steps: int, /) -> None:
        """
        start(string,int)
        Possible exceptions: (Exception).
        """

    def next(self, b: int = 0, /) -> None:
        """
        next()
        Possible exceptions: (Exception, RuntimeError).
        """

    def stop(self) -> None:
        """
        stop()
        Possible exceptions: (Exception).
        """


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

    def set(self, pstr: str, /):
        """
        Set(string) -- Set the material.

        The material must be one of the following values:
        Brass, Bronze, Copper, Gold, Pewter, Plaster, Plastic, Silver, Steel, Stone, Shiny plastic,
        Satin, Metalized, Neon GNC, Chrome, Aluminium, Obsidian, Neon PHC, Jade, Ruby or Emerald.
        """


# DocumentObjectGroupPy.xml
class DocumentObjectGroup(FreeCAD.DocumentObject, FreeCAD.GroupExtension):
    """
    This class can be imported.
    This class handles document objects in group
    """


# GeoFeaturePy.xml
class GeoFeature(FreeCAD.DocumentObject):
    """
    This class can be imported.
    App.GeoFeature class.

    Base class of all geometric document objects.
    This class does the whole placement and position handling.
    With the method `getPropertyOfGeometry` is possible to obtain
    the main geometric property in general form, without reference
    to any particular property name.
    """

    @property
    def Placement(self) -> FreeCAD.Placement:
        """
        [Prop_NoRecompute] Modified property doesn't touch its container for recompute.
        Property TypeId: App::PropertyPlacement.
        """

    @Placement.setter
    def Placement(self, value: FreeCAD.Matrix | FreeCAD.Placement): ...

    def getGlobalPlacement(self) -> FreeCAD.Placement:
        """
        getGlobalPlacement() -> Base.Placement

        Returns the placement of the object in the global coordinate space, respecting all stacked
        relationships.
        Note: This function is not available during recompute, as there the placements of parents
        can change after the execution of this object, rendering the result wrong.
        Possible exceptions: (RuntimeError).
        """

    def getPaths(self):
        """
        getPaths()

        Returns all possible paths to the root of the document.
        Note: Not implemented.
        Possible exceptions: (NotImplementedError).
        """

    def getPropertyNameOfGeometry(self) -> str | None:
        """
        getPropertyNameOfGeometry() -> str or None

        Returns the property name of the actual geometry.
        For example for a Part feature it returns the value 'Shape', for a mesh feature the value
        'Mesh' and so on.
        If an object has no such property then None is returned.
        """

    def getPropertyOfGeometry(self) -> MeshModule.MeshObject | PartModule.Shape | PointsModule.PointKernel | None:
        """
        getPropertyOfGeometry() -> object or None

        Returns the property of the actual geometry.
        For example for a Part feature it returns its Shape property, for a Mesh feature its
        Mesh property and so on.
        If an object has no such property then None is returned.
        Unlike to getPropertyNameOfGeometry this function returns the geometry, not its name.
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

    @property
    def Label2(self) -> str:
        """
        [Prop_Hidden] Property won't appear in the editor.
        Property group: Base.
        Property TypeId: App::PropertyString.
        User description of the object (UTF8).
        """

    @Label2.setter
    def Label2(self, value: str): ...

    @property
    def Visibility(self) -> bool:
        """Property TypeId: App::PropertyBool."""

    @Visibility.setter
    def Visibility(self, value: int | bool): ...

    def addProperty(self, sType: str, sName: str = None, sGroup: str = None, sDoc: str = None, attr: int = 0, ro: bool = False, hd: bool = False, /) -> FreeCAD.DocumentObject:
        """
        addProperty(string, string) -- Add a generic property.
                            The first argument specifies the type, the second the
                            name of the property.
        """

    def adjustRelativeLinks(self, pyobj: FreeCAD.DocumentObject, recursive=True, /) -> bool:
        """adjustRelativeLinks(parent,recursive=True) -- auto correct potential cyclic dependencies"""

    def clearExpression(self, path: str = None, /):
        """Clear the expression for a property"""

    def enforceRecompute(self):
        """Mark the object for recompute"""

    @classmethod
    def evalExpression(cls, expr: str, /):
        """Evaluate an expression"""

    def getLinkedObject(self, recursive: bool = True, matrix=None, transform: bool = True, depth: int = 0) -> tuple[FreeCAD.DocumentObject, FreeCAD.Matrix] | FreeCAD.DocumentObject:
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

    def getParentGeoFeatureGroup(self) -> typing.Any | None:
        """
        Returns the GeoFeatureGroup, and hence the local coordinate system, the object 
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

    def getPathsByOutList(self, o: FreeCAD.DocumentObject, /) -> list[list]:
        """
        Get all paths from this object to another object following the OutList.
        Possible exceptions: (RuntimeError).
        """

    def getStatusString(self) -> str:
        """
        Returns the status of the object as string.
        If the object is invalid its error description will be returned.
        If the object is valid but touched then 'Touched' will be returned,
        'Valid' otherwise.

        Possible exceptions: (RuntimeError).
        """

    def getSubObject(self, subname, retType: int = 0, matrix: FreeCAD.Matrix = None, transform: bool = True, depth: int = 0) -> typing.Any | FreeCAD.Placement | FreeCAD.Matrix | tuple[typing.Any, FreeCAD.Matrix, typing.Any] | tuple[typing.Any, ...] | None:
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
                
        Possible exceptions: (ValueError, TypeError).
        """

    def getSubObjectList(self, subname: str, /) -> list:
        """
        getSubObjectList(subname)

        Return a list of objects referenced by a given subname including this object
        """

    def getSubObjects(self, reason: int = 0, /) -> tuple[str, ...]:
        """getSubObjects(reason=0): Return subname reference of all sub-objects"""

    def hasChildElement(self) -> bool:
        """Return true to indicate the object having child elements"""

    def isElementVisible(self, element: str = None, /) -> int:
        """
        isElementVisible(element): Check if a child element is visible
        Return -1 if element visibility is not supported or element not found, 0 if invisible, or else 1
        """

    def isValid(self) -> bool:
        """
        Returns True if the object is valid, False otherwise
        Possible exceptions: (RuntimeError).
        """

    def purgeTouched(self):
        """Mark the object as unchanged"""

    def recompute(self, recursive: bool = False, /) -> bool:
        """
        recompute(recursive=False): Recomputes this object
        Possible exceptions: (RuntimeError).
        """

    def removeProperty(self, sName: str, /) -> bool:
        """
        removeProperty(string) -- Remove a generic property.
                            Note, you can only remove user-defined properties but not built-in ones.
        """

    def resolve(self, subname: str, /) -> tuple[typing.Any, typing.Any, str, str]:
        """
        resolve(subname) -- resolve the sub object

        Returns a tuple (subobj,parent,elementName,subElement), where 'subobj' is the
        last object referenced in 'subname', and 'parent' is the direct parent of
        'subobj', and 'elementName' is the name of the subobj, which can be used
        to call parent.isElementVisible/setElementVisible(). 'subElement' is the
        non-object sub-element name if any.
        """

    def resolveSubElement(self, subname: str, append: bool = False, type: int = 0, /) -> tuple[typing.Any, str, str]:
        """
        resolveSubElement(subname,append,type) -- resolve both new and old style sub element

        subname: subname reference containing object hierarchy
        append: Whether to append object hierarchy prefix inside subname to returned element name
        type: 0: normal, 1: for import, 2: for export

        Return tuple(obj,newElementName,oldElementName)
        """

    def setElementVisible(self, element: str = None, visible: bool = True, /) -> int:
        """
        setElementVisible(element,visible): Set the visibility of a child element
        Return -1 if element visibility is not supported, 0 if element not found, 1 if success
        """

    def setExpression(self, path: str = None, expr=None, comment: str = None, /):
        """
        Register an expression for a property
        Possible exceptions: (TypeError).
        """

    def supportedProperties(self) -> list[str]:
        """A list of supported property types"""

    def touch(self, propName: str = None, /):
        """
        Mark the object as changed (touched)
        Possible exceptions: (RuntimeError).
        """


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
    def _ChildCache(self) -> list[FreeCAD.DocumentObject | None]:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Hidden] Property won't appear in the editor.
        [Prop_NoPersist] Property won't be saved to file at all.
        Property group: Link.
        Property TypeId: App::PropertyLinkList.
        """

    @property
    def _LinkOwner(self) -> int:
        """
        [Prop_Hidden] Property won't appear in the editor.
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Link.
        Property TypeId: App::PropertyInteger.
        """

    @_LinkOwner.setter
    def _LinkOwner(self, value: int): ...

    @property
    def _LinkTouched(self) -> bool:
        """
        [Prop_Hidden] Property won't appear in the editor.
        [Prop_NoPersist] Property won't be saved to file at all.
        Property group: Link.
        Property TypeId: App::PropertyBool.
        """

    @_LinkTouched.setter
    def _LinkTouched(self, value: int | bool): ...

    def cacheChildLabel(self, enable=True, /):
        """
        cacheChildLabel(enable=True): enable/disable child label cache

        The cache is not updated on child label change for performance reason. You must
        call this function on any child label change
        """

    @typing.overload
    def configLinkProperty(self, key=None, *args): ...

    @typing.overload
    def configLinkProperty(self, key, /, *args): ...

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
        it is assumed that the actual property name is the same as 'key'
        """

    def expandSubname(self, subname: str, /) -> str:
        """
        expandSubname(subname) -> string

        Return an expanded subname in case it references an object inside a linked plain group
        """

    def flattenSubname(self, subname: str, /) -> str:
        """
        flattenSubname(subname) -> string

        Return a flattened subname in case it references an object inside a linked plain group
        """

    def getLinkExtProperty(self, name: str, /):
        """
        getLinkExtProperty(name): return the property value by its predefined name 
        Possible exceptions: (AttributeError).
        """

    def getLinkExtPropertyName(self, name: str, /) -> str:
        """
        getLinkExtPropertyName(name): lookup the property name by its predefined name 
        Possible exceptions: (AttributeError, RuntimeError).
        """

    @typing.overload
    def getLinkPropertyInfo(self) -> tuple[tuple[str, str, str], ...] | tuple[str, str, str] | tuple[str, str]: ...

    @typing.overload
    def getLinkPropertyInfo(self, index: int = 0, /) -> tuple[tuple[str, str, str], ...] | tuple[str, str, str] | tuple[str, str]: ...

    @typing.overload
    def getLinkPropertyInfo(self, name: str, /) -> tuple[tuple[str, str, str], ...] | tuple[str, str, str] | tuple[str, str]:
        """
        getLinkPropertyInfo(): return a tuple of (name,type,doc) for all supported properties.

        getLinkPropertyInfo(index): return (name,type,doc) of a specific property

        getLinkPropertyInfo(name): return (type,doc) of a specific property
        
        Possible exceptions: (ValueError).
        """

    @typing.overload
    def setLink(self, obj, /, subName=None, subElements=None): ...

    @typing.overload
    def setLink(self, obj, /, *args): ...

    @typing.overload
    def setLink(self, arg1, /, *args): ...

    @typing.overload
    def setLink(self, arg1, arg2, /):
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
    def Material(self) -> FreeCAD.DocumentObject | None:
        """
        Property TypeId: App::PropertyLink.
        The Material for this Part.
        """

    @Material.setter
    def Material(self, value: FreeCAD.DocumentObject | None): ...

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

    def addObject(self, object: FreeCAD.DocumentObject, /) -> list[FreeCAD.DocumentObject]:
        """
        Add an object to the group. Returns all objects that have been added.
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def addObjects(self, object, /) -> list[FreeCAD.DocumentObject]:
        """Adds multiple objects to the group. Expects a list and returns all objects that have been added."""

    def getObject(self, pcName: str, /) -> FreeCAD.DocumentObject:
        """Return the object with the given name"""

    def hasObject(self, object: FreeCAD.DocumentObject, recursivePy: bool = False, /) -> bool:
        """
        hasObject(obj, recursive=false)
                        Checks if the group has a given object
                        @param obj        the object to check for.
                        @param recursive  if true check also if the obj is child of some sub group (default is false).
            
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def newObject(self, sType: str, sName: str = None, /) -> FreeCAD.DocumentObject:
        """Create and add an object with given type and name to the group"""

    def removeObject(self, object: FreeCAD.DocumentObject, /) -> list[FreeCAD.DocumentObject]:
        """
        Remove an object from the group and returns all objects that have been removed.
        Possible exceptions: (FreeCAD.Base.FreeCADError).
        """

    def removeObjects(self, object, /) -> list[FreeCAD.DocumentObject]:
        """Remove multiple objects from the group. Expects a list and returns all objects that have been removed."""

    def removeObjectsFromDocument(self):
        """Remove all child objects from the group and document"""

    def setObjects(self, object, /) -> list[FreeCAD.DocumentObject]:
        """Sets the objects of the group. Expects a list and returns all objects that are now in the group."""


# ExtensionPy.xml
class Extension(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    Base class for all extensions
    """


# MetadataPy.xml
class Metadata(FreeCAD.PyObjectBase):
    """
    This class can be imported.
    App.Metadata class.

    A Metadata object reads an XML-formatted package metadata file and provides
    read and write access to its contents.

    The following constructors are supported:

    Metadata()
    Empty constructor.

    Metadata(metadata)
    Copy constructor.
    metadata : App.Metadata

    Metadata(file)
    Reads the XML file and provides access to the metadata it specifies.
    file : str
        XML file name.
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, filename: str, /): ...

    @typing.overload
    def __init__(self, o: FreeCAD.Metadata, /):
        """
        App.Metadata class.

        A Metadata object reads an XML-formatted package metadata file and provides
        read and write access to its contents.

        The following constructors are supported:

        Metadata()
        Empty constructor.

        Metadata(metadata)
        Copy constructor.
        metadata : App.Metadata

        Metadata(file)
        Reads the XML file and provides access to the metadata it specifies.
        file : str
            XML file name.
        Possible exceptions: (FreeCAD.Base.XMLBaseException, FreeCAD.Base.FreeCADError).
        """

    @property
    def Author(self) -> list[ReturnGetAuthorDict]:
        """
        List of author objects, each with a 'name' and a (potentially empty) 'email'
        string attribute.
        """

    @property
    def Classname(self) -> str:
        """
        String representing the name of the main Python class this item
        creates/represents.
        """

    @property
    def Conflict(self) -> list:
        """List of conflicts, format identical to dependencies."""

    @property
    def Content(self) -> dict[typing.Any, list[FreeCAD.Metadata]]:
        """
        Dictionary of lists of content items: defined recursively, each item is itself
        a Metadata object.
        See package.xml file format documentation for details.
        """

    @property
    def Date(self) -> str:
        """String representing the date of this item in YYYY-MM-DD format (format not currently programmatically enforced)"""

    @property
    def Depend(self) -> list:
        """
        List of dependencies, as objects with the following attributes:
        * package
            Required. Must exactly match the contents of the 'name' element in the
            referenced package's package.xml file.
        * version_lt
            Optional. The dependency to the package is restricted to versions less than
            the stated version number.
        * version_lte
            Optional. The dependency to the package is restricted to versions less or
            equal than the stated version number.
        * version_eq
            Optional. The dependency to the package is restricted to a version equal
            than the stated version number.
        * version_gte
            Optional. The dependency to the package is restricted to versions greater
            or equal than the stated version number.
        * version_gt
            Optional. The dependency to the package is restricted to versions greater
            than the stated version number.
        * condition
            Optional. Conditional expression as documented in REP149.
        """

    @property
    def Description(self) -> str:
        """String representing the description of this item (text only, no markup allowed)."""

    @property
    def File(self) -> list[str]:
        """
        List of files associated with this item.
        The meaning of each file is implementation-defined.
        """

    @property
    def FreeCADMax(self) -> str:
        """
        String representing the maximum version of FreeCAD needed for this item.
        If unset it will be 0.0.0.
        """

    @property
    def FreeCADMin(self) -> str:
        """
        String representing the minimum version of FreeCAD needed for this item.
        If unset it will be 0.0.0.
        """

    @property
    def Icon(self) -> str:
        """Relative path to an icon file."""

    @property
    def License(self) -> list[ReturnGetLicenseDict]:
        """List of applicable licenses as objects with 'name' and 'file' string attributes."""

    @property
    def Maintainer(self) -> list[ReturnGetMaintainerDict]:
        """List of maintainer objects with 'name' and 'email' string attributes."""

    @property
    def Name(self) -> str:
        """String representing the name of this item."""

    @property
    def PythonMin(self) -> str:
        """
        String representing the minimum version of Python needed for this item.
        If unset it will be 0.0.0.
        """

    @property
    def Replace(self) -> list:
        """
        List of things this item is considered by its author to replace. The format is
        identical to dependencies.
        """

    @property
    def Subdirectory(self) -> str:
        """
        String representing the name of the subdirectory this content item is located in.
        If empty, the item is in a directory named the same as the content item.
        """

    @property
    def Tag(self) -> list[str]:
        """List of strings."""

    @property
    def Urls(self) -> list[ReturnGetUrlsDict]:
        """
        List of URLs as objects with 'location' and 'type' string attributes, where type
        is one of:
        * website
        * repository
        * bugtracker
        * readme
        * documentation
        """

    @property
    def Version(self) -> str:
        """String representing the version of this item in semantic triplet format."""

    def addAuthor(self, name: str = None, email: str = None, /) -> None:
        """
        addAuthor(name, email)

        Add a new Author with name 'name', and optionally email 'email'. 
        Possible exceptions: (Exception).
        """

    @typing.overload
    def addConflict(self, name, kind, /): ...

    @typing.overload
    def addConflict(self, dictionary: dict = None, /) -> None:
        """
        addConflict(name, kind)

        Add a new Conflict. See documentation for addDepend(). 
        Possible exceptions: (Exception).
        """

    def addContentItem(self, contentType: str = None, contentItem: FreeCAD.Metadata = None, /) -> None:
        """
        addContentItem(content_type,metadata)

        Add a new content item of type 'content_type' with metadata 'metadata'.
        """

    @typing.overload
    def addDepend(self, name, kind, optional, /): ...

    @typing.overload
    def addDepend(self, dictionary: dict = None, /) -> None:
        """
        addDepend(name, kind, optional)

        Add a new Dependency on package 'name' of kind 'kind' (optional, one of 'auto' (the default),

        'internal', 'addon', or 'python'). 
        Possible exceptions: (Exception).
        """

    def addFile(self, file: str = None, /) -> None:
        """
        addFile(filename)

        Add a new File. 
        Possible exceptions: (Exception).
        """

    def addLicense(self, shortCode: str = None, path: str = None, /) -> None:
        """
        addLicense(short_code,path)

        Add a new License. 
        Possible exceptions: (Exception).
        """

    def addMaintainer(self, name: str = None, email: str = None, /) -> None:
        """
        addMaintainer(name, email)

        Add a new Maintainer. 
        Possible exceptions: (Exception).
        """

    def addReplace(self, dictionary: dict = None, /) -> None:
        """
        addReplace(name)

        Add a new Replace. 
        Possible exceptions: (Exception).
        """

    def addTag(self, tag: str = None, /) -> None:
        """
        addTag(tag)

        Add a new Tag. 
        Possible exceptions: (Exception).
        """

    def addUrl(self, urlTypeCharStar: str = None, link: str = None, branch: str = None, /) -> None:
        """
        addUrl(url_type,url,branch)

        Add a new Url or type 'url_type' (which should be one of 'repository', 'readme',

        'bugtracker', 'documentation', or 'webpage') If type is 'repository' you

        must also specify the 'branch' parameter. 
        Possible exceptions: (Exception).
        """

    def getFirstSupportedFreeCADVersion(self) -> str | None:
        """
        getFirstSupportedFreeCADVersion() -> str or None

        Search through all content package items, and determine if a minimum supported
        version of FreeCAD is set.
        Returns 0.0 if no minimum version is set, or if *any* content item fails to
        provide a minimum version (implying that that content item will work with all
        known versions. Technically limited to 0.20 as the lowest known version since
        the metadata standard was added then).
        """

    def getGenericMetadata(self, name: str, /) -> list[ReturnGetGenericMetadataDict]:
        """
        getGenericMetadata(name) -> list

        Get the list of GenericMetadata objects with key 'name'.
        Generic metadata objects are Python objects with a string 'contents' and a
        dictionary of strings, 'attributes'. They represent unrecognized simple XML tags
        in the metadata file.
        """

    def getLastSupportedFreeCADVersion(self) -> str | None:
        """
        getLastSupportedFreeCADVersion() -> str or None

        Search through all content package items, and determine if a maximum supported
        version of FreeCAD is set.
        Returns None if no maximum version is set, or if *any* content item fails to
        provide a maximum version (implying that that content item will work with all
        known versions).
        """

    def removeAuthor(self, name: str = None, email: str = None, /) -> None:
        """
        removeAuthor(name, email)

        Remove the Author. 
        Possible exceptions: (Exception).
        """

    @typing.overload
    def removeConflict(self, name, kind, /): ...

    @typing.overload
    def removeConflict(self, dictionary: dict = None, /) -> None:
        """
        removeConflict(name, kind)

        Remove the Conflict. See documentation for removeDepend().
        Possible exceptions: (Exception).
        """

    def removeContentItem(self, contentType: str = None, contentName: str = None, /) -> None:
        """
        removeContentItem(content_type,name)

        Remove the content item of type 'content_type' with name 'name'.
        """

    @typing.overload
    def removeDepend(self, name, kind, /): ...

    @typing.overload
    def removeDepend(self, dictionary: dict = None, /) -> None:
        """
        removeDepend(name, kind)

        Remove the Dependency on package 'name' of kind 'kind' (optional - if unspecified any

        matching name is removed). 
        Possible exceptions: (Exception).
        """

    def removeFile(self, file: str = None, /) -> None:
        """
        removeFile(filename)

        Remove the File. 
        Possible exceptions: (Exception).
        """

    def removeLicense(self, shortCode: str = None, path: str = None, /) -> None:
        """
        removeLicense(short_code)

        Remove the License. 
        Possible exceptions: (Exception).
        """

    def removeMaintainer(self, name: str = None, email: str = None, /) -> None:
        """
        removeMaintainer(name, email)

        Remove the Maintainer. 
        Possible exceptions: (Exception).
        """

    def removeReplace(self, dictionary: dict = None, /) -> None:
        """
        removeReplace(name)

        Remove the Replace. 
        Possible exceptions: (Exception).
        """

    def removeTag(self, tag: str = None, /) -> None:
        """
        removeTag(tag)

        Remove the Tag. 
        Possible exceptions: (Exception).
        """

    def removeUrl(self, urlTypeCharStar: str = None, link: str = None, branch: str = None, /) -> None:
        """
        removeUrl(url_type,url)

        Remove the Url. 
        Possible exceptions: (Exception).
        """

    def supportsCurrentFreeCAD(self) -> bool:
        """
        supportsCurrentFreeCAD() -> bool

        Returns False if this metadata object directly indicates that it does not
        support the current version of FreeCAD, or True if it makes no indication, or
        specifically indicates that it does support the current version. Does not
        recurse into Content items.
        """

    def write(self, filename: str = None, /) -> None:
        """
        write(filename)

        Write the metadata to the given file as XML data.
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

    def addExtension(self, typeId: str, proxy=None, /):
        """
        Adds an extension to the object. Requires the string identifier for the python extension as argument
        Possible exceptions: (TypeError, DeprecationWarning).
        """

    def hasExtension(self, type: str, deriv: bool = True, /) -> bool:
        """
        Returns if this object has the specified extension
        Possible exceptions: (TypeError).
        """


# DocumentPy.xml
class Document(FreeCAD.PropertyContainer):
    """
    This class can be imported.
    This is a Document class
    """

    @property
    def ActiveObject(self) -> FreeCAD.DocumentObject | None:
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
    def Objects(self) -> list[FreeCAD.DocumentObject]:
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
    def RedoNames(self) -> list[str]:
        """A List of Redo names"""

    @property
    def Restoring(self) -> bool:
        """Indicate if the document is restoring"""

    @property
    def RootObjects(self) -> list[FreeCAD.DocumentObject]:
        """The list of root object of this document"""

    @property
    def Temporary(self) -> bool:
        """Check if this is a temporary document"""

    @property
    def TopologicalSortedObjects(self) -> list[FreeCAD.DocumentObject]:
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
    def ShowHidden(self) -> bool:
        """
        Property TypeId: App::PropertyBool.
        Whether to show hidden object items in the tree view.
        """

    @ShowHidden.setter
    def ShowHidden(self, value: int | bool): ...

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

    def addObject(self, type: str, name: str = None, objProxy=None, viewProxy=None, attach: bool = False, viewType: str = None) -> FreeCAD.DocumentObject:
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
        Possible exceptions: (TypeError).
        """

    def clearDocument(self):
        """Clear the whole document"""

    def clearUndos(self):
        """Clear the undo stack of the document"""

    def commitTransaction(self):
        """Commit an Undo/Redo transaction"""

    def copyObject(self, obj, rec: bool = False, retAll: bool = False, /) -> typing.Any | tuple[typing.Any, ...]:
        """
        copyObject(object, with_dependencies=False, return_all=False)
        Copy an object or objects from another document to this document. 

        object: can either a single object or sequence of objects
        with_dependencies: if True, all internal dependent objects are copied too.
        return_all: if True, return all copied objects, or else return only the copied
                    object corresponding to the input objects.
          
        Possible exceptions: (TypeError).
        """

    def exportGraphviz(self, fn: str = None, /) -> str:
        """Export the dependencies of the objects as graph"""

    def findObjects(self, Type: str = 'App::DocumentObject', Name: str = None, Label: str = None) -> list[FreeCAD.DocumentObject]:
        """
        findObjects([Type=string], [Name=string], [Label=string]) -> list
        Return a list of objects that match the specified type, name or label.
        Name and label support regular expressions. All parameters are optional.
        Possible exceptions: (RuntimeError).
        """

    def getDependentDocuments(self, sort: bool = True, /) -> list:
        """
        getDependentDocuments(sort=True)

        Returns a list of documents that this document directly or indirectly links to including itself.

        sort: whether to topologically sort the return list
        """

    def getFileName(self) -> str:
        """
        For a regular document it returns its file name property.
        For a temporary document it returns its transient directory.
        """

    def getLinksTo(self, pyobj=None, options: int = 0, count: int = 0, /) -> tuple[typing.Any, ...]:
        """
        getLinksTo(obj, options=0, maxCount=0): return objects linked to 'obj'

        options: 1: recursive, 2: check link array. Options can combine.
        maxCount: to limit the number of links returned
        """

    @typing.overload
    def getObject(self, name: str = None, /) -> FreeCAD.DocumentObject: ...

    @typing.overload
    def getObject(self, id: int = -1, /) -> FreeCAD.DocumentObject:
        """
        Return the object with the given name
        Possible exceptions: (TypeError).
        """

    def getObjectsByLabel(self, sName: str, /) -> list[FreeCAD.DocumentObject]:
        """
        Return the objects with the given label name.
        NOTE: It's possible that several objects have the same label name.
        """

    def getProgramVersion(self) -> str:
        """Get the program version that a project file was created with"""

    def getTempFileName(self, value, /) -> str:
        """
        Returns a file name with path in the temp directory of the document.
        Possible exceptions: (TypeError).
        """

    def importLinks(self, obj=None, /) -> tuple[typing.Any, ...]:
        """
        importLinks(object|[object...])

        Import any externally linked object given a list of objects in
        this document.  Any link type properties of the input objects
        will be automatically reassigned to the imported object

        If no object is given as input, it import all externally linked
        object of this document.
          
        Possible exceptions: (TypeError).
        """

    def isClosable(self) -> bool:
        """Check if the document can be closed. The default value is True"""

    def isSaved(self) -> bool:
        """Checks if the document is saved"""

    def isTouched(self) -> bool:
        """Check if any object is in touched state"""

    def load(self, filename: str = None, /):
        """Load the document from the given path"""

    def mergeProject(self, filename: str, /):
        """Merges this document with another project file"""

    @typing.overload
    def moveObject(self, object, /, bool_with_dependencies=False): ...

    @typing.overload
    def moveObject(self, sName: str, /):
        """
        moveObject(object, bool with_dependencies = False)
        Transfers an object from another document to this document.
              
        object: can either a single object or sequence of objects
        with_dependencies: if True, all internal dependent objects are copied too.
        
        Possible exceptions: (ValueError).
        """

    def mustExecute(self) -> bool:
        """Check if any object must be recomputed"""

    def openTransaction(self, value=None, /):
        """
        openTransaction(name) - Open a new Undo/Redo transaction.

        This function no long creates a new transaction, but calls
        FreeCAD.setActiveTransaction(name) instead, which will auto creates a
        transaction with the given name when any change happed in any opened document.
        If more than one document is changed, all newly created transactions will have
        the same internal ID and will be undo/redo together.
          
        Possible exceptions: (TypeError).
        """

    def purgeTouched(self):
        """Purge the touched state of all objects"""

    def recompute(self, pyobjs=None, force: bool = False, checkCycle: bool = False, /) -> int:
        """
        recompute(objs=None): Recompute the document and returns the amount of recomputed features
        Possible exceptions: (TypeError).
        """

    def redo(self):
        """Redo a previously undone transaction"""

    def removeObject(self, sName: str, /):
        """
        Remove an object from the document
        Possible exceptions: (ValueError).
        """

    def restore(self):
        """Restore the document from disk"""

    def save(self):
        """
        Save the document to disk
        Possible exceptions: (ValueError).
        """

    def saveAs(self, fn: str, /):
        """Save the document under a new name to disk"""

    def saveCopy(self, fn: str, /):
        """Save a copy of the document under a new name to disk"""

    def setClosable(self, close: bool, /):
        """Set a flag that allows or forbids to close a document"""

    def supportedTypes(self) -> list[str]:
        """A list of supported types of objects"""

    def undo(self):
        """Undo one transaction"""


# PropertyContainerPy.xml
class PropertyContainer(FreeCAD.Persistence):
    """
    This class can be imported.
    App.PropertyContainer class.
    """

    @property
    def PropertiesList(self) -> list[str]:
        """A list of all property names."""

    def dumpPropertyContent(self, Property: str, Compression: int = 3):
        """
        dumpPropertyContent(Property, Compression=3) -> bytearray

        Dumps the content of the property, both the XML representation and the additional
        data files required, into a byte representation.

        Property : str
            Property Name.
        Compression : int
            Set the data compression level in the range [0, 9]. Set to 0 for no compression.
        Possible exceptions: (IOError).
        """

    def getDocumentationOfProperty(self, pstr: str, /) -> str:
        """
        getDocumentationOfProperty(name) -> str

        Returns the documentation string of the property of this class.

        name : str
            Property name.
        """

    def getEditorMode(self, name: str, /) -> list[str]:
        """
        getEditorMode(name) -> list

        Get the behaviour of the property in the property editor.
        It returns a list of strings with the current mode. If the list is empty there are no
        special restrictions.
        If the list contains 'ReadOnly' then the item appears in the property editor but is
        disabled.
        If the list contains 'Hidden' then the item even doesn't appear in the property editor.

        name : str
            Property name.
        """

    def getEnumerationsOfProperty(self, pstr: str, /) -> list[str]:
        """
        getEnumerationsOfProperty(name) -> list or  None

        Return all enumeration strings of the property of this class or None if not a
        PropertyEnumeration.

        name : str
            Property name.
        """

    def getGroupOfProperty(self, pstr: str, /) -> str:
        """
        getGroupOfProperty(name) -> str

        Returns the name of the group which the property belongs to in this class.
        The properties are sorted in different named groups for convenience.

        name : str
            Property name.
        """

    def getPropertyByName(self, pstr: str, checkOwner: int = 0, /) -> FreeCAD.Property | tuple[typing.Any, FreeCAD.Property]:
        """
        getPropertyByName(name, checkOwner=0) -> object or Tuple

        Returns the value of a named property. Note that the returned property may not
        always belong to this container (e.g. from a linked object).

        name : str
             Name of the property.
        checkOwner : int
            0: just return the property.
            1: raise exception if not found or the property does not belong to this container.
            2: return a tuple (owner, propertyValue).
        Possible exceptions: (ValueError).
        """

    def getPropertyStatus(self, name: str = '', /) -> list[str | int]:
        """
        getPropertyStatus(name='') -> list

        Get property status.

        name : str
            Property name. If empty, returns a list of supported text names of the status.
        """

    def getPropertyTouchList(self, pstr: str, /) -> tuple[int, ...]:
        """
        getPropertyTouchList(name) -> tuple

        Returns a list of index of touched values for list type properties.

        name : str
            Property name.
        """

    def getTypeIdOfProperty(self, pstr: str, /) -> str:
        """
        getTypeIdOfProperty(name) -> str

        Returns the C++ class name of a named property.

        name : str
            Property name.
        """

    def getTypeOfProperty(self, pstr: str, /) -> list[str]:
        """
        getTypeOfProperty(name) -> list

        Returns the type of a named property. This can be a list conformed by elements in
        (Hidden, NoRecompute, NoPersist, Output, ReadOnly, Transient).

        name : str
            Property name.
        """

    def restorePropertyContent(self, property: str, buffer, /):
        """
        restorePropertyContent(name, obj) -> None

        Restore the content of the object from a byte representation as stored by `dumpPropertyContent`.
        It could be restored from any Python object implementing the buffer protocol.

        name : str
            Property name.
        obj : buffer
            Object with buffer protocol support.
        Possible exceptions: (TypeError, IOError).
        """

    def setDocumentationOfProperty(self, pstr: str, doc: str, /):
        """
        setDocumentationOfProperty(name, docstring) -> None

        Set the documentation string of a dynamic property of this class.

        name : str
            Property name.
        docstring : str
            Documentation string.
        """

    @typing.overload
    def setEditorMode(self, name: str, type: int, /): ...

    @typing.overload
    def setEditorMode(self, name: str, iter, /):
        """
        setEditorMode(name, type) -> None

        Set the behaviour of the property in the property editor.

        name : str
            Property name.
        type : int, sequence of str
            Property type.
            0: default behaviour. 1: item is ready-only. 2: item is hidden. 3: item is hidden and read-only.
            If sequence, the available items are 'ReadOnly' and 'Hidden'.
        Possible exceptions: (TypeError).
        """

    def setGroupOfProperty(self, pstr: str, group: str, /):
        """
        setGroupOfProperty(name, group) -> None

        Set the name of the group of a dynamic property.

        name : str
            Property name.
        group : str
            Group name.
        """

    def setPropertyStatus(self, name: str, pyValue, /):
        """
        setPropertyStatus(name, val) -> None

        Set property status.

        name : str
            Property name.
        val : int, str, sequence of str or int
            Call getPropertyStatus() to get a list of supported text value.
            If the text start with '-' or the integer value is negative, then the status is cleared.
        Possible exceptions: (TypeError).
        """


# ComplexGeoDataPy.xml
class ComplexGeoData(FreeCAD.Persistence):
    """Father of all complex geometric data types"""

    @property
    def BoundBox(self) -> FreeCAD.BoundBox:
        """Get the BoundBox of the object"""

    @property
    def CenterOfGravity(self) -> FreeCAD.Vector:
        """Get the center of gravity"""

    @property
    def Placement(self) -> FreeCAD.Placement:
        """Get the current transformation of the object as placement"""

    @Placement.setter
    def Placement(self, value: FreeCAD.Placement): ...

    @property
    def Tag(self) -> int:
        """Geometry Tag"""

    def applyRotation(self, obj: FreeCAD.Rotation, /):
        """
        Apply an additional rotation to the placement
        Possible exceptions: (RuntimeError).
        """

    def applyTranslation(self, obj: FreeCAD.Vector, /):
        """
        Apply an additional translation to the placement
        Possible exceptions: (RuntimeError).
        """

    def countSubElements(self, type: str, /) -> int:
        """
        Return the number of elements of a type
        Possible exceptions: (RuntimeError).
        """

    def getElementTypes(self) -> list[str]:
        """Return a list of element types"""

    def getFaces(self, accuracy: float = 0.05, /) -> tuple[list[FreeCAD.Vector], list[tuple[int, int, int]]]:
        """
        Return a tuple of points and triangles with a given accuracy
        Possible exceptions: (RuntimeError).
        """

    def getFacesFromSubElement(self, type: str, index: int, /) -> tuple[list[FreeCAD.Vector], list[tuple[int, int, int]]]:
        """
        Return vertexes and faces from a sub-element
        Possible exceptions: (RuntimeError).
        """

    def getLines(self, accuracy: float = 0.05, /) -> tuple[list[FreeCAD.Vector], list[tuple[int, int]]]:
        """
        Return a tuple of points and lines with a given accuracy
        Possible exceptions: (RuntimeError).
        """

    def getLinesFromSubElement(self, type: str, index: int, /) -> tuple[list[FreeCAD.Vector], list[tuple[int, int]]]:
        """
        Return vertexes and lines from a sub-element
        Possible exceptions: (RuntimeError).
        """

    def getPoints(self, accuracy: float = 0.05, /) -> tuple[list[FreeCAD.Vector], list[FreeCAD.Vector]]:
        """
        Return a tuple of points and normals with a given accuracy
        Possible exceptions: (RuntimeError).
        """

    def transformGeometry(self, obj: FreeCAD.Matrix, /):
        """
        Apply a transformation to the underlying geometry
        Possible exceptions: (RuntimeError).
        """


# Application.cpp
class FreeCADError(RuntimeError):
    pass


class FreeCADAbort(BaseException):
    pass


class XMLBaseException(Exception):
    pass


class XMLParseException(FreeCAD.XMLBaseException):
    pass


class XMLAttributeError(FreeCAD.XMLBaseException):
    pass


class UnknownProgramOption(BaseException):
    pass


class BadFormatError(FreeCAD.FreeCADError):
    pass


class BadGraphError(FreeCAD.FreeCADError):
    pass


class ExpressionError(FreeCAD.FreeCADError):
    pass


class ParserError(FreeCAD.FreeCADError):
    pass


class CADKernelError(FreeCAD.FreeCADError):
    pass


# ApplicationPy.cpp
def ParamGet(pstr: str = None, /):
    """Get parameters by path"""


def saveParameter(pstr: str = 'User parameter', /) -> None:
    """
    saveParameter(config='User parameter') -> None
    Save parameter set to file. The default set is 'User parameter'
    Possible exceptions: (ValueError, RuntimeError).
    """


def Version() -> list[str]:
    """Print the version to the output."""


def ConfigGet(pstr: str, /) -> str:
    """ConfigGet(string) -- Get the value for the given key."""


def ConfigSet(pstr: str, pstr2: str, /) -> None:
    """ConfigSet(string, string) -- Set the given key to the given value."""


def ConfigDump() -> dict[str, str]:
    """Dump the configuration to the output."""


def addImportType(psKey: str, psMod: str, /):
    """Register filetype for import"""


def changeImportModule(key: str, oldMod: str, newMod: str, /):
    """Change the import module name of a registered filetype"""


def getImportType(psKey: str = None, /) -> list[str] | dict[typing.Any, str | list[str] | None]:
    """Get the name of the module that can import the filetype"""


def addExportType(psKey: str, psMod: str, /):
    """Register filetype for export"""


def changeExportModule(key: str, oldMod: str, newMod: str, /):
    """Change the export module name of a registered filetype"""


def getExportType(psKey: str = None, /) -> list[str] | dict[typing.Any, str | list[str] | None]:
    """Get the name of the module that can export the filetype"""


def getResourceDir() -> str:
    """Get the root directory of all resources"""


def getLibraryDir() -> str:
    """Get the directory of all extension modules"""


def getTempPath() -> str:
    """Get the root directory of cached files"""


def getUserCachePath() -> str:
    """Get the root path of cached files"""


def getUserConfigDir() -> str:
    """Get the root path of user config files"""


def getUserAppDataDir() -> str:
    """Get the root directory of application data"""


def getUserMacroDir(actual: bool = False, /) -> str:
    """
    getUserMacroDir(bool=False) -> stringGet the directory of the user's macro directory
    If parameter is False (the default) it returns the standard path in theuser's home directory, otherwise it returns the user-defined path.
    """


def getHelpDir() -> str:
    """Get the directory of the documentation"""


def getHomePath() -> str:
    """Get the home path, i.e. the parent directory of the executable"""


def loadFile(path: str, doc: str = '', mod: str = '', /):
    """
    loadFile(string=filename,[string=module]) -> None

    Loads an arbitrary file by delegating to the given Python module:
    * If no module is given it will be determined by the file extension.
    * If more than one module can load a file the first one will be taken.
    * If no module exists to load the file an exception will be raised.
    """


def open(name: str, hidden: bool = False) -> FreeCAD.Document:
    """
    See openDocument(string)
    Possible exceptions: (IOError).
    """


def openDocument(name: str, hidden: bool = False) -> FreeCAD.Document:
    """
    openDocument(filepath,hidden=False) -> object
    Create a document and load the project file into the document.

    filepath: file path to an existing file. If the file doesn't exist
              or the file cannot be loaded an I/O exception is thrown.
              In this case the document is kept alive.
    hidden: whether to hide document 3D view.
    Possible exceptions: (IOError).
    """


def newDocument(name: str = None, label: str = None, hidden: bool = False, temp: bool = False) -> FreeCAD.Document:
    """
    newDocument(name, label=None, hidden=False, temp=False) -> object
    Create a new document with a given name.

    name: unique document name which is checked automatically.
    label: optional user changeable label for the document.
    hidden: whether to hide document 3D view.
    temp: mark the document as temporary so that it will not be saved
    """


def closeDocument(pstr: str = None, /):
    """
    closeDocument(string) -> None

    Close the document with a given name.
    """


def activeDocument() -> FreeCAD.Document:
    """
    activeDocument() -> object or None

    Return the active document or None if there is no one.
    """


def setActiveDocument(pstr: str = None, /):
    """
    setActiveDocement(string) -> None

    Set the active document by its name.
    """


def getDocument(pstr: str = None, /) -> FreeCADGui.Document:
    """
    getDocument(string) -> object

    Get a document by its name or raise an exception
    if there is no document with the given name.
    """


def listDocuments(sort: bool = False, /) -> dict[str, FreeCAD.PyObjectBase]:
    """
    listDocuments(sort=False) -> list

    Return a list of names of all documents, optionally sort in dependency order.
    """


@typing.overload
def addDocumentObserver(): ...


@typing.overload
def addDocumentObserver(o, /):
    """
    addDocumentObserver() -> None

    Add an observer to get notified about changes on documents.
    """


@typing.overload
def removeDocumentObserver(): ...


@typing.overload
def removeDocumentObserver(o, /):
    """
    removeDocumentObserver() -> None

    Remove an added document observer.
    """


def setLogLevel(tag: str, pcObj, /) -> None:
    """
    setLogLevel(tag, level) -- Set the log level for a string tag.
    'level' can either be string 'Log', 'Msg', 'Wrn', 'Error', or an integer value
    """


def getLogLevel(tag: str, /) -> int:
    """getLogLevel(tag) -- Get the log level of a string tag"""


def checkLinkDepth(depth: int = 0, /) -> int:
    """checkLinkDepth(depth) -- check link recursion depth"""


def getLinksTo(pyobj=None, options: int = 0, count: int = 0, /) -> tuple[typing.Any, ...]:
    """
    getLinksTo(obj,options=0,maxCount=0) -- return the objects linked to 'obj'

    options: 1: recursive, 2: check link array. Options can combine.
    maxCount: to limit the number of links returned
    """


@typing.overload
def getDependentObjects(obj_obj, /, *args, options=0): ...


@typing.overload
def getDependentObjects(obj, options: int = 0, /) -> tuple[typing.Any, ...]:
    """
    getDependentObjects(obj|[obj,...], options=0)
    Return a list of dependent objects including the given objects.

    options: can have the following bit flags,
             1: to sort the list in topological order.
             2: to exclude dependency of Link type object.
    Possible exceptions: (TypeError).
    """


def setActiveTransaction(name: str, persist: bool = False, /) -> int:
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


def getActiveTransaction() -> tuple[str, int]:
    """getActiveTransaction() -> (name,id) return the current active transaction name and ID"""


def closeActiveTransaction(abort: bool = False, id: int = 0, /):
    """closeActiveTransaction(abort=False) -- commit or abort current active transaction"""


def isRestoring() -> bool:
    """isRestoring() -> Bool -- Test if the application is opening some document"""


def checkAbort():
    """
    checkAbort() -- check for user abort in length operation.

    This only works if there is an active sequencer (or ProgressIndicator in Python).
    There is an active sequencer during document restore and recomputation. User may
    abort the operation by pressing the ESC key. Once detected, this function will
    trigger a Base.FreeCADAbort exception.
    """



App = FreeCAD
Log = FreeCAD.Console.PrintLog
Msg = FreeCAD.Console.PrintMessage
Err = FreeCAD.Console.PrintError
Wrn = FreeCAD.Console.PrintWarning
# be careful with following variables -
# some of them are set in FreeCADGui (GuiUp after InitApplications),
# so may not exist until FreeCADGuiInit is initialized - use `getattr`
GuiUp: typing.Literal[0, 1]
Gui = FreeCADGui
ActiveDocument: FreeCAD.Document | None
