import typing

import FreeCAD
import Materials


# MaterialPy.xml
class Material(FreeCAD.BaseClass):
    """
    This class can be imported.
    Material descriptions.
    """

    def __init__(self):
        """Material descriptions."""

    @property
    def AppearanceModels(self) -> list[str]:
        """List of implemented models."""

    @property
    def AppearanceProperties(self) -> dict[str, str]:
        """deprecated -- Dictionary of material appearance properties."""

    @property
    def Author(self) -> str:
        """Author information."""

    @property
    def AuthorAndLicense(self) -> str:
        """deprecated -- Author and license information."""

    @property
    def Description(self) -> str:
        """Description of the material."""

    @property
    def Directory(self) -> str:
        """Model directory relative to the library root."""

    @property
    def LibraryIcon(self) -> str:
        """Model icon path."""

    @property
    def LibraryName(self) -> str:
        """Model library name."""

    @property
    def LibraryRoot(self) -> str:
        """Model library path."""

    @property
    def License(self) -> str:
        """License information."""

    @property
    def Name(self) -> str:
        """Model name."""

    @property
    def Parent(self) -> str:
        """Parent material UUID."""

    @property
    def PhysicalModels(self) -> list[str]:
        """List of implemented models."""

    @property
    def PhysicalProperties(self) -> dict[str, str]:
        """deprecated -- Dictionary of material physical properties."""

    @property
    def Properties(self) -> dict[str, str]:
        """deprecated -- Dictionary of all material properties."""

    @property
    def Reference(self) -> str:
        """Reference for material data."""

    @property
    def Tags(self) -> list[str]:
        """List of searchable tags."""

    @property
    def URL(self) -> str:
        """URL to a material reference."""

    @property
    def UUID(self) -> str:
        """Unique model identifier."""

    def getAppearanceValue(self, name: str, /):
        """Get the value associated with the property"""

    def getPhysicalValue(self, name: str, /) -> Materials.Array2D | Materials.Array3D | typing.Any:
        """Get the value associated with the property"""

    def hasAppearanceModel(self, uuid: str, /) -> bool:
        """Check if the material implements the appearance model with the given UUID"""

    def hasAppearanceProperty(self, name: str, /) -> bool:
        """Check if the material implements the appearance property with the given name"""

    def hasPhysicalModel(self, uuid: str, /) -> bool:
        """Check if the material implements the physical model with the given UUID"""

    def hasPhysicalProperty(self, name: str, /) -> bool:
        """Check if the material implements the physical property with the given name"""

    def isAppearanceModelComplete(self, name: str, /) -> bool:
        """Check if the material implements the appearance model with the given UUID, and has values defined for each property"""

    def isPhysicalModelComplete(self, name: str, /) -> bool:
        """Check if the material implements the physical model with the given UUID, and has values defined for each property"""


# ModelPy.xml
class Model(FreeCAD.BaseClass):
    """
    This class can be imported.
    Material model descriptions.
    """

    def __init__(self):
        """Material model descriptions."""

    @property
    def DOI(self) -> str:
        """Digital Object Identifier (see https://doi.org/)"""

    @property
    def Description(self) -> str:
        """Description of the model."""

    @property
    def Directory(self) -> str:
        """Model directory."""

    @property
    def Inherited(self) -> list[str]:
        """List of inherited models identified by UUID."""

    @property
    def LibraryIcon(self) -> str:
        """Model icon path."""

    @property
    def LibraryName(self) -> str:
        """Model library name."""

    @property
    def LibraryRoot(self) -> str:
        """Model library path."""

    @property
    def Name(self) -> str:
        """Model name."""

    @property
    def Properties(self) -> dict[str, Materials.ModelProperty]:
        """Dictionary of model properties."""

    @property
    def URL(self) -> str:
        """URL to a detailed description of the model."""

    @property
    def UUID(self) -> str:
        """Unique model identifier."""


