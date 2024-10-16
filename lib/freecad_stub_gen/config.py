from pathlib import Path

from freecad_stub_gen.logger import LEVEL_CODE

LIB_DIR = Path(__file__).resolve().parent
PROJECT_DIR = LIB_DIR.parents[1]

FREECAD_DIR = (PROJECT_DIR / 'FreeCAD').resolve()
SOURCE_DIR = (FREECAD_DIR / 'src').resolve()
TARGET_DIR = (PROJECT_DIR / 'freecad_stubs/').resolve()

LOGGER_LEVEL = LEVEL_CODE
DOCSTRING_DEBUG_NOTES = False
