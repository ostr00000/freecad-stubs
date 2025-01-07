import logging
from pathlib import Path

import typed_argparse as tap

from stub_gen.macro.generate_intermediate import (
    cleanBuildDir,
    generateIntermediateFiles,
)

logger = logging.getLogger(__name__)

# TODO @PO: [P5] remove after this library is finished.
FREECAD_DIR = Path(__name__).resolve().expanduser().parents[3] / 'FreeCAD'


class MacroArgs(tap.TypedArgs):
    repo_path: Path = tap.arg(help="Git project with C++ code.", default=FREECAD_DIR)
    clean: bool = tap.arg(
        help="Clean build directory before generation.", default=False
    )


def runner(args: MacroArgs):
    if args.clean:
        cleanBuildDir(args.repo_path)

    generateIntermediateFiles(args.repo_path)


def main():
    logging.basicConfig(level=logging.DEBUG)
    tap.Parser(MacroArgs).bind(runner).run()


if __name__ == '__main__':
    main()
