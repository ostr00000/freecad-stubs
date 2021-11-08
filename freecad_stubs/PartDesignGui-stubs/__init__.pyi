import FreeCADGui


# ViewProviderPy.xml
class ViewProvider(FreeCADGui.ViewProviderDocumentObject):
    """This is the father of all PartDesign ViewProvider classes"""

    def makeTemporaryVisible(self, bool: bool, /) -> None:
        """
        makeTemporaryVisible(bool): makes this viewprovider visible in the
        scene graph without changing any properties, not the visibility one and also not
        the display mode. This can be used to show the shape of this viewprovider from
        other viewproviders without doing anything to the document and properties.
        """

    def setBodyMode(self, bool: bool, /) -> None:
        """
        setBodyMode(bool): body mode means that the object is part of a body
        and that the body is used to set the visual properties, not the features. Hence
        setting body mode to true will hide most viewprovider properties.
        """
