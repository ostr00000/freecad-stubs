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

    def getNamespaceForStem(self, name: str) -> str:
        possiblePaths = self.stemToPaths[name]
        assert len(possiblePaths) > 0
        if len(possiblePaths) > 1:
            paths = [p.relative_to(self.sourcePath) for p in possiblePaths]
            logger.warning(f'There is more than one possible {paths=}')

        path = possiblePaths[0]
        if 'Mod' in str(path):
            return path.parent.parent.name
        else:
            return path.parent.name

    def __contains__(self, item: str):
        return item in self.stemToPaths

    NAMESPACE_TO_MODULE = {
        'Base': 'FreeCAD',
        'App': 'FreeCAD',
        'Gui': 'FreeCAD.Gui',
        'Data': 'FreeCAD',
    }

    def convertNamespaceToModule(self, namespace: str):
        return self.NAMESPACE_TO_MODULE.get(namespace, namespace)


moduleNamespace = _ModuleNamespace()
