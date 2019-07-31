#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import json
import sqlite3


class SqliteDB(object):

    def __init__(self):
        self.conn = sqlite3.connect(r"C:\Projects\learn\zuntiku\zuntiku.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(
            """CREATE TABLE "spider_kst" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,"kaoshi" varchar(200),"subject" varchar(200),"chapter" varchar(200),"section" varchar(200),"tixing" varchar(20),"question_case" text,"question" text,"a" varchar(1000),"b" varchar(1000),"c" varchar(1000),"d" varchar(1000),"e" varchar(1000),"other_sections" varchar(3000),"answer" varchar(500),"analysis" text,"source" text);"""
        )

    def data_clean(self, table,data: dict):
        keys,values = [],[]
        for k, v in data.items():
            if not v:continue
            keys.append(k)
            values.append(str(v))
        self.insert_data(table,keys,values)


    def insert_data(self, table, keys,values):
        params = ['?' for i in range(len(keys))]
        sql = '''INSERT INTO {}({}) VALUES({})'''.format(table, ','.join(keys), ','.join(params))
        self.cursor.execute(sql,values)
        self.conn.commit()


db = SqliteDB()

if __name__ == '__main__':
    db.create_table()


