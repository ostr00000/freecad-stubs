import logging
import re
from itertools import chain
from typing import Iterable

from freecad_stub_gen.generators.from_cpp.base import FreecadStubGeneratorFromCpp, Method
from freecad_stub_gen.generators.method.function_finder import findFunctionCall, \
    generateExpressionUntilChar

logger = logging.getLogger(__name__)


# TODO P2 add DocumentObserverPython


class FreecadStubGeneratorFromCppClass(FreecadStubGeneratorFromCpp):
    REG_INIT_TYPE = re.compile(r'::init_type\([^{;]*{')
    REG_CLASS_NAME = re.compile(r'behaviors\(\)\.name\(\s*"([\w.]+)"\s*\);')
    REG_CLASS_NAME_ALT = re.compile(r'behaviors\(\)\.name\(\s*"([\w.]+)"\s*\);')
    REG_CLASS_DOC = re.compile(r'behaviors\(\).doc\("((?:[^"\\]*(?:\\.)?(?:"\s*")?)+)"\);')

    def _genStub(self):
        for match in self.REG_INIT_TYPE.finditer(self.impContent):
            funcCall = findFunctionCall(self.impContent, match.span()[0])

            gen = self._findFunctionCallsGen(funcCall)
            result = ''.join(self._genAllMethods(gen, isStatic=True))
            if not result:
                continue
            content = self.indent(result)

            classMatch = self.REG_CLASS_NAME.search(funcCall)
            if classMatch:
                className = classMatch.group(1).replace('.', '_')
            else:
                logger.debug(f'Cannot find function name in {self.baseGenFilePath}')
                continue  # it is a template

            if docsMatch := self.REG_CLASS_DOC.search(funcCall):
                docs = self.indent(self._genDocFromStr(docsMatch.group(1)) + '\n')
            else:
                docs = ''

            yield f"class {className}:\n{docs}{content}\n"

    REG_NOARGS_METHOD = re.compile('add_noargs_method')
    REG_VARGS_METHOD = re.compile('add_varargs_method')
    REG_KEYWORD_METHOD = re.compile('add_keyword_method')

    def _findFunctionCallsGen(self, content: str) -> Iterable[Method]:
        for match in chain(
                self.REG_NOARGS_METHOD.finditer(content),
                self.REG_VARGS_METHOD.finditer(content),
                self.REG_KEYWORD_METHOD.finditer(content),
        ):
            funcCall = findFunctionCall(
                content, match.span()[0], bracketL='(', bracketR=')')
            funcCallStartPos = funcCall.find('(') + 1
            method = Method(list(generateExpressionUntilChar(
                funcCall, funcCallStartPos, splitChar=',')))
            yield from self._genMethodWithArgs(method)
