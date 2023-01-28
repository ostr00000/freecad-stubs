import typing

import FreeCAD
import Part as PartModule


# BodyPy.xml
class Body(PartModule.BodyBase):
    """PartDesign body class"""

    @property
    def VisibleFeature(self) -> typing.Any | object:
        """Return the visible feature of this body"""

    def insertObject(self, featurePy: FreeCAD.DocumentObject, targetPy, afterPy: bool = False, /):
        """
        insertObject(feature, target, after=False)
                                Insert the feature into the body after the given feature.

                                @param feature  The feature to insert into the body
                                @param target   The feature relative which one should be inserted the given.
                                  If target is NULL than insert into the end if where is InsertBefore
                                  and into the begin if where is InsertAfter.
                                @param after    if true insert the feature after the target. Default is false.

                                @note the method doesn't modify the Tip unlike addObject()
                    
        Possible exceptions: (SystemError).
        """


# FeaturePy.xml
class Feature(PartModule.Feature):
    """This is the father of all PartDesign object classes"""

    @property
    def BaseFeature(self) -> FreeCAD.DocumentObject | None:
        """Property TypeId: App::PropertyLink."""

    @BaseFeature.setter
    def BaseFeature(self, value: FreeCAD.DocumentObject | None): ...

    @property
    def _Body(self) -> FreeCAD.DocumentObject | None:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Transient] Property content won't be saved to file, but still saves name, type and status.
        [Prop_Hidden] Property won't appear in the editor.
        [Prop_Output] Modified property doesn't touch its parent container.
        Property group: Base.
        Property TypeId: App::PropertyLinkHidden.
        """

    def getBaseObject(self) -> FreeCAD.DocumentObject | None:
        """getBaseObject: returns feature this one fuses itself to, or None. Normally, this should be the same as BaseFeature property, except for legacy workflow. In legacy workflow, it will look up the support of referenced sketch."""
