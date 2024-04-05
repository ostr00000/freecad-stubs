import contextlib
import contextvars
from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.file_functions import readContent
from freecad_stub_gen.ordered_set import OrderedStrSet

currentPath = contextvars.ContextVar[Path]('currentPath')
"""Path to currently processed file."""

currentSource = contextvars.ContextVar[str]('currentSource')
"""Text from currently processed file."""

requiredImports = contextvars.ContextVar[OrderedStrSet]('requiredImports')
"""All imports required in current stub file."""


@contextlib.contextmanager
def newImportContext():
    oldImports = requiredImports.get()
    newImports = type(oldImports)()
    requiredImports.set(newImports)
    try:
        yield newImports
    finally:
        requiredImports.set(oldImports)


def initContext(filePath: Path):
    for implSuffix in ('Imp', 'Impl'):
        impPath = filePath.with_stem(filePath.stem + implSuffix).with_suffix('.cpp')
        if impPath.exists():
            break
    else:
        # special case for PyObjectBase
        impPath = filePath.with_suffix('.cpp')

    currentPath.set(filePath)
    currentSource.set(readContent(impPath))
    requiredImports.set(OrderedStrSet())


def getCurrentNamespace():
    parts = currentPath.get().relative_to(SOURCE_DIR).parts
    try:
        index = parts.index('Mod')
        namespace = parts[index + 1]
    except ValueError as exc:
        for k in ('App', 'Base', 'Gui'):
            if k in parts:
                namespace = k
                break
        else:
            raise ValueError from exc

    return namespace
