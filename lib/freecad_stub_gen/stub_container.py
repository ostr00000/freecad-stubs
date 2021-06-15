import copy
import sys
from collections import defaultdict
from pathlib import Path

from freecad_stub_gen.config import TARGET_DIR


class StubContainer:
    def __init__(self, stubContent: str = '', requiredImports: set = (), name: str = '',
                 subContainers=None):
        self.content = stubContent
        self.requiredImports = set(requiredImports)
        self.name = name
        self.subContainers: dict[str, StubContainer] = \
            subContainers or defaultdict(StubContainer)

    def __add__(self, other):
        if not isinstance(other, (type(self), str)):
            return NotImplemented

        if isinstance(other, str):
            return StubContainer(
                self.content + other, self.requiredImports, self.name)

        if self.content and other.content:
            content = '\n'.join((self.content, other.content))
        else:
            content = self.content or other.content

        subContainers = copy.deepcopy(self.subContainers)
        for s in other.subContainers.values():
            subContainers[s.name] += s

        return StubContainer(
            content,
            self.requiredImports.union(other.requiredImports),
            self.name or other.name, subContainers)

    def __matmul__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        self.subContainers[other.name] += other
        return self

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'{self.genImports()}{self.content}'

    def genImports(self):
        sysImports, libImports, localImports = [], [], []
        try:  # required python 3.10
            stdlib_module_names = sys.stdlib_module_names
        except AttributeError:
            stdlib_module_names = ()

        for imp in self.requiredImports:
            if imp in stdlib_module_names:
                importList = sysImports
            elif 'import' not in imp:
                importList = libImports
            else:
                importList = localImports

            if 'import' not in imp:
                imp = f'import {imp}'
            importList.append(imp)

        sysImportText = '\n'.join(sorted(sysImports))
        libImportText = '\n'.join(sorted(libImports))
        locImportText = '\n'.join(sorted(localImports))
        res = '\n\n'.join(filter(None, (sysImportText, libImportText, locImportText)))
        if res:
            res += '\n\n\n'
        return res

    def save(self, targetPath: Path = TARGET_DIR):
        if not self.content:
            return

        self.content = self.content.rstrip() + '\n'

        savePath = targetPath / self.name
        if self.subContainers:
            savePath.mkdir(parents=True, exist_ok=True)
            for sc in self.subContainers.values():
                sc.save(savePath)
            savePath = savePath / '__init__'

        with open(savePath.with_suffix('.pyi'), 'w') as file:
            file.write(str(self))
