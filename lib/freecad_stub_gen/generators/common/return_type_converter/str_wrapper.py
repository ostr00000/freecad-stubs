from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class AffixCmp:
    class AffixType(Enum):
        PREFIX = auto()
        INFIX = auto()
        SUFFIX = auto()

    text: str
    affixType: AffixType

    def __eq__(self, other):
        if not isinstance(other, str):
            return False
        match self.affixType:
            case self.AffixType.PREFIX:
                return self.text.startswith(other)
            case self.AffixType.SUFFIX:
                return self.text.endswith(other)
            case self.AffixType.INFIX:
                return other in self.text
            case _:
                raise NotImplementedError

    def __str__(self):
        return self.text


class StrWrapperMeta(type):
    def __call__(cls, *args, **kwargs):
        if len(args) == 1:
            val = args[0]
            if isinstance(val, StrWrapper):
                return val
        return super().__call__(*args, **kwargs)


class StrWrapper(str, metaclass=StrWrapperMeta):
    __slots__ = ()
    __match_args__ = ('start', 'contain', 'end')

    @property
    def start(self):
        return AffixCmp(self, AffixCmp.AffixType.PREFIX)

    @property
    def contain(self):
        return AffixCmp(self, AffixCmp.AffixType.INFIX)

    @property
    def end(self):
        return AffixCmp(self, AffixCmp.AffixType.SUFFIX)
