#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import pandas as pd
import pymysql


def connect_db():
    MYSQL_HOSTS = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_PORT = 3306
    MYSQL_DB = 'xiaoshuo'
    conn = pymysql.connect(
        host=MYSQL_HOSTS,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        passwd=MYSQL_PASSWORD,
        db=MYSQL_DB,
        charset="utf8")
    return conn


def select_data(dict=False):
    conn = connect_db()
    sql = '''select * from dd_name'''
    cursor = conn.cursor()
    if not dict:
        sql = '''select xs_name,category,name_id,xs_author from dd_name'''
    else:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def save_as(data, columns):
    df = pd.DataFrame(data=list(data), index=range(len(data)), columns=columns)
    df.to_csv("output.csv")
    df.to_excel("output.xlsx")


def modelOne():
    data = select_data()
    columns = ["名称", "分类", "书号", "作者", ]
    save_as(data, columns)


def modelTwo():
    data = select_data(dict=True)
    columns = ["xs_name", "category", "name_id", "xs_author", ]
    save_as(data, columns)


modelOne()
# modelTwo()

df = pd.read_excel('output.xlsx')
# data=df.ix[::-1].values
# data=df.ix[0,1]

# data=df.ix[:,['名称','作者']].values#读所有行的title以及data列的值，这里需要嵌套列表
# data =df.columns.values
# print(data)
