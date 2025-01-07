import logging

import typed_argparse as tap

from stub_gen.scan.function import genFunctionReturnValues
from stub_gen.scan.python_structs import genCreatedPyModules
from stub_gen.scan.tu_storage import getFreeCADPath, transactionUnitStorage
from stub_gen.scan.wrapper import DiagnosticRepr, transactionUnit

logger = logging.getLogger(__name__)


class ScanArgs(tap.TypedArgs):
    pass


def runner(args: ScanArgs):
    exampleFile = getFreeCADPath() / 'src/Gui/Application.cpp'
    tu = transactionUnitStorage[exampleFile]
    transactionUnit.set(tu)

    dr = DiagnosticRepr(tu)
    dr.logErrorDiagnostics()

    modules = list(genCreatedPyModules(tu))
    logger.debug(modules)

    for m in modules:
        for func in m.moduleFunctions:
            retValues = list(genFunctionReturnValues(func.meth))
            logger.info(f'Function {func.functionName} returns: {retValues}')


def main():
    logging.basicConfig(level=logging.DEBUG)
    tap.Parser(ScanArgs).bind(runner).run()


if __name__ == '__main__':
    main()
