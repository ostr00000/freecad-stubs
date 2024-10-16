import contextlib
import contextvars
from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.file_functions import readContent
from freecad_stub_gen.ordered_set import OrderedStrSet

currentPath = contextvars.ContextVar[Path]('currentPath')
"""Path to currently processed file."""

implementationPath = contextvars.ContextVar[Path]('implementationPath')
"""Path to implementation file (may be same as `currentPath`)."""

currentSource = contextvars.ContextVar[str]('currentSource')
"""Text from currently processed file."""

requiredImports = contextvars.ContextVar[OrderedStrSet]('requiredImports')
"""All imports required in current stub file."""

allContextVars: list[contextvars.ContextVar] = [
    currentPath,
    implementationPath,
    currentSource,
    requiredImports,
]


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
    match filePath.suffix:
        case '.cpp' | '.xml':
            for implSuffix in ('Imp', 'Impl'):
                impPath = filePath.with_stem(filePath.stem + implSuffix).with_suffix(
                    '.cpp'
                )
                if impPath.exists():
                    break
            else:
                impPath = filePath
        case _:
            impPath = filePath

    currentPath.set(filePath)
    implementationPath.set(impPath)
    currentSource.set(readContent(impPath))
    requiredImports.set(OrderedStrSet())


@contextlib.contextmanager
def isolatedContext(filePath: Path | None = None):
    oldContext = [c.get(None) for c in allContextVars]
    try:
        if filePath is not None:
            initContext(filePath)
        yield
    finally:
        for c, v in zip(allContextVars, oldContext, strict=True):
            c.set(v)


def getCurrentNamespace():
    parts = currentPath.get().relative_to(SOURCE_DIR).parts
    try:
        index = parts.index('Mod')
        namespace = parts[index + 1]
    except ValueError:
        for k in ('App', 'Base', 'Gui'):
            if k in parts:
                namespace = k
                break
        else:
            # maybe some external module? we are not interested
            namespace = '.'.join(parts[:-1])

    return namespace


def isGuiInNamespace() -> bool:
    return 'Gui' in currentPath.get().relative_to(SOURCE_DIR).parts
