#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x 
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = Node(None)
        self.rear = self.front

    def enQueue(self, element):
        n = Node(element)
        self.rear.next = n
        self.rear = n

    def deQueue(self):
        if self.empty():
            print('队空')
            return
        temp = self.front.next
        self.front = self.front.next
        if self.rear == temp:
            self.rear = self.front
        del temp

    def getHead(self):
        if self.empty():
            print('队空')
            return
        return self.front.next.data

    def empty(self):
        return self.rear == self.front

    def printQueue(self):
        cur = self.front.next
        while cur != None:
            print(cur.data)
            cur = cur.next

    def length(self):
        cur = self.front.next
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count


if __name__ == '__main__':
    queue = Queue()
    queue.enQueue(23)
    queue.enQueue(2)
    queue.enQueue(4)
    queue.printQueue()
    queue.deQueue()
    # queue.printQueue()
    l = queue.length()
    print("长度是: %d" % l)
    queue.deQueue()
    # queue.printQueue()
    l = queue.length()
    print("长度是: %d" % l)
    queue.deQueue()
    # queue.printQueue()
    l = queue.length()
    print("长度是: %d" % l)
