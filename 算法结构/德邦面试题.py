#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x

# 1: 判断下列正确与否
# class A(object):
#     pass
#
# class B(A):
#     pass
#
# b = B()
#
# print(isinstance(b,B))
# print(isinstance(b,A))
# print(isinstance(b,object))
# print(isinstance(B,A))

# 2：map映射
# b= [22,12,33]
# b=sorted(b,key=lambda x:x)
# print(b)
# a = map(lambda x:x**3,[1,2,3])
# print(list(a))

# x,y = divmod(4,3)
# print(x,y)

# from __future__ import division
#
# print(1/2)
# print(1//2)


# a =1
# for i in range(1,5):
#     if i==2:
#         break
#

# print('a'<'b'<'c')
# print('a'>'b' or 'c')

# a = '123'
# b= '123'
#
# print(a is b)
# print(a == 123)


# x = [i*i for i in range(3)]
# print(x)
#
# a = 1
# try:
#     a +=1
# except:
#     a+=1
# else:
#     a+=1
# finally:
#     a+=1
#
# print(a)


# 如何解释下面的执行结果?
# print 1.2 - 1.0 == 0.2
# False
# 1.2-1.0 ==0.19999999999999996
# 浮点数无法精确表示

# t1 = 'gun\'s %s %%'%('gun')
# t1 = 'gun\'s %c %%'%(2)
# print(t1)

class Solution(object):
    def parse_idx(self, nums, target):
        data = {}
        for idx,num in enumerate(nums):
            if num in data:
                return [idx,data[num]]
            else:
                data[target-num] = idx
        return data

# s = [1,2,4]
# print(str(Solution().parse_idx(s, 3)))



# 某电商公司有一个文本文件如下，每一行包括客户ID，email地址，订单时间，订单总价值。
# 每个客户可能有多个订单。在shell下，如果快速找出复购次数最多的10个客户。


# customer_id|email_address|order_date|order_value|
# 126818|marr.tano@comcast.net|2009-04-13 21:06:20|299.0|
# 126819|greggh@tamconsulting.com|2009-04-13 21:19:15|349.0|
# 126820|brooer@aol.com|2009-04-13 21:25:51|249.0|
# 126821|tearry.elliott@comcast.net|2009-04-14 00:19:20|249.0|
# 126822|61brianl@comcast.net|2009-04-14 19:33:29|598.0|
# 126823|pauline7@q.com|2009-04-18 16:18:32|249.0|
# 126824|calheemin1@gmail.com|2009-04-23 22:17:37|299.0|
# 126825|cmbachinteres@yahoo.es|2009-04-24 17:11:18|299.0|
# 126826|garfielcdogilvie@clearchannel.com|2009-04-24 20:16:27|548.0|
# 126827|cwrigaht@pepsicenter.com|2009-04-24 21:17:13|249.0|
# 126828|rafaltm@yahoo.com|2009-04-25 02:23:58|249.0|
# 126829|gary@goowymedia.com|2009-04-27 17:55:28|648.0|
# 126830|jjpmaranto@yahoo.com|2009-04-28 19:15:06|548.0|
# 126831|manssbachmom@aol.com|2009-05-01 01:24:34|499.0|
# 126832|deborrah@deborahjonesstudio.com|2009-05-14 21:05:41|199.0|
# 126833|jonrmmarks@hotmail.com|2009-05-26 19:35:12|299.0|
# 126834|pdbowlles@gmail.com|2009-06-13 19:43:39|338.0|
# 126835|shodanlisa@yahoo.com|2009-06-15 19:34:18|249.0|
# 126828|rafal_tm@yahoo.com|2009-06-16 22:27:46|249.0|
# 126836|centa_cops@netscape.net|2009-06-16 22:43:12|249.0|
# 126837|frankscp1@gmail.com|2009-06-16 22:51:38|249.0|


# cut -d "|" -f 1 testdata| sort|uniq -c|sort -k1nr|head -10






# 大概估计一下上海由多少所幼儿园(不需要准确答案，大致量级靠谱即可)。写出思路，和每一步的计算。
# 1:上本地居1500w人口, 平均年龄 80岁. 人口老龄化,婚育率低 .3~6岁学前儿童 :
# 1500w * (4/80)* (3/5) = 50w
# 外来人口1000w, 大部分为务工人员,适龄儿童较少:
# 	1000w * (4/100) = 40w
# 共 有 90w /(40 个人* (3*3) 个班) = 2500所幼儿园


# 2:上海共有16区共有105个街道、107个镇和2个乡
# 107* 10  + 105*5 + 2*20  = 1800所

'''
Python的生成器式什么？迭代器是什么？
什么是生成器？
　　在Python中，这种一边循环一边计算的机制，称为生成器：generator
　　生成器是一个特殊的程序，可以被用作控制循环的迭代行为，python中生成器是迭代器的一种，
   使用yield返回值函数，每次调用yield会暂停，而可以使用next()函数和send()函数恢复生成器。
　　生成器类似于返回值为数组的一个函数，这个函数可以接受参数，可以被调用，但是，
不同于一般的函数会一次性返回包括了所有数值的数组，生成器一次只能产生一个值，这样消耗的内存数量将大大减小，而且允许调用函数可以很快的处理前几个返回值
因此生成器看起来像是一个函数，但是表现得却像是迭代器


那么什么迭代器呢？
    它是一个带状态的对象，他能在你调用next()方法的时候返回容器中的下一个值，
    任何实现了__iter__和__next__()（python2中实现next()）方法的对象都是迭
    代器，__iter__返回迭代器自身，__next__返回容器中的下一个值，如果容器中没有更多
    元素了，则抛出StopIteration异常，至于它们到底是如何实现的这并不重要。
    
    所以，迭代器就是实现了工厂模式的对象，它在你每次你询问要下一个值的时候给你返
    回。有很多关于迭代器的例子，比如itertools函数返回的都是迭代器对象。

'''






