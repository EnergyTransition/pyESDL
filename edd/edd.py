"""Definition of meta model 'edd'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'edd'
nsURI = 'http://www.tno.nl/edr/edd'
nsPrefix = 'edd'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
AnnotationTypeEnum = EEnum('AnnotationTypeEnum', literals=[
                           'GENERAL', 'TECHNICAL_DIMENSIONS', 'COSTS', 'ENERGY_FLOWS', 'MATERIAL_FLOWS', 'EMISSIONS', 'OTHER'])


class EnergyDataDescription(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    title = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    tags = EAttribute(eType=EString, unique=True, derived=False, changeable=True, upper=-1)
    version = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    graphURL = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    esdlType = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    lastChanged = EAttribute(eType=EDate, unique=True, derived=False,
                             changeable=True, transient=True)
    publicationDate = EAttribute(eType=EDate, unique=True, derived=False,
                                 changeable=True, transient=True)
    validityYear = EAttribute(eType=EIntegerObject, unique=True, derived=False, changeable=True)
    author = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    esdl = EReference(ordered=True, unique=True, containment=True, derived=False)
    image = EReference(ordered=True, unique=True, containment=True, derived=False)
    annotation = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, id=None, title=None, description=None, tags=None, esdl=None, image=None, version=None, graphURL=None, esdlType=None, lastChanged=None, publicationDate=None, validityYear=None, author=None, annotation=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if title is not None:
            self.title = title

        if description is not None:
            self.description = description

        if tags:
            self.tags.extend(tags)

        if version is not None:
            self.version = version

        if graphURL is not None:
            self.graphURL = graphURL

        if esdlType is not None:
            self.esdlType = esdlType

        if lastChanged is not None:
            self.lastChanged = lastChanged

        if publicationDate is not None:
            self.publicationDate = publicationDate

        if validityYear is not None:
            self.validityYear = validityYear

        if author is not None:
            self.author = author

        if esdl is not None:
            self.esdl = esdl

        if image is not None:
            self.image = image

        if annotation:
            self.annotation.extend(annotation)


class Image(EObject, metaclass=MetaEClass):
    """Adds the possiblity to add an image to the EDD"""
    contentType = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    imageData = EAttribute(eType=EByteArray, unique=True, derived=False, changeable=True)

    def __init__(self, *, contentType=None, imageData=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if contentType is not None:
            self.contentType = contentType

        if imageData is not None:
            self.imageData = imageData


@abstract
class Annotation(EObject, metaclass=MetaEClass):
    """The annotation class can be used to add additional explanation to parts of the ESDL, when the ESDL is not sufficient to describe the contents ifself, e.g. some extra explanation on the cost figures.
It is up to the software to place these annotations in the correct place in the GUI, e.g. by checking if a certain attribute of an object requires further explanation, by iterating through the list of annotations."""
    explanation = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, explanation=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if explanation is not None:
            self.explanation = explanation


class ESDLDriveMetaData(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    metadata = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, metadata=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if metadata:
            self.metadata.extend(metadata)


class ResourceMetaData(EObject, metaclass=MetaEClass):

    resourcePath = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    byteSize = EAttribute(eType=ELong, unique=True, derived=False, changeable=True)
    objectCount = EAttribute(eType=ELong, unique=True, derived=False, changeable=True)
    resourceReference = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, resourcePath=None, byteSize=None, objectCount=None, resourceReference=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if resourcePath is not None:
            self.resourcePath = resourcePath

        if byteSize is not None:
            self.byteSize = byteSize

        if objectCount is not None:
            self.objectCount = objectCount

        if resourceReference is not None:
            self.resourceReference = resourceReference


class CategoryAnnotation(Annotation):
    """The CategoryAnnotation allows to annotate an ESDL based on predifined categories.
- The type attribute allows you to select the type of annotation (e.g. a cost annotation)
- The explanation attribute is a free text field to describe the explanation in detail
"""
    type = EAttribute(eType=AnnotationTypeEnum, unique=True, derived=False, changeable=True)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class ObjectAnnotation(Annotation):
    """ObjectAnnotation allows one to annotate an ESDL object with some explanation text in the esdl-part of the EDD, by using a reference the the object and the attribute name (optional)
- The explanation attribute is a free text field to describe the explanation in detail
- The about refrence refers to an object inside the ESDL, e.g. the main asset class, such as WindTurbine
- If the aboutAttribute (optional) is present it refers to a specific attribute of the object described by the 'about' objectclass that need explanation, e.g. the power attribute of a WindTurbine"""
    aboutAttribute = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    about = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, about=None, aboutAttribute=None, **kwargs):

        super().__init__(**kwargs)

        if aboutAttribute is not None:
            self.aboutAttribute = aboutAttribute

        if about is not None:
            self.about = about
