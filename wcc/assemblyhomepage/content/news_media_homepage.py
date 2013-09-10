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

from collective import dexteritytextindexer

from Products.ATContentTypes.interfaces.topic import IATTopic
from plone.app.collection.interfaces import ICollection
from wcc.carousel.interfaces import ICarouselImageEnabled


# Interface class; used to define content-type schema.

class INewsMediaHomepage(form.Schema, IImageScaleTraversable):
    """
    
    """

    dexteritytextindexer.searchable('text')
    form.widget(text="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    text = schema.Text(
        title=_(u'label_body_text', u"Body Text"),
        description=u'',
        required=False,
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

