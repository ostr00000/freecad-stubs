# TaskDialogPython.cpp
class Control:
    """Control for task dialogs"""

    def showDialog(self, dialog, /) -> None:
        """
        show the given dialog in the task panel
        showDialog(dialog)
        --
        if a task is already active a RuntimeError is raised
        """

    def activeDialog(self) -> bool:
        """
        check if a dialog is active in the task panel
        activeDialog() --> bool
        """

    def closeDialog(self) -> None:
        """
        close the active dialog
        closeDialog()
        """

    def addTaskWatcher(self, TaskWatcher_list, /) -> None:
        """
        install a (list of) TaskWatcher
        addTaskWatcher(TaskWatcher | list)
        """

    def clearTaskWatcher(self) -> None:
        """
        remove all TaskWatchers
        clearTaskWatcher()
        """

    def isAllowedAlterDocument(self) -> bool:
        """
        return the permission to alter the current Document
        isAllowedAlterDocument() --> bool
        """

    def isAllowedAlterView(self) -> bool:
        """
        return the permission to alter the current View
        isAllowedAlterView() --> bool
        """

    def isAllowedAlterSelection(self) -> bool:
        """
        return the permission to alter the current Selection
        isAllowedAlterSelection() --> bool
        """

    def showTaskView(self) -> None:
        """
        show the Task panel
        showTaskView()
        """

    def showModelView(self) -> None:
        """
        show the Model panel
        showModelView()
        """
