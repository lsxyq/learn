#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x
class Stack(object):
    def __init__(self):
        self.pTop = None
        self.pBottom = None


class Node(object):
    def __init__(self, data=None, pNext=None):
        self.data = data
        self.pNext = pNext


def push(s, new):
    new.pNext = s.pTop
    s.pTop = new


def pop(s):
    cur = s.pTop
    # while cur != s.pBottom:
    #     if cur.data == val:
    #         s.pTop = cur.pNext
    #         break
    #     cur = cur.pNext
    # else:
    #     print('没有找到此元素')
    while cur != s.pBottom:
        s.pTop = cur.pNext
        print("出栈的元素是: %d" % cur.data)
        cur = cur.pNext
    else:
        print("出栈失败")


def getAll(s):
    cur = s.pTop
    while cur != s.pBottom:
        print(cur.data)
        cur = cur.pNext


def is_empty(s):
    if s.pTop == s.pBottom:
        return True
    else:
        return False


def clear(s):
    if is_empty(s):
        return None
    p = s.pTop
    q = None
    while p != s.pBottom:
        q = p.pNext
        del p
        p = q
    else:
        s.pBottom = s.pTop


head = Node()
s = Stack()
s.pTop = s.pBottom = head
n1 = Node(2)
push(s, n1)
n1 = Node(5)
push(s, n1)
n1 = Node(89)
push(s, n1)
print("##############遍历元素##########")
getAll(s)
# print("##############出栈元素#######")
# pop(s)
print("##############清空栈##########")
clear(s)
print("##############遍历元素##########")
getAll(s)
