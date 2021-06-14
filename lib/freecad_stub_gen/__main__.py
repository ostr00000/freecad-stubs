import logging

from freecad_stub_gen.config import LOGGER_LEVEL
from freecad_stub_gen.logger import configLogFilter

logging.basicConfig(level=LOGGER_LEVEL)
configLogFilter()

from freecad_stub_gen.generate import generateFreeCadStubs

generateFreeCadStubs()

if __name__ == '__main__':
    print('ok')
