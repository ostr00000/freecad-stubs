import FreeCAD


# MaterialPy.xml
class Material(FreeCAD.BaseClass):
    """
    This class can be imported.
    Material descriptions.
    """

    def __init__(self):
        """Material descriptions."""

    @property
    def AppearanceModels(self) -> list:
        """
        List of implemented models.
        Possible exceptions: (AttributeError).
        """

    @property
    def AppearanceProperties(self) -> dict:
        """
        deprecated -- Dictionary of material appearance properties.
        Possible exceptions: (AttributeError).
        """

    @property
    def Author(self) -> str:
        """
        Author information.
        Possible exceptions: (AttributeError).
        """

    @property
    def AuthorAndLicense(self) -> str:
        """
        deprecated -- Author and license information.
        Possible exceptions: (AttributeError).
        """

    @property
    def Description(self) -> str:
        """
        Description of the material.
        Possible exceptions: (AttributeError).
        """

    @property
    def Directory(self) -> str:
        """
        Model directory relative to the library root.
        Possible exceptions: (AttributeError).
        """

    @property
    def LibraryIcon(self) -> str:
        """
        Model icon path.
        Possible exceptions: (AttributeError).
        """

    @property
    def LibraryName(self) -> str:
        """
        Model library name.
        Possible exceptions: (AttributeError).
        """

    @property
    def LibraryRoot(self) -> str:
        """
        Model library path.
        Possible exceptions: (AttributeError).
        """

    @property
    def License(self) -> str:
        """
        License information.
        Possible exceptions: (AttributeError).
        """

    @property
    def Name(self) -> str:
        """
        Model name.
        Possible exceptions: (AttributeError).
        """

    @property
    def Parent(self) -> str:
        """
        Parent material UUID.
        Possible exceptions: (AttributeError).
        """

    @property
    def PhysicalModels(self) -> list:
        """
        List of implemented models.
        Possible exceptions: (AttributeError).
        """

    @property
    def PhysicalProperties(self) -> dict:
        """
        deprecated -- Dictionary of material physical properties.
        Possible exceptions: (AttributeError).
        """

    @property
    def Properties(self) -> dict:
        """
        deprecated -- Dictionary of all material properties.
        Possible exceptions: (AttributeError).
        """

    @property
    def Reference(self) -> str:
        """
        Reference for material data.
        Possible exceptions: (AttributeError).
        """

    @property
    def Tags(self) -> list:
        """
        List of searchable tags.
        Possible exceptions: (AttributeError).
        """

    @property
    def URL(self) -> str:
        """
        URL to a material reference.
        Possible exceptions: (AttributeError).
        """

    @property
    def UUID(self) -> str:
        """
        Unique model identifier.
        Possible exceptions: (AttributeError).
        """

    def getAppearanceValue(self):
        """
        Get the value associated with the property
        Possible exceptions: (NotImplementedError).
        """

    def getPhysicalValue(self):
        """
        Get the value associated with the property
        Possible exceptions: (NotImplementedError).
        """

    def hasAppearanceModel(self):
        """
        Check if the material implements the appearance model with the given UUID
        Possible exceptions: (NotImplementedError).
        """

    def hasAppearanceProperty(self):
        """
        Check if the material implements the appearance property with the given name
        Possible exceptions: (NotImplementedError).
        """

    def hasPhysicalModel(self):
        """
        Check if the material implements the physical model with the given UUID
        Possible exceptions: (NotImplementedError).
        """

    def hasPhysicalProperty(self):
        """
        Check if the material implements the physical property with the given name
        Possible exceptions: (NotImplementedError).
        """

    def isAppearanceModelComplete(self):
        """
        Check if the material implements the appearance model with the given UUID, and has values defined for each property
        Possible exceptions: (NotImplementedError).
        """

    def isPhysicalModelComplete(self):
        """
        Check if the material implements the physical model with the given UUID, and has values defined for each property
        Possible exceptions: (NotImplementedError).
        """


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
        """
        Digital Object Identifier (see https://doi.org/)
        Possible exceptions: (AttributeError).
        """

    @property
    def Description(self) -> str:
        """
        Description of the model.
        Possible exceptions: (AttributeError).
        """

    @property
    def Directory(self) -> str:
        """
        Model directory.
        Possible exceptions: (AttributeError).
        """

    @property
    def Inherited(self) -> list:
        """
        List of inherited models identified by UUID.
        Possible exceptions: (AttributeError).
        """

    @property
    def LibraryIcon(self) -> str:
        """
        Model icon path.
        Possible exceptions: (AttributeError).
        """

    @property
    def LibraryName(self) -> str:
        """
        Model library name.
        Possible exceptions: (AttributeError).
        """

    @property
    def LibraryRoot(self) -> str:
        """
        Model library path.
        Possible exceptions: (AttributeError).
        """

    @property
    def Name(self) -> str:
        """
        Model name.
        Possible exceptions: (AttributeError).
        """

    @property
    def Properties(self) -> dict:
        """
        Dictionary of model properties.
        Possible exceptions: (AttributeError).
        """

    @property
    def URL(self) -> str:
        """
        URL to a detailed description of the model.
        Possible exceptions: (AttributeError).
        """

    @property
    def UUID(self) -> str:
        """
        Unique model identifier.
        Possible exceptions: (AttributeError).
        """


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
        """
        Property description.
        Possible exceptions: (AttributeError).
        """

    @property
    def Name(self) -> str:
        """
        Property name.
        Possible exceptions: (AttributeError).
        """

    @property
    def Type(self) -> str:
        """
        Property type.
        Possible exceptions: (AttributeError).
        """

    @property
    def URL(self) -> str:
        """
        URL to a detailed description of the property.
        Possible exceptions: (AttributeError).
        """

    @property
    def Units(self) -> str:
        """
        Property units category.
        Possible exceptions: (AttributeError).
        """


