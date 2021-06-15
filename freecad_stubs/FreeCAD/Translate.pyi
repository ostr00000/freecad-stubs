# Translate.cpp
def translate(arg1: str, arg2: str, arg3: str = None, arg4: int = None, /):
    """translate(context, sourcetext, disambiguation = None, n=-1)
    -- Returns the translation text for sourceText, by querying
    the installed translation files. The translation files are
    searched from the most recently installed file back to the
    first installed file."""


def QT_TRANSLATE_NOOP(arg1: object, arg2: object, /):
    """QT_TRANSLATE_NOOP(context, sourcetext)
    Marks the UTF-8 encoded string literal sourcetext for delayed translation in the given context.
    The context is typically a class name and also needs to be specified as a string literal."""


def QT_TRANSLATE_NOOP3(arg1: object, arg2: object, arg3: object, /):
    """QT_TRANSLATE_NOOP3(context, sourcetext, disambiguation)
    Marks the UTF-8 encoded string literal sourceText for delayed translation in the given context
    with the given disambiguation. The context is typically a class and also needs to be specified
    as a string literal. The string literal disambiguation should be a short semantic tag to tell
    apart otherwise identical strings."""


def QT_TRANSLATE_NOOP_UTF8(arg1: object, arg2: object, /):
    """QT_TRANSLATE_NOOP_UTF8(context, sourcetext)
    Same as QT_TRANSLATE_NOOP"""


def QT_TR_NOOP(arg1: object, /):
    """QT_TR_NOOP(sourcetext)
    Marks the UTF-8 encoded string literal sourcetext for delayed translation in the current context"""


def QT_TR_NOOP_UTF8(arg1: object, /):
    """QT_TR_NOOP_UTF8(sourcetext)
    Same as QT_TR_NOOP"""
