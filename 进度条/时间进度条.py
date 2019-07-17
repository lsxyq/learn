#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import datetime
import time


class Tiao(object):
    def __init__(self):
        self.obj1 = datetime.timedelta(seconds=1)
        self.var = '%H:%M:%S'

    def add(self, var):
        a = datetime.datetime.strptime(var, self.var)
        b = a + self.obj1
        return str(b.strftime(self.var))

    def str_time(self, var3):
        a, b, c = [int(i) for i in var3.split(":")]
        a *= 3600
        b *= 60
        return a + b + c

    def yuan(self, var1, var2):
        """
        计算 百分比
        :param var1: 现在时间
        :param var2: 总时间
        """
        var1 = self.str_time(var1)
        var2 = self.str_time(var2)
        return '{:.2%}'.format(var1 / var2)


def zhanshi(var):
    a = Tiao()
    b = "00:00:00"
    while True:
        if var == b:
            break
        b = a.add(b)
        print('\r%s/%s (%s)' % (b, var, a.yuan(b, var)), end='')
        time.sleep(1)


zhanshi("00:25:37")
