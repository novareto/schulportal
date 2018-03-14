# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

from zope.interface import Interface
from zope.schema import TextLine, Choice


class IStammdaten(Interface):
    """ Benuzter Stammdaten Verwaltung """

    anr = Choice(
            title = u"Anrede",
            values = ('Herr', 'Frau'),
            )

    titel = TextLine(
            title = u"Titel",
            required = False,
            )

    vname = TextLine(
            title = u"Vorname"
            )

    nname = TextLine(
            title = u"Nachname"
            )

    funktion = TextLine(
            title = u"Funktion",
            )

    email = TextLine(
            title = u"E-Mail",
            )

    vwhl = TextLine(
            title = u"Vorwahl"
            )

    tlnr = TextLine(
            title = u"Telefonnummer"
            )

