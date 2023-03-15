import logging
import re
from collections.abc import Iterable

from freecad_stub_gen.generators.common.annotation_parameter import AnnotationParam
from freecad_stub_gen.generators.common.cpp_function import findFunctionCall
from freecad_stub_gen.generators.common.doc_string import formatDocstring
from freecad_stub_gen.generators.common.names import getClassWithModulesFromPointer, getModuleName
from freecad_stub_gen.generators.common.return_type_converter.str_wrapper import StrWrapper
from freecad_stub_gen.generators.from_cpp.base import BaseGeneratorFromCpp
from freecad_stub_gen.importable_map import importableMap
from freecad_stub_gen.util import indent, readContent

logger = logging.getLogger(__name__)


class FreecadStubGeneratorFromCppClass(BaseGeneratorFromCpp):
    """Generate class from cpp code with methods."""
    REG_INIT_TYPE = re.compile(r'::init_type\([^{;]*{')
    REG_CLASS_NAME = re.compile(r'behaviors\(\)\.name\(\s*"([\w.]+)"\s*\);')
    REG_CLASS_DOC = re.compile(r'behaviors\(\).doc\("((?:[^"\\]|\\.|"\s*")+)"\);')

    def _genStub(self, moduleName: str) -> Iterable[str]:
        for match in self.REG_INIT_TYPE.finditer(self.impContent):
            funcCall = findFunctionCall(self.impContent, match.start())

            classMatch = self.REG_CLASS_NAME.search(funcCall)
            if classMatch:
                className = classMatch.group(1).replace('.', '_')
                self.classNameWithModules = f'{moduleName}.{className}'
            else:
                logger.debug(f'Cannot find function name in {self.baseGenFilePath}')
                continue  # it is a template

            gen = self._findFunctionCallsGen(funcCall)
            result = ''.join(self._genAllMethods(gen, firstParam=AnnotationParam.SELF_PARAM))
            if not result:
                result = 'pass'
            content = indent(result)

            doc = ''
            if importableMap.isImportable(self.classNameWithModules):
                doc = "This class can be imported.\n"
            if docsMatch := self.REG_CLASS_DOC.search(funcCall):
                doc += docsMatch.group(1)
            if doc:
                doc = indent(formatDocstring(doc))

            baseClasses = self._getBaseClasses(className)
            yield f"class {className}{baseClasses}:\n{doc}\n{content}\n"

    REG_BASE_CLASS_INHERITANCE = re.compile(r"""
(?:public|protected|private)\s+     # access modifier
(?P<baseClass>.+?)\s*               # there may be template class with many parameters
(?:{|                               # either end of expression
,\s*(?:public|protected|private)    # or more base classes
)""", re.VERBOSE)

    def _getBaseClasses(self, className: str) -> str:
        if className.endswith('Py'):
            className = className.removesuffix('Py')
        else:
            return ''

        if not (twinHeaderContent := self._getTwinHeaderContent()):
            return ''

        if not (match := re.search(rf"""
class\s+            # keyword `class`
(?:\w+\s+)?         # there may be optional macro: GuiExport|AppExport
{className}\s*:\s*  # original class name
(?P<inh>[^{{]*      # all inherited classes until {{
{{)                 # terminating char {{
""", twinHeaderContent, re.VERBOSE)):
            return ''  # there is no inheritance

        baseClasses = []
        for baseClassMatch in re.finditer(
                self.REG_BASE_CLASS_INHERITANCE, match.group('inh')):
            baseClass = baseClassMatch.group('baseClass').strip()
            if pythonClass := self._getPythonClass(baseClass):
                baseClasses.append(pythonClass)

        if baseClasses:
            return f"({', '.join(baseClasses)})"

        return ''

    def _getTwinHeaderContent(self) -> str | None:
        currentName = self.baseGenFilePath.stem
        if currentName.endswith('Py'):
            twinName = currentName.removesuffix('Py')
            twinFile = self.baseGenFilePath.with_stem(twinName).with_suffix('.h')
            try:
                return readContent(twinFile)
            except OSError:
                # rare case when twin file is with not standard name
                twinFile = self.baseGenFilePath.with_stem(currentName).with_suffix('.h')
                try:
                    return readContent(twinFile)
                except OSError as ose:
                    logger.error(ose)

        return None

    def _getPythonClass(self, baseClass: str) -> str | None:
        match StrWrapper(baseClass):
            case 'QMainWindow':
                classWithModule = 'qtpy.QtWidgets.QMainWindow'
            case StrWrapper('Q'):
                raise ValueError("Unknown qt class")
            case StrWrapper(end='Py'):
                classWithModule = getClassWithModulesFromPointer(baseClass)
            case _:
                return None # Not a python class, or it is a C template class

        if mod := getModuleName(classWithModule):
            self.requiredImports.add(mod)
        return classWithModule
