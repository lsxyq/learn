#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x 

# 求最大数
# 给定一个由非负整数（数字不可拆开）组成的一个数列，重新排序至其可组成一个最大的数字
num_list = [10, 2, 909, 1000, 9676, 653]


def maxNum(num_list, flag=True):
    num_list.sort(key=lambda num: str(num)[0], reverse=True)
    tmp_list = [str(num) for num in num_list]

    while flag:
        for i in range(len(tmp_list) - 1):
            num1 = tmp_list[i]
            num2 = tmp_list[i + 1]
            if int(num1[0]) == int(num2[0]):
                print(tmp_list)
                if len(num1) >= len(num2):
                    if int(num1[:len(num2)]) <= int(num2):
                        tmp_list[i], tmp_list[i + 1] = num2, num1
                        break
                else:
                    if int(num1) < int(num2[:len(num1)]):
                        tmp_list[i], tmp_list[i + 1] = num2, num1
                        break
        else:
            flag = False
    return int(''.join(tmp_list))

maxNum = maxNum(num_list)
print(maxNum)
