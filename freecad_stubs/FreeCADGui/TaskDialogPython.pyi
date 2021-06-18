# TaskDialogPython.cpp
def showDialog(dialog: object, /):
    """show the given dialog in the task panel
    showDialog(dialog)
    --
    if a task is already active a RuntimeError is raised"""


def activeDialog():
    """check if a dialog is active in the task panel
    activeDialog() --> bool"""


def closeDialog():
    """close the active dialog
    closeDialog()"""


def addTaskWatcher(TaskWatcher_list: object, /):
    """install a (list of) TaskWatcher
    addTaskWatcher(TaskWatcher | list)"""


def clearTaskWatcher():
    """remove all TaskWatchers
    clearTaskWatcher()"""


def isAllowedAlterDocument():
    """return the permission to alter the current Document
    isAllowedAlterDocument() --> bool"""


def isAllowedAlterView():
    """return the permission to alter the current View
    isAllowedAlterView() --> bool"""


def isAllowedAlterSelection():
    """return the permission to alter the current Selection
    isAllowedAlterSelection() --> bool"""


def showTaskView():
    """show the Task panel
    showTaskView()"""


def showModelView():
    """show the Model panel
    showModelView()"""
