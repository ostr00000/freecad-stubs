import logging
from inspect import Parameter, formatannotation, Signature
from typing import Optional, Sequence

from freecad_stub_gen.util import OrderedSet

logger = logging.getLogger(__name__)


class RawRepr:
    __slots__ = 'values'

    def __new__(cls, *values):
        if len(values) == 1 and values[0] in (Parameter.empty, 'object'):
            return Parameter.empty
        return super().__new__(cls)

    def __init__(self, *values):
        self.values = OrderedSet(map(str, values))

    def __repr__(self):
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
            case _, (self.empty | 'object'):
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

    def __init__(self, parameters: Optional[Sequence[Parameter]] = None, *,
                 return_annotation=Signature.empty,
                 __validate_parameters__=True):

        if parameters is not None:
            if len(parameters) == 1:
                selfParam = parameters[0]
                if selfParam.name == 'self' and selfParam.kind == Parameter.POSITIONAL_ONLY:
                    parameters = list(parameters)
                    parameters[0] = selfParam.replace(kind=Parameter.POSITIONAL_OR_KEYWORD)
            elif len(parameters) >= 2:
                selfParam = parameters[0]
                secondParam = parameters[1]
                if (selfParam.name == 'self'
                        and selfParam.kind == Parameter.POSITIONAL_ONLY
                        and secondParam.kind == Parameter.POSITIONAL_OR_KEYWORD):
                    parameters = list(parameters)
                    parameters[0] = selfParam.replace(kind=Parameter.POSITIONAL_OR_KEYWORD)

        try:
            super().__init__(parameters, return_annotation=return_annotation,
                             __validate_parameters__=__validate_parameters__)
        except ValueError as v:
            if parameters is not None:
                logger.error(v)
                for p in parameters:
                    logger.error(f'{p} [{p.kind}]')
            raise
