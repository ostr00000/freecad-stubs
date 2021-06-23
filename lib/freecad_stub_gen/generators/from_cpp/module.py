import re
from collections.abc import Iterable
from typing import Optional

import more_itertools

from freecad_stub_gen.generators.from_cpp.base import FreecadStubGeneratorFromCpp
from freecad_stub_gen.generators.method.function_finder import findFunctionCall
from freecad_stub_gen.stub_container import StubContainer


class FreecadStubGeneratorFromCppModule(FreecadStubGeneratorFromCpp):
    """Generate functions from cpp code directly added to module."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._modName: Optional[str] = None

    REG_MODULE_INIT = re.compile(r'Py::ExtensionModule<\w+>\("(\w+)"\)')

    def getStub(self) -> Optional[StubContainer]:
        hasStub, gen = more_itertools.spy(self._genStub())
        if not hasStub:
            return

        mainStub = StubContainer()
        for st in gen:
            mainStub @= st
        return mainStub

    def _genStub(self) -> Iterable[StubContainer]:
        for result in self._genModules():
            if result := result.rstrip():
                header = f'# {self.baseGenFilePath.name}\n'
                assert self._modName
                yield StubContainer(
                    header + result + '\n\n',
                    self.requiredImports, name=self._modName)
                self.requiredImports = set()

    def _genModules(self) -> Iterable[str]:
        for match in self.REG_MODULE_INIT.finditer(self.impContent):
            start, end = match.span()
            moduleInitBody = findFunctionCall(self.impContent, end)

            gen = self._findFunctionCallsGen(moduleInitBody)
            if result := ''.join(self._genAllMethods(gen, isStatic=False, functionSpacing=2)):
                self._modName = match.group(1)
                yield result
