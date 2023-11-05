from inspect import Parameter

from freecad_stub_gen.generators.common.annotation_parameter import SelfSignature
from freecad_stub_gen.generators.common.arguments_converter.definitions import (
    DEFAULT_ARG_NAME,
)


class SignatureMerger:
    NO_ANNOTATIONS = (None, 'object', Parameter.empty)

    def __init__(
        self,
        codeSignatures: list[SelfSignature],
        docSignatures: list[SelfSignature],
        firstParam: Parameter | None = None,
        cFunName: str = '',
    ):
        self.codeSignatures = codeSignatures
        self.docSignatures = docSignatures
        self.cFunName = cFunName

        self._retParam: list[Parameter] = []
        self._yielded = False
        self._remainingSig: list[SelfSignature] = []

        if firstParam is not None:
            self._retParam.append(firstParam)

    def genMergedCodeAndDocSignatures(self):
        if len(self.codeSignatures) == len(self.docSignatures) == 0:
            return  # function does not exist, neither in code nor xml

        yield from self._mergeCodeWithUnknownParametersAndDocsSignatures()
        if self._yielded:
            return

        yield from self._mergeCodeAndDocsSignatures()
        yield from self._genRemainingCodeSignatures()
        if self._yielded:
            return

        # this should never be reachable
        yield SelfSignature(self._retParam)
        raise NotImplementedError

    def _mergeCodeWithUnknownParametersAndDocsSignatures(self):
        codeS: SelfSignature
        match self.codeSignatures:
            case [SelfSignature(unknown_parameters=True) as codeS]:
                pass
            case _:
                return

        for docS in self.docSignatures:
            joinedParams = list(
                self._mergeParamNamesGen(
                    list(codeS.parameters.values()), list(docS.parameters.values())
                )
            )
            yield codeS.replace(parameters=self._retParam + joinedParams)
            self._yielded = True

    @classmethod
    def _mergeParamNamesGen(
        cls, codeParams: list[Parameter], docsParams: list[Parameter]
    ):
        cParamIt = iter(codeParams)
        pos = 0
        # we iterate over `docsParams` first to not exhaust `cParamIt` iterator
        for dp, cp in zip(docsParams, cParamIt):
            if dp.kind == Parameter.VAR_POSITIONAL:
                # docs are vague about params from this position, so we prefer code params
                yield cp
                break

            toReplace = {'name': dp.name}
            if dp.default not in (Parameter.empty, None):
                toReplace['default'] = dp.default
            yield cp.replace(**toReplace)
            pos += 1

        # use yield only from one
        yield from cParamIt
        yield from docsParams[pos:]

    def _mergeCodeAndDocsSignatures(self):
        usedCodeSignatures = []
        for docS in self.docSignatures:
            docYielded = False

            for codeS in self.codeSignatures:
                matchedParam = self._matchParameters(codeS.parameters, docS.parameters)
                if matchedParam is not None:
                    usedCodeSignatures.append(codeS)
                    yield codeS.replace(parameters=matchedParam)
                    self._yielded = True
                    docYielded = True

            if not docYielded:
                yield docS.replace(
                    parameters=self._retParam + list(docS.parameters.values())
                )
                self._yielded = True

        self._remainingSig = [
            codeS for codeS in self.codeSignatures if codeS not in usedCodeSignatures
        ]

    def _matchParameters(self, codeParams, docParams) -> list[Parameter] | None:
        matchedParam = list(self._retParam)
        docSignatureIt = iter(docParams.values())

        for codeParam in codeParams.values():
            try:
                docParam = next(docSignatureIt)
            except StopIteration:
                if codeParam.default is not Parameter.empty:
                    # maybe docs have only required params
                    matchedParam.append(codeParam)
                    continue

                return None

            newArg = codeParam
            if codeParam.name.startswith(
                DEFAULT_ARG_NAME
            ) and not docParam.name.startswith(DEFAULT_ARG_NAME):
                newArg = newArg.replace(name=docParam.name)

            if codeParam.default is None and docParam.default not in (
                None,
                Parameter.empty,
            ):
                newArg = newArg.replace(default=docParam.default)

            if (
                codeParam.annotation in self.NO_ANNOTATIONS
                and docParam.annotation not in self.NO_ANNOTATIONS
            ):
                newArg = newArg.replace(annotation=docParam.annotation)

            matchedParam.append(newArg)

        if list(docSignatureIt):
            return None  # there remain more arguments

        return matchedParam

    def _genRemainingCodeSignatures(self):
        """Maybe `docSignatures` is empty, in that case try gen `codeSignatures`."""
        for codeS in self._remainingSig:
            yield codeS.replace(
                parameters=self._retParam + list(codeS.parameters.values())
            )
            self._yielded = True
