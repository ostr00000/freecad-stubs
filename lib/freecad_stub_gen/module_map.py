import logging
from collections import defaultdict
from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR

logger = logging.getLogger(__name__)


def genXmlFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).glob('**/*.xml')


class _ModuleNamespace:
    def __init__(self):
        self.stemToPaths = defaultdict(list)
        for file in genXmlFiles():
            self.stemToPaths[file.stem].append(file)

    def getNamespaceForStem(self, name: str) -> str:
        paths = self.stemToPaths[name]
        assert len(paths) == 1
        return paths[0].parent.name

    def __contains__(self, item: str):
        return item in self.stemToPaths


moduleNamespace = _ModuleNamespace()
