import logging
import re
from collections.abc import Iterator
from inspect import Parameter

from freecad_stub_gen.generators.common.annotation_parameter import AnnotationParam, RawRepr
from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar
from freecad_stub_gen.generators.common.names import getClassWithModulesFromPointer, getModuleName

logger = logging.getLogger(__name__)

DEFAULT_ARG_NAME = 'arg'


class InvalidPointerFormat(ValueError):
    pass


class TypesConverter:
    REG_REMOVE_WHITESPACES = re.compile(r'\s+')

    def __init__(self, funCall: str, requiredImports: set[str],
                 onlyPositional: bool, formatStrPosition: int, *,
                 argNumStart=1, realStartArgNum: int = 2, xmlPath=None):
        self.funCall = funCall
        self.requiredImports = requiredImports
        self.onlyPositional = onlyPositional
        self.formatStrPosition = formatStrPosition
        self.argNumStart = argNumStart
        self.realStartArgNum = realStartArgNum
        self.xmlPath = xmlPath

        sub = re.sub(self.REG_REMOVE_WHITESPACES, '', funCall)  # remove whitespace
        self.argumentStrings = list(generateExpressionUntilChar(sub, sub.find('(') + 1, ','))
        self._removeMacros()

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

        if 'PARAM_REF(' in self.funCall:
            varArg = slice(self.formatStrPosition + 1, None)
            self.argumentStrings[varArg] = [
                argS for argS in self.argumentStrings[varArg]
                if all(fm not in argS for fm in self._FORBIDDEN_MACROS)]

    def convertFormatToTypes(self, kwargList: list[str]) -> Iterator[Parameter]:
        formatStr = self.argumentStrings[self.formatStrPosition]
        realArgNum = self.realStartArgNum
        argNum = 0

        default = Parameter.empty
        if kwargList:
            parameterKind = Parameter.POSITIONAL_OR_KEYWORD
        else:
            parameterKind = Parameter.POSITIONAL_ONLY

        try:
            while formatStr:
                for formatSize in range(3, 0, -1):
                    curVal = formatStr[:formatSize]
                    if curVal == 'O!':
                        parseTypeMap['O!'] = self._findPointerType(realArgNum)

                    elif curVal == '(':
                        parseSizeMap['('], parseTypeMap['('], formatSize = \
                            self._parseSequence(formatStr)

                    if objType := parseTypeMap.get(curVal):
                        name = self._getArgName(formatStr, kwargList, argNum)
                        yield AnnotationParam(
                            name, parameterKind, default=default,
                            annotation=RawRepr(objType))

                        argNum += 1
                        realArgNum += parseSizeMap[curVal]
                        formatStr = formatStr[formatSize:]
                        break
                else:
                    curVal = formatStr[0]
                    if curVal == '|':
                        default = None
                    elif curVal == '$':
                        parameterKind = Parameter.KEYWORD_ONLY
                    elif curVal in ':;':
                        formatStr = []
                    else:
                        logger.error(f"Unknown format: {formatStr}")
                    formatStr = formatStr[1:]
        except InvalidPointerFormat as ex:
            logger.error(f'{ex}, {formatStr=}, {self.funCall=}, {self.xmlPath=}')

    def _findPointerType(self, realArgNum: int) -> str | None:
        try:
            pointerArg = self.argumentStrings[realArgNum]
        except IndexError:  # some implementations are broken, example:
            # PyObject* BSplineCurve2dPy::insertKnot(PyObject * args)
            # with expectedArg=7, but providedArg=5, code:
            # if (!PyArg_ParseTuple(args, "d|idO!", &U, &M, &tol))
            raise InvalidPointerFormat(f"Function has not enough arguments {self.funCall}")

        if pointerArg[0] == '&':
            if (typ := self._convertPointerToType(pointerArg[1:])) is not None:
                return typ
        elif pointerArg.endswith('::type_object()'):
            logger.debug(f"Cannot detect pointer {pointerArg=}")
        else:
            exc = InvalidPointerFormat(f"Unknown pointer format {pointerArg=}")
            try:
                if self._findPointerType(realArgNum + 1) is not None:
                    exc = InvalidPointerFormat("Format has swapped type")
            except Exception:
                pass
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

    def _parseSequence(self, sequence: str) -> tuple[int, str, int]:
        """:return realArguments, type, skipSize"""
        self.requiredImports.add('typing')
        if sequence.startswith(f := '(s)'):
            return len(f) - 2, 'typing.Sequence[str]', len(f)
        elif sequence.startswith(f := '(fff)'):
            return len(f) - 2, 'typing.Sequence[float, float, float]', len(f)

        # there are only two known cases, too much work to automate this
        raise NotImplementedError

    def _getArgName(self, formatStr: str, kwargList: list[str], argNum: int) -> str | None:
        if not self.onlyPositional:
            try:
                return kwargList[argNum]
            except IndexError:
                logger.error(
                    f"Too few kw arguments for {formatStr=}, {self.funCall=}, {self.xmlPath=}")
        return f'{DEFAULT_ARG_NAME}{self.argNumStart + argNum}'


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
"""
parseTypeMap: dict[str, str] = {
    (keyAndValue := line.split(' ', maxsplit=1))[0]: keyAndValue[1]
    for line in parseTupleStr.splitlines() if line}
parseSizeMap = {k: len(v.split('[')[1].split(',')) for k, v in parseTypeMap.items()}
parseTypeMap = {k: v.removeprefix('(').split(' ')[0].removesuffix(')').removesuffix(',')
                for k, v in parseTypeMap.items()}
_autoGenTypeToRealType = {
    'read-only': 'bytes',
    'read-write': 'bytes',
    'bytes-like': 'bytes',
    'object': 'typing.Any',
}
parseTypeMap = {k: _autoGenTypeToRealType.get(v, v) for k, v in parseTypeMap.items()}
