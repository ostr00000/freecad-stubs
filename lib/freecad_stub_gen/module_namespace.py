import logging
from collections import defaultdict
from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.util import genXmlFiles

logger = logging.getLogger(__name__)


class _ModuleNamespace:
    def __init__(self, sourcePath: Path = SOURCE_DIR):
        self.sourcePath = sourcePath
        self.stemToPaths = defaultdict(list)
        for file in genXmlFiles(sourcePath):
            self.stemToPaths[file.stem].append(file)

    def getFileForStem(self, stem: str, namespace: str = '') -> Path:
        match self.stemToPaths[stem]:
            case []:
                raise ValueError(f"There is no path for {stem=}")
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
        'Mesh': 'MeshModule',  # need to use alias, because there is also class 'Mesh'
    }

    def convertNamespaceToModule(self, namespace: str):
        return self.NAMESPACE_TO_MODULE.get(namespace, namespace)


__all__ = ['moduleNamespace']
moduleNamespace = _ModuleNamespace()
