import FreeCAD


# MeasurementPy.xml
class Measurement(FreeCAD.BaseClass):
    """
    This class can be imported.
    Make a measurement
    """

    def addReference3D(self, arg1: str, arg2: str, /):
        """add a geometric reference"""

    def angle(self):
        """measure the angle between two edges"""

    def clear(self):
        """measure the difference between references to obtain resultant vector"""

    def com(self):
        """measure the center of mass for selected volumes"""

    def delta(self):
        """measure the difference between references to obtain resultant vector"""

    def has3DReferences(self):
        """does Measurement have links to 3D geometry"""

    def length(self):
        """measure the length of the references"""

    def radius(self):
        """measure the radius of an arc or circle edge"""
