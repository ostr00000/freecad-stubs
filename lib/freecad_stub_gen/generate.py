import logging
import shutil
import typing
from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR, TARGET_DIR
from freecad_stub_gen.file_functions import genCppFiles, genXmlFiles
from freecad_stub_gen.FreeCADTemplates import additionalPath
from freecad_stub_gen.generators.common.gen_base import BaseGenerator
from freecad_stub_gen.generators.common.names import (
    convertNamespaceToModule,
    getModFromAlias,
)
from freecad_stub_gen.generators.exceptions.gen import ExceptionGenerator
from freecad_stub_gen.generators.from_cpp.functions import (
    FreecadStubGeneratorFromCppFunctions,
)
from freecad_stub_gen.generators.from_cpp.klass import FreecadStubGeneratorFromCppClass
from freecad_stub_gen.generators.from_cpp.module import (
    FreecadStubGeneratorFromCppModule,
)
from freecad_stub_gen.generators.from_xml.full import FreecadStubGeneratorFromXML
from freecad_stub_gen.python_code.module_container import Module

logger = logging.getLogger(__name__)
generators: typing.Sequence[type[BaseGenerator]] = (
    FreecadStubGeneratorFromCppFunctions,
    FreecadStubGeneratorFromCppClass,
    FreecadStubGeneratorFromCppModule,
    ExceptionGenerator,
)


def _genModule(
    sourcesRoot: Module,
    modulePath: Path,
    sourcePath=SOURCE_DIR,
    moduleName='',
    subModuleName='',
):
    for xmlPath in genXmlFiles(modulePath):
        if not (tg := FreecadStubGeneratorFromXML.safeCreate(xmlPath, sourcePath)):
            continue
        tg.getStub(sourcesRoot, moduleName, submodule=subModuleName)

    for cppPath in genCppFiles(modulePath):
        match cppPath.stem:
            # this is special case when we create separate module
            # FreeCAD
            case 'Translate':
                curModuleName = f'{moduleName}._Qt'
            case 'UnitsApiPy':
                curModuleName = f'{moduleName}._Units'
            case 'Console':
                curModuleName = f'{moduleName}._Console'
            case 'TaskDialogPython' as stem:
                curModuleName = f'{moduleName}._{stem}'

            # FreeCADGui
            case 'Selection' as stem:
                curModuleName = f'{moduleName}._{stem}'
            case 'UiLoader':
                curModuleName = f'{moduleName}._PySideUic'

            case _:
                curModuleName = moduleName

        for cl in generators:
            if not (mg := cl.safeCreate(cppPath, sourcePath)):
                continue
            mg.getStub(sourcesRoot, curModuleName)


def improve_FreeCAD(sourcesRoot: Module, sourcePath: Path):
    freeCad = sourcesRoot['FreeCAD']
    freeCad += 'class PyObjectBase(object): ...\n\n\n'

    _genModule(
        sourcesRoot,
        sourcePath / 'Base',
        sourcePath,
        moduleName='FreeCAD',
        subModuleName='Base',
    )
    _genModule(sourcesRoot, sourcePath / 'App', sourcePath, moduleName='FreeCAD')

    freeCad += """
# Be careful with following variables.
# Some of them are set in `FreeCADGui` (`GuiUp` after `InitApplications`),
# so may not exist until `FreeCADGuiInit` is initialized.
# You may want to use `getattr(FreeCAD, 'GuiUp', False)`.
GuiUp: typing.Literal[0, 1]
ActiveDocument: FreeCAD.Document | None
Gui = FreeCADGui
"""

    freeCad += """
# You cannot import these modules in FreeCAD,
# but you can access it from this module ex. `FreeCAD.Console`:
Console = _Console
Units = _Units
Qt = _Qt
    """
    freeCad.imports.update(
        (
            'typing',
            'FreeCADGui',
            'from FreeCAD import _Console',
            'from FreeCAD import _Units',
            'from FreeCAD import _Qt',
            'from FreeCAD import Base as Base',
            'from FreeCAD.Base import *',
        )
    )


