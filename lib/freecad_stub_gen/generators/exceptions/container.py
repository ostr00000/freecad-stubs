import re

from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar
from freecad_stub_gen.generators.common.names import getModuleName, getClassName, \
    getNamespaceWithClass
from freecad_stub_gen.module_namespace import moduleNamespace
from freecad_stub_gen.util import OrderedSet, indent, genCppFiles, readContent


class ExceptionData:
    def __init__(self, exceptionName: str, newExceptionArgs: list[str]):
        excModuleWithClass = newExceptionArgs[0].removeprefix('"').removesuffix('"')
        self.pyModuleRaw = getModuleName(excModuleWithClass)
        self.pyModule = moduleNamespace.convertNamespaceToModule(self.pyModuleRaw)
        self.pyClass = getClassName(excModuleWithClass)

        self.baseCppNamespace, self.baseCppClass = getNamespaceWithClass(newExceptionArgs[1])
        if self.baseCppNamespace is None:
            if self.baseCppClass.startswith('PyExc'):
                self.baseCppNamespace = '__python__'
            else:
                # no namespace means it is exception from current namespace
                self.baseCppNamespace = self.pyModuleRaw

        self.cppNamespace, self.cppClass = getNamespaceWithClass(exceptionName)
        if self.cppClass == 'OCCError':  # there is additional assignment
            self.cppClass = 'PartExceptionOCCError'
        if self.cppNamespace is None:
            # no namespace means it is exception from current namespace
            self.cppNamespace = self.pyModuleRaw

        self.requiredImports = OrderedSet()

    def __str__(self):
        if self.baseCppNamespace == '__python__':
            baseClass = self.baseCppClass.removeprefix('PyExc_')
        else:
            ed = exceptionContainer.getExceptionData(self.baseCppClass, self.baseCppNamespace)
            self.requiredImports.add(ed.pyModule)
            baseClass = f'{ed.pyModule}.{ed.pyClass}'

        return f'class {self.pyClass}({baseClass}):\n{indent("pass")}\n'

    def __repr__(self):
        return f'{self.pyModuleRaw}.{self.pyClass} [{self.cppNamespace}.{self.cppClass}]'


class ExceptionContainer:
    REG_NEW_EXCEPTION = re.compile(r"""
    (?P<name>
        (\w+)                   # variable name
        (\s*::\s*\w+)?          # may be with namespace
    )
    \s*=\s*
    PyErr_NewException\(
    (?P<funArg>[^)]*)       # function arguments
    \);
    """, re.VERBOSE)

    # OCCError = PyErr_NewException("Part.OCCError", Base::PyExc_FC_GeneralError, nullptr);

    def __init__(self):
        self.exceptions = list(self._genExceptions())

    def checkAllExceptionsCorrect(self):
        for e in self.exceptions:
            repr(e)

    def _genExceptions(self):
        for file in genCppFiles():
            content = readContent(file)
            yield from self.findExceptions(content)

    @classmethod
    def findExceptions(cls, content):
        seen = set()  # there are two exception for OCCError
        for match in cls.REG_NEW_EXCEPTION.finditer(content):
            name = match.group('name')
            if name in seen:
                continue
            seen.add(name)

            fc = match.group('funArg')
            funArgs = [e.strip() for e in generateExpressionUntilChar(
                fc, 0, ',', bracketL='(', bracketR=')')]

            ed = ExceptionData(name, funArgs)
            yield ed

    def getExceptionData(self, cppClass: str, cppNamespace: str):
        for e in self.exceptions:
            if e.cppClass == cppClass and e.cppNamespace == cppNamespace:
                return e

        raise ValueError(f"Cannot find exception: {cppClass=} {cppNamespace=}")

    def getExceptionText(self, cTypeExceptionText: str) -> str:
        cppNamespace, cppClass = getNamespaceWithClass(cTypeExceptionText)
        for e in self.exceptions:
            if e.cppClass == cppClass:
                pyModule = e.pyModuleRaw if e.pyModuleRaw != 'Base' else 'FreeCAD.Base'
                return f'{pyModule}.{e.pyClass}'

        if cTypeExceptionText.startswith('PyExc_'):
            return cTypeExceptionText.removeprefix('PyExc_')

        if 'getPyExceptionType()' in cTypeExceptionText:
            # The return type of this c++ function is PyObject.
            # An implementation return in this function various FreeCAD exceptions,
            # but we are unable to determine which one is used.
            return 'Exception'

        raise ValueError(f"Unknown exception {cTypeExceptionText=}")


exceptionContainer = ExceptionContainer()
exceptionContainer.checkAllExceptionsCorrect()
