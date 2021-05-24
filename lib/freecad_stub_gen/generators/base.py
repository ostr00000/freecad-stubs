import re
import sys
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional
from xml.etree.ElementTree import ParseError

from freecad_stub_gen.config import INDENT_SIZE, SOURCE_DIR

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
    def indent(block, distance=1, indentSize=INDENT_SIZE):
        return textwrap.indent(block, ' ' * distance * indentSize)

    @classmethod
    def _genDocFromStr(cls, docs: Optional[str]) -> Optional[str]:
        if docs is None:
            return None
        return f'"""{docs}"""\n'

    @classmethod
    def _getDocFromNode(cls, node: ET.Element) -> Optional[str]:
        if docs := node.find("./Documentation//UserDocu").text:
            return docs

    def genImports(self):
        sysImports, libImports = [], []
        for imp in self.requiredImports:
            importList = sysImports if imp in sys.stdlib_module_names else libImports
            importList.append(f'import {imp}')

        res = '\n'.join(sorted(sysImports))
        if res:
            res += '\n\n'
        res += '\n'.join(sorted(libImports))
        if res:
            res += '\n\n\n'
        return res

    @property
    def parentXml(self) -> Optional[Path]:
        if self.currentNode is None:
            return

        fatherInclude = self.currentNode.attrib['FatherInclude'].replace('/', '.')
        parentFile = (self.sourceDir / fatherInclude).with_suffix('.xml')
        return parentFile
