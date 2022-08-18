import typing

from FreeCAD.Base import Unit, Quantity
import FreeCAD


# UnitsApiPy.cpp
@typing.overload
def parseQuantity(string: str, /) -> FreeCAD.Quantity: ...


@typing.overload
def parseQuantity(arg0: str, /) -> FreeCAD.Quantity:
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
def listSchemas(int: int, /) -> tuple[str, ...] | str:
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


def setSchema(int: int, /):
    """
    setSchema(int) -> None

    Sets the current schema to the given number, if possible
    Possible exceptions: (ValueError).
    """


def schemaTranslate(Quantity: FreeCAD.Quantity, int: int, /) -> tuple[str, float, str]:
    """
    schemaTranslate(Quantity, int) -> tuple

    Translate a quantity to a given schema
    Possible exceptions: (ValueError).
    """


@typing.overload
def toNumber(Quantity_or_float: FreeCAD.Quantity, format: str = 'g', decimals: int = -1, /) -> str: ...


@typing.overload
def toNumber(Quantity_or_float: float, format: str = 'g', decimals: int = -1, /) -> str:
    """
    toNumber(Quantity or float, [format='g', decimals=-1]) -> str

    Convert a quantity or float to a string
    Possible exceptions: (TypeError, ValueError).
    """


Unit = Unit
Quantity = Quantity
