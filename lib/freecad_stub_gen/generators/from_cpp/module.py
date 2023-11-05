import re
from collections.abc import Iterable

from freecad_stub_gen.generators.common.cpp_function import findFunctionCall
from freecad_stub_gen.generators.from_cpp.base import BaseGeneratorFromCpp
from freecad_stub_gen.python_code.module_container import Module
from freecad_stub_gen.module_namespace import moduleNamespace
from freecad_stub_gen.ordered_set import OrderedStrSet


class FreecadStubGeneratorFromCppModule(BaseGeneratorFromCpp):
    """Generate functions from cpp code directly added to module."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._modName: str | None = None

    REG_MODULE_INIT = re.compile(r'Py::ExtensionModule<\w+>\("(\w+)"\)')

    def getStub(self, mod: Module, moduleName: str):
        header = f'# {self.baseGenFilePath.name}\n'

        for result in self._genStub(moduleName):
            if result.rstrip():
                # we prefer name with more details
                assert self._modName
                curModName = moduleName if '.' in moduleName else self._modName
                curModName = moduleNamespace.convertNamespaceToModule(curModName)

                mod[curModName].update(Module(
                    header + result, self.requiredImports))
                self.requiredImports = OrderedStrSet()

    def _genStub(self, moduleName: str) -> Iterable[str]:
        for match in self.REG_MODULE_INIT.finditer(self.impContent):
            moduleInitBody = findFunctionCall(self.impContent, match.end())

            gen = self._findFunctionCallsGen(moduleInitBody)
            if result := ''.join(self._genAllMethods(gen, functionSpacing=2)):
                self._modName = match.group(1)
                yield result
