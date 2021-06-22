import dataclasses
import logging
import re
from abc import ABC
from collections import defaultdict
from typing import Any, Iterable, DefaultDict, Optional

from freecad_stub_gen.generators.method.arg_suit_merger import mergeArgSuitesGen
from freecad_stub_gen.generators.method.doc_string import generateArgSuitFromDocstring
from freecad_stub_gen.generators.method.format_finder import FormatFinder
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


class FreecadStubGeneratorFromCpp(FormatFinder, ABC):
    def getStub(self) -> Optional[StubContainer]:
        if result := ''.join(self._genStub()).rstrip():
            header = f'# {self.baseGenFilePath.name}\n'
            return StubContainer(header + result + '\n\n', self.requiredImports)

    def _genStub(self):
        raise NotImplementedError

    def _genAllMethods(self, it: Iterable[Method], isStatic: bool,
                       functionSpacing: int = 1) -> Iterable[str]:
        methodNameToMethod: DefaultDict[str, list[Method]] = defaultdict(list)
        for method in it:
            methodNameToMethod[method.pythonMethodName].append(method)

        for methods in methodNameToMethod.values():
            docContent = next((met.doc for met in methods), None)
            uniqueMethods = list({str(m): m for m in methods}.values())
            yield self.convertMethodToStr(
                methods[0].pythonMethodName, uniqueMethods,
                docContent, isStatic=isStatic, functionSpacing=functionSpacing)

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
