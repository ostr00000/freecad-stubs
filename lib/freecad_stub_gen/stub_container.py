import sys
from collections import defaultdict
from pathlib import Path

from freecad_stub_gen.config import TARGET_DIR


class StubContainer:
    def __init__(self, stubContent: str = '', requiredImports: set = (), name: str = '',
                 subContainers=None, siblingContainers=None):
        self.content = stubContent
        self.requiredImports: set[str] = set(requiredImports)
        self.name = name
        self.subContainers: dict[str, StubContainer] = \
            subContainers or defaultdict(StubContainer)
        self.siblingContainers: dict[str, StubContainer] = \
            siblingContainers or defaultdict(StubContainer)

    def __add__(self, other):
        """Adding stub containers merge both text."""
        if not isinstance(other, (type(self), str)):
            return NotImplemented

        if isinstance(other, str):
            self.content += other
            return self

        self.name = self.name or other.name
        self.requiredImports.update(other.requiredImports)

        if self.content and other.content:
            self.content = '\n'.join((self.content, other.content))
        else:
            self.content = self.content or other.content

        for name, cont in other.subContainers.items():
            self.subContainers[name] += cont

        for name, cont in other.siblingContainers.items():
            if name == self.name:  # this is not sibling but it is the same stub
                self.__add__(cont)
            else:
                self.siblingContainers[name] += cont

        return self

    def __matmul__(self, other):
        """Operator @ add stub container as sibling to this container."""
        if not isinstance(other, type(self)):
            return NotImplemented

        self.siblingContainers[other.name] += other
        return self

    def __truediv__(self, other):
        """Div operation add sub module with stubs."""
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
            if imp.startswith('from '):
                sortModule = imp.removeprefix('from ').split(' ')[0]
            else:
                sortModule = imp
                if 'import' not in imp:
                    imp = f'import {imp}'

            if sortModule in stdlib_module_names:
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

    def save(self, targetPath: Path = TARGET_DIR):
        for sc in self.siblingContainers.values():
            sc.save(targetPath)

        savePath = targetPath / self.name
        if self.subContainers:
            for sc in self.subContainers.values():
                sc.save(savePath)

            if savePath.exists():
                (savePath / '__init__.pyi').touch()

            savePath = savePath / '__init__'

        if not self.content:
            return

        self.content = self.content.rstrip() + '\n'
        savePath.parent.mkdir(parents=True, exist_ok=True)
        with open(savePath.with_suffix('.pyi'), 'w') as file:
            file.write(str(self))

    def moveSubContainersFrom(self, other: 'StubContainer'):
        for name, cont in other.subContainers.items():
            self.subContainers[name] += cont
        other.subContainers.clear()

    def makeSiblingContainersAsPackage(self):
        for sc in self.siblingContainers.values():
            sc /= StubContainer()
            sc.makeSiblingContainersAsPackage()
