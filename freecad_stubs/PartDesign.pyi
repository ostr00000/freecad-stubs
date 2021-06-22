import FreeCAD
import FreeCADGui
import Part


# BodyPy.xml
class Body(Part.BodyBase):
    """PartDesign body class"""

    @property
    def VisibleFeature(self) -> object:
        """Return the the visible feature of this body"""

    def insertObject(self, feature: FreeCAD.DocumentObject, target: object, after: bool = False, /):
        """insertObject(feature, target, after=False)
                                Insert the feature into the body after the given feature.

                                @param feature  The feature to insert into the body
                                @param target   The feature relative which one should be inserted the given.
                                  If target is NULL than insert into the end if where is InsertBefore
                                  and into the begin if where is InsertAfter.
                                @param after    if true insert the feature after the target. Default is false.

                                @note the method doesn't modify the Tip unlike addObject()
                            """


# FeaturePy.xml
class Feature(Part.Feature):
    """This is the father of all PartDesign object classes"""


# ViewProviderPy.xml
class ViewProvider(FreeCADGui.ViewProviderDocumentObject):
    """This is the father of all PartDesign ViewProvider classes"""

    def makeTemporaryVisible(self, bool: bool, /):
        """makeTemporaryVisible(bool): makes this viewprovider visible in the
        scene graph without changing any properties, not the visibility one and also not
        the display mode. This can be used to show the shape of this viewprovider from
        other viewproviders without doing anything to the document and properties.
        """

    def setBodyMode(self, bool: bool, /):
        """setBodyMode(bool): body mode means that the object is part of a body
        and that the body is used to set the visual properties, not the features. Hence
        setting body mode to true will hide most viewprovider properties."""
