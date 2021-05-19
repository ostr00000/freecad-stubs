import dataclasses
import logging
import re
import xml.etree.ElementTree as ET
from typing import Iterator, Optional, Any

from freecad_stub_gen.generators.method.function_finder import generateExpressionUntilChar
from freecad_stub_gen.generators.names import genBaseClasses, genTypeForStem
from freecad_stub_gen.module_map import moduleNamespace

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Arg:
    order: int
    type: str
    default: bool
    name: str = None
    value: Any = None

    def __str__(self):
        argName = self.name or f'arg{self.order}'
        ret = argName
        if self.type:
            ret += f': {self.type}'
        if self.default:
            argValue = self.value or 'None'
            ret += f' = {argValue}'
        return ret


class PositionalOnlyArg(Arg):
    def __str__(self):
        return '/'


class KeyWorldOnlyArg(Arg):
    def __str__(self):
        return '*'


class InvalidPointerFormat(ValueError):
    pass


class TypesConverter:
    REG_REMOVE_WHITESPACES = re.compile(r'\s+')

    def __init__(self, funCall: str, currentNode: ET.Element, requiredImports: set[str],
                 onlyPositional: bool, formatStrPosition: int, startArgNum=1, xmlPath=None,
                 realStartArgNum: int = 2):
        self.funCall = funCall
        self.currentNode = currentNode
        self.requiredImports = requiredImports
        self.onlyPositional = onlyPositional
        self.formatStrPosition = formatStrPosition
        self.startArgNum = startArgNum
        self.realStartArgNum = realStartArgNum
        self.xmlPath = xmlPath

        sub = re.sub(self.REG_REMOVE_WHITESPACES, '', funCall)  # remove whitespace
        self.argumentStrings = list(generateExpressionUntilChar(sub, sub.find('(') + 1, ','))
        self._removeMacros()

    REG_STRING = re.compile(r"""(["'])(?=(?P<text>.*?(?!\\\1)\1))(?P=text)""")
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

    def convertFormatToTypes(self) -> Iterator[Arg]:
        formatStr = self.argumentStrings[self.formatStrPosition]
        realArgNum = self.realStartArgNum
        argNum = 0
        optional = False

        try:
            while formatStr:
                for size in range(3, 0, -1):
                    curVal = formatStr[:size]
                    if curVal == 'O!':
                        parseTupleMap['O!'] = self._findPointerType(realArgNum)

                    if objType := parseTupleMap.get(curVal):
                        yield Arg(self.startArgNum + argNum, objType, optional)
                        argNum += 1
                        realArgNum += parseSizeMap[curVal]
                        formatStr = formatStr[size:]
                        break
                else:
                    curVal = formatStr[0]
                    if curVal == '|':
                        optional = True
                    elif curVal == '$':
                        yield KeyWorldOnlyArg(-1, '', default=False)
                    elif curVal in ':;':
                        formatStr = []
                    else:
                        logger.error(f"Unknown format: {formatStr}")
                    formatStr = formatStr[1:]
        except InvalidPointerFormat as ex:
            logger.error(f'{ex}, {formatStr=}, {self.funCall=}, {self.xmlPath=}')

        if self.onlyPositional and argNum != 0:
            yield PositionalOnlyArg(-1, '', default=False)

    def _findPointerType(self, realArgNum: int) -> Optional[str]:
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
                    exc = InvalidPointerFormat(f"Format has swapped type ")
            except Exception:
                pass
            raise exc

        return 'object'

    def _convertPointerToType(self, pointerArg: str) -> Optional[str]:
        pointerArg = pointerArg.removeprefix('&').removeprefix('(').removesuffix(')')

        if pointerArg.endswith('::Type'):
            return self._convertCustomClass(pointerArg)
        elif pointerArg.startswith('Py'):
            return cTypeToPythonType[pointerArg]
        else:
            logger.error(f"Unknown pointer kind {pointerArg=}")

    def _convertCustomClass(self, pointerArg: str) -> Optional[str]:
        pTypePy = pointerArg.removesuffix('::Type')
        if '::' in pTypePy:
            namespace, pTypePy = pTypePy.split('::')

        fullTypeName = genTypeForStem(pTypePy)
        module = fullTypeName[:fullTypeName.rfind('.')]
        self.requiredImports.add(module)
        return fullTypeName


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
parseTupleMap: dict[str, str] = {
    (keyAndValue := line.split(' ', maxsplit=1))[0]: keyAndValue[1]
    for line in parseTupleStr.splitlines() if line}
parseSizeMap = {k: len(v.split('[')[1].split(',')) for k, v in parseTupleMap.items()}
parseTupleMap = {k: v.removeprefix('(').split(' ')[0].removesuffix(')').removesuffix(',')
                 for k, v in parseTupleMap.items()}
_autoGenTypeToRealType = {'read-only': 'bytes', 'read-write': 'bytes', 'bytes-like': 'bytes'}
parseTupleMap = {k: _autoGenTypeToRealType.get(v, v) for k, v in parseTupleMap.items()}
