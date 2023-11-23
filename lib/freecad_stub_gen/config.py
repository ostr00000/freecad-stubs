from pathlib import Path

from freecad_stub_gen.logger import LEVEL_CODE

myDir = Path(__file__).resolve().parent

LOGGER_LEVEL = LEVEL_CODE
SOURCE_DIR = (myDir / '../../FreeCAD/src/').resolve()
TARGET_DIR = (myDir / '../../freecad_stubs/').resolve()
