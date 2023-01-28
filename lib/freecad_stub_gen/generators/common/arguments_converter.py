import logging
import re
from collections.abc import Iterator
from dataclasses import dataclass
from functools import lru_cache
from inspect import Parameter
from typing import Any

from freecad_stub_gen.generators.common.annotation_parameter import AnnotationParam, RawRepr, \
    RawStringRepresentation
from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar, \
    findFunctionCall
from freecad_stub_gen.generators.common.names import getClassWithModulesFromPointer, getModuleName, \
    convertToPythonValue
from freecad_stub_gen.generators.common.return_type_converter.str_wrapper import StrWrapper

logger = logging.getLogger(__name__)
DEFAULT_ARG_NAME = 'arg'
MISSING_DEFAULT_ARG = object()
UNKNOWN_DEFAULT_ARG = object()


class InvalidPointerFormat(ValueError):
    pass


@dataclass
class StackVal:
    objType: str
    pythonArgName: str
    default: Any


class TypesConverter:
    def __init__(self, functionBody: str,
                 funStart: int,
                 requiredImports: set[str],
                 onlyPositional: bool,
                 formatStrPosition: int,
                 argNumStart=1, *,
                 realStartArgNum: int = 2,
                 xmlPath=None,
                 functionName='',
                 ):
        self._functionBody = functionBody
        self._funStart = funStart
        self._funCall = self._getFunCall()

        self.requiredImports = requiredImports
        self.onlyPositional = onlyPositional
        self.formatStrPosition = formatStrPosition
        self.argNumStart = argNumStart
        self.realStartArgNum = realStartArgNum

        self.xmlPath = xmlPath
        self.functionName = functionName
        self._sequenceStack: list[list[StackVal]] = []
        self._isArgOptional = False

        self.argumentStrings = self._getArgumentString()
        self._removeMacros()

        self._kwargList = self._getKwargList()
        self._parameterKind = self._getInitialParameterKind()

    def _getFunCall(self):
        return findFunctionCall(
            self._functionBody, self._funStart, bracketL='(', bracketR=')')

    REG_REMOVE_WHITESPACES = re.compile(r'\s+')

    def _getArgumentString(self):
        sub = re.sub(self.REG_REMOVE_WHITESPACES, '', self._funCall)  # remove whitespace
        argStr = [c.removeprefix('&').strip()
                  for c in generateExpressionUntilChar(sub, sub.find('(') + 1, ',')]
        argStr = [a[1:-1] if a.startswith('(') and a.endswith(')') else a for a in argStr]
        return argStr

    REG_STRING = re.compile(r"""
(["'])          # start with quotation mark as group 1,
(?=             # do not consume matched characters - we match it after we are sure about it,
  (?P<text>     # save matched chars as `text`,
    .*?         # all chars but lazy,
    (?!\\\1)    # skip escaped char from group 1,
    \1          # matched text must ends with same char as group 1,
  )
)
(?P=text)       # then find again a content of group named 'text'
    """, re.VERBOSE)
    _FORBIDDEN_MACROS = ['PARAM_REF', 'PARAM_FARG', 'AREA_PARAMS_OPCODE']

    def _removeMacros(self):
        clearFormat = ''
        formatStr = self.argumentStrings[self.formatStrPosition]
        for strVal in re.finditer(self.REG_STRING, formatStr):
            clearFormat += strVal.group().removesuffix('"').removeprefix('"')
        self.argumentStrings[self.formatStrPosition] = clearFormat

        if 'PARAM_REF(' in self._funCall:
            varArg = slice(self.formatStrPosition + 1, None)
            self.argumentStrings[varArg] = [
                argS for argS in self.argumentStrings[varArg]
                if all(fm not in argS for fm in self._FORBIDDEN_MACROS)]

    def _getKwargList(self):
        if self.onlyPositional:
            return []

        kwargsArgumentName = self.argumentStrings[self.formatStrPosition + 1]
        matches: list[str] = re.findall(
            rf'{kwargsArgumentName}\s*\[\s*]\s*=\s*{{((?:.|\s)*?)}}',
            self._varDeclarationCode)
        if not matches:
            return []

        # take the latest match and remove whitespaces
        kwargsStr = ''.join(matches[-1].split())
        return [
            kw[1:-1]
            for kw in generateExpressionUntilChar(kwargsStr, 0, ',')
            if kw.startswith('"') and kw.endswith('"')]

    @property
    def _varDeclarationCode(self):
        return self._functionBody[:self._funStart]

    def _getInitialParameterKind(self):
        if self._kwargList:
            return Parameter.POSITIONAL_OR_KEYWORD
        else:
            return Parameter.POSITIONAL_ONLY

    def convertFormatToTypes(self) -> Iterator[Parameter]:
        formatStr = self.argumentStrings[self.formatStrPosition]
        cArgNum = self.realStartArgNum
        pythonArgNum = 0

        try:
            while formatStr:
                for formatSize in range(min(3, len(formatStr)), 0, -1):
                    pythonArgName = None
                    defaultValue = MISSING_DEFAULT_ARG
                    curVal = formatStr[:formatSize]
                    if curVal == 'O!':
                        parseTypeMap['O!'] = self._findPointerType(cArgNum)

                    elif curVal == '(':
                        self._startSequenceParsing()
                        formatStr = formatStr[formatSize:]
                        break

                    elif curVal == ')':
                        parseTypeMap[')'], pythonArgName, defaultValue = self._endSequenceParsing()

                    if objType := parseTypeMap.get(curVal):
                        if pythonArgName is None:
                            pythonArgName = self._getPythonArgName(curVal, cArgNum, pythonArgNum)
                        assert isinstance(pythonArgName, str)

                        if defaultValue is MISSING_DEFAULT_ARG:
                            defaultValue = self._getDefaultValue(curVal, cArgNum)

                        if self._sequenceStack:
                            self._addElementToSequence(objType, pythonArgName, defaultValue)
                        else:

                            if defaultValue is UNKNOWN_DEFAULT_ARG:
                                # replace when we are ready
                                # (after _addElementToSequence will no longer be used)
                                defaultValue = None

                            try:
                                yield AnnotationParam(
                                    pythonArgName, self._parameterKind, default=defaultValue,
                                    annotation=RawRepr(objType))
                            except ValueError:
                                raise
                            pythonArgNum += 1

                        cArgNum += parseSizeMap[curVal]
                        formatStr = formatStr[formatSize:]
                        break
                else:
                    curVal = formatStr[0]
                    if curVal == '|':
                        self._isArgOptional = True
                    elif curVal == '$':
                        self._isArgOptional = True
                        self._parameterKind = Parameter.KEYWORD_ONLY
                    elif curVal in ':;':
                        formatStr = []
                    else:
                        logger.error(f"Unknown format: {formatStr}")
                    formatStr = formatStr[1:]
        except InvalidPointerFormat as ex:
            logger.error(f'{ex}, {formatStr=}, {self._funCall=}, {self.xmlPath=}')

    def _findPointerType(self, cArgNum: int) -> str | None:
        try:
            pointerArg = self.argumentStrings[cArgNum]
        except IndexError:  # some implementations are broken, example:
            # PyObject* BSplineCurve2dPy::insertKnot(PyObject * args)
            # with expectedArg=7, but providedArg=5, code:
            # if (!PyArg_ParseTuple(args, "d|idO!", &U, &M, &tol))
            raise InvalidPointerFormat(f"Function has not enough arguments {self._funCall}")

        if (typ := self._convertPointerToType(pointerArg)) is not None:
            return typ
        elif pointerArg.endswith('::type_object()'):
            logger.debug(f"Cannot detect pointer {pointerArg=}")
        else:
            exc = InvalidPointerFormat(f"Unknown pointer format {pointerArg=}")
            try:
                if self._findPointerType(cArgNum + 1) is not None:
                    exc = InvalidPointerFormat("Format has swapped type")
            except Exception:
                raise exc
            else:
                raise exc

        self.requiredImports.add('typing')
        return 'typing.Any'

    def _convertPointerToType(self, pointerArg: str) -> str | None:
        pointerArg = pointerArg.removeprefix('&').removeprefix('(').removesuffix(')')

        if pointerArg.endswith('::Type'):
            classWithModules = getClassWithModulesFromPointer(pointerArg)
            self.requiredImports.add(getModuleName(classWithModules))
            return classWithModules
        elif pointerArg.startswith('Py'):
            return cTypeToPythonType[pointerArg]
        else:
            logger.error(f"Unknown pointer kind {pointerArg=}")

    def _startSequenceParsing(self):
        self._sequenceStack.append([])

    def _addElementToSequence(self, objType: str, pythonArgName: str, default):
        self._sequenceStack[-1].append(StackVal(objType, pythonArgName, default))

    def _endSequenceParsing(self):
        stackVals = self._sequenceStack.pop()
        # Probably in C this may be a `typing.Sequence`,
        # but at this moment in `typing` only a tuple support variable length.
        objType = f'tuple[{", ".join(s.objType for s in stackVals)}]'

        firstObjName = stackVals[0].pythonArgName
        if all(s.pythonArgName == firstObjName for s in stackVals):
            # if all sub arguments have the same name -> we use it (probably from kwargList)
            objName = firstObjName
        else:
            objName = '_'.join(s.pythonArgName for s in stackVals)

        if all(s.default is UNKNOWN_DEFAULT_ARG for s in stackVals):
            # we cannot decode it
            objDefault = UNKNOWN_DEFAULT_ARG
        elif all(s.default is Parameter.empty for s in stackVals):
            # there is no argument
            objDefault = Parameter.empty
        else:
            content = ['None' if s.default is UNKNOWN_DEFAULT_ARG else repr(s.default)
                       for s in stackVals]
            if len(content) == 1:
                content[0] = f'{content[0]},'
            objDefault = RawStringRepresentation(f'({", ".join(content)})')

        return objType, objName, objDefault

    def _getPythonArgName(self, curFormat: str, cArgNum: int, pythonArgNum: int) -> str:
        if not self.onlyPositional:
            try:
                return self._kwargList[pythonArgNum]
            except IndexError:
                logger.error(f"Too few kw arguments for {curFormat=}, "
                             f"{self._funCall=}, {self.xmlPath=}")

        if cArgName := self._getCurArgName(curFormat, cArgNum):
            # Is this always a unique name?
            return cArgName

        return f'{DEFAULT_ARG_NAME}{self.argNumStart + pythonArgNum}'

    @lru_cache(maxsize=None)
    def _getCurArgName(self, curFormat: str, cArgNum: int) -> str | None:
        if curFormat in ('O!', 'O&') or curFormat.startswith('e'):
            # variable offset - skip type_object/converter/encoding
            cArgNum += 1
        try:
            cArgName = self.argumentStrings[cArgNum]
        except IndexError:
            logger.error(f"Too few arguments for {self._funCall=}, {self.xmlPath=}")
        else:
            if cArgName.isalnum():
                return cArgName

    def _getDefaultValue(self, curFormat: str, cArgNum: int):
        retVal = UNKNOWN_DEFAULT_ARG if self._isArgOptional else Parameter.empty
        if not (cArgName := self._getCurArgName(curFormat, cArgNum)):
            return retVal

        fa = list(re.finditer(
            rf'\b{cArgName}\b\s*=\s*(?P<value>[^;,]*)',
            self._varDeclarationCode))
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


