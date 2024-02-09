import io
import logging
import re
from pathlib import Path
from typing import TextIO

from pcpp import Preprocessor

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.decorators import logCurrentTaskDecFactory
from freecad_stub_gen.file_functions import ENCODING

logger = logging.getLogger(__name__)


def getContentForOriginalFile(fileName: str, fp: TextIO) -> str:
    """Based on `cxxheaderparser.preprocessor:_pcpp_filter`.

    the output of pcpp includes the contents of all the included files, which
    isn't what a typical user of cxxheaderparser would want, so we strip out
    the line directives and any content that isn't in our original file
    """
    lineEnding = f'{fileName}"\n'
    newOutput = io.StringIO()
    keep = True
    for line in fp:
        if line.startswith("#line"):
            keep = line.endswith(lineEnding)

        if keep:
            newOutput.write(line)

    return newOutput.getvalue()


def fixPath(pp: Preprocessor, filename: Path) -> Path:
    """Based on code in `cxxheaderparser.preprocessor`."""
    # pcpp emits the #line directive using the filename you pass in
    # but will rewrite it if it's on the include path it uses. This
    # is copied from pcpp:
    absSource = str(filename.resolve())
    for pattern, repl in pp.rewrite_paths:
        temp = re.sub(pattern, repl, absSource)
        if temp != absSource:
            return Path(temp)

    return filename


def readContentForPreprocess(file: Path):
    content = file.read_text(ENCODING)
    # fix cmake directives https://stackoverflow.com/a/42719518

    # this is a workaround for static variables
    for comment in (
        '#define _FC_LOG_LEVEL_INIT',
        '#define FC_LOG_LEVEL_INIT',
        'FC_LOG_LEVEL_INIT',
    ):
        content = content.replace(comment, f'// {comment}')

    return content.replace('#cmakedefine', '#define')


@logCurrentTaskDecFactory(msg="Cleaning preprocess files")
def cleanPreprocessFiles(path: Path = SOURCE_DIR):
    for file in path.rglob('*.ii'):
        file.unlink(missing_ok=True)


def removeEmptyLines(content: str) -> str:
    return '\n'.join(line for line in content.splitlines() if line.strip())
