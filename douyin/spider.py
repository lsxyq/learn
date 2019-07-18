#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import json
import re
import shutil
from contextlib import closing
from pathlib import Path

import requests
import urllib3

from douyin.pathtool import douyin_path
from douyin.progressbar import index
from douyin.sharelinkjiexi import JieXiShareLink

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
}


class DouYinSpider(object):

    def __init__(self, watermark=False):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.watermark = watermark

    def move_dir(self, path):
        shutil.move(path, douyin_path.finish_dir)

    def get_json_data(self, path):
        f = open(path, 'r', encoding='utf8')
        data = f.read()
        f.close()
        return json.loads(data)

    def parser_data(self, data: dict):
        aweme_list = []
        if not data.get('aweme_list'): return aweme_list
        for aweme_info in data.get('aweme_list'):
            video_info = {
                'share_title': self.get_video_title(aweme_info),
                'nickname': self.get_author_nickname(aweme_info),
                'share_url': self.get_share_url(aweme_info),
                'create_time': self.get_create_time(aweme_info),
            }
            aweme_list.append(video_info)
        return aweme_list

    def get_share_url(self, aweme_info):
        return aweme_info['share_url']

    def get_author_nickname(self, aweme_info):
        return aweme_info['author']['nickname']

    def get_video_title(self, aweme_info):
        return aweme_info['desc']

    def get_create_time(self, aweme_info):
        import arrow
        date = arrow.get(aweme_info['create_time']).format('YYYYMMDD')
        return date

    def download_videos(self, aweme_list):
        for video_info in aweme_list:
            video_path, video_name = self.get_video_path(video_info)
            if Path(video_path).exists(): continue
            video_url = self.get_download_url(video_info['share_url'])
            if not video_url: continue
            self.insert_download_url(video_url)
            self.stream_download(video_url, video_path, video_name)

    def stream_download(self, video_url, video_path, video_name):
        size = 0
        with closing(requests.get(video_url, headers=headers, verify=False, stream=True)) as response:
            try:
                content_size = int(response.headers['content-length'])
                with open(video_path, "wb") as file:
                    for data in response.iter_content(chunk_size=2048):
                        file.write(data)
                        size += len(data)
                        file.flush()
                        self.progress_bar(size, content_size, video_name)
            except Exception as e:
                pass

    def progress_bar(self, size, content_size, video_name):
        tips = '%s:%0.2f MB' % (video_name, content_size / 1024 / 1024)
        if size >= content_size:
            print(index(size, content_size) + '\t' + tips)
        else:
            print(index(size, content_size) + '\t' + tips, end='')

    def get_video_path(self, video_info):
        if self.watermark:
            return douyin_path.get_watermark_path(video_info)
        return douyin_path.get_video_path(video_info)

    def get_download_url(self, share_url):
        try:
            if not self.watermark:
                return JieXiShareLink.remove_watermark(share_url)
            req = requests.get(share_url, verify=False, headers=headers).text
            download_url = re.findall(r'class="video-player" src="(.*?)"', req)[0]
            return download_url
        except Exception as e:
            pass

    def insert_download_url(self, download_url):
        with open(douyin_path.download_url, 'a+', encoding='utf8') as f:
            f.write(download_url + '\n')

    def run(self):
        dir = douyin_path.urls_dir
        for path in Path(dir).iterdir():
            data = self.get_json_data(path)
            aweme_list = self.parser_data(data)
            self.download_videos(aweme_list)
            self.move_dir(path.as_posix())


if __name__ == '__main__':
    DouYinSpider().run()
