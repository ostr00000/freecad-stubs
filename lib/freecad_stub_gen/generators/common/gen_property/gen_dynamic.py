import re
from abc import ABC
from collections.abc import Iterable
from functools import cached_property
from itertools import chain

from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.common.gen_property.gen_base import \
    BasePropertyGenerator
from freecad_stub_gen.generators.common.gen_property.macro.full import PropertyMacro


class DynamicPropertyGenerator(BasePropertyGenerator, ABC):

    def getCppClassName(self) -> str:
        raise NotImplementedError

    def getCppContent(self) -> str | None:
        raise NotImplementedError

    def getHContent(self) -> str | None:
        raise NotImplementedError

    REG_DYNAMIC_PROPERTY = re.compile(r'\bADD_PROPERTY\(')
    REG_DYNAMIC_PROPERTY_TYPE = re.compile(r'\bADD_PROPERTY_TYPE\(')
    REG_DYNAMIC_PROPERTY_EXP = re.compile(r'\bEXTENSION_ADD_PROPERTY\(')
    REG_DYNAMIC_PROPERTY_EXP_TYPE = re.compile(r'\bEXTENSION_ADD_PROPERTY_TYPE\(')

    REG_PATTERN_CLASS_DEC = r'class .*\b{}[^{{]*'

    def genDynamicProperties(self) -> Iterable[str]:
        """This function search for dynamic properties added in cpp code."""
        if not (cppIncludeContent := self.getCppContent()):
            return

        cppClassName = self.getCppClassName()

        # there may be few separated declarations (ex. DocumentObject)
        hIncludeContent = self.getHContent()
        reg = re.compile(self.REG_PATTERN_CLASS_DEC.format(cppClassName))
        classDeclarationBodies = [
            findFunctionCall(hIncludeContent, classMatch.start())
            for classMatch in re.finditer(reg, hIncludeContent)]

        for match in re.finditer(f'{cppClassName}::{cppClassName}', cppIncludeContent):
            constructorBody = findFunctionCall(cppIncludeContent, match.start())
            for propMatch in chain(
                    re.finditer(self.REG_DYNAMIC_PROPERTY, constructorBody),
                    re.finditer(self.REG_DYNAMIC_PROPERTY_TYPE, constructorBody),
                    re.finditer(self.REG_DYNAMIC_PROPERTY_EXP, constructorBody),
                    re.finditer(self.REG_DYNAMIC_PROPERTY_EXP_TYPE, constructorBody)
            ):
                macroBody = findFunctionCall(
                    constructorBody, propMatch.start(), bracketL='(', bracketR=')')
                macroCallStartPos = macroBody.find('(') + 1
                macroArgs = [exp.strip() for exp in generateExpressionUntilChar(
                    macroBody, expStart=macroCallStartPos, splitChar=',')]

                pm = PropertyMacro(
                    *macroArgs, constructorBody=constructorBody, namespace=self._curNamespace,
                    cppContent=cppIncludeContent, classDeclarationBodies=classDeclarationBodies)
                yield self.getProperty(
                    pm.name, pm.pythonGetType, pm.pythonSetType,
                    docs=pm.docs, readOnly=pm.readOnly)

            # We assume that they may be more than one constructor,
            # but each constructor add the same properties.
            break

    @cached_property
    def _curNamespace(self):
        parts = self.baseGenFilePath.parts
        try:
            index = parts.index('Mod')
            namespace = parts[index + 1]
        except ValueError:
            for k in ('App', 'Gui'):
                if k in parts:
                    namespace = k
                    break
            else:
                raise ValueError

        return namespace
