#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x 
import unittest
def multiply_of_three(data):
    data = map(lambda num:num*3,data)
    return list(data)

def sort_and_distinct(data):
    temp = list(dict.fromkeys(data).keys())
    return temp.sort()


def sort_by_amount(data):
    temp = sorted(data,key=lambda voucher:voucher[1],reverse=True)
    return temp


def calc(operation,x,y):
    if operation =='multiply':
        return x*y
    elif operation =='add':
        return x+y
    elif operation =='divide':
        return x/y
    elif operation =='subtract':
        return x-y
    else:
        return '不支持此操作'





class TestProgram(unittest.TestCase):
    def test_task_1(self):
        data = range(0,100)
        filtered =multiply_of_three(data)
        for num in filtered:
            self.assertTrue(num%3==0)



data = [('a',8900),('b',2800),('c',1300),('d',453400)]

if __name__ == '__main__':
    unittest.main()