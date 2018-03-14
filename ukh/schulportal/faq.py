# -*- coding: utf-8 -*-

import grok
import uvcsite


grok.templatedir('templates')


class FAQ(object):

    def __init__(self, q, a, order):
        self.question = q
        self.answer = a
        self.order = order

    def __repr__(self):
        return "<FAQ ITEM>"


# ###############################################################################
# # FAQ01 Erläuterungen zur Unfallanzeige                                       #
# ###############################################################################

FAQ_01_01 = u"""
<p>
Die Unfallanzeige wird zur Feststellung des Versicherungsfalls in der gesetzlichen Unfallversicherung benötigt.
</p>
<p>
Der Unternehmer – also die Leiterin oder der Leiter einer Schule – bestätigt mit seinen Angaben gegenüber dem
</p>
<p>
Unfallversicherungsträger das Vorliegen des Unfalls.
</p>
<br/>
<p>
Der Unfallversicherungsträger kann nur dann tätig werden, wenn er über einen Unfall rechtzeitig informiert wird.
</p>
<p>
Die Anzeige soll ihn möglichst schnell und umfassend über diejenigen Fakten und Daten unterrichten,
</p>
<p>
die zur Bearbeitung des Versicherungsfalls bekannt sein müssen.
</p>
<p>
So kann zum Beispiel anhand der Angaben über Art und Schwere der Verletzung frühzeitig erkannt werden,
</p>
<p>
welche Maßnahmen für eine zügige Rehabilitation des verletzten Kindes eingeleitet werden müssen.
</p>
"""

FAQ_01_02 = u"""
<p>
Unternehmer im Sinne der gesetzlichen Unfallversicherung ist in der Schule der Leiter oder die Leiterin der Einrichtung.
</p>
<p>
Er beziehungsweise sie wird aber in der Regel die Unfallanzeige nicht selbst ausfüllen.
</p>
<p>
Damit befasst sind zumeist die Lehrkräfte oder auch die Schulsekretärinnen.
</p>
<p>
Deshalb bietet die Unfallkasse Hessen ihren Rat bei der sachgemäßen Erstellung einer Unfallanzeige auch in ihren
</p>
<p>
Seminaren für Schulleitungen und Schulsekretärinnen an.
</p>
<br/>
<p>
Diejenigen, die die Unfallanzeigen ausfüllen, sind auf die Informationen der Verletzten und gegebenenfalls der Zeugen angewiesen.
</p>
<p>
Insbesondere bei Wegeunfällen (Unfällen auf den Wegen von und zur Schule) sind die Informationen der Erziehungsberechtigten sehr wertvoll.
</p>
<p>
Eltern müssen darüber informiert sein, dass sie bei einem Wegeunfall ihres Kindes oder einer danach von ihnen veranlassten
</p>
<p>
ärztlichen Behandlung die Schule umgehend benachrichtigen.
</p>
<br/>
<p>
Unabhängig vom Einzelfall besteht für die Verantwortlichen in den Schulen die generelle Pflicht zur Erstattung einer Unfallanzeige.
</p>
<p>
Sie kann nicht auf Eltern oder Dritte übertragen werden!
</p>
"""

FAQ_01_03 = u"""
<p>
Jeder Unfall, bei dem Kosten anfallen (Arztbesuch, Transport), muss dem jeweiligen Unfallversicherungsträger
innerhalb von drei Tagen mittels einer Unfallanzeige mitgeteilt werden.
</p>
"""

FAQ_01_04 = u"""
<p>
Die Erstattung der gesetzlichen Unfallanzeige erfolgt für die hessischen Schulen ausschließlich über das Schulportal der UKH.
</p>
<p>
Mittels der elektronischen Unfallmeldung werden Unfälle direkt an die Unfallkasse Hessen gemeldet.
</p>
<p>
Ein übersichtliches Formular ermöglicht es, die Meldung schnell und fehlerfrei zu übermitteln.
</p>
<p>
Die Anwendung führt bequem und sicher durch das „Formular“. Mit der „eUA“ erfüllen die Unternehmer ihre Meldepflicht nach dem Sozialgesetzbuch.
</p>
<p>
Eine Meldung per Post oder Fax ist überflüssig. Eine formlose Meldung anstelle einer gesetzlichen Unfallanzeige ist nicht zulässig.
</p>
"""

