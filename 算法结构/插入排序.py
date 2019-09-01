#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:YiJun
from timeit import Timer


# def insertSort(li):
#     for i in range(len(li)):
#         tmp = li[i]
#         j = i - 1
#         while j >= 0 and li[j] > tmp:
#             li[j + 1] = li[j]
#             j = j - 1
#
#         li[j + 1] = tmp
#         print(li)
#
#     return li
#
#
# li = [5, 12, 3, 45, 56, 8, 23, 14]
#
# li = insertSort(li)
#
# print(li)


def insertSort(li):
    for i in range(len(li)):
        index = i
        j=i+1
        while j<len(li):
            if li[index] > li[j]:
                index = j
            j+=1
        li[i],li[index] = li[index],li[i]
    return li

li = [5, 12, 3, 45, 56, 8, 23, 14]
li = insertSort(li)

print(li)