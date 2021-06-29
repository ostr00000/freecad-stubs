import dataclasses
from typing import Iterator, Union

from freecad_stub_gen.generators.method.types_converter import Arg, PositionalOnlyArg, \
    KeyWorldOnlyArg


def mergeArgSuitesGen(codeSuites: list[list[Arg]], docSuites: list[list[Arg]],
                      firstArgumentName: str = None) -> Iterator[str]:
    if len(codeSuites) == len(docSuites) == 0:
        return  # function does not exist neither in code nor xml

    retVal: list[Union[str, Arg]] = []
    if firstArgumentName:
        retVal.append(firstArgumentName)

    yielded = False
    for docS in docSuites:
        for codeS in codeSuites:
            compatible = True
            matchedSuite = list(retVal)
            docSuiteIt = iter(docS)

            for codeArg in codeS:
                if isinstance(codeArg, (PositionalOnlyArg, KeyWorldOnlyArg)):
                    matchedSuite.append(codeArg)
                    continue

                try:
                    docArg = next(docSuiteIt)
                except StopIteration:
                    compatible = False
                    break

                newArg = codeArg
                if codeArg.name is None:
                    newArg = dataclasses.replace(codeArg, name=docArg.name)
                if codeArg.default and codeArg.value is None:
                    newArg = dataclasses.replace(newArg, value=docArg.value)

                matchedSuite.append(newArg)

            if compatible and len(list(docSuiteIt)) == 0:
                yield ', '.join(map(str, matchedSuite))
                yielded = True

        # maybe nameSuite is empty, try argSuite
    if not yielded:
        for codeS in codeSuites:
            yield ', '.join(map(str, retVal + codeS))
            yielded = True

        # maybe argSuite is empty, try nameSuite
    if not yielded:
        for docS in docSuites:
            yield ', '.join(map(str, retVal + docS))
            yielded = True

        # this should never be reachable
    if not yielded:
        yield ', '.join(retVal)
