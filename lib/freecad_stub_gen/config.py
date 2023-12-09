from pathlib import Path

from freecad_stub_gen.logger import LEVEL_CODE

libDir = Path(__file__).resolve().parent
projectDir = libDir.parents[1]

LOGGER_LEVEL = LEVEL_CODE
SOURCE_DIR = (projectDir / 'FreeCAD/src/').resolve()
TARGET_DIR = (projectDir / 'freecad_stubs/').resolve()
