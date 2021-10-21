import dataclasses
import logging
import re
from abc import ABC
from collections import defaultdict
from inspect import Signature, Parameter
from itertools import chain
from typing import Any, Iterable, DefaultDict

from freecad_stub_gen.generators.common.arg_suit_merger import mergeParamIntoSignatureGen
from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.common.doc_string import generateArgSuitFromDocstring
from freecad_stub_gen.generators.common.gen_method import MethodGenerator
from freecad_stub_gen.logger import LEVEL_CODE
from freecad_stub_gen.module_container import Module

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Method:
    args: list[str]
    pythonMethodName: str = ''
    cFunction: str = ''
    doc: str = None
    pythonSignature: Signature = None

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

    def insertParam(self, param: Parameter):
        assert self.pythonSignature is not None
        newParameters = [param] + list(self.pythonSignature.parameters.values())
        self.pythonSignature = self.pythonSignature.replace(parameters=newParameters)

    def __repr__(self):
        return f'{self.cClass}::{self.cFunction}'

    def __str__(self):
        assert self.pythonSignature is not None
        return str(self.pythonSignature)


@dataclasses.dataclass(repr=False)
class PyMethodDef(Method):
    flags: Any = None

    def __post_init__(self):
        super().__post_init__()
        self.flags = self.args[2]


class BaseGeneratorFromCpp(MethodGenerator, ABC):
    def getStub(self, mod: Module, moduleName: str):
        if (result := ''.join(self._genStub(moduleName))).rstrip():
            header = f'# {self.baseGenFilePath.name}\n'
            newMod = Module(header + result, self.requiredImports)
            mod[moduleName].update(newMod)

    def _genStub(self, moduleName: str) -> Iterable[str]:
        raise NotImplementedError

    def _genAllMethods(self, it: Iterable[Method], firstParam=None,
                       functionSpacing: int = 1) -> Iterable[str]:
        methodNameToMethod: DefaultDict[str, list[Method]] = defaultdict(list)
        for method in it:
            methodNameToMethod[method.pythonMethodName].append(method)

        for methods in methodNameToMethod.values():
            if firstParam:
                for m in methods:
                    m.insertParam(firstParam)

            docContent = next((met.doc for met in methods if met.doc is not None), '')
            uniqueMethods = list({str(m): m for m in methods}.values())
            yield self.convertMethodToStr(
                methods[0].pythonMethodName, uniqueMethods,
                docContent, functionSpacing=functionSpacing)

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

    def _genMethodWithArgs(self, method: Method, argNumStart=1) -> Iterable[Method]:
        if method.doc is None:
            docSuites = []
        else:
            docSuites = list(generateArgSuitFromDocstring(
                method.pythonMethodName, method.doc))
        codeSuites = list(self.generateArgFromCode(
            method.cFunction, method.cClass, argNumStart=argNumStart))

        yielded = False
        for sig in mergeParamIntoSignatureGen(codeSuites, docSuites):
            yielded = True
            yield dataclasses.replace(method, pythonSignature=sig)

        if not yielded:
            logger.debug(f"Not found args for {method=!r} {self.baseGenFilePath=}")
            if logger.isEnabledFor(LEVEL_CODE):
                logger.log(LEVEL_CODE, self.findFunctionBody(
                    method.cFunction, method.cClass))
