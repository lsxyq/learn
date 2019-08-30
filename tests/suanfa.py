#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
# 统计字符
# content='sdasdasjdopxcjopajscpoasdjfmcxznmckwjeioroiqsdydsuizxczmcmxjfkjvhxkvncxnvmzxcviudhs'
# ret =set(content)
# for i in ret:
#     count = content.count(i)
#     print('{}:{}'.format(i,count))

# #冒泡排序
def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[i]<arr[j]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr

print(bubbleSort([13,4,3,2,5,7,8,0,4,2,4,76,9]))

#选择排序
def buusort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr

print(buusort([13,4,3,2,5,7,8,0,4,2,4,76,9]))