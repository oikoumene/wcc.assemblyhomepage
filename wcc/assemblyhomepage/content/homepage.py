from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent

from wcc.assemblyhomepage import MessageFactory as _

from Products.ATContentTypes.interfaces.topic import IATTopic
from plone.app.collection.interfaces import ICollection
from wcc.carousel.interfaces import ICarouselImageEnabled

# Interface class; used to define content-type schema.

class IHomepage(form.Schema, IImageScaleTraversable):
    """
    
    """

    languageindependent('slider_items')
    slider_items = RelationList(
        title=u'Slider items',
        value_type=RelationChoice(
            source=ObjPathSourceBinder(
                object_provides=ICarouselImageEnabled.__identifier__
            )
        ),
        required=True
    )

    languageindependent('news_source')
    news_source = RelationChoice(
        title=u'Source collection for news listing',
        source=ObjPathSourceBinder(
            object_provides=[IATTopic.__identifier__,
                            ICollection.__identifier__]
        ),
        required=False
    )

    languageindependent('more_news_target')
    more_news_target = RelationChoice(
        title=u'Target for "More News" link',
        source=ObjPathSourceBinder(
            object_provides=[IATTopic.__identifier__,
                            ICollection.__identifier__]
        ),
        required=False,
    )

    languageindependent('video_url')
    video_url = schema.TextLine(
        title=u'Youtube URL to video',
        description=u'If set, This will replace the slider',
        required=False
    )

    languageindependent('embed_html')
    embed_html = schema.Text(
        title=u'Embed HTML',
        description=u'If set, this will replace the slider/youtube video',
        required=False
    )

