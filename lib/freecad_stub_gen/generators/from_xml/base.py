from abc import ABC
from pathlib import Path
from xml.etree.ElementTree import Element

from freecad_stub_gen.generators.common.gen_base import BaseGenerator


class BaseXmlGenerator(BaseGenerator, ABC):
    def __init__(self, filePath: Path, sourceDir: Path):
        super().__init__(filePath, sourceDir)
        self.currentNode: Element | None = None
