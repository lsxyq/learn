#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:YiJun
# def bubbleSort(li):
#     for i in range(len(li)-1):
#         for j in range(len(li)-1-i):
#             if li[j]>li[j+1]:
#                 li[j],li[j+1]=li[j+1],li[j]
#
#
#     return li
#
li = [5,12,3,45,56,8,9,32]




def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1]= li[j+1],li[j]

    return li


li = bubbleSort(li)
print(li)



