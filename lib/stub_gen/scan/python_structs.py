import enum
from collections.abc import Iterable
from dataclasses import dataclass
from functools import cached_property
from typing import ClassVar

from clang import cindex as cc

from stub_gen.scan.filter_gen import Gen, getCallArgs
from stub_gen.scan.walk import (
    getAssignment,
    getEnum,
    getList,
    getString,
    stripCast,
)
from stub_gen.scan.wrapper import CursorWrapper


class FunctionFlags(enum.IntFlag):
    # https://github.com/python/cpython/blob/2228e92da31ca7344a163498f848973a1b356597/Include/methodobject.h#L85
    METH_VARARGS = 0x1
    METH_KEYWORDS = 0x2
    METH_NOARGS = 0x4
    METH_O = 0x8
    METH_CLASS = 0x10
    METH_STATIC = 0x20
    METH_COEXIST = 0x40
    METH_FASTCALL = 0x80
    METH_STACKLESS = 0x100
    METH_METHOD = 0x200


@dataclass(frozen=True)
class PyMethodDef:
    """Structure for functions in module.

    C-API documentation:
    https://docs.python.org/3/c-api/structures.html#c.PyMethodDef

    struct PyMethodDef {
        const char  *ml_name;   /* The name of the built-in function/method */
        PyCFunction ml_meth;    /* The C function that implements it */
        int         ml_flags;   /* Combination of METH_xxx flags, which mostly
                                   describe the args expected by the C func */
        const char  *ml_doc;    /* The __doc__ attribute, or NULL */
    };
    """

    name: CursorWrapper
    meth: CursorWrapper
    flags: CursorWrapper
    doc: CursorWrapper

    @cached_property
    def functionName(self) -> str:
        return getString(self.name)

    @cached_property
    def functionDoc(self) -> str:
        return getString(self.doc)

    @cached_property
    def functionImpl(self) -> CursorWrapper:
        return stripCast(self.meth)

    @cached_property
    def functionFlags(self) -> FunctionFlags:
        return getEnum(self.flags, FunctionFlags)


@dataclass(frozen=True)
class PyModuleDef:
    """Module structure.

    C-API documentation:
    https://docs.python.org/3/c-api/module.html#c.PyModuleDef

    struct PyModuleDef {
      PyModuleDef_Base m_base;
      const char* m_name;
      const char* m_doc;
      Py_ssize_t m_size;
      PyMethodDef *m_methods;
      PyModuleDef_Slot *m_slots;
      traverseproc m_traverse;
      inquiry m_clear;
      freefunc m_free;
    };
    """

    base: CursorWrapper
    name: CursorWrapper
    doc: CursorWrapper
    size: CursorWrapper
    methods: CursorWrapper
    slots: CursorWrapper
    traverse: CursorWrapper
    clear: CursorWrapper
    free: CursorWrapper

    @cached_property
    def moduleName(self) -> str:
        return getString(self.name)

    @cached_property
    def moduleDocs(self) -> str:
        """Return docstring for module.

        Macro definition:
        https://github.com/python/cpython/blob/aef52ca8b334ff90e8032da39f4d06e7b5130eb9/Include/pymacro.h#L109
        """
        return getString(self.doc)

    METHOD_ENTRY_LEN: ClassVar[int] = 4
    MODULE_ENTRY_LEN: ClassVar[int] = 9

    @cached_property
    def moduleFunctions(self) -> list[PyMethodDef]:
        functions: list[PyMethodDef] = []

        if self.methods.cursor.type == cc.CursorKind.CXX_NULL_PTR_LITERAL_EXPR:
            return functions

        methodWrappers = getList(self.methods)
        for mw in methodWrappers:
            entries = getList(mw)
            assert (
                len(entries) == self.METHOD_ENTRY_LEN
            ), "Expected 4 elements in method"

            fun = PyMethodDef(*entries)
            functions.append(fun)

        lastElem = functions.pop()
        assert lastElem.name.cursor.kind == cc.CursorKind.CXX_NULL_PTR_LITERAL_EXPR
        return functions


def getPyModuleDef(cursorWrapper: CursorWrapper) -> PyModuleDef:
    sa = getAssignment(cursorWrapper).getChildren()
    assert len(sa) == PyModuleDef.MODULE_ENTRY_LEN, "Expected 9 elements in PyModuleDef"
    return PyModuleDef(*sa)


def genCreatedPyModules(tu: cc.TranslationUnit) -> Iterable[PyModuleDef]:
    for m in Gen.genChildren(tu).genConstructors().genDefinedInTU(tu=tu):
        for cw in Gen.walkPreorder(m).genCall().genWithSpelling('PyModule_Create2'):
            moduleCreateArgs = getCallArgs(cw, expectedArgNum=2)
            moduleRef = moduleCreateArgs[0]

            pyMod = getPyModuleDef(moduleRef)
            yield pyMod