# ModelPropertyPy.xml
class ModelProperty(FreeCAD.BaseClass):
    """
    This class can be imported.
    Material property descriptions.
    """

    def __init__(self):
        """Material property descriptions."""

    @property
    def Description(self) -> str:
        """Property description."""

    @property
    def Name(self) -> str:
        """Property name."""

    @property
    def Type(self) -> str:
        """Property type."""

    @property
    def URL(self) -> str:
        """URL to a detailed description of the property."""

    @property
    def Units(self) -> str:
        """Property units category."""


# Array3DPy.xml
class Array3D(FreeCAD.BaseClass):
    """3D Array of material properties."""

    def __init__(self):
        """3D Array of material properties."""

    @property
    def Array(self) -> list[list]:
        """The 3 dimensional array."""

    @property
    def Columns(self) -> int:
        """The number of columns in the array."""

    @property
    def Depth(self) -> int:
        """The depth of the array (3rd dimension)."""

    def getDepthValue(self, depth: int, /) -> FreeCAD.Quantity:
        """
        Get the column value at the given depth
        Possible exceptions: (IndexError).
        """

    def getRows(self, depth: int = None, /) -> int:
        """Get the number of rows in the array at the specified depth."""

    def getValue(self, depth: int, row: int, column: int, /) -> FreeCAD.Quantity:
        """
        Get the value at the given row and column
        Possible exceptions: (IndexError).
        """


# MaterialManagerPy.xml
class MaterialManager(FreeCAD.BaseClass):
    """
    This class can be imported.
    Material descriptions.
    """

    def __init__(self):
        """Material descriptions."""

    @property
    def MaterialLibraries(self) -> list[tuple[str, str, str]]:
        """List of Material libraries."""

    @property
    def Materials(self) -> dict[str, FreeCAD.Material]:
        """List of Materials."""

    def getMaterial(self, uuid: str, /) -> FreeCAD.Material:
        """
        Get a material object by specifying its UUID
        Possible exceptions: (LookupError).
        """

    def getMaterialByPath(self, path: str, lib: str = '', /) -> FreeCAD.Material:
        """
        Get a material object by specifying its path and library name
        Possible exceptions: (LookupError).
        """

    def materialsWithModel(self, uuid: str, /) -> dict[str, FreeCAD.Material]:
        """Get a list of materials implementing the specified model"""

    def materialsWithModelComplete(self, uuid: str, /) -> dict[str, FreeCAD.Material]:
        """Get a list of materials implementing the specified model, with values for all properties"""


# ModelManagerPy.xml
class ModelManager(FreeCAD.BaseClass):
    """
    This class can be imported.
    Material model descriptions.
    """

    def __init__(self):
        """Material model descriptions."""

    @property
    def ModelLibraries(self) -> list[tuple[str, str, str]]:
        """List of model libraries."""

    @property
    def Models(self) -> dict[str, Materials.Model]:
        """List of model libraries."""

    def getModel(self, uuid: str, /) -> Materials.Model:
        """
        Get a model object by specifying its UUID
        Possible exceptions: (LookupError).
        """

    def getModelByPath(self, path: str, lib: str = '', /) -> Materials.Model:
        """
        Get a model object by specifying its path
        Possible exceptions: (LookupError).
        """


# Array2DPy.xml
class Array2D(FreeCAD.BaseClass):
    """2D Array of material properties."""

    def __init__(self):
        """2D Array of material properties."""

    @property
    def Array(self) -> list[list]:
        """The 2 dimensional array."""

    @property
    def Columns(self) -> int:
        """The number of columns in the array."""

    @property
    def Rows(self) -> int:
        """The number of rows in the array."""

    def getRow(self, row: int, /) -> list[FreeCAD.Quantity]:
        """
        Get the row given the first column value
        Possible exceptions: (IndexError).
        """

    def getValue(self, row: int, column: int, /) -> FreeCAD.Quantity:
        """
        Get the value at the given row and column
        Possible exceptions: (IndexError).
        """
