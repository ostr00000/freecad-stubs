"""
using namespace Gui;
std::vector<SelectionObserverPython*> SelectionObserverPython::_instances;
SelectionObserverPython::SelectionObserverPython(const Py::Object& obj, ResolveMode resolve)
    : SelectionObserver(true, resolve), inst(obj)
{
    do { py_onSelectionChanged = Py::Object(); if (PyObject_HasAttrString(obj.ptr(), "onSelectionChanged")) { Py::Object _obj(PyObject_GetAttrString(obj.ptr(), "onSelectionChanged"), true); if (_obj.isCallable()) py_onSelectionChanged = _obj; } } while (0); do { py_addSelection = Py::Object(); if (PyObject_HasAttrString(obj.ptr(), "addSelection")) { Py::Object _obj(PyObject_GetAttrString(obj.ptr(), "addSelection"), true); if (_obj.isCallable()) py_addSelection = _obj; } } while (0); do { py_removeSelection = Py::Object(); if (PyObject_HasAttrString(obj.ptr(), "removeSelection")) { Py::Object _obj(PyObject_GetAttrString(obj.ptr(), "removeSelection"), true); if (_obj.isCallable()) py_removeSelection = _obj; } } while (0); do { py_setSelection = Py::Object(); if (PyObject_HasAttrString(obj.ptr(), "setSelection")) { Py::Object _obj(PyObject_GetAttrString(obj.ptr(), "setSelection"), true); if (_obj.isCallable()) py_setSelection = _obj; } } while (0); do { py_clearSelection = Py::Object(); if (PyObject_HasAttrString(obj.ptr(), "clearSelection")) { Py::Object _obj(PyObject_GetAttrString(obj.ptr(), "clearSelection"), true); if (_obj.isCallable()) py_clearSelection = _obj; } } while (0); do { py_setPreselection = Py::Object(); if (PyObject_HasAttrString(obj.ptr(), "setPreselection")) { Py::Object _obj(PyObject_GetAttrString(obj.ptr(), "setPreselection"), true); if (_obj.isCallable()) py_setPreselection = _obj; } } while (0); do { py_removePreselection = Py::Object(); if (PyObject_HasAttrString(obj.ptr(), "removePreselection")) { Py::Object _obj(PyObject_GetAttrString(obj.ptr(), "removePreselection"), true); if (_obj.isCallable()) py_removePreselection = _obj; } } while (0); do { py_pickedListChanged = Py::Object(); if (PyObject_HasAttrString(obj.ptr(), "pickedListChanged")) { Py::Object _obj(PyObject_GetAttrString(obj.ptr(), "pickedListChanged"), true); if (_obj.isCallable()) py_pickedListChanged = _obj; } } while (0);
}
SelectionObserverPython::~SelectionObserverPython() = default;
void SelectionObserverPython::addObserver(const Py::Object& obj, ResolveMode resolve)
{
    _instances.push_back(new SelectionObserverPython(obj, resolve));
}
void SelectionObserverPython::removeObserver(const Py::Object& obj)
{
    SelectionObserverPython* obs=nullptr;
    for (std::vector<SelectionObserverPython*>::iterator it =
        _instances.begin(); it != _instances.end(); ++it) {
        if ((*it)->inst == obj) {
            obs = *it;
            _instances.erase(it);
            break;
        }
    }
    delete obs;
}
"""
import pytest

from conftest import InputCode
from stub_gen.scan.filter_gen import genMethods
from stub_gen.scan.function import genFunctionReturnValues


@pytest.mark.parametrize(
    'inputCode',
    [
        InputCode(
            """
using namespace Gui;

class SelectionObserverPython{
    void removeObserver(const Py::Object& obj);
}
 
void SelectionObserverPython::removeObserver(const Py::Object& obj)
{
    SelectionObserverPython* obs=nullptr;
    for (std::vector<SelectionObserverPython*>::iterator it =
        _instances.begin(); it != _instances.end(); ++it) {
        if ((*it)->inst == obj) {
            obs = *it;
            _instances.erase(it);
            break;
        }
    }
    delete obs;
}
std::vector<SelectionObserverPython*> SelectionObserverPython::_instances;

""",
            returnCount=0,
        )
    ],
)
def test_simple(inputCode: InputCode):
    methods = list(genMethods(inputCode.trWrapper.getChildren()))
    assert len(methods) == 1
    for c in methods:
        returnValues = list(genFunctionReturnValues(c))
        assert len(returnValues) == inputCode.returnCount
