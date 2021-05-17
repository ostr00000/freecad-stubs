import logging

logging.basicConfig(level=logging.INFO)

from freecad_stub_gen.generate import generateFreeCadStubs

generateFreeCadStubs()

if __name__ == '__main__':
    print('ok')