# based on https://pyo3.rs/v0.11.1/conversions.html
typesTableStr = """
Python;Rust;Rust (Python-native)
object;-;&PyAny
str;String, Cow<str>, &str;&PyUnicode
bytes;Vec<u8>, &[u8];&PyBytes
bool;bool;&PyBool
int;Any integer type (i32, u32, usize, etc);&PyLong
float;f32, f64;&PyFloat
complex;num_complex::Complex1;&PyComplex
list[T];Vec<T>;&PyList
dict[K, V];HashMap<K, V>, BTreeMap<K, V>;&PyDict
tuple[T, U];(T, U), Vec<T>;&PyTuple
set[T];HashSet<T>, BTreeSet<T>;&PySet
frozenset[T];HashSet<T>, BTreeSet<T>;&PyFrozenSet
bytearray;Vec<u8>;&PyByteArray
slice;-;&PySlice
type;-;&PyType
module;-;&PyModule
datetime.datetime;-;&PyDateTime
datetime.date;-;&PyDate
datetime.time;-;&PyTime
datetime.tzinfo;-;&PyTzInfo
datetime.timedelta;-;&PyDelta
typing.Optional[T];Option<T>;-
typing.Sequence[T];Vec<T>;&PySequence
typing.Iterator[Any];-;&PyIterator
typing.Type;-;PyClass;this is special case for python2
"""

