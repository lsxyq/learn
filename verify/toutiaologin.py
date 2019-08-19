#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x

import random
import time
from io import BytesIO

import cv2
import numpy as np
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CrackSlider():
    """
    通过浏览器截图，识别验证码中缺口位置，获取需要滑动距离，并模仿人类行为破解滑动验证码
    """

    def __init__(self):
        self.url = 'https://www.toutiao.com/'
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        self.bg_image = 'bg_image.png'
        self.bg_block = 'bg_block.png'
        self.zoom = 1

    def open(self):
        self.driver.get(self.url)

    def load_login_page(self):
        self.driver.find_element_by_class_name('login-button').click()
        self.driver.find_element_by_id('login-type-account').click()

    def insert_data(self):
        self.driver.find_element_by_id('user-name').send_keys('18358467482')
        self.driver.find_element_by_id('password').send_keys('359287416xyQ')
        self.driver.find_element_by_id('login-button').click()
        time.sleep(2)

    def get_pic(self):
        bg_image_tag = self.wait.until(EC.presence_of_element_located((By.ID, 'validate-big')))
        bg_block_tag = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'validate-block')))

        bg_image_link = bg_image_tag.get_attribute('src')
        bg_block_link = bg_block_tag.get_attribute('src')

        bg_image = Image.open(BytesIO(requests.get(bg_image_link).content))
        bg_block = Image.open(BytesIO(requests.get(bg_block_link).content))
        bg_image.save(self.bg_image)
        bg_block.save(self.bg_block)

        bg_image_obj = Image.open(self.bg_image)
        bg_block_obj = Image.open(self.bg_block)
        self.bg_image_size = bg_image_obj.size
        self.bg_block_size = bg_block_obj.size

        self.zoom = 268 / int(self.bg_image_size[0])

    def set_over_length(self, distance):
        over_length = 15
        bg_block_width = self.bg_block_size[0]
        bg_image_width = self.bg_image_size[0]
        while distance + over_length + bg_block_width > bg_image_width:
            over_length -= 1
        return over_length

    def get_back_tracks(self, distance):
        over_length = self.set_over_length(distance)
        distance += over_length
        back_tracks = []
        while over_length > 3:
            offset = random.choice((-1, -2, -3))
            back_tracks.append(offset)
            over_length += offset
        res = '-{}'.format(over_length)
        back_tracks.append(int(res))
        return distance, back_tracks

    def get_tracks(self, distance):
        v = 0  # 速度
        t = 0.2  # 时间
        forward_tracks = []
        current = 0
        distance, back_tracks = self.get_back_tracks(distance)
        mid = distance * 3 / 5  # 减速阀值
        while current < distance:
            if current < mid:
                a = 2  # 加速度为+2
            else:
                a = -3  # 加速度-3
            s = v * t + 0.5 * a * (t ** 2)  # 滑动距离
            v = v + a * t  # 当前速度
            current += s  # 当前位置
            forward_tracks.append(round(s))
        return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}

    def match(self):
        img_rgb = cv2.imread(self.bg_image)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        bg_block = cv2.imread(self.bg_block, 0)
        # w, h = bg_block.shape[::-1]
        # print(w, h)
        res = cv2.matchTemplate(img_gray, bg_block, cv2.TM_CCOEFF_NORMED)
        run = 1

        # 使用二分法查找阈值的精确值
        L = 0
        R = 1
        while run < 20:
            run += 1
            threshold = (R + L) / 2
            if threshold < 0:
                print('Error')
                return None
            x_position = np.where(res >= threshold)
            if len(x_position[1]) > 1:
                L += (R - L) / 2
            elif len(x_position[1]) == 1:
                print('X坐标为：%d' % x_position[1][0])
                break
            elif len(x_position[1]) < 1:
                R -= (R - L) / 2
        return x_position[1][0]

    def crack_slider(self, tracks):
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'drag-button')))
        ActionChains(self.driver).click_and_hold(slider).perform()

        for track in tracks['forward_tracks']:
            ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()

        time.sleep(0.2)
        for back_tracks in tracks['back_tracks']:
            ActionChains(self.driver).move_by_offset(xoffset=back_tracks, yoffset=0).perform()

        # ActionChains(self.driver).move_by_offset(xoffset=-4, yoffset=0).perform()
        # ActionChains(self.driver).move_by_offset(xoffset=4, yoffset=0).perform()
        time.sleep(0.2)

        ActionChains(self.driver).release().perform()

    def main(self):
        self.open()
        self.load_login_page()
        self.insert_data()
        cs.get_pic()
        distance = cs.match()
        tracks = cs.get_tracks((distance + 3) * cs.zoom)  # 对位移的缩放计算
        cs.crack_slider(tracks)


if __name__ == '__main__':
    cs = CrackSlider()
    cs.main()
