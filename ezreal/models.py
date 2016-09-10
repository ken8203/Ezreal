# -*- coding: utf-8 -*-

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('poems.db', journal_mode='WAL')

class BaseModel(Model):
    class Meta:
        database = db

class Poems(BaseModel):
    author = CharField()
    title = CharField()
    content = CharField()
    dynasty = CharField()

