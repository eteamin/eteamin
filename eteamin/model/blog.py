# -*- coding: utf-8 -*-
from datetime import datetime


from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import relation
from tg import abort

from eteamin.lib.mixins import ConstructorMixin
from eteamin.lib.storage import store
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
    image = Column(Unicode, unique=True, nullable=False)

    created = Column(DateTime, default=datetime.now)
    views = Column(Integer, default=0)

    def __repr__(self):
        return '<Article: name=%s>' % repr(self.title)

    def __unicode__(self):
        return self.title

    @classmethod
    def as_json(cls):
        return dict(uid=cls.uid, title=cls.title, text=cls.text)

    @classmethod
    def one_or_none(cls, uid):
        instance = DBSession.query(cls).filter(cls.uid == uid).one_or_none()
        if not instance:
            abort(404, passthrough='json')
        instance.views = instance.views + 1
        return instance

    @classmethod
    def from_request(cls, **kwargs):
        instance = cls()
        instance.image = store(kwargs.get('image'))
        del kwargs['image']
        for k, v in cls.as_json().items():
            instance.__setattr__(k, kwargs.get(k))
        DBSession.add(instance)
        return instance


class Tag(DeclarativeBase, ConstructorMixin):

    __tablename__ = 'tag'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(Unicode(25), unique=True, nullable=False)

    articles = relation(Article, secondary=article_tag_table, backref='tag')

    @classmethod
    def as_json(cls):
        return dict(uid=cls.uid, title=cls.title)
