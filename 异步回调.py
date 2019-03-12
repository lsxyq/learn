#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
# def callback(f):
#     def wrapper(obj, *args, **kwargs):
#         resp = f(obj, *args, **kwargs)
#         if kwargs.get('callback'):
#             mcallback = kwargs['callback']
#             if isinstance(callback, str) and hasattr(obj, mcallback):
#                 func = getattr(obj, mcallback)
#             elif hasattr(mcallback, 'im_self') and mcallback.im_self is obj:
#                 func = mcallback
#                 kwargs['callback'] = func.__name__
#             else:
#                 raise NotImplementedError("self.%s() not implemented!" % callback)
#         return func(resp)
#     return wrapper

#
# class BaseHandler(object):
#     """在self.crawl(url,callback=$func)时,通过装饰器callback即可实现回调,在self.crawl方法中,只需要专注于得到$func的参数即可"""
#     @callback
#     def crawl(self, url, **kwargs):
#         url = quote_chinese(_build_url(url.strip(), kwargs.get('params')))
#         return requests.get(url)
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
