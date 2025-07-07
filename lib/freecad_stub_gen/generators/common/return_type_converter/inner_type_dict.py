import re
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

from freecad_stub_gen.cpp_code.converters import removeQuote
from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar
from freecad_stub_gen.generators.common.return_type_converter.arg_types import (
    AnnotatedMarker,
    AnyValue,
    ComplexArgumentBase,
    DictArgument,
    RetType,
    TypedDictGen,
)
from freecad_stub_gen.generators.common.return_type_converter.base import (
    ReturnTypeConverterBase,
)

PAR = ParamSpec('PAR')
RET = TypeVar('RET')


def lazyDec[**PAR, RET](fun: Callable[PAR, RET]) -> Callable[PAR, Callable[[], RET]]:
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
            self._getInnerDictGetItem(variableName, decEndPos, endPos),
        ):
            da: ComplexArgumentBase = wrapper()
            if da:
                signature = da.formatPythonSignature()
                self.requiredImports.update(da.imports)
                return AnnotatedMarker(signature, self, variableName)

        if 'PARAM_PY_DICT' in self.functionBody:
            return AnnotatedMarker(varType, self, variableName)

        msg = 'Cannot extract dict inner types.'
        raise ValueError(msg)

    @lazyDec
    def _getInnerTypePyDictSetItemString(
        self, variableName: str, startPos: int, endPos: int
    ):
        """Extract parametrized type from `PyDict_SetItemString`.

        Example: `PyDict_SetItemString(pyDict, "name", strCmdName)`.
        """
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
        """Extract parametrized type from `PyDict_SetItem`.

        Example: `PyDict_SetItem(pDict, pKey, pValue);`.
        """
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
        """Extract parametrized type from `var.setItem(...)`.

        Example: `dict.setItem(it->c_str(), list);`.
        """
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
                keyLiteral = removeQuote(key)
                tdg.add(keyLiteral, value)
            else:
                keyVariable = self.getExpressionType(key, endPos)
                da.add(keyVariable, value)

        if tdg and da:
            msg = "Values in `TypedDict` are mixed with `dict`"
            raise ValueError(msg)
        if tdg:
            return tdg
        return da

    @lazyDec
    def _getInnerTypeDictAssignLiterals(
        self, variableName: str, startPos: int, endPos: int
    ):
        """Extract parametrized type from `var["a"] = y`.

        Example: `ret["UserFriendlyName"] = strs[0];`.
        """
        tdg = TypedDictGen(self.functionName)
        regex = re.compile(rf'{variableName}\b\[\"(\w+)\"]\s*=\s*([^;]*);')
        for match in regex.finditer(self.functionBody, startPos, endPos):
            key = match.group(1)
            value = self.getExpressionType(match.group(2), endPos)
            tdg.add(key, value)

        return tdg

    @lazyDec
    def _getInnerTypeDictAssign(self, variableName: str, startPos: int, endPos: int):
        """Extract parametrized type from `var[x] = y`.

        Example: `pyRM[AttachEngine::getModeName(rm.first)] = pyListOfCombinations;`.
        """
        da = DictArgument()
        regex = re.compile(rf'{variableName}\b\[(.*)]\s*=\s*([^;]*);')
        for match in regex.finditer(self.functionBody, startPos, endPos):
            key = self.getExpressionType(match.group(1), endPos)
            value = self.getExpressionType(match.group(2), endPos)
            da.add(key, value)
        return da

    @lazyDec
    def _getInnerDictGetItem(self, variableName: str, startPos: int, endPos: int):
        """Extract parametrized type from `y = var[x]`.

        Example: `auto value = ret[Py::String(v.index.appendToStringBuffer(s))];`
        """
        da = DictArgument()
        regex = re.compile(rf'(\w+)\s*=\s*{variableName}\s*\[\s*(.*)]\s*;')
        for match in regex.finditer(self.functionBody, startPos, endPos):
            try:
                value = self.getExpressionType(match.group(1), endPos)
            except RecursionError:
                # probably it would be better to have some flag for
                # `getExpressionType` to skip `dict` extraction
                value = AnyValue
            key = self.getExpressionType(match.group(2), endPos)
            da.add(key, value)
        return da
