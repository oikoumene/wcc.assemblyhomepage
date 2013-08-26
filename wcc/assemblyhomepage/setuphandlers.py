from collective.grok import gs
from wcc.assemblyhomepage import MessageFactory as _

@gs.importstep(
    name=u'wcc.assemblyhomepage', 
    title=_('wcc.assemblyhomepage import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.assemblyhomepage.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
