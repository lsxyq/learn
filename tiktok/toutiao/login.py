#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from verify.toutiaologin import SliderVerifyLogin


class TouTiaoLogin(SliderVerifyLogin):

    def __init__(self):
        super().__init__()
        self.url = 'https://www.toutiao.com/'

    def load_login_page(self):
        self.driver.find_element_by_class_name('login-button').click()
        self.driver.find_element_by_id('login-type-account').click()

    def insert_data(self):
        self.driver.find_element_by_id('user-name').send_keys('18358467482')
        self.driver.find_element_by_id('password').send_keys('359287416xyQ')
        self.driver.find_element_by_id('login-button').click()
        time.sleep(2)

    def get_picture_tag(self):
        bg_image_tag = self.wait.until(EC.presence_of_element_located((By.ID, 'validate-big')))
        bg_block_tag = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'validate-block')))
        return bg_image_tag, bg_block_tag

    def get_slider_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'drag-button')))

    def login_action(self):
        self.load_home_page()
        self.load_login_page()
        self.insert_data()
        self.verify_action()
        return self


if __name__ == '__main__':
    TouTiaoLogin().login_action()
