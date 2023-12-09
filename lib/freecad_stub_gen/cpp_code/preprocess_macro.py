import io
import logging
from pathlib import Path
from typing import Iterator

from cxxheaderparser.preprocessor import _CustomPreprocessor

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.file_functions import preprocessFiles

logger = logging.getLogger(__name__)

encoding = 'iso8859-1'
pre = _CustomPreprocessor(encoding, None)
pre.define('__linux__')
pre.define('PY_MAJOR_VERSION 3')


def logProgress[T](it: Iterator[T], total: int, desc='') -> Iterator[T]:
    for i, val in enumerate(it):
        logger.debug(f'Progress {desc}[{i:{len(str(total))}}/{total}]')
        yield val


def cleanPreprocessFiles(path: Path = SOURCE_DIR):
    for file in path.rglob('*.ii'):
        file.unlink(missing_ok=True)


def processAll():
    file: Path
    for file in logProgress(preprocessFiles(), sum(1 for _ in preprocessFiles())):
        content = file.read_text(encoding)
        pre.parse(content, str(file))

        s = io.StringIO()
        pre.write(s)
        text = s.getvalue()

        file.with_suffix(file.suffix + '.ii').write_text(text)

    logger.error(pre.errors)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    cleanPreprocessFiles()
    processAll()
