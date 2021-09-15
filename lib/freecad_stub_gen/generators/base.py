from pathlib import Path
from xml.etree.ElementTree import ParseError

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.module_container import Module
from freecad_stub_gen.util import readContent


class BaseGenerator:
    @classmethod
    def safeCreate(cls, *args, **kwargs):
        try:
            return cls(*args, **kwargs)
        except(FileNotFoundError, ParseError):
            return None

    def __init__(self, filePath: Path, sourceDir: Path = SOURCE_DIR):
        self.sourceDir = sourceDir
        self.baseGenFilePath = filePath
        self.requiredImports = set()
        self.currentNode = None  # TODO refactor P2 delete

        impPath = filePath.with_stem(filePath.stem + 'Imp').with_suffix('.cpp')
        if not impPath.exists():  # special case for PyObjectBase
            impPath = filePath.with_suffix('.cpp')

        self.impContent = readContent(impPath)

    def getStub(self, mod: Module, moduleName: str):
        """An argument `moduleName` may be optionally used
        if the generator cannot determine correct package."""
        raise NotImplementedError
