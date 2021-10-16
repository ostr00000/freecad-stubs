from itertools import islice


def findFunctionCall(text: str, bodyStart: int, bracketL='{', bracketR='}'):
    bracketDeep = 0
    bodyEnd = 0

    sliceIt = islice(text, bodyStart, len(text))
    for bodyEnd, char in enumerate(sliceIt, bodyStart):
        if char == bracketL:
            bracketDeep += 1
        elif char == bracketR:
            bracketDeep -= 1
            if not bracketDeep:
                break

    functionText = text[bodyStart:bodyEnd + 1]
    return functionText


def generateExpressionUntilChar(text: str, expStart: int, splitChar: str,
                                bracketL='(', bracketR=')'):
    assert splitChar not in f'\\"{bracketL}{bracketR}'

    bracketDeep = 0
    expEnd = 0
    ignore = False
    escaped = False

    sliceIt = islice(text, expStart, len(text) + 1)
    for expEnd, char in enumerate(sliceIt, expStart):
        if escaped:
            escaped = False
        elif char == '\\':
            escaped = True
        elif char == '"':
            ignore = not ignore
        elif ignore:
            pass
        elif char == bracketL:
            bracketDeep += 1
        elif char == bracketR:
            bracketDeep -= 1
            if bracketDeep < 0:
                yield text[expStart:expEnd]
                return
        elif char == splitChar and bracketDeep == 0:
            yield text[expStart:expEnd]
            expStart = expEnd + 1

    yield text[expStart:expEnd + 1]
