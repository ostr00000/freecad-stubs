import json
import shlex
import subprocess
from dataclasses import dataclass
from functools import cache
from pathlib import Path


@cache
def getClangStandardIncludes() -> list[Path]:
    """Return clang standard includes.

    This is similar to:
    > clang -E -v - < /dev/null 2>&1 | grep "^ /\
    """
    out = subprocess.check_output(  # noqa: S603
        ['/usr/bin/clang', '-E', '-v', '-'],
        text=True,
        stderr=subprocess.STDOUT,
        input='',
    )
    includes = []
    for rawLine in out.splitlines():
        line = rawLine.strip()
        if line.startswith('/'):
            includes.append(Path(line).resolve())

    return includes


@dataclass
class CompileEntry:
    directory: Path
    file: Path
    output: Path
    command: str

    def __post_init__(self):
        self.directory = Path(self.directory)
        self.file = Path(self.file)
        self.output = Path(self.output)

    @property
    def _commandList(self) -> list[str]:
        return shlex.split(self.command)

    @property
    def commandArgs(self) -> list[str]:
        # Example `command` attribute:
        # '/usr/bin/clang++
        # -DBOOST_ATOMIC_DYN_LINK
        # -DCMAKE_BUILD_TYPE=\\"Debug\\"
        # -D_OCC64
        # -I/workspaces/freecad_typing/FreeCAD/build/debug/src/Gui/FreeCADGui_autogen/include # noqa: E501,ERA001
        # -I/workspaces/freecad_typing/FreeCAD/src/Gui/..
        # -I/usr/include/eigen3
        # -I/workspaces/freecad_typing/FreeCAD/build/debug/_deps/fmt-src/include
        # -isystem /usr/include/python3.11
        # -Wall -Wextra -Wpedantic -Wno-write-strings
        # -g -DFC_DEBUG -std=gnu++17 -fPIC
        # -o CMakeFiles/FreeCADGui.dir/ApplicationPy.cpp.o
        # -c /workspaces/freecad_typing/FreeCAD/src/Gui/ApplicationPy.cpp'
        allowedFlags = ('-I', '-i', '-D', '-W', '-std')
        pairArguments = ('-isystem',)

        resultArgs = []
        resultArgs.extend(f'-I{p}' for p in getClangStandardIncludes())
        commandIt = iter(self._commandList)
        for ca in commandIt:
            if not ca.startswith(allowedFlags):
                continue

            if ca in pairArguments:
                resultArgs.append(ca)
                resultArgs.append(next(commandIt))
                continue

            resultArgs.append(ca)

        return resultArgs


def getCompileEntries(compileCommandsPath: Path) -> list[CompileEntry]:
    with compileCommandsPath.open() as file:
        data = json.load(file)

    return [CompileEntry(**entry) for entry in data]
