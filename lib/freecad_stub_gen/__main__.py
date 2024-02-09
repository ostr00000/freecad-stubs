import logging

from freecad_stub_gen.config import (
    LOGGER_LEVEL,
)
from freecad_stub_gen.cpp_code.macro.cache import isNewGitHead

logger = logging.getLogger(__name__)


def configLogger():
    from freecad_stub_gen.logger import RepeatedFilter

    logging.basicConfig(level=LOGGER_LEVEL)
    logging.getLogger().addFilter(RepeatedFilter())


def main():
    if isNewGitHead():
        from freecad_stub_gen.cpp_code.generate_xml_files import generateXmlFiles
        from freecad_stub_gen.cpp_code.macro.run import generatePreprocessedFiles

        generateXmlFiles()
        generatePreprocessedFiles()

    from freecad_stub_gen.generate import generateFreeCadStubs
    from freecad_stub_gen.generators.types_enum import generateTypes

    generateTypes()
    generateFreeCadStubs()


if __name__ == '__main__':
    configLogger()
    main()
    logging.info("freecad_stub_gen finished successfully")
