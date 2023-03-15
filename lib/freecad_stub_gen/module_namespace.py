import logging
from collections import defaultdict
from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.util import genXmlFiles

logger = logging.getLogger(__name__)


class _ModuleNamespace:
    def __init__(self, sourcePath: Path = SOURCE_DIR):
        self.sourcePath = sourcePath
        self.stemToPaths: defaultdict[str, list[Path]] = defaultdict(list)
        for file in genXmlFiles(sourcePath):
            self.stemToPaths[file.stem].append(file)

    def getFileForStem(self, stem: str, namespace: str = '') -> Path:
        match self.stemToPaths[stem]:
            case []:
                raise ValueError(f"There is no path for {stem=}")
            case [onlyOnePath]:
                return onlyOnePath
            case manyPaths if any(namespace in str(pathWithNamespace := p) for p in manyPaths):
                # noinspection PyUnboundLocalVariable
                return pathWithNamespace
            case [anyPath, *_] as possiblePaths:
                paths = [p.relative_to(self.sourcePath) for p in possiblePaths]
                logger.warning(f'There is more than one possible {paths=}')
                return anyPath
            case _:
                raise NotImplementedError

    NAMESPACE_TO_MODULE = {
        'Base': 'FreeCAD',
        'App': 'FreeCAD',
        'Gui': 'FreeCADGui',
        'Data': 'FreeCAD',
        'Attacher': 'Part',
    }

    # Some modules have class with the same name therefore we must use alias.
    MODULE_TO_ALIAS = {
        'Mesh': 'MeshModule',
        'Path': 'PathModule',
        'Points': 'PointsModule',
        'Part': 'PartModule',
    }

    def getModFromAlias(self, alias: str, default=None):
        for k, v in self.MODULE_TO_ALIAS.items():
            if v == alias:
                return k
        return default

    def convertNamespaceToModule(self, namespace: str) -> str:
        mod = self.NAMESPACE_TO_MODULE.get(namespace, namespace)
        aliasedMod = self.MODULE_TO_ALIAS.get(mod, mod)
        return aliasedMod


__all__ = ['moduleNamespace']
moduleNamespace = _ModuleNamespace()
