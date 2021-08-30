import re
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional
from xml.etree.ElementTree import ParseError

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.stub_container import StubContainer

_REG_COMMENT_REM = re.compile(
    r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
    re.DOTALL | re.MULTILINE)


def _replacer(match):
    s = match.group(0)
    if s.startswith('/'):
        return " "  # note: a space and not an empty string
    else:
        return s


def commentRemover(text):
    """Based on https://stackoverflow.com/a/241506"""
    return re.sub(_REG_COMMENT_REM, _replacer, text)


class BaseGenerator:
    @classmethod
    def safeCreate(cls, *args, **kwargs):
        try:
            return cls(*args, **kwargs)
        except(FileNotFoundError, UnicodeDecodeError, ParseError):
            return None

    def __init__(self, filePath: Path, sourceDir: Path = SOURCE_DIR):
        self.sourceDir = sourceDir
        self.baseGenFilePath = filePath
        self.requiredImports = set()
        self.currentNode: Optional[ET.Element] = None

        impPath = filePath.with_stem(filePath.stem + 'Imp').with_suffix('.cpp')
        if not impPath.exists():  # special case for PyObjectBase
            impPath = filePath.with_suffix('.cpp')

        self.impContent = commentRemover(impPath.read_text())

    @staticmethod
    def indent(block, distance=1, indentSize=4):
        return textwrap.indent(block, ' ' * distance * indentSize)

    REG_REMOVE_NEW_LINE = re.compile(r'\\n"\s*"')
    REG_WHITESPACE_WITH_APOSTROPHE = re.compile(r'"\s*"')

    @classmethod
    def _genDocFromStr(cls, docs: Optional[str]) -> Optional[str]:
        if docs is None:
            return None

        docs = cls.REG_REMOVE_NEW_LINE.sub('\n', docs)
        docs = cls.REG_WHITESPACE_WITH_APOSTROPHE.sub('', docs)
        docs = docs.replace('\\n', '\n').replace('\\"', '"')

        return f'"""{docs}"""\n'

    @classmethod
    def _getDocFromNode(cls, node: ET.Element) -> Optional[str]:
        if docs := node.find("./Documentation//UserDocu").text:
            return docs

    def getStub(self) -> Optional[StubContainer]:
        raise NotImplementedError
