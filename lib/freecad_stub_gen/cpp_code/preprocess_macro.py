import argparse
import io
import logging
import re
import sys
from functools import wraps
from pathlib import Path
from typing import Literal, TextIO

from joblib import Parallel, delayed
from pcpp import Action, OutputDirective, Preprocessor
from pcpp.parser import Macro

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.debug_functions import genFilesWithLog, timeDec
from freecad_stub_gen.file_functions import genFilesToPreprocess

logger = logging.getLogger(__name__)
ENCODING = 'iso8859-1'


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


class MatchWrapper:
    def __init__(self, origMatch: re.Match):
        self.origMatch: re.Match | None = origMatch
        self.state: dict | None = None

    def __getstate__(self):
        if self.state is not None:
            return self.state

        if self.origMatch is None:
            msg = "Original match is `None`!"
            raise TypeError(msg)

        return {'groups': self.origMatch.groups()}

    def __setstate__(self, state):
        if not isinstance(state, dict):
            msg = f"Expected dict to restore state for {type(self)}"
            raise TypeError(msg)

        self.origMatch = None
        self.state = state

    def __getattr__(self, item):
        if self.origMatch is None:
            if self.state is None:
                msg = "State object is `None`!"
                raise TypeError(msg)
            try:
                return self.state[item]
            except KeyError as ke:
                raise AttributeError from ke

        return getattr(self.origMatch, item)


class Visitor:
    """Based on https://github.com/mbr/visitor/blob/master/visitor/__init__.py."""

    def visit(self, node):
        mro = (node if isinstance(node, type) else type(node)).mro()
        for cls in mro:
            meth = getattr(self, 'visit_' + cls.__name__, None)
            if meth is not None:
                return meth(node)

        return self.default(node)

    def default(self, node):
        pass


class PickleFixerVisitor(Visitor):
    def visit_list(self, listNode: list):
        return [self.visit(el) for el in listNode]

    def visit_tuple(self, tupleNode: list):
        return tuple(self.visit(t) for t in tupleNode)

    def visit_dict(self, dictNode: dict):
        return {self.visit(k): self.visit(v) for k, v in dictNode.items()}

    def visit_Match(self, match: re.Match):
        return MatchWrapper(match)

    def visit_MatchWrapper(self, node):
        return node

    def default(self, node):
        if hasattr(node, '__dict__'):
            for attrName, attrVal in node.__dict__.items():
                node.__dict__[attrName] = self.visit(attrVal)
        elif node.__class__.__module__ in sys.stdlib_module_names:
            return node

        return node


def preprocessPickleDec(fun):
    @wraps(fun)
    def _innerPreProcess(*arg, **kwargs):
        ret = fun(*arg, **kwargs)
        pfv = PickleFixerVisitor()
        return pfv.visit(ret)

    return _innerPreProcess


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


_commonMacros = {}


class SaveErrorsPreprocessor(Preprocessor):
    """Based on `cxxheaderparser.preprocessor._CustomPreprocessor`."""

    def __init__(self):
        super().__init__()
        self.errors = list[str]()
        self.assume_encoding = ENCODING

        self.macros.update(_commonMacros)

    def setLineDirective(self, *, include=False):
        self.line_directive = '#line' if include else None

    def on_error(self, file, line, msg):
        if 'arguments but was passed' in msg and '3rdParty' in file:
            return  # probably there is used another macro?

        self.errors.append(f"{file}:{line} error: {msg}")

    def on_include_not_found(self, *ignored):
        raise OutputDirective(Action.IgnoreAndPassThrough)

    def on_comment(self, tok) -> bool | None:  # type: ignore[reportIncompatibleMethodOverride]
        return True

    def on_file_open(self, is_system_include, includepath):
        with super().on_file_open(is_system_include, includepath) as file:
            return io.StringIO(file.read().replace('#cmakedefine', '#define'))

    def on_directive_unknown(
        self, directive, toks, ifpassthru, precedingtoks
    ) -> Literal[True] | None:
        if directive.value in ('pragma', 'line'):
            raise OutputDirective(Action.IgnoreAndPassThrough)

        ret: bool | None = None
        val = ''.join(tok.value for tok in toks)

        match directive.value:
            case 'error':
                self.return_code += 1
                ret = True
            case 'warning':
                ret = True
            case _:
                val = f"Unknown directive: {val}"

        msg = f"{directive.source}:{directive.lineno:d} {directive.value}: {val}"
        self.errors.append(msg)
        return ret


