import sys
from pathlib import Path

from freecad_stub_gen.config import TARGET_DIR


class StubContainer:
    def __init__(self, stubContent: str = '', requiredImports: set = (), name: str = ''):
        self.content = stubContent
        self.requiredImports = set(requiredImports)
        self.name = name

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

        return StubContainer(
            content,
            self.requiredImports.union(other.requiredImports),
            self.name or other.name)

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'{self.genImports()}{self.content}'

    def genImports(self):
        sysImports, libImports = [], []
        try:  # required python 3.10
            stdlib_module_names = sys.stdlib_module_names
        except AttributeError:
            stdlib_module_names = ()

        for imp in self.requiredImports:
            importList = sysImports if imp in stdlib_module_names else libImports
            importList.append(f'import {imp}')

        res = '\n'.join(sorted(sysImports))
        if res:
            res += '\n\n'
        res += '\n'.join(sorted(libImports))
        if res:
            res += '\n\n\n'
        return res

    def save(self, targetPath: Path = TARGET_DIR):
        if not self.content:
            return

        self.content = self.content.rstrip() + '\n'

        with open((targetPath / self.name).with_suffix('.pyi'), 'w')as file:
            file.write(str(self))
