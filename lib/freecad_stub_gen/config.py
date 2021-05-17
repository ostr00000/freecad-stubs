import uuid
from pathlib import Path

myDir = Path(__file__).resolve().parent

GENERATOR_UUID = uuid.uuid4()
SOURCE_DIR = (myDir / '../../data/').resolve()
GEN_DIR = (myDir / '../../gen/').resolve()
TARGET_DIR = (myDir / '../../target/').resolve()
TARGET_PYTHON = (3, 8)
INDENT_SIZE = 4
