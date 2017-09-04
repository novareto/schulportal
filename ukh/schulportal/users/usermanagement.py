#!/usr/bin/python
# -*- coding: utf-8 -*-

import grok
import uvcsite

from ukhtheme.grok.layout import ILayer
from zope.pluggableauth.factories import Principal, AuthenticatedPrincipalFactory
from uvcsite.extranetmembership.interfaces import IUserManagement, IExtranetMember
from zope.pluggableauth.interfaces import IPrincipalInfo, AuthenticatedPrincipalCreated

from sqlalchemy import and_
from z3c.saconfig import Session
from ukh.schulportal.configs.database_setup import users
from zope.sqlalchemy import mark_changed


class User(dict):
    pass


class UserManagement(grok.GlobalUtility):
    """ Utility for Usermanagement """
    grok.implements(IUserManagement)

    UserInterface = IExtranetMember

    def updUser(self, **kwargs):
        """Updates a User"""
        mnr = kwargs.get('mnr')
        az = kwargs.get('az')
        session = Session()
        sql = users.update().where(
            and_(users.c.login == mnr, users.c.az == az)
            ).values(passwort=kwargs.get('passwort'))  # , =','.join(kw.get('rollen')))
        session.execute(sql)
        mark_changed(session)

    def deleteUser(self, cn):
        mnr, az = self.zerlegUser(cn)
        session = Session()
        sql = users.delete().where(and_(users.c.login == mnr, users.c.az == az))
        session.execute(sql)
        mark_changed(session)

    def addUser(self, **kw):
        mnr, az = kw['mnr'].split('-')
        mnr, az = self.zerlegUser(kw['mnr'])
        user = self.getUser(mnr)
        session = Session()
        sql = users.insert(dict(
            login=mnr,
            passwort=kw.get('passwort'),
            az=az,
            email=kw.get('email', ''),
            oid=str(user['oid']),
            )
        )
        session.execute(sql)
        mark_changed(session)

    def zerlegUser(self, mnr):
        ll = mnr.split('-')
        if len(ll) == 1:
            return mnr, 'eh'
        return ll

    def getUser(self, mnr):
        """Return a User"""
        mnr, az = self.zerlegUser(mnr)
        session = Session()
        query = session.query(users).filter(
            users.c.login == mnr, users.c.az == az)

        if query.count() == 1:
            result = query.one()
            az = result.az
            if result.az == 'eh':
                az = '00'
            return User(
                mnr=result.login,
                az=az,
                oid=result.oid,
                email=result.email,
                passwort=result.passwort,
                rollen=[])
        return None

    def getUsersByMnr(self, mnr):
        return self.getUser(mnr)

    def getUserByEMail(self, mail):
        session = Session()
        query = session.query(users).filter(
            users.c.email == mail)

        if query.count() == 1:
            result = query.one()
            az = result.az
            if result.az == 'eh':
                az = '00'
            return User(
                mnr=result.login,
                az=az,
                oid=result.oid,
                email=result.email,
                passwort=result.passwort,
                rollen=[])
        return None

    def getUserGroups(self, mnr):
        """Return a group of Users"""
        ret = []
        session = Session()
        query = session.query(users).filter(users.c.login == mnr)
        for x in query.all():
            if x.az == "eh":
                continue
            usr = "%s-%s" % (x.login, x.az)
            ret.append(User(
                cn=usr, mnr=x.login, rollen=x.merkmal or [], az=x.az))
        return ret

    def updatePasswort(self, **kwargs):
        """Change a passwort from a user"""

    def checkRule(self, login):
        uvcsite.log(login)
        return True


class UVCPrincipal(Principal):

    foo = u"bar"


class MyOwnPrincpalFactory(AuthenticatedPrincipalFactory, grok.MultiAdapter):
    grok.adapts(IPrincipalInfo, ILayer)

    def __call__(self, authentication):
        principal = UVCPrincipal(
            authentication.prefix + self.info.id,
            self.info.title,
            self.info.description)
        grok.notify(AuthenticatedPrincipalCreated(
            authentication, principal, self.info, self.request))
        return principal
