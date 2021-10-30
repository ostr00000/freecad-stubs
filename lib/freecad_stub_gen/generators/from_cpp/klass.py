import logging
import re
from typing import Iterable

from freecad_stub_gen.generators.common.cpp_function import findFunctionCall
from freecad_stub_gen.generators.common.doc_string import formatDocstring
from freecad_stub_gen.generators.common.annotation_parameter import AnnotationParam
from freecad_stub_gen.generators.from_cpp.base import BaseGeneratorFromCpp
from freecad_stub_gen.importable_map import importableMap
from freecad_stub_gen.util import indent

logger = logging.getLogger(__name__)


class FreecadStubGeneratorFromCppClass(BaseGeneratorFromCpp):
    """Generate class from cpp code with methods."""
    REG_INIT_TYPE = re.compile(r'::init_type\([^{;]*{')
    REG_CLASS_NAME = re.compile(r'behaviors\(\)\.name\(\s*"([\w.]+)"\s*\);')
    REG_CLASS_DOC = re.compile(r'behaviors\(\).doc\("((?:[^"\\]*(?:\\.)?(?:"\s*")?)+)"\);')

    def _genStub(self, moduleName: str) -> Iterable[str]:
        for match in self.REG_INIT_TYPE.finditer(self.impContent):
            funcCall = findFunctionCall(self.impContent, match.start())

            classMatch = self.REG_CLASS_NAME.search(funcCall)
            if classMatch:
                className = classMatch.group(1).replace('.', '_')
            else:
                logger.debug(f'Cannot find function name in {self.baseGenFilePath}')
                continue  # it is a template

            gen = self._findFunctionCallsGen(funcCall)
            result = ''.join(self._genAllMethods(gen, firstParam=AnnotationParam.SELF_PARAM))
            if not result:
                result = 'pass'
            content = indent(result)

            doc = ''
            fullClassName = f'{moduleName}.{className}'
            if importableMap.isImportable(fullClassName):
                doc = "This class can be imported.\n"
            if docsMatch := self.REG_CLASS_DOC.search(funcCall):
                doc += docsMatch.group(1)
            if doc:
                doc = indent(formatDocstring(doc))

            yield f"class {className}:\n{doc}\n{content}\n"
