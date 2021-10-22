import logging
import xml.etree.ElementTree as ET
from abc import ABC
from distutils.util import strtobool
from functools import cached_property
from inspect import Parameter, Signature
from pathlib import Path
from typing import Iterator

from freecad_stub_gen.generators.common.signature_merger import mergeSignaturesGen
from freecad_stub_gen.generators.common.doc_string import generateSignaturesFromDocstring, \
    getDocFromNode
from freecad_stub_gen.generators.common.gen_method import MethodGenerator
from freecad_stub_gen.generators.common.names import getClassNameFromNode
from freecad_stub_gen.generators.common.annotation_parameter import AnnotationParam, SelfSignature
from freecad_stub_gen.generators.from_xml.base import BaseXmlGenerator

logger = logging.getLogger(__name__)


class XmlMethodGenerator(BaseXmlGenerator, MethodGenerator, ABC):
    def genInit(self) -> str:
        """Generate stub for __init__ method."""
        # maybe should check self.currentNode.attrib['Constructor']
        className = getClassNameFromNode(self.currentNode)
        return self.genMethod(self.currentNode, cName='PyInit',
                              docName=className, pythonName='__init__')

    def genMethod(self, node: ET.Element, cName: str = None,
                  docName: str = None, pythonName: str = None) -> str:
        """Generate stub for method specified in arguments."""
        cName = cName or node.attrib['Name']
        docName = docName or node.attrib['Name']
        pythonName = pythonName or node.attrib['Name']
        static = strtobool(node.attrib.get('Static', 'False'))
        classic = strtobool(node.attrib.get('Class', 'False'))
        firstParam = AnnotationParam.getFirstParam(bool(static), bool(classic))

        uniqueSignatures = dict.fromkeys(map(
            str, self._signatureArgGen(cName, docName, node, firstParam)))
        signatures = list(uniqueSignatures.keys())
        return self.convertMethodToStr(
            pythonName, signatures, getDocFromNode(node), classic, static)

    def _signatureArgGen(self, cName: str, docName: str, node: ET.Element,
                         firstParam: Parameter = None) -> Iterator[Signature]:
        parameters = []
        if firstParam:
            parameters.append(firstParam)

        if not self.impContent:
            yield SelfSignature(parameters)
            return

        codeSignatures = list(self.generateSignaturesFromCode(
            cName, argNumStart=len(parameters)))
        docSignatures = list(self._generateSignaturesFromDocString(
            docName, node, argNumStart=len(parameters)))

        yield from mergeSignaturesGen(codeSignatures, docSignatures, firstParam)

    @classmethod
    def _generateSignaturesFromDocString(
            cls, name: str, node: ET.Element, argNumStart: int) -> Iterator[Signature]:
        if not (docString := node.find("./Documentation/UserDocu").text):
            return

        yield from generateSignaturesFromDocstring(name, docString, argNumStart)

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
        ret += cls._genEmptyMethod('__truediv__', 'other', retType=className)
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

    def findFunctionBody(self, funcName: str, className: str = '') -> str | None:
        """Override method to search `funcName` also in parent."""
        if res := super().findFunctionBody(funcName, className):
            return res

        if not (baseClass := type(self).safeCreate(self.parentXmlPath)):
            if funcName == 'PyInit':
                pass  # skip implicit constructor - probably inherited from PyObject
            else:
                logger.error(f"Cannot find {self.parentXmlPath=} for {self.baseGenFilePath=}")
            return

        return baseClass.findFunctionBody(funcName, className)

    @cached_property
    def parentXmlPath(self) -> Path:
        fatherInclude = self.currentNode.attrib['FatherInclude'].replace('/', '.')
        parentFile = (self.sourceDir / fatherInclude).with_suffix('.xml')
        return parentFile
