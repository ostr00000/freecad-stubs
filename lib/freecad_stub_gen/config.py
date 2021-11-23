import logging
from pathlib import Path

myDir = Path(__file__).resolve().parent

LOGGER_LEVEL = logging.INFO
SOURCE_DIR = (myDir / '../../FreeCAD/src/').resolve()
TARGET_DIR = (myDir / '../../freecad_stubs/').resolve()
