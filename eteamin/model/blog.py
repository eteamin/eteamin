# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import relation

from eteamin.model import DeclarativeBase, metadata


article_tag_table = Table('article_table', metadata,
                          Column('article_id', Integer,
                                 ForeignKey('article.article_id',
                                            onupdate="CASCADE",
                                            ondelete="CASCADE"),
                                 primary_key=True),
                          Column('tag_id', Integer,
                                 ForeignKey('tag.tag_id',
                                            onupdate="CASCADE",
                                            ondelete="CASCADE"),
                                 primary_key=True)
                          )


class Article(DeclarativeBase):

    __tablename__ = 'article'

    article_id = Column(Integer, autoincrement=True, primary_key=True)
    article_title = Column(Unicode(255), unique=True, nullable=False)
    article_text = Column(Unicode, unique=True, nullable=False)
    article_image = Column(Unicode(25), unique=True, nullable=False)

    created = Column(DateTime, default=datetime.now)
    views = Column(Integer, default=0)

    def __repr__(self):
        return '<Article: name=%s>' % repr(self.title)

    def __unicode__(self):
        return self.title


class Tag(DeclarativeBase):

    __tablename__ = 'tag'

    tag_id = Column(Integer, autoincrement=True, primary_key=True)
    tag_title = Column(Unicode(25), unique=True, nullable=False)

    articles = relation(Article, secondary=article_tag_table, backref='tag')
