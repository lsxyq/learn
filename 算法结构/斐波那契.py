#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x


# 斐波那契数列：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

def fb(num):
    a=0
    b=1
    for i in range(num):
        c =a+b
        print(c)
        a=b
        b=c

fb(10)






def fibRecursion(num):
    print(100-num+1)
    '''
    直接使用递归法求解斐波那契数量的第num个数字
    '''
    if num<2:
        return num
    return fibRecursion(num-1)+fibRecursion(num-2)





def fibTailRecursion(num,res,temp):
    '''
    使用尾递归法求解斐波那契数量的第num个数字
    '''
    if num==0:
        return res
    else:
        return fibTailRecursion(num-1, temp, res+temp)



# res2= fibTailRecursion(100,1,1)
# print(res2)