# Array3DPy.xml
class Array3D(FreeCAD.BaseClass):
    """3D Array of material properties."""

    def __init__(self):
        """3D Array of material properties."""

    @property
    def Array(self) -> list:
        """
        The 3 dimensional array.
        Possible exceptions: (AttributeError).
        """

    @property
    def Columns(self) -> int:
        """
        The number of columns in the array.
        Possible exceptions: (AttributeError).
        """

    @property
    def Depth(self) -> int:
        """
        The depth of the array (3rd dimension).
        Possible exceptions: (AttributeError).
        """

    def getDepthValue(self):
        """
        Get the column value at the given depth
        Possible exceptions: (NotImplementedError).
        """

    def getRows(self):
        """
        Get the number of rows in the array at the specified depth.
        Possible exceptions: (NotImplementedError).
        """

    def getValue(self):
        """
        Get the value at the given row and column
        Possible exceptions: (NotImplementedError).
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
    def MaterialLibraries(self) -> list:
        """
        List of Material libraries.
        Possible exceptions: (AttributeError).
        """

    @property
    def Materials(self) -> dict:
        """
        List of Materials.
        Possible exceptions: (AttributeError).
        """

    def getMaterial(self):
        """
        Get a material object by specifying its UUID
        Possible exceptions: (NotImplementedError).
        """

    def getMaterialByPath(self):
        """
        Get a material object by specifying its path and library name
        Possible exceptions: (NotImplementedError).
        """

    def materialsWithModel(self):
        """
        Get a list of materials implementing the specified model
        Possible exceptions: (NotImplementedError).
        """

    def materialsWithModelComplete(self):
        """
        Get a list of materials implementing the specified model, with values for all properties
        Possible exceptions: (NotImplementedError).
        """


# ModelManagerPy.xml
class ModelManager(FreeCAD.BaseClass):
    """
    This class can be imported.
    Material model descriptions.
    """

    def __init__(self):
        """Material model descriptions."""

    @property
    def ModelLibraries(self) -> list:
        """
        List of model libraries.
        Possible exceptions: (AttributeError).
        """

    @property
    def Models(self) -> dict:
        """
        List of model libraries.
        Possible exceptions: (AttributeError).
        """

    def getModel(self):
        """
        Get a model object by specifying its UUID
        Possible exceptions: (NotImplementedError).
        """

    def getModelByPath(self):
        """
        Get a model object by specifying its path
        Possible exceptions: (NotImplementedError).
        """


# Array2DPy.xml
class Array2D(FreeCAD.BaseClass):
    """2D Array of material properties."""

    def __init__(self):
        """2D Array of material properties."""

    @property
    def Array(self) -> list:
        """
        The 2 dimensional array.
        Possible exceptions: (AttributeError).
        """

    @property
    def Columns(self) -> int:
        """
        The number of columns in the array.
        Possible exceptions: (AttributeError).
        """

    @property
    def Rows(self) -> int:
        """
        The number of rows in the array.
        Possible exceptions: (AttributeError).
        """

    def getRow(self):
        """
        Get the row given the first column value
        Possible exceptions: (NotImplementedError).
        """

    def getValue(self):
        """
        Get the value at the given row and column
        Possible exceptions: (NotImplementedError).
        """
