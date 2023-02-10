from abc import ABC
from pathlib import Path
from xml.etree.ElementTree import Element

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.generators.common.gen_base import BaseGenerator


class BaseXmlGenerator(BaseGenerator, ABC):
    def __init__(self, filePath: Path, sourceDir: Path = SOURCE_DIR):
        super().__init__(filePath, sourceDir)
        self._currentNode: Element | None = None

    @property
    def currentNode(self) -> Element:
        assert isinstance(self._currentNode, Element)
        return self._currentNode

    @currentNode.setter
    def currentNode(self, newNode: Element):
        self._currentNode = newNode
