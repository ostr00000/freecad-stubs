import typing

import FreeCAD


# UnitsApiPy.cpp
def parseQuantity(arg1: str, /):
    """parseQuantity(string) -> Base.Quantity()

    calculate a mathematical expression with units to a quantity object. 
    can be used for simple unit translation like: 
    parseQuantity('10m')
    or for more complex espressions:
    parseQuantity('sin(pi)/50.0 m/s^2')
    """


@typing.overload
def listSchemas(): ...


@typing.overload
def listSchemas(arg1: int, /):
    """listSchemas() -> a tuple of schemas

    listSchemas(int) -> description of the given schema

    """


def getSchema():
    """getSchema() -> int

    The int is the position of the tuple returned by listSchemas"""


def schemaTranslate(arg1: FreeCAD.Quantity, arg2: int, /):
    """schemaTranslate(Quantity, int) -> tuple

    Translate a quantity to a given schema"""
