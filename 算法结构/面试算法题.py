#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x


# 给定一个元素为整数的nums列表如nums = [0,-1,-3,4,-2,0,0,-7],
# 要求在不改变非零元素的顺序的情况下，把0都排到最后去,不能另外创建新的数组，基于原数组进行
# 列如nums = [0,-1,-3,4,-2,0,0,-7]==》nums=[-1，-3,4，-2，-7,0,0,0]
nums = [0,-1,-3,4,-2,0,0,-7,9,0,-11]

def zeroSort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] == 0 and nums[j + 1] != 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print(nums)
zeroSort(nums)


def moveZeroes(nums):
    i, j = 0, 0
    while i < len(nums):
        if nums[i] == 0:
            j = i + 1
            while j < len(nums):
                if nums[j] != 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
                j += 1
            if j >= len(nums):
                break
        i += 1
    print(nums)

moveZeroes(nums)




# print(zeroSort(nums))
# [-1, -3, 4, -2, -7, 0, 0, 0]

# 给定一个数组[-2,1,4,2,-1],请用算法求出连续子序数的最大值是多少？
# 例如
nums = [-2, 1, 4, 2, -1, 5]


def maxSum(nums):
    Thisnum, MaxNum = 0, 0
    for i in range(len(nums)):
        Thisnum = 0
        for j in range(i, len(nums)):
            Thisnum += nums[j]
            if Thisnum > MaxNum:
                MaxNum = Thisnum
    print(MaxNum)


def MAXSUBSEQSUM3(nums):
    ThisSum, MaxSum = 0, 0
    for i in range(len(nums)):
        ThisSum += nums[i]  # 向右累加
        if ThisSum > MaxSum:
            MaxSum = ThisSum  # 发现更大和则更新当前结果
        elif ThisSum < 0:  # 如果当前子列和为负数
            ThisSum = 0  # 则不可能使后面的部分和增大，则该抛弃掉
    print(MaxSum)



# 给两个有序数组,把数组nums2合并到nums1中，数组的长度分别是m,n,,假定nums的长度完全够合并nums2,仍然使nums1有序
nums1 = [1, 2, 5, 0, 0, 0]  # m =3
nums2 = [2, 3, 6]  # n= 3

def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:  # 若nums1中最后一个元素大于nums2中最后一个元素
            nums1[m + n - 1] = nums1[m - 1]  # 则扩展后的列表最后一个元素是俩元素中最大的
            m -= 1  # nums1中元素-1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:  # 若nums1完了，nums2还没完
        nums1[:n] = nums2[:n]  # 把剩下nums2加在最开始

# 实现一个range函数，参数接受的形式和Python中的参数一致
def diyRange(start, end=None, step=1):
    if not end:
        end = start
        start = 0
    while start < end:
        yield start
        start += step


# for i in diyRange(10):
#     print(i)


# 实现一个返回素数的生成器，用next调用会返回一个自然数中的质数

def prime():
    i = 1
    while True:
        i += 1
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


#
# for i in prime():
#     print(i)


# 给定一个嵌套的列表，定义一个函数，把列表中的所有的元素都依次取出，合并成一个列表返回
# def mergeList(nums):
#     for s in nums:
#         if isinstance(s,list):
#             for item in mergeList(s):
#                 yield item
#         else:
#             yield s

def mergeList(nums):
    for s in nums:
        if isinstance(s, list):
            yield from mergeList(s)
        else:
            yield s


numList = [1, 2, 3, [4, 5, 6, [7, 8, 9], 10, 11, 12], 13, 14, 15]


#
# for i in mergeList(numList):
#     print(i)


def parse_idx(self, nums, target):
    data = {}
    for idx, num in enumerate(nums):
        if num in data:
            return [idx, data[num]]
        else:
            data[target - num] = idx
    return data


# 求1到100的和
# from functools import reduce
#
# res = reduce(lambda x,y:x+y,range(101))
# print(res)


result = [(16, 78), (77, 67), (55, 98), (99, 59)]

# result.sort(key=lambda x:x[1])


# x= map(lambda x:list(x),result)
# x = filter(lambda x:x[1]<80,result)
# print(list(x))
