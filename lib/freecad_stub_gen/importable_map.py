import logging
import re
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass
from functools import cached_property

from freecad_stub_gen.cpp_code.converters import removeQuote
from freecad_stub_gen.file_functions import genCppFiles, readContent
from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar
from freecad_stub_gen.module_namespace import moduleNamespace

logger = logging.getLogger(__name__)


@dataclass
class AddTypeArguments:
    cFullType: str
    moduleName: str
    pythonName: str

    @cached_property
    def namespace(self) -> str | None:
        if '::' in self.cFullType:
            return self.cFullType.split('::', maxsplit=1)[0]
        return None

    @cached_property
    def cTypeWithoutNamespace(self) -> str:
        if '::' in self.cFullType:
            return self.cFullType.split('::', maxsplit=1)[1]
        return self.cFullType

    @cached_property
    def fullPythonName(self):
        if self.namespace:
            module = moduleNamespace.convertNamespaceToModule(self.namespace)
            return f'{module}.{self.pythonName}'
        return self.pythonName

    def __post_init__(self):
        self.cFullType = (
            self.cFullType.removeprefix('&')
            .removesuffix('::type_object()')
            .removesuffix('::Type')
        )

        self.pythonName = removeQuote(self.pythonName)


class ImportableClassMap(dict[str, str]):
    """This dict map c++ class name to python name available in imports."""

    # there are some types that are renamed in code
    # https://github.com/FreeCAD/FreeCAD/blob/8ac722c1e89ef530564293efd30987db09017e12/src/Mod/Part/App/AppPart.cpp#L226
    # regex to find non-matching names:
    # Base::Interpreter\(\).addType\(\&\w+::(\w+)Py\s*::Type,\s*\w+,"(?!\1")

    def __init__(self):
        self.dup = defaultdict[str, set[str]](set)
        # remove duplicated keys - not all classes have namespace
        super().__init__(self._filterDuplicatedKeys(self._genTypes()))
        for duplicatedKey in self.dup:
            del self[duplicatedKey]

    def isImportable(self, className: str):
        return className in self.values() or any(
            className in duplicatedSet for duplicatedSet in self.dup.values()
        )

    def _filterDuplicatedKeys(self, it: Iterable[tuple[str, str]]):
        seen: dict[str, str] = {}
        for key, val in it:
            if key in seen:
                self.dup[key].add(seen[key])
                self.dup[key].add(val)
            else:
                seen[key] = val

            yield key, val

    REG_ADD_TYPE = re.compile(
        r'Base\s*:\s*:\s*Interpreter\s*\(\s*\)\s*\.\s*addType\s*\('
    )

    def _genTypes(self):
        logger.info("Generating types for importable map...")
        for cppFile in genCppFiles():
            cppContent = readContent(cppFile)
            for match in self.REG_ADD_TYPE.finditer(cppContent):
                addTypeList = [
                    c.replace(' ', '').replace('\n', '')
                    for c in generateExpressionUntilChar(
                        cppContent, match.end(), ',', bracketL='(', bracketR=')'
                    )
                ]

                addTypeArgs = AddTypeArguments(*addTypeList)
                yield addTypeArgs.cTypeWithoutNamespace, addTypeArgs.fullPythonName
        logger.info("Generating types for importable map - finished.")


__all__ = ['importableMap']
importableMap = ImportableClassMap()