@preprocessPickleDec
def getCommonMacros() -> dict[str, Macro]:
    macros = [
        # stub generator macros
        'STUB_GEN_COMMENT_START /*',
        'STUB_GEN_COMMENT_END */',
        (
            'STUB_GEN_COMMENT(P_FUN, ...) '
            'STUB_GEN_COMMENT_START '
            'P_FUN ## __VA_ARGS__ '
            'STUB_GEN_COMMENT_END'
        ),
        '_Pragma(...) #pragma(__VA_ARGS__)',
        # some generic macros
        '__linux__',
        'FC_OS_LINUX',
        'PY_MAJOR_VERSION 3',
        '_M_X64 1',
        '__GNUC__ 13',
        'REVISION_ID',
        # this will be redefined later
        '__FILE__',
        # this is a workaround to avoid defining SIZE_MAX as `(~(size_t)0)`
        f'SIZE_MAX {2**64}',
        # Qt macros
        # /usr/include/x86_64-linux-gnu/qt5/QtCore/qobjectdefs.h
        'Q_SIGNALS public STUB_GEN_COMMENT(Q_SIGNALS)',
    ]
    commentedMacros = [
        # Qt macros
        'Q_SLOTS',
        'Q_EMIT',
        'Q_OBJECT',
        'Q_DISABLE_COPY(...)',
        'Q_DECLARE_METATYPE(...)',
        # open inventor macros
        'SO_NODE_HEADER(...)',
        'FC_LOG_LEVEL_INIT(...)',
    ]

    pre = SaveErrorsPreprocessor()
    pre.add_path('/usr/include/x86_64-linux-gnu/qt5')
    for m in macros:
        pre.define(m)
    for cm in commentedMacros:
        fun = cm.replace('...', '__VA_ARGS__')
        pre.define(f'{cm} STUB_GEN_COMMENT({fun})')

    p = Path('/usr/include/x86_64-linux-gnu/qt5/QtCore/qobject.h')
    content = readContentForPreprocess(p)

    pre.parse(content, str(p))
    macroContent = io.StringIO()
    pre.write(macroContent)

    return pre.macros


# noinspection PyRedeclaration
_commonMacros = getCommonMacros()


def cleanPreprocessFiles(path: Path = SOURCE_DIR):
    for file in path.rglob('*.ii'):
        file.unlink(missing_ok=True)
    for file in path.rglob('*.ii.cpp'):
        file.unlink(missing_ok=True)


def processFile(filePath: Path) -> list[str]:
    outFile = filePath.with_suffix(filePath.suffix + '.ii')
    if outFile.exists():
        logger.info(f"File `{filePath}` exists - skipping")
        return []

    logger.debug(f"Processing: {filePath=}")
    pre = SaveErrorsPreprocessor()
    pre.add_path(str(SOURCE_DIR))

    content = readContentForPreprocess(filePath)
    pre.parse(content, str(filePath))

    macroContent = io.StringIO()
    pre.write(macroContent)
    macroContent.seek(0)

    fixedPath = fixPath(pre, filePath)
    onlyCurrentFileContent = getContentForOriginalFile(str(fixedPath), macroContent)

    if pre.errors:
        return list(pre.errors)

    outFile.write_text(removeEmptyLines(onlyCurrentFileContent))
    if filePath.suffix in ('.c', '.cpp', '.cxx', '.cc'):
        text = removeEmptyLines(macroContent.getvalue())
        filePath.with_suffix(f'{filePath.suffix}.ii{filePath.suffix}').write_text(text)

    return []


def _genTasks():
    dpf = delayed(processFile)
    for filePath in genFilesWithLog(genFilesToPreprocess, desc="Generate macros"):
        yield dpf(filePath)


@timeDec
def generatePreprocessedFiles():
    with Parallel(
        n_jobs=-1,
        return_as='generator',
    ) as p:
        allErrors = [e for errors in p(_genTasks()) if errors for e in errors]

    for e in allErrors:
        logger.error(e)


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


def removeEmptyLines(content: str) -> str:
    return '\n'.join(line for line in content.splitlines() if line.strip())


def main(args=None):
    ap = argparse.ArgumentParser()
    ap.add_argument(
        '--clean',
        action='store_true',
        default=True,
    )
    par = ap.parse_args(args)

    if par.clean:
        logger.info("Preprocess files - cleaning...")
        cleanPreprocessFiles()
        logger.info("Preprocess files - cleaned.")

    generatePreprocessedFiles()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
