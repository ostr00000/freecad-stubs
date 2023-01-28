import FreeCAD


# MeasurementPy.xml
class Measurement(FreeCAD.BaseClass):
    """
    This class can be imported.
    Make a measurement
    """

    def __init__(self):
        """Make a measurement"""

    def addReference3D(self, ObjectName: str, SubName: str, /):
        """
        add a geometric reference
        Possible exceptions: (ValueError).
        """

    def angle(self) -> float:
        """measure the angle between two edges"""

    def clear(self):
        """measure the difference between references to obtain resultant vector"""

    def com(self) -> FreeCAD.Vector:
        """measure the center of mass for selected volumes"""

    def delta(self) -> FreeCAD.Vector:
        """measure the difference between references to obtain resultant vector"""

    def has3DReferences(self) -> bool:
        """does Measurement have links to 3D geometry"""

    def length(self) -> float:
        """measure the length of the references"""

    def radius(self) -> float:
        """measure the radius of an arc or circle edge"""
