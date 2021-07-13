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
class _FeaturePythonGeneral:
    def onBeforeChangeLabel(self, obj: FreeCAD.DocumentObject, newLabel: str) -> str:
        """FreeCAD call this function if present"""

    def getViewProviderName(self, obj: FreeCAD.DocumentObject) -> str:
        """FreeCAD call this function if present"""

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
        """FreeCAD call this function if present"""

    def getSubObjects(self, obj: FreeCAD.DocumentObject, reason: int
                      ) -> typing.Optional[typing.Sequence[str]]:
        """FreeCAD call this function if present"""

    def getLinkedObject(self, obj: FreeCAD.DocumentObject, recurse: bool,
                        matrix: FreeCAD.Matrix, transform: bool, depth: int
                        ) -> typing.Union[
        None,
        tuple[
            typing.Optional[FreeCAD.DocumentObject],
            FreeCAD.Matrix,
        ],
    ]:
        """FreeCAD call this function if present"""

    def canLinkProperties(self, obj: FreeCAD.DocumentObject) -> bool:
        """FreeCAD call this function if present"""

    def allowDuplicateLabel(self, obj: FreeCAD.DocumentObject) -> bool:
        """FreeCAD call this function if present"""

    def redirectSubName(self, obj: FreeCAD.DocumentObject, ss: str,
                        topParent: typing.Union[FreeCAD.DocumentObject, object],
                        child: typing.Union[FreeCAD.DocumentObject, object]
                        ) -> typing.Optional[str]:
        """FreeCAD call this function if present"""

    def canLoadPartial(self, obj: FreeCAD.DocumentObject) -> int:
        """FreeCAD call this function if present"""

    def hasChildElement(self, obj: FreeCAD.DocumentObject) -> bool:
        """FreeCAD call this function if present"""

    def isElementVisible(self, obj: FreeCAD.DocumentObject, element: str) -> int:
        """FreeCAD call this function if present"""

    def setElementVisible(self, obj: FreeCAD.DocumentObject, element: str,
                          visible: bool) -> int:
        """FreeCAD call this function if present"""


