#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
s='hello alex alex say hello sb sb'
dic={}
words=s.split()
for word in words: #word='alex'
    dic.setdefault(word,s.count(word))
    print(dic)


# words_set=set(words)
# for word in words_set:
#     dic[word]=s.count(word)
#     print(dic)