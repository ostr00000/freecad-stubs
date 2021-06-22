# TaskDialogPython.cpp
class Control:
    """Control for task dialogs"""

    @staticmethod
    def showDialog(dialog: object, /):
        """show the given dialog in the task panel
        showDialog(dialog)
        --
        if a task is already active a RuntimeError is raised"""

    @staticmethod
    def activeDialog():
        """check if a dialog is active in the task panel
        activeDialog() --> bool"""

    @staticmethod
    def closeDialog():
        """close the active dialog
        closeDialog()"""

    @staticmethod
    def addTaskWatcher(TaskWatcher_list: object, /):
        """install a (list of) TaskWatcher
        addTaskWatcher(TaskWatcher | list)"""

    @staticmethod
    def clearTaskWatcher():
        """remove all TaskWatchers
        clearTaskWatcher()"""

    @staticmethod
    def isAllowedAlterDocument():
        """return the permission to alter the current Document
        isAllowedAlterDocument() --> bool"""

    @staticmethod
    def isAllowedAlterView():
        """return the permission to alter the current View
        isAllowedAlterView() --> bool"""

    @staticmethod
    def isAllowedAlterSelection():
        """return the permission to alter the current Selection
        isAllowedAlterSelection() --> bool"""

    @staticmethod
    def showTaskView():
        """show the Task panel
        showTaskView()"""

    @staticmethod
    def showModelView():
        """show the Model panel
        showModelView()"""
