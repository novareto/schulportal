# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


import grok
import uvcsite
from zope.component import getUtility
from uvcsite.extranetmembership.interfaces import IUserManagement
from uvcsite.utils.mail import send_mail


TEXT = u"""
Sehr geehrte Damen und Herren,

bitte öffnen Sie nachfolgenden Link um Ihr Passwort zurückzusetzen und ein neues Passwort zu vergeben.

https://schulportal-weblogin.ukh.de/resetpassword?form.field.username=%s&form.field.challenge=%s


Mit freundlichen Grüßen
Ihr UKH-Team
"""


TEXT_CONFIRM = u"""
Sehr geehrte Damen und Herren,

kürzlich wurde das Passwort für Ihren Zugang zum UKH-Schulportal geändert.
Benutzername: %s

Wenn Sie diese Passwortänderung nicht angefordert haben, wenden Sie sich bitte an das UKH-Team.


Web: http://www.ukh.de
E-Mail: ukh@ukh.de

Ihr UKH-Team

"""


class PasswordActions(grok.JSON):
    grok.context(uvcsite.IUVCSite)

    @property
    def um(self):
        return getUtility(IUserManagement)

    def get_user(self):
        mnr = self.request.form.get('username', None)
        if mnr:
            user = self.um.getUser(mnr)
            if user:
                return dict(mnr=user['mnr'], passwort=user['passwort'], email=user['email'])
        return {'auth': 0}

    def send_mail(self):
        user = self.request.form.get('username')
        mail = self.request.form.get('email')
        hash = self.request.form.get('hash_value')
        text = TEXT % (user, hash)
        send_mail('schulportal@ukh.de', (mail, 'ck@novareto.de'), u"UKH Schulportal Passwortänderung", text)
        return {'success': 'true'}

    def set_user(self):
        username = self.request.form.get('username')
        password = self.request.form.get('password')
        if username and password:
            self.um.updatePasswort(mnr=username, passwort=password)
            return {'success': 'true'}
        return {'success': 'false'}

    def send_confirm(self):
        user = self.request.form.get('username')
        mail = self.request.form.get('email')
        text = TEXT_CONFIRM % (user)
        userobject = self.um.getUser(user)
        send_mail('schulportal@ukh.de', (userobject['email'], 'ck@novareto.de'), u"UKH Schulportal Passwortänderung", text)
        return {'success': 'true'}
