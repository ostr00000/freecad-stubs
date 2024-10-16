from pathlib import Path
from xml.etree import ElementTree

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.cpp_code.converters import removeComments

ENCODING = 'iso8859-1'


def readContent(file: Path):
    try:
        content = file.read_text(ENCODING)
    except UnicodeDecodeError:
        content = file.read_text('utf-8')

    return removeComments(content)


def genCppFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).rglob('*.cpp')


def genHFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).rglob('*.h')


def genFilesToPreprocess(sourcePath: Path = SOURCE_DIR):
    yield from genHFiles(sourcePath)
    yield from genCppFiles(sourcePath)


def genIiFiles(sourcePath: Path = SOURCE_DIR):
    """Generate preprocessed (intermediate) files."""
    yield from Path(sourcePath).rglob('*.ii')


def genCppIiFiles(sourcePath: Path = SOURCE_DIR):
    """Generate preprocessed (intermediate) files with inlined headers."""
    yield from Path(sourcePath).rglob('*.cpp.ii')


def genHIiFiles(sourcePath: Path = SOURCE_DIR):
    """Generate preprocessed (intermediate) files with inlined headers."""
    yield from Path(sourcePath).rglob('*.h.ii')


def genXmlFiles(sourcePath: Path = SOURCE_DIR):
    if sourcePath != SOURCE_DIR:
        yield from Path(sourcePath).rglob('*.xml')
        return

    for searchDirName in ('App', 'Base', 'Gui', 'Mod'):
        yield from (sourcePath / searchDirName).rglob('*Py.xml')


def parseXml(file: Path) -> ElementTree.ElementTree:
    try:
        return ElementTree.parse(file)
    except ElementTree.ParseError as e:
        e.add_note(f"Parsing {file=}")
        raise
