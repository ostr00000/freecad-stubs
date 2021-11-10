import re
from dataclasses import dataclass
from enum import auto, Enum
from functools import cached_property
from inspect import Signature

from freecad_stub_gen.generators.common.annotation_parameter import RawRepr
from freecad_stub_gen.generators.common.arguments_converter import logger
from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.common.names import getClassWithModulesFromPointer, getModuleName
from freecad_stub_gen.generators.common.py_build_converter import parsePyBuildValues
from freecad_stub_gen.util import OrderedSet


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
        match StrWrapper(returnText):
            case 'Py::Object()':
                # we must use `Union` wrapper,
                # otherwise `object` may be ignored if there are no other types
                return 'typing.Union[object]'
            case 'Py_None' | 'Py::None()' | 'Py_Return':
                return 'None'
            case '0' | '-1' | 'NULL' | 'nullptr' | '0L':
                return  # an exception

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
                return 'list'  # TODO P3 maybe extract parametrized type?
            case StrWrapper('Py::Dict' | 'PyDict_New'):
                return 'dict'
            case StrWrapper('Py::Callable'):
                return 'typing.Callable'

            # PyCXX wrapper classes, search for `typedef GeometryT<`
            case StrWrapper('Py::BoundingBox('):
                return 'FreeCAD.BoundingBox'
            case StrWrapper('Py::Matrix('):
                return 'FreeCAD.Matrix'
            case StrWrapper('Py::Rotation('):
                return 'FreeCAD.Rotation'
            case StrWrapper('Py::Placement('):
                return 'FreeCAD.Placement'
            # typedef PythonClassObject<Base::Vector2dPy> Vector2d;
            case StrWrapper('Py::Vector2d('):
                return 'FreeCAD.Vector2d'
            case StrWrapper('Py::Vector('):
                return 'FreeCAD.Vector'

            case StrWrapper('shape2pyshape' | 'Part::shape2pyshape'):
                return 'Part.Shape'

            # TODO P2 findCentroid do not return Vector

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
                return 'object'

            case StrWrapper('new ' | 'Py::asObject(new '):
                return self._findClassWithModule(returnText)
            case StrWrapper(end='Py') as i if i.isidentifier() and i[0].isupper():
                return self._findClassWithModule(returnText)

            case StrWrapper(end='->getPyObject()' | '.getPyObject()'):
                pass  # TODO P2 guess python type from cpp type - find variable name
                return 'object'

            case StrWrapper('Py_BuildValue("'):
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
                return self._findVariableType(rawReturnVarName, endPos)

            case _ if onlyLiteral:
                return 'object'

            case _ if returnText.isidentifier():
                return self._findVariableType(returnText, endPos)

            case _:
                logger.warning(f"Unknown return variable: '{returnText}'")

        return None

    def _findClassWithModule(self, text: str):
        cType = text.removeprefix('Py::asObject(new ').removeprefix('new ')
        cType = cType.split('(', maxsplit=1)[0]
        classWithModule = getClassWithModulesFromPointer(cType)
        if mod := getModuleName(classWithModule):
            self.requiredImports.add(mod)
        return classWithModule

    def _findVariableType(self, variableName: str, endPos: int) -> str | None:
        if variableName == 'this':
            assert self.classNameWithModule is not None
            return self.classNameWithModule

        variableDec = re.compile(rf'([\w:]+)\s*\*?\s*\b{variableName}\b(?:\s*=\s*(.*);)?')
        for declarationMatch in variableDec.finditer(self.functionBody, endpos=endPos):
            varTypeDec = declarationMatch.group(1)
            if varTypeDec in ('auto', 'PyObject', 'Py::Object'):
                if assignValue := declarationMatch.group(2):
                    #  we can try resolve real type by checking right side
                    varType = self._getReturnTypeForText(assignValue, endPos, onlyLiteral=True)
                else:
                    varType = 'object'

            else:
                varType = self._getReturnTypeForText(varTypeDec, endPos, onlyLiteral=True)

            if varType is None or varType == 'object':
                variableDec = re.compile(rf'{variableName}\b\s*=\s*(.*);')
                for assignmentMatch in variableDec.finditer(
                        self.functionBody, pos=declarationMatch.end(), endpos=endPos):
                    assignValue = assignmentMatch.group(1)
                    varType = self._getReturnTypeForText(assignValue, endPos, onlyLiteral=True)
                    if not (varType is None or varType == 'object'):
                        break

            return varType

        varType = self._getReturnTypeForText(variableName, endPos, onlyLiteral=True)
        if varType is None:
            raise ValueError(f"Not found variable declaration for '{variableName}'")
        return varType
