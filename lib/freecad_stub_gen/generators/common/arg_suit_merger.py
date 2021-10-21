from inspect import Parameter, Signature
from typing import Iterator

from freecad_stub_gen.generators.common.types_converter import DEFAULT_ARG_NAME, SelfSignature


def mergeParamIntoSignatureGen(
        codeSuites: list[list[Parameter]],
        docSuites: list[list[Parameter]],
        firstArgumentName: Parameter = None,
) -> Iterator[Signature]:
    if len(codeSuites) == len(docSuites) == 0:
        return  # function does not exist neither in code nor xml

    retVal: list[Parameter] = []
    if firstArgumentName:
        retVal.append(firstArgumentName)

    yielded = False
    for docS in docSuites:
        for codeS in codeSuites:
            compatible = True
            matchedSuite = list(retVal)
            docSuiteIt = iter(docS)

            for codeParam in codeS:
                try:
                    docParam = next(docSuiteIt)
                except StopIteration:
                    compatible = False
                    break

                newArg = codeParam
                if codeParam.name.startswith(DEFAULT_ARG_NAME) \
                        and not docParam.name.startswith(DEFAULT_ARG_NAME):
                    newArg = newArg.replace(name=docParam.name)

                if codeParam.default is None \
                        and docParam.default not in (None, Parameter.empty):
                    newArg = newArg.replace(default=docParam.default)

                matchedSuite.append(newArg)

            if compatible and len(list(docSuiteIt)) == 0:
                yield SelfSignature(matchedSuite)
                yielded = True

    # maybe nameSuite is empty, try argSuite
    if not yielded:
        for codeS in codeSuites:
            yield SelfSignature(retVal + codeS)
            yielded = True

    # maybe argSuite is empty, try nameSuite
    if not yielded:
        for docS in docSuites:
            yield SelfSignature(retVal + docS)
            yielded = True

    # this should never be reachable
    if not yielded:
        yield SelfSignature(retVal)
