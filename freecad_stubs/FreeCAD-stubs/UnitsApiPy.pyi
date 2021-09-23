import typing

import FreeCAD


# UnitsApiPy.cpp
@typing.overload
def parseQuantity(string: str, /): ...


@typing.overload
def parseQuantity(arg: str, /):
    """
    parseQuantity(string) -> Base.Quantity()

    calculate a mathematical expression with units to a quantity object. 
    can be used for simple unit translation like: 
    parseQuantity('10m')
    or for more complex espressions:
    parseQuantity('sin(pi)/50.0 m/s^2')
    """


@typing.overload
def listSchemas(): ...


@typing.overload
def listSchemas(int: int, /):
    """
    listSchemas() -> a tuple of schemas

    listSchemas(int) -> description of the given schema
    """


def getSchema():
    """
    getSchema() -> int

    The int is the position of the tuple returned by listSchemas
    """


def setSchema(int: int, /):
    """
    setSchema(int) -> None

    Sets the current schema to the given number, if possible
    """


def schemaTranslate(Quantity: FreeCAD.Quantity, int: int, /):
    """
    schemaTranslate(Quantity, int) -> tuple

    Translate a quantity to a given schema
    """
