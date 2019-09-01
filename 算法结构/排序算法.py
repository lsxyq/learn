#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x 

li = [5, 12, 3, 45, 56, 8, 9, 32]
"""
冒泡排序思想：每一次循环比较当前值和后一个值的大小，把较大的值交换到后面
循环整个列表，每次冒出一个最大值，排到最后
"""
def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j+1]<li[j]:
                li[j+1],li[j] = li[j],li[j+1]
    return li


li = bubbleSort(li)
print(li)


"""
插入排序思想:假设当前循环的值是最小值，判断后续的值是否小于当前值，如果是，更新最小值的索引，一次比较完成后，交换位置
第一次循环：选出最小值，插入到第一个位置
第二次循环：选出第二大的值，插入到第二个位置
"""

#
# def insertSort(li):
#     for i in range(len(li)-1):
#         min =i
#         for j in range(i+1,len(li)):
#             if li[j]<li[min]:
#                 min = j
#         li[i],li[min] =li[min],li[i]
#     return li
#
#
#
#
# li = insertSort(li)
# print(li)


"""
选择排序思想:和插入排序相似，但是是直接交换位置，不更新索引
第一次循环：选出最小值，插入到第一个位置
第二次循环：选出第二大的值，插入到第二个位置
"""
# def selectSort(li):
#     for i in range(len(li)-1):
#         min =i
#         for j in range(i+1,len(li)):
#             if li[j]<li[min]:
#                 li[min],li[j] = li[j],li[min]
#     return li
#
#
# li = selectSort(li)
# print(li)