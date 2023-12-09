import logging

from freecad_stub_gen.config import (
    GENERATE_FROM_XML,
    LOGGER_LEVEL,
    PREPROCESS_CPP_FILES,
)


def configLogger():
    from freecad_stub_gen.logger import RepeatedFilter

    logging.basicConfig(level=LOGGER_LEVEL)
    logging.getLogger().addFilter(RepeatedFilter())


def main():
    from freecad_stub_gen.generate import generateFreeCadStubs
    from freecad_stub_gen.generators.types_enum import generateTypes
    from freecad_stub_gen.cpp_code.generate_xml_files import generateXmlFiles
    from freecad_stub_gen.cpp_code.preprocess_macro import (
        cleanPreprocessFiles,
        preprocessAllCppFiles,
    )

    if GENERATE_FROM_XML:
        generateXmlFiles()

    if PREPROCESS_CPP_FILES:
        cleanPreprocessFiles()
        preprocessAllCppFiles()

    generateTypes()
    generateFreeCadStubs()


if __name__ == '__main__':
    configLogger()
    main()
    logging.info("freecad_stub_gen finished successfully")
