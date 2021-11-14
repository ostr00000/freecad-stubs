import re
from dataclasses import dataclass
from enum import auto, Enum
from functools import cached_property
from inspect import Signature

from freecad_stub_gen.generators.common.annotation_parameter import RawRepr
from freecad_stub_gen.generators.common.arguments_converter import logger
from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.common.names import getClassWithModulesFromPointer, \
    getModuleName, getClassName
from freecad_stub_gen.generators.common.py_build_converter import parsePyBuildValues
from freecad_stub_gen.util import OrderedSet


class _EmptyType:
    @property
    def value(self):
        return self

    def __eq__(self, other):
        return other is None or other == 'object'

    def __hash__(self):
        return 1

    def __str__(self):
        return 'object'


EmptyType = _EmptyType()


class ArgumentsIter:
    @cached_property
    def imports(self):
        return OrderedSet()

    def __iter__(self):
        """
        Cannot inherit this class from Iterable/Iterator
        because super() will not find correct class.
        """
        for argType in super().__iter__():
            match argType:
                case str() if '[' not in argType and (mod := getModuleName(argType)):
                    self.imports.add(mod)
                case UnionArguments() as ua:
                    self.imports.update(ua.imports)
            yield str(argType)


class UnionArguments(ArgumentsIter, OrderedSet):
    def __str__(self):
        return ' | '.join(self)


class TupleArgument(ArgumentsIter, list):
    def __str__(self):
        if self:
            return f'tuple[{", ".join(self)}]'
        return 'tuple'


RetType = UnionArguments[str] | _EmptyType | str


@dataclass
class AffixCmp:
    class AffixType(Enum):
        PREFIX = auto()
        INFIX = auto()
        SUFFIX = auto()

    text: str
    type: AffixType

    def __eq__(self, other: str):
        match self.type:
            case self.AffixType.PREFIX:
                return self.text.startswith(other)
            case self.AffixType.SUFFIX:
                return self.text.endswith(other)
            case self.AffixType.INFIX:
                return other in self.text
            case _:
                raise NotImplementedError


class StrWrapper(str):
    __match_args__ = ('start', 'contain', 'end')

    @cached_property
    def start(self):
        return AffixCmp(self, AffixCmp.AffixType.PREFIX)

    @cached_property
    def contain(self):
        return AffixCmp(self, AffixCmp.AffixType.INFIX)

    @cached_property
    def end(self):
        return AffixCmp(self, AffixCmp.AffixType.SUFFIX)


class InvalidReturnType(ValueError):
    pass