def improve_FreeCAD_Base(sourcesRoot: Module):
    freeCadBase = sourcesRoot['FreeCAD.Base']
    freeCadBase.imports.add(
        "from FreeCAD import ProgressIndicator as ProgressIndicator"
    )


def improve_FreeCAD_Units(sourcesRoot: Module):
    freeCADUnits = sourcesRoot['FreeCAD._Units']
    freeCADUnits.imports.update(
        (
            'from FreeCAD.Base import _Unit',
            'from FreeCAD.Base import _Quantity',
        )
    )
    freeCADUnits += UNITS


def improve_FreeCADGui(sourcesRoot: Module, sourcePath: Path):
    _genModule(sourcesRoot, sourcePath / 'Gui', sourcePath, moduleName='FreeCADGui')
    _genModule(sourcesRoot, sourcePath / 'Main', sourcePath, moduleName='FreeCADGui')

    freeCadGui = sourcesRoot['FreeCADGui']
    freeCadGui += 'Workbench = FreeCADGui.PythonWorkbench  # noqa'
    freeCadGui += 'ActiveDocument: FreeCADGui.Document | None'
    freeCadGui += (
        'Control = ControlClass()  # hack to show this module in current module hints'
    )
    freeCadGui += 'Selection = _Selection'
    freeCadGui += 'PySideUic = _PySideUic'
    freeCadGui.imports.update(
        (
            'from FreeCADGui import _Selection',
            'from FreeCADGui import _PySideUic',
            'from FreeCADGui.TaskDialogPython import Control as ControlClass',
        )
    )


def improve_FreeCADGui_PySideUic(sourcesRoot: Module):
    pySideUic = sourcesRoot['FreeCADGui._PySideUic']
    pySideUic.replace(
        'def loadUiType() -> tuple[typing.Any, typing.Any] | None:',
        """
@typing.overload
def loadUi(args: tuple[str]) -> _OptWid_t: ...
@typing.overload
def loadUi(args: tuple[str, qtpy.QtCore.QObject | None]) -> _OptWid_t:
""".rstrip(),
    )
    pySideUic.replace(
        'def loadUi() -> typing.Any | None:',
        """
class _UiGeneratedClass:
    def setupUi(self, widget: qtpy.QtWidgets.QWidget) -> None: ...
    def retranslateUi(self, widget: qtpy.QtWidgets.QWidget) -> None: ...

_LoadRes_t: typing.TypeAlias =  tuple[_UiGeneratedClass, qtpy.QtWidgets.QWidget]

def loadUiType(args: tuple[str]) -> _LoadRes_t | None:
""".rstrip(),
    )
    pySideUic.replace(
        'def createCustomWidget():',
        """
_OptWid_t: typing.TypeAlias = qtpy.QtWidgets.QWidget | None

@typing.overload
def createCustomWidget(args: tuple[str]) -> _OptWid_t: ...
@typing.overload
def createCustomWidget(args: tuple[str, qtpy.QtWidgets.QWidget]) -> _OptWid_t: ...
@typing.overload
def createCustomWidget(args: tuple[str, qtpy.QtWidgets.QWidget, str]) -> _OptWid_t:
""".rstrip(),
    )
    pySideUic.imports.update(('typing', 'qtpy.QtCore', 'qtpy.QtWidgets'))


def improve_Mod(sourcesRoot: Module, sourcePath: Path):
    for mod in (sourcePath / 'Mod').iterdir():
        moduleName = mod.name
        if moduleName == 'Test':
            continue

        moduleName = convertNamespaceToModule(moduleName)
        _genModule(sourcesRoot, mod / 'App', sourcePath, moduleName=moduleName)
        _genModule(sourcesRoot, mod / 'Gui', sourcePath, moduleName=moduleName)


