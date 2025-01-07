import logging
import re
from collections import defaultdict
from operator import itemgetter

from stub_gen.decorators import logCurrentTaskDecFactory

from freecad_stub_gen.file_functions import genCppFiles, readContent
from freecad_stub_gen.FreeCADTemplates import additionalPath
from freecad_stub_gen.python_code import indent

initType = re.compile(r'(\w[\w: ]+?)\s*::init\(\)')
logger = logging.getLogger(__name__)

_PrefixToTypes_t = dict[str, set[tuple[str, str]]]


@logCurrentTaskDecFactory(msg="Searching for FreeCAD type consts")
def _searchTypes() -> _PrefixToTypes_t:
    prefixToTypes: _PrefixToTypes_t = defaultdict(set)
    for filePath in genCppFiles():
        fileContent = readContent(filePath)

        for match in initType.finditer(fileContent):
            originalType = match.group(1).replace(' ', '')
            typeName = originalType.replace('::', '_')

            if '_' in typeName:
                prefix, name = typeName.split('_', maxsplit=1)
                if not prefix:
                    continue
            else:
                prefix = 'Common'
                name = typeName

            prefixToTypes[prefix].add((name, originalType))

    return prefixToTypes


@logCurrentTaskDecFactory(msg="Generating FreeCAD type content")
def _generateContent(prefixToTypes: _PrefixToTypes_t):
    typeText = '# fmt: off\n'  # disable `black` formatting for this file
    for prefix, typeNames in sorted(prefixToTypes.items(), key=itemgetter(0)):
        klassText = f'class {prefix}:\n'
        body = '\n'.join(
            f"{name} = '{originalType}'" for name, originalType in sorted(typeNames)
        )
        typeText += klassText + indent(body) + '\n\n\n'

    typeText = typeText.rstrip() + '\n'

    typesPath = additionalPath / 'type_consts.py'
    with typesPath.open('w', encoding='utf-8') as outputFile:
        outputFile.write(typeText)


def generateTypes():
    prefixToTypes = _searchTypes()
    _generateContent(prefixToTypes)
