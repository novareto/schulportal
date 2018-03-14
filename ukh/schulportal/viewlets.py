# -*- coding: utf-8 -*-

import grok
from os import path
from ukhtheme.grok.layout import ILayer
from ukhtheme.grok.viewlets import SocialLinks
from zope.interface import Interface
from zope.viewlet.interfaces import IContentProvider
from zope.component import getMultiAdapter, queryMultiAdapter
from megrok.pagetemplate import PageTemplate
from zope.pagetemplate.interfaces import IPageTemplate
from uvc.api.api import get_template
from ukhtheme.grok.viewlets import BGHeader
from ukh.spsuaz.components import SUnfallanzeigen
from uvc.letterbasket.components import LetterBasket

from ukh.schulportal.layout import ISchulportalLayer as ILayer

templates_dir = path.join(path.dirname(__file__), 'templates')


class BGHeader(BGHeader):
    grok.layer(ILayer)
    template = get_template(templates_dir, 'bgheader.cpt')

    def MyTitle(self):
        if '-' in self.request.principal.id:
            return "Mein Profil"
        return "Benutzerverwaltung"

    def welcome(self):
        pr = self.request.principal
        if hasattr(pr, 'getAdresse'):
            adr = pr.getAdresse()
            #name = adr.get('iknam1', '')
            n1 = adr.get('iknam1', '').strip()
            n2 = adr.get('iknam2', '').strip()
            name = n1 + ' ' + n2
            return "<h3>Herzlich willkommen</h3> <p> %s </p>" % name
        return ""

    def links(self):
        rc = {}
        pr = self.request.principal
        if pr.title == u'Unauthenticated User':
            return rc
        rc['logout'] = "%s/logout" % self.view.application_url()
        rc['profile'] = "%spersonalpanelview" % uvcsite.getHomeFolderUrl(self.request)
        return rc


class Navigation(grok.ViewletManager):
    grok.name('navigation')
    grok.context(Interface)
    grok.layer(ILayer)


class UniqueNavigation(grok.Viewlet):
    grok.name('central_nav')
    grok.context(Interface)
    grok.layer(ILayer)
    grok.viewletmanager(Navigation)
    grok.require('zope.View')

    id = "globalmenuviewlet"

    def update(self):
        globalmenu = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IContentProvider, 'globalmenu')

        quicklinks = queryMultiAdapter(
            (self.view.context, self.request, self.view),
            IContentProvider, 'quicklinks')

        self.menus = {
            #'globalmenu': globalmenu.getMenuItems(),
            #'personalpreferences': personalpreferences.getMenuItems(),
            #'footer': footer.getMenuItems(),
            'quicklinks': quicklinks.getMenuItems(),
        }
        menus = [x for x in self.menus.values() if x]
        am = []
        for amenu in menus:
            for menu in amenu:
                am.append(menu)
        self.smenus = sorted(am, key=lambda item: item.get('order', 1))
        self.renderables = globalmenu.getRenderableItems()

    def render(self):
        template = getMultiAdapter((self, self.request), IPageTemplate)
        return template()


class UniqueNavTemplate(PageTemplate):
    grok.view(UniqueNavigation)
    grok.layer(ILayer)
    template = get_template(templates_dir, 'unique.cpt')


class SocialLinks(SocialLinks):
    grok.layer(ILayer)

    def available(self):
        return False

from uvc.layout.interfaces import IQuickLinks
import uvcsite


class Home(uvcsite.MenuItem):
    grok.viewletmanager(IQuickLinks)
    grok.context(Interface)
    grok.order(10)

    @property
    def title(self):
        return '<span class="glyphicon glyphicon-home" aria-hidden="true"></span>'

    @property
    def action(self):
        return self.view.application_url()


class Verbandbuch(uvcsite.ProductMenuItem):
    grok.viewletmanager(IQuickLinks)
    grok.context(Interface)
    grok.order(20)
    reg_name = "KinderUnfallanzeige"
    title = "Verbandbuch"

    @property
    def action(self):
        action = super(Verbandbuch, self).action
        action = action.replace('/add', '?filter=vb')
        return action


class Unfallanzeige(uvcsite.ProductMenuItem):
    grok.viewletmanager(IQuickLinks)
    grok.context(Interface)
    grok.order(30)
    reg_name = "KinderUnfallanzeige"
    title = "Unfallanzeigen"

    @property
    def action(self):
        action = super(Unfallanzeige, self).action
        action = action.replace('/add', '?filter=uaz')
        return action



from uvc.layout.slots.interfaces import IRenderable
class Postfach(uvcsite.ProductMenuItem):
    grok.viewletmanager(uvcsite.IQuickLinks)
    grok.context(Interface)
    grok.order(30)
    reg_name = "nachrichten"
    title = "Postfach"

    @property
    def action(self):
        action = super(Postfach, self).action
        action = action.replace('/@@add', '')
        return action


class PostfachP(uvcsite.ProductMenuItem):
    grok.viewletmanager(uvcsite.IGlobalMenu)
    grok.context(Interface)
    grok.implements(IRenderable)
    grok.order(30)
    reg_name = "nachrichten"
    title = "Postfach"

    @property
    def action(self):
        action = super(PostfachP, self).action
        #action = action.replace('/@@add', '')
        return action

    def render(self):
        return "<ul id='main-nav' class='list-unstyled nav pull-right'> <li> <a href='%s'> <img src='/fanstatic/ukh.schulportal/mail_icon_weiss.png'/>  </a> </li> </ul>" % self.action


class MeinDaten(uvcsite.MenuItem):
    grok.context(uvcsite.IMyHomeFolder)
    grok.title(u'Schuldaten')
    grok.viewletmanager(uvcsite.IPersonalMenu)

    @property
    def action(self):
        return self.view.url(self.context, 'meinedaten')


from uvc.layout.slots.managers import Tabs


class Tabs(Tabs):
    grok.layer(ILayer)

    def render(self):
        return ""
