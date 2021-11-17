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
        variableLengthTuple = True
        regex = re.compile(rf'{variableName}\.setItem\(([^;]+)\);')
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            funArgs = list(generateExpressionUntilChar(
                variableMatch.group(1), 0, ',', bracketL='(', bracketR=')'))
            variableLengthTuple &= not funArgs[0].isnumeric()
            yield self._getReturnTypeForText(funArgs[1], endPos)
        return variableLengthTuple

    def _genInnerTypePyTupleSetItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `PyTuple_SetItem(t, 1, Py::new_reference_to( Py::Float(c.g) ));`"""
        regex = re.compile(rf"""
        PyTuple_(?:SetItem|SET_ITEM)
        \s*\(\s*            # function or macro call
        {variableName}      # tuple variable name, 
        \s*,\s*             # next arg,
        (?P<index>[\w+]+)   # position index,
        \s*,\s*             # next arg,
        (?P<value>[^;]+)    # tuple value. 
        \);                 # end function or macro call
        """, re.VERBOSE)
        variableLengthTuple = True
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            variableLengthTuple &= not variableMatch.group('index').isnumeric()
            yield self._getReturnTypeForText(variableMatch.group('value'), endPos)
        return variableLengthTuple

    def _genInnerTypeTupleAssignItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `list[0] = Py::Float(7.0)`"""
        regex = re.compile(rf"""
        {variableName}      # tuple variable name
        \s*\[\s*            # indexing start
        (?P<index>\w+)      # position index
        \s*]\s*=\s*         # indexing end
        (?P<value>[^;]+)    # tuple value
        ;""", re.VERBOSE)
        variableLengthTuple = True
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            variableLengthTuple &= not variableMatch.group('index').isnumeric()
            yield self._getReturnTypeForText(variableMatch.group('value'), endPos)
        return variableLengthTuple

    def _genInnerTypeTupleConstructor(self, variableName: str, startPos: int, endPos: int):
        """Example: `Py::TupleN list(Py::Float(7.0), Py::Float(7.0));`"""
        regex = re.compile(rf'TupleN\s*{variableName}\s*\(([^;]+)\);')
        if match := regex.search(self.functionBody, startPos, endpos=endPos):
            funArgs = list(generateExpressionUntilChar(
                match.group(1), 0, ',', bracketL='(', bracketR=')'))
            for fa in funArgs:
                yield self._getReturnTypeForText(fa, endPos)
