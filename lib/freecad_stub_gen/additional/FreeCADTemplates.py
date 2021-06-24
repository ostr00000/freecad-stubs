"""
This module has templates for some python object used in FreeCAD.

The ideal solution would use optional protocol,
but at the moment there is such feature in Python
https://www.python.org/dev/peps/pep-0544/#support-optional-protocol-members
"""
import typing

import FreeCAD
import FreeCADGui


class ProxyPython:
    __object__: FreeCAD.DocumentObject = None

    def attach(self, obj: FreeCAD.DocumentObject):
        """Should be implemented in python"""

    def __getstate__(self):
        """Should be implemented in python"""

    def __setstate__(self, value):
        """Should be implemented in python"""


class ViewProxyPython:
    __vobject__: FreeCADGui.ViewProviderDocumentObject = None


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
        """Should be implemented in python"""

    def IsActive(self) -> bool:
        """Should be implemented in python"""

    def Activated(self):
        """Should be implemented in python"""


class CheckAbleDict(ResourceDict):
    Checkable: bool


class CheckAbleCommandPython(CommandPython):
    def GetResources(self) -> CheckAbleDict:
        """Should be implemented in python"""

    def Activated(self, checked: bool = None):
        """Should be implemented in python"""


class DocumentObserverGui:
    """This is template class. You should copy it to your code."""

    def CreatedDocument(self, doc: FreeCADGui.Document):
        """Should be implemented in python"""

    def DeletedDocument(self, doc: FreeCADGui.Document):
        """Should be implemented in python"""

    def RelabelDocument(self, doc: FreeCADGui.Document):
        """Should be implemented in python"""

    def RenameDocument(self, doc: FreeCADGui.Document):
        """Should be implemented in python"""

    def ActivateDocument(self, doc: FreeCADGui.Document):
        """Should be implemented in python"""

    def CreatedObject(self,
                      viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """Should be implemented in python"""

    def DeletedObject(self,
                      viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """Should be implemented in python"""

    def BeforeChangeObject(self,
                           viewProvider: FreeCADGui.ViewProviderDocumentObject,
                           propContainerName: str):
        """Should be implemented in python"""

    def ChangedObject(self, viewProvider: FreeCADGui.ViewProviderDocumentObject,
                      propContainerName: str):
        """Should be implemented in python"""

    def InEdit(self, viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """Should be implemented in python"""

    def ResetEdit(self, viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """Should be implemented in python"""


class DocumentObserverApp:
    """This is template class. You should copy it to your code."""

    def CreatedDocument(self, doc: FreeCAD.Document):
        """Should be implemented in python"""

    def DeletedDocument(self, doc: FreeCAD.Document):
        """Should be implemented in python"""

    def RelabelDocument(self, doc: FreeCAD.Document):
        """Should be implemented in python"""

    def ActivateDocument(self, doc: FreeCAD.Document):
        """Should be implemented in python"""

    def UndoDocument(self, doc: FreeCAD.Document):
        """Should be implemented in python"""

    def RedoDocument(self, doc: FreeCAD.Document):
        """Should be implemented in python"""

    def BeforeChangeDocument(self, doc: FreeCAD.Document, propContainerName: str):
        """Should be implemented in python"""

    def ChangedDocument(self, obj: FreeCAD.DocumentObject, propContainerName: str):
        """Should be implemented in python"""

    def CreatedObject(self, obj: FreeCAD.DocumentObject):
        """Should be implemented in python"""

    def DeletedObject(self, obj: FreeCAD.DocumentObject):
        """Should be implemented in python"""

    def BeforeChangeObject(self, obj: FreeCAD.DocumentObject,
                           propContainerName: str):
        """Should be implemented in python"""

    def ChangedObject(self, obj: FreeCAD.DocumentObject, propContainerName: str):
        """Should be implemented in python"""

    def RecomputedObject(self, obj: FreeCAD.DocumentObject):
        """Should be implemented in python"""

    def BeforeRecomputeDocument(self, doc: FreeCAD.Document):
        """Should be implemented in python"""

    def RecomputedDocument(self, doc: FreeCAD.Document):
        """Should be implemented in python"""

    def OpenTransaction(self, doc: FreeCAD.Document, name: str):
        """Should be implemented in python"""

    def CommitTransaction(self, doc: FreeCAD.Document):
        """Should be implemented in python"""

    def AbortTransaction(self, doc: FreeCAD.Document):
        """Should be implemented in python"""

    def Undo(self):
        """Should be implemented in python"""

    def Redo(self):
        """Should be implemented in python"""

    def BeforeCloseTransaction(self, abort: bool):
        """Should be implemented in python"""

    def CloseTransaction(self, abort: bool):
        """Should be implemented in python"""

    def StartSaveDocument(self, doc: FreeCAD.Document, fileName: str):
        """Should be implemented in python"""

    def FinishSaveDocument(self, doc: FreeCAD.Document, fileName: str):
        """Should be implemented in python"""

    def AppendDynamicProperty(self, propContainer: FreeCAD.PropertyContainer,
                              propContainerName: str):
        """Should be implemented in python"""

    def RemoveDynamicProperty(self, propContainer: FreeCAD.PropertyContainer,
                              propContainerName: str):
        """Should be implemented in python"""

    def ChangePropertyEditor(self, propContainer: FreeCAD.PropertyContainer,
                             propContainerName: str):
        """Should be implemented in python"""

    def BeforeAddingDynamicExtension(self,
                                     extension: FreeCAD.ExtensionContainer,
                                     extensionName: str):
        """Should be implemented in python"""

    def AddedDynamicExtension(self,
                              extension: FreeCAD.ExtensionContainer,
                              extensionName: str):
        """Should be implemented in python"""