class ReturnTypeConverter:
    REG_RETURN = re.compile(r'return ([^;]+);')

    def __init__(self, requiredImports: OrderedSet, functionBody: str,
                 classNameWithModule: str, functionName: str = None):
        self.requiredImports = requiredImports
        self.functionBody = functionBody
        self.classNameWithModule = classNameWithModule
        self.functionName = functionName

    @cached_property
    def className(self):
        return getClassName(self.classNameWithModule)

    def getReturnType(self):
        returnTypes = OrderedSet(self._genReturnType())
        if not returnTypes:
            return Signature.empty
        return RawRepr(*returnTypes)

    def _genReturnType(self):
        for match in self.REG_RETURN.finditer(self.functionBody):
            try:
                retType = self._getReturnTypeForText(match.group(1), match.end())
            except InvalidReturnType:
                continue
            if not isinstance(retType, UnionArguments):
                retType = UnionArguments((retType,))
            yield from retType
            self.requiredImports.update(retType.imports)

    def _getReturnTypeForText(self, returnText: str, endPos: int, onlyLiteral=False) -> RetType:
        returnText = returnText.strip()
        if returnText.endswith(')') \
                and (returnText.startswith('new_reference_to(')
                     or returnText.startswith('Py::new_reference_to(')):
            returnText = returnText \
                .removeprefix('Py::') \
                .removeprefix('new_reference_to(') \
                .removesuffix(')').strip()

        if returnText.startswith('*'):
            returnText = returnText.removeprefix('*').strip()

        match StrWrapper(returnText):
            case '':
                return EmptyType
            case 'Py::Object()':
                # we must use `Union` wrapper,
                # otherwise `object` may be ignored if there are no other types
                return 'typing.Union[object]'
            case 'Py_None' | 'Py::None()' | 'Py_Return':
                return 'None'
            case '0' | '-1' | 'NULL' | 'nullptr' | '0L':
                if onlyLiteral:
                    return EmptyType
                else:
                    raise InvalidReturnType

            case 'getDocumentObjectPtr()':
                return 'FreeCAD.DocumentObject'

            case StrWrapper('Py::Boolean' | 'PyBool_From' | 'Py::True' | 'Py::False'):
                return 'bool'
            case StrWrapper('Py::Long' | 'PyLong_From' | 'Py::Int' | 'PyInt_From'):
                return 'int'
            case StrWrapper('Py::Float' | 'PyFloat_From'):
                return 'float'
            case StrWrapper('Py::String' | 'PyUnicode_From' | 'PyUnicode_DecodeUTF8'):
                return 'str'
            case StrWrapper('Py::Tuple' | 'PyTuple_New'):
                return 'tuple'
            case StrWrapper('Py::List' | 'PyList_New'):
                return 'list'
            case StrWrapper('Py::Dict' | 'PyDict_New'):
                return 'dict'
            case StrWrapper('Py::Callable'):
                return 'typing.Callable'

            # PyCXX wrapper classes, search for `typedef GeometryT<`
            case StrWrapper('Py::BoundingBox'):
                return 'FreeCAD.BoundingBox'
            case StrWrapper('Py::Matrix'):
                return 'FreeCAD.Matrix'
            case StrWrapper('Py::Rotation'):
                return 'FreeCAD.Rotation'
            case StrWrapper('Py::Placement'):
                return 'FreeCAD.Placement'
            # typedef PythonClassObject<Base::Vector2dPy> Vector2d;
            case StrWrapper('Py::Vector2d'):
                return 'FreeCAD.Vector2d'
            case StrWrapper('Py::Vector'):
                return 'FreeCAD.Vector'

            case StrWrapper('shape2pyshape' | 'Part::shape2pyshape'):
                return 'Part.Shape'

            case StrWrapper('wrap.fromQObject('):
                return 'qtpy.QtCore.QObject'
            case StrWrapper('wrap.fromQWidget('):
                fc = findFunctionCall(
                    returnText, bodyStart=returnText.find('('),
                    bracketL='(', bracketR=')').removeprefix('(').removesuffix(')')
                funArgs = list(generateExpressionUntilChar(
                    fc, 0, ',', bracketL='(', bracketR=')'))
                assert len(funArgs) == 2
                widgetType = funArgs[1].strip().removeprefix('"').removesuffix('"')
                return f'qtpy.QtWidgets.{widgetType}'
            case StrWrapper('wrap.fromQIcon('):
                return 'qtpy.QtGui.QIcon'

            case StrWrapper('PyRun_String'):
                return EmptyType

            case StrWrapper('new ' | 'Py::asObject(new '):
                return self._findClassWithModule(returnText)
            case StrWrapper(end='Py') as i if i.isidentifier() and i[0].isupper():
                return self._findClassWithModule(returnText)

            case StrWrapper(end='->getPyObject()' | '.getPyObject()'):
                expText = returnText \
                    .removesuffix('getPyObject()') \
                    .removesuffix('.') \
                    .removesuffix('->') \
                    .removesuffix(')')
                varTextStartPos = expText.rfind('(') + 1
                varText = expText[varTextStartPos:]
                return self._getReturnTypeForText(varText, endPos=endPos)

            case StrWrapper('Py_BuildValue("'):
                fc = findFunctionCall(
                    returnText, bodyStart=len('Py_BuildValue'), bracketL='(', bracketR=')',
                ).removeprefix('(').removesuffix(')')
                funArgs = list(generateExpressionUntilChar(
                    fc, 0, ',', bracketL='(', bracketR=')'))
                formatText = funArgs[0].removeprefix('"').removesuffix('"')
                if pythonType := parsePyBuildValues(formatText):
                    if pythonType == EmptyType:
                        objArg = funArgs[1].strip()
                        pythonType = self._getReturnTypeForText(objArg, endPos, onlyLiteral=True)
                    return pythonType

            case StrWrapper(contain='Py_True' | 'Py_False'):
                # must be before identifier and should be after Py_BuildValue
                return 'bool'

            case StrWrapper('Py::asObject(' | 'Py::Object('):
                fc = findFunctionCall(
                    returnText, bodyStart=returnText.find('('),
                    bracketL='(', bracketR=')').removeprefix('(').removesuffix(')')
                funArgs = list(generateExpressionUntilChar(
                    fc, 0, ',', bracketL='(', bracketR=')'))
                rawReturnVarName = funArgs[0]
                return self._getReturnTypeForText(rawReturnVarName, endPos)

            case _ if onlyLiteral:
                if all(i.isidentifier() for i in returnText.split('::')):
                    maybeClass = f'{returnText}Py'
                    return self._findClassWithModule(maybeClass, mustDiffer=returnText)
                return EmptyType

            case _ if returnText.isidentifier():
                return self._findVariableType(returnText, endPos)

            case StrWrapper('(', end=')'):
                return self._getReturnTypeForText(
                    returnText.removeprefix('(').removesuffix(')'), endPos, onlyLiteral)

            case StrWrapper(contain='=='):
                return 'bool'

            case _:
                logger.warning(f"Unknown return variable: '{returnText}'")
        return EmptyType

    def _findClassWithModule(self, text: str, mustDiffer: str = '') -> RetType:
        cType = text.removeprefix('Py::asObject(new ').removeprefix('new ')
        cType = cType.split('(', maxsplit=1)[0]
        classWithModule = getClassWithModulesFromPointer(cType)

        match classWithModule:
            case self.className:
                return self.classNameWithModule

            case 'SplitView3DInventor':
                # we must use take base class
                return 'FreeCADGui.AbstractSplitViewPy'
            case 'View3DInventorViewer':
                return 'FreeCADGui.View3DInventorViewerPy'

            case 'PropertyComplexGeoData':
                # it may be any of following
                # access via: `getPropertyOfGeometry` function,
                # search: `App::PropertyComplexGeoData)`,
                return UnionArguments(['Mesh.MeshObject', 'Part.Shape', 'Points.PointKernel'])

            case _ if classWithModule != mustDiffer and (mod := getModuleName(classWithModule)):
                self.requiredImports.add(mod)
                return classWithModule

        return EmptyType

    def _findVariableType(self, variableName: str, endPos: int) -> RetType:
        """Search variable type based on its name - declaration/assignment."""
        if variableName == 'this':
            assert self.classNameWithModule is not None
            return self.classNameWithModule

        variableDecReg = re.compile(rf"""
        ([\w:]+(?<!:))     # word with ':', but cannot end with ':'
        \s*\*?             # may be a pointer
        (?:>::(?:const_)?iterator)?\s* # may be iterator or const_iterator
        \b{variableName}\b # variable name must be separate word
        (?:\s*=\s*(.*);)?  # there may be optional assignment expression 
        """, re.VERBOSE)
        matches = list(variableDecReg.finditer(self.functionBody, endpos=endPos))
        for declarationMatch in reversed(matches):
            varTypeDec = declarationMatch.group(1)
            if varTypeDec in ('return', 'else'):
                continue

            elif varTypeDec in ('auto', 'PyObject', 'Py::Object'):
                if assignValue := declarationMatch.group(2):
                    #  we can try resolve real type by checking right side
                    varType = self._getReturnTypeForText(assignValue, endPos, onlyLiteral=True)
                else:
                    varType = EmptyType

            else:
                varType = self._getReturnTypeForText(varTypeDec, endPos, onlyLiteral=True)

            if varType == EmptyType:
                varType = self._getRetTypeFromAssignment(
                    variableName, declarationMatch.end(), endPos)

            varType = self._getInnerType(
                varType, variableName, declarationMatch.start(), declarationMatch.end(), endPos)

            return varType

        return self._getReturnTypeForText(variableName, endPos, onlyLiteral=True)

    def _getRetTypeFromAssignment(self, variableName: str, startPos: int, endPos: int) -> RetType:
        """Example: `myVar = Py::Float(7.0)`."""
        return next(self._genVariableTypeFromRegex(
            re.compile(rf'{variableName}\b\s*=\s*([^;]*);'), startPos, endPos), EmptyType)

    def _genVariableTypeFromRegex(self, regex: re.Pattern, startPos: int, endPos: int,
                                  onlyLiteral=True):
        """General match function by regex between declaration and `return` keyword."""
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            variableTypeText = variableMatch.group(1)
            varType = self._getReturnTypeForText(variableTypeText, endPos, onlyLiteral=onlyLiteral)
            if varType != EmptyType:
                yield varType

    def _getInnerType(self, varType: str | _EmptyType, variableName: str,
                      decStartPos: int, decEndPos: int, endPos: int) -> str:
        """Additional search for generic types."""
        match varType:
            case 'list':
                innerTypes = self._getInnerTypeList(variableName, decEndPos, endPos)
                if not innerTypes:
                    innerTypes = self._getInnerTypePyListSetItem(variableName, decEndPos, endPos)

                if innerTypes:
                    varType += f'[{innerTypes}]'
                    self.requiredImports.update(innerTypes.imports)

            case 'tuple':
                listTypes = TupleArgument(self._genInnerTypeTupleSetItem(
                    variableName, decEndPos, endPos))
                if not listTypes:
                    listTypes = TupleArgument(self._genInnerTypePyTupleSetItem(
                        variableName, decEndPos, endPos))
                if not listTypes:
                    listTypes = TupleArgument(self._genInnerTypeTupleAssignItem(
                        variableName, decEndPos, endPos))
                if not listTypes:
                    listTypes = TupleArgument(self._genInnerTypeTupleConstructor(
                        variableName, decStartPos, endPos))

                assert listTypes, "Cannot find inner type for tuple"
                varType = str(listTypes)
                self.requiredImports.update(listTypes.imports)

            case 'dict':
                pass  # TODO P2 add dict types

        return varType

    def _getInnerTypeList(self, variableName: str, startPos: int, endPos: int):
        regex = re.compile(rf'{variableName}\b.append\(([^;]*)\);')
        return UnionArguments(
            self._genVariableTypeFromRegex(regex, startPos, endPos, onlyLiteral=False))

    def _getInnerTypePyListSetItem(self, variableName: str, startPos: int, endPos: int):
        """Example: `PyList_SetItem(pyList, i++, str);`."""
        arg = UnionArguments()
        regex = re.compile(rf'PyList_SetItem\s*\(\s*{variableName}\s*,\s*[\w+]+\s*,([^;]+)\);')
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            varType = self._getReturnTypeForText(variableMatch.group(1), endPos)
            assert varType != EmptyType
            arg.add(varType)
        return arg

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