class _FeaturePython(_FeaturePythonGeneral):
    def execute(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""

    def mustExecute(self, obj: FreeCAD.DocumentObject) -> bool:
        """FreeCAD call this function if present"""

    def onBeforeChange(self, obj: FreeCAD.DocumentObject, propertyName: str):
        """FreeCAD call this function if present"""

    def onChanged(self, obj: FreeCAD.DocumentObject, propertyName: str):
        """FreeCAD call this function if present"""

    def onDocumentRestored(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""


class ProxyPython(_FeaturePython):
    def attach(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""

    def __getstate__(self):
        """FreeCAD call this function if present"""

    def __setstate__(self, value):
        """FreeCAD call this function if present"""


class _FeaturePythonObj(_FeaturePythonGeneral):
    def execute(self):
        """FreeCAD call this function if present"""

    def mustExecute(self) -> bool:
        """FreeCAD call this function if present"""

    def onBeforeChange(self, propertyName: str):
        """FreeCAD call this function if present"""

    def onChanged(self, propertyName: str):
        """FreeCAD call this function if present"""

    def onDocumentRestored(self):
        """FreeCAD call this function if present"""


class ProxyPythonObj(_FeaturePythonObj):
    """This is the same as ProxyPython, but has __object__ attribute.
    All method will be called without additional argument."""
    __object__: FreeCAD.DocumentObject = None

    def attach(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""

    def __getstate__(self):
        """FreeCAD call this function if present"""

    def __setstate__(self, value):
        """FreeCAD call this function if present"""


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
        """FreeCAD call this function if present"""

    def IsActive(self) -> bool:
        """FreeCAD call this function if present"""

    def Activated(self):
        """FreeCAD call this function if present"""


class CheckAbleDict(ResourceDict):
    Checkable: bool


class CheckAbleCommandPython(CommandPython):
    def GetResources(self) -> CheckAbleDict:
        """FreeCAD call this function if present"""

    def Activated(self, checked: bool = None):
        """FreeCAD call this function if present"""


# Gui/DocumentObserverPython.cpp
class DocumentObserverGui:
    """This is template class. You should copy it to your code."""

    def slotCreatedDocument(self, doc: FreeCADGui.Document):
        """FreeCAD call this function if present"""

    def slotDeletedDocument(self, doc: FreeCADGui.Document):
        """FreeCAD call this function if present"""

    def slotRelabelDocument(self, doc: FreeCADGui.Document):
        """FreeCAD call this function if present"""

    def slotRenameDocument(self, doc: FreeCADGui.Document):
        """FreeCAD call this function if present"""

    def slotActivateDocument(self, doc: FreeCADGui.Document):
        """FreeCAD call this function if present"""

    def slotCreatedObject(self, viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """FreeCAD call this function if present"""

    def slotDeletedObject(self, viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """FreeCAD call this function if present"""

    def slotBeforeChangeObject(self, viewProvider: FreeCADGui.ViewProviderDocumentObject,
                               propContainerName: str):
        """FreeCAD call this function if present"""

    def slotChangedObject(self, viewProvider: FreeCADGui.ViewProviderDocumentObject,
                          propContainerName: str):
        """FreeCAD call this function if present"""

    def slotInEdit(self, viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """FreeCAD call this function if present"""

    def slotResetEdit(self, viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """FreeCAD call this function if present"""


# App/DocumentObserverPython.cpp
class DocumentObserverApp:
    """This is template class. You should copy it to your code."""

    def slotCreatedDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotDeletedDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotRelabelDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotActivateDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotUndoDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotRedoDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotBeforeChangeDocument(self, doc: FreeCAD.Document, propContainerName: str):
        """FreeCAD call this function if present"""

    def slotChangedDocument(self, obj: FreeCAD.DocumentObject, propContainerName: str):
        """FreeCAD call this function if present"""

    def slotCreatedObject(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""

    def slotDeletedObject(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""

    def slotBeforeChangeObject(self, obj: FreeCAD.DocumentObject, propContainerName: str):
        """FreeCAD call this function if present"""

    def slotChangedObject(self, obj: FreeCAD.DocumentObject, propContainerName: str):
        """FreeCAD call this function if present"""

    def slotRecomputedObject(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""

    def slotBeforeRecomputeDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotRecomputedDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotOpenTransaction(self, doc: FreeCAD.Document, name: str):
        """FreeCAD call this function if present"""

    def slotCommitTransaction(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotAbortTransaction(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotUndo(self):
        """FreeCAD call this function if present"""

    def slotRedo(self):
        """FreeCAD call this function if present"""

    def slotBeforeCloseTransaction(self, abort: bool):
        """FreeCAD call this function if present"""

    def slotCloseTransaction(self, abort: bool):
        """FreeCAD call this function if present"""

    def slotStartSaveDocument(self, doc: FreeCAD.Document, fileName: str):
        """FreeCAD call this function if present"""

    def slotFinishSaveDocument(self, doc: FreeCAD.Document, fileName: str):
        """FreeCAD call this function if present"""

    def slotAppendDynamicProperty(self, propContainer: FreeCAD.PropertyContainer,
                                  propContainerName: str):
        """FreeCAD call this function if present"""

    def slotRemoveDynamicProperty(self, propContainer: FreeCAD.PropertyContainer,
                                  propContainerName: str):
        """FreeCAD call this function if present"""

    def slotChangePropertyEditor(self, propContainer: FreeCAD.PropertyContainer,
                                 propContainerName: str):
        """FreeCAD call this function if present"""

    def slotBeforeAddingDynamicExtension(self, extension: FreeCAD.ExtensionContainer,
                                         extensionName: str):
        """FreeCAD call this function if present"""

    def slotAddedDynamicExtension(self, extension: FreeCAD.ExtensionContainer,
                                  extensionName: str):
        """FreeCAD call this function if present"""
