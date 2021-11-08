# Translate.cpp
def translate(context: str, sourcetext: str, disambiguation: str = None, n: int = -1, /):
    """
    translate(context, sourcetext, disambiguation = None, n=-1)
    -- Returns the translation text for sourceText, by querying
    the installed translation files. The translation files are
    searched from the most recently installed file back to the
    first installed file.
    """


def QT_TRANSLATE_NOOP(context, sourcetext, /):
    """
    QT_TRANSLATE_NOOP(context, sourcetext)
    Marks the UTF-8 encoded string literal sourcetext for delayed translation in the given context.
    The context is typically a class name and also needs to be specified as a string literal.
    """


def QT_TRANSLATE_NOOP3(context, sourcetext, disambiguation, /):
    """
    QT_TRANSLATE_NOOP3(context, sourcetext, disambiguation)
    Marks the UTF-8 encoded string literal sourceText for delayed translation in the given context
    with the given disambiguation. The context is typically a class and also needs to be specified
    as a string literal. The string literal disambiguation should be a short semantic tag to tell
    apart otherwise identical strings.
    """


def QT_TRANSLATE_NOOP_UTF8(context, sourcetext, /):
    """
    QT_TRANSLATE_NOOP_UTF8(context, sourcetext)
    Same as QT_TRANSLATE_NOOP
    """


def QT_TR_NOOP(sourcetext, /):
    """
    QT_TR_NOOP(sourcetext)
    Marks the UTF-8 encoded string literal sourcetext for delayed translation in the current context
    """


def QT_TR_NOOP_UTF8(sourcetext, /):
    """
    QT_TR_NOOP_UTF8(sourcetext)
    Same as QT_TR_NOOP
    """


def installTranslator(arg1: str, /) -> bool:
    """Install a translator for testing purposes"""


def removeTranslators() -> bool:
    """Remove test translators"""
