# -*- coding: utf-8 -*-

import grok
import uvcsite
import zope.component

from zope.interface import Interface
from zope import schema
from zope.session.interfaces import ISession
from resources import taxicss, taxijs
from zeam.form.base import NO_VALUE, Error
from time import strptime

grok.templatedir('templates')


KEY = "taxigutschein"


class ITaxiGutscheine(Interface):
    nname = schema.TextLine(title=u'Name des Schülers *',)
    vname = schema.TextLine(title=u'Vorname des Schülers *',)
    geburtsdatum = schema.TextLine(title=u'Geburtsdatum des Schülers *',)
    unfalltag = schema.TextLine(title=u'Tag des Unfalls *',)
    tagfahrt = schema.TextLine(title=u'Tag der Fahrt *',)
    zielfahrt = schema.TextLine(title=u'Ziel der Fahrt *',)


class TaxiGutscheineInfo(uvcsite.Form):
    grok.context(Interface)
    grok.name('taxigutscheine')
    label = u"Taxi-Gutschein"

    @uvcsite.action('Abbrechen')
    def handle_cancel(self):
        self.flash(u'Die Aktion wurde abgebrochen.')
        self.redirect(self.application_url())

    @uvcsite.action('Taxi-Gutschein')
    def handle_send(self):
        self.redirect(self.url(self.context, 'taxigutscheineview'))


class TaxiGutscheineView(uvcsite.Form):
    grok.implements(ITaxiGutscheine)
    grok.context(Interface)
    grok.name('taxigutscheineview')
    label = u"Taxi-Gutschein"

    fields = uvcsite.Fields(ITaxiGutscheine)

    def update(self):
        taxicss.need()
        taxijs.need()


    @property
    def macros(self):
        return zope.component.getMultiAdapter(
            (self.context, self.request),
            name='fieldmacros'
        ).template.macros

    @uvcsite.action('Abbrechen')
    def handle_cancel(self):
        self.flash(u'Die Aktion wurde abgebrochen.')
        self.redirect(self.application_url())

    @uvcsite.action('Taxi-Gutschein erstellen')
    def handle_send(self):
        data, errors = self.extractData()
        if errors:
            return
        adr = self.request.principal.getAdresse()
        taxidata = {}
        taxidata['name'] = data['vname'] + ' ' + data['nname']
        taxidata['geburtsdatum'] = data['geburtsdatum']
        taxidata['unfalltag'] = data['unfalltag']
        taxidata['zielfahrt'] = data['zielfahrt']
        taxidata['tagfahrt'] = data['tagfahrt']
        taxidata['adrname'] = adr['iknam1'].strip() + ' ' + adr['iknam2'].strip() + ' ' + adr['iknam3'].strip()
        taxidata['adrstrasse'] = adr['ikstr'].strip() + ' ' + str(adr['ikhnr']).strip()
        taxidata['adrplzort'] = str(adr['ikhplz']).strip() + ' ' + adr['ikhort'].strip()
        taxidata['schulnummer'] = str(adr['enrlfd']).strip()
        vssession = ISession(self.request)[KEY]
        vssession['daten'] = taxidata
        self.redirect(self.url(self.context, 'taxigutschein'))

    def validateData(self, fields, data):
        errors = super(TaxiGutscheineView, self).validateData(fields, data)
        for x in [['nname', u'Nachname des Schülers'],
                  ['vname', u'Vorname des Schülers'],
                  ['zielfahrt', u'Ziel der Fahrt']]:
            if data.get(x[0]) == NO_VALUE or data.get(x[0]) == '':
                t1 = u'Fehler im Feld " '
                t2 = x[1]
                t3 = u' " Das Feld darf nicht leer sein, bitte geben Sie einen Text ein.'
                errors.append(Error(u'Fehler!!!'))
                self.flash(t1 + t2 + t3)
        for x in [['geburtsdatum', u'Geburtsdatum des Schülers'],
                  ['unfalltag', u'Tag des Unfalls'],
                  ['tagfahrt', u'Tag der Fahrt']]:
            if data.get(x[0]) == NO_VALUE or data.get(x[0]) == '':
                t1 = u'Fehler im Feld " '
                t2 = x[1]
                t3 = u' " Das Feld darf nicht leer sein, bitte geben Sie ein Datum ein.'
                errors.append(Error(u'Fehler!!!'))
                self.flash(t1 + t2 + t3)
        ######################################################################
        # CHECK Datum                                                        #
        ######################################################################
        for x in [['geburtsdatum', u'Geburtsdatum des Schülers'],
                  ['unfalltag', u'Tag des Unfalls'],
                  ['tagfahrt', u'Tag der Fahrt']]:
            if data.get(x[0]) != NO_VALUE and data.get(x[0]) != '':
                d = False
                try:
                    strptime(data.get(x[0]), "%d.%m.%Y")
                    d = True
                except ValueError:
                    t1 = u'Fehler im Feld " '
                    t2 = x[1]
                    t3 = u' " Das Datum hat einen Fehler. Bitte überprüfen Sie das Datum!'
                    errors.append(Error(u'Fehler!!!'))
                    self.flash(t1 + t2 + t3)
                if d is True:
                    j = data.get(x[0])[6:8]
                    if j < '19' or j > '20':
                        t1 = u'Fehler im Feld " '
                        t2 = x[1]
                        t3 = u' " Die Jahreszahl ist falsch! Bitte ändern Sie das Datum.'
                        errors.append(Error(u'Fehler!!!'))
                        self.flash(t1 + t2 + t3)
        return errors
