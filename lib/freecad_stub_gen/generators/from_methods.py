import dataclasses
import logging
import re
from collections import defaultdict
from itertools import chain
from typing import Any, Iterable, DefaultDict, Optional

from more_itertools import islice_extended

from freecad_stub_gen.generators.method.arg_suit_merger import mergeArgSuitesGen
from freecad_stub_gen.generators.method.doc_string import generateArgSuitFromDocstring
from freecad_stub_gen.generators.method.format_finder import FormatFinder
from freecad_stub_gen.generators.method.function_finder import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.logger import LEVEL_CODE
from freecad_stub_gen.stub_container import StubContainer

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Method:
    args: list[str]
    pythonMethodName: str = ''
    cFunction: str = ''
    doc: str = None
    pythonArgs: str = None

    REG_WHITESPACE_WITH_APOSTROPHE = re.compile(r'"\s*"')

    def __post_init__(self):
        self.args = [
            e.strip().removesuffix('}').removesuffix('"').removeprefix('"')
            for e in self.args]

        self.pythonMethodName = self.args[0]
        self.cClass, self.cFunction = self._parsePointer(self.args[1])
        try:
            self.doc = re.sub(
                self.REG_WHITESPACE_WITH_APOSTROPHE, '', self.args[-1]
            ).replace('\\n', '\n')
        except IndexError:
            pass

    REG_POINTER = re.compile(r'(?:\w+::)*?(?:(?P<class>\w+)::)?\b(?P<func>\w+)\b\W*$')

    @classmethod
    def _parsePointer(cls, pointer: str) -> tuple[str, str]:
        match = cls.REG_POINTER.search(pointer)
        assert match
        return match.group('class') or '', match.group('func')

    def __repr__(self):
        return f'{self.cClass}::{self.cFunction}'

    def __str__(self):
        assert self.pythonArgs is not None
        return self.pythonArgs


@dataclasses.dataclass(repr=False)
class PyMethodDef(Method):
    flags: Any = None

    def __post_init__(self):
        super().__post_init__()
        self.flags = self.args[2]


class FreecadStubGeneratorFromMethods(FormatFinder):

    def getStub(self) -> Optional[StubContainer]:
        if result := ''.join(self._genAllMethods()).rstrip():
            header = f'# {self.baseGenFilePath.name}\n'
            return StubContainer(header + result + '\n\n', self.requiredImports)

    def _genAllMethods(self) -> Iterable[str]:
        methodNameToMethod: DefaultDict[str, list[Method]] = defaultdict(list)
        for method in chain(self._findArrayGen(), self._findFunctionCallsGen()):
            methodNameToMethod[method.pythonMethodName].append(method)

        for methods in methodNameToMethod.values():
            docContent = next((met.doc for met in methods), None)
            uniqueMethods = list({str(m): m for m in methods}.values())
            yield self.convertMethodToStr(
                methods[0].pythonMethodName, uniqueMethods,
                docContent, functionSpacing=2)

    REG_METHOD_DEF = re.compile(r'PyMethodDef(?!\s*\*)')

    def _findArrayGen(self) -> Iterable[Method]:
        """Based on https://docs.python.org/3/c-api/structures.html#c.PyMethodDef"""
        for match in self.REG_METHOD_DEF.finditer(self.impContent):
            start, end = match.span()
            arrayStr = findFunctionCall(self.impContent, start)
            arrayStrStartPos = arrayStr.find('{') + 1

            for arrayElemText in islice_extended(generateExpressionUntilChar(
                    arrayStr, arrayStrStartPos, ',', bracketL='{', bracketR='}'), -1):
                arrayElemStartPos = arrayElemText.find('{') + 1
                method = PyMethodDef(list(
                    generateExpressionUntilChar(arrayElemText, arrayElemStartPos, ',')))
                yield from self._genMethodWithArgs(method)

    def _genMethodWithArgs(self, method: Method) -> Iterable[Method]:
        docSuites = list(generateArgSuitFromDocstring(
            method.pythonMethodName, method.doc))
        codeSuites = list(self.generateArgFromCode(method.cFunction, method.cClass))

        yielded = False
        for argList in mergeArgSuitesGen(codeSuites, docSuites):
            yielded = True
            yield dataclasses.replace(method, pythonArgs=argList)

        if not yielded:
            logger.debug(f"Not found args for {method=!r} {self.baseGenFilePath=}")
            if logger.isEnabledFor(LEVEL_CODE):
                logger.log(LEVEL_CODE, self.findFunctionBody(
                    method.cFunction, method.cClass))

    REG_NOARGS_METHOD = re.compile('add_noargs_method')
    REG_VARGS_METHOD = re.compile('add_varargs_method')
    REG_KEYWORD_METHOD = re.compile('add_keyword_method')

    def _findFunctionCallsGen(self) -> Iterable[Method]:
        for match in chain(
                self.REG_NOARGS_METHOD.finditer(self.impContent),
                self.REG_VARGS_METHOD.finditer(self.impContent),
                self.REG_KEYWORD_METHOD.finditer(self.impContent),
        ):
            funcCall = findFunctionCall(
                self.impContent, match.span()[0], bracketL='(', bracketR=')')
            funcCallStartPos = funcCall.find('(') + 1
            method = Method(list(generateExpressionUntilChar(
                funcCall, funcCallStartPos, splitChar=',')))
            yield from self._genMethodWithArgs(method)
