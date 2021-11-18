from inspect import Parameter, Signature
from typing import Iterator

from freecad_stub_gen.generators.common.annotation_parameter import SelfSignature
from freecad_stub_gen.generators.common.arguments_converter import DEFAULT_ARG_NAME

NO_ANNOTATIONS = (None, 'object', Parameter.empty)


def mergeSignaturesGen(
        codeSignatures: list[SelfSignature],
        docSignatures: list[SelfSignature],
        firstParam: Parameter = None,
) -> Iterator[SelfSignature]:
    if len(codeSignatures) == len(docSignatures) == 0:
        return  # function does not exist neither in code nor xml

    retParam: list[Parameter] = []
    if firstParam:
        retParam.append(firstParam)

    yielded = False
    for docS in docSignatures:
        for codeS in codeSignatures:
            compatible = True
            matchedParam = list(retParam)
            docSignatureIt = iter(docS.parameters.values())

            for codeParam in codeS.parameters.values():
                try:
                    docParam = next(docSignatureIt)
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

                if codeParam.annotation in NO_ANNOTATIONS \
                        and docParam.annotation not in NO_ANNOTATIONS:
                    newArg = newArg.replace(annotation=docParam.annotation)

                matchedParam.append(newArg)

            if compatible and len(list(docSignatureIt)) == 0:
                yield SelfSignature(matchedParam, return_annotation=codeS.return_annotation,
                                    exceptions=codeS.exceptions)
                yielded = True

    # maybe docSignatures is empty, try codeSignatures
    if not yielded:
        for codeS in codeSignatures:
            yield SelfSignature(retParam + list(codeS.parameters.values()),
                                return_annotation=codeS.return_annotation,
                                exceptions=codeS.exceptions)
            yielded = True

    # maybe codeSignatures is empty, try docSignatures
    if not yielded:
        for docS in docSignatures:
            yield SelfSignature(retParam + list(docS.parameters.values()),
                                return_annotation=docS.return_annotation)
            yielded = True

    # this should never be reachable
    if not yielded:
        yield SelfSignature(retParam)
