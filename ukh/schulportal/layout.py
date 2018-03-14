import grok

from ukhtheme.grok.layout import ILayer
from uvc.tbskin.skin import ITBSkin


class ISchulportalLayer(ILayer):
    pass


class ISchulportalskin(ISchulportalLayer, ITBSkin):
    grok.skin('ukh_schulportaltheme')

