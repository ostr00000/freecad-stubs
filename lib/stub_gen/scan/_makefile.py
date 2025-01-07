import io
from collections.abc import Iterable
from contextlib import redirect_stdout
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, TypedDict

from mkparse.mkparse import Parser as MakefileParser


class MakefileTarget(TypedDict):
    dependencies: list[str]
    statements: list[str]


class MakefileVariable(TypedDict):
    operator: Literal['=', '?=', ':=']
    value: list[str]


@dataclass
class ParsedMakefile:
    targets: dict[str, MakefileTarget]
    variables: dict[str, MakefileVariable]
    comments: dict[int, str]


def getMakefileArgs(makefile: Path) -> ParsedMakefile:
    """Get makefile arguments.

    https://github.com/Thanatisia/makefile-parser-python#installing
    NOTE: use strict hash version in dependency.
    """
    mp = MakefileParser(makefile.name, str(makefile.parent))

    with io.StringIO() as out, redirect_stdout(out):
        rawResult = mp.parse_makefile(mp.makefile_name, mp.makefile_path)
        if val := out.getvalue():
            raise ValueError(val)

        match rawResult:
            case [targets, variables, comments]:
                pm = ParsedMakefile(targets, variables, comments)
            case _:
                msg = f"Unexpected parse result: {rawResult}"
                raise ValueError(msg)

    return pm


def genClangArguments(pm: ParsedMakefile) -> Iterable[str]:
    for argName in ('CXX_DEFINES', 'CXX_INCLUDES', 'CXX_FLAGS'):
        if not (variable := pm.variables.get(argName)):
            continue

        if not (values := variable.get('value')):
            continue

        yield from values
