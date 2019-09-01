#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x 

#输入一个数（大于等于一的整数），判断其是否为质数
# 质数：在大于等于1的自然数中，除了1和它本身以外不能被其他数整除
import numpy

def isPrime(number):
    for i in (2,numpy.sqrt(number)+1):
        if number%i == 0:
            return False
        else:
            return True

res = isPrime(100000)
print(res)



