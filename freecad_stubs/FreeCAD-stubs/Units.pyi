import typing

from FreeCAD.Base import Unit, Quantity
import FreeCAD


# UnitsApiPy.cpp
def parseQuantity(pstr: str, /) -> FreeCAD.Quantity:
    """
    parseQuantity(string) -> Base.Quantity()

    calculate a mathematical expression with units to a quantity object. 
    can be used for simple unit translation like: 
    parseQuantity('10m')
    or for more complex espressions:
    parseQuantity('sin(pi)/50.0 m/s^2')
    """


@typing.overload
def listSchemas() -> tuple[str, ...] | str: ...


@typing.overload
def listSchemas(index: int, /) -> tuple[str, ...] | str:
    """
    listSchemas() -> a tuple of schemas

    listSchemas(int) -> description of the given schema


    Possible exceptions: (ValueError, TypeError).
    """


def getSchema() -> int:
    """
    getSchema() -> int

    The int is the position of the tuple returned by listSchemas
    """


def setSchema(index: int, /):
    """
    setSchema(int) -> None

    Sets the current schema to the given number, if possible
    Possible exceptions: (ValueError).
    """


def schemaTranslate(q: FreeCAD.Quantity, index: int, /) -> tuple[str, float, str]:
    """
    schemaTranslate(Quantity, int) -> tuple

    Translate a quantity to a given schema
    Possible exceptions: (ValueError).
    """


@typing.overload
def toNumber(q: FreeCAD.Quantity, format: str = 'g', decimals: int = -1, /) -> str: ...


@typing.overload
def toNumber(value: float, format: str = 'g', decimals: int = -1, /) -> str:
    """
    toNumber(Quantity or float, [format='g', decimals=-1]) -> str

    Convert a quantity or float to a string
    Possible exceptions: (TypeError, ValueError).
    """


Unit = Unit
Quantity = Quantity

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
# (length, weight, time, current, temperature, amount of substance, luminous intensity, angle)

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
