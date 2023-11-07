from freecad_stub_gen.generators.common.gen_property.macro.getter_type import (
    PropertyMacroGetter,
)
from freecad_stub_gen.generators.common.gen_property.macro.setter_type import (
    PropertyMacroSetter,
)
from freecad_stub_gen.generators.common.gen_property.property_type import PropertyType


class PropertyMacro(PropertyMacroGetter, PropertyMacroSetter):
    @property
    def docs(self):
        result = '\n'

        for p in self.type:
            result += f'[{p.name}] {p.description}.\n'

        if self.group:
            result += f'Property group: {self.group}.\n'

        if self.typeId:
            result += f'Property TypeId: {self.typeId}.\n'

        if self._docs:
            result += self._docs + '\n'

        return result

    @property
    def readOnly(self):
        res = bool(self.type & PropertyType.Prop_ReadOnly)
        if not res and self.typeId == "App::PropertyExpressionEngine":
            res = True
        return res
