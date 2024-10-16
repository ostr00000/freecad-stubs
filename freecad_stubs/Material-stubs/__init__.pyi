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


# UUIDsPy.xml
class UUIDs(FreeCAD.BaseClass):
    """
    This class can be imported.
    Material model UUID identifiers.
    """

    def __init__(self):
        """Material model UUID identifiers."""

    @property
    def AdvancedRendering(self) -> str:
        """
        UUID for model System:Rendering/AdvancedRendering
        Possible exceptions: (AttributeError).
        """

    @property
    def Architectural(self) -> str:
        """
        UUID for model System:Architectural/Architectural
        Possible exceptions: (AttributeError).
        """

    @property
    def ArchitecturalRendering(self) -> str:
        """
        UUID for model System:Architectural/ArchitecturalRendering
        Possible exceptions: (AttributeError).
        """

    @property
    def BasicRendering(self) -> str:
        """
        UUID for model System:Rendering/BasicRendering
        Possible exceptions: (AttributeError).
        """

    @property
    def Costs(self) -> str:
        """
        UUID for model System:Costs/Costs
        Possible exceptions: (AttributeError).
        """

    @property
    def Density(self) -> str:
        """
        UUID for model System:Mechanical/Density
        Possible exceptions: (AttributeError).
        """

    @property
    def Electromagnetic(self) -> str:
        """
        UUID for model System:Electromagnetic/Electromagnetic
        Possible exceptions: (AttributeError).
        """

    @property
    def Father(self) -> str:
        """
        UUID for model System:Legacy/Father
        Possible exceptions: (AttributeError).
        """

    @property
    def Fluid(self) -> str:
        """
        UUID for model System:Fluid/Fluid
        Possible exceptions: (AttributeError).
        """

    @property
    def IsotropicLinearElastic(self) -> str:
        """
        UUID for model System:Mechanical/IsotropicLinearElastic
        Possible exceptions: (AttributeError).
        """

    @property
    def LinearElastic(self) -> str:
        """
        UUID for model System:Mechanical/LinearElastic
        Possible exceptions: (AttributeError).
        """

    @property
    def MaterialStandard(self) -> str:
        """
        UUID for model System:Legacy/MaterialStandard
        Possible exceptions: (AttributeError).
        """

    @property
    def OgdenYld2004p18(self) -> str:
        """
        UUID for model System:Mechanical/OgdenYld2004p18
        Possible exceptions: (AttributeError).
        """

    @property
    def OrthotropicLinearElastic(self) -> str:
        """
        UUID for model System:Mechanical/OrthotropicLinearElastic
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderAppleseed(self) -> str:
        """
        UUID for model System:Rendering/RenderAppleseed
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderCarpaint(self) -> str:
        """
        UUID for model System:Rendering/RenderCarpaint
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderCycles(self) -> str:
        """
        UUID for model System:Rendering/RenderCycles
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderDiffuse(self) -> str:
        """
        UUID for model System:Rendering/RenderDiffuse
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderDisney(self) -> str:
        """
        UUID for model System:Rendering/RenderDisney
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderEmission(self) -> str:
        """
        UUID for model System:Rendering/RenderEmission
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderGlass(self) -> str:
        """
        UUID for model System:Rendering/RenderGlass
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderLuxcore(self) -> str:
        """
        UUID for model System:Rendering/RenderLuxcore
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderLuxrender(self) -> str:
        """
        UUID for model System:Rendering/RenderLuxrender
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderMixed(self) -> str:
        """
        UUID for model System:Rendering/RenderMixed
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderOspray(self) -> str:
        """
        UUID for model System:Rendering/RenderOspray
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderPbrt(self) -> str:
        """
        UUID for model System:Rendering/RenderPbrt
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderPovray(self) -> str:
        """
        UUID for model System:Rendering/RenderPovray
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderSubstancePBR(self) -> str:
        """
        UUID for model System:Rendering/RenderSubstancePBR
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderTexture(self) -> str:
        """
        UUID for model System:Rendering/RenderTexture
        Possible exceptions: (AttributeError).
        """

    @property
    def RenderWB(self) -> str:
        """
        UUID for model System:Rendering/RenderWB
        Possible exceptions: (AttributeError).
        """

    @property
    def TestModel(self) -> str:
        """
        UUID for model System:Test/Test Model
        Possible exceptions: (AttributeError).
        """

    @property
    def TextureRendering(self) -> str:
        """
        UUID for model System:Rendering/TextureRendering
        Possible exceptions: (AttributeError).
        """

    @property
    def Thermal(self) -> str:
        """
        UUID for model System:Thermal/Thermal
        Possible exceptions: (AttributeError).
        """

    @property
    def VectorRendering(self) -> str:
        """
        UUID for model System:Rendering/VectorRendering
        Possible exceptions: (AttributeError).
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
