# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import relation

from eteamin.lib.mixins import ConstructorMixin
from eteamin.model import DeclarativeBase, metadata, DBSession


article_tag_table = Table('article_table', metadata,
                          Column('article_id', Integer,
                                 ForeignKey('article.uid',
                                            onupdate="CASCADE",
                                            ondelete="CASCADE"),
                                 primary_key=True),
                          Column('tag_id', Integer,
                                 ForeignKey('tag.uid',
                                            onupdate="CASCADE",
                                            ondelete="CASCADE"),
                                 primary_key=True)
                          )


class Article(DeclarativeBase, ConstructorMixin):

    __tablename__ = 'article'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    text = Column(Unicode, unique=True, nullable=False)
    image = Column(Unicode(25), unique=True, nullable=False)

    created = Column(DateTime, default=datetime.now)
    views = Column(Integer, default=0)

    def __repr__(self):
        return '<Article: name=%s>' % repr(self.title)

    def __unicode__(self):
        return self.title

    @classmethod
    def as_json(cls):
        return dict(uid=cls.uid, title=cls.title, text=cls.text, image=cls.image)


class Tag(DeclarativeBase, ConstructorMixin):

    __tablename__ = 'tag'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(Unicode(25), unique=True, nullable=False)

    articles = relation(Article, secondary=article_tag_table, backref='tag')

    @classmethod
    def as_json(cls):
        return dict(uid=cls.uid, title=cls.title)