def generateFreeCadStubs(sourcePath=SOURCE_DIR, targetPath=TARGET_DIR):
    sourcesRoot = Module()

    improve_FreeCAD(sourcesRoot, sourcePath)
    improve_FreeCAD_Base(sourcesRoot)
    improve_FreeCAD_Units(sourcesRoot)
    improve_FreeCADGui(sourcesRoot, sourcePath)
    improve_FreeCADGui_PySideUic(sourcesRoot)
    improve_Mod(sourcesRoot, sourcePath)

    sourcesRoot.setSubModulesAsPackage()

    shutil.rmtree(targetPath, ignore_errors=True)
    targetPath.mkdir(parents=True, exist_ok=True)
    (targetPath / '__init__.pyi').touch(exist_ok=True)
    sourcesRoot.save(targetPath)

    for stubPackage in targetPath.iterdir():
        if stubPackage.is_dir():
            if mod := getModFromAlias(stubPackage.name):
                newName = mod
            else:
                newName = stubPackage.name

            stubPackage.rename(stubPackage.with_name(f'{newName}-stubs'))

    shutil.copytree(additionalPath, targetPath / additionalPath.name)


# TODO @PO: [P4] preprocess and remove macros
# https://www.tutorialspoint.com/cplusplus/cpp_preprocessor.htm

