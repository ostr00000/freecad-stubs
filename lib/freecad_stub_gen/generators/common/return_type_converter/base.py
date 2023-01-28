import logging
import re
from functools import cached_property

from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.common.names import getClassName, getClassWithModulesFromPointer, \
    getModuleName
from freecad_stub_gen.generators.common.py_build_converter import parsePyBuildValues
from freecad_stub_gen.generators.common.return_type_converter.arg_types import EmptyType, \
    Empty, UnionArguments, RetType, InvalidReturnType
from freecad_stub_gen.generators.common.return_type_converter.str_wrapper import StrWrapper
from freecad_stub_gen.util import OrderedSet

logger = logging.getLogger(__name__)


class ReturnTypeConverterBase:
    def __init__(self, functionBody: str, requiredImports: OrderedSet = None,
                 classNameWithModule: str = '', functionName: str = ''):
        self.requiredImports = OrderedSet() if requiredImports is None else requiredImports
        self.functionBody = functionBody
        self.classNameWithModule = classNameWithModule
        self.functionName = functionName

    @cached_property
    def className(self):
        return getClassName(self.classNameWithModule)

    def getExpressionType(self, varText: str, endPos: int, onlyLiteral=False) -> RetType:
        varText = varText.strip()
        if varText.endswith(')') \
                and (varText.startswith('new_reference_to(')
                     or varText.startswith('Py::new_reference_to(')):
            varText = varText \
                .removeprefix('Py::') \
                .removeprefix('new_reference_to(') \
                .removesuffix(')').strip()

        if varText.startswith('*'):
            varText = varText.removeprefix('*').strip()

        match StrWrapper(varText):
            case '':
                return Empty
            case 'Py::Object()':
                return 'object'
            case 'Py_None' | 'Py::None()' | 'Py_Return':
                return 'None'
            case '0' | '-1' | 'NULL' | 'nullptr' | '0L':
                if onlyLiteral:
                    return Empty
                else:
                    raise InvalidReturnType

            case 'getDocumentObjectPtr()':
                return 'FreeCAD.DocumentObject'
            case StrWrapper('(GetApplication().openDocument('):
                return 'FreeCAD.Document'

            case StrWrapper('Py::Boolean' | 'PyBool_From' | 'Py::True' | 'Py::False'):
                return 'bool'
            case StrWrapper('Py::Long' | 'PyLong_From' | 'Py::Int'
                            | 'PyInt_From' | 'PYINT_FROMLONG'):
                return 'int'
            case StrWrapper('Py::Float' | 'PyFloat_From'):
                return 'float'
            case StrWrapper('Py::String' | 'PyString_From'
                            | 'PyUnicode_From' | 'Py::Char'
                            | 'PyUnicode_DecodeUTF8' | 'PYSTRING_FROMSTRING'):
                return 'str'
            case StrWrapper('Py::TupleN'):
                if onlyLiteral:
                    return 'tuple'
                else:
                    return self.getInnerType('tuple', variableName=varText, decStartPos=0,
                                             decEndPos=endPos, endPos=endPos)
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
                return 'FreeCAD.BoundBox'
            case StrWrapper('Py::Matrix'):
                return 'FreeCAD.Matrix'
            case StrWrapper('Py::Rotation'):
                return 'FreeCAD.Rotation'
            case StrWrapper('Py::Placement'):
                return 'FreeCAD.Placement'
            # typedef PythonClassObject<Base::Vector2dPy> Vector2d;
            case StrWrapper('Py::Vector2d' | 'Base::Vector2dPy::create('):
                return 'FreeCAD.Vector2d'
            case StrWrapper('Py::Vector'):
                return 'FreeCAD.Vector'

            case StrWrapper('shape2pyshape' | 'Part::shape2pyshape'):
                return 'Part.Shape'
            case StrWrapper('getShapes<'):
                templateClass = varText.removeprefix('getShapes<').split('>')[0]
                innerClass = self.getExpressionType(templateClass, endPos)
                return f'list[{innerClass}]'

            case StrWrapper('Base::Interpreter().createSWIGPointerObj('):
                fc = varText.removeprefix('Base::Interpreter().createSWIGPointerObj(')
                funArgs = [
                    exp.strip().removeprefix('"').removesuffix('"')
                    for exp in generateExpressionUntilChar(
                        fc, 0, ',', bracketL='(', bracketR=')')]
                module: str = funArgs[0]
                klass: str = funArgs[1]
                if not module.startswith('pivy') or '(' in klass:
                    return Empty
                klass = klass.removeprefix('_p_').removesuffix('*').strip()
                return f'{module}.{klass}'

            case StrWrapper('MainWindowPy::createWrapper'):
                return 'FreeCADGui.MainWindowPy'

            case StrWrapper('wrap.fromQObject('):
                return 'qtpy.QtCore.QObject'
            case StrWrapper('wrap.fromQWidget('):
                fc = findFunctionCall(
                    varText, bodyStart=varText.find('('),
                    bracketL='(', bracketR=')').removeprefix('(').removesuffix(')')
                funArgs = list(generateExpressionUntilChar(
                    fc, 0, ',', bracketL='(', bracketR=')'))
                if len(funArgs) == 1:
                    widgetType = 'QWidget'
                else:
                    assert len(funArgs) == 2
                    widgetType = funArgs[1].strip().removeprefix('"').removesuffix('"')
                    if not widgetType.startswith('Q'):
                        widgetType = 'QWidget'
                return f'qtpy.QtWidgets.{widgetType}'
            case StrWrapper('wrap.fromQIcon('):
                return 'qtpy.QtGui.QIcon'

            case StrWrapper('PyRun_String'):
                return Empty

            case StrWrapper('new ' | 'Py::asObject(new '):
                return self._findClassWithModule(varText)
            case StrWrapper(end='Py') as i if i.isidentifier() and i[0].isupper():
                return self._findClassWithModule(varText)

            case StrWrapper(end='->getPyObject()' | '.getPyObject()'):
                expText = varText \
                    .removesuffix('getPyObject()') \
                    .removesuffix('.') \
                    .removesuffix('->') \
                    .removesuffix(')')
                varTextStartPos = expText.rfind('(') + 1
                varText = expText[varTextStartPos:]
                return self.getExpressionType(varText, endPos=endPos)

            case StrWrapper('Py_BuildValue("'):
                fc = findFunctionCall(
                    varText, bodyStart=len('Py_BuildValue'), bracketL='(', bracketR=')',
                ).removeprefix('(').removesuffix(')')
                funArgs = list(generateExpressionUntilChar(
                    fc, 0, ',', bracketL='(', bracketR=')'))
                formatText = funArgs[0].removeprefix('"').removesuffix('"')
                if pythonType := parsePyBuildValues(formatText):
                    if pythonType == Empty:
                        objArg = funArgs[1].strip()
                        pythonType = self.getExpressionType(objArg, endPos, onlyLiteral=True)
                    return pythonType

            case StrWrapper(contain='Py_True' | 'Py_False'):
                # must be before identifier and should be after Py_BuildValue
                return 'bool'

            case StrWrapper('Py::asObject(' | 'Py::Object(' | 'createPyObject('):
                fc = findFunctionCall(
                    varText, bodyStart=varText.find('('),
                    bracketL='(', bracketR=')').removeprefix('(').removesuffix(')')
                funArgs = list(generateExpressionUntilChar(
                    fc, 0, ',', bracketL='(', bracketR=')'))
                rawReturnVarName = funArgs[0]
                return self.getExpressionType(rawReturnVarName, endPos)

            case _ if onlyLiteral:
                if all(i.isidentifier() for i in varText.split('::')):
                    maybeClass = varText
                    if not maybeClass.endswith('Py'):
                        maybeClass += 'Py'
                    return self._findClassWithModule(maybeClass, mustDiffer=varText)
                return Empty

            case _ if varText.isidentifier():
                return self._findVariableType(varText, endPos)

            case StrWrapper('(', end=')'):
                return self.getExpressionType(varText.removeprefix('(').removesuffix(')'), endPos,
                                              onlyLiteral)

            case StrWrapper(contain='=='):
                return 'bool'

            case _:
                logger.warning(f"Unknown return variable: '{varText}'")
        return Empty

    def _findClassWithModule(self, text: str, mustDiffer: str = '') -> RetType:
        cType = text.removeprefix('Py::asObject(new ').removeprefix('new ')
        cType = cType.split('(', maxsplit=1)[0]
        classWithModule = getClassWithModulesFromPointer(cType)
        cl = getClassName(classWithModule)

        match StrWrapper(cl):
            case self.className:
                return self.classNameWithModule

            # yet another exception from rules
            case 'MDIView' | 'View3DInventorViewerPy' | 'View3DInventorPy' | 'AbstractSplitViewPy':
                return classWithModule + 'Py'

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

        return Empty

    def _findVariableType(self, variableName: str, endPos: int) -> RetType:
        """Search variable type based on its name - declaration/assignment."""
        if variableName == 'this':
            assert self.classNameWithModule is not None
            return self.classNameWithModule

        variableDecReg = re.compile(rf"""
        (?P<directive>\#)?              # we skip directive later in code 
        \s*                             # (otherwise need to use variable lookbehind)
        (?P<type>
            [^\d\W][\w:]*               # word not starting with digits, may contain ':'
            (?<!:))                     # but cannot end with ':'
        \s*\*?                          # may be a pointer
        (?:>::(?:const_)?iterator)?\s*  # may be iterator or const_iterator
        (?:\b\w+\s*,\s*)*               # there may be multiple declaration for one type
        \b{variableName}\b              # variable name must be separate word
        (?:\s*
            =\s*(?P<val>.*);            # there may be optional assignment expression
            |
            \((?P<args>[^;]+)\);        # there may be arguments to constructor
        )?
        """, re.VERBOSE)
        matches = list(variableDecReg.finditer(self.functionBody, endpos=endPos))
        for declarationMatch in reversed(matches):
            if declarationMatch.group('directive'):
                continue

            varTypeDec = declarationMatch.group('type')
            if varTypeDec in ('return', 'else'):
                continue

            elif varTypeDec in ('auto', 'PyObject', 'Py::Object'):
                if assignValue := declarationMatch.group('val'):
                    #  we can try resolve real type by checking right side
                    varType = self.getExpressionType(assignValue, endPos, onlyLiteral=True)
                elif varTypeDec != 'auto' and (argsValue := declarationMatch.group('args')):
                    funArgs = list(generateExpressionUntilChar(
                        argsValue, 0, ',', bracketL='(', bracketR=')'))
                    #  we can try resolve real type from constructor argument
                    varType = self.getExpressionType(funArgs[0], endPos, onlyLiteral=False)
                else:
                    varType = Empty

            else:
                varType = self.getExpressionType(varTypeDec, endPos, onlyLiteral=True)

            if (isNone := (varType == 'None')) or varType == Empty:
                varType = self._getRetTypeFromAssignment(
                    variableName, declarationMatch.end(), endPos)
                if isNone:
                    match varType:
                        case UnionArguments():
                            varType.add('None')
                        case str():
                            varType = UnionArguments(('None', varType))
                        case Empty.value:
                            varType = 'None'

            varType = self.getInnerType(varType, variableName, declarationMatch.start(),
                                        declarationMatch.end(), endPos)

            return varType

        return self.getExpressionType(variableName, endPos, onlyLiteral=True)

    def _getRetTypeFromAssignment(self, variableName: str, startPos: int, endPos: int) -> RetType:
        """Example: `myVar = Py::Float(7.0)`."""
        regex = re.compile(rf'{variableName}\b\s*=\s*([^;]*);')
        gen = self._genVariableTypeFromRegex(regex, startPos, endPos, onlyLiteral=False)
        if union := UnionArguments(gen):
            return union
        return Empty

    def _genVariableTypeFromRegex(self, regex: re.Pattern, startPos: int, endPos: int,
                                  onlyLiteral=True):
        """General match function by regex between declaration and `return` keyword."""
        for variableMatch in regex.finditer(self.functionBody, startPos, endpos=endPos):
            variableTypeText = variableMatch.group(1)
            varType = self.getExpressionType(variableTypeText, endPos, onlyLiteral=onlyLiteral)
            match varType:
                case UnionArguments():
                    yield from varType
                case str():
                    yield varType

    def getInnerType(self, varType: str | EmptyType, variableName: str,
                     decStartPos: int, decEndPos: int, endPos: int) -> str:
        """Additional search for generic types."""
        return varType
