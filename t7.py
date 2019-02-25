#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from selenium import webdriver
from PIL import Image
import random
def screen_shot(url):
    driver = webdriver.PhantomJS()
    driver.maximize_window()
    name = get_file_name()
    driver.get(url)
    driver.save_screenshot(name)  # 截取全屏
    driver.quit()

def get_file_name(suffix='png'):
    str = get_random_string(20)
    return 'temp/{}.{}'.format(str,suffix)


def get_random_string(length=12,allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    return ''.join(random.choice(allowed_chars) for i in range(length))


if __name__ == '__main__':
    url_list = ['https://wxapp.ehafo.com/']
    for url in url_list:
        screen_shot(url)
