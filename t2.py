#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from PIL import Image


class EditPhoto():
    def __init__(self, ):
        self.im_list = []
        self.save_path = 'temp/merge.png'

    def image_merge(self, ):
        print('开始合并图片')
        max_width = 0
        total_height = 0
        # 计算合成后图片的宽度（以最宽的为准）和高度
        for img in self.im_list:
            width, height = img.size
            if width > max_width:
                max_width = width
            total_height += height
        # 产生一张空白图
        new_img = Image.new('RGB', (max_width, total_height), 255)
        x = y = 0
        for img in self.im_list:
            width, height = img.size
            new_img.paste(img, (x, y))
            y += height
        new_img.save(self.save_path)
        print('截图成功:', self.save_path)


api = EditPhoto()

im1=Image.open('temp/1.png')
im2=Image.open('temp/2.png')
im3=Image.open('temp/3.png')

api.im_list.append(im1)
api.im_list.append(im2)
api.im_list.append(im3)
api.image_merge()