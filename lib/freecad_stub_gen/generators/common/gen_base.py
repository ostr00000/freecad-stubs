from pathlib import Path
from xml.etree.ElementTree import ParseError

from freecad_stub_gen.file_functions import readContent
from freecad_stub_gen.ordered_set import OrderedStrSet
from freecad_stub_gen.python_code.module_container import Module


class BaseGenerator:
    @classmethod
    def safeCreate(cls, *args, **kwargs):
        try:
            return cls(*args, **kwargs)
        except (FileNotFoundError, ParseError):
            return None

    def __init__(self, filePath: Path, sourceDir: Path):
        self.sourceDir = sourceDir
        self.baseGenFilePath = filePath
        self.requiredImports = OrderedStrSet()

        impPath = filePath.with_stem(filePath.stem + 'Imp').with_suffix('.cpp')
        if not impPath.exists():  # special case for PyObjectBase
            impPath = filePath.with_suffix('.cpp')

        self.impContent = readContent(impPath)

    def getStub(self, mod: Module, moduleName: str):
        """Generate stub file for module `mod`.

        An argument `moduleName` may be optionally used if the generator
        cannot determine correct package.
        """
        raise NotImplementedError
