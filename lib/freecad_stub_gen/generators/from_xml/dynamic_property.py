import logging
from abc import ABC
from pathlib import Path
from typing import Literal

from freecad_stub_gen.generators.common.gen_property.gen_dynamic import DynamicPropertyGenerator
from freecad_stub_gen.generators.from_xml.base import BaseXmlGenerator
from freecad_stub_gen.file_functions import readContent

logger = logging.getLogger(__name__)


class XmlDynamicPropertyGenerator(BaseXmlGenerator, DynamicPropertyGenerator, ABC):
    def getCppClassName(self):
        twinName = self.currentNode.attrib.get('Twin')
        assert twinName is not None, f"'Twin' not found in {self.baseGenFilePath}"
        return twinName

    def getCppContent(self):
        return self._getIncludeContent('.cpp')

    def getHContent(self):
        return self._getIncludeContent('.h')

    def _getIncludeContent(self, extension: Literal['.cpp', '.h']) -> str | None:
        inc = self.currentNode.get('Include')
        assert inc is not None, f"'Include' not found in {self.baseGenFilePath}"

        parts = self.baseGenFilePath.parts
        baseParts = parts[:parts.index('src') + 1] + (inc,)
        pathFromSrc = Path(*baseParts)
        pathFromLocal = self.baseGenFilePath.parent / inc

        for p in (pathFromSrc, pathFromLocal):
            for ext in (extension, Path(inc).suffix):
                try:
                    return readContent(p.with_suffix(ext))
                except FileNotFoundError:
                    pass

        if inc.endswith('.hxx'):
            return None  # probably these files are generated - just ignore them

        logger.warning(f"Could not find cpp file for {self.baseGenFilePath}")
        return None
