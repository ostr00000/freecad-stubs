import re
from functools import wraps
from typing import ParamSpec, Callable, TypeVar

from freecad_stub_gen.cpp_code.converters import removeQuote
from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar
from freecad_stub_gen.generators.common.return_type_converter.arg_types import (
    DictArgument,
    TypedDictGen,
    ArgumentsIter,
    RetType,
)
from freecad_stub_gen.generators.common.return_type_converter.base import (
    ReturnTypeConverterBase,
)

PAR = ParamSpec('PAR')
RET = TypeVar('RET')


def lazyDec(fun: Callable[PAR, RET]) -> Callable[PAR, Callable[[], RET]]:
    @wraps(fun)
    def lazyInner(*args: PAR.args, **kwargs: PAR.kwargs):
        def callRequired():
            return fun(*args, **kwargs)

        return callRequired

    return lazyInner


class ReturnTypeInnerDict(ReturnTypeConverterBase):
    def getInnerType(
        self,
        varType: str,
        variableName: str,
        decStartPos: int,
        decEndPos: int,
        endPos: int,
    ) -> RetType:
        if varType != 'dict':
            return super().getInnerType(
                varType, variableName, decStartPos, decEndPos, endPos
            )

        for wrapper in (
            self._getInnerTypePyDictSetItemString(variableName, decEndPos, endPos),
            self._getInnerTypePyDictSetItem(variableName, decEndPos, endPos),
            self._getInnerTypeDictSetItem(variableName, decEndPos, endPos),
            self._getInnerTypeDictAssignLiterals(variableName, decEndPos, endPos),
            self._getInnerTypeDictAssign(variableName, decEndPos, endPos),
        ):
            da: ArgumentsIter = wrapper()
            if da:
                varType = str(da)
                self.requiredImports.update(da.imports)
                return varType

        if 'PARAM_PY_DICT' in self.functionBody:
            return varType

        raise ValueError("Cannot extract dict inner types.")

    @lazyDec
    def _getInnerTypePyDictSetItemString(
        self, variableName: str, startPos: int, endPos: int
    ):
        """Example: `PyDict_SetItemString(dict,It->first.c_str(), PyUnicode_FromString(It`"""
        da = DictArgument()
        regex = re.compile(rf'PyDict_SetItemString\s*\(\s*({variableName}\s*,[^;]*)\);')
        for match in regex.finditer(self.functionBody, startPos, endPos):
            funArgs = list(
                generateExpressionUntilChar(
                    match.group(1), 0, ',', bracketL='(', bracketR=')'
                )
            )
            value = self.getExpressionType(funArgs[2], endPos)
            da.add('str', value)
        return da

    @lazyDec
    def _getInnerTypePyDictSetItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `PyDict_SetItem(pDict, pKey, pValue);`"""
        da = DictArgument()
        regex = re.compile(rf'PyDict_SetItem\s*\(\s*({variableName}\s*,[^;]*)\);')
        for match in regex.finditer(self.functionBody, startPos, endPos):
            funArgs = list(
                generateExpressionUntilChar(
                    match.group(1), 0, ',', bracketL='(', bracketR=')'
                )
            )
            key = self.getExpressionType(funArgs[1], endPos)
            value = self.getExpressionType(funArgs[2], endPos)
            da.add(key, value)
        return da

    @lazyDec
    def _getInnerTypeDictSetItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `dict.setItem(it->c_str(), list);`"""
        da = DictArgument()
        tdg = TypedDictGen(self.functionName)
        regex = re.compile(rf'{variableName}\b\.setItem\(([^;]*)\);')

        for match in regex.finditer(self.functionBody, startPos, endPos):
            funArgs = list(
                generateExpressionUntilChar(
                    match.group(1), 0, ',', bracketL='(', bracketR=')'
                )
            )

            value = self.getExpressionType(funArgs[1], endPos)
            key = funArgs[0]
            if key.startswith('"') and key.endswith('"'):
                tKey = removeQuote(key)
                tdg.add(tKey, value)
            else:
                tKey = self.getExpressionType(key, endPos)
                da.add(tKey, value)

        if tdg:
            assert not da, "Values in `TypedDict` are mixed with `dict`"
            return tdg
        return da

    @lazyDec
    def _getInnerTypeDictAssignLiterals(
        self, variableName: str, startPos: int, endPos: int
    ):
        """Example: `ret["UserFriendlyName"] = strs[0];`"""
        tdg = TypedDictGen(self.functionName)
        regex = re.compile(rf'{variableName}\b\[\"(\w+)\"]\s*=\s*([^;]*);')
        for match in regex.finditer(self.functionBody, startPos, endPos):
            key = match.group(1)
            value = self.getExpressionType(match.group(2), endPos)
            tdg.add(key, value)

        return tdg

    @lazyDec
    def _getInnerTypeDictAssign(self, variableName: str, startPos: int, endPos: int):
        """Example: `pyRM[AttachEngine::getModeName(rm.first)] = pyListOfCombinations;`"""
        da = DictArgument()
        regex = re.compile(rf'{variableName}\b\[(.*)]\s*=\s*([^;]*);')
        for match in regex.finditer(self.functionBody, startPos, endPos):
            key = self.getExpressionType(match.group(1), endPos)
            value = self.getExpressionType(match.group(2), endPos)
            da.add(key, value)
        return da
