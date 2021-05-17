import re
import textwrap
from pathlib import Path
from typing import Optional
from xml.etree.ElementTree import ParseError

from freecad_stub_gen.config import INDENT_SIZE, SOURCE_DIR
import xml.etree.ElementTree as ET

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
        except(FileNotFoundError, ParseError):
            return None

    def __init__(self, xmlPath: Path, sourceDir: Path = SOURCE_DIR):
        self.sourceDir = sourceDir
        self.xmlPath = xmlPath
        self.requiredImports = set()
        self.currentNode: Optional[ET.Element] = None

        impPath = xmlPath.with_stem(xmlPath.stem + 'Imp').with_suffix('.cpp')
        if not impPath.exists():  # special case for PyObjectBase
            impPath = xmlPath.with_suffix('.cpp')

        self.impContent = commentRemover(impPath.read_text())

    @staticmethod
    def indent(block, distance=1, indentSize=INDENT_SIZE):
        return textwrap.indent(block, ' ' * distance * indentSize)

    @classmethod
    def _genDoc(cls, node: ET.Element) -> Optional[str]:
        if docs := node.find("./Documentation//UserDocu").text:
            return f'"""{docs}"""\n'

    @classmethod
    def _genName(cls, name: str, module: str = None):
        name = name.removesuffix('Py')
        name = name.removesuffix('Topo')
        if module:
            name = module + '.' + name
        return name

    def genImports(self):
        return '\n'.join(f'import {imp}' for imp in sorted(self.requiredImports)) + '\n\n'

    @property
    def parentXml(self):
        assert self.currentNode is not None

        fatherInclude = self.currentNode.attrib['FatherInclude'].replace('/', '.')
        parentFile = (self.sourceDir / fatherInclude).with_suffix('.xml')
        return parentFile
