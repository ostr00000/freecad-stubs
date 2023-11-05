import logging
import re
from inspect import Parameter
from typing import Iterator

from ordered_set import OrderedSet

from freecad_stub_gen.cpp_code.converters import convertToPythonValue
from freecad_stub_gen.generators.common.annotation_parameter import AnnotationParam, RawRepr, \
    RawStringRepresentation
from freecad_stub_gen.generators.common.arguments_converter.definitions import \
    C_TYPE_TO_PYTHON_TYPE, MISSING_DEFAULT_ARG, UNKNOWN_DEFAULT_ARG, parseSizeMap, parseTypeMap
from freecad_stub_gen.generators.common.arguments_converter.function_conv import FunctionConv
from freecad_stub_gen.generators.common.arguments_converter.sequence_stack import SequenceStack
from freecad_stub_gen.generators.common.names import getClassWithModulesFromPointer, \
    getModuleName
from freecad_stub_gen.generators.common.return_type_converter.str_wrapper import StrWrapper

logger = logging.getLogger(__name__)


class InvalidPointerFormat(ValueError):
    pass


class TypesConverter:

    def __init__(self, functionConv: FunctionConv,
                 requiredImports: OrderedSet[str],
                 cArgNum: int = 2):
        self.fun = functionConv
        self.requiredImports = requiredImports
        self._sequenceStack = SequenceStack()
        self._isArgOptional = False

        if self.fun.kwargList:
            self._parameterKind = Parameter.POSITIONAL_OR_KEYWORD
        else:
            self._parameterKind = Parameter.POSITIONAL_ONLY

        self._pythonArgNum = 0
        self._cArgNum = cArgNum
        self._remainingFormat = self.fun.formatStr

    def safeConvertFormatToTypes(self) -> Iterator[Parameter]:
        try:
            yield from self._convertFormatToTypes()
        except InvalidPointerFormat as ex:
            logger.error(f'{ex}, {self._remainingFormat=}, {self.fun}')

    def _convertFormatToTypes(self) -> Iterator[Parameter]:
        while self._remainingFormat:
            for formatSize in range(min(3, len(self._remainingFormat)), 0, -1):

                pythonArgName = None
                defaultValue = MISSING_DEFAULT_ARG
                curFormat: str = self._remainingFormat[:formatSize]

                match curFormat:
                    case '(':
                        self._sequenceStack.startSequenceParsing()
                        self._nextFormat(formatSize)
                        break

                    case ')':
                        curType, pythonArgName, defaultValue = \
                            self._sequenceStack.endSequenceParsing()

                    case 'O!':
                        curType = self._findPointerType(self._cArgNum)

                    case _:
                        if (curType := parseTypeMap.get(curFormat)) is None:
                            continue

                yield from self._processParam(curFormat, curType, pythonArgName, defaultValue)
                self._cArgNum += parseSizeMap[curFormat]
                self._nextFormat(formatSize)
                break
            else:
                self._remainingFormat = self._processSpecialFormat()

    def _nextFormat(self, formatSize: int):
        self._remainingFormat = self._remainingFormat[formatSize:]

    def _findPointerType(self, cArgNum: int) -> str:
        # pylint: disable=raise-missing-from
        try:
            pointerArg = self.fun.argumentStrings[cArgNum]
        except IndexError:  # some implementations are broken, example:
            # PyObject* BSplineCurve2dPy::insertKnot(PyObject * args)
            # with expectedArg=7, but providedArg=5, code:
            # if (!PyArg_ParseTuple(args, "d|idO!", &U, &M, &tol))
            raise InvalidPointerFormat(f"Function has not enough arguments {self.fun}")

        if (typ := self._convertPointerToType(pointerArg)) is not None:
            return typ

        if pointerArg.endswith('::type_object()'):
            logger.debug(f"Cannot detect pointer {pointerArg=}")
            self.requiredImports.add('typing')
            return 'typing.Any'

        exc = InvalidPointerFormat(f"Unknown pointer format {pointerArg=}")
        try:
            if self._findPointerType(cArgNum + 1) is not None:
                exc = InvalidPointerFormat("Format has swapped type")
        except Exception:
            raise exc

        raise exc

    def _convertPointerToType(self, pointerArg: str) -> str | None:
        pointerArg = pointerArg.removeprefix('&').removeprefix('(').removesuffix(')')

        match StrWrapper(pointerArg):
            case StrWrapper(end='::Type' | '::type_object('):
                classWithModules = getClassWithModulesFromPointer(pointerArg)
                self.requiredImports.add(getModuleName(classWithModules, required=True))
                return classWithModules

            case StrWrapper(start='Py'):
                return C_TYPE_TO_PYTHON_TYPE[pointerArg]

            case _:
                logger.error(f"Unknown pointer kind {pointerArg=}")
                return None

    def _processParam(self, curFormat: str, curType: str, pythonArgName: str | None, defaultValue):
        if pythonArgName is None:
            pythonArgName = self.fun.getPythonArgName(curFormat, self._cArgNum, self._pythonArgNum)
        assert isinstance(pythonArgName, str)

        if defaultValue is MISSING_DEFAULT_ARG:
            defaultValue = self._getDefaultValue(curFormat, self._cArgNum)

        if self._sequenceStack:
            self._sequenceStack.addElementToSequence(curType, pythonArgName, defaultValue)
            return

        if defaultValue is UNKNOWN_DEFAULT_ARG:
            # replace when we are ready
            # (after addElementToSequence will no longer be used)
            defaultValue = None

        yield AnnotationParam(
            pythonArgName, self._parameterKind, default=defaultValue,
            annotation=RawRepr(curType))
        self._pythonArgNum += 1

    def _getDefaultValue(self, curFormat: str, cArgNum: int):
        retVal = UNKNOWN_DEFAULT_ARG if self._isArgOptional else Parameter.empty
        if not (cArgName := self.fun.getCurArgName(curFormat, cArgNum)):
            return retVal

        fa = list(re.finditer(
            rf'\b{cArgName}\b\s*=\s*(?P<value>[^;,]*)',
            self.fun.varDeclarationCode))
        for m in fa:
            val = m.group('value')
            if val.startswith('Py_'):
                val = val.removeprefix('Py_')

            ok, pVal = convertToPythonValue(val)
            if ok:
                retVal = pVal
                break

            match StrWrapper(val):
                case 'nullptr':
                    retVal = None
                case StrWrapper(end='_MAX'):
                    self.requiredImports.add('sys')
                    retVal = RawStringRepresentation('sys.float_info.max')
                case StrWrapper('M_PI/8'):
                    self.requiredImports.add('math')
                    retVal = RawStringRepresentation('math.pi / 8')
                case _:
                    continue
            break
        else:
            if fa and retVal is not Parameter.empty:
                expressions = [m.group('value') for m in fa]
                ignoreText = ['->', '()', '::']
                if all(i not in e for e in expressions for i in ignoreText):
                    logger.warning(f"Unable to convert c {expressions=} to python")

        if retVal is not Parameter.empty:
            self._isArgOptional = True

        return retVal

    def _processSpecialFormat(self):
        curVal = self._remainingFormat[0]
        if curVal == '|':
            self._isArgOptional = True
        elif curVal == '$':
            self._isArgOptional = True
            self._parameterKind = Parameter.KEYWORD_ONLY
        elif curVal in ':;':
            self._remainingFormat = ''
        else:
            logger.error(f"Unknown format: {self._remainingFormat}")
        return self._remainingFormat[1:]
