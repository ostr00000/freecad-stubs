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

    def __init__(self, requiredImports: OrderedSet, functionBody: str):
        self.requiredImports = requiredImports
        self.functionBody = functionBody

    def getReturnType(self):
        returnTypes = OrderedSet(self._getReturnType())
        if not returnTypes:
            return Signature.empty
        return RawRepr(*returnTypes)

    def _getReturnType(self):
        for match in self.REG_RETURN.finditer(self.functionBody):
            returnText = match.group(1).strip()
            if returnText.startswith('(') and returnText.endswith(')'):
                returnText = returnText.removeprefix('(').removesuffix(')')

            match returnText:
                case 'Py_None' | 'Py::None()' | 'Py_Return':
                    yield 'None'
                case '0' | '-1' | 'NULL' | 'nullptr' | '0L':
                    continue  # an exception

                case _ if returnText.startswith('Py::Boolean') \
                          or returnText.startswith('PyBool_From'):
                    yield 'bool'
                case _ if returnText.startswith('Py::Long') \
                          or returnText.startswith('PyLong_From'):
                    yield 'int'
                case _ if returnText.startswith('Py::Float') \
                          or returnText.startswith('PyFloat_From'):
                    yield 'float'
                case _ if returnText.startswith('Py::String') \
                          or returnText.startswith('PyUnicode_From'):
                    yield 'str'

                case _ if returnText.startswith('new ') \
                          or returnText.startswith('Py::asObject(new '):
                    cType = returnText.removeprefix('Py::asObject(new ').removeprefix('new ')
                    cType = cType.split('(', maxsplit=1)[0]
                    classWithModule = getClassWithModulesFromPointer(cType)
                    if mod := getModuleName(classWithModule):
                        self.requiredImports.add(mod)
                    yield classWithModule

                case _ if returnText.startswith('Py::asObject(') \
                          or returnText.startswith('Py::new_reference_to(') \
                          or returnText.startswith('new_reference_to(') \
                          or returnText.startswith('Py::Object(') \
                          or returnText.isidentifier():
                    pass  # TODO P2 new object from some variable

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
                            pythonType = self._parseObject(objArg)
                        yield pythonType

                case _ if returnText.endswith('->getPyObject()') \
                          or returnText.endswith('.getPyObject()'):
                    pass  # TODO P2 guess python type from cpp type - find variable name

                case _:
                    logger.warning(f"Unknown return variable: '{returnText}'")

    @staticmethod
    def _parseObject(objText: str):
        if 'Py_True' in objText or 'Py_False' in objText:
            return 'bool'

        logger.debug(f"Possible object extraction: {objText}")
        return 'object'
