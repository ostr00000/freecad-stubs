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
