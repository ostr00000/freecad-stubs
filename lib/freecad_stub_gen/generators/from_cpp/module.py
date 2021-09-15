import re
from collections.abc import Iterable
from typing import Optional

from freecad_stub_gen.generators.from_cpp.base import FreecadStubGeneratorFromCpp
from freecad_stub_gen.generators.method.function_finder import findFunctionCall
from freecad_stub_gen.module_container import Module


class FreecadStubGeneratorFromCppModule(FreecadStubGeneratorFromCpp):
    """Generate functions from cpp code directly added to module."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._modName: Optional[str] = None

    REG_MODULE_INIT = re.compile(r'Py::ExtensionModule<\w+>\("(\w+)"\)')

    def getStub(self, mod: Module, moduleName: str):
        header = f'# {self.baseGenFilePath.name}\n'

        for result in self._genStub():
            if result.rstrip():
                # we prefer name with more details
                curModName = moduleName if '.' in moduleName else self._modName
                assert self._modName

                mod[curModName].update(Module(
                    header + result, self.requiredImports))
                self.requiredImports = set()

    def _genStub(self) -> Iterable[str]:
        for match in self.REG_MODULE_INIT.finditer(self.impContent):
            moduleInitBody = findFunctionCall(self.impContent, match.end())

            gen = self._findFunctionCallsGen(moduleInitBody)
            if result := ''.join(self._genAllMethods(gen, functionSpacing=2)):
                self._modName = match.group(1)
                yield result
