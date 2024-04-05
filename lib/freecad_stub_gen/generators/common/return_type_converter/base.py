import atexit
import logging
import re
from functools import cached_property
from itertools import islice

from freecad_stub_gen.cpp_code.converters import removeQuote
from freecad_stub_gen.generators.common.cpp_function import (
    generateExpressionUntilChar,
    genFuncArgs,
)
from freecad_stub_gen.generators.common.names import (
    getClassName,
    getClassWithModulesFromPointer,
    getModuleName,
    removeAffix,
)
from freecad_stub_gen.generators.common.py_build_converter import parsePyBuildValues
from freecad_stub_gen.generators.common.return_type_converter.arg_types import (
    AnyValue,
    InvalidReturnType,
    RetType,
    UnionArgument,
)
from freecad_stub_gen.generators.common.return_type_converter.str_wrapper import (
    StrWrapper,
)
from freecad_stub_gen.ordered_set import OrderedStrSet

logger = logging.getLogger(__name__)


class ReturnTypeConverterBase:
    def __init__(
        self,
        functionBody: str = '',
        requiredImports: OrderedStrSet | None = None,
        classNameWithModule: str = '',
        functionName: str = '',
    ):
        self.requiredImports = (
            OrderedStrSet() if requiredImports is None else requiredImports
        )
        self.functionBody = functionBody
        self.classNameWithModule = classNameWithModule
        self.functionName = functionName

    @cached_property
    def className(self):
        return getClassName(self.classNameWithModule)

    def getExpressionType(
        self, varText: str, endPos: int = 0, *, onlyLiteral=False
    ) -> RetType:
        varText = self._removeAffixes(varText)
        sw = StrWrapper(varText)

        for method in (
            self._matchLiterals,
            self._matchPyType,
            self._matchSpecial,
            self._matchQt,
            self._matchMethodCall,
            self._matchFreeCAD,
            self._matchFinalPossibilities,
        ):
            if (result := method(sw, endPos, onlyLiteral=onlyLiteral)) is not None:
                return result

        return AnyValue

    def _matchLiterals(
        self, varText: str, endPos: int = 0, *, onlyLiteral
    ) -> RetType | None:
        match StrWrapper(varText):
            case '':
                return AnyValue

            case '0' | '-1' | 'NULL' | 'nullptr' | '0L':
                if onlyLiteral:
                    return AnyValue
                raise InvalidReturnType

        return None

    def _matchPyType(
        self, varText: str, endPos: int = 0, *, onlyLiteral
    ) -> RetType | None:
        ret = None
        match StrWrapper(varText):
            case 'Py::Object()':
                ret = 'object'

            case 'Py_None' | 'Py::None()' | 'Py_Return':
                ret = 'None'

            case StrWrapper('Py::Boolean' | 'PyBool_From' | 'Py::True' | 'Py::False'):
                ret = 'bool'

            case StrWrapper(
                'Py::Long'
                | 'PyLong_From'
                | 'Py::Int'
                | 'PyInt_From'
                | 'PYINT_FROMLONG'
                | 'int',
            ):
                ret = 'int'

            case StrWrapper('Py::Float' | 'PyFloat_From'):
                ret = 'float'

            case StrWrapper('Py::List' | 'PyList_New'):
                ret = 'list'

            case StrWrapper('Py::Dict' | 'PyDict_New'):
                ret = 'dict'

            case StrWrapper('Py::Callable'):
                ret = 'typing.Callable'

            case StrWrapper('PyByteArray_From'):
                ret = 'bytes'

            case StrWrapper(
                'Py::String'
                | 'PyString_From'
                | 'PyUnicode_From'
                | 'Py::Char'
                | 'PyUnicode_DecodeUTF8'
                | 'PYSTRING_FROMSTRING'
                | 'QString'
            ):
                ret = 'str'

            case StrWrapper(contain='Py_True' | 'Py_False'):
                # must be before identifier and should be after Py_BuildValue
                ret = 'bool'

            case StrWrapper('Py::TupleN'):
                if onlyLiteral:
                    return 'tuple'
                return self.getInnerType(
                    'tuple',
                    variableName=varText,
                    decStartPos=0,
                    decEndPos=endPos,
                    endPos=endPos,
                )

            case StrWrapper('PyTuple_Pack'):
                subTypes = [
                    str(self.getExpressionType(v, endPos))
                    for v in islice(genFuncArgs(varText), 1, None)
                ]
                ret = f'tuple[{", ".join(subTypes)}]'

            case StrWrapper('Py::Tuple' | 'PyTuple_New'):
                ret = 'tuple'

        return ret

    def _matchSpecial(
        self, varText: str, endPos: int = 0, *, onlyLiteral
    ) -> RetType | None:
        match StrWrapper(varText):
            case 'getDocumentObjectPtr()':
                return 'FreeCAD.DocumentObject'
            case StrWrapper('(GetApplication().openDocument('):
                return 'FreeCAD.Document'

        return None

    def _matchQt(self, varText: str, endPos: int = 0, *, onlyLiteral) -> RetType | None:
        match StrWrapper(varText):
            case StrWrapper('wrap.fromQObject('):
                return 'qtpy.QtCore.QObject'

            case StrWrapper('QWidget'):
                return 'qtpy.QtWidgets.QWidget'

            case StrWrapper('wrap.fromQWidget('):
                return self._extractWidget(varText)

            case StrWrapper('wrap.fromQIcon('):
                return 'qtpy.QtGui.QIcon'

        return None

    def _matchMethodCall(
        self, varText: str, endPos: int = 0, *, onlyLiteral
    ) -> RetType | None:
        ret = None
        match StrWrapper(varText):
            case 'type->tp_new(type, this, nullptr)':
                ret = self.getExpressionType('type', endPos)

            case 'this->GetType()' | 'IncRef()':
                ret = self.classNameWithModule

            case StrWrapper(end='->copyPyObject()'):
                original = varText.removesuffix('->copyPyObject()')
                ret = self.getExpressionType(original, endPos)

            case StrWrapper(end='->c_str()'):
                ret = 'str'

            case StrWrapper('PyRun_String'):
                ret = AnyValue

            case StrWrapper('Base::Interpreter().createSWIGPointerObj('):
                ret = self._extractPivy(varText)

            case StrWrapper('new ' | 'Py::asObject(new '):
                ret = self._findClassWithModule(varText)

            case StrWrapper('Py_BuildValue("'):
                ret = self._extractBuildValue(varText, endPos)

            case StrWrapper('Py::asObject(' | 'Py::Object(' | 'createPyObject('):
                rawReturnVarName = next(iter(genFuncArgs(varText)))
                return self.getExpressionType(rawReturnVarName, endPos)

            case StrWrapper('Base::getTypeAsObject('):
                rawReturnVarName = next(iter(genFuncArgs(varText)))
                return self.getExpressionType(rawReturnVarName, endPos)

            case StrWrapper(end='Py') as i if i.isidentifier() and i[0].isupper():
                ret = self._findClassWithModule(varText)

            case StrWrapper(end='->getPyObject()' | '.getPyObject()'):
                varText = removeAffix(
                    varText, suffixes=('getPyObject()', '.', '->', ')')
                )
                varText = varText[varText.rfind('(') + 1 :]
                ret = self.getExpressionType(varText, endPos=endPos)

        return ret

    def _matchFreeCAD(
        self, varText: str, endPos: int = 0, *, onlyLiteral
    ) -> RetType | None:
        ret = None
        match StrWrapper(varText):
            # PyCXX wrapper classes, search for `typedef GeometryT<`
            case StrWrapper('Py::BoundingBox'):
                ret = 'FreeCAD.BoundBox'
            case StrWrapper('Py::Matrix'):
                ret = 'FreeCAD.Matrix'
            case StrWrapper('Py::Rotation'):
                ret = 'FreeCAD.Rotation'
            case StrWrapper('Py::Placement'):
                ret = 'FreeCAD.Placement'
            # typedef PythonClassObject<Base::Vector2dPy> Vector2d;
            case StrWrapper('Py::Vector2d' | 'Base::Vector2dPy::create('):
                ret = 'FreeCAD.Vector2d'
            case StrWrapper('Py::Vector'):
                ret = 'FreeCAD.Vector'

            case StrWrapper('MainWindowPy::createWrapper'):
                ret = 'FreeCADGui.MainWindowPy'

            case StrWrapper('shape2pyshape' | 'Part::shape2pyshape'):
                ret = 'Part.Shape'

            case StrWrapper('getShapes<'):
                templateClass = varText.removeprefix('getShapes<').split('>')[0]
                innerClass = self.getExpressionType(templateClass, endPos)
                ret = f'list[{innerClass}]'

        return ret

    def _matchFinalPossibilities(
        self, varText: str, endPos: int = 0, *, onlyLiteral
    ) -> RetType | None:
        ret = None
        match StrWrapper(varText):
            case maybeClass if onlyLiteral:
                ret = retVal if (retVal := self._findClass(maybeClass)) else AnyValue

            case _ if varText.isidentifier():
                ret = self._findVariableType(varText, endPos)

            case StrWrapper('(', end=')'):
                ret = self.getExpressionType(
                    removeAffix(varText, '(', ')'),
                    endPos,
                    onlyLiteral=onlyLiteral,
                )

            case StrWrapper(contain='=='):
                ret = 'bool'

            case maybeClass if retType := self._findClass(maybeClass):
                ret = retType

            case _:
                logger.warning(f"Unknown return variable: '{varText}'")
                typeExtractor.missedTypes += 1

        return ret

    def _findClass(self, varText: str) -> RetType | None:
        if not all(i.isidentifier() for i in varText.split('::')):
            return None

        if not varText[0].isupper():
            return None

        varText = varText.removesuffix('::Type')
        return self._findClassWithModule(varText, mustDiffer=varText)

    @staticmethod
    def _removeAffixes(varText: str) -> str:
        varText = varText.strip()
        match StrWrapper(varText):
            case StrWrapper(
                start='new_reference_to(' | 'Py::new_reference_to(', end=')'
            ):
                varText = removeAffix(varText, ('Py::', 'new_reference_to('), ')')

        return removeAffix(varText, ('const', '*', '&'), ('*', '&'))

    @classmethod
    def _extractPivy(cls, varText: str):
        withoutPrefix = varText.removeprefix('Base::Interpreter().createSWIGPointerObj')
        funArgs = list(genFuncArgs(withoutPrefix))
        module = removeQuote(funArgs[0])
        klass = removeQuote(funArgs[1])

        if not module.startswith('pivy') or '(' in klass:
            return AnyValue

        klass = removeAffix(klass, '_p_', '*')
        return f'{module}.{klass}'

    @classmethod
    def _extractWidget(cls, varText: str):
        funArgs = list(genFuncArgs(varText))
        match funArgs:
            case [_castArg]:
                widgetType = 'QWidget'
            case [_castArg, castType]:
                widgetType = removeQuote(castType)
                if not widgetType.startswith('Q'):
                    widgetType = 'QWidget'
            case _:
                raise NotImplementedError
        return f'qtpy.QtWidgets.{widgetType}'

    def _extractBuildValue(self, varText: str, endPos: int) -> RetType:
        funArgs = list(genFuncArgs(varText))
        formatText = removeQuote(funArgs[0])
        if (pythonType := parsePyBuildValues(formatText)) != AnyValue:
            return pythonType

        objArg = funArgs[1].strip()
        return self.getExpressionType(objArg, endPos, onlyLiteral=True)

    def _findClassWithModule(self, text: str, mustDiffer: str = '') -> RetType:
        cType = removeAffix(text, ('Py::asObject(', 'new '))
        cType = cType.split('(', maxsplit=1)[0]
        classWithModule = getClassWithModulesFromPointer(cType)
        cl = getClassName(classWithModule)
        match StrWrapper(cl):
            case self.className:
                return self.classNameWithModule

            case 'PropertyComplexGeoData':
                # it may be any of following
                # access via: `getPropertyOfGeometry` function,
                # search: `App::PropertyComplexGeoData)`,
                return UnionArgument(
                    ['Mesh.MeshObject', 'Part.Shape', 'Points.PointKernel']
                )

            case _ if classWithModule != mustDiffer and (
                mod := getModuleName(classWithModule)
            ):
                self.requiredImports.add(mod)
                return classWithModule

        return AnyValue

    def _findVariableType(self, variableName: str, endPos: int) -> RetType:
        """Search variable type based on its name - declaration/assignment."""
        if variableName == 'this':
            if self.classNameWithModule is None:
                raise TypeError
            return self.classNameWithModule

        variableDecReg = re.compile(
            rf"""
        (?P<directive>\#)?      # we skip directive later in code
                                # (otherwise need to use variable lookbehind)
        (?>\s*)                 # skip whiespace, do not backtrack from there
        (?P<type>
            [^\d\W][\w:<>*\s]*  # word not starting with digits, may contain ':'
            (?<![:\s]))         # but cannot end with ':' or \s
        \s*
        (?:\b\w+\s*,\s*)*       # there may be multiple declaration for one type
        \b{variableName}\b      # variable name must be separate word
        \s*
        (?:
            (?:,\s*\w+\s*)*     # there may be multiple declaration for one type
            |
            =\s*(?P<val>[^;]*)  # there may be optional assignment expression
            |
            \((?P<args>[^;]+)\) # there may be arguments to constructor
        )?
        [;:]                    # end of statement or this is for loop
        """,
            re.VERBOSE,
        )
        matches = list(variableDecReg.finditer(self.functionBody, endpos=endPos))
        for declarationMatch in reversed(matches):
            if declarationMatch.group('directive'):
                continue

            if not (varTypeDec := self._extractTypeFromMatch(declarationMatch)):
                continue

            return self._findVariableTypeFromRegex(
                variableName, endPos, declarationMatch, varTypeDec
            )

        return self.getExpressionType(variableName, endPos, onlyLiteral=True)

    def _findVariableTypeFromRegex(
        self,
        variableName: str,
        endPos: int,
        declarationMatch: re.Match,
        varTypeDec: str,
    ) -> RetType:
        if varTypeDec in {
            'auto',
            'PyObject',
            'Py::Object',
            'PyTypeObject',
            'PyObjectBase',
        }:
            if assignValue := declarationMatch.group('val'):
                #  we can try resolve real type by checking right side
                varType = self.getExpressionType(assignValue, endPos, onlyLiteral=True)
            elif varTypeDec != 'auto' and (argsValue := declarationMatch.group('args')):
                #  we can try resolve real type from constructor argument
                funArgs = list(
                    generateExpressionUntilChar(
                        argsValue, 0, ',', bracketL='(', bracketR=')'
                    )
                )
                varType = self.getExpressionType(funArgs[0], endPos, onlyLiteral=False)
            else:
                varType = AnyValue

        else:
            varType = self.getExpressionType(varTypeDec, endPos, onlyLiteral=True)

        if varType == 'None':
            varType = self._findVariableTypeNone(
                variableName, declarationMatch.end(), endPos
            )
        if varType == AnyValue:
            varType = self._getRetTypeFromAssignment(
                variableName, declarationMatch.end(), endPos
            )

        if isinstance(varType, str):
            varType = self.getInnerType(
                varType,
                variableName,
                declarationMatch.start(),
                declarationMatch.end(),
                endPos,
            )

        return varType

    def _findVariableTypeNone(
        self, variableName: str, startPos: int, endPos: int
    ) -> RetType:
        varType = self._getRetTypeFromAssignment(variableName, startPos, endPos)

        match varType:
            case UnionArgument():
                varType.add('None')
            case str():
                varType = UnionArgument(('None', varType))
            case AnyValue.value:
                varType = 'None'

        return varType

    @staticmethod
    def _extractTypeFromMatch(match) -> str | None:
        if not (v := match.group('type')):
            return None
        if v in {'return', 'else', 'delete'}:
            return None

        if '<' in v and '>' in v:
            v = v.split('<', maxsplit=1)[1].split('>', maxsplit=1)[0]
        return removeAffix(v, 'const', '*')

    def _getRetTypeFromAssignment(
        self, variableName: str, startPos: int, endPos: int
    ) -> RetType:
        """Extract parametrized type from `x = ...`.

        Example: `myVar = Py::Float(7.0)`.
        """
        regex = re.compile(rf'{variableName}\b\s*=\s*([^;]*);')
        gen = self._genVariableTypeFromRegex(regex, startPos, endPos, onlyLiteral=False)
        if union := UnionArgument(gen):
            return union
        return AnyValue

    def _genVariableTypeFromRegex(
        self, regex: re.Pattern, startPos: int, endPos: int, *, onlyLiteral=True
    ):
        """General match function by regex between declaration and `return` keyword."""
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            variableTypeText = variableMatch.group(1)
            varType = self.getExpressionType(
                variableTypeText, endPos, onlyLiteral=onlyLiteral
            )
            match varType:
                case UnionArgument():
                    yield from varType
                case str():
                    yield varType

    def getInnerType(
        self,
        varType: str,
        variableName: str,
        decStartPos: int,
        decEndPos: int,
        endPos: int,
    ) -> RetType:
        # pylint: disable=unused-argument
        """Additional search for generic types."""
        return varType


class TypeExtractor:
    def __init__(self):
        self.missedTypes = 0

        atexit.register(self.atExit)

    def atExit(self):
        logger.info(f"Cannot find return types for {self.missedTypes} functions")


typeExtractor = TypeExtractor()
