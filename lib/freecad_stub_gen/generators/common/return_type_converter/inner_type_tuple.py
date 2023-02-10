import re

from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar
from freecad_stub_gen.generators.common.return_type_converter.arg_types import TupleArgument, \
    RetType
from freecad_stub_gen.generators.common.return_type_converter.base import ReturnTypeConverterBase


class ReturnTypeInnerTuple(ReturnTypeConverterBase):

    def getInnerType(self, varType: str, variableName: str, decStartPos: int,
                     decEndPos: int, endPos: int) -> RetType:
        if varType != 'tuple':
            return super().getInnerType(varType, variableName, decStartPos, decEndPos, endPos)

        for gen in (
                self._genInnerTypeTupleConstructorWithoutAssignment(decStartPos, decEndPos),
                self._genInnerTypeTupleSetItem(variableName, decEndPos, endPos),
                self._genInnerTypePyTupleSetItem(variableName, decEndPos, endPos),
                self._genInnerTypeTupleAssignItem(variableName, decEndPos, endPos),
                self._genInnerTypeTupleConstructor(variableName, decStartPos, endPos),
        ):
            if tupleArg := TupleArgument(gen):
                varType = str(tupleArg)
                self.requiredImports.update(tupleArg.imports)
                return varType

        raise ValueError("Cannot find inner type for tuple")

    def _genInnerTypeTupleConstructorWithoutAssignment(self, startPos: int, endPos: int):
        """Py::TupleN(Py::Object(v.first->getPyObject(),true),Py::String(v.second))"""
        regex = re.compile(r'TupleN\s*\(([^;]+)\)')
        if match := regex.search(self.functionBody, startPos, endPos):
            funArgs = list(generateExpressionUntilChar(
                match.group(1), 0, ',', bracketL='(', bracketR=')'))
            for arg in funArgs:
                yield self.getExpressionType(arg, endPos=endPos)

    def _genInnerTypeTupleSetItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `list.setItem(0, Py::Float(7.0));`"""
        variableLengthTuple = True
        regex = re.compile(rf'{variableName}\.setItem\(([^;]+)\);')
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            funArgs = list(generateExpressionUntilChar(
                variableMatch.group(1), 0, ',', bracketL='(', bracketR=')'))
            variableLengthTuple &= not funArgs[0].isnumeric()
            yield self.getExpressionType(funArgs[1], endPos)
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
        (?P<value>[^;]+)    # tuple value,
        \);                 # end function or macro call
        """, re.VERBOSE)
        variableLengthTuple = True
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            variableLengthTuple &= not variableMatch.group('index').isnumeric()
            yield self.getExpressionType(variableMatch.group('value'), endPos)
        return variableLengthTuple

    def _genInnerTypeTupleAssignItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `list[0] = Py::Float(7.0)`"""
        regex = re.compile(rf"""
        {variableName}      # tuple variable name
        \s*\[\s*            # indexing start
        (?P<index>          # position index
            \w+             # number or variable
            (?:\+\+)?       # optional incrementing
        )      
        \s*]\s*=\s*         # indexing end
        (?P<value>[^;]+)    # tuple value
        ;""", re.VERBOSE)
        variableLengthTuple = True
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            variableLengthTuple &= not variableMatch.group('index').isnumeric()
            yield self.getExpressionType(variableMatch.group('value'), endPos)
        return variableLengthTuple

    def _genInnerTypeTupleConstructor(self, variableName: str, startPos: int, endPos: int):
        """Example: `Py::TupleN list(Py::Float(7.0), Py::Float(7.0));`"""
        regex = re.compile(rf'TupleN\s+{variableName}\s*\(([^;]+)\);')
        if match := regex.search(self.functionBody, startPos, endpos=endPos):
            funArgs = list(generateExpressionUntilChar(
                match.group(1), 0, ',', bracketL='(', bracketR=')'))
            for fa in funArgs:
                yield self.getExpressionType(fa, endPos)
