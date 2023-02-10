import re
import textwrap
from collections.abc import Hashable
from pathlib import Path
from typing import Generic, Iterable, TypeVar

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


T = TypeVar('T', bound=Hashable)


class OrderedSet(Generic[T]):
    def __init__(self, it: Iterable[T] = ()):
        self._data: dict[T, None] = dict.fromkeys(it)

    def add(self, item: T):
        self._data[item] = None

    def pop(self, item: T):
        self._data.pop(item)

    def first(self):
        return next(iter(self))

    def update(self, it: Iterable[T]):
        self._data.update(dict.fromkeys(it))

    def clear(self):
        self._data.clear()

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        return '|'.join(map(str, self))


class OrderedStrSet(OrderedSet[str]):
    pass


def toBool(text: str | bool | None) -> bool:
    match str(text).lower():
        case 'y' | 'yes' | 't' | 'true' | 'on' | '1':
            return True
        case 'n' | 'no' | 'f' | 'false' | 'off' | '0' | 'none':
            return False
        case _:
            raise ValueError(f"Unknown bool value: {text}")
