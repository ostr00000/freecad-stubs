import logging
import xml.etree.ElementTree as ET
from abc import ABC
from collections.abc import Iterator
from distutils.util import strtobool
from functools import cached_property, lru_cache
from inspect import Parameter
from pathlib import Path

from freecad_stub_gen.generators.common.annotation_parameter import AnnotationParam, SelfSignature
from freecad_stub_gen.generators.common.doc_string import generateSignaturesFromDocstring, \
    getDocFromNode
from freecad_stub_gen.generators.common.gen_method import MethodGenerator
from freecad_stub_gen.generators.common.names import getClassNameFromNode
from freecad_stub_gen.generators.common.signature_merger import mergeSignaturesGen
from freecad_stub_gen.generators.from_xml.base import BaseXmlGenerator

logger = logging.getLogger(__name__)


class XmlMethodGenerator(BaseXmlGenerator, MethodGenerator, ABC):
    def genInit(self) -> str:
        """Generate stub for __init__ method."""
        # maybe should check self.currentNode.attrib['Constructor']
        className = getClassNameFromNode(self.currentNode)
        return self.genMethod(self.currentNode, cFunName='PyInit',
                              cClassName=className, pythonFunName='__init__',
                              docsFunName=className)

    def genMethod(self, node: ET.Element, cFunName: str = None,
                  cClassName: str = None, pythonFunName: str = None,
                  docsFunName: str = None) -> str:
        """Generate stub for method specified in arguments."""
        cFunName = cFunName or node.attrib['Name']
        pythonFunName = pythonFunName or node.attrib['Name']
        docsFunName = docsFunName or node.attrib['Name']

        isStatic = strtobool(node.attrib.get('Static', 'False'))
        isClassic = strtobool(node.attrib.get('Class', 'False'))
        firstParam = AnnotationParam.getFirstParam(isStatic, isClassic)

        allSignatures = list(self._signatureArgGen(
            cFunName, cClassName, docsFunName, node, firstParam))
        uniqueSignatures = dict.fromkeys(map(str, allSignatures))
        signatures = list(uniqueSignatures.keys())

        docs = getDocFromNode(node)
        docs += SelfSignature.getExceptionsDocs(allSignatures)

        return self.convertMethodToStr(
            pythonFunName, signatures, docs, isClassic, isStatic)

    def _signatureArgGen(self, cFunName: str, cClassName: str, docsFunName: str, node: ET.Element,
                         firstParam: Parameter = None) -> Iterator[SelfSignature]:
        parameters = []
        if firstParam:
            parameters.append(firstParam)

        if not self.impContent:
            yield SelfSignature(parameters)
            return

        codeSignatures = list(self.generateSignaturesFromCode(
            cFunName, cClassName=cClassName, argNumStart=len(parameters)))
        docSignatures = list(self._generateSignaturesFromDocString(
            docsFunName, node, argNumStart=len(parameters)))

        yield from mergeSignaturesGen(codeSignatures, docSignatures, firstParam)

    @classmethod
    def _generateSignaturesFromDocString(
            cls, name: str, node: ET.Element, argNumStart: int) -> Iterator[SelfSignature]:
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

    @lru_cache
    def findFunctionBody(self, cFuncName: str, cClassName: str):
        """Override method to search `funcName` also in parent."""
        if res := super().findFunctionBody(cFuncName, cClassName):
            return res

        if not (baseClass := type(self).safeCreate(self.parentXmlPath)):
            if cFuncName == 'PyInit':
                pass  # skip implicit constructor - probably inherited from PyObject
            else:
                logger.error(f"Cannot find {self.parentXmlPath=} for {self.baseGenFilePath=}")
            return

        return baseClass.findFunctionBody(cFuncName, cClassName)

    @cached_property
    def parentXmlPath(self) -> Path:
        fatherInclude = self.currentNode.attrib['FatherInclude'].replace('/', '.')
        parentFile = (self.sourceDir / fatherInclude).with_suffix('.xml')
        return parentFile
