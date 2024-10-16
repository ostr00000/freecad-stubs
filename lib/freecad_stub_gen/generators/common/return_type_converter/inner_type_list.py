import logging
import re

from freecad_stub_gen.generators.common.return_type_converter.arg_types import (
    AnnotatedMarker,
    AnyValue,
    RetType,
    UnionArgument,
)
from freecad_stub_gen.generators.common.return_type_converter.base import (
    ReturnTypeConverterBase,
)

logger = logging.getLogger(__name__)


class ReturnTypeInnerList(ReturnTypeConverterBase):
    def getInnerType(
        self,
        varType: str,
        variableName: str,
        decStartPos: int,
        decEndPos: int,
        endPos: int,
    ) -> RetType:
        if varType != 'list':
            return super().getInnerType(
                varType, variableName, decStartPos, decEndPos, endPos
            )

        innerTypes = self._getInnerTypeList(variableName, decEndPos, endPos)
        if not innerTypes:
            innerTypes = self._getInnerTypePyListSetItem(
                variableName, decEndPos, endPos
            )

        if innerTypes:
            varType += f'[{innerTypes}]'
            self.requiredImports.update(innerTypes.imports)

        return AnnotatedMarker(varType, self, lookupType=variableName)

    def _getInnerTypeList(self, variableName: str, startPos: int, endPos: int):
        regex = re.compile(rf'{variableName}\b.append\(([^;]*)\);')
        gen = self._genVariableTypeFromRegex(regex, startPos, endPos, onlyLiteral=False)
        return UnionArgument(gen)

    def _getInnerTypePyListSetItem(self, variableName: str, startPos: int, endPos: int):
        """Extract parametrized type from `PyList_SetItem`.

        Example: `PyList_SetItem(pyList, i++, str);`.
        """
        arg = UnionArgument()
        regex = re.compile(
            rf'PyList_SetItem\s*\(\s*{variableName}\s*,\s*[\w+]+\s*,([^;]+)\);'
        )
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            varName = variableMatch.group(1)
            varType = self.getExpressionType(varName, endPos)
            if varType == AnyValue:
                raise ValueError
            arg.add(varType)
        return arg
