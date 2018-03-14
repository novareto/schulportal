#!/usr/bin/env python
# -*- coding: utf-8 -*-
import grok
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import black, blue
from time import gmtime, strftime
from uvcsite.utils.dataviews import BasePDF
from zope.session.interfaces import ISession                                                                                                                   


KEY = "taxigutschein"

class TGPDF(BasePDF):
    grok.name('taxigutschein')
    grok.title('Taxi-Gutschein')


    def genpdf(self):
        # Einlesen der Daten aus dem Zwischenpeicher der Session
        vssession = ISession(self.request)[KEY]
        data = vssession['daten']
        print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        print data
        print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        # Layout Seite 1
        #fillcolortransparent = Color(0, 0, 0, alpha=0.2)
        #c = canvas.Canvas(tmp, pagesize=A4)
        c = self.c
        c.setAuthor("UKH")
        c.setTitle(u'Taxi-Gutschein')
        schriftart = "Helvetica"
        schriftartfett = "Helvetica-Bold"
        datum = strftime("%d.%m.%Y", gmtime())
        #####################################################
        # Grauer Hintergrund                                #
        #####################################################
        #c.setFillGray(0.85)
        #c.rect(1.4 * cm, 0.5 * cm, width=19.0 * cm, height=28.9 * cm, stroke=0, fill=1)
        #####################################################
        # Überschrift                                       #
        #####################################################
        c.setFillColor(black)
        c.setFont(schriftart, 20)
        #c.setFont(schriftartfett, 20)
        c.drawString(1.6 * cm, 28.5 * cm, u"Taxi-Gutschein")
        #####################################################
        # Name                                              #
        #####################################################
        x = 1.6
        y = 27.0
        ab1 = 0.4
        c.setFont(schriftart, 9)
        c.drawString(x * cm, y * cm, u"Die Unfallkasse Hessen (UKH) sorgt nach einem Schulunfall für die ärztliche Behandlung der Schüler. Um die Unfallfolgen")
        y -= ab1
        c.drawString(x * cm, y * cm, u"so gering wie möglich zu halten, ist häufig die schnelle Vorstellung beim Arzt oder im Krankenhaus notwendig. Diese stellen")
        y -= ab1
        c.drawString(x * cm, y * cm, u"wir mit unserem „Taxi-Gutschein“ sicher. Für Taxifahrten zahlen wir die Kosten nach dem gültigen amtlichen Taxitarif. Für")
        y -= ab1
        c.drawString(x * cm, y * cm, u"Beförderungen mit einem Mietwagen übernehmen wir die ortsüblichen Beförderungskosten, höchstens jedoch den für den")
        y -= ab1
        c.drawString(x * cm, y * cm, u"Bezirk geltenden Taxitarif. Bitte füllen Sie den Fahrauftrag vollständig aus und leiten Sie diesen anschließend an die Taxi")
        y -= ab1
        c.drawString(x * cm, y * cm, u"Frankfurt eG weiter. Von dort erhalten die beauftragten Taxiunternehmen die Beförderungskosten spätestens einen Monat")
        y -= ab1
        c.drawString(x * cm, y * cm, u"nach Ihrer Abrechnung per Überweisung. Taxi Frankfurt eG berechnet für die zentrale Abrechnung eine branchenübliche")
        y -= ab1
        c.drawString(x * cm, y * cm, u"Gebühr in Höhe von maximal 5 % der Beförderungskosten zzgl. gesetzlicher Mehrwertsteuer.")
        y -= ab1
        y -= ab1
        c.drawString(x * cm, y * cm, u"Ihre Unfallkasse Hessen")
        y -= ab1
        y -= ab1
        c.drawString(x * cm, y * cm, u"Bitte zurücksenden an folgende Adresse: Taxi Frankfurt eG, Heidelberger Straße 25, 60327 Frankfurt am Main")
        y -= ab1
        y -= ab1
        c.setFont(schriftartfett, 9)
        c.drawString(x * cm, y * cm, u"Telefon 069 252025")
        y -= ab1
        y -= ab1
        c.setLineWidth(1.0)
        c.line(x * cm, y * cm, 19.0 * cm, y * cm)
        y -= ab1
        y -= ab1
        c.setFont(schriftartfett, 16)
        c.drawString(x * cm, y * cm, u"Fahrauftrag an das Taxiunternehmen")
        y -= ab1
        c.setFont(schriftart, 9)
        c.drawString(x * cm, y * cm, u"(von der Schule auszufüllen)")
        y -= ab1
        y -= ab1
        c.drawString(x * cm, y * cm, u"Hiermit beauftragen wir das Taxiunternehmen, die unten bezeichnete Person auf Rechnung der Unfallkasse Hessen zum")
        y -= ab1
        c.drawString(x * cm, y * cm, u"Arzt bzw. ins Krankenhaus zu befördern.")
        y -= ab1
        y -= ab1
        c.drawString(x * cm, y * cm, u"Name und Anschrift der Schule:")
        c.drawString(7.0 * cm, y * cm, data['adrname'])
        y -= ab1
        c.drawString(7.0 * cm, y * cm, data['adrstrasse'])
        y -= ab1
        c.drawString(7.0 * cm, y * cm, data['adrplzort'])
        y -= ab1
        c.drawString(x * cm, y * cm, u"Schulnummer:")
        c.drawString(7.0 * cm, y * cm, data['schulnummer'])
        y -= ab1
        c.drawString(x * cm, y * cm, u"Vorname und Name des Schülers:")
        c.drawString(7.0 * cm, y * cm, data['name'])
        y -= ab1
        c.drawString(x * cm, y * cm, u"Geburtsdatum des Schülers:")
        c.drawString(7.0 * cm, y * cm, data['geburtsdatum'])
        y -= ab1
        c.drawString(x * cm, y * cm, u"Tag des Unfalls:")
        c.drawString(7.0 * cm, y * cm, data['unfalltag'])
        y -= ab1
        c.drawString(x * cm, y * cm, u"Tag der Fahrt:")
        c.drawString(7.0 * cm, y * cm, data['tagfahrt'])
        y -= ab1
        c.drawString(x * cm, y * cm, u"Ziel der Fahrt:")
        c.drawString(7.0 * cm, y * cm, data['zielfahrt'])
        y -= ab1
        y -= ab1
        y -= ab1
        c.drawString(x * cm, y * cm, u"Unterschrift der Lehrkraft bzw. Schulsekretariat:")
        y -= 0.1
        c.setLineWidth(0.5)
        c.line(x * cm, y * cm, 19.0 * cm, y * cm)
        y -= ab1
        y -= ab1
        c.setFont(schriftartfett, 9)
        c.drawString(x * cm, y * cm, u"Wichtig: Dieser Fahrauftrag gilt nicht für Fahrten zur nachgehenden ärztlichen Behandlung, für tägliche Fahrten zur")
        y -= ab1
        c.drawString(x * cm, y * cm, u"Schule und bei Erkrankungen ohne Unfallereignis (z.B. Übelkeit, Fieber, Bauchschmerzen, Schwindel etc.).")
        y -= ab1
        y -= ab1
        c.setLineWidth(1.0)
        c.line(x * cm, y * cm, 19.0 * cm, y * cm)
        y -= ab1
        y -= ab1
        c.setFont(schriftartfett, 16)
        c.drawString(x * cm, y * cm, u"Rechnung")
        y -= ab1
        c.setFont(schriftart, 9)
        c.drawString(x * cm, y * cm, u"(vom Taxiunternehmen auszufüllen)")
        y -= ab1
        y -= ab1
        c.drawString(x * cm, y * cm, u"Taxiunternehmen:")
        c.drawString(12.0 * cm, y * cm, u"Steuernummer:")
        y -= 0.1
        c.setLineWidth(0.5)
        c.line(x * cm, y * cm, 19.0 * cm, y * cm)
        y -= ab1
        c.drawString(x * cm, y * cm, u"Taxi- und Rechnungsnummer:")
        y -= 0.1
        c.setLineWidth(0.5)
        c.line(x * cm, y * cm, 19.0 * cm, y * cm)
        y -= ab1
        c.drawString(x * cm, y * cm, u"Ziel der Fahrt (Name und Anschrift):")
        y -= 0.1
        c.setLineWidth(0.5)
        c.line(x * cm, y * cm, 19.0 * cm, y * cm)
        y -= ab1
        c.drawString(x * cm, y * cm, u"Datum der Fahrt:")
        y -= 0.1
        c.setLineWidth(0.5)
        c.line(x * cm, y * cm, 19.0 * cm, y * cm)
        y -= ab1
        c.drawString(x * cm, y * cm, u"Gefahrene Kilometer:")
        c.drawString(12.0 * cm, y * cm, u"Fahrpreis inkl. MwSt.:")
        y -= 0.1
        c.setLineWidth(0.5)
        c.line(x * cm, y * cm, 19.0 * cm, y * cm)
        y -= ab1
        y -= ab1
        c.setFont(schriftartfett, 9)
        c.drawString(x * cm, y * cm, u"Überweisung des Fahrpreises bitte auf folgendes Konto:")
        y -= ab1
        y -= ab1
        c.setFont(schriftart, 9)
        c.drawString(x * cm, y * cm, u"Geldinstitut:")
        y -= 0.1
        c.setLineWidth(0.5)
        c.line(x * cm, y * cm, 19.0 * cm, y * cm)
        y -= ab1
        c.drawString(x * cm, y * cm, u"IBAN:")
        c.drawString(12.0 * cm, y * cm, u"BIC:")
        y -= 0.1
        c.setLineWidth(0.5)
        c.line(x * cm, y * cm, 19.0 * cm, y * cm)
        y -= ab1
        c.drawString(x * cm, y * cm, u"Kontoinhaber:")
        y -= 0.1
        c.setLineWidth(0.5)
        c.line(x * cm, y * cm, 19.0 * cm, y * cm)
        y -= ab1
        y -= ab1
        c.drawString(x * cm, y * cm, u"Datum und Unterschrift des Taxiunternehmens:")
        y -= ab1
        y -= ab1
        y -= ab1
        c.setLineWidth(0.5)
        c.line(x * cm, y * cm, 19.0 * cm, y * cm)
        y -= ab1
        c.drawString(x * cm, y * cm, u"Die Taxi Frankfurt eG regelt die Abrechnung im Auftrag der Unfallkasse Hessen.")









        #####################################################
        # Datum                                             #
        #####################################################
        c.setFont(schriftart, 10)
        c.drawString(18.2 * cm, 0.6 * cm, datum)
        # Seitenumbruch
        c.showPage()
        # ENDE und Save
        ###c.save()






def taxipdf(data, tmp):


        # Layout Seite 1
        #fillcolortransparent = Color(0, 0, 0, alpha=0.2)
    c = canvas.Canvas(tmp, pagesize=A4)

    c.setAuthor("UKH")
    c.setTitle(u'Taxi-Gutschein')
    schriftart = "Helvetica"
    schriftartfett = "Helvetica-Bold"
    datum = strftime("%d.%m.%Y", gmtime())
    #####################################################
    # Grauer Hintergrund                                #
    #####################################################
    c.setFillGray(0.85)
    c.rect(1.4 * cm, 0.5 * cm, width=19.0 * cm, height=28.9 * cm, stroke=0, fill=1)
    #####################################################
    # Überschrift                                       #
    #####################################################
    c.setFillColor(black)
    c.setFont(schriftartfett, 20)
    c.drawString(1.6 * cm, 28.5 * cm, u"BlaBlaBla")
    #####################################################
    # Name                                              #
    #####################################################
















    #####################################################
    # Datum                                             #
    #####################################################
    c.setFont(schriftart, 10)
    c.drawString(18.2 * cm, 0.6 * cm, datum)
    # Seitenumbruch
    c.showPage()
    # ENDE und Save
    ###c.save()


