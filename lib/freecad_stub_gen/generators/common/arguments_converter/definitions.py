import re

DEFAULT_ARG_NAME = 'arg'
MISSING_DEFAULT_ARG = object()
UNKNOWN_DEFAULT_ARG = object()

# based on https://pyo3.rs/v0.11.1/conversions.html
_TYPES_TABLE_STR = """
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

C_TYPE_TO_PYTHON_TYPE: dict[str, str] = {
    (pyRustC := line.split(';'))[2]: pyRustC[0]
    for line in _TYPES_TABLE_STR.splitlines()
    if line
}
C_TYPE_TO_PYTHON_TYPE = {
    k.removeprefix('&') + '_Type': v.split('[')[0]
    for k, v in C_TYPE_TO_PYTHON_TYPE.items()
}
# based on https://docs.python.org/3/c-api/arg.html
C_API_TYPES_STR = """
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
et# (str, bytes or bytearray) [const char *encoding, char **buffer, int *buffer_length]
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


def _initParseMaps():
    cApiLineReg = re.compile(
        r"""
        (?P<key>\S+)        # API symbol
        \s+\(
        (?P<rawPythonType>\w+) # we take only first type
        [^)]*               # remaining types
        \)\s+\[
        (?P<cppTypes>[^]]*) # all between []
        ].*                 # ignore rest of the line
        """,
        re.VERBOSE,
    )
    rawPythonTypeToPythonType = {
        'read': 'bytes',
        'read-only': 'bytes',
        'read-write': 'bytes',
        'bytes-like': 'bytes',
        'object': 'typing.Any',
    }
    locParseSizeMap = {}
    locParseTypeMap = {}

    for line in C_API_TYPES_STR.splitlines():
        if not line:
            continue
        if not (m := cApiLineReg.match(line)):
            raise ValueError

        key = m.group('key')
        rawPythonType = m.group('rawPythonType')
        cppTypes = m.group('cppTypes')

        cppSize = len(cppTypes.split(',')) if cppTypes else 0
        fixedPythonType = rawPythonTypeToPythonType.get(rawPythonType, rawPythonType)

        locParseSizeMap[key] = cppSize
        locParseTypeMap[key] = fixedPythonType

    return locParseSizeMap, locParseTypeMap


parseSizeMap, parseTypeMap = _initParseMaps()
