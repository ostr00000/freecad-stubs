import logging
import re
from typing import Iterable

from freecad_stub_gen.generators.from_cpp.base import FreecadStubGeneratorFromCpp
from freecad_stub_gen.generators.method.function_finder import findFunctionCall

logger = logging.getLogger(__name__)


class FreecadStubGeneratorFromCppClass(FreecadStubGeneratorFromCpp):
    """Generate class from cpp code with methods."""
    REG_INIT_TYPE = re.compile(r'::init_type\([^{;]*{')
    REG_CLASS_NAME = re.compile(r'behaviors\(\)\.name\(\s*"([\w.]+)"\s*\);')
    REG_CLASS_DOC = re.compile(r'behaviors\(\).doc\("((?:[^"\\]*(?:\\.)?(?:"\s*")?)+)"\);')

    def _genStub(self) -> Iterable[str]:
        for match in self.REG_INIT_TYPE.finditer(self.impContent):
            funcCall = findFunctionCall(self.impContent, match.start())

            classMatch = self.REG_CLASS_NAME.search(funcCall)
            if classMatch:
                className = classMatch.group(1).replace('.', '_')
            else:
                logger.debug(f'Cannot find function name in {self.baseGenFilePath}')
                continue  # it is a template

            gen = self._findFunctionCallsGen(funcCall)
            result = ''.join(self._genAllMethods(gen, firstArgName='self'))
            if not result:
                continue
            content = self.indent(result)

            if docsMatch := self.REG_CLASS_DOC.search(funcCall):
                docs = self.indent(self._getDocFromStr(docsMatch.group(1)) + '\n')
            else:
                docs = ''

            yield f"class {className}:\n{docs}{content}\n"
