import logging
import shlex
import sys
from subprocess import check_call

from freecad_stub_gen.config import PROJECT_DIR
from freecad_stub_gen.decorators import logCurrentTaskDecFactory
from freecad_stub_gen.file_functions import genXmlFiles

logger = logging.getLogger(__name__)
generatePath = PROJECT_DIR / 'FreeCAD/src/Tools/generate.py'


@logCurrentTaskDecFactory(msg="Generating FreeCAD code from xml files")
def generateXmlFiles():
    for xmlPath in genXmlFiles():
        outputPath = xmlPath.parent
        args = [
            sys.executable,
            str(generatePath),
            '--outputPath',
            str(outputPath),
            str(xmlPath),
        ]

        logger.info(f"Generating {outputPath}")
        logger.debug(f"CMD:\n{shlex.join(args)}")

        # ignore: `subprocess` call: check for execution of untrusted input
        check_call(args)  # noqa: S603
