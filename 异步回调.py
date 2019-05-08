#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
def callback(func):
    def inner(obj, *args, **kwargs):
        res = func(obj, *args, **kwargs)
        if kwargs.get('callback'):
            callback = kwargs.get('callback')
            success = getattr(obj, callback)
            success()
        return success()

    return inner


class BaseHandler(object):
    @callback
    def reverse_str(self, str, *args, **kwargs):
        return str[::-1]

    def success(self):
        return 'success'


res= BaseHandler().reverse_str('abcdefgh', callback='success')
print(res)
