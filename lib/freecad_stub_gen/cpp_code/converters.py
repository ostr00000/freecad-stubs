import ast
import builtins
import logging
import re
from typing import overload

logger = logging.getLogger(__name__)


@overload
def removeQuote(v: str) -> str:
    ...


@overload
def removeQuote(*val: str) -> list[str]:
    ...


def removeQuote(*val: str):
    withoutQuote = [v.strip().removeprefix('"').removesuffix('"') for v in val]
    if len(withoutQuote) == 1:
        return withoutQuote[0]
    return withoutQuote


_REG_COMMENT_REM = re.compile(
    r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"', re.DOTALL | re.MULTILINE
)


def _replacer(match):
    s = match.group(0)
    if s.startswith('/'):
        return ' '  # note: a space and not an empty string
    return s


def removeComments(text):
    """Based on https://stackoverflow.com/a/241506"""
    return re.sub(_REG_COMMENT_REM, _replacer, text)


def toBool(text: str | bool | None) -> bool:
    match str(text).lower():
        case 'y' | 'yes' | 't' | 'true' | 'on' | '1':
            return True
        case 'n' | 'no' | 'f' | 'false' | 'off' | '0' | 'none':
            return False
        case _:
            raise ValueError(f"Unknown bool value: {text}")


def validatePythonValue(value: str) -> str | None:
    if value in builtins.__dict__:
        return value

    if value in ('true', 'false'):
        return value.title()

    # pylint: disable=broad-exception-caught
    try:
        ast.literal_eval(value)
    except (SyntaxError, ValueError):
        pass
    except Exception as exc:
        logger.error(f'Cannot evaluate value: {exc}')
    else:
        return value

    if value and value[-1].lower() in ('f', 'l'):
        # maybe float literal (ex. 3.14f)
        return validatePythonValue(value[:-1])

    return None


def convertToPythonValue(value: str):
    if (safe := validatePythonValue(value)) is None:
        return False, None

    if value in builtins.__dict__:
        conv = builtins.__dict__[value]
    else:
        conv = ast.literal_eval(safe)

    return True, conv