FAQ_01_05 = u"""
<p>
Damit der Unfallhergang zuverlässig wiedergegeben wird, sollen der beziehungsweise
die Verletzte und gegebenenfalls die Zeugen
</p>
<p>
(bzw. die aufsichtführende Lehrkraft) dazu befragt werden. Alle auf dem Vordruck gestellten Fragen sind ausnahmslos zu beantworten.
</p>
<br/>
<p>
Hier die wichtigsten Hinweise zum Ausfüllen der Unfallanzeige:
</p>
<br/>
<ul>
<li>
<b>Ortsangabe:</b> Den Ort genau benennen wie zum Beispiel den Pausenhof, die Treppe, das Klassenzimmer, den Sportplatz oder die Turnhalle!
</p>
<p>
Wenn möglich, sollte auch die genaue Stelle des Unfalls bezeichnet werden. Dabei kann unter Umständen eine Skizze hilfreich sein.
</p>
</li>
<li>
<p>
<b>Zeitangabe:</b> Es sollte rekonstruierbar sein, in welcher Unterrichtsstunde, welcher Pause, ob am Anfang oder am Ende einer
</p>
<p>
Unterrichtseinheit (z. B. Sportunterricht) sich der gemeldete Unfall ereignet hat.
</p>
</li>
<li>
<p>
<b>Tätigkeit:</b> Die Darstellung des Unfallhergangs sollte die Beschreibung der Vorgänge einschließen, die dem Unfall unmittelbar vorausgingen.
</p>
<p>
Es kann zum Beispiel heißen: „auf dem Weg zum Pausenhof“, „beim Aufwärmen zu Beginn der Sportstunde“.
</p>
</li>
<li>
<p>
<b>Unfallhergang:</b> Die Darstellung des Unfalls soll die Bewegungsabsicht enthalten, die dem Unfall vorausging. Sie umfasst alle Umstände,
</p>
<p>
die dazu beitragen können, das Geschehen zu erklären oder falsche Schlussfolgerungen zu vermeiden.
</p>
<br/>
<p>
Die Eintragungen sollen geeignet sein, die besonderen Umstände des Unfalls, vielleicht sogar die Unfallursachen, auszumachen.
</p>
<p>
Daher sind nur Tatsachen einzutragen, keine Schuldzuweisungen, Entschuldigungen („unkonzentriert“, „handelte gegen die Anweisung“,
</p>
<p>
„stürzte unglücklich“ usw.) oder Spekulationen.
</p>
</li>
</ul>
<br/>
<p>
Füllen Sie deshalb Ihre Unfallanzeigen bitte ehrlich und vollständig aus!
</p>
<p>
Damit leisten Sie einen wichtigen Beitrag auch zur Vermeidung von Unfällen in Ihrem Verantwortungsbereich.
</p>
"""

FAQ_01_06 = u"""
<p>
<b>Tödliche Unfälle, Massenunfälle und Unfälle mit schwerwiegenden Gesundheitsschäden</b> sind sofort
</p>
<p>
der Unfallkasse Hessen telefonisch unter 069/29972-440 oder per Mail ukh@ukh.de zu melden.
</p>
"""

FAQITEMS01 = (
    FAQ(u'Warum brauchen die UV-Träger eine Unfallanzeige?', FAQ_01_01, order=1),
    FAQ(u'Wer muss die Unfallanzeige erstatten?', FAQ_01_02, order=2),
    FAQ(u'Wann ist eine Unfallanzeige zu erstatten?', FAQ_01_03, order=3),
    FAQ(u'Wie erfolgt die Meldung?', FAQ_01_04, order=4),
    FAQ(u'Auf den Inhalt kommt es an', FAQ_01_05, order=5),
    FAQ(u'Was ist bei schweren Unfällen, Massenunfällen und Todesfällen zu beachten?', FAQ_01_06, order=6)
)


class FAQ01View(uvcsite.Page):
    # HessGiss
    grok.context(uvcsite.IUVCSite)
    grok.name('faq01')
    title = u"FAQ"
    d1 = u'Nach dem Unfall eines Kindes in der Schule oder bei einer schulischen Veranstaltung '
    d2 = u'gehört es zu den Pflichten des „Unternehmers“, die Unfallanzeige zu erstatten. '
    d3 = u'Um diese gesetzliche Verpflichtung sachgerecht zu erfüllen, sind einige Dinge zu beachten.'
    description = d1 + d2 + d3
    items = FAQITEMS01


# ###############################################################################
# # FAO02 Warum ein Verbandbuch?                                                #
# ###############################################################################

