from __future__ import annotations

import logging
from collections.abc import Iterable, Mapping, Sequence
from inspect import Parameter, Signature, _empty, _void
from typing import cast

from freecad_stub_gen.ordered_set import OrderedStrSet
from freecad_stub_gen.python_code import indent

logger = logging.getLogger(__name__)


class RawRepr:
    """By default inspect.Signature uses."""

    __slots__ = ('values',)

    def __new__(cls, *values):
        match values:
            case () | (Parameter.empty | 'typing.Any',):
                return Parameter.empty
        return super().__new__(cls)

    def __init__(self, *values):
        self.values = OrderedStrSet(map(str, values))

    def __repr__(self):
        if 'None' in self.values:
            self.values.pop('None')
            self.values.add('None')
        return ' | '.join(self.values)

    def __eq__(self, other):
        if isinstance(other, str) and len(self.values) == 1:
            return other == self.values.first()
        return super().__eq__(other)

    def __add__(self, other: str | RawRepr):
        match other:
            case str(s):
                self.values.add(s)
            case RawRepr() as r:
                self.values.update(r.values)
            case _:
                raise NotImplementedError
        return self


class RawStringRepresentation(str):
    __slots__ = ()

    def __repr__(self):
        return str(self)


class AnnotationParam(Parameter):
    """Add annotation in __str__ method."""

    SELF_PARAM = Parameter('self', Parameter.POSITIONAL_ONLY)
    CLS_PARAM = Parameter('cls', Parameter.POSITIONAL_ONLY)
    ARGS_PARAM = Parameter('args', Parameter.VAR_POSITIONAL)

    @classmethod
    def getFirstParam(
        cls, *, isStaticMethod: bool, isClassMethod: bool
    ) -> Parameter | None:
        if isStaticMethod:
            return None

        if isClassMethod:
            return cls.CLS_PARAM

        return cls.SELF_PARAM


type InitParameters_t = Sequence[Parameter] | None
type ReplaceParameters_t = InitParameters_t | Mapping[str, Parameter] | type[_void]


class SelfSignature(Signature):
    """Skip separator if there is only self parameter."""

    __slots__ = ('exceptions', 'unknown_parameters')

    def __init__(
        self,
        parameters: InitParameters_t = None,
        *,
        unknown_parameters: bool = False,
        return_annotation: RawRepr | type[_empty] = Signature.empty,
        exceptions: OrderedStrSet | None = None,
    ):
        parameters = self._convertFirstParam(parameters)
        try:
            super().__init__(parameters, return_annotation=return_annotation)
            self.exceptions = OrderedStrSet() if exceptions is None else exceptions
            self.unknown_parameters = unknown_parameters
        except ValueError:
            if parameters is not None:
                paramsStr = '\n'.join(indent(f'{p} [{p.kind}]') for p in parameters)
                msg = f"Cannot create signature with provided parameters:\n{paramsStr}"
                logger.exception(msg)

            raise

    @classmethod
    def _convertFirstParam(cls, parameters: InitParameters_t) -> InitParameters_t:
        match parameters:
            case [Parameter(name='self', kind=Parameter.POSITIONAL_ONLY) as selfParam]:
                pass
            case [
                Parameter(name='self', kind=Parameter.POSITIONAL_ONLY) as selfParam,
                Parameter(kind=Parameter.POSITIONAL_OR_KEYWORD),
                *_,
            ]:
                pass
            case _:
                return parameters

        parameters = list(parameters)
        parameters[0] = selfParam.replace(kind=Parameter.POSITIONAL_OR_KEYWORD)
        return parameters

    @classmethod
    def getExceptionsDocs(cls, signatures: Iterable[SelfSignature]) -> str:
        uniqueExceptions = OrderedStrSet()
        for sig in signatures:
            uniqueExceptions.update(sig.exceptions)

        if not uniqueExceptions:
            return ''

        return f"\nPossible exceptions: ({', '.join(uniqueExceptions)})."

    __void = _void  # only to access in pattern matching

    def replace(
        self,
        *,
        parameters: ReplaceParameters_t = _void,
        return_annotation: RawRepr | type[_void] = _void,
        exceptions: OrderedStrSet | type[_void] = _void,
        unknown_parameters: bool | type[_void] = _void,
    ) -> SelfSignature:
        initParameters: InitParameters_t
        match parameters:
            case self.__void:
                initParameters = list(self.parameters.values())
            case Mapping():
                initParameters = list(parameters.values())
            case _:
                initParameters = cast(InitParameters_t, parameters)

        if isinstance(return_annotation, RawRepr):
            retAnnotation = return_annotation
        else:
            retAnnotation = self.return_annotation

        if isinstance(exceptions, OrderedStrSet):
            initExc = exceptions
        else:
            initExc = self.exceptions

        if isinstance(unknown_parameters, bool):
            unknownParams = unknown_parameters
        else:
            unknownParams = self.unknown_parameters

        return type(self)(
            initParameters,
            unknown_parameters=unknownParams,
            return_annotation=retAnnotation,
            exceptions=initExc,
        )
