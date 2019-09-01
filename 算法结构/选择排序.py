#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:YiJun
def selectSort(li):
    for i in range(len(li)-1):
        min = i
        for j in range(i+1,len(li)):
            if li[min]>li[j]:
                li[min],li[j]=li[j],li[min]
    return li


li = [5,12,3,45,56,8,23,14]

li = selectSort(li)

print(li)

