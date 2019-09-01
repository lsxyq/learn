#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x 
class Child(object):
    first = None

    def __init__(self, no=None, pNext=None):
        self.no = no
        self.pNext = pNext

    def addChild(self):
        cur = None
        for i in range(4):
            child = Child(i + 1)
            if i == 0:
                self.first = child
                child.pNext = self.first
                cur = self.first
            else:
                cur.pNext = child
                child.pNext = self.first
                cur = cur.pNext

    def showChild(self):
        cur = self.first
        while cur.pNext != self.first:
            print("孩子的编号是: %s" % cur.no)
            cur = cur.pNext
        print("孩子的编号是: %s" % cur.no)

    def countChild(self,start,count):
        tail = self.first

        while tail.pNext != self.first:
            tail = tail.pNext

        for i in range(start-1):
            self.first = self.first.pNext
            tail = tail.pNext

        while tail != self.first:  # 当tail == first 说明只剩一个人
            for i in range(count-1):
                tail = tail.pNext
                self.first = self.first.pNext
            self.first = self.first.pNext
            tail.pNext = self.first

        print('number:',tail.no)



child = Child()
child.addChild()
child.showChild()
child.countChild(1,1)
