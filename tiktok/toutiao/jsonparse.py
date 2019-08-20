#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import json
import re
import time
from contextlib import closing
from pathlib import Path

import pydash
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tiktok.downloadtoos import index

videos = Path(r'C:\Projects\learn\tiktok\toutiao\videos')


def wrapper(func):
    def inner(*args, **kwargs):
        begin = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('页面加载用时\t{}s'.format(end - begin))
        return res

    return inner


class ChromeHeadLess(object):
    def __enter__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)
        self._link_handle = open('a.txt', 'w', encoding='utf8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        self._link_handle.close()

    def video_link(self, url):
        self.page_load(url)
        li1 = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))
        li2 = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'player__videoTitle')))

        video_link = li1.get_attribute('src')
        video_title = li2.text
        return video_link, video_title

    @wrapper
    def page_load(self, url):
        self.driver.get(url + "/")

    def json_parse(self, path):
        with open(path, 'r', encoding='utf8') as f:
            data = json.loads(f.read())
        return pydash.get(data, 'data')

    def write_video_link(self, *args):
        if not self._link_handle:
            self._link_handle = open('a.txt', 'a+', encoding='utf8')
        text = ';'.join(args)
        self._link_handle.write(text + '\n')

    def main(self):
        for path in Path(r'C:\Projects\learn\tiktok\toutiao\json').iterdir():
            print(path)
            data_list = self.json_parse(path)
            for data in data_list:
                article_genre = pydash.get(data, 'article_genre')
                video_title = pydash.get(data, 'title')
                if article_genre != 'video': continue
                item_id = pydash.get(data, 'item_id')
                video_path, video_title = self.format_data(item_id, video_title)
                # if Path(video_path).exists(): continue
                video_url = 'https://www.toutiao.com/i{}/'.format(item_id)
                video_link, _ = self.video_link(video_url)
                self.write_video_link(video_url, video_link, item_id, video_title)
                # self.stream_download(video_link, video_path, video_title)

    def format_data(self, item_id, video_title):
        video_title = video_title if video_title else item_id
        name = '{}.mp4'.format(video_title)
        video_path = videos.joinpath(name).as_posix()
        video_path = video_path.replace('?',"").replace('\n','')
        return video_path, name

    def stream_download(self, video_url, video_path, video_name):
        size = 0
        with closing(requests.get(video_url, stream=True)) as response:
            try:
                content_size = int(response.headers['content-length'])
                with open(video_path, "wb") as file:
                    for data in response.iter_content(chunk_size=2048):
                        file.write(data)
                        size += len(data)
                        file.flush()
                        self.progress_bar(size, content_size, video_name)
            except Exception as e:
                print(e)

    def progress_bar(self, size, content_size, video_name):
        tips = '%s:%0.2f MB' % (video_name, content_size / 1024 / 1024)
        if size >= content_size:
            print(index(size, content_size) + '\t' + tips)
        else:
            print(index(size, content_size) + '\t' + tips, end='')

    def open_urls(self):
        with open('a.txt', 'r', encoding='utf8') as f:
            for data in f.readlines():
                video_url, video_link, item_id, video_title = data.strip('\n').split(';', 3)
                video_path, name = self.format_data(item_id, video_title)
                if Path(video_path).exists(): continue
                self.stream_download(video_url, video_path, name)


if __name__ == '__main__':
    with ChromeHeadLess() as c:
        c.main()
