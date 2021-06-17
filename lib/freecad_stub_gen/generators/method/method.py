import logging
import xml.etree.ElementTree as ET
from distutils.util import strtobool
from typing import Iterator

from freecad_stub_gen.generators.method.arg_suit_merger import mergeArgSuitesGen
from freecad_stub_gen.generators.method.doc_string import generateArgSuitFromDocstring
from freecad_stub_gen.generators.method.format_finder import FormatFinder
from freecad_stub_gen.generators.method.types_converter import Arg
from freecad_stub_gen.generators.names import getSimpleClassName

logger = logging.getLogger(__name__)


class MethodGenerator(FormatFinder):
    def genInit(self) -> str:
        # maybe should check self.currentNode.attrib['Constructor']
        className = getSimpleClassName(self.currentNode)
        return self.genMethod(self.currentNode, cName='PyInit',
                              docName=className, pythonName='__init__')

    def genMethod(self, node: ET.Element, cName: str = None,
                  docName: str = None, pythonName: str = None) -> str:
        cName = cName or node.attrib['Name']
        docName = docName or node.attrib['Name']
        pythonName = pythonName or node.attrib['Name']
        static = strtobool(node.attrib.get('Static', 'False'))
        classic = strtobool(node.attrib.get('Class', 'False'))
        firstArgumentName = self._firstArgumentName(bool(static), bool(classic))

        uniqueArgs = dict.fromkeys(self._signatureArgGen(
            cName, docName, node, firstArgumentName))
        sigArgs = list(uniqueArgs.keys())
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

    def _signatureArgGen(self, cName: str, docName: str, node: ET.Element,
                         firstArgumentName: str) -> Iterator[str]:
        retVal = []
        if firstArgumentName:
            retVal.append(firstArgumentName)

        if not self.impContent:
            yield ', '.join(retVal)
            return

        codeSuites = list(self.generateArgFromCode(
            cName, argNumStart=len(retVal)))
        docSuites = list(self._generateArgSuiteFromDocString(
            docName, node, argNumStart=len(retVal)))
        yield from mergeArgSuitesGen(codeSuites, docSuites, firstArgumentName)

    @classmethod
    def _generateArgSuiteFromDocString(
            cls, name: str, node: ET.Element, argNumStart: int) -> Iterator[list[Arg]]:
        if not (docString := node.find("./Documentation/UserDocu").text):
            return

        yield from generateArgSuitFromDocstring(name, docString, argNumStart)

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
    def genNumberProtocol(cls, className: str) -> str:
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
