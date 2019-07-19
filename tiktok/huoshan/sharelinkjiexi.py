#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import re
from urllib.parse import quote

import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
    'referer': "http://3g.gljlw.com/diy/douyin.php",
}
u = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"


class JieXiShareLink(object):

    @classmethod
    def match_url(cls, str):
        pattern = re.compile(u, re.S)
        res = pattern.findall(string=str)
        if res: return res[0]

    @classmethod
    def match_video_id(cls, str):
        res = re.findall("video_id=(.*?)&",str)
        if res: return res[0]

    @classmethod
    def remove_watermark(cls, video_info):
        """获得无水印的视频播放地址
        share_url: 带水印的视频地址
        video_share_link:抖音视频分享链接
        jiexi_url:分享链接解析网站请求地址
        wuma_url:无水印的视频地址
        """
        video_share_link = cls.get_video_share_link(video_info)
        if not video_share_link: return
        cls.insert_share_url(video_share_link)
        jiexi_url = cls.get_jiexi_url(video_share_link)
        return jiexi_url

    @classmethod
    def get_video_share_link(cls, video_info):
        """生成抖音视频分享链接
        :param share_url:
        :return:
        """
        share_url = video_info['share_url']
        video_id = video_info['video_id']
        format_share_url = "{}&schema_url=sslocal://item?id={}".format(share_url, video_id)
        encode_share_url = str(quote(format_share_url))
        url = "https://api.huoshan.com/hotsoon/share/link_command/?url_schema_url={}".format(encode_share_url)
        r = requests.get(url)
        share_link = cls.match_url(r.text)
        return share_link

    @classmethod
    def get_jiexi_url(cls, video_share_link):
        """
        由抖音分享链接计算抖音链接解析网站的加密参数，并生成请求地址
        :param url:
        :return:
        """
        pass

        return ""

    @classmethod
    def insert_share_url(cls, video_share_link):
        """将分享链接插入文件
        :param video_share_link:
        :return:
        """
        from tiktok.douyin.douyinpath import douyin_path
        with open(douyin_path.share_url, 'a+', encoding='utf8') as f:
            f.write(video_share_link + '\n')
