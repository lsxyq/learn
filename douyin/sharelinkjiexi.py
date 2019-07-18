#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import json
import random
import time
from hashlib import md5

import requests
from bs4 import BeautifulSoup

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
    'referer': "http://3g.gljlw.com/diy/douyin.php",
}


class JieXiShareLink(object):

    @classmethod
    def get_jiexi_url(cls, url):
        time.sleep(2)
        link = url.replace('复制此链接，打开【抖音短视频】，直接观看视频！', '')
        last_index = link.rindex("http://")
        if last_index == -1:
            c = link.rindex("https://")
        else:
            c = last_index
        if c == -1: return
        link = link[c:]
        random_res = random.random()
        r = str(random_res)[2:]
        parseTempStr = link + '@&^' + r
        md = md5()
        md.update(parseTempStr.encode('utf8'))
        s = md.hexdigest()
        url = 'http://3g.gljlw.com/diy/douyin2019.php?url=' + link + '&r=' + r + '&s=' + s
        return url

    @classmethod
    def get_video_share_link(cls, video_url):
        target = str(video_url).split("//", 1)[-1]
        url = "https://lf.snssdk.com/shorten/?target={}&belong=aweme".format(target)
        r = requests.get(url)
        return json.loads(r.text).get('data')

    @classmethod
    def remove_watermark(cls, share_url):
        """
        获得无水印的视频播放地址
        Parameters:
            share_url: 带水印的视频地址
        Returns:
            无水印的视频下载地址
        """
        video_share_url = cls.get_video_share_link(share_url)
        if not video_share_url: return
        cls.insert_share_url(video_share_url)
        jiexi_url = cls.get_jiexi_url(video_share_url)
        html = requests.get(jiexi_url, headers=headers).text
        bf = BeautifulSoup(html, 'lxml')
        wuma_url = bf.find('textarea').get_text()
        return wuma_url

    @classmethod
    def insert_share_url(cls, share_url):
        from douyin.pathtool import douyin_path
        with open(douyin_path.share_url, 'a+', encoding='utf8') as f:
            f.write(share_url + '\n')
