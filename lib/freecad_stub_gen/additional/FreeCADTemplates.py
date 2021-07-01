"""
This module has templates for some python object used in FreeCAD.

The ideal solution would use optional protocol,
but at the moment there is such feature in Python
https://www.python.org/dev/peps/pep-0544/#support-optional-protocol-members

Find regex:
^\s*FC_PY_ELEMENT\((\w+)\)[^\S\n]*\\?
Replace:
    def $1(self):\n        \"\"\"May be implemented in python\"\"\""""
import typing

import FreeCAD
import FreeCADGui


# FeaturePython.cpp
class FeaturePythonGeneral:
    def onBeforeChangeLabel(self, obj: FreeCAD.DocumentObject, newLabel: str) -> str:
        """May be implemented in python"""

    def getViewProviderName(self, obj: FreeCAD.DocumentObject) -> str:
        """May be implemented in python"""

    def getSubObject(self, obj: FreeCAD.DocumentObject, subName: str,
                     num: typing.Literal[1, 2], matrix: FreeCAD.Matrix,
                     transform: bool, depth: int
                     ) -> typing.Union[
        None,
        tuple[
            typing.Optional[FreeCAD.DocumentObject],
            FreeCAD.Matrix,
        ],
        tuple[
            typing.Optional[FreeCAD.DocumentObject],
            FreeCAD.Matrix,
            typing.Any,
        ],
    ]:
        """May be implemented in python"""

    def getSubObjects(self, obj: FreeCAD.DocumentObject, reason: int
                      ) -> typing.Optional[typing.Sequence[str]]:
        """May be implemented in python"""

    def getLinkedObject(self, obj: FreeCAD.DocumentObject, recurse: bool,
                        matrix: FreeCAD.Matrix, transform: bool, depth: int
                        ) -> typing.Union[
        None,
        tuple[
            typing.Optional[FreeCAD.DocumentObject],
            FreeCAD.Matrix,
        ],
    ]:
        """May be implemented in python"""

    def canLinkProperties(self, obj: FreeCAD.DocumentObject) -> bool:
        """May be implemented in python"""

    def allowDuplicateLabel(self, obj: FreeCAD.DocumentObject) -> bool:
        """May be implemented in python"""

    def redirectSubName(self, obj: FreeCAD.DocumentObject, ss: str,
                        topParent: typing.Union[FreeCAD.DocumentObject, object],
                        child: typing.Union[FreeCAD.DocumentObject, object]
                        ) -> typing.Optional[str]:
        """May be implemented in python"""

    def canLoadPartial(self, obj: FreeCAD.DocumentObject) -> int:
        """May be implemented in python"""

    def hasChildElement(self, obj: FreeCAD.DocumentObject) -> bool:
        """May be implemented in python"""

    def isElementVisible(self, obj: FreeCAD.DocumentObject, element: str) -> int:
        """May be implemented in python"""

    def setElementVisible(self, obj: FreeCAD.DocumentObject, element: str,
                          visible: bool) -> int:
        """May be implemented in python"""


class FeaturePython(FeaturePythonGeneral):
    def execute(self):
        """May be implemented in python"""

    def mustExecute(self) -> bool:
        """May be implemented in python"""

    def onBeforeChange(self, propertyName: str):
        """May be implemented in python"""

    def onChanged(self, propertyName: str):
        """May be implemented in python"""

    def onDocumentRestored(self):
        """May be implemented in python"""


class ProxyPython(FeaturePython):
    def attach(self, obj: FreeCAD.DocumentObject):
        """May be implemented in python"""

    def __getstate__(self):
        """May be implemented in python"""

    def __setstate__(self, value):
        """May be implemented in python"""


class FeaturePythonObj(FeaturePythonGeneral):
    def execute(self, obj: FreeCAD.DocumentObject):
        """May be implemented in python"""

    def mustExecute(self, obj: FreeCAD.DocumentObject) -> bool:
        """May be implemented in python"""

    def onBeforeChange(self, obj: FreeCAD.DocumentObject, propertyName: str):
        """May be implemented in python"""

    def onChanged(self, obj: FreeCAD.DocumentObject, propertyName: str):
        """May be implemented in python"""

    def onDocumentRestored(self, obj: FreeCAD.DocumentObject):
        """May be implemented in python"""


class ProxyPythonObj(FeaturePythonObj):
    """This is the same as ProxyPython, but has __object__ attribute.
    All method will be called without additional argument."""
    __object__: FreeCAD.DocumentObject = None

    def attach(self, obj: FreeCAD.DocumentObject):
        """May be implemented in python"""

    def __getstate__(self):
        """May be implemented in python"""

    def __setstate__(self, value):
        """May be implemented in python"""


class ViewProxyPython:
    __vobject__: FreeCADGui.ViewProviderDocumentObject = None


# Gui/Command.cpp
class ResourceDict(typing.TypedDict, total=False):
    CmdType: str
    Pixmap: str
    WhatsThis: str
    MenuText: str
    ToolTip: str
    StatusTip: str
    Accel: str


