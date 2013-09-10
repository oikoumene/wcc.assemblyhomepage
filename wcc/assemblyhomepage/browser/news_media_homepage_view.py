from five import grok
from plone.directives import dexterity, form
from wcc.assemblyhomepage.content.news_media_homepage import INewsMediaHomepage

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(INewsMediaHomepage)
    grok.require('zope2.View')
    grok.template('news_media_homepage_view')
    grok.name('view')

    def news_items(self):
        rel = self.context.news_source
        if not rel:
            return []
        source = rel.to_object
        results = source.queryCatalog(batch=False) or []
        return [i.getObject() for i in results[:3]]

    def more_news_target(self):
        if self.context.more_news_target:
            return self.context.more_news_target.to_object
        return self.context.news_source.to_object

