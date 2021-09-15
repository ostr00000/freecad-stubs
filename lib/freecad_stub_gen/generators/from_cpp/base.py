import dataclasses
import logging
import re
from abc import ABC
from collections import defaultdict
from itertools import chain
from typing import Any, Iterable, DefaultDict

from freecad_stub_gen.generators.method.arg_suit_merger import mergeArgSuitesGen
from freecad_stub_gen.generators.method.doc_string import generateArgSuitFromDocstring
from freecad_stub_gen.generators.method.format_finder import FormatFinder
from freecad_stub_gen.generators.method.function_finder import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.logger import LEVEL_CODE
from freecad_stub_gen.module_container import Module

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
        if len(self.args) > 2:
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


class FreecadStubGeneratorFromCpp(FormatFinder, ABC):
    def getStub(self, mod: Module, moduleName: str):
        if (result := ''.join(self._genStub())).rstrip():
            header = f'# {self.baseGenFilePath.name}\n'
            newMod = Module(header + result, self.requiredImports)
            mod[moduleName].update(newMod)

    def _genStub(self) -> Iterable[str]:
        raise NotImplementedError

    def _genAllMethods(self, it: Iterable[Method], firstArgName='',
                       functionSpacing: int = 1) -> Iterable[str]:
        methodNameToMethod: DefaultDict[str, list[Method]] = defaultdict(list)
        for method in it:
            methodNameToMethod[method.pythonMethodName].append(method)

        for methods in methodNameToMethod.values():
            if firstArgName:
                for m in methods:
                    m.pythonArgs = f'{firstArgName}{", " if m.pythonArgs else ""}{m.pythonArgs}'

            docContent = next((met.doc for met in methods if met.doc is not None), None)
            uniqueMethods = list({str(m): m for m in methods}.values())
            yield self.convertMethodToStr(
                methods[0].pythonMethodName, uniqueMethods,
                docContent, functionSpacing=functionSpacing)

    def _genMethodWithArgs(self, method: Method) -> Iterable[Method]:
        if method.doc is None:
            docSuites = []
        else:
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

    def _findFunctionCallsGen(self, content: str) -> Iterable[Method]:
        for match in chain(
                self.REG_NOARGS_METHOD.finditer(content),
                self.REG_VARGS_METHOD.finditer(content),
                self.REG_KEYWORD_METHOD.finditer(content),
        ):
            funcCall = findFunctionCall(
                content, match.start(), bracketL='(', bracketR=')')
            funcCallStartPos = funcCall.find('(') + 1
            method = Method(list(generateExpressionUntilChar(
                funcCall, funcCallStartPos, splitChar=',')))
            yield from self._genMethodWithArgs(method)
