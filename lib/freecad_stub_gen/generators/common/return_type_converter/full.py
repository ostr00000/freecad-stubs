import logging
import re
from inspect import Signature

from freecad_stub_gen.generators.common.annotation_parameter import RawRepr
from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar
from freecad_stub_gen.generators.common.names import validatePythonValue
from freecad_stub_gen.generators.common.return_type_converter.arg_types import InvalidReturnType, \
    UnionArguments
from freecad_stub_gen.generators.common.return_type_converter.base import ReturnTypeConverterBase
from freecad_stub_gen.generators.common.return_type_converter.inner_type_dict import \
    ReturnTypeInnerDict
from freecad_stub_gen.generators.common.return_type_converter.inner_type_list import \
    ReturnTypeInnerList
from freecad_stub_gen.generators.common.return_type_converter.inner_type_tuple import \
    ReturnTypeInnerTuple
from freecad_stub_gen.generators.common.return_type_converter.str_wrapper import StrWrapper
from freecad_stub_gen.module_namespace import moduleNamespace
from freecad_stub_gen.util import OrderedSet

logger = logging.getLogger(__name__)


class ReturnTypeConverter(
    ReturnTypeInnerList, ReturnTypeInnerTuple, ReturnTypeInnerDict, ReturnTypeConverterBase
):
    REG_RETURN = re.compile(r'return ([^;]+);')

    def getStrReturnType(self) -> str:
        if (ret := self.getReturnType()) != Signature.empty:
            return str(ret)
        return 'object'

    def getReturnType(self):
        returnTypes = OrderedSet(self._genReturnType())
        return RawRepr(*returnTypes)

    def _genReturnType(self):
        for match in self.REG_RETURN.finditer(self.functionBody):
            try:
                retType = self._getReturnTypeForText(match.group(1), match.end())
            except InvalidReturnType:
                continue
            if not isinstance(retType, UnionArguments):
                retType = UnionArguments((retType,))
            yield from retType
            self.requiredImports.update(retType.imports)

    EXCEPTION_SET_STRING_REG = re.compile(r'PyErr_SetString\(([^;]+)\);')
    EXCEPTION_PY_REG = re.compile(r'throw\s+Py::(?P<exc>\w+)\((?P<args>[^;]*)\);')

    def getExceptionsFromCode(self):
        exceptions = OrderedSet()

        for exceptionMatch in self.EXCEPTION_PY_REG.finditer(self.functionBody):
            exceptionName = exceptionMatch.group('exc')
            if exceptionName == 'Exception' and (exceptionArgs := exceptionMatch.group('args')):
                args = list(generateExpressionUntilChar(
                    exceptionArgs, 0, ',', bracketL='(', bracketR=')'))
                if realExceptionName := args[0]:
                    exceptions.add(self._getExceptionTypeFromArgument(realExceptionName))
                    continue

            if validatePythonValue(exceptionName) is None:
                logger.error(f'Invalid exception value: {exceptionName}')
            else:
                exceptions.add(exceptionName)

        for exceptionMatch in self.EXCEPTION_SET_STRING_REG.finditer(self.functionBody):
            funArgs = list(generateExpressionUntilChar(
                exceptionMatch.group(1), 0, ',', bracketL='(', bracketR=')'))
            exceptions.add(self._getExceptionTypeFromArgument(funArgs[0]))

        return exceptions

    def _getExceptionTypeFromArgument(self, exceptionArgument: str):
        exception: str
        match exceptionArgument.split('::'):
            case [str(exception)]:
                pass
            case [_namespace, str(exception)]:
                pass
            case _:
                raise ValueError

        match StrWrapper(exception):
            case StrWrapper('PyExc_'):
                exceptionType = exception.removeprefix('PyExc_')

            case StrWrapper('BaseException'):
                exception = exception.removeprefix('BaseException')
                exceptionType = f'FreeCAD.{exception}'
                self.requiredImports.add('FreeCAD')

            case StrWrapper('PartException'):
                exception = exception.removeprefix('PartException')
                exceptionType = f'Part.{exception}'
                self.requiredImports.add(moduleNamespace.MODULE_TO_ALIAS['Part'])

            case _:
                raise ValueError(f'Unknown exception: "{exception}"')

        return exceptionType
