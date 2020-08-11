# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.setEnabled(True)
        LoginWindow.resize(373, 283)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userLbl = QtWidgets.QLabel(self.centralwidget)
        self.userLbl.setGeometry(QtCore.QRect(60, 40, 81, 41))
        self.userLbl.setObjectName("userLbl")
        self.passwordLbl = QtWidgets.QLabel(self.centralwidget)
        self.passwordLbl.setGeometry(QtCore.QRect(60, 110, 81, 41))
        self.passwordLbl.setObjectName("passwordLbl")
        self.userEdt = QtWidgets.QLineEdit(self.centralwidget)
        self.userEdt.setGeometry(QtCore.QRect(150, 50, 161, 31))
        self.userEdt.setObjectName("userEdt")
        self.passwordEdt = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdt.setGeometry(QtCore.QRect(150, 120, 161, 31))
        self.passwordEdt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdt.setObjectName("passwordEdt")
        self.studentRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.studentRadio.setGeometry(QtCore.QRect(70, 180, 115, 19))
        self.studentRadio.setChecked(True)
        self.studentRadio.setObjectName("studentRadio")
        self.adminRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.adminRadio.setGeometry(QtCore.QRect(180, 180, 115, 19))
        self.adminRadio.setObjectName("adminRadio")
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(130, 220, 93, 28))
        self.loginBtn.setObjectName("loginBtn")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "登录"))
        self.userLbl.setText(_translate("LoginWindow", "用户名"))
        self.passwordLbl.setText(_translate("LoginWindow", "密 码"))
        self.userEdt.setPlaceholderText(_translate("LoginWindow", "请输入用户名"))
        self.passwordEdt.setPlaceholderText(_translate("LoginWindow", "请输入密码"))
        self.studentRadio.setText(_translate("LoginWindow", "学生"))
        self.adminRadio.setText(_translate("LoginWindow", "管理员"))
        self.loginBtn.setText(_translate("LoginWindow", "登陆"))
