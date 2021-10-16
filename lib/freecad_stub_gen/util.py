import re
import textwrap
from pathlib import Path

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
        content = file.read_text()
    except UnicodeDecodeError:
        content = file.read_text('iso8859-1')

    return removeComments(content)


def genPyCppFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).glob('**/*.cpp')


def genXmlFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).glob('**/*.xml')
