from dataclasses import dataclass
from inspect import Parameter
from typing import Any

from freecad_stub_gen.generators.common.annotation_parameter import (
    RawStringRepresentation,
)
from freecad_stub_gen.generators.common.arguments_converter.definitions import (
    UNKNOWN_DEFAULT_ARG,
)


@dataclass
class StackVal:
    objType: str
    pythonArgName: str
    default: Any


class SequenceStack:
    def __init__(self):
        self._values: list[list[StackVal]] = []

    def __bool__(self):
        return bool(self._values)

    def startSequenceParsing(self):
        self._values.append([])

    def addElementToSequence(self, objType: str, pythonArgName: str, default):
        self._values[-1].append(StackVal(objType, pythonArgName, default))

    def endSequenceParsing(self):
        stackVals = self._values.pop()
        # Probably in C this may be a `typing.Sequence`,
        # but at this moment in `typing` only a tuple support variable length.
        objType = f'tuple[{", ".join(s.objType for s in stackVals)}]'

        firstObjName = stackVals[0].pythonArgName
        if all(s.pythonArgName == firstObjName for s in stackVals):
            # if all sub arguments have the same name -> we use it (probably from kwargList)
            objName = firstObjName
        else:
            objName = '_'.join(s.pythonArgName for s in stackVals)

        if all(s.default is UNKNOWN_DEFAULT_ARG for s in stackVals):
            # we cannot decode it
            objDefault = UNKNOWN_DEFAULT_ARG
        elif all(s.default is Parameter.empty for s in stackVals):
            # there is no argument
            objDefault = Parameter.empty
        else:
            content = [
                'None' if s.default is UNKNOWN_DEFAULT_ARG else repr(s.default)
                for s in stackVals
            ]
            if len(content) == 1:
                content[0] = f'{content[0]},'
            objDefault = RawStringRepresentation(f'({", ".join(content)})')

        return objType, objName, objDefault
