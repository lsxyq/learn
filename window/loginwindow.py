# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(800, 600)
        self.gridLayout = QtWidgets.QGridLayout(login_window)
        self.gridLayout.setObjectName("gridLayout")
        self.title_label = QtWidgets.QLabel(login_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMaximumSize(QtCore.QSize(200, 200))
        self.title_label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bernard MT Condensed")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setTextFormat(QtCore.Qt.AutoText)
        self.title_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.title_label.setObjectName("title_label")
        self.gridLayout.addWidget(self.title_label, 4, 0, 1, 1)
        self.qrocde_lable = QtWidgets.QLabel(login_window)
        self.qrocde_lable.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qrocde_lable.sizePolicy().hasHeightForWidth())
        self.qrocde_lable.setSizePolicy(sizePolicy)
        self.qrocde_lable.setMinimumSize(QtCore.QSize(20, 20))
        self.qrocde_lable.setMaximumSize(QtCore.QSize(200, 200))
        self.qrocde_lable.setBaseSize(QtCore.QSize(22, 20))
        self.qrocde_lable.setText("")
        self.qrocde_lable.setPixmap(QtGui.QPixmap("../wxlogin/qrcode.jpg"))
        self.qrocde_lable.setScaledContents(True)
        self.qrocde_lable.setObjectName("qrocde_lable")
        self.gridLayout.addWidget(self.qrocde_lable, 5, 0, 1, 1)
        self.tips_label = QtWidgets.QLabel(login_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tips_label.sizePolicy().hasHeightForWidth())
        self.tips_label.setSizePolicy(sizePolicy)
        self.tips_label.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(14)
        self.tips_label.setFont(font)
        self.tips_label.setTextFormat(QtCore.Qt.AutoText)
        self.tips_label.setScaledContents(True)
        self.tips_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.tips_label.setObjectName("tips_label")
        self.gridLayout.addWidget(self.tips_label, 6, 0, 1, 1)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "Form"))
        self.title_label.setText(_translate("login_window", "登陆视频压缩"))
        self.tips_label.setText(_translate("login_window", "使用微信扫一扫登陆"))

