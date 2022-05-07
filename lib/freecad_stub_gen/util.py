import re
import textwrap
from collections.abc import Iterable
from pathlib import Path
from typing import TypeVar

from freecad_stub_gen.config import SOURCE_DIR


def indent(block, distance=1, indentSize=4):
    return textwrap.indent(block, ' ' * distance * indentSize)


_REG_COMMENT_REM = re.compile(
    r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
    re.DOTALL | re.MULTILINE)


def _replacer(match):
    s = match.group(0)
    if s.startswith('/'):
        return ' '  # note: a space and not an empty string
    else:
        return s


def removeComments(text):
    """Based on https://stackoverflow.com/a/241506"""
    return re.sub(_REG_COMMENT_REM, _replacer, text)


def readContent(file: Path):
    try:
        content = file.read_text('utf-8')
    except UnicodeDecodeError:
        content = file.read_text('iso8859-1')

    return removeComments(content)


def genCppFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).glob('**/*.cpp')


def genXmlFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).glob('**/*.xml')


T = TypeVar('T')


class OrderedSet(dict[T, None]):
    def __init__(self, it: Iterable[T] = ()):
        super().__init__(dict.fromkeys(it))

    def add(self, key: T):
        self[key] = None

    def update(self, keys: Iterable[T], **kwargs):
        for k in keys:
            self.add(k)

    def first(self):
        return next(iter(self.keys()))

    def __repr__(self):
        return '|'.join(self)
