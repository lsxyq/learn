#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x
"""
多个函数调用时，按照“先调用后返回”的原则，函数之间的信息传递和控制转移必须借助栈来实现，即系统将整个
程序运行时所需要的数据空间安排在一个栈中，每当调用一个函数时，就在栈顶分配一个存储区，进行压栈操作，
每当一个函数退出时，就释放他的存储区，即进行出栈操作，当前运行的函数永远在栈顶的位置

"""


def f():
    print('FFFFFFF')
    g()


def g():
    print('GGGGGGG')
    k()


def k():
    print('KKKKKKK')

#
# if __name__ == "__main__":
#     f()


# 自己调用自己也是和上面的原理一样

#
# def f(n):
#     if n == 1:
#         print('hello')
#     else:
#         f(n - 1)


"""
递归满足的条件
递归必须有一个明确的终止条件
该函数所处理的数据规模是必须递减的
这个转化必须是可解的
"""

#求阶乘
#for循环实现
# multi = 1
# for i in range(3):
#     multi = multi * (i+1)
# print(multi)
# 递归实现


def foo_tail(n,res):
    if 1 ==n:
        return res
    else:
        return foo_tail(n-1,res*n)

foo_tail(1000,1)


def foo(n):
    if 1 == n:
        return 1
    else:
        return foo(n-1)*n

foo(1000)




#1+2+3+....+100的和
def sum(n):

    if n == 1:
        return n
    else:
        return sum(n-1)+n



#递归
# 不易于理解
# 速度慢
# 存储空间大


# 循环
# 易于理解
# 速度快
# 存储空间小
