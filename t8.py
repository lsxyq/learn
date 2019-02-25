#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Firefox()
# driver.get('http://www.baidu.com')
#
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su').click()
# sleep(3)
# driver.get_screenshot_as_file('baidu.jpg')
# driver.quit()


import time
from selenium import webdriver
browser = webdriver.Firefox()
browser.set_window_size(1055, 800)
browser.get("https://www.jb51.net/")
browser.find_element_by_id("idClose").click()
time.sleep(5)
browser.save_screenshot("shot.png")
browser.quit()
