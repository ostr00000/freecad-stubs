import logging
from pathlib import Path

myDir = Path(__file__).resolve().parent

LOGGER_LEVEL = logging.INFO
SOURCE_DIR = (myDir / '../../data/src/').resolve()
TARGET_DIR = (myDir / '../../stub_target/').resolve()
INDENT_SIZE = 4
