from collections.abc import Iterable
from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.cpp_code.converters import removeComments


def readContent(file: Path):
    try:
        content = file.read_text('iso8859-1')
    except UnicodeDecodeError:
        content = file.read_text('utf-8')

    return removeComments(content)


def _excludeIiFiles(it: Iterable[Path]):
    for p in it:
        if p.name.endswith(('.cpp.ii', '.h.ii')):
            continue
        yield p


def genCppFiles(sourcePath: Path = SOURCE_DIR):
    yield from _excludeIiFiles(Path(sourcePath).rglob('*.cpp'))


def genHFiles(sourcePath: Path = SOURCE_DIR):
    yield from _excludeIiFiles(Path(sourcePath).rglob('*.h'))


def genFilesToPreprocess(sourcePath: Path = SOURCE_DIR):
    yield from genHFiles(sourcePath)
    yield from genCppFiles(sourcePath)


def genIiFiles(sourcePath: Path = SOURCE_DIR):
    """Generate preprocessed (intermediate) files."""
    yield from Path(sourcePath).rglob('*.ii')


def genIiCppFiles(sourcePath: Path = SOURCE_DIR):
    """Generate preprocessed (intermediate) files with inlined headers."""
    yield from Path(sourcePath).rglob('*.ii.cpp')


def genXmlFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).rglob('*.xml')
