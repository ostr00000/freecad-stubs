import dataclasses
import logging
import re
import xml.etree.ElementTree as ET
from distutils.util import strtobool
from itertools import count
from typing import Iterator, Generator

from freecad_stub_gen.generators.method.format_finder import FormatFinder
from freecad_stub_gen.generators.method.function_finder import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.method.types_converter import KeyWorldOnlyArg, PositionalOnlyArg, \
    Arg

logger = logging.getLogger(__name__)


class MethodGenerator(FormatFinder):
    def genInit(self) -> str:
        # maybe should check self.currentNode.attrib['Constructor']
        return self.genMethod(self.currentNode, cName='PyInit', pythonName='__init__')

    _OVERLOAD = '@typing.overload\n'
    _STATIC = '@staticmethod\n'
    _CLASSIC = '@classmethod\n'

    def genMethod(self, node: ET.Element, cName: str = None, pythonName: str = None) -> str:
        # TODO check more *Py.cpp ?
        ret = ''
        cName = cName or node.attrib["Name"]
        pythonName = pythonName or node.attrib["Name"]
        static = self._STATIC if strtobool(node.attrib.get('Static', 'False')) else ''
        classic = self._STATIC if strtobool(node.attrib.get('Class', 'False')) else ''
        firstArgumentName = self._firstArgumentName(bool(static), bool(classic))

        sigArgs = list(self._signatureArgGen(cName, node, firstArgumentName))
        if len(sigArgs) > 1:  # only one signature should not have overload
            self.requiredImports.add('typing')

            ret += static
            ret += classic
            ret += self._OVERLOAD
            ret += f'def {pythonName}({sigArgs[0]}): ...\n\n'

            for arg in sigArgs[1:-1]:
                ret += static
                ret += classic
                ret += self._OVERLOAD
                ret += f'def {pythonName}({arg}): ...\n\n'

            ret += static
            ret += classic
            ret += self._OVERLOAD

        elif len(sigArgs) > 0:
            ret += static
            ret += classic

        if len(sigArgs) > 0:
            # last signature should have docstring
            body = '\n' + self.indent(docs) if (docs := self._genDoc(node)) else ' ...\n'
            ret += f'def {pythonName}({sigArgs[-1]}):{body}\n'

        if strtobool(node.attrib.get('RichCompare', 'False')):
            ret += self._genRichCompare()
        if strtobool(node.attrib.get('NumberProtocol', 'False')):
            ret += self._genNumberProtocol()

        return ret

    @classmethod
    def _firstArgumentName(cls, isStaticMethod: bool, isClassMethod: bool) -> str:
        if isStaticMethod:
            retVal = ''
        elif isClassMethod:
            retVal = 'cls'
        else:
            retVal = 'self'
        return retVal

    def _signatureArgGen(self, methodName: str, node: ET.Element,
                         firstArgumentName: str) -> Iterator[str]:
        retVal = []
        if firstArgumentName:
            retVal.append(firstArgumentName)

        if not self.impContent:
            yield ', '.join(retVal)
            return

        yielded = False
        codeSuites = list(self._generateArgFromCode(methodName, start=len(retVal)))
        docSuite = list(self._generateArgSuiteFromDocString(
            methodName, node, start=len(retVal)))
        if len(codeSuites) == len(docSuite) == 0:
            return  # function does not exist neither in code nor xml

        for docS in docSuite:
            for codeS in codeSuites:
                compatible = True
                matchedSuite = list(retVal)
                docSuiteIt = iter(docS)

                for codeArg in codeS:
                    if isinstance(codeArg, (PositionalOnlyArg, KeyWorldOnlyArg)):
                        matchedSuite.append(codeArg)
                        continue

                    try:
                        docArg = next(docSuiteIt)
                    except StopIteration:
                        compatible = False
                        break

                    newArg = codeArg
                    if codeArg.name is None:
                        newArg = dataclasses.replace(codeArg, name=docArg.name)
                    if codeArg.default and codeArg.value is None:
                        newArg = dataclasses.replace(newArg, value=docArg.value)

                    matchedSuite.append(newArg)

                if compatible and len(list(docSuiteIt)) == 0:
                    yield ', '.join(map(str, matchedSuite))
                    yielded = True

        # maybe nameSuite is empty, try argSuite
        if not yielded:
            for codeS in codeSuites:
                yield ', '.join(map(str, retVal + codeS))
                yielded = True

        # maybe argSuite is empty, try nameSuite
        if not yielded:
            for docS in docSuite:
                yield ', '.join(map(str, retVal + docS))
                yielded = True

        # this should never be reachable
        if not yielded:
            yield ', '.join(retVal)

    @classmethod
    def _generateArgSuiteFromDocString(
            cls, name: str, node: ET.Element, start) -> Iterator[list[Arg]]:
        if not (docString := node.find("./Documentation/UserDocu").text):
            return

        for match in re.finditer(fr'{name}\((.*?)\):?', docString):
            funStart, _funEnd = match.span()
            funCall = findFunctionCall(docString, funStart, bracketL='(', bracketR=')')
            funCall = funCall.removeprefix(name).removeprefix('(').removesuffix(')')
            yield list(cls._argSuiteGen(funCall, start))

    @classmethod
    def _argSuiteGen(cls, funDocString: str, start) -> Iterator[Arg]:
        uniqueNameGen = cls._uniqueArgNameGen(start)
        next(uniqueNameGen)

        for argText in generateExpressionUntilChar(funDocString, 0, ','):
            argText = argText.strip()
            if argText[-2:] == '[]':
                pass
            else:
                argText = argText.removeprefix('[').removesuffix(']')

            if '=' in argText:
                argName, defValue = argText.split('=')
                argName, defValue = argName.strip(), defValue.strip()
                try:
                    eval(defValue, {}, {})
                except Exception as exc:
                    logger.debug(f'Cannot evaluate value: {exc}')
                    defValue = None
            else:
                argName, defValue = argText, None
            uniqueName, argNum = uniqueNameGen.send(argName)
            yield Arg(argNum, '', defValue is not None, uniqueName, defValue)

    REG_ALL_EXCEPT_WORLD = re.compile(r'\W+')
    REG_START_WITH_LETTER = re.compile(r'[a-zA-Z].*')

    @classmethod
    def _uniqueArgNameGen(cls, start=1) -> Generator[tuple[str, int], str, None]:
        name: str = yield
        seen = set()

        for argNum in count(start):
            name = re.sub(cls.REG_ALL_EXCEPT_WORLD, '_', name)
            if not re.match(cls.REG_START_WITH_LETTER, name):
                name = 'arg'

            if name in seen:
                name = f'{name}{argNum}'
            else:
                seen.add(name)
            name = yield name, argNum

    @classmethod
    def _genRichCompare(cls) -> str:
        ret = ''
        ret += cls._genEmptyMethod('__eq__')
        ret += cls._genEmptyMethod('__ne__')
        ret += cls._genEmptyMethod('__lt__')
        ret += cls._genEmptyMethod('__le__')
        ret += cls._genEmptyMethod('__ge__')
        ret += cls._genEmptyMethod('__gt__')
        return ret

    @classmethod
    def _genNumberProtocol(cls) -> str:
        ret = ''
        ret += cls._genEmptyMethod('__add__', 'other')
        ret += cls._genEmptyMethod('__sub__', 'other')
        ret += cls._genEmptyMethod('__mul__', 'other')
        ret += cls._genEmptyMethod('__floordiv__', 'other')
        ret += cls._genEmptyMethod('__divmod__', 'other')
        ret += cls._genEmptyMethod('__pow__', 'power', 'modulo=None')
        ret += cls._genEmptyMethod('__neg__')
        ret += cls._genEmptyMethod('__pos__')
        ret += cls._genEmptyMethod('__abs__')
        ret += cls._genEmptyMethod('__invert__')
        ret += cls._genEmptyMethod('__lshift__', 'other')
        ret += cls._genEmptyMethod('__rshift__', 'other')
        ret += cls._genEmptyMethod('__and__', 'other')
        ret += cls._genEmptyMethod('__xor__', 'other')
        ret += cls._genEmptyMethod('__or__', 'other')
        ret += cls._genEmptyMethod('__int__')
        ret += cls._genEmptyMethod('__float__')
        return ret

    @classmethod
    def _genEmptyMethod(cls, name: str, *args) -> str:
        return f'def {name}({", ".join(("self",) + args)}): ...\n\n'
