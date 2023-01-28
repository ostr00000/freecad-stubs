import contextlib
import logging
import xml.etree.ElementTree as ET
from abc import ABC
from collections.abc import Iterator
from functools import cached_property, lru_cache
from inspect import Parameter
from pathlib import Path

from freecad_stub_gen.generators.common.annotation_parameter import AnnotationParam, SelfSignature
from freecad_stub_gen.generators.common.doc_string import generateSignaturesFromDocstring, \
    getDocFromNode
from freecad_stub_gen.generators.common.gen_method import MethodGenerator
from freecad_stub_gen.generators.common.names import getClassNameFromNode
from freecad_stub_gen.generators.common.signature_merger import SignatureMerger
from freecad_stub_gen.generators.from_xml.base import BaseXmlGenerator
from freecad_stub_gen.util import toBool

logger = logging.getLogger(__name__)


class XmlMethodGenerator(BaseXmlGenerator, MethodGenerator, ABC):
    @contextlib.contextmanager
    def newImportContext(self):
        oldImports = self.requiredImports
        self.requiredImports = type(self.requiredImports)()
        try:
            yield
        finally:
            self.requiredImports = oldImports

    def genInit(self) -> str:
        """Generate stub for __init__ method."""
        className = getClassNameFromNode(self.currentNode)

        # Maybe we should check `self.currentNode.attrib['Constructor']`?
        # Better check `PyMake` - it is possible to return something different from `nullptr`

        with self.newImportContext():
            makeSignatures = list(self.generateSignaturesFromCode('PyMake', cClassName=className))

        if not makeSignatures:
            # Cannot find `PyMake` signature, therefore we also do not find `PyInit`.
            return ''

        if all(ms.return_annotation == Parameter.empty for ms in makeSignatures):
            # A return type of `PyMake` should not be empty,
            # otherwise it means that the developer do not want to call `__init__`.
            return ''

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

        isStatic = toBool(node.attrib.get('Static', False))
        isClassic = toBool(node.attrib.get('Class', False))
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

        sigMerger = SignatureMerger(codeSignatures, docSignatures, firstParam, cFunName=cFunName)
        yield from sigMerger.genMergedCodeAndDocSignatures()

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
        """
        Source: find `PyNumberMethods` in `src/Tools/generateTemplates/templateClassPyExport.py`
        https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/generateTemplates/templateClassPyExport.py
        https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods
        https://docs.python.org/3/c-api/typeobj.html#sub-slots
        """
        # TODO P3 find real IN and OUT types - ex.:
        #  assert isinstance(FreeCAD.Vector(1, 2, 3) * FreeCAD.Vector(1, 2, 3), int)
        # TODO P3 remove fake methods - methods that always raise exception when called
        # TODO P3 implement other Protocols - ex. PySequenceMethods
        ret = ''
        ret += cls._genEmptyMethod('__add__', 'other', retType=className, reflected=True)
        ret += cls._genEmptyMethod('__sub__', 'other', retType=className, reflected=True)
        ret += cls._genEmptyMethod('__mul__', 'other', retType=className, reflected=True)
        ret += cls._genEmptyMethod('__mod__', 'other', reflected=True)
        ret += cls._genEmptyMethod('__divmod__', 'other', reflected=True)
        ret += cls._genEmptyMethod('__pow__', 'power', 'modulo=None', reflected=True)
        ret += cls._genEmptyMethod('__neg__', retType=className)
        ret += cls._genEmptyMethod('__pos__', retType=className)
        ret += cls._genEmptyMethod('__abs__', retType=className)
        ret += cls._genEmptyMethod('__bool__', retType=className)
        ret += cls._genEmptyMethod('__invert__')
        ret += cls._genEmptyMethod('__lshift__', 'other', reflected=True)
        ret += cls._genEmptyMethod('__rshift__', 'other', reflected=True)
        ret += cls._genEmptyMethod('__and__', 'other', reflected=True)
        ret += cls._genEmptyMethod('__xor__', 'other', reflected=True)
        ret += cls._genEmptyMethod('__or__', 'other', reflected=True)
        ret += cls._genEmptyMethod('__int__')
        ret += cls._genEmptyMethod('__float__')
        ret += cls._genEmptyMethod('__truediv__', 'other', retType=className, reflected=True)
        return ret

    @classmethod
    def _genEmptyMethod(cls, name: str, *args, retType=None, reflected=False) -> str:
        if reflected:
            reflectedName = '__r' + name[2:]
            ret = cls._genEmptyMethod(name, *args, retType=retType)
            ret += cls._genEmptyMethod(reflectedName, *args, retType=retType)
            return ret

        retType = f' -> {retType}' if retType else ''
        return f'def {name}({", ".join(("self",) + args)}){retType}: ...\n\n'

    @lru_cache
    def findFunctionBody(self, cFuncName: str, cClassName: str):
        """Override method to search `funcName` also in parent."""
        if res := super().findFunctionBody(cFuncName, cClassName):
            return res

        try:
            p = self.parentXmlPath
        except AttributeError:
            baseClass = None
        else:
            baseClass = type(self).safeCreate(p)

        if baseClass:
            return baseClass.findFunctionBody(cFuncName, cClassName)

        if cFuncName in ('PyInit', 'PyMake'):
            # skip implicit constructor - probably inherited from PyObject
            return

        logger.error(f"Cannot find {self.parentXmlPath=} for {self.baseGenFilePath=}")

    @cached_property
    def parentXmlPath(self) -> Path:
        fatherInclude = self.currentNode.attrib['FatherInclude']
        parentFile = (self.sourceDir / fatherInclude).with_suffix('.xml')
        return parentFile
