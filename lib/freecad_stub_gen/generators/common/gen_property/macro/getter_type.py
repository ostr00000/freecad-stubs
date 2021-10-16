from freecad_stub_gen.generators.common.gen_property.macro.base import PropertyMacroBase
from freecad_stub_gen.generators.common.gen_property.macro.setter_type import PropertyMacroSetter


class PropertyMacroGetter(PropertyMacroSetter, PropertyMacroBase):

    @property
    def pythonGetType(self) -> str:
        return self.pythonSetType