UNITS = """
NanoMetre     = Quantity('nm')
MicroMetre    = Quantity('um')
MilliMetre    = Quantity('mm')
CentiMetre    = Quantity('cm')
DeciMetre     = Quantity('dm')
Metre         = Quantity('m')
KiloMetre     = Quantity('km')

MilliLiter    = Quantity('ml')
Liter         = Quantity('l')

Hertz         = Quantity('Hz')
KiloHertz     = Quantity('kHz')
MegaHertz     = Quantity('MHz')
GigaHertz     = Quantity('GHz')
TeraHertz     = Quantity('THz')

MicroGram     = Quantity('ug')
MilliGram     = Quantity('mg')
Gram          = Quantity('g')
KiloGram      = Quantity('kg')
Ton           = Quantity('t')

Second        = Quantity('s')
Minute        = Quantity('min')
Hour          = Quantity('h')

Ampere        = Quantity('A')
MilliAmpere   = Quantity('mA')
KiloAmpere    = Quantity('kA')
MegaAmpere    = Quantity('MA')

Kelvin        = Quantity('K')
MilliKelvin   = Quantity('mK')
MicroKelvin   = Quantity('uK')

MilliMole     = Quantity('mmol')
Mole          = Quantity('mol')

Candela       = Quantity('cd')

Inch          = Quantity('in')
Foot          = Quantity('ft')
Thou          = Quantity('thou')
Yard          = Quantity('yd')
Mile          = Quantity('mi')

SquareFoot    = Quantity('sqft')
CubicFoot     = Quantity('cft')

Pound         = Quantity('lb')
Ounce         = Quantity('oz')
Stone         = Quantity('st')
Hundredweights= Quantity('cwt')

Newton        = Quantity('N')
MilliNewton   = Quantity('mN')
KiloNewton    = Quantity('kN')
MegaNewton    = Quantity('MN')

Pascal        = Quantity('Pa')
KiloPascal    = Quantity('kPa')
MegaPascal    = Quantity('MPa')
GigaPascal    = Quantity('GPa')

MilliBar      = Quantity('mbar')
Bar           = Quantity('bar')

PoundForce    = Quantity('lbf')
Torr          = Quantity('Torr')
mTorr         = Quantity('mTorr')
yTorr         = Quantity('uTorr')

PSI           = Quantity('psi')
KSI           = Quantity('ksi')
MPSI          = Quantity('Mpsi')

Watt          = Quantity('W')
MilliWatt     = Quantity('mW')
KiloWatt      = Quantity('kW')
VoltAmpere    = Quantity('VA')

Volt          = Quantity('V')
MilliVolt     = Quantity('mV')
KiloVolt      = Quantity('kV')

Siemens       = Quantity('S')
MilliSiemens  = Quantity('mS')
MicroSiemens  = Quantity('uS')

Ohm          = Quantity('Ohm')
KiloOhm      = Quantity('kOhm')
MegaOhm      = Quantity('MOhm')

Coulomb       = Quantity('C')

Tesla         = Quantity('T')
Gauss         = Quantity('G')

Weber         = Quantity('Wb')

Oersted       = Quantity('Oe')

PicoFarad     = Quantity('pF')
NanoFarad     = Quantity('nF')
MicroFarad    = Quantity('uF')
MilliFarad    = Quantity('mF')
Farad         = Quantity('F')

NanoHenry     = Quantity('nH')
MicroHenry    = Quantity('uH')
MilliHenry    = Quantity('mH')
Henry         = Quantity('H')

Joule         = Quantity('J')
MilliJoule    = Quantity('mJ')
KiloJoule     = Quantity('kJ')
NewtonMeter   = Quantity('Nm')
VoltAmpereSecond   = Quantity('VAs')
WattSecond    = Quantity('Ws')
KiloWattHour  = Quantity('kWh')
ElectronVolt  = Quantity('eV')
KiloElectronVolt = Quantity('keV')
MegaElectronVolt = Quantity('MeV')
Calorie       = Quantity('cal')
KiloCalorie   = Quantity('kcal')

MPH           = Quantity('mi/h')
KMH           = Quantity('km/h')

Degree        = Quantity('deg')
Radian        = Quantity('rad')
Gon           = Quantity('gon')
AngularMinute = Quantity().AngularMinute
AngularSecond = Quantity().AngularSecond

Length        = Unit(1)
Area          = Unit(2)
Volume        = Unit(3)
Mass          = Unit(0,1)

# https://wiki.freecad.org/Quantity#Internal_representation
# Unit: dimension index - dimension name
# 0 - length
# 1 - weight
# 2 - time
# 3 - current
# 4 - temperature
# 5 - amount of substance
# 6 - luminous intensity
# 7 - angle

# Angle
Angle            = Unit(0,0,0,0,0,0,0,1)
AngleOfFriction  = Unit(0,0,0,0,0,0,0,1)

Density       = Unit(-3,1)

TimeSpan      = Unit(0,0,1)
Frequency     = Unit(0,0,-1)
Velocity      = Unit(1,0,-1)
Acceleration  = Unit(1,0,-2)
Temperature   = Unit(0,0,0,0,1)

ElectricCurrent       = Unit(0,0,0,1)
ElectricPotential     = Unit(2,1,-3,-1)
ElectricCharge        = Unit(0,0,1,1)
MagneticFluxDensity   = Unit(0,1,-2,-1)
ElectricalCapacitance = Unit(-2,-1,4,2)
ElectricalInductance  = Unit(2,1,-2,-2)
ElectricalConductance = Unit(-2,-1,3,2)
ElectricalResistance  = Unit(2,1,-3,-2)
AmountOfSubstance = Unit(0,0,0,0,0,1)
LuminousIntensity = Unit(0,0,0,0,0,0,1)

# Pressure
CompressiveStrength     = Unit(-1,1,-2)
Pressure                = Unit(-1,1,-2)
ShearModulus            = Unit(-1,1,-2)
Stress                  = Unit(-1,1,-2)
UltimateTensileStrength = Unit(-1,1,-2)
YieldStrength           = Unit(-1,1,-2)
YoungsModulus           = Unit(-1,1,-2)

Force         = Unit(1,1,-2)
Work          = Unit(2,1,-2)
Power         = Unit(2,1,-3)

SpecificEnergy               = Unit(2,0,-2)
ThermalConductivity          = Unit(1,1,-3,0,-1)
ThermalExpansionCoefficient  = Unit(0,0,0,0,-1)
VolumetricThermalExpansionCoefficient  = Unit(0,0,0,0,-1)
SpecificHeat                 = Unit(2,0,-2,0,-1)
ThermalTransferCoefficient   = Unit(0,1,-3,0,-1)
HeatFlux                     = Unit(0,1,-3,0,0)
DynamicViscosity             = Unit(-1,1,-1)
KinematicViscosity           = Unit(2,0,-1)
VacuumPermittivity           = Unit(-3,-1,4,2)

from enum import IntEnum

class Scheme(IntEnum):
    SI1 = 0
    SI2 = 1
    Imperial1 = 2
    ImperialDecimal = 3
    Centimeters = 4
    ImperialBuilding = 5
    MmMin = 6
    ImperialCivil = 7
    FemMilliMeterNewton = 8
"""
