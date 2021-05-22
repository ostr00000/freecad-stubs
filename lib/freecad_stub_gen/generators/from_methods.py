import dataclasses
import logging
import re
from collections import defaultdict
from itertools import chain
from pathlib import Path
from typing import Any, Iterable, DefaultDict

from more_itertools import islice_extended

from freecad_stub_gen.generators.method.format_finder import FormatFinder
from freecad_stub_gen.generators.method.function_finder import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.method.types_converter import Arg

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Method:
    args: list[str]
    pythonMethodName: str = ''
    cPointer: str = ''
    doc: str = None
    pythonArgs: list[Arg] = None

    REG_WHITESPACE_WITH_APOSTROPHE = re.compile(r'"\s*"')

    def __post_init__(self):
        self.args = [
            e.strip().removesuffix('}').removesuffix('"').removeprefix('"')
            for e in self.args]

        self.pythonMethodName = self.args[0]
        self.cPointer = self.parsePointer(self.args[1])
        try:
            self.doc = re.sub(
                self.REG_WHITESPACE_WITH_APOSTROPHE, '', self.args[-1]
            ).replace('\\n', '\n')
        except IndexError:
            pass

    REG_POINTER = re.compile(r'.*\b(\w+)\b')

    @classmethod
    def parsePointer(cls, pointer: str) -> str:
        match = cls.REG_POINTER.match(pointer)
        assert match
        return match.group(1)

    def __str__(self):
        return ', '.join(map(str, self.pythonArgs))


@dataclasses.dataclass
class PyMethodDef(Method):
    flags: Any = None

    def __post_init__(self):
        super().__post_init__()
        self.flags = self.args[2]


class FreecadStubGeneratorFromMethods(FormatFinder):

    def generateToFile(self, targetFile: Path):
        if (content := self.getMethodsText()).strip():
            targetFile.parent.mkdir(exist_ok=True, parents=True)
            with open(targetFile, 'w') as file:
                file.write(content)

    def getMethodsText(self) -> str:
        result = ''.join(self._genAllMethods())
        return f'{self.genImports()}{result}'.rstrip() + '\n'

    def _genAllMethods(self) -> Iterable[str]:
        methodNameToMethod: DefaultDict[str, list[Method]] = defaultdict(list)
        for method in chain(self._findArrayGen(), self._findFunctionCallsGen()):
            methodNameToMethod[method.pythonMethodName].append(method)

        for methods in methodNameToMethod.values():
            docContent = next((met.doc for met in methods), None)
            yield self.convertMethodToStr(
                methods[0].pythonMethodName, methods, docContent, functionSpacing=2)

    REG_METHOD_DEF = re.compile(r'PyMethodDef')

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
        yielded = False
        for argList in self.generateArgFromCode(method.cPointer):
            yielded = True
            yield dataclasses.replace(method, pythonArgs=argList)

        if not yielded:
            logger.debug(f"Not found args for {method.pythonMethodName=} "
                         f"{self.baseGenFilePath=}")

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
