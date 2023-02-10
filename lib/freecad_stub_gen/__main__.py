import logging

from freecad_stub_gen.config import LOGGER_LEVEL
from freecad_stub_gen.logger import RepeatedFilter

logging.basicConfig(level=LOGGER_LEVEL)
logging.getLogger().addFilter(RepeatedFilter())

from freecad_stub_gen.generators.types_enum import generateTypes
from freecad_stub_gen.generate import generateFreeCadStubs

generateTypes()
generateFreeCadStubs()

if __name__ == '__main__':
    print('ok')
