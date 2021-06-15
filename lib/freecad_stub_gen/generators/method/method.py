import dataclasses
import keyword
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
from freecad_stub_gen.generators.names import validatePythonValue

logger = logging.getLogger(__name__)


class MethodGenerator(FormatFinder):
    def genInit(self) -> str:
        # maybe should check self.currentNode.attrib['Constructor']
        return self.genMethod(self.currentNode, cName='PyInit', pythonName='__init__')

    def genMethod(self, node: ET.Element, cName: str = None, pythonName: str = None) -> str:
        cName = cName or node.attrib["Name"]
        pythonName = pythonName or node.attrib["Name"]
        static = strtobool(node.attrib.get('Static', 'False'))
        classic = strtobool(node.attrib.get('Class', 'False'))
        firstArgumentName = self._firstArgumentName(bool(static), bool(classic))

        sigArgs = list(self._signatureArgGen(cName, node, firstArgumentName))
        return self.convertMethodToStr(
            pythonName, sigArgs, self._getDocFromNode(node), classic, static)

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
        codeSuites = list(self.generateArgFromCode(methodName, start=len(retVal)))
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
                defValue = validatePythonValue(defValue)
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
            elif keyword.iskeyword(name):
                name += '_'

            if name in seen:
                name = f'{name}{argNum}'
            else:
                seen.add(name)
            name = yield name, argNum

    @classmethod
    def genRichCompare(cls) -> str:
        ret = ''
        ret += cls._genEmptyMethod('__eq__', 'other', retType='bool')
        ret += cls._genEmptyMethod('__ne__', 'other', retType='bool')
        ret += cls._genEmptyMethod('__lt__', 'other', retType='bool')
        ret += cls._genEmptyMethod('__le__', 'other', retType='bool')
        ret += cls._genEmptyMethod('__ge__', 'other', retType='bool')
        ret += cls._genEmptyMethod('__gt__', 'other', retType='bool')
        return ret

    @classmethod
    def genNumberProtocol(cls, className:str) -> str:
        ret = ''
        ret += cls._genEmptyMethod('__add__', 'other', retType=className)
        ret += cls._genEmptyMethod('__sub__', 'other', retType=className)
        ret += cls._genEmptyMethod('__mul__', 'other', retType=className)
        ret += cls._genEmptyMethod('__floordiv__', 'other')
        ret += cls._genEmptyMethod('__divmod__', 'other')
        ret += cls._genEmptyMethod('__pow__', 'power', 'modulo=None')
        ret += cls._genEmptyMethod('__neg__', retType=className)
        ret += cls._genEmptyMethod('__pos__', retType=className)
        ret += cls._genEmptyMethod('__abs__', retType=className)
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
    def _genEmptyMethod(cls, name: str, *args, retType=None) -> str:
        retType = f' -> {retType}' if retType else ''
        return f'def {name}({", ".join(("self",) + args)}){retType}: ...\n\n'
