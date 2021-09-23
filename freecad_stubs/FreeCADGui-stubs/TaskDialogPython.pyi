# TaskDialogPython.cpp
class Control:
    """Control for task dialogs"""

    def showDialog(self, dialog: object, /):
        """
        show the given dialog in the task panel
        showDialog(dialog)
        --
        if a task is already active a RuntimeError is raised
        """

    def activeDialog(self):
        """
        check if a dialog is active in the task panel
        activeDialog() --> bool
        """

    def closeDialog(self):
        """
        close the active dialog
        closeDialog()
        """

    def addTaskWatcher(self, TaskWatcher_list: object, /):
        """
        install a (list of) TaskWatcher
        addTaskWatcher(TaskWatcher | list)
        """

    def clearTaskWatcher(self):
        """
        remove all TaskWatchers
        clearTaskWatcher()
        """

    def isAllowedAlterDocument(self):
        """
        return the permission to alter the current Document
        isAllowedAlterDocument() --> bool
        """

    def isAllowedAlterView(self):
        """
        return the permission to alter the current View
        isAllowedAlterView() --> bool
        """

    def isAllowedAlterSelection(self):
        """
        return the permission to alter the current Selection
        isAllowedAlterSelection() --> bool
        """

    def showTaskView(self):
        """
        show the Task panel
        showTaskView()
        """

    def showModelView(self):
        """
        show the Model panel
        showModelView()
        """
