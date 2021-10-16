from freecad_stub_gen.generators.common.gen_property.macro.base import PropertyMacroBase


class PropertyMacroSetter(PropertyMacroBase):

    @property
    def pythonSetType(self) -> str:
        if not (typeId := self.TypeId):
            return ''

        constraint = '{t} | tuple[{t}, {t}, {t}, {t}]'
        match typeId, typeId.lower():
            case _, listProp if 'list' in listProp:
                container = 'dict[int, {t}] | typing.Iterable[{t}] | typing.Sequence[{t}]'
            case _, listProp if 'set' in listProp:
                container = 'typing.Sequence[{t}] | {t}'
            case (_, constraintProp) if 'constraint' in constraintProp:
                container = constraint
            case ("App::PropertyPercent", _):
                container = constraint
            case _:
                container = '{t}'

        match typeId, typeId.lower():
            case 'App::PropertyEnumeration', _:
                return self._getEnumType()

            case (("App::PropertyQuantity" | "App::PropertyDistance" | "App::PropertyFrequency"
                   | "App::PropertySpeed" | "App::PropertyAcceleration"), _):
                innerType = 'str | float | FreeCAD.Quantity | FreeCAD.Unit'

            case (("App::PropertyQuantityConstraint" | "App::PropertyLength" | "App::PropertyArea"
                   | "App::PropertyVolume" | "App::PropertyAngle" | "App::PropertyPressure"
                   | "App::PropertyForce" | "App::PropertyVacuumPermittivity"), _):
                innerType = 'str | float | FreeCAD.Quantity'

            case "App::PropertyPercent", _:
                innerType = 'int'

            case ("App::PropertyFloatConstraint" | "App::PropertyPrecision"), _:
                innerType = 'float | tuple[float, float, float, float]'

            case "App::PropertyMap", _:
                return 'dict[str, str]'

            case "App::PropertyStringList", _:
                innerType = 'str | bytes'

            case ("App::PropertyPersistentObject" | "App::PropertyUUID" | "App::PropertyFont"
                  | "App::PropertyFile"), _:
                return 'str'

            case (("App::PropertyLink" | "App::PropertyLinkChild" | "App::PropertyLinkGlobal" |
                   "App::PropertyLinkHidden" | "App::PropertyLinkList" |
                   "App::PropertyPlacementLink"), _):
                innerType = 'FreeCAD.DocumentObject | None'

            case (("App::PropertyLinkSub" | "App::PropertyLinkSubChild"
                   | "App::PropertyLinkSubGlobal" | "App::PropertyLinkSubHidden"
                   | "App::PropertyLinkListChild" | "App::PropertyLinkListGlobal"
                   | "App::PropertyLinkListHidden" | "App::PropertyLinkSubList"
                   | "App::PropertyLinkSubListChild" | "App::PropertyLinkSubListGlobal"
                   | "App::PropertyLinkSubListHidden" | "App::PropertyXLink"
                   | "App::PropertyXLinkSub" | "App::PropertyXLinkSubList"
                   | "App::PropertyXLinkList" | "App::PropertyXLinkContainer"), _):
                partResult = '{t} | tuple[{t}, {s}] | list[{t} | {s}] | None'
                innerType = partResult.format(
                    t='FreeCAD.DocumentObject', s='str | typing.Sequence[str]')

            case "App::PropertyMatrix", _:
                partResult = 'FreeCAD.Matrix | tuple[{t}]'
                innerType = partResult.format(t=', '.join('float' for _ in range(16)))

            case ("App::PropertyVector" | "App::PropertyVectorDistance" | "App::PropertyPosition"
                  | "App::PropertyDirection" | "App::PropertyVectorList"), _:
                partResult = 'FreeCAD.Vector | tuple[{t}, {t}, {t}]'
                innerType = partResult.format(t='float | int')

            case "App::PropertyPlacement":
                innerType = 'FreeCAD.Matrix | FreeCAD.Placement'

            case ("App::PropertyColor" | "App::PropertyColorList"), _:
                partResult = 'tuple[{t}, {t}, {t}] | tuple[{t}, {t}, {t}, {t}] | int'
                innerType = partResult.format(t='float')

            case ("App::PropertyMaterial" | "App::PropertyMaterialList"), _:
                innerType = 'FreeCAD.Material'

            case "App::PropertyPath":
                innerType = 'Path.Path'  # TODO fix Path (ToolPath)

            case "App::PropertyFileIncluded":
                partResult = '{t} | tuple[{t} {t}]'
                innerType = partResult.format(t='str | bytes | io.IOBase')

            case "App::PropertyPythonObject":
                innerType = 'object'

            case _, low if 'bool' in low:
                innerType = 'int | bool'
            case _, low if 'float' in low:
                innerType = 'float | int'
            case _, low if 'int' in low:
                innerType = 'int'
            case _, low if 'string' in low:
                innerType = 'str'
            case _:
                return ''

        return container.format(t=innerType)