cTypeToPythonType: dict[str, str] = {
    (pyRustC := line.split(';'))[2]: pyRustC[0]
    for line in typesTableStr.splitlines() if line}
cTypeToPythonType = {
    k.removeprefix('&') + '_Type': v.split('[')[0]
    for k, v in cTypeToPythonType.items()}
# based on https://docs.python.org/3/c-api/arg.html
parseTupleStr = """
s (str) [const char *]
s* (str or bytes-like object) [Py_buffer]
s# (str, read-only bytes-like object) [const char *, int or Py_ssize_t]
z (str or None) [const char *]
z* (str, bytes-like object or None) [Py_buffer]
z# (str, read-only bytes-like object or None) [const char *, int or Py_ssize_t]
y (read-only bytes-like object) [const char *]
y* (bytes-like object) [Py_buffer]
y# (read-only bytes-like object) [const char *, int or Py_ssize_t]
S (bytes) [PyBytesObject *]
Y (bytearray) [PyByteArrayObject *]
u (str) [const Py_UNICODE *]
u# (str) [const Py_UNICODE *, int or Py_ssize_t]
Z (str or None) [const Py_UNICODE *]
Z# (str or None) [const Py_UNICODE *, int or Py_ssize_t]
U (str) [PyObject *]
w* (read-write bytes-like object) [Py_buffer]
es (str) [const char *encoding, char **buffer]
et (str, bytes or bytearray) [const char *encoding, char **buffer]
es# (str) [const char *encoding, char **buffer, int or Py_ssize_t *buffer_length]
et# (str, bytes or bytearray) [const char *encoding, char **buffer, int or Py_ssize_t *buffer_length]
b (int) [unsigned char]
B (int) [unsigned char]
h (int) [short int]
H (int) [unsigned short int]
i (int) [int]
I (int) [unsigned int]
l (int) [long int]
k (int) [unsigned long]
L (int) [long long]
K (int) [unsigned long long]
n (int) [Py_ssize_t]
c (bytes or bytearray of length 1) [char]
C (str of length 1) [int]
f (float) [float]
d (float) [double]
D (complex) [Py_complex]
O (object) [PyObject *]
O! (object) [typeobject, PyObject *]
O& (object) [converter, anything]
p (bool) [int]
( (tuple) []
) (tuple) []
"""
parseTypeMap: dict[str, str] = {
    (keyAndValue := line.split(' ', maxsplit=1))[0]: keyAndValue[1].strip()
    for line in parseTupleStr.splitlines() if line}
parseSizeMap = {k: len(spVal) if (spVal := v.split('[')[1].split(']')[0].split(',')) != [''] else 0
                for k, v in parseTypeMap.items()}
parseTypeMap = {k: v.removeprefix('(').split(' ')[0].removesuffix(')').removesuffix(',')
                for k, v in parseTypeMap.items()}
_autoGenTypeToRealType = {
    'read-only': 'bytes',
    'read-write': 'bytes',
    'bytes-like': 'bytes',
    'object': 'typing.Any',
}
parseTypeMap = {k: _autoGenTypeToRealType.get(v, v) for k, v in parseTypeMap.items()}
