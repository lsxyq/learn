#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import sys


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PIL import Image
from pathlib import Path

import threading


class ScreenShotMerge():
    def __init__(self, page, over_flow_size):
        self.im_list = []
        self.page = page
        self.over_flow_size = over_flow_size
        self.get_path()

    def get_path(self):
        self.root_path = Path(__file__).parent.joinpath('temp')
        if not self.root_path.exists():
            self.root_path.mkdir(parents=True)
        self.save_path = self.root_path.joinpath('merge.png')

    def add_im(self, path):
        if len(self.im_list) == self.page:
            im = self.reedit_image(path)
        else:
            im = Image.open(path)

        im.save('{}/{}.png'.format(self.root_path, len(self.im_list) + 1))
        self.im_list.append(im)

    def get_new_size(self):
        max_width = 0
        total_height = 0
        # 计算合成后图片的宽度（以最宽的为准）和高度
        for img in self.im_list:
            width, height = img.size
            if width > max_width:
                max_width = width
            total_height += height
        return max_width, total_height

    def image_merge(self, ):
        if len(self.im_list) > 1:
            max_width, total_height = self.get_new_size()
            # 产生一张空白图
            new_img = Image.new('RGB', (max_width - 15, total_height), 255)
            x = y = 0
            for img in self.im_list:
                width, height = img.size
                new_img.paste(img, (x, y))
                y += height
            new_img.save(self.save_path)
            print('截图成功:', self.save_path)
        else:
            obj = self.im_list[0]
            width, height = obj.size
            left, top, right, bottom = 0, 0, width, height
            box = (left, top, right, bottom)
            region = obj.crop(box)
            new_img = Image.new('RGB', (width, height), 255)
            new_img.paste(region, box)
            new_img.save(self.save_path)
            print('截图成功:', self.save_path)

    def reedit_image(self, path):
        obj = Image.open(path)
        width, height = obj.size
        left, top, right, bottom = 0, height - self.over_flow_size, width, height
        box = (left, top, right, bottom)
        region = obj.crop(box)
        return region

class Worker(QThread):
    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        pass





class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('易哈佛')
        self.temp_height = 0

    def urlScreenShot(self, url):
        self.browser = QWebEngineView()
        self.browser.load(QUrl(url))
        self.browser.loadFinished.connect(self.check_page)
        box = (600,800)
        self.setGeometry(0,0,*box)
        self.setCentralWidget(self.browser)

    def check_page(self):
        p_width, p_height = self.get_page_size()
        self.page, self.over_flow_size = divmod(p_height, self.height())
        print(self.page, self.over_flow_size)
        if self.page == 0:
            self.page = 1
        self.ssm = ScreenShotMerge(self.page, self.over_flow_size)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.exe_command)
        self.timer.setInterval(400)
        self.timer.start()

    def screen_shot(self):
        screen = QApplication.primaryScreen()
        winid = self.browser.winId()
        pix = screen.grabWindow(int(winid))
        name = '{}/temp.png'.format(self.ssm.root_path)
        pix.save(name)
        self.ssm.add_im(name)

    def exe_command(self):
        if self.page > 0:
            self.screen_shot()
            self.run_js()

        elif self.page < 0:
            self.timer.stop()
            self.ssm.image_merge()
            self.close()

        elif self.over_flow_size > 0:
            self.screen_shot()
            self.run_js()
        self.page -= 1

    def run_js(self):
        script = """
            var scroll = function (dHeight) {
            var t = document.documentElement.scrollTop
            var h = document.documentElement.scrollHeight
            dHeight = dHeight || 0
            var current = t + dHeight
            if (current > h) {
                window.scrollTo(0, document.documentElement.clientHeight)
              } else {
                window.scrollTo(0, current)
              }
            }
        """
        # script = open('D:\learn\screenshot\loadsize.js', 'r', encoding='utf8').read()
        command = script + '\n scroll({})'.format(self.height())
        self.browser.page().runJavaScript(command)

    def close_window(self):
        self.close()

    def start_window(self):
        self.start()

    def information(self):
        desktop = QDesktopWidget()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()
        screen_count = desktop.screenCount()
        print("屏幕数量》》》",screen_count)

        return screen_width, screen_height

    def get_page_size(self):
        size = self.browser.page().contentsSize()
        self.set_height = size.height()
        self.set_width = size.width()
        return size.width(), size.height()

    def closeEvent(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    url = 'http://blog.sina.com.cn/lm/rank/focusbang//'
    app = QApplication(sys.argv)
    win = MainWindow()
    win.urlScreenShot(url)
    win.show()
    app.exit(app.exec_())







