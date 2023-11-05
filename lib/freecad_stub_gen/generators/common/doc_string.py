import keyword
import re
from collections.abc import Iterator
from inspect import Parameter, _ParameterKind, _empty
from itertools import count
from typing import Generator
from xml.etree import ElementTree as ET

from freecad_stub_gen.generators.common.annotation_parameter import AnnotationParam, RawRepr, \
    SelfSignature
from freecad_stub_gen.generators.common.arguments_converter.definitions import DEFAULT_ARG_NAME
from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.cpp_code.converters import validatePythonValue


def generateSignaturesFromDocstring(name: str, docString: str, argNumStart: int = 0):
    for match in re.finditer(fr'{name}\((.*?)\):?', docString):
        funCall = findFunctionCall(docString, match.start(), bracketL='(', bracketR=')')
        funCall = funCall.removeprefix(name).removeprefix('(')
        if funCall.endswith(')'):
            funCall = funCall.removesuffix(')')
        else:
            # missed ending bracket
            funCall = funCall.split('\n', maxsplit=1)[0]

        yield SelfSignature(list(_signatureGen(funCall, argNumStart)))


def _signatureGen(funDocString: str, argNumStart: int) -> Iterator[Parameter]:
    if not funDocString:
        return

    uniqueNameGen = _uniqueArgNameGen(argNumStart)
    try:
        next(uniqueNameGen)
    except StopIteration as exc:
        raise ValueError("Unique generator should never end") from exc

    paramType: _ParameterKind = Parameter.POSITIONAL_ONLY

    for argText in generateExpressionUntilChar(funDocString, 0, ','):
        argText = argText.strip()
        annotation: type[_empty] | str = Parameter.empty

        if argText[-2:] == '[]':
            argText = argText[:-2] + 'None'
            annotation = 'list'

        if argText.startswith('[') and argText.endswith(']'):
            paramType = Parameter.POSITIONAL_OR_KEYWORD

        argText = argText.removeprefix('[').removesuffix(']')

        if '=' in argText:
            argName, defValue = argText.split('=')
            argName, defValue = argName.strip(), defValue.strip()
            defValue = validatePythonValue(defValue)
        elif argText == '...':
            yield AnnotationParam.ARGS_PARAM
            paramType = Parameter.KEYWORD_ONLY
            continue

        else:
            argName, defValue = argText, Parameter.empty

        if defValue is Parameter.empty and paramType != Parameter.POSITIONAL_ONLY:
            defValue = None
        if defValue is not Parameter.empty and paramType == Parameter.POSITIONAL_ONLY:
            paramType = Parameter.POSITIONAL_OR_KEYWORD

        uniqueName, _argNum = uniqueNameGen.send(argName)
        yield AnnotationParam(
            uniqueName, paramType, default=RawRepr(defValue), annotation=RawRepr(annotation))


REG_ALL_EXCEPT_WORLD = re.compile(r'\W+')
REG_START_WITH_LETTER = re.compile(r'[a-zA-Z].*')


def _uniqueArgNameGen(argNumStart: int = 1) -> Generator[tuple[str, int], str, None]:
    name: str = yield '', 0
    seen = set()

    for argNum in count(argNumStart):
        name = re.sub(REG_ALL_EXCEPT_WORLD, '_', name)
        if not re.match(REG_START_WITH_LETTER, name):
            name = f'{DEFAULT_ARG_NAME}{argNum}'
        elif keyword.iskeyword(name):
            name += '_'

        if name in seen:
            name = f'{name}{argNum}'

        seen.add(name)
        name = yield name, argNum


_REG_REMOVE_NEW_LINE = re.compile(r'\\n"\s*"')
_REG_WHITESPACE_WITH_APOSTROPHE = re.compile(r'"\s*"')


def prepareDocs(docs: str) -> str:
    docs = _REG_REMOVE_NEW_LINE.sub('\n', docs)
    docs = _REG_WHITESPACE_WITH_APOSTROPHE.sub('', docs)
    docs = docs.replace('\\n', '\n').replace('\\"', '"')

    docs = docs.strip()
    if docs.count('\n'):
        if not docs.startswith('\n'):
            docs = '\n' + docs
        if not docs.endswith('\n'):
            docs = docs + '\n'

    return docs


def formatDocstring(docs: str):
    if preparedDocs := prepareDocs(docs):
        return f'"""{preparedDocs}"""\n'
    return ''


def getDocFromNode(node: ET.Element) -> str:
    # https://youtrack.jetbrains.com/issue/PY-49523/default-argument-for-xml-Element.findtext-is-incorrectly-identified-as-the-wrong-type
    # noinspection PyTypeChecker
    return node.findtext('./Documentation//UserDocu', default='')
