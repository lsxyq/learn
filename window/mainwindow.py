# -*- coding: utf-8 -*-
import sys
import pydash
import json
import requests
from PyQt5.Qt import *
from window.loginwindow import Ui_login_window


class LoginWindow(QWidget, Ui_login_window):
    login_success = pyqtSignal()
    close_all = pyqtSignal()

    def __init__(self,):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('视频压缩')
        self.qrcode_image()
        self.init_timer()
        self.show()

    def init_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_login)
        self.timer.setInterval(500)
        self.timer.start()

    def qrcode_image(self):
        origin = 'https://c.ehafolive.com/api/users/wx/login/token/'
        response = requests.get(origin)
        data = self.parser_response(response)
        url = pydash.get(data, 'data.url')
        self.token = pydash.get(data, 'data.token')
        photo = QPixmap()
        r = requests.get(url)
        photo.loadFromData(r.content)
        self.qrocde_lable.setPixmap(photo)

    def check_login(self):
        origin = 'https://c.ehafolive.com/api/users/wx/login/check/?token={}'.format(self.token)
        response = requests.get(origin)
        if response.status_code == 200:
            self.timer.stop()
            self.login_success.emit()

    def parser_response(self, response):
        data = response.content.decode('utf8')
        return json.loads(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginWindow()
    sys.exit(app.exec_())
