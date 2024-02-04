import pytest

from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar


@pytest.mark.parametrize(
    'textToParse, pos, expected',
    [
        ('a(1, 2)', 2, ['1', '2']),
        ('b(3, 4)', 2, ['3', '4']),
        ('c(5, 6, 7)', 2, ['5', '6', '7']),
        ('d(e(12, 34), f(5), 6)', 2, ['e(12, 34)', 'f(5)', '6']),
        ('g([34], f[345])', 2, ['[34]', 'f[345]']),
        (
            'h("abc", "(def)", "\\\"", "\\\"(not)")',
            2,
            ['"abc"', '"(def)"', '"\\\""', '"\\\"(not)"'],
        ),
        ('j(qwerty, )', 2, ['qwerty', '']),
        ('i((), (((()), (), ), ))', 2, ['()', '(((()), (), ), )']),
        ('k("ok, or not ok")', 2, ['"ok, or not ok"']),
        ('12345', 2, ['345']),
        ('tuple.setItem(0, type)', 14, ['0', 'type']),
    ],
)
def test_parsing_expression(textToParse: str, pos: int, expected: list[str]):
    exp = [i.strip() for i in generateExpressionUntilChar(textToParse, pos)]
    assert exp == expected


@pytest.mark.parametrize(
    'textToParse, _pos, expected',
    [
        ('a(1, 2)', 2, ['1', '2']),
        ('b(3, 4)', 2, ['3', '4']),
        ('c(5, 6, 7)', 2, ['5', '6', '7']),
        ('d(e(12, 34), f(5), 6)', 2, ['e(12, 34)', 'f(5)', '6']),
        ('g([34], f[345])', 2, ['[34]', 'f[345]']),
        (
            'h("abc", "(def)", "\\\"", "\\\"(not)")',
            2,
            ['"abc"', '"(def)"', '"\\\""', '"\\\"(not)"'],
        ),
        ('j(qwerty, )', 2, ['qwerty', '']),
        ('i((), (((()), (), ), ))', 2, ['()', '(((()), (), ), )']),
        ('k("ok, or not ok")', 2, ['"ok, or not ok"']),
        # diff:
        ('12345', 2, ['1234']),
        ('tuple.setItem(0, type)', 14, ['0', 'type']),
    ],
)
def test_parsing_expression_reverse(textToParse: str, _pos: int, expected: list[str]):
    exp = [
        i.strip()
        for i in generateExpressionUntilChar(
            textToParse, len(textToParse) - 2, startFromEnd=True
        )
    ]
    rev = list(reversed(exp))
    assert rev == expected
