#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x 
class Hero(object):
    def __init__(self, no=None, nickname=None, name=None, pNext = None):
        self.no = no
        self.nickname = nickname
        self.name = name
        self.pNext = pNext


def addHero(head, pNew):
    cur = head
    while cur.pNext != None:
        if cur.pNext.no > pNew.no:
            break
        cur = cur.pNext
    pNew.pNext = cur.pNext
    cur.pNext = pNew

def showHero(head):
    if isEmpty(head):
        return None

    cur = head

    while cur.pNext != None:
        print("英雄的编号是: %s, 外号是：%s, 姓名:%s" % (cur.pNext.no, cur.pNext.nickname, cur.pNext.name))
        cur = cur.pNext

def isEmpty(head):
    if head.pNext != None:
        return False
    return True

def delHero(head, no):
    cur = head
    while cur.pNext != None:
        if cur.pNext.no == no:
            cur.pNext = cur.pNext.pNext
            break
        cur = cur.pNext
    print('不存在')

def append(head,pNew):
    cur = head
    while cur.pNext != None:
        cur = cur.pNext
    cur.pNext = pNew


# 头结点
head = Hero()

## 首节点
h1 = Hero(1, '及时雨', '宋江')
h2 = Hero(2, '玉麒麟', '卢俊义')
h3 = Hero(6, '豹子头', '林冲')
h4 = Hero(4, '入云龙', '公孙胜')

addHero(head, h1)
addHero(head, h2)
addHero(head, h3)
addHero(head, h4)

showHero(head)
print('*'*40)

delHero(head,4)
showHero(head)
print('*'*40)
