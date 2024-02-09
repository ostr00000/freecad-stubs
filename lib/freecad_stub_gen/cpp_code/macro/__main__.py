import argparse
import logging

from freecad_stub_gen.cpp_code.macro.cache import isNewGitHead
from freecad_stub_gen.cpp_code.macro.file_preparation import cleanPreprocessFiles

logger = logging.getLogger(__name__)


def main(args=None):
    isNewCode = isNewGitHead()

    ap = argparse.ArgumentParser()
    ap.add_argument(
        '--clean',
        action='store_true',
        default=isNewCode,
    )
    par = ap.parse_args(args)

    if par.clean:
        cleanPreprocessFiles()

    # import locally, because this is heavy time-consuming import
    from freecad_stub_gen.cpp_code.macro.run import generatePreprocessedFiles

    generatePreprocessedFiles()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
