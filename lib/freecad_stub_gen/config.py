import logging
from pathlib import Path

myDir = Path(__file__).resolve().parent

LOGGER_LEVEL = logging.INFO
SOURCE_DIR = (myDir / '../../data/src/').resolve()
TARGET_DIR = (myDir / '../../freecad_stubs/').resolve()
INDENT_SIZE = 4
