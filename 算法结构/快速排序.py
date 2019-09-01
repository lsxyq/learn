#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:YiJun
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right = right - 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left = left + 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quickSort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quickSort(li, left, mid - 1)
        quickSort(li, mid + 1, right)


li = [5,12,3,45,56,8,9,32]

quickSort(li,0,len(li)-1)
print(li)