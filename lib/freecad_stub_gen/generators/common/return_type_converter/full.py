import re
from inspect import Signature

from freecad_stub_gen.generators.common.annotation_parameter import RawRepr
from freecad_stub_gen.generators.common.return_type_converter.arg_types import InvalidReturnType, \
    UnionArguments
from freecad_stub_gen.generators.common.return_type_converter.base import ReturnTypeConverterBase
from freecad_stub_gen.generators.common.return_type_converter.inner_type_dict import \
    ReturnTypeInnerDict
from freecad_stub_gen.generators.common.return_type_converter.inner_type_list import \
    ReturnTypeInnerList
from freecad_stub_gen.generators.common.return_type_converter.inner_type_tuple import \
    ReturnTypeInnerTuple
from freecad_stub_gen.util import OrderedSet


class ReturnTypeConverter(
    ReturnTypeInnerList, ReturnTypeInnerTuple, ReturnTypeInnerDict, ReturnTypeConverterBase
):
    REG_RETURN = re.compile(r'return ([^;]+);')

    def getStrReturnType(self) -> str:
        if (ret := self.getReturnType()) != Signature.empty:
            return str(ret)
        return 'object'

    def getReturnType(self):
        returnTypes = OrderedSet(self._genReturnType())
        return RawRepr(*returnTypes)

    def _genReturnType(self):
        for match in self.REG_RETURN.finditer(self.functionBody):
            try:
                retType = self._getReturnTypeForText(match.group(1), match.end())
            except InvalidReturnType:
                continue
            if not isinstance(retType, UnionArguments):
                retType = UnionArguments((retType,))
            yield from retType
            self.requiredImports.update(retType.imports)
