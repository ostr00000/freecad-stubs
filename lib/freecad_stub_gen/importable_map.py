import logging
import re
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass, field

from freecad_stub_gen.cpp_code.converters import removeQuote
from freecad_stub_gen.decorators import logCurrentTaskDecFactory
from freecad_stub_gen.file_functions import genCppFiles, readContent
from freecad_stub_gen.generators.common.context import (
    getCurrentNamespace,
    initContext,
    isolatedContext,
)
from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar
from freecad_stub_gen.generators.common.names import (
    convertNamespaceToModule,
    removeAffix,
)

logger = logging.getLogger(__name__)


@dataclass
class AddTypeArguments:
    cFullType: str
    moduleName: str
    pythonName: str
    namespace: str = field(init=False)

    def __post_init__(self):
        self.cFullType = removeAffix(self.cFullType, '&', ('::type_object()', '::Type'))

        self.pythonName = removeQuote(self.pythonName)
        self.namespace = self._getNamespace()

    def _getNamespace(self) -> str:
        if '::' in self.cFullType:
            return self.cFullType.rsplit('::', maxsplit=1)[0]
        return getCurrentNamespace()

    @property
    def cTypeWithoutNamespace(self) -> str:
        if '::' in self.cFullType:
            return self.cFullType.rsplit('::', maxsplit=1)[1]
        return self.cFullType

    @property
    def fullPythonName(self):
        module = convertNamespaceToModule(self.namespace)
        return f'{module}.{self.pythonName}'


class ImportableClassMap(dict[str, str]):
    """This dict map c++ class name to python name available in imports."""

    # there are some types that are renamed in code
    # https://github.com/FreeCAD/FreeCAD/blob/8ac722c1e89ef530564293efd30987db09017e12/src/Mod/Part/App/AppPart.cpp#L226
    # regex to find non-matching names:
    # Base::Interpreter\(\).addType\(\&\w+::(\w+)Py\s*::Type,\s*\w+,"(?!\1")

    @logCurrentTaskDecFactory(msg="Generating types for importable map")
    def __init__(self):
        self.namespaceAndClassToPython = {}
        self.dup = defaultdict[str, set[str]](set)

        with isolatedContext():
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
        for cppFile in genCppFiles():
            initContext(cppFile)
            cppContent = readContent(cppFile)
            for match in self.REG_ADD_TYPE.finditer(cppContent):
                addTypeList = [
                    c.replace(' ', '').replace('\n', '')
                    for c in generateExpressionUntilChar(
                        cppContent, match.end(), ',', bracketL='(', bracketR=')'
                    )
                ]

                ata = AddTypeArguments(*addTypeList)
                # TODO @PO: [P2] verify `namespaceAndClass` vs `cTypeWithoutNamespace`
                self.namespaceAndClassToPython[ata.cTypeWithoutNamespace] = (
                    ata.fullPythonName
                )
                yield ata.cTypeWithoutNamespace, ata.fullPythonName


__all__ = ['importableMap']
importableMap = ImportableClassMap()
