import textwrap


def indent(block, distance=1, indentSize=4):
    return textwrap.indent(block, ' ' * distance * indentSize)