class CommandPython:
    def GetResources(self) -> ResourceDict:
        """May be implemented in python"""

    def IsActive(self) -> bool:
        """May be implemented in python"""

    def Activated(self):
        """May be implemented in python"""


class CheckAbleDict(ResourceDict):
    Checkable: bool


class CheckAbleCommandPython(CommandPython):
    def GetResources(self) -> CheckAbleDict:
        """May be implemented in python"""

    def Activated(self, checked: bool = None):
        """May be implemented in python"""


# Gui/DocumentObserverPython.cpp
class DocumentObserverGui:
    """This is template class. You should copy it to your code."""

    def CreatedDocument(self, doc: FreeCADGui.Document):
        """May be implemented in python"""

    def DeletedDocument(self, doc: FreeCADGui.Document):
        """May be implemented in python"""

    def RelabelDocument(self, doc: FreeCADGui.Document):
        """May be implemented in python"""

    def RenameDocument(self, doc: FreeCADGui.Document):
        """May be implemented in python"""

    def ActivateDocument(self, doc: FreeCADGui.Document):
        """May be implemented in python"""

    def CreatedObject(self,
                      viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """May be implemented in python"""

    def DeletedObject(self,
                      viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """May be implemented in python"""

    def BeforeChangeObject(self,
                           viewProvider: FreeCADGui.ViewProviderDocumentObject,
                           propContainerName: str):
        """May be implemented in python"""

    def ChangedObject(self, viewProvider: FreeCADGui.ViewProviderDocumentObject,
                      propContainerName: str):
        """May be implemented in python"""

    def InEdit(self, viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """May be implemented in python"""

    def ResetEdit(self, viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """May be implemented in python"""


# App/DocumentObserverPython.cpp
class DocumentObserverApp:
    """This is template class. You should copy it to your code."""

    def CreatedDocument(self, doc: FreeCAD.Document):
        """May be implemented in python"""

    def DeletedDocument(self, doc: FreeCAD.Document):
        """May be implemented in python"""

    def RelabelDocument(self, doc: FreeCAD.Document):
        """May be implemented in python"""

    def ActivateDocument(self, doc: FreeCAD.Document):
        """May be implemented in python"""

    def UndoDocument(self, doc: FreeCAD.Document):
        """May be implemented in python"""

    def RedoDocument(self, doc: FreeCAD.Document):
        """May be implemented in python"""

    def BeforeChangeDocument(self, doc: FreeCAD.Document, propContainerName: str):
        """May be implemented in python"""

    def ChangedDocument(self, obj: FreeCAD.DocumentObject, propContainerName: str):
        """May be implemented in python"""

    def CreatedObject(self, obj: FreeCAD.DocumentObject):
        """May be implemented in python"""

    def DeletedObject(self, obj: FreeCAD.DocumentObject):
        """May be implemented in python"""

    def BeforeChangeObject(self, obj: FreeCAD.DocumentObject,
                           propContainerName: str):
        """May be implemented in python"""

    def ChangedObject(self, obj: FreeCAD.DocumentObject, propContainerName: str):
        """May be implemented in python"""

    def RecomputedObject(self, obj: FreeCAD.DocumentObject):
        """May be implemented in python"""

    def BeforeRecomputeDocument(self, doc: FreeCAD.Document):
        """May be implemented in python"""

    def RecomputedDocument(self, doc: FreeCAD.Document):
        """May be implemented in python"""

    def OpenTransaction(self, doc: FreeCAD.Document, name: str):
        """May be implemented in python"""

    def CommitTransaction(self, doc: FreeCAD.Document):
        """May be implemented in python"""

    def AbortTransaction(self, doc: FreeCAD.Document):
        """May be implemented in python"""

    def Undo(self):
        """May be implemented in python"""

    def Redo(self):
        """May be implemented in python"""

    def BeforeCloseTransaction(self, abort: bool):
        """May be implemented in python"""

    def CloseTransaction(self, abort: bool):
        """May be implemented in python"""

    def StartSaveDocument(self, doc: FreeCAD.Document, fileName: str):
        """May be implemented in python"""

    def FinishSaveDocument(self, doc: FreeCAD.Document, fileName: str):
        """May be implemented in python"""

    def AppendDynamicProperty(self, propContainer: FreeCAD.PropertyContainer,
                              propContainerName: str):
        """May be implemented in python"""

    def RemoveDynamicProperty(self, propContainer: FreeCAD.PropertyContainer,
                              propContainerName: str):
        """May be implemented in python"""

    def ChangePropertyEditor(self, propContainer: FreeCAD.PropertyContainer,
                             propContainerName: str):
        """May be implemented in python"""

    def BeforeAddingDynamicExtension(self,
                                     extension: FreeCAD.ExtensionContainer,
                                     extensionName: str):
        """May be implemented in python"""

    def AddedDynamicExtension(self,
                              extension: FreeCAD.ExtensionContainer,
                              extensionName: str):
        """May be implemented in python"""
