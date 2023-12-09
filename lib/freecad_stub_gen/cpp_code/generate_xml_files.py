import logging
import shlex
import sys
from subprocess import check_call

from freecad_stub_gen.config import SOURCE_DIR, projectDir

logger = logging.getLogger(__name__)
generatePath = projectDir / 'FreeCAD/src/Tools/generate.py'


def generateXmlFiles():
    for searchDirName in ('App', 'Base', 'Gui', 'Mod'):
        for xmlPath in (SOURCE_DIR / searchDirName).rglob('*Py.xml'):
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
            check_call(args)
