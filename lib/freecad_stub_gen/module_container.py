from __future__ import annotations

import logging
import sys
from collections.abc import Iterable
from pathlib import Path

from freecad_stub_gen.config import TARGET_DIR
from freecad_stub_gen.module_namespace import moduleNamespace
from freecad_stub_gen.util import OrderedStrSet

logger = logging.getLogger(__name__)


class Module:
    EXT = '.pyi'

    def __init__(self, content='', imports: Iterable[str] = (), name: str = ''):
        self.name = name
        self.imports = OrderedStrSet(imports)
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

        mainPart = moduleNamespace.getModFromAlias(mainPart, mainPart)
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
        sysImports: list[str] = []
        libImports: list[str] = []
        localImports: list[str] = []
        types: list[str] = []

        for imp in self.imports:
            if imp.startswith('from '):
                sortModule = imp.removeprefix('from ').split(' ')[0]
            elif any(t in imp for t in ('TypeAlias', 'TypeVar', 'TypedDict')):
                if 'TypedDict' in imp and 'class' in imp:
                    imp = f'\n{imp}\n'
                types.append(imp)
                continue
            elif modName := moduleNamespace.getModFromAlias(imp):
                sortModule = modName
                imp = f'import {modName} as {imp}'
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
        typesText = '\n'.join(types)

        res = '\n\n'.join(filter(None, (sysImportText, libImportText, locImportText, typesText)))
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
