import argparse
import io
import logging
from pathlib import Path

from pcpp import Action, OutputDirective, Preprocessor

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.debug_functions import timeDec
from freecad_stub_gen.file_functions import genFilesToPreprocess

logger = logging.getLogger(__name__)
ENCODING = 'iso8859-1'


class SaveErrorsPreprocessor(Preprocessor):
    """Based on `cxxheaderparser.preprocessor._CustomPreprocessor`."""

    def __init__(self):
        super().__init__()
        self.errors = list[str]()
        self.assume_encoding = ENCODING
        self._initDefines()

    def _initDefines(self):
        self.define('__linux__')
        self.define('FC_OS_LINUX')
        self.define('PY_MAJOR_VERSION 3')
        self.define('_M_X64 1')
        self.define('__GNUC__ 13')
        self.define('REVISION_ID')

    def on_error(self, file, line, msg):
        if 'arguments but was passed' in msg and '3rdParty' in file:
            return  # probably there is used another macro?

        self.errors.append(f"{file}:{line} error: {msg}")

    def on_include_not_found(self, *ignored):
        raise OutputDirective(Action.IgnoreAndPassThrough)

    def on_comment(self, *ignored):
        return True

    def on_directive_unknown(self, directive, toks, ifpassthru, precedingtoks):
        if directive.value in ('pragma', 'line'):
            return OutputDirective(Action.IgnoreAndPassThrough)

        if directive.value in ('error', 'warning'):
            val = ''.join(tok.value for tok in toks)
            msg = f"{directive.source}:{directive.lineno:d} {directive.value}: {val}"
            self.errors.append(msg)

            if directive.value == 'error':
                self.return_code += 1

            return True

        return None


def cleanPreprocessFiles(path: Path = SOURCE_DIR):
    for file in path.rglob('*.ii'):
        file.unlink(missing_ok=True)


def readContentForPreprocess(file: Path):
    content = file.read_text(ENCODING)
    # fix cmake directives https://stackoverflow.com/a/42719518
    return content.replace('#cmakedefine', '#define')


@timeDec
def generatePreprocessedFiles():
    errors = list[str]()

    for file in genFilesToPreprocess(desc="generate macros"):
        outFile = file.with_suffix(file.suffix + '.ii')
        if outFile.exists():
            continue

        pre = SaveErrorsPreprocessor()
        content = readContentForPreprocess(file)
        pre.parse(content, str(file))

        s = io.StringIO()
        pre.write(s)

        if pre.errors:
            errors.extend(pre.errors)
            continue

        text = s.getvalue()
        outFile.write_text(text)

    for e in errors:
        logger.error(e)


def main(args=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--clean', action='store_true', default=True)
    par = ap.parse_args(args)

    if par.clean:
        cleanPreprocessFiles()

    generatePreprocessedFiles()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
