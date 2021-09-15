import logging
from collections import defaultdict
from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR

logger = logging.getLogger(__name__)


def genPyCppFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).glob('**/*.cpp')


def genXmlFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).glob('**/*.xml')


class _ModuleNamespace:
    def __init__(self, sourcePath: Path = SOURCE_DIR):
        self.sourcePath = sourcePath
        self.stemToPaths = defaultdict(list)
        for file in genXmlFiles(sourcePath):
            self.stemToPaths[file.stem].append(file)

    def getFileForStem(self, stem: str, namespace: str = ''):
        match self.stemToPaths[stem]:
            case []:
                assert False, f"There is no path for {stem=}"
            case [onlyOnePath]:
                return onlyOnePath
            case manyPaths if any(namespace in str(pathWithNamespace := p) for p in manyPaths):
                return pathWithNamespace
            case [anyPath, *_] as possiblePaths:
                paths = [p.relative_to(self.sourcePath) for p in possiblePaths]
                logger.warning(f'There is more than one possible {paths=}')
                return anyPath

    NAMESPACE_TO_MODULE = {
        'Base': 'FreeCAD',
        'App': 'FreeCAD',
        'Gui': 'FreeCADGui',
        'Data': 'FreeCAD',
        'Attacher': 'Part',
    }

    def convertNamespaceToModule(self, namespace: str):
        return self.NAMESPACE_TO_MODULE.get(namespace, namespace)


moduleNamespace = _ModuleNamespace()
