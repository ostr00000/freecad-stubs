import re

from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar
from freecad_stub_gen.generators.common.return_type_converter.arg_types import EmptyType, \
    TupleArgument
from freecad_stub_gen.generators.common.return_type_converter.base import ReturnTypeConverterBase


class ReturnTypeInnerTuple(ReturnTypeConverterBase):

    def getInnerType(self, varType: str | EmptyType, variableName: str,
                     declarationStartPos: int, declarationEndPos: int, endPos: int) -> str:
        if varType != 'tuple':
            return super().getInnerType(
                varType, variableName, declarationStartPos, declarationEndPos, endPos)

        listTypes = TupleArgument(self._genInnerTypeTupleSetItem(
            variableName, declarationEndPos, endPos))
        if not listTypes:
            listTypes = TupleArgument(self._genInnerTypePyTupleSetItem(
                variableName, declarationEndPos, endPos))
        if not listTypes:
            listTypes = TupleArgument(self._genInnerTypeTupleAssignItem(
                variableName, declarationEndPos, endPos))
        if not listTypes:
            listTypes = TupleArgument(self._genInnerTypeTupleConstructor(
                variableName, declarationStartPos, endPos))

        assert listTypes, "Cannot find inner type for tuple"
        varType = str(listTypes)
        self.requiredImports.update(listTypes.imports)
        return varType

    def _genInnerTypeTupleSetItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `list.setItem(0, Py::Float(7.0));`"""
        regex = re.compile(rf'{variableName}\.setItem\(([^;]+)\);')
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            funArgs = list(generateExpressionUntilChar(
                variableMatch.group(1), 0, ',', bracketL='(', bracketR=')'))
            yield self._getReturnTypeForText(funArgs[1], endPos)

    def _genInnerTypePyTupleSetItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `PyTuple_SetItem(t, 1, Py::new_reference_to( Py::Float(c.g) ));`"""
        regex = re.compile(rf'PyTuple_SetItem\s*\(\s*{variableName}\s*,\s*[\w+]+\s*,([^;]+)\);')
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            yield self._getReturnTypeForText(variableMatch.group(1), endPos)

    def _genInnerTypeTupleAssignItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `list[0] = Py::Float(7.0)`"""
        regex = re.compile(rf'{variableName}\s*\[\s*\d+\s*]\s*=\s*([^;]+);')
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            yield self._getReturnTypeForText(variableMatch.group(1), endPos)

    def _genInnerTypeTupleConstructor(self, variableName: str, startPos: int, endPos: int):
        """Example: `Py::TupleN list(Py::Float(7.0), Py::Float(7.0));`"""
        regex = re.compile(rf'TupleN\s*{variableName}\s*\(([^;]+)\);')
        if match := regex.search(self.functionBody, startPos, endpos=endPos):
            funArgs = list(generateExpressionUntilChar(
                match.group(1), 0, ',', bracketL='(', bracketR=')'))
            for fa in funArgs:
                yield self._getReturnTypeForText(fa, endPos)
