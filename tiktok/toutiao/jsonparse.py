#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def wrapper(func):
    def inner(*args, **kwargs):
        begin = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('加载页面{}s'.format(end - begin))
        return res

    return inner


class ChromeHeadLess(object):
    def __enter__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()

    @wrapper
    def video_link(self, url):
        self.page_load(url)
        video_link = self.driver.find_element_by_class_name('definition').get_attribute('url')
        return video_link

    @wrapper
    def page_load(self, url):
        self.driver.get(url + "/")


url = 'https://www.toutiao.com/c/user/55820860631/'
# url = 'https://www.ixigua.com/i6725181254221692942/'
with ChromeHeadLess() as chrome:
    html = chrome.driver.page_source
    print(html)


