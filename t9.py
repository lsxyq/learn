#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
executable_path=r'C:\Users\teacher\AppData\Local\Programs\Python\Python36\Scripts'
dcap = dict(DesiredCapabilities.PHANTOMJS)  # 设置userAgent
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")

obj = webdriver.PhantomJS(executable_path=executable_path, desired_capabilities=dcap)  # 加载网址
obj.get('http://wap.95533pc.com')  # 打开网址
obj.save_screenshot("1.png")  # 截图保存
obj.quit()