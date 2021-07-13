import re
from collections import defaultdict
from operator import itemgetter

from freecad_stub_gen.additional import additionalPath
from freecad_stub_gen.generators.base import commentRemover, BaseGenerator
from freecad_stub_gen.module_map import genPyCppFiles

initType = re.compile(r'(\w[\w: ]+?)\s*::init\(\)')


def generateTypes():
    prefixToTypes: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for filePath in genPyCppFiles():
        with open(filePath) as file:
            try:
                fileContent = commentRemover(file.read())
            except UnicodeDecodeError:
                continue

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

    typeText = ''
    for prefix, typeNames in sorted(
            prefixToTypes.items(), key=itemgetter(0)):
        klassText = f'class {prefix}:\n'
        body = '\n'.join(f"{name} = '{originalType}'"
                         for name, originalType in sorted(typeNames))
        typeText += klassText + BaseGenerator.indent(body) + '\n\n\n'

    typeText = typeText.rstrip() + '\n'

    with open(additionalPath / 'FreeCADTypes.py', 'w') as outputFile:
        outputFile.write(typeText)
