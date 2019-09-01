#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x 

import time
import pickle
import hashlib

cache = {}

def isExist(key):
    return key in cache


def getKey(func, args, kwargs):
    key = pickle.dumps((func.__name__, args, kwargs))
    return hashlib.md5(key).hexdigest()


def cacheData(duration=10):
    def wrapper(func):
        def inner(*args, **kwargs):
            key = getKey(func, args, kwargs)
            if isExist(key):
                now = time.time()
                if now - cache[key]['time'] < duration:
                    return cache[key]['value']
            value = func(*args, **kwargs)
            cache[key] = {'value': value, 'time': time.time()}
            return cache[key]['value']
        return inner
    return wrapper


@cacheData()
def sum(x, y):
    return x + y

sum(1,2)
sum(3,4)
sum(1,2)
sum(3,4)