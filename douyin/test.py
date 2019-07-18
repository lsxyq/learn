#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import random
from hashlib import md5

import requests

JS_PATH = "C:\Projects\learn\douyin\jiexi.js"
"""
			var r = generateRandom().toString();
			var parseTempStr = link + '@&^' + r
            var s = generateStr(parseTempStr)
			window.location.href='douyin2019.php?url=' + link + '&r=' + r + '&s=' + s;
"""
url = "http://v.douyin.com/BSxFLM/"


# url = "http://3g.gljlw.com/douyin2019.php?url="

# url = "https://lf.snssdk.com/shorten/?target=www.iesdouyin.com/share/video/6713471359558651144/?region=CN&mid=6713502787633974020&u_code=k2a0i7cf&titleType=title&belong=aweme"
# # url ='http://3g.gljlw.com/diy/douyin2019.php?url=http://v.douyin.com/BSxFLM/&r=9050539804539828&s=15aa893f5959260183dfe5f938a43406'
# r = requests.get(url)
# print(r.text,print(type(r.text)))
# with open(r'C:\\Projects\\learn\\douyin\\videos\\胡阿小小\\向暗恋的人表白的话，会发生什么?#暗恋.mp4','wb') as f:
#     f.write(r.content)
# jiexi_headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cache-control': 'max-age=0',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
#     'referer':"http://3g.gljlw.com/diy/douyin.php",
# }
#
#
# def get_jiexi_url(url):
#     link = url.replace('复制此链接，打开【抖音短视频】，直接观看视频！', '')
#     last_index = link.rindex("http://")
#     if last_index == -1:
#         c = link.rindex("https://")
#     else:
#         c = last_index
#     if c == -1: return
#     link = link[c:]
#     random_res = random.random()
#     r = str(random_res)[2:]
#     print(r)
#     parseTempStr = link + '@&^' + r
#     md = md5()
#     md.update(parseTempStr.encode('utf8'))
#     s = md.hexdigest()
#     url = 'http://3g.gljlw.com/diy/douyin2019.php?url=' + link + '&r=' + r + '&s=' + s
#     print(url)
#     return url
#
#
# url = get_jiexi_url(url)
# r = requests.get(url,headers=jiexi_headers)
# print(r.text)


import os

path = "C:\\Projects\\learn\\douyin\\videos\\刘亦菲吧官方\\#刘亦菲# 向天空大声的呼唤说声我爱你 ($≧▽≦)  仙粉宝宝们知道这是什么梗吗~.mp4"
with open(path,'w') as f:
    print(path)
