import logging

from freecad_stub_gen.generators.common.gen_property.macro.base import PropertyMacroBase
from freecad_stub_gen.generators.common.names import useAliasedModule
from freecad_stub_gen.module_namespace import moduleNamespace

logger = logging.getLogger(__name__)
seen = set()


class PropertyMacroGetter(PropertyMacroBase):
    @property
    def pythonGetType(self) -> str:
        if not (typeId := self.typeId):
            return ''

        if 'List' in typeId:
            container = 'list[{t}]'
        else:
            container = '{t}'

        match typeId:
            case (
                "App::PropertyInteger"
                | "App::PropertyIntegerConstraint"
                | "App::PropertyEnumeration"
                | "App::PropertyPercent"
            ):
                innerType = 'int'

            case "App::PropertyBool" | "App::PropertyBoolList":
                innerType = 'bool'
                if typeId == "App::PropertyBoolList":
                    container = 'tuple[{t}, ...]'

            case (
                "App::PropertyFloat"
                | "App::PropertyFloatConstraint"
                | "App::PropertyPrecision"
                | "App::PropertyFloatList"
            ):
                innerType = 'float'

            case (
                "App::PropertyQuantity"
                | "App::PropertyDistance"
                | "App::PropertyFrequency"
                | "App::PropertySpeed"
                | "App::PropertyAcceleration"
                | "App::PropertyPressure"
                | "App::PropertyStiffness"
                | "App::PropertyForce"
                | "App::PropertyVacuumPermittivity"
                | "App::PropertyQuantityConstraint"
                | "App::PropertyLength"
                | "App::PropertyArea"
                | "App::PropertyVolume"
                | "App::PropertyAngle"
            ):
                innerType = 'FreeCAD.Quantity'

            case "App::PropertyPersistentObject" | "App::PropertyPythonObject":
                innerType = 'object'

            case "App::PropertyMap":
                innerType = 'dict[str, str]'

            case (
                "App::PropertyString"
                | "App::PropertyUUID"
                | "App::PropertyFont"
                | "App::PropertyFile"
                | "App::PropertyPath"
                | "App::PropertyFileIncluded"
                | "App::PropertyStringList"
            ):
                innerType = 'str'

            case (
                "App::PropertyLink"
                | "App::PropertyLinkChild"
                | "App::PropertyLinkGlobal"
                | "App::PropertyLinkHidden"
                | "App::PropertyPlacementLink"
            ):
                innerType = 'FreeCAD.DocumentObject | None'

            case (
                "App::PropertyLinkSub"
                | "App::PropertyLinkSubChild"
                | "App::PropertyLinkSubGlobal"
                | "App::PropertyLinkSubHidden"
            ):
                innerType = 'tuple[FreeCAD.DocumentObject, list[str]] | None'

            case (
                "App::PropertyLinkList"
                | "App::PropertyLinkListChild"
                | "App::PropertyLinkListGlobal"
                | "App::PropertyLinkListHidden"
            ):
                innerType = 'FreeCAD.DocumentObject | None'

            case (
                "App::PropertyLinkSubList"
                | "App::PropertyLinkSubListChild"
                | "App::PropertyLinkSubListGlobal"
                | "App::PropertyLinkSubListHidden"
            ):
                innerType = 'tuple[FreeCAD.DocumentObject, list[str]]'

            case "App::PropertyXLink":
                innerType = (
                    'None | FreeCAD.DocumentObject '
                    '| tuple[FreeCAD.DocumentObject, str | list[str]]'
                )
            case "App::PropertyXLinkSub":
                innerType = 'None | tuple[FreeCAD.DocumentObject | list[str]]'
            case "App::PropertyXLinkSubList":
                innerType = 'tuple[FreeCAD.DocumentObject, list[str]]'
            case "App::PropertyXLinkList":
                innerType = 'tuple[FreeCAD.DocumentObject, list[str]]'
                container += ' | list[FreeCAD.DocumentObject]'

            case "App::PropertyMatrix":
                innerType = 'FreeCAD.Matrix'

            case "App::PropertyColor" | "App::PropertyColorList":
                partResult = 'tuple[{t}, {t}, {t}, {t}]'
                innerType = partResult.format(t='float')

            case "App::PropertyMaterial":
                innerType = 'FreeCAD.Material'

            case (
                "App::PropertyVector"
                | "App::PropertyVectorDistance"
                | "App::PropertyPosition"
                | "App::PropertyDirection"
                | "App::PropertyVectorList"
            ):
                innerType = 'FreeCAD.Vector'

            case "App::PropertyPlacement":
                innerType = 'FreeCAD.Placement'

            case "App::PropertyMaterialList":
                innerType = 'tuple[FreeCAD.Material, ...]'

            case "App::PropertyExpressionEngine":
                innerType = 'list[tuple[str, str]]'

            case "Mesh::PropertyMeshKernel":
                mod = moduleNamespace.convertNamespaceToModule('Mesh')
                innerType = f'{mod}.Mesh'

            case "Part::PropertyGeometryList":
                innerType = 'Part.Geometry'
            case "Part::PropertyPartShape":
                innerType = 'Part.Shape'

            case "Spreadsheet::PropertySheet":
                innerType = 'Spreadsheet.Sheet'
            case "Spreadsheet::PropertyColumnWidths":
                innerType = 'Spreadsheet.PropertyColumnWidths'
            case "Spreadsheet::PropertyRowHeights":
                innerType = 'Spreadsheet.PropertyRowHeights'

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
                    logger.error(f"Missing getter case for {typeId=}")
                return ''

        return container.format(t=useAliasedModule(innerType))
