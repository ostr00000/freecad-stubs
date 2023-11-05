from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.cpp_code.converters import removeComments


def readContent(file: Path):
    try:
        content = file.read_text('utf-8')
    except UnicodeDecodeError:
        content = file.read_text('iso8859-1')

    return removeComments(content)


def genCppFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).glob('**/*.cpp')


def genXmlFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).glob('**/*.xml')
