import re

from freecad_stub_gen.generators.common.return_type_converter.arg_types import UnionArguments, \
    Empty, EmptyType
from freecad_stub_gen.generators.common.return_type_converter.base import ReturnTypeConverterBase


class ReturnTypeInnerList(ReturnTypeConverterBase):

    def getInnerType(self, varType: str | EmptyType, variableName: str, decStartPos: int,
                     decEndPos: int, endPos: int) -> str:
        if varType != 'list':
            return super().getInnerType(varType, variableName, decStartPos, decEndPos, endPos)

        innerTypes = self._getInnerTypeList(variableName, decEndPos, endPos)
        if not innerTypes:
            innerTypes = self._getInnerTypePyListSetItem(variableName, decEndPos, endPos)

        if innerTypes:
            varType += f'[{innerTypes}]'
            self.requiredImports.update(innerTypes.imports)

        return varType

    def _getInnerTypeList(self, variableName: str, startPos: int, endPos: int):
        regex = re.compile(rf'{variableName}\b.append\(([^;]*)\);')
        gen = self._genVariableTypeFromRegex(regex, startPos, endPos, onlyLiteral=False)
        return UnionArguments(gen)

    def _getInnerTypePyListSetItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `PyList_SetItem(pyList, i++, str);`."""
        arg = UnionArguments()
        regex = re.compile(rf'PyList_SetItem\s*\(\s*{variableName}\s*,\s*[\w+]+\s*,([^;]+)\);')
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            varType = self._getReturnTypeForText(variableMatch.group(1), endPos)
            assert varType != Empty
            arg.add(varType)
        return arg
