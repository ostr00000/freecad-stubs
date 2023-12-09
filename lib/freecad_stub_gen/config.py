from pathlib import Path

from freecad_stub_gen.logger import LEVEL_CODE

libDir = Path(__file__).resolve().parent
projectDir = libDir.parents[1]

LOGGER_LEVEL = LEVEL_CODE
SOURCE_DIR = (projectDir / 'FreeCAD/src/').resolve()
TARGET_DIR = (projectDir / 'freecad_stubs/').resolve()

# these options should be changed when FreeCAD branch is changed
# (maybe cache last used git rev for FreeCad?)
GENERATE_FROM_XML = False
PREPROCESS_CPP_FILES = False
