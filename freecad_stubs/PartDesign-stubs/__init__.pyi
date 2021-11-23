import FreeCAD
import Part as PartModule


# BodyPy.xml
class Body(PartModule.BodyBase):
    """PartDesign body class"""

    def insertObject(self, feature: FreeCAD.DocumentObject, target, after=False, /):
        """
        insertObject(feature, target, after=False)
                                Insert the feature into the body after the given feature.

                                @param feature  The feature to insert into the body
                                @param target   The feature relative which one should be inserted the given.
                                  If target is NULL than insert into the end if where is InsertBefore
                                  and into the begin if where is InsertAfter.
                                @param after    if true insert the feature after the target. Default is false.

                                @note the method doesn't modify the Tip unlike addObject()
                    
        Possible exceptions: (SystemError, ValueError).
        """


# FeaturePy.xml
class Feature(PartModule.Feature):
    """This is the father of all PartDesign object classes"""

    @property
    def BaseFeature(self) -> FreeCAD.DocumentObject | None:
        """Property TypeId: App::PropertyLink."""

    @BaseFeature.setter
    def BaseFeature(self, value: FreeCAD.DocumentObject | None): ...
