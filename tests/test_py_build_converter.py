from freecad_stub_gen.generators.common.py_build_converter import parsePyBuildValues


def test_parse():
    for i in (
        "",
        "i",
        "iii",
        "s",
        "y",
        "ss",
        "s#",
        "y#",
        "()",
        "(i)",
        "(ii)",
        "(i,i)",
        "[i,i]",
        "{s:i,s:i}",
        "((ii)(ii)) (ii)",
    ):
        print(parsePyBuildValues(i))
