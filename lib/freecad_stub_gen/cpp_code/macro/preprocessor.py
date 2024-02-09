import io
import logging
from pathlib import Path
from typing import Literal

from pcpp import Action, OutputDirective, Preprocessor
from pcpp.parser import Macro

from freecad_stub_gen.cpp_code.macro.file_preparation import readContentForPreprocess
from freecad_stub_gen.cpp_code.macro.pickle_fixer import preprocessPickleDec
from freecad_stub_gen.file_functions import ENCODING

logger = logging.getLogger(__name__)
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

    def on_include_not_found(self, *_ignored):
        raise OutputDirective(Action.IgnoreAndPassThrough)

    def on_comment(self, tok) -> bool | None:  # type: ignore[reportIncompatibleMethodOverride]
        return True

    def on_file_open(self, is_system_include, includepath):
        with super().on_file_open(is_system_include, includepath) as file:
            return io.StringIO(file.read().replace('#cmakedefine', '#define'))

    def on_directive_unknown(
        self, directive, toks, ifpassthru, precedingtoks
    ) -> Literal[True] | None:
        del ifpassthru, precedingtoks
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
