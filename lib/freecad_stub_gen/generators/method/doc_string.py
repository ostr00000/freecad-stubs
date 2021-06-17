import keyword
import re
from itertools import count
from typing import Generator, Iterator

from freecad_stub_gen.generators.method.function_finder import generateExpressionUntilChar, \
    findFunctionCall
from freecad_stub_gen.generators.method.types_converter import Arg
from freecad_stub_gen.generators.names import validatePythonValue


def generateArgSuitFromDocstring(name: str, docString: str, argNumStart: int = 0):
    for match in re.finditer(fr'{name}\((.*?)\):?', docString):
        funStart, _funEnd = match.span()
        funCall = findFunctionCall(docString, funStart, bracketL='(', bracketR=')')
        funCall = funCall.removeprefix(name).removeprefix('(').removesuffix(')')
        yield list(_argSuiteGen(funCall, argNumStart))


def _argSuiteGen(funDocString: str, argNumStart: int) -> Iterator[Arg]:
    uniqueNameGen = _uniqueArgNameGen(argNumStart)
    next(uniqueNameGen)

    for argText in generateExpressionUntilChar(funDocString, 0, ','):
        argText = argText.strip()
        if argText == '':
            return
        elif argText[-2:] == '[]':
            pass
        else:
            argText = argText.removeprefix('[').removesuffix(']')

        if '=' in argText:
            argName, defValue = argText.split('=')
            argName, defValue = argName.strip(), defValue.strip()
            defValue = validatePythonValue(defValue)
        else:
            argName, defValue = argText, None
        uniqueName, argNum = uniqueNameGen.send(argName)
        yield Arg(argNum, '', defValue is not None, uniqueName, defValue)


REG_ALL_EXCEPT_WORLD = re.compile(r'\W+')
REG_START_WITH_LETTER = re.compile(r'[a-zA-Z].*')


def _uniqueArgNameGen(argNumStart: int = 1) -> Generator[tuple[str, int], str, None]:
    name: str = yield
    seen = set()

    for argNum in count(argNumStart):
        name = re.sub(REG_ALL_EXCEPT_WORLD, '_', name)
        if not re.match(REG_START_WITH_LETTER, name):
            name = 'arg'
        elif keyword.iskeyword(name):
            name += '_'

        if name in seen:
            name = f'{name}{argNum}'
        else:
            seen.add(name)
        name = yield name, argNum
