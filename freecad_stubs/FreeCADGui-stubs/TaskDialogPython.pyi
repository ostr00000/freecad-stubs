import qtpy.QtWidgets


# TaskDialogPython.cpp
class Control:
    """Control for task dialogs"""

    def showDialog(self, dialog, /) -> None:
        """
        show the given dialog in the task panel
        showDialog(dialog)
        --
        if a task is already active a RuntimeError is raised
        Possible exceptions: (Exception, RuntimeError).
        """

    def activeDialog(self) -> bool:
        """
        check if a dialog is active in the task panel
        activeDialog() --> bool
        Possible exceptions: (Exception).
        """

    def activeTaskDialog(self):
        """
        return the active task dialog if there is one
        activeTaskDialog() --> TaskDialog or None
        Possible exceptions: (Exception).
        """

    def closeDialog(self) -> None:
        """
        close the active dialog
        closeDialog()
        Possible exceptions: (Exception).
        """

    def addTaskWatcher(self, TaskWatcher_list, /) -> None:
        """
        install a (list of) TaskWatcher
        addTaskWatcher(TaskWatcher | list)
        Possible exceptions: (Exception).
        """

    def clearTaskWatcher(self) -> None:
        """
        remove all TaskWatchers
        clearTaskWatcher()
        Possible exceptions: (Exception).
        """

    def isAllowedAlterDocument(self) -> bool:
        """
        return the permission to alter the current Document
        isAllowedAlterDocument() --> bool
        Possible exceptions: (Exception).
        """

    def isAllowedAlterView(self) -> bool:
        """
        return the permission to alter the current View
        isAllowedAlterView() --> bool
        Possible exceptions: (Exception).
        """

    def isAllowedAlterSelection(self) -> bool:
        """
        return the permission to alter the current Selection
        isAllowedAlterSelection() --> bool
        Possible exceptions: (Exception).
        """

    def showTaskView(self) -> None:
        """
        show the Task panel
        showTaskView()
        Possible exceptions: (Exception).
        """

    def showModelView(self) -> None:
        """
        show the Model panel
        showModelView()
        Possible exceptions: (Exception).
        """


class TaskDialog:
    """Task dialog"""

    def getDialogContent(self) -> list[qtpy.QtWidgets.QWidget]:
        """
        Returns the widgets of the task dialog -> list
        Possible exceptions: (Exception).
        """

    def getStandardButtons(self) -> int:
        """
        Get the standard buttons of the box -> flags
        Possible exceptions: (Exception).
        """

    def setEscapeButtonEnabled(self) -> None:
        """Defines whether the task dialog can be rejected by pressing Esc"""

    def isEscapeButtonEnabled(self) -> bool:
        """
        Checks if the task dialog can be rejected by pressing Esc -> bool
        Possible exceptions: (Exception).
        """

    def setAutoCloseOnTransactionChange(self) -> None:
        """
        Defines whether a task dialog must be closed if the document changes the
        active transaction
        """

    def isAutoCloseOnTransactionChange(self) -> bool:
        """
        Checks if the task dialog will be closed when the active transaction has changed -> bool
        Possible exceptions: (Exception).
        """

    def getDocumentName(self) -> str:
        """
        Get the name of the document the task dialog is attached to -> str
        Possible exceptions: (Exception).
        """

    def isAllowedAlterDocument(self) -> bool:
        """
        Indicates whether this task dialog allows other commands to modify
        the document while it is open -> bool
        Possible exceptions: (Exception).
        """

    def isAllowedAlterView(self) -> bool:
        """
        Indicates whether this task dialog allows other commands to modify
        the 3d view while it is open -> bool
        Possible exceptions: (Exception).
        """

    def isAllowedAlterSelection(self) -> bool:
        """
        Indicates whether this task dialog allows other commands to modify
        the selection while it is open -> bool
        Possible exceptions: (Exception).
        """

    def needsFullSpace(self) -> bool:
        """
        Indicates whether the task dialog fully requires the available space -> bool
        Possible exceptions: (Exception).
        """

    def accept(self) -> None:
        """
        Accept the task dialog
        Possible exceptions: (Exception).
        """

    def reject(self) -> None:
        """
        Reject the task dialog
        Possible exceptions: (Exception).
        """
