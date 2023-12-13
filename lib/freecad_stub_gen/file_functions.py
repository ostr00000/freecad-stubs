from collections.abc import Iterable
from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.cpp_code.converters import removeComments
from freecad_stub_gen.debug_functions import logProgress


def readContent(file: Path):
    try:
        content = file.read_text('iso8859-1')
    except UnicodeDecodeError:
        content = file.read_text('utf-8')

    return removeComments(content)


def genCppFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).rglob('*.cpp')


def genHFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).rglob('*.h')


def _genFilesToPreprocess(sourcePath: Path = SOURCE_DIR):
    yield from genHFiles(sourcePath)
    yield from genCppFiles(sourcePath)


def genFilesToPreprocess(sourcePath: Path = SOURCE_DIR, **kwargs) -> Iterable[Path]:
    total = sum(1 for _ in _genFilesToPreprocess(sourcePath))
    yield from logProgress(_genFilesToPreprocess(sourcePath), total, **kwargs)


def genIiFiles(sourcePath: Path = SOURCE_DIR):
    """Generate preprocessed (intermediate) files."""
    yield from Path(sourcePath).rglob('*.ii')


def genXmlFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).rglob('*.xml')
