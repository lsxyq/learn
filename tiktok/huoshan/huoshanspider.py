#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import re
import shutil
from contextlib import closing
from pathlib import Path

import requests
import urllib3

from tiktok.downloadtoos import index
from tiktok.huoshan.huoshandatacleaning import DataCleaning
from tiktok.huoshan.huoshanpath import huoshan_path
from tiktok.huoshan.sharelinkjiexi import JieXiShareLink

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
}


class HuoShanSpider(object):

    def __init__(self, watermark=False):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.watermark = watermark

    def move_dir(self, path):
        shutil.move(path, huoshan_path.finish_dir)

    def download_videos(self, aweme_list):
        for video_info in aweme_list:
            video_path, video_name = self.get_video_path(video_info)
            if Path(video_path).exists(): continue
            video_url = self.get_download_url(video_info)
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
            return huoshan_path.get_watermark_path(video_info)
        return huoshan_path.get_video_path(video_info)

    def get_download_url(self, video_info):
        try:
            req = requests.get(video_info['share_url'], verify=False, headers=headers).text
            download_url = re.findall(r'class="player" data-src="(.*?)"', req)[0]
            if not self.watermark:
                download_url = self.remove_watermark(download_url)
            return download_url
        except Exception as e:
            print(e)

    def insert_download_url(self, download_url):
        with open(huoshan_path.download_url, 'a+', encoding='utf8') as f:
            f.write(download_url + '\n')

    def remove_watermark(self, download_url):
        video_id = JieXiShareLink.match_video_id(download_url)
        if not video_id: return
        wuma_url = "http://hotsoon.snssdk.com/hotsoon/item/video/_playback/?video_id={}".format(video_id)
        return wuma_url

    def run(self):
        dir = huoshan_path.urls_dir
        for path in Path(dir).iterdir():
            clean_data = DataCleaning(path.as_posix())
            data_list = clean_data.cleaned_data_list
            self.download_videos(data_list)
            self.move_dir(path.as_posix())


if __name__ == '__main__':
    HuoShanSpider().run()
