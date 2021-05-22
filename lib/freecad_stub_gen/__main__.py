import logging
import sys

from freecad_stub_gen.config import LOGGER_LEVEL

logging.basicConfig(level=LOGGER_LEVEL)

requiredPythonVersion = (3, 10)
if sys.version_info < requiredPythonVersion:
    logging.critical(f"Sorry but this program has {requiredPythonVersion=}")
    exit(1)

from freecad_stub_gen.generate import generateFreeCadStubs

generateFreeCadStubs()

if __name__ == '__main__':
    print('ok')
