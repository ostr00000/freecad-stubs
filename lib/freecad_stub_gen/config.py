import logging
from pathlib import Path

myDir = Path(__file__).resolve().parent

LOGGER_LEVEL = logging.INFO
SOURCE_DIR = (myDir / '../../data/src/').resolve()
GEN_DIR = (myDir / '../../gen/').resolve()
TARGET_DIR = (myDir / '../../target/').resolve()
INDENT_SIZE = 4
