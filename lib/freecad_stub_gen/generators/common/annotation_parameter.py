from __future__ import annotations

import logging
from collections.abc import Mapping, Iterable, Sequence
from inspect import Parameter, Signature, _void
from typing import cast, TypeAlias

from freecad_stub_gen.ordered_set import OrderedStrSet

logger = logging.getLogger(__name__)


class RawRepr:
    __slots__ = ('values',)

    def __new__(cls, *values):
        match values:
            case () | (Parameter.empty | 'typing.Any', ):
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

    def __add__(self, other):
        if isinstance(other, str):
            self.values.add(other)
            return self

        if isinstance(other, RawRepr):
            self.values.update(other.values)
            return self

        raise NotImplementedError


class RawStringRepresentation(str):
    def __repr__(self):
        return str(self)


class AnnotationParam(Parameter):
    """Add annotation in __str__ method."""

    SELF_PARAM = Parameter('self', Parameter.POSITIONAL_ONLY)
    CLS_PARAM = Parameter('cls', Parameter.POSITIONAL_ONLY)
    ARGS_PARAM = Parameter('args', Parameter.VAR_POSITIONAL)

    @classmethod
    def getFirstParam(cls, isStaticMethod: bool, isClassMethod: bool) -> Parameter | None:
        if isStaticMethod:
            return None

        if isClassMethod:
            return cls.CLS_PARAM

        return cls.SELF_PARAM


InitParameters_t: TypeAlias = Sequence[Parameter] | None
ReplaceParameters_t: TypeAlias = Sequence[Parameter] | type[_void] | None


class SelfSignature(Signature):
    """Skip separator if there is only self parameter"""
    __slots__ = ('exceptions', 'unknown_parameters')

    def __init__(self, parameters: InitParameters_t = None, *,
                 unknown_parameters=False,
                 return_annotation=Signature.empty,
                 exceptions: OrderedStrSet | None = None,
                 ):
        parameters = self._convertFirstParam(parameters)
        try:
            super().__init__(parameters, return_annotation=return_annotation)
            self.exceptions = OrderedStrSet() if exceptions is None else exceptions
            self.unknown_parameters = unknown_parameters
        except ValueError as v:
            if parameters is not None:
                logger.error(v)
                for p in parameters:
                    logger.error(f'{p} [{p.kind}]')
            raise

    @staticmethod
    def _convertFirstParam(parameters: InitParameters_t) -> InitParameters_t:
        match parameters:
            case [Parameter(name='self', kind=Parameter.POSITIONAL_ONLY) as selfParam]:
                pass
            case [Parameter(name='self', kind=Parameter.POSITIONAL_ONLY) as selfParam,
                  Parameter(kind=Parameter.POSITIONAL_OR_KEYWORD), *_]:
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

    def replace(self, *, parameters: ReplaceParameters_t | Mapping[str, Parameter] = _void,
                return_annotation=_void,
                exceptions=_void,
                unknown_parameters=_void,
                ) -> SelfSignature:
        initParameters: InitParameters_t
        match parameters:
            case self.__void:
                initParameters = list(self.parameters.values())
            case Mapping():
                initParameters = list(parameters.values())
            case _:
                initParameters = cast(InitParameters_t, parameters)

        if return_annotation is _void:
            return_annotation = self.return_annotation
        if exceptions is _void:
            exceptions = self.exceptions
        if unknown_parameters is _void:
            unknown_parameters = self.unknown_parameters

        return type(self)(
            initParameters,
            unknown_parameters=unknown_parameters,
            return_annotation=return_annotation,
            exceptions=exceptions,
        )