FAQ_02_01 = u"""
<p>
Unfälle, die keine Kosten verursacht haben, also auch keine Unfallanzeige erfordern,
sollten zur Dokumentation in ein Verbandbuch eingetragen werden.
</p>
<p>
Es handelt sich dabei um Bagatellverletzungen, die nach einer Erstversorgung in der Einrichtung
keine weitere ärztliche Behandlung erfordern.
</p>
<p>
Im Verbandbuch wird der Unfall kurz beschrieben, zum Beispiel „Schnittverletzung am Daumen mit Pflasterversorgung“.
</p>
<p>
Der Eintrag in das Verbandbuch kann bei später auftretenden Unfallfolgen, wie der Infektion der Wunde, als Beleg dafür gelten,
</p>
<p>
dass es sich um einen Schulunfall handelte. So können eventuell doch noch entstehende Leistungsansprüche abgesichert werden.
</p>
<p>
Auch hierfür ist im Schulportal ein <b>„elektronisches Verbandbuch“</b> für die hessischen Schulen eingerichtet.
</p>
<p>
<b>Sie können übrigens aus einer Verbandbuch-Eintragung jederzeit eine offizielle Unfallmeldung machen.</b>
</p>
"""

FAQITEMS02 = (
    FAQ(u'Warum ein Verbandbuch?', FAQ_02_01, order=1),
)


class FAQ02View(uvcsite.Page):
    # Warum ein Verbandbuch?
    grok.context(uvcsite.IUVCSite)
    grok.name('faq02')
    title = u"FAQ"
    description = u'Das „e-Verbandbuch“'
    items = FAQITEMS02


# ##############################################################
# # FAQ03 Erste Hilfe                                          #
# ##############################################################


FAQ_03_FRA1 = u"""
Müssen die Berechtigungsscheine bestimmten Fachlehrkräften übergeben werden?
"""

FAQ_03_FRA2 = u"""
Sind an Ihrer Schule regelmäßig Integrationshelfer*innen eingesetzt, die beim Schulträger beschäftigt sind
(nicht bei einem Sonder- oder heilpädagogischen Dienst oder im Rahmen des Elternarbeitgebermodells!),
und die Sie gerne zum/zur Ersthelfer*in aus- oder fortbilden möchten?
"""

FAQ_03_01 = u"""
<p>
Nein. Über die Verteilung der Berechtigungsscheine entscheidet jede Schule individuell, abhängig vom bestehenden Bedarf.
</p>
"""

FAQ_03_02 = u"""
<p>
Ein Antrag ist grundsätzlich durch die Schule oder den Schulträger möglich. Sofern Sie als Schule beantragen möchten,
</p>
<p>
berücksichtigen Sie die Anzahl der regelmäßig eingesetzten Integrationshelfer*innen bitte in Kontingent 7. Wichtig ist,
</p>
<p>
dass keine Doppelbeantragung erfolgt. Daher stimmen Sie sich bitte unbedingt mit Ihrem Schulträger ab,
</p>
<p>
wer sich um die Beantragung der Berechtigungsscheine für Integrationshelfer*innen kümmert.
</p>
<p>
Etwaig zu Unrecht erhaltene Leistungen sind uns in Höhe der entstandenen Kosten zu erstatten.
</p>
"""

FAQITEMS03 = (
    FAQ(FAQ_03_FRA1, FAQ_03_01, order=1),
    FAQ(FAQ_03_FRA2, FAQ_03_02, order=2),
)


class FAQ03View(uvcsite.Page):
    grok.context(uvcsite.IUVCSite)
    grok.name('faq03')
    title = u"FAQ"
    description = u"Kontingent 7 – Erste Hilfe in Schulen"
    items = FAQITEMS03


# ###############################################################################
# # FAQ04 HessGiss                                                              #
# ###############################################################################

FAQ_04_FRA1 = u"""
Haben Sie Fragen zu HessGISS?
"""

FAQ_04_01 = u"""
<p>
Für die spezifische Situation der Schulen wird durch HeeGISS eine zeitgemäße und praktikable Hilfe angeboten
</p>
<p>
- als umfassendes Service-Paket für das Gefahrstoff-Management in der Schule.
</p>
<p>
Individuelle Fragen beantworten die Autoren per Mail. Die Mailadresse finden Sie in der Anwendung.
</p>
"""

FAQITEMS04 = (
    FAQ(FAQ_04_FRA1, FAQ_04_01, order=1),
)


class FAQ04View(uvcsite.Page):
    # HessGiss
    grok.context(uvcsite.IUVCSite)
    grok.name('faq04')
    title = u"FAQ"
    description = u'HessGISS'
    items = FAQITEMS04
