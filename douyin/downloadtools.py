#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import json
import re
from contextlib import closing
from pathlib import Path

import requests
import urllib3

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
}


class Index(object):
    def __init__(self, number=50, decimal=2):
        """
        :param decimal: 你保留的保留小数位
        :param number: # 号的 个数
        """
        self.decimal = decimal
        self.number = number
        self.a = 100 / number  # 在百分比 为几时增加一个 # 号

    def __call__(self, now, total):
        # 1. 获取当前的百分比数
        percentage = self.percentage_number(now, total)

        # 2. 根据 现在百分比计算
        well_num = int(percentage / self.a)
        # print("well_num: ", well_num, percentage)

        # 3. 打印字符进度条
        progress_bar_num = self.progress_bar(well_num)

        # 4. 完成的进度条
        result = "\r%s %s" % (progress_bar_num, percentage)
        return result + '%'

    def percentage_number(self, now, total):
        """
        计算百分比
        :param now:  现在的数
        :param total:  总数
        :return: 百分
        """
        return round(now / total * 100, self.decimal)

    def progress_bar(self, num):
        """
        显示进度条位置
        :param num:  拼接的  “#” 号的
        :return: 返回的结果当前的进度条
        """
        # 1. "#" 号个数
        well_num = "#" * num

        # 2. 空格的个数
        space_num = " " * (self.number - num)

        return '[%s%s]' % (well_num, space_num)


index = Index()


class DouYinSpider(object):

    def __init__(self):
        pass

    def get_json_data(self, path):
        print(path)
        f = open(path, 'r', encoding='utf8')
        data = f.read()
        f.close()
        return json.loads(data)

    def parser_data(self, data: dict):
        aweme_list = []
        if not data.get('aweme_list'):return aweme_list
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
            self.stream_download(video_url, video_path, video_name)

    def stream_download(self, video_url, video_path, video_name):
        size = 0
        with closing(requests.get(video_url, headers=headers, verify=False, stream=True)) as response:
            try:
                content_size = int(response.headers['content-length'])
                with open(video_path, "wb") as file:
                    for data in response.iter_content(chunk_size=1024):
                        file.write(data)
                        size += len(data)
                        file.flush()
                        self.process_bar(size, content_size, video_name)
            except Exception as e:
                pass

    def process_bar(self, size, content_size, video_name):
        tips = '%s:%0.2f MB' % (video_name, content_size / 1024 / 1024)
        if size >= content_size:
            print(index(size, content_size) + '\t' + tips)
        else:
            print(index(size, content_size) + '\t' + tips, end='')

    def get_video_path(self, video_info):
        video_name = '{}.mp4'.format(video_info['share_title'])
        video_name = video_name.replace('?','')
        root = Path(__file__).parent.joinpath('videos').joinpath(video_info['nickname'])
        if not root.exists():
            root.mkdir(parents=True)
        video_path = root.joinpath(video_name).as_posix()
        return video_path, video_name

    def get_download_url(self, video_url, watermark_flag=None):
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            req = requests.get(video_url, verify=False, headers=headers).text
            download_url = re.findall(r'class="video-player" src="(.*?)"', req)[0]
            self.insert_download_url(download_url)
            return download_url
        except Exception as e:
            pass

    def remove_watermark(self, video_url):
        """
        获得无水印的视频播放地址
        Parameters:
            video_url: 带水印的视频地址
        Returns:
            无水印的视频下载地址
        """
        pass
        # self.driver.visit('http://douyin.iiilab.com/')
        # self.driver.find_by_tag('input').fill(video_url)
        # self.driver.find_by_xpath('//button[@class="btn btn-default"]').click()
        # html = self.driver.find_by_xpath('//div[@class="thumbnail"]/div/p')[0].html
        # bf = BeautifulSoup(html, 'lxml')
        # return bf.find('a').get('href')

    def insert_download_url(self, download_url):
        with open('C:\Projects\learn\douyin\download_url.txt', 'a+', encoding='utf8') as f:
            f.write(download_url + '\n')

    def run(self):
        dir = r"C:\Projects\learn\douyin\urls"
        for path in Path(dir).iterdir():
            data = self.get_json_data(path)
            aweme_list = self.parser_data(data)
            self.download_videos(aweme_list)


if __name__ == '__main__':
    DouYinSpider().run()
