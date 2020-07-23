# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PythonFirewall\GUIdesign\Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from connectSRX.ssh_firewall_SRX_threads import exportConfig_SRX


#hostIP_SRX = ['172.29.5.16', '172.21.200.161', '172.21.200.173', '172.21.200.165']
#hostName_SRX = ['DC7_eHR_DEV_FW1', 'DC5_PTST_EHR_FW_C01', 'DC5_STST_EHR_FW_C01', 'DC5_PTST_EHR_FW_E01']
hostIP_SRX = ['172.21.200.161', '172.21.200.163', '172.21.200.165']
hostName_SRX = ['DC5P_eHR_FW_C01', 'DC5P_eHR_FW_D01', 'DC5P_eHR_FW_E01']

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setWindowModality(QtCore.Qt.WindowModal)
        Login.resize(388, 300)
        Login.setMinimumSize(QtCore.QSize(388, 300))
        Login.setMaximumSize(QtCore.QSize(388, 300))
        Login.setToolTipDuration(-1)
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(0, 0, 401, 51))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.lineEditUserName = QtWidgets.QLineEdit(Login)
        self.lineEditUserName.setGeometry(QtCore.QRect(170, 90, 191, 21))
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.lineEditPassword = QtWidgets.QLineEdit(Login)
        self.lineEditPassword.setGeometry(QtCore.QRect(170, 130, 191, 21))
        self.lineEditPassword.setStatusTip("")
        self.lineEditPassword.setInputMask("")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setCursorPosition(0)
        self.lineEditPassword.setPlaceholderText("")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.labelUserName = QtWidgets.QLabel(Login)
        self.labelUserName.setGeometry(QtCore.QRect(60, 90, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelUserName.setFont(font)
        self.labelUserName.setTextFormat(QtCore.Qt.AutoText)
        self.labelUserName.setObjectName("labelUserName")
        self.labelPassword = QtWidgets.QLabel(Login)
        self.labelPassword.setGeometry(QtCore.QRect(60, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelPassword.setFont(font)
        self.labelPassword.setTextFormat(QtCore.Qt.AutoText)
        self.labelPassword.setObjectName("labelPassword")
        self.pushButtonLogin = QtWidgets.QPushButton(Login)
        self.pushButtonLogin.setGeometry(QtCore.QRect(20, 200, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setObjectName("pushButtonLogin")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Login Firewall Device"))
        self.labelUserName.setText(_translate("Login", "Username:"))
        self.labelPassword.setText(_translate("Login", "Password:"))
        self.pushButtonLogin.setText(_translate("Login", "Login"))


    def ConfigBackup(self):
       
        #print(self.lineEditUserName.text())
        #print(self.lineEditPassword.text())
        
        #exportConfig_SSG(hostIP_SSG, hostName_SSG, self.lineEditUserName.text(), self.lineEditPassword.text())
        exportConfig_SRX(hostIP_SRX, hostName_SRX,  self.lineEditUserName.text(), self.lineEditPassword.text())
        
