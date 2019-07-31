#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x

from sqlalchemy import Column, Integer, VARCHAR, Text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
"""
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"kaoshi" varchar(200),
"subject" varchar(200),
"chapter" varchar(200),
"section" varchar(200),
"tixing" varchar(20),
"question_case" text,
"question" text,
"a" varchar(1000),
"b" varchar(1000),
"c" varchar(1000),
"d" varchar(1000),
"e" varchar(1000),
"other_sections" varchar(3000),
"answer" varchar(500),
"analysis" text,
source" text
"""


class TiKu(Base):
    __tablename__ = 'spider_tiku'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    kaoshi = Column(VARCHAR(200), nullable=True)
    subject = Column(VARCHAR(200), nullable=True)
    chapter = Column(VARCHAR(200), nullable=True)
    section = Column(VARCHAR(200), nullable=True)
    tixing = Column(VARCHAR(20), nullable=True)
    question_case = Column(Text(), nullable=True)
    question = Column(Text, nullable=True)
    a = Column(VARCHAR(1000), nullable=True)
    b = Column(VARCHAR(1000), nullable=True)
    c = Column(VARCHAR(1000), nullable=True)
    d = Column(VARCHAR(1000), nullable=True)
    e = Column(VARCHAR(1000), nullable=True)
    other_sections = Column(VARCHAR(3000), nullable=True)
    answer = Column(VARCHAR(500), nullable=True)
    analysis = Column(Text(), nullable=True)
    source = Column(Text(), nullable=True)

    def __str__(self):
        return '< {} {} {}>'.format(self.kaoshi, self.subject, self.chapter)


class SqliteOrm(object):

    def __init__(self, path):
        sqlite_path = 'sqlite:///{}'.format(path)
        self.engine = create_engine(sqlite_path)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_table(self):
        self.drop_table()
        Base.metadata.create_all(self.engine)

    def insert(self, obj):
        # 将该实例插入到表
        self.session.add(obj)
        self.session.commit()

    def insert_many(self, batch_data: list):
        # 一次插入多条记录形式
        self.session.add_all(batch_data)
        self.session.commit()

    def drop_table(self, table_name='spider_tiku'):
        try:
            self.execute_sql('drop table %s' % table_name)
        except Exception as e:
            pass

    def execute_sql(self, sql):
        self.session.execute(sql)
