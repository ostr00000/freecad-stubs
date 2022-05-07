import logging
import re

from freecad_stub_gen.generators.common.cpp_function import generateExpressionUntilChar
from freecad_stub_gen.generators.common.gen_property.macro.alias import PropertyTypeAlias, \
    PropertyTypeVar
from freecad_stub_gen.generators.common.gen_property.macro.base import PropertyMacroBase
from freecad_stub_gen.generators.common.names import useAliasedModule
from freecad_stub_gen.module_namespace import moduleNamespace

logger = logging.getLogger(__name__)
seen = set()


class PropertyMacroSetter(PropertyMacroBase):

    @property
    def pythonSetType(self) -> str:
        if not (typeId := self.TypeId):
            return ''

        requiredTypes = []
        withoutContainer = '{t}'
        container = ''

        match typeId:
            case 'App::PropertyEnumeration':
                return self._getEnumType()

            case ("App::PropertyPercent" | "App::PropertyInteger"
                  | "App::PropertyIntegerConstraint"):
                innerType = 'int'

            case "App::PropertyBool" | "App::PropertyBoolList":
                innerType = 'int | bool'

            case ("App::PropertyFloat" | "App::PropertyFloatList"
                  | "App::PropertyFloatConstraint" | "App::PropertyPrecision"):
                innerType = 'float'

            case ("App::PropertyQuantity" | "App::PropertyDistance" | "App::PropertyFrequency"
                  | "App::PropertySpeed" | "App::PropertyAcceleration" | "App::PropertyPressure"
                  | "App::PropertyForce"
                  | "App::PropertyVacuumPermittivity"):
                innerType = 'str | float | FreeCAD.Quantity | FreeCAD.Unit'

            case ("App::PropertyQuantityConstraint" | "App::PropertyLength"
                  | "App::PropertyArea" | "App::PropertyVolume" | "App::PropertyAngle"):
                container = withoutContainer
                innerType = 'str | float | FreeCAD.Quantity'

            case "App::PropertyPythonObject":
                innerType = 'object'

            case "App::PropertyMap":
                container = withoutContainer
                innerType = 'dict[str, str]'

            case ("App::PropertyPersistentObject" | "App::PropertyUUID" | "App::PropertyFont"
                  | "App::PropertyFile" | "App::PropertyString" | "App::PropertyStringList"
                  | "App::PropertyPath"):
                innerType = 'str'

            case ("App::PropertyLink" | "App::PropertyLinkChild"
                  | "App::PropertyLinkGlobal" | "App::PropertyLinkHidden"
                  | "App::PropertyPlacementLink"):
                innerType = 'FreeCAD.DocumentObject | None'

            case ("App::PropertyLinkSub" | "App::PropertyLinkSubChild"
                  | "App::PropertyLinkSubGlobal" | "App::PropertyLinkSubHidden"):
                requiredTypes = [self.TYPE_LINK_SUB]
                innerType = 'LinkSub_t'

            case ("App::PropertyLinkList" | "App::PropertyLinkListChild"
                  | "App::PropertyLinkListGlobal" | "App::PropertyLinkListHidden"):
                requiredTypes = [self.TYPE_LINK_LIST]
                innerType = 'LinkList_t'
                container = withoutContainer

            case ("App::PropertyLinkSubList" | "App::PropertyLinkSubListChild"
                  | "App::PropertyLinkSubListGlobal" | "App::PropertyLinkSubListHidden"):
                requiredTypes = [self.TYPE_LINK_SUB, self.TYPE_LINK_LIST, self.TYPE_LINK_SUB_LIST]
                innerType = 'LinkSub_t | LinkList_t | LinkSubList_t'
                container = withoutContainer

            case ("App::PropertyXLink" | "App::PropertyXLinkSub"
                  | "App::PropertyXLinkSubList" | "App::PropertyXLinkList"):
                requiredTypes = [self.TYPE_PROPERTY_X]
                innerType = self.TYPE_PROPERTY_X.name

            case "App::PropertyMatrix":
                requiredTypes = [self.TYPE_SEXDECUPLE]
                innerType = f'FreeCAD.Matrix | {self.TYPE_SEXDECUPLE.name}[float]'

            case ("App::PropertyVector" | "App::PropertyVectorDistance" | "App::PropertyPosition"
                  | "App::PropertyDirection" | "App::PropertyVectorList"):
                requiredTypes = [self.TYPE_TRIPLE]
                innerType = f'FreeCAD.Vector | {self.TYPE_TRIPLE.name}[float]'

            case "App::PropertyPlacement":
                innerType = 'FreeCAD.Matrix | FreeCAD.Placement'

            case "App::PropertyColor" | "App::PropertyColorList":
                requiredTypes = [self.TYPE_TRIPLE, self.TYPE_QUADRUPLE]
                innerType = f'{self.TYPE_TRIPLE.name}[float] ' \
                            f'| {self.TYPE_QUADRUPLE.name}[float] | int'

            case "App::PropertyMaterial" | "App::PropertyMaterialList":
                innerType = 'FreeCAD.Material'

            case "App::PropertyFileIncluded":
                requiredTypes = [self.TYPE_STR_IO]
                innerType = '{t} | tuple[{t}, {t}]'.format(t=self.TYPE_STR_IO.name)

            case "App::PropertyExpressionEngine":
                innerType = ''  # read only

            case "Mesh::PropertyMeshKernel":
                mod = moduleNamespace.convertNamespaceToModule('Mesh')
                innerType = f'{mod}.Mesh | list[list[float]]'

            case "Part::PropertyGeometryList":
                innerType = 'Part.Geometry'
            case "Part::PropertyPartShape":
                innerType = 'Part.Shape'

            case "Spreadsheet::PropertySheet":
                innerType = 'Spreadsheet.Sheet'
            case "Spreadsheet::PropertyColumnWidths" | "Spreadsheet::PropertyRowHeights":
                innerType = ''  # read only

            case "TechDraw::PropertyCosmeticVertexList":
                innerType = 'TechDraw.CosmeticVertex'
            case "TechDraw::PropertyCosmeticEdgeList":
                innerType = 'TechDraw.CosmeticEdge'
            case "TechDraw::PropertyCenterLineList":
                innerType = 'TechDraw.CenterLine'
            case "TechDraw::PropertyGeomFormatList":
                innerType = 'TechDraw.GeomFormat'

            case "Sketcher::PropertyConstraintList":
                innerType = 'Sketcher.Constraint'

            case _:
                if typeId not in seen:
                    seen.add(typeId)
                    logger.error(f"Missing setter case for {typeId=}")
                return ''

        if not container:  # chose container only if not chosen yet
            if 'List' in typeId:
                container = 'typing.Iterable[{t}] | dict[int, {t}]'
            elif 'Constraint' in typeId:
                requiredTypes.append(self.TYPE_QUADRUPLE)
                container = f'{{t}} | {self.TYPE_QUADRUPLE.name}[{{t}}]'
            else:
                container = withoutContainer

        result = PropertyTypeAlias.join(requiredTypes)
        result += container.format(t=useAliasedModule(innerType))
        return result

    TYPE_DOC_AND_STR = PropertyTypeAlias(
        'DocAndStr_t', 'tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]')
    TYPE_LINK_SUB = PropertyTypeAlias(
        'LinkSub_t', "FreeCAD.DocumentObject | None | tuple[()] | DocAndStr_t", TYPE_DOC_AND_STR)
    TYPE_LINK_LIST = PropertyTypeAlias(
        'LinkList_t', 'None | FreeCAD.DocumentObject')
    TYPE_SEQ_DOC = PropertyTypeAlias(
        'SequenceDoc_t', 'tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]')
    TYPE_SEQ_NONE = PropertyTypeAlias(
        'SequenceNone_t', 'tuple[None, typing.Any]')
    TYPE_PROPERTY_X = PropertyTypeAlias(
        'PropX_t', 'None | FreeCAD.DocumentObject | SequenceNone_t | SequenceDoc_t',
        TYPE_SEQ_NONE, TYPE_SEQ_DOC)
    TYPE_LINK_SUB_LIST = PropertyTypeAlias(
        'LinkSubList_t', 'typing.Sequence[SequenceDoc_t | FreeCAD.DocumentObject]', TYPE_SEQ_DOC)
    TYPE_STR_IO = PropertyTypeAlias('StrIO_t', 'str | bytes | io.IOBase')

    TYPE_PARAM_T = PropertyTypeVar('_T')
    TYPE_TRIPLE = PropertyTypeAlias('Triple_t', 'tuple[_T, _T, _T]', TYPE_PARAM_T)
    TYPE_QUADRUPLE = PropertyTypeAlias('Quadruple_t', 'tuple[_T, _T, _T, _T]', TYPE_PARAM_T)
    # https://en.wikipedia.org/wiki/Tuple#Names_for_tuples_of_specific_lengths
    TYPE_SEXDECUPLE = PropertyTypeAlias(
        'Sexdecuple_t', f'tuple[{", ".join("_T" for _ in range(16))}]', TYPE_PARAM_T)

    REG_PATTERN_ENUM_VAR_NAME = r'{}\.setEnums\(\s*(\w+)\s*\)'
    REG_PATTERN_ENUM_ARRAY = r'{}\s*\[\s*]\s*=\s*([^;]+)'

    def _getEnumType(self) -> str:
        reg = self.REG_PATTERN_ENUM_VAR_NAME.format(self.name)
        if varNameMatch := re.search(reg, self.constructorBody):
            reg = self.REG_PATTERN_ENUM_ARRAY.format(varNameMatch.group(1))

            if match := re.search(reg, self.constructorBody):
                literalsRaw = match.group(1)
            elif match := re.search(reg, self.cppContent):
                literalsRaw = match.group(1)
            else:
                raise ValueError("Cannot find enum variable")

            literalsStart = literalsRaw.find('{') + 1
            literalsArray = [exp.strip().removeprefix('"').removesuffix('"')
                             for exp in generateExpressionUntilChar(
                    literalsRaw, literalsStart, ",", bracketL='{', bracketR='}')]
            literalsArray = literalsArray[:-1]  # remove NULL

            return f'typing.Literal{literalsArray}'

        logger.error(f"Unknown enum values for {self.namespace=} {self.group=} {self.name=}")
        return ''
