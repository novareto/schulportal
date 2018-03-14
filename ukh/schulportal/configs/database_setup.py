# -*- coding: utf-8 -*-
#
#
# 15.06.2010

import grok
import logging


from z3c.saconfig import EngineFactory, GloballyScopedSession
from z3c.saconfig.interfaces import IEngineCreatedEvent
from zope.app.appsetup.product import getProductConfiguration
from sqlalchemy import Table, MetaData, create_engine


#logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)


config = getProductConfiguration('database')
DSN = config['dsn']
print DSN
USER_TABLE = config['user_table']
ENR_TABLE = config['enr_table']
TRG_TABLE = config['trg_table']


engine_factory = EngineFactory(DSN, echo=False)
scoped_session = GloballyScopedSession()

grok.global_utility(engine_factory, direct=True)
grok.global_utility(scoped_session, direct=True)


engine = engine_factory()
metadata = MetaData(bind=engine)

schema_name = "UKHINTERN"
schema_name2 = "ukhph"
schema_name3 = "educusadat"

users = Table('z1ehr1aa_t', metadata, schema=schema_name, autoload=True, autoload_with=engine)
einrichtungen = Table('z1ehr1ac_t', metadata, schema=schema_name, autoload=True, autoload_with=engine)
traegeruaz = Table('mitrg1aa', metadata, schema=schema_name3, autoload=True, autoload_with=engine)
