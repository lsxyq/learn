#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import json
import sys
from contextlib import closing

import requests
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class douyin_spider(object):
    """docstring for douyin_spider"""

    def __init__(self, _signature, dytk):
        print('*******DouYin_spider******')
        self.init_spider(_signature, dytk)

    def init_spider(self, _signature, dytk):
        self.userid = self.get_user_id()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3325.146 Safari/537.36'}
        mobile_emulation = {'deviceName': 'iPhone X'}
        # chrome浏览器模拟iPhone X进行页面访问
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.browser = webdriver.Chrome(chrome_options=options)
        self._signature = _signature
        self.dytk = dytk
        self.url = 'https://www.amemv.com/aweme/v1/aweme/post/?user_id=%s&count=32&max_cursor=0&aid=1128&_signature=%s&dytk=%s' % (
            self.userid, self._signature, self.dytk)

    def handle_url(self):
        url_list = [self.url, ]
        self.browser.get(self.url)
        web_data = self.browser.page_source
        soup = BeautifulSoup(web_data, 'lxml')
        web_data = soup.pre.string
        web_data = json.loads(str(web_data))
        if web_data['status_code'] == 0:
            while web_data['has_more'] == 1:
                # 最大加载32条视频信息，has_more等于1表示还未全部加载完
                max_cursor = web_data['max_cursor']
                # 获取时间戳
                url = 'https://www.amemv.com/aweme/v1/aweme/post/?user_id=%s&count=32&max_cursor=%s&aid=1128&_signature=%s&dytk=%s' % (
                    self.userid, max_cursor, self._signature, self.dytk)
                url_list.append(url)
                self.browser.get(url)
                web_data = self.browser.page_source
                soup = BeautifulSoup(web_data, 'lxml')
                web_data = soup.pre.string
                web_data = json.loads(str(web_data))
            else:
                max_cursor = web_data['max_cursor']
                # 获取时间戳
                url = 'https://www.amemv.com/aweme/v1/aweme/post/?user_id=%s&count=32&max_cursor=%s&aid=1128&_signature=%s&dytk=%s' % (
                    self.userid, max_cursor, self._signature, self.dytk)
                url_list.append(url)
        else:
            url_list = []
        return url_list

    def get_download_url(self, url_list):
        download_url = []
        title_list = []
        if len(url_list) > 0:
            for url in url_list:
                self.browser.get(url)
                web_data = self.browser.page_source
                soup = BeautifulSoup(web_data, 'lxml')
                web_data = soup.pre.string
                web_data = json.loads(str(web_data))
                if web_data['status_code'] == 0:
                    for i in range(len(web_data['aweme_list'])):
                        download_url.append(web_data['aweme_list'][i]['video']['play_addr']['url_list'][0])
                        title_list.append(web_data['aweme_list'][i]['share_info']['share_desc'].encode('utf-8'))
            return download_url, title_list

    def videodownloader(self, url, title):
        size = 0
        path = title + '.mp4'
        with closing(requests.get(url, headers=self.headers, stream=True, verify=False)) as response:
            chunk_size = 1024
            content_size = int(response.headers['content-length'])
            if response.status_code == 200:
                print('%s is downloading...' % title)
                sys.stdout.write('[File Size]: %0.2f MB\n' % (content_size / chunk_size / 1024))
                with open(path, 'wb') as f:
                    for data in response.iter_content(chunk_size=chunk_size):
                        f.write(data)
                        size += len(data)
                        f.flush()
                        sys.stdout.write('[Progress]: %0.2f%%' % float(size / content_size * 100) + '\r')
                        sys.stdout.flush()
            else:
                print(response.status_code)

    def run(self):
        url = 'https://www.amemv.com/aweme/v1/aweme/post/?user_id=%s&count=32&max_cursor=0&aid=1128&_signature=%s&dytk=%s' % (
            self.userid, self._signature, self.dytk)
        url_list = self.handle_url()
        download_url, title_list = self.get_download_url(url_list)
        for i in range(len(download_url)):
            url = download_url[i]
            title = title_list[i]
            self.videodownloader(url, title)

    def get_user_id(self):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
        }
        user_id = input('请输入ID(例如108561773):')
        search_url = 'https://api.amemv.com/aweme/v1/discover/search/?cursor=0&keyword=%s&count=10&type=1&retry_type=no_retry&iid=17900846586&device_id=34692364855&ac=wifi&channel=xiaomi&aid=1128&app_name=aweme&version_code=162&version_name=1.6.2&device_platform=android&ssmix=a&device_type=MI+5&device_brand=Xiaomi&os_api=24&os_version=7.0&uuid=861945034132187&openudid=dc451556fc0eeadb&manifest_version_code=162&resolution=1080*1920&dpi=480&update_version_code=1622' % user_id
        req = requests.get(url=search_url, verify=False, headers=headers)
        html = json.loads(req.text)
        print(html)
        # print("获取到的html",html)
        aweme_count = html['user_list'][0]['user_info']['aweme_count']
        uid = html['user_list'][0]['user_info']['uid']
        nickname = html['user_list'][0]['user_info']['nickname']
        unique_id = html['user_list'][0]['user_info']['unique_id']
        return uid


if __name__ == '__main__':
    # 创建对象
    # 传入三个参数，user_id,_signature,dytk
    _signature = 'NHR3wRAdaWD6H.ETP-ZZFzR0d9'
    dytk = '59963f1120b67f52d6a715e173e21587'
    douyin_spider = douyin_spider(_signature, dytk)
    douyin_spider.run()
    print('******DouYin_spider@Awesome_Tang、******')
