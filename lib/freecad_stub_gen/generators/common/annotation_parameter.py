from __future__ import annotations

import logging
from collections.abc import Iterable, Sequence
from inspect import Parameter, formatannotation, Signature

from freecad_stub_gen.util import OrderedSet

logger = logging.getLogger(__name__)


class RawRepr:
    __slots__ = 'values'

    def __new__(cls, *values):
        match values:
            case () | (Parameter.empty | 'typing.Any', ):
                return Parameter.empty
        return super().__new__(cls)

    def __init__(self, *values):
        self.values = OrderedSet(map(str, values))

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

        elif isinstance(other, RawRepr):
            self.values.update(other.values)
            return self

        else:
            raise NotImplementedError


class AnnotationParam(Parameter):
    """Add annotation in __str__ method."""

    SELF_PARAM = Parameter('self', Parameter.POSITIONAL_ONLY)
    CLS_PARAM = Parameter('cls', Parameter.POSITIONAL_ONLY)
    ARGS_PARAM = Parameter('args', Parameter.VAR_POSITIONAL)

    @classmethod
    def getFirstParam(cls, isStaticMethod: bool, isClassMethod: bool) -> Parameter | None:
        if isStaticMethod:
            return
        elif isClassMethod:
            return cls.CLS_PARAM
        else:
            return cls.SELF_PARAM

    def __str__(self):
        # in current implementation (3.10) there is lack of annotation formatting
        match self.default, self.annotation:
            case self.empty, self.empty:
                formatted = self.name
            case self.empty, _:
                formatted = f'{self.name}: {formatannotation(self.annotation)}'
            case _, self.empty:
                formatted = f'{self.name}={repr(self.default)}'
            case _:
                formatted = f'{self.name}: {formatannotation(self.annotation)} = {repr(self.default)}'

        if (kind := self.kind) == self.VAR_POSITIONAL:
            formatted = '*' + formatted
        elif kind == self.VAR_KEYWORD:
            formatted = '**' + formatted

        return formatted


class SelfSignature(Signature):
    """Skip separator if there is only self parameter"""
    __slots__ = ('exceptions',)

    def __init__(self, parameters: Sequence[Parameter] | None = None, *,
                 return_annotation=Signature.empty, exceptions=(),
                 __validate_parameters__=True):

        match parameters:
            case [Parameter(name='self', kind=Parameter.POSITIONAL_ONLY) as selfParam]:
                pass
            case [Parameter(name='self', kind=Parameter.POSITIONAL_ONLY) as selfParam,
                  Parameter(kind=Parameter.POSITIONAL_OR_KEYWORD), *_]:
                pass
            case _:
                selfParam = None
        if selfParam is not None:
            parameters = list(parameters)
            parameters[0] = selfParam.replace(kind=Parameter.POSITIONAL_OR_KEYWORD)

        try:
            super().__init__(parameters, return_annotation=return_annotation,
                             __validate_parameters__=__validate_parameters__)
            self.exceptions: OrderedSet[str] | tuple[()] = exceptions
        except ValueError as v:
            if parameters is not None:
                logger.error(v)
                for p in parameters:
                    logger.error(f'{p} [{p.kind}]')
            raise

    @classmethod
    def getExceptionsDocs(cls, signatures: Iterable[SelfSignature]) -> str:
        uniqueExceptions = OrderedSet()
        for sig in signatures:
            uniqueExceptions.update(sig.exceptions)

        if not uniqueExceptions:
            return ''

        return f"\nPossible exceptions: ({', '.join(uniqueExceptions)})."
