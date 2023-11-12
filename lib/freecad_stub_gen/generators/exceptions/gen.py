import more_itertools

from freecad_stub_gen.generators.common.gen_python_api import PythonApiGenerator
from freecad_stub_gen.generators.exceptions.container import exceptionContainer
from freecad_stub_gen.python_code.module_container import Module


class ExceptionGenerator(PythonApiGenerator):
    def getStub(self, mod: Module, moduleName: str):
        hasException, it = more_itertools.spy(
            exceptionContainer.findExceptions(self.impContent)
        )
        if not hasException:
            return

        text = f'# {self.baseGenFilePath.name}\n'
        for e in it:
            text += f'{e}\n\n'
            self.requiredImports.update(e.requiredImports)
        mod[moduleName].update(Module(text, self.requiredImports))
