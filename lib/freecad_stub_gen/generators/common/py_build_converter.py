from functools import lru_cache

from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar


@lru_cache()
def parsePyBuildValues(formatText: str) -> str:
    formatText = formatText.replace(' ', '')
    results = []
    while formatText:
        if formatText[0] in '([{':
            singleResult, size = _parsePyBuildComplexValue(formatText)
        else:
            for formatSize in range(2, 0, -1):
                singleFormat = formatText[:formatSize]
                if singleResult := parseTypeMap.get(singleFormat):
                    size = formatSize
                    break
            else:
                raise ValueError("Unknown format sting", formatText)

        formatText = formatText[size:]
        results.append(singleResult)

    if len(results) > 1:
        return f'tuple[{", ".join(results)}]'
    elif results:
        return results[0]
    else:
        return 'None'


@lru_cache()
def _parsePyBuildComplexValue(formatText: str) -> tuple[str | None, int]:
    firstChar = formatText[0]
    lastChar = {'(': ')', '[': ']', '{': '}'}[firstChar]

    subValueFormatText = findFunctionCall(
        formatText, bodyStart=0, bracketL=firstChar, bracketR=lastChar
    ).removeprefix(firstChar).removesuffix(lastChar)
    complexFormats = list(generateExpressionUntilChar(
        subValueFormatText, expStart=0, splitChar=',',
        bracketL='([{', bracketR=')]}'))

    if firstChar == '{':
        result = _parsePyBuildDict(complexFormats)
    elif firstChar == '[':
        result = _parsePyBuildList(complexFormats)
    elif firstChar == '(':
        result = _parsePyBuildTuple(complexFormats)
    else:
        raise ValueError

    return result, len(subValueFormatText) + 2


def _parsePyBuildDict(complexFormats: list[str]):
    keys = set()
    values = set()
    for cf in complexFormats:
        key, val = cf.split(':', maxsplit=1)
        keys.add(parsePyBuildValues(key))
        values.add(parsePyBuildValues(val))
    result = f'dict[{" | ".join(keys)}, {" | ".join(values)}]'
    return result


def _parsePyBuildList(complexFormats: list[str]):
    values = set()
    for cf in complexFormats:
        values.add(parsePyBuildValues(cf))
    result = f'list[{" | ".join(values)}]'
    return result


def _parsePyBuildTuple(complexFormats: list[str]):
    if len(complexFormats) == 1:
        if complexFormats[0]:
            result = parsePyBuildValues(complexFormats[0])
            if not result.startswith('tuple['):
                result = f'tuple[{result}]'
        else:
            result = 'tuple[()]'
    else:
        values = []
        for cf in complexFormats:
            values.append(parsePyBuildValues(cf))
        result = f'tuple[{", ".join(values)}]'
    return result


# https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue
# https://docs.python.org/3/extending/extending.html#building-arbitrary-values
pyBuildValues = """
s (str or None) [const char *]
s# (str or None) [const char *, Py_ssize_t]
y (bytes) [const char *]
y# (bytes) [const char *, Py_ssize_t]
z (str or None) [const char *]
z# (str or None) [const char *, Py_ssize_t]
u (str) [const wchar_t *]
u# (str) [const wchar_t *, Py_ssize_t]
U (str or None) [const char *]
U# (str or None) [const char *, Py_ssize_t]
i (int) [int]
b (int) [char]
h (int) [short int]
l (int) [long int]
B (int) [unsigned char]
H (int) [unsigned short int]
I (int) [unsigned int]
k (int) [unsigned long]
L (int) [long long]
K (int) [unsigned long long]
n (int) [Py_ssize_t]
c (bytes of length 1) [char]
C (str of length 1) [int]
d (float) [double]
f (float) [float]
D (complex) [Py_complex *]
O (object) [PyObject *]
S (object) [PyObject *]
N (object) [PyObject *]
O& (object) [converter, anything]
(items) (tuple) [matching-items]
[items] (list) [matching-items]
{items} (dict) [matching-items]
"""
parseTypeMap = {
    (keyAndValue := line.split(' ', maxsplit=1))[0]: keyAndValue[1]
    for line in pyBuildValues.splitlines() if line}
parseSizeMap = {k: len(v.split('[')[1].split(',')) for k, v in parseTypeMap.items()}
parseTypeMap = {k: v.removeprefix('(').split(' ')[0].removesuffix(')').removesuffix(',')
                for k, v in parseTypeMap.items()}

if __name__ == '__main__':
    def testParsing():
        for i in (
                "",
                "i",
                "iii",
                "s",
                "y",
                "ss",
                "s#",
                "y#",
                "()",
                "(i)",
                "(ii)",
                "(i,i)",
                "[i,i]",
                "{s:i,s:i}",
                "((ii)(ii)) (ii)",
        ):
            print(parsePyBuildValues(i))

    testParsing()
