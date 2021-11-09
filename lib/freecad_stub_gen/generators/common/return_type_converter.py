import re
from inspect import Signature

from freecad_stub_gen.generators.common.annotation_parameter import RawRepr
from freecad_stub_gen.generators.common.arguments_converter import logger
from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.common.names import getClassWithModulesFromPointer, getModuleName
from freecad_stub_gen.generators.common.py_build_converter import parsePyBuildValues
from freecad_stub_gen.util import OrderedSet


class ReturnTypeConverter:
    REG_RETURN = re.compile(r'return ([^;]+);')

    def __init__(self, requiredImports: OrderedSet, functionBody: str,
                 classNameWithModule: str = None, functionName: str = None):
        self.requiredImports = requiredImports
        self.functionBody = functionBody
        self.classNameWithModule = classNameWithModule
        self.functionName = functionName

    def getReturnType(self):
        returnTypes = OrderedSet(self._genReturnType())
        if not returnTypes:
            return Signature.empty
        return RawRepr(*returnTypes)

    def _genReturnType(self):
        for match in self.REG_RETURN.finditer(self.functionBody):
            returnText = match.group(1).strip()

            if returnText.endswith(')') \
                    and (returnText.startswith('(')
                         or returnText.startswith('new_reference_to(')
                         or returnText.startswith('Py::new_reference_to(')):
                returnText = returnText \
                    .removeprefix('Py::') \
                    .removeprefix('new_reference_to') \
                    .removeprefix('(').removesuffix(')')

            retType = self._getReturnTypeForText(returnText, match.end())
            if retType is None:
                continue

            if mod := getModuleName(retType):
                self.requiredImports.add(mod)

            yield retType

    def _getReturnTypeForText(self, returnText: str, endPos: int, onlyLiteral=False):
        returnText = returnText.strip()
        match returnText:
            case 'Py::Object()':
                # we must use `Union` wrapper,
                # otherwise `object` may be ignored if there are no other types
                return 'typing.Union[object]'
            case 'Py_None' | 'Py::None()' | 'Py_Return':
                return 'None'
            case '0' | '-1' | 'NULL' | 'nullptr' | '0L':
                return  # an exception

            case _ if returnText.startswith('Py::Boolean') \
                      or returnText.startswith('PyBool_From') \
                      or returnText.startswith('Py::True') \
                      or returnText.startswith('Py::False'):
                return 'bool'
            case _ if returnText.startswith('Py::Long') \
                      or returnText.startswith('PyLong_From') \
                      or returnText.startswith('Py::Int') \
                      or returnText.startswith('PyInt_From'):
                return 'int'
            case _ if returnText.startswith('Py::Float') \
                      or returnText.startswith('PyFloat_From'):
                return 'float'
            case _ if returnText.startswith('Py::String') \
                      or returnText.startswith('PyUnicode_From') \
                      or returnText.startswith('PyUnicode_DecodeUTF8'):
                return 'str'
            case _ if returnText.startswith('Py::Tuple') \
                      or returnText.startswith('PyTuple_New'):
                return 'tuple'
            case _ if returnText.startswith('Py::List') \
                      or returnText.startswith('PyList_New'):
                return 'list'  # TODO P3 maybe extract parametrized type?
            case _ if returnText.startswith('Py::Dict') \
                      or returnText.startswith('PyDict_New'):
                return 'dict'
            case _ if returnText.startswith('Py::Callable'):
                return 'typing.Callable'

            # PyCXX wrapper classes, search for `typedef GeometryT<`
            case _ if returnText.startswith('Py::BoundingBox('):
                return 'FreeCAD.BoundingBox'
            case _ if returnText.startswith('Py::Matrix('):
                return 'FreeCAD.Matrix'
            case _ if returnText.startswith('Py::Rotation('):
                return 'FreeCAD.Rotation'
            case _ if returnText.startswith('Py::Placement('):
                return 'FreeCAD.Placement'
            # typedef PythonClassObject<Base::Vector2dPy> Vector2d;
            case _ if returnText.startswith('Py::Vector2d('):
                return 'FreeCAD.Vector2d'
            case _ if returnText.startswith('Py::Vector('):
                return 'FreeCAD.Vector'

            case _ if returnText.startswith('shape2pyshape') \
                      or returnText.startswith('Part::shape2pyshape'):
                return 'Part.Shape'

            # TODO P2 findCentroid do not return Vector

            case _ if returnText.startswith('wrap.fromQWidget('):
                fc = findFunctionCall(
                    returnText, bodyStart=returnText.find('('),
                    bracketL='(', bracketR=')').removeprefix('(').removesuffix(')')
                funArgs = list(generateExpressionUntilChar(
                    fc, 0, ',', bracketL='(', bracketR=')'))
                assert len(funArgs) == 2
                widgetType = funArgs[1].strip().removeprefix('"').removesuffix('"')
                return f'qtpy.QtWidgets.{widgetType}'
            case _ if returnText.startswith('wrap.fromQIcon('):
                return 'qtpy.QtGui.QIcon'

            case _ if returnText.startswith('PyRun_String'):
                return 'object'

            case _ if returnText.startswith('new ') \
                      or returnText.startswith('Py::asObject(new ') \
                      or (returnText.isidentifier()
                          and returnText[0].isupper()
                          and returnText.endswith('Py')):
                cType = returnText.removeprefix('Py::asObject(new ').removeprefix('new ')
                cType = cType.split('(', maxsplit=1)[0]
                classWithModule = getClassWithModulesFromPointer(cType)
                if mod := getModuleName(classWithModule):
                    self.requiredImports.add(mod)
                return classWithModule

            case _ if returnText.endswith('->getPyObject()') \
                      or returnText.endswith('.getPyObject()'):
                pass  # TODO P2 guess python type from cpp type - find variable name
                return 'object'

            case _ if returnText.startswith('Py_BuildValue("'):
                fc = findFunctionCall(
                    returnText, bodyStart=len('Py_BuildValue'), bracketL='(', bracketR=')',
                ).removeprefix('(').removesuffix(')')
                funArgs = list(generateExpressionUntilChar(
                    fc, 0, ',', bracketL='(', bracketR=')'))
                formatText = funArgs[0].removeprefix('"').removesuffix('"')
                if pythonType := parsePyBuildValues(formatText):
                    if pythonType == 'object':
                        objArg = funArgs[1].strip()
                        pythonType = self._getReturnTypeForText(objArg, endPos, onlyLiteral=True)
                    return pythonType

            case _ if 'Py_True' in returnText \
                      or 'Py_False' in returnText:
                # must be before identifier and should be after Py_BuildValue
                return 'bool'

            case _ if returnText.startswith('Py::asObject(') \
                      or returnText.startswith('Py::Object('):
                fc = findFunctionCall(
                    returnText, bodyStart=returnText.find('('),
                    bracketL='(', bracketR=')').removeprefix('(').removesuffix(')')
                funArgs = list(generateExpressionUntilChar(
                    fc, 0, ',', bracketL='(', bracketR=')'))
                rawReturnVarName = funArgs[0]
                return self._findVariableType(rawReturnVarName, endPos)

            case _ if onlyLiteral:
                return 'object'

            case _ if returnText.isidentifier():
                return self._findVariableType(returnText, endPos)

            case _:
                logger.warning(f"Unknown return variable: '{returnText}'")

        return None

    def _findVariableType(self, variableName: str, endPos: int) -> str | None:
        if variableName == 'this':
            assert self.classNameWithModule is not None
            return self.classNameWithModule

        variableDec = re.compile(rf'([\w:]+)\s*\*?\s*\b{variableName}\b(?:\s*=\s*(.*);)?')
        for match in variableDec.finditer(self.functionBody, endpos=endPos):
            varTypeDec = match.group(1)
            if varTypeDec in ('auto', 'PyObject', 'Py::Object'):
                if assignValue := match.group(2):
                    #  we can try resolve real type by checking right side
                    # TODO P3 search for more assignment expr
                    varType = self._getReturnTypeForText(assignValue, endPos, onlyLiteral=True)
                else:
                    varType = 'object'
            else:
                varType = self._getReturnTypeForText(varTypeDec, endPos, onlyLiteral=True)
            return varType

        varType = self._getReturnTypeForText(variableName, endPos, onlyLiteral=True)
        if varType is None:
            raise ValueError(f"Not found variable declaration for '{variableName}'")
        return varType
