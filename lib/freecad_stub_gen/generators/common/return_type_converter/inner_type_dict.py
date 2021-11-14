from freecad_stub_gen.generators.common.return_type_converter.arg_types import EmptyType
from freecad_stub_gen.generators.common.return_type_converter.base import ReturnTypeConverterBase


class ReturnTypeInnerDict(ReturnTypeConverterBase):
    def getInnerType(self, varType: str | EmptyType, variableName: str,
                     declarationStartPos: int, declarationEndPos: int, endPos: int) -> str:
        if varType != 'dict':
            return super().getInnerType(
                varType, variableName, declarationStartPos, declarationEndPos, endPos)

        return varType  # TODO P2 add dict types
