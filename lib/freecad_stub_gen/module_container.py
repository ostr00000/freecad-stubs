from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Iterable

from freecad_stub_gen.config import TARGET_DIR

logger = logging.getLogger(__name__)


class Module:
    EXT = '.pyi'

    def __init__(self, content='', imports: Iterable[str] = (), name: str = ''):
        self.name = name
        self.imports = set(imports)
        self.content = content
        self.subModules = SourcesDict()

        self.parent: Module | None = None
        self.forcePackage = False

    def __str__(self):
        if self.parent and self.parent.name:
            return f'{self.parent}.{self.name}'
        return self.name

    def __getitem__(self, item: str):
        assert item
        mainPart, *otherParts = item.split('.', maxsplit=1)

        mod = self.subModules[mainPart]
        if mod.parent is None:
            mod.parent = self

        if otherParts:
            mod = mod[otherParts[0]]

        return mod

    def __setitem__(self, key: str, value: Module):
        mod = self[key]
        mod.update(value)

    def __add__(self, other):
        if isinstance(other, str):
            if not other.endswith('\n'):
                other += '\n'
            self.content += other
            return self

        return NotImplemented

    def update(self, sameModule: Module):
        self.imports.update(sameModule.imports)
        self.content += sameModule.content
        self.subModules.update(sameModule.subModules)

    def save(self, targetPath: Path = TARGET_DIR):
        savePath = targetPath / self.name

        if self.subModules:
            for sm in self.subModules.values():
                sm.save(savePath)

            if savePath.exists():
                (savePath / f'__init__{self.EXT}').touch()

        if not self.content:
            return

        if self.subModules or self.forcePackage:
            savePath = savePath / '__init__'

        savePath.parent.mkdir(parents=True, exist_ok=True)
        savePath.with_suffix(self.EXT).write_text(self.getContent())

    def getContent(self):
        return f'{self._genImports()}{self.content.rstrip()}\n'

    def _genImports(self):
        sysImports, libImports, localImports = [], [], []
        for imp in self.imports:
            if imp.startswith('from '):
                sortModule = imp.removeprefix('from ').split(' ')[0]
            else:
                sortModule = imp
                if 'import' not in imp:
                    imp = f'import {imp}'

            if sortModule in sys.stdlib_module_names:
                importList = sysImports
            else:
                importList = libImports

            importList.append(imp)

        sysImportText = '\n'.join(sorted(sysImports))
        libImportText = '\n'.join(sorted(libImports))
        locImportText = '\n'.join(sorted(localImports))
        res = '\n\n'.join(filter(None, (sysImportText, libImportText, locImportText)))
        if res:
            res += '\n\n\n'
        return res

    def setSubModulesAsPackage(self):
        for sm in self.subModules.values():
            sm.forcePackage = True


class SourcesDict(dict[str, Module]):
    def __missing__(self, key: str):
        val = self[key] = Module(name=key)
        return val
