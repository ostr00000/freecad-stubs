from dataclasses import dataclass
from enum import Enum, auto
from functools import cached_property


@dataclass
class AffixCmp:
    class AffixType(Enum):
        PREFIX = auto()
        INFIX = auto()
        SUFFIX = auto()

    text: str
    type: AffixType

    def __eq__(self, other: str):
        match self.type:
            case self.AffixType.PREFIX:
                return self.text.startswith(other)
            case self.AffixType.SUFFIX:
                return self.text.endswith(other)
            case self.AffixType.INFIX:
                return other in self.text
            case _:
                raise NotImplementedError


class StrWrapper(str):
    __match_args__ = ('start', 'contain', 'end')

    @cached_property
    def start(self):
        return AffixCmp(self, AffixCmp.AffixType.PREFIX)

    @cached_property
    def contain(self):
        return AffixCmp(self, AffixCmp.AffixType.INFIX)

    @cached_property
    def end(self):
        return AffixCmp(self, AffixCmp.AffixType.SUFFIX)
