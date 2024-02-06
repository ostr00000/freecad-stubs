import typing

import Part as PartModule


# ViewProviderSketchGeometryExtensionPy.xml
class ViewProviderSketchGeometryExtension(PartModule.GeometryExtension):
    """
    This class can be imported.
    Describes a ViewProviderSketchGeometryExtension
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, VisualLayerId: int, /):
        """
        Describes a ViewProviderSketchGeometryExtension
        Possible exceptions: (TypeError).
        """

    @property
    def VisualLayerId(self) -> int:
        """Sets/returns this geometry's Visual Layer Id."""

    @VisualLayerId.setter
    def VisualLayerId(self, value: int): ...
