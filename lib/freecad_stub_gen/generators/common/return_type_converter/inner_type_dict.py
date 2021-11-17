import re

from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar
from freecad_stub_gen.generators.common.return_type_converter.arg_types import EmptyType, \
    DictArgument, TypedDictGen
from freecad_stub_gen.generators.common.return_type_converter.base import ReturnTypeConverterBase


class ReturnTypeInnerDict(ReturnTypeConverterBase):
    def getInnerType(self, varType: str | EmptyType, variableName: str,
                     declarationStartPos: int, declarationEndPos: int, endPos: int) -> str:
        if varType != 'dict':
            return super().getInnerType(
                varType, variableName, declarationStartPos, declarationEndPos, endPos)

        da = self._getInnerTypePyDictSetItemString(variableName, declarationEndPos, endPos)
        if not da:
            da = self._getInnerTypePyDictSetItem(variableName, declarationEndPos, endPos)
        if not da:
            da = self._getInnerTypeDictSetItem(variableName, declarationEndPos, endPos)
        if not da:
            da = self._getInnerTypeDictAssignLiterals(variableName, declarationEndPos, endPos)
        if not da:
            da = self._getInnerTypeDictAssign(variableName, declarationEndPos, endPos)

        if not da:
            if 'PARAM_PY_DICT' in self.functionBody:
                return varType
            else:
                raise ValueError("Cannot extract dict inner types.")

        assert da
        varType = str(da)
        self.requiredImports.update(da.imports)
        return varType

    def _getInnerTypePyDictSetItemString(self, variableName: str, startPos: int, endPos: int):
        """Example: `PyDict_SetItemString(dict,It->first.c_str(), PyUnicode_FromString(It`"""
        da = DictArgument()
        regex = re.compile(rf'PyDict_SetItemString\s*\(\s*({variableName}\s*,[^;]*)\);')
        for match in regex.finditer(self.functionBody, startPos, endPos):
            funArgs = list(generateExpressionUntilChar(
                match.group(1), 0, ',', bracketL='(', bracketR=')'))
            value = self._getReturnTypeForText(funArgs[2], endPos)
            da.add('str', value)
        return da

    def _getInnerTypePyDictSetItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `PyDict_SetItem(pDict, pKey, pValue);`"""
        da = DictArgument()
        regex = re.compile(rf'PyDict_SetItem\s*\(\s*({variableName}\s*,[^;]*)\);')
        for match in regex.finditer(self.functionBody, startPos, endPos):
            funArgs = list(generateExpressionUntilChar(
                match.group(1), 0, ',', bracketL='(', bracketR=')'))
            key = self._getReturnTypeForText(funArgs[1], endPos)
            value = self._getReturnTypeForText(funArgs[2], endPos)
            da.add(key, value)
        return da

    def _getInnerTypeDictSetItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `dict.setItem(it->c_str(), list);`"""
        da = DictArgument()
        tdg = TypedDictGen(self.functionName)
        regex = re.compile(rf'{variableName}\b\.setItem\(([^;]*)\);')

        for match in regex.finditer(self.functionBody, startPos, endPos):
            funArgs = list(generateExpressionUntilChar(
                match.group(1), 0, ',', bracketL='(', bracketR=')'))

            value = self._getReturnTypeForText(funArgs[1], endPos)
            key = funArgs[0]
            if key.startswith('"') and key.endswith('"'):
                key = key.removeprefix('"').removesuffix('"')
                tdg.add(key, value)
            else:
                key = self._getReturnTypeForText(key, endPos)
                da.add(key, value)

        if tdg:
            return tdg
        return da

    def _getInnerTypeDictAssignLiterals(self, variableName: str, startPos: int, endPos: int):
        """Example: `ret["UserFriendlyName"] = strs[0];`"""
        tdg = TypedDictGen(self.functionName)
        regex = re.compile(rf'{variableName}\b\[\"(\w+)\"]\s*=\s*([^;]*);')
        for match in regex.finditer(self.functionBody, startPos, endPos):
            key = match.group(1)
            value = self._getReturnTypeForText(match.group(2), endPos)
            tdg.add(key, value)

        return tdg

    def _getInnerTypeDictAssign(self, variableName: str, startPos: int, endPos: int):
        """Example: `pyRM[AttachEngine::getModeName(rm.first)] = pyListOfCombinations;`"""
        da = DictArgument()
        regex = re.compile(rf'{variableName}\b\[(.*)]\s*=\s*([^;]*);')
        for match in regex.finditer(self.functionBody, startPos, endPos):
            key = self._getReturnTypeForText(match.group(1), endPos)
            value = self._getReturnTypeForText(match.group(2), endPos)
            da.add(key, value)
        return da
