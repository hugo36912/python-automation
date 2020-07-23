from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QWidget, QListWidgetItem, QLineEdit, QApplication  # ++
from shutil import copyfile
# from tkinter import *
# from tkinter.ttk import *
from tkinter import messagebox
from functools import partial
from connectDatabase.getZoneFromDB import getZoneInfoFromExcel
from connectDatabase.getGatewayFromDB import getGatewayInfoFromExcel
from connectDatabase.getApplicationFromDB import getAppInfoFromExcel
from connectDatabase.getGroupFromDB import getGroupInfoFromExcel
# from connectSRX.getPolicy_SRX import getPolicy_SRX
from connectSRX.getConfig_SRX import getConfig_SRX
from connectSRX.setConfig_SRX import setConfig_SRX
from connectSRX.clearConfig_SRX import clearConfig_SRX
from connectSRX.addObject_SRX import addObject_SRX
from connectSRX.getRuleFromConfig import getRuleFromConfig
from connectSRX.getSchedulerFromConfig import getSchedulerFromConfig
from connectSRX.getDefaultGroupFromConfig import getDefaultGroupFromConfig
from connectSRX.checkInput_FullName import checkInput_FullName
from connectSRX.checkInput_Combination import checkInput_Combination
# from firewallRule import Ui_FirewallRule
# from LoginPage import Login
from Login import Ui_Login
from pathlib import Path
from connectDatabase.getDataFromExcel import getDataFromExcel
from connectSRX.ssh_firewall_SRX import startExport
from connectSRX.ssh_firewall_SRX_threads import exportConfig_SRX
from revokeop import excum
# import tkinter as tk
import sys, os
import tkinter
import traceback
#developed by Hugo Chan All Right Reserved

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 690)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 300))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxInput = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxInput.setGeometry(QtCore.QRect(10, 0, 1171, 151))
        self.groupBoxInput.setTitle("")
        self.groupBoxInput.setObjectName("groupBoxInput")
        self.labelSource = QtWidgets.QLabel(self.groupBoxInput)
        self.labelSource.setGeometry(QtCore.QRect(50, 0, 51, 20))
        self.labelSource.setObjectName("labelSource")
        self.textEditSource = QtWidgets.QTextEdit(self.groupBoxInput)
        self.textEditSource.setGeometry(QtCore.QRect(50, 20, 251, 121))
        self.textEditSource.setObjectName("textEditSource")
        self.textEditDestination = QtWidgets.QTextEdit(self.groupBoxInput)
        self.textEditDestination.setGeometry(QtCore.QRect(310, 20, 251, 121))
        self.textEditDestination.setObjectName("textEditDestination")
        self.labelDestination = QtWidgets.QLabel(self.groupBoxInput)
        self.labelDestination.setGeometry(QtCore.QRect(310, 0, 81, 16))
        self.labelDestination.setObjectName("labelDestination")
        self.textEditApplication = QtWidgets.QTextEdit(self.groupBoxInput)
        self.textEditApplication.setGeometry(QtCore.QRect(570, 20, 121, 121))
        self.textEditApplication.setObjectName("textEditApplication")
        self.labelApplication = QtWidgets.QLabel(self.groupBoxInput)
        self.labelApplication.setGeometry(QtCore.QRect(570, 0, 61, 16))
        self.labelApplication.setObjectName("labelApplication")
        self.labelInputDescription = QtWidgets.QLabel(self.groupBoxInput)
        self.labelInputDescription.setGeometry(QtCore.QRect(700, 0, 81, 16))
        self.labelInputDescription.setObjectName("labelInputDescription")
        self.textEditDescription = QtWidgets.QTextEdit(self.groupBoxInput)
        self.textEditDescription.setGeometry(QtCore.QRect(700, 20, 161, 121))
        self.textEditDescription.setObjectName("textEditDescription")
        self.pushButtonCheck = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCheck.setGeometry(QtCore.QRect(10, 160, 1171, 41))
        self.pushButtonCheck.setObjectName("pushButtonCheck")
        self.groupDC1_C01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC1_C01.setGeometry(QtCore.QRect(0, 200, 301, 101))
        self.groupDC1_C01.setTitle("")
        self.groupDC1_C01.setObjectName("groupDC1_C01")
        self.textDC1_C01 = QtWidgets.QTextBrowser(self.groupDC1_C01)
        self.textDC1_C01.setGeometry(QtCore.QRect(10, 20, 281, 71))
        self.textDC1_C01.setObjectName("textDC1_C01")
        self.groupDC1_D01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC1_D01.setGeometry(QtCore.QRect(0, 300, 301, 91))
        self.groupDC1_D01.setTitle("")
        self.groupDC1_D01.setObjectName("groupDC1_D01")
        self.textDC1_D01 = QtWidgets.QTextBrowser(self.groupDC1_D01)
        self.textDC1_D01.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.textDC1_D01.setObjectName("textDC1_D01")
        self.groupDC1_E01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC1_E01.setGeometry(QtCore.QRect(0, 390, 301, 91))
        self.groupDC1_E01.setTitle("")
        self.groupDC1_E01.setObjectName("groupDC1_E01")
        self.textDC1_E01 = QtWidgets.QTextBrowser(self.groupDC1_E01)
        self.textDC1_E01.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.textDC1_E01.setObjectName("textDC1_E01")
        self.groupDC1_F01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC1_F01.setGeometry(QtCore.QRect(0, 480, 301, 91))
        self.groupDC1_F01.setTitle("")
        self.groupDC1_F01.setObjectName("groupDC1_F01")
        self.textDC1_F01 = QtWidgets.QTextBrowser(self.groupDC1_F01)
        self.textDC1_F01.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.textDC1_F01.setObjectName("textDC1_F01")
        self.groupDC2_C01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC2_C01.setGeometry(QtCore.QRect(300, 200, 301, 101))
        self.groupDC2_C01.setTitle("")
        self.groupDC2_C01.setObjectName("groupDC2_C01")
        self.textDC2_C01 = QtWidgets.QTextBrowser(self.groupDC2_C01)
        self.textDC2_C01.setGeometry(QtCore.QRect(10, 20, 281, 71))
        self.textDC2_C01.setObjectName("textDC2_C01")
        self.groupDC2_D01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC2_D01.setGeometry(QtCore.QRect(300, 300, 301, 91))
        self.groupDC2_D01.setTitle("")
        self.groupDC2_D01.setObjectName("groupDC2_D01")
        self.textDC2_D01 = QtWidgets.QTextBrowser(self.groupDC2_D01)
        self.textDC2_D01.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.textDC2_D01.setObjectName("textDC2_D01")
        self.groupDC2_E01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC2_E01.setGeometry(QtCore.QRect(300, 390, 301, 91))
        self.groupDC2_E01.setTitle("")
        self.groupDC2_E01.setObjectName("groupDC2_E01")
        self.textDC2_E01 = QtWidgets.QTextBrowser(self.groupDC2_E01)
        self.textDC2_E01.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.textDC2_E01.setObjectName("textDC2_E01")
        self.groupDC2_F01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC2_F01.setGeometry(QtCore.QRect(300, 480, 301, 91))
        self.groupDC2_F01.setTitle("")
        self.groupDC2_F01.setObjectName("groupDC2_F01")
        self.textDC2_F01 = QtWidgets.QTextBrowser(self.groupDC2_F01)
        self.textDC2_F01.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.textDC2_F01.setObjectName("textDC2_F01")
        self.groupDC7_E01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC7_E01.setGeometry(QtCore.QRect(900, 390, 301, 91))
        self.groupDC7_E01.setTitle("")
        self.groupDC7_E01.setObjectName("groupDC7_E01")
        self.textDC7_E01 = QtWidgets.QTextBrowser(self.groupDC7_E01)
        self.textDC7_E01.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.textDC7_E01.setObjectName("textDC7_E01")
        self.groupDC6_C01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC6_C01.setGeometry(QtCore.QRect(600, 200, 301, 101))
        self.groupDC6_C01.setTitle("")
        self.groupDC6_C01.setObjectName("groupDC6_C01")
        self.textDC6_C01 = QtWidgets.QTextBrowser(self.groupDC6_C01)
        self.textDC6_C01.setGeometry(QtCore.QRect(10, 20, 281, 71))
        self.textDC6_C01.setObjectName("textDC6_C01")
        self.groupDC7_C01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC7_C01.setGeometry(QtCore.QRect(900, 200, 301, 101))
        self.groupDC7_C01.setTitle("")
        self.groupDC7_C01.setObjectName("groupDC7_C01")
        self.textDC7_C01 = QtWidgets.QTextBrowser(self.groupDC7_C01)
        self.textDC7_C01.setGeometry(QtCore.QRect(10, 20, 281, 71))
        self.textDC7_C01.setObjectName("textDC7_C01")
        self.groupDC7_D01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC7_D01.setGeometry(QtCore.QRect(900, 300, 301, 91))
        self.groupDC7_D01.setTitle("")
        self.groupDC7_D01.setObjectName("groupDC7_D01")
        self.textDC7_D01 = QtWidgets.QTextBrowser(self.groupDC7_D01)
        self.textDC7_D01.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.textDC7_D01.setObjectName("textDC7_D01")
        self.groupDC6_D01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC6_D01.setGeometry(QtCore.QRect(600, 300, 301, 91))
        self.groupDC6_D01.setTitle("")
        self.groupDC6_D01.setObjectName("groupDC6_D01")
        self.textDC6_D01 = QtWidgets.QTextBrowser(self.groupDC6_D01)
        self.textDC6_D01.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.textDC6_D01.setObjectName("textDC6_D01")
        self.groupDC6_E01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC6_E01.setGeometry(QtCore.QRect(600, 390, 301, 91))
        self.groupDC6_E01.setTitle("")
        self.groupDC6_E01.setObjectName("groupDC6_E01")
        self.textDC6_E01 = QtWidgets.QTextBrowser(self.groupDC6_E01)
        self.textDC6_E01.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.textDC6_E01.setObjectName("textDC6_E01")
        self.groupDC7_F01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC7_F01.setGeometry(QtCore.QRect(900, 480, 301, 91))
        self.groupDC7_F01.setTitle("")
        self.groupDC7_F01.setObjectName("groupDC7_F01")
        self.textDC7_F01 = QtWidgets.QTextBrowser(self.groupDC7_F01)
        self.textDC7_F01.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.textDC7_F01.setObjectName("textDC7_F01")
        self.groupDC6_F01 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDC6_F01.setGeometry(QtCore.QRect(600, 480, 301, 91))
        self.groupDC6_F01.setTitle("")
        self.groupDC6_F01.setObjectName("groupDC6_F01")
        self.textDC6_F01 = QtWidgets.QTextBrowser(self.groupDC6_F01)
        self.textDC6_F01.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.textDC6_F01.setObjectName("textDC6_F01")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButtonAddPolicy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddPolicy.setGeometry(QtCore.QRect(10, 580, 361, 61))
        self.pushButtonAddPolicy.setObjectName("pushButtonAddPolicy")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Revoke Function"))
        self.labelSource.setText(_translate("MainWindow", "Source IP"))
        self.labelDestination.setText(_translate("MainWindow", "Destinaion IP"))
        self.labelApplication.setText(_translate("MainWindow", "Application"))
        self.labelInputDescription.setText(_translate("MainWindow", "Description"))
        self.pushButtonCheck.setWhatsThis(_translate("MainWindow","<html><head/><body><p><span style=\" font-weight:600;\">Check</span></p></body></html>"))
        self.pushButtonCheck.setText(_translate("MainWindow", "Revoke"))
        self.pushButtonAddPolicy.setText(_translate("MainWindow", "Add policy to tmp config "))

    def revoke(self):
        try:
            self.textDC1_C01.setText("")
            self.textDC1_D01.setText("")
            self.textDC1_E01.setText("")
            self.textDC1_F01.setText("")
            self.textDC2_C01.setText("")
            self.textDC2_D01.setText("")
            self.textDC2_E01.setText("")
            self.textDC2_F01.setText("")
            self.textDC6_C01.setText("")
            self.textDC6_D01.setText("")
            self.textDC6_E01.setText("")
            self.textDC6_F01.setText("")
            self.textDC7_C01.setText("")
            self.textDC7_D01.setText("")
            self.textDC7_E01.setText("")
            self.textDC7_F01.setText("")
            self.CommandAdd_DC1_C01 = []
            self.CommandAdd_DC1_D01 = []
            self.CommandAdd_DC1_E01 = []
            self.CommandAdd_DC1_F01 = []
            self.CommandAdd_DC2_C01 = []
            self.CommandAdd_DC2_D01 = []
            self.CommandAdd_DC2_E01 = []
            self.CommandAdd_DC2_F01 = []
            self.CommandAdd_DC6_C01 = []
            self.CommandAdd_DC6_D01 = []
            self.CommandAdd_DC6_E01 = []
            self.CommandAdd_DC6_F01 = []
            self.CommandAdd_DC7_C01 = []
            self.CommandAdd_DC7_D01 = []
            self.CommandAdd_DC7_E01 = []
            self.CommandAdd_DC7_F01 = []

            inputSource = []
            inputSource = ' '.join(self.textEditSource.toPlainText().split('\n')).split()
            inputDestination = []
            inputDestination = ' '.join(self.textEditDestination.toPlainText().split('\n')).split()
            inputApplication = []
            inputApplication = ' '.join(self.textEditApplication.toPlainText().split('\n')).split()
            strTCP = "_TCP"  # default TCP
            for idx, item in enumerate(inputApplication):
                if inputApplication[idx].isdigit():
                    inputApplication[idx] = inputApplication[idx] + strTCP
            inputSource.sort()
            inputDestination.sort()
            inputApplication.sort()
            print(inputSource)
            print(inputDestination)
            print(inputApplication)
            InputSourceZoneInfo = []
            InputSourceGroupInfo = []
            InputDestinationZoneInfo = []
            InputDestinationGroupInfo = []
            InputAppInfo = []
            excelDeviceFull = []
            excelDeviceShort = []
            tempGroupInfo = []
            startCheck = 0
            startPoint = 4
            i = 0
            for rowData in getDataFromExcel.startGetData("Path"):
                excelDeviceFull.append(rowData[1])
                excelDeviceShort.append(rowData[3])

            fw_gateway_get_data = getDataFromExcel.startGetData("gateway_lookup")
            print("gateway lookup completed")

            fw_app_get_data = getDataFromExcel.startGetData("app_lookup")
            print("app lookup completed")

            fw_zone_get_data = getDataFromExcel.startGetData("hcp_zone_lookup")
            print("zone completed")


            for source in inputSource:
                tempGroupInfo = getGroupInfoFromExcel.startGetGroupInfo(source)
                if not tempGroupInfo:
                    msg = QMessageBox()
                    msg.setWindowTitle("Input Source not found")
                    msg.setText("Input Source " + source + " not found in Excel")
                    msg.exec_()
                    return 1


            for dest in inputDestination:
                tempGroupInfo = getGroupInfoFromExcel.startGetGroupInfo(dest)
                if tempGroupInfo == []:
                    msg = QMessageBox()
                    msg.setWindowTitle("Input destination not found")
                    msg.setText("Input destination " + dest + " not found in Excel")
                    msg.exec_()
                    return 1


            for app in inputApplication:
                tempInputAppInfo = getAppInfoFromExcel.startGetAppInfo(app,fw_app_get_data)  ## whole row date from excel
                if tempInputAppInfo == None:
                    msg = QMessageBox()
                    msg.setWindowTitle("Input Application not found")
                    msg.setText("Input Application " + app + " not found in Excel")
                    msg.exec_()
                    return 1
                InputAppInfo.append(tempInputAppInfo)
            # developed by Hugo Chan All Right Reserved
            cp=[]
            l=0
            total=len(inputSource)*len(inputDestination)*len(inputApplication)
            i=0
            while i<len(inputSource):
                j = 0
                while j<len(inputDestination):
                    k=0
                    while k<len(inputApplication):
                        jp=[]
                        jp.append(inputSource[i])
                        jp.append(inputDestination[j])
                        jp.append(inputApplication[k])
                        cp.append(jp)
                        k+=1
                        l+=1
                    j=j+1
                i+=1
            for ccp in cp:
                print(ccp)
            config_list = [[] for i in range(16)]
            all_config_list = []
            for startCount in range(0, 16):
                config_list[startCount] = getConfig_SRX.startGetConfig(excelDeviceFull[startPoint + startCount],
                                                                       excelDeviceFull)
                all_config_list.append(config_list[startCount])

            print("Get config completed")

            config_dict_list = [[] for i in range(16)]
            for startCount in range(0, 16):
                config_dict_list[startCount] = getRuleFromConfig.getConfig(excelDeviceFull[startPoint + startCount],
                                                                           excelDeviceFull)
            self.policyCommandAdd_list = [[] for i in range(16)]
            self.objectAdd = [[] for i in range(16)]

            self.policyCommandAdd_list[0] = ""
            self.policyCommandAdd_list[1] = ""
            self.policyCommandAdd_list[2] = ""
            self.policyCommandAdd_list[3] = ""
            self.policyCommandAdd_list[4] = ""
            self.policyCommandAdd_list[5] = ""
            self.policyCommandAdd_list[6] = ""
            self.policyCommandAdd_list[7] = ""
            self.policyCommandAdd_list[8] = ""
            self.policyCommandAdd_list[9] = ""
            self.policyCommandAdd_list[10] = ""
            self.policyCommandAdd_list[11] = ""
            self.policyCommandAdd_list[12] = ""
            self.policyCommandAdd_list[13] = ""
            self.policyCommandAdd_list[14] = ""
            self.policyCommandAdd_list[15] = ""
            cp1=[]
            cp2 = []
            cp3 = []
            policy=[]

            for i in range(0, 16):
              dicmic={}
              cc=[]
              for key in config_dict_list[i].keys():
                for policyy in config_dict_list[i][key]:
                    policy = policyy.split()
                    for jj in cp:
                        if 'source-address' in policy:
                            if '.' in policy[11]:
                                s = policy[11].split('-')
                                cp1.append(policy[8])
                        if 'destination-address' in policy:
                            if '.' in policy[11]:
                                d = policy[11].split('-')
                                cp2.append(policy[8])
                        if 'application' in policy:
                            cp3.append(policy[11])

              set1 = set(cp1).intersection(set(cp2))
              jc = set1.intersection(set(cp3))
              if jc:
                  for ij in jc :
                     ea=(excum(ij,config_dict_list[i],cp,inputSource,inputDestination,inputApplication,dicmic))
                     cc.extend(ea)
              self.policyCommandAdd_list[i]=cc
              jc = ''
              cp1 = []
              cp2 = []
              cp3 = []
              policy=[]

            # developed by Hugo Chan All Right Reserved
            print("finished")
            self.groupDC1_C01.setTitle(excelDeviceShort[4])
            self.groupDC1_D01.setTitle(excelDeviceShort[5])
            self.groupDC1_E01.setTitle(excelDeviceShort[6])
            self.groupDC1_F01.setTitle(excelDeviceShort[7])
            self.groupDC2_C01.setTitle(excelDeviceShort[8])
            self.groupDC2_D01.setTitle(excelDeviceShort[9])
            self.groupDC2_E01.setTitle(excelDeviceShort[10])
            self.groupDC2_F01.setTitle(excelDeviceShort[11])
            self.groupDC6_C01.setTitle(excelDeviceShort[12])
            self.groupDC6_D01.setTitle(excelDeviceShort[13])
            self.groupDC6_E01.setTitle(excelDeviceShort[14])
            self.groupDC6_F01.setTitle(excelDeviceShort[15])
            self.groupDC7_C01.setTitle(excelDeviceShort[16])
            self.groupDC7_D01.setTitle(excelDeviceShort[17])
            self.groupDC7_E01.setTitle(excelDeviceShort[18])
            self.groupDC7_F01.setTitle(excelDeviceShort[19])
            print("############" + excelDeviceShort[startPoint + 0] + "############")
            self.textDC1_C01.setText("")

            for readline in self.policyCommandAdd_list[0]:
                print(readline)
                self.groupDC1_C01.setTitle(excelDeviceShort[startPoint + 0])
                # self.textBrowser1.setText("testPri-C01 ")
                self.textDC1_C01.append(readline)
            for readline in self.objectAdd[0]:
                print(readline)

                self.textDC1_C01.append(readline)

            print("############" + excelDeviceShort[startPoint + 4] + "############")
            self.textDC2_C01.setText("")
            for readline in self.policyCommandAdd_list[4]:
                print(readline)
                self.groupDC2_C01.setTitle(excelDeviceShort[startPoint + 4])
                self.textDC2_C01.append(readline)
            for readline in self.objectAdd[4]:
                print(readline)
                self.textDC2_C01.append(readline)

            print("############" + excelDeviceShort[startPoint + 1] + "############")
            self.textDC1_D01.setText("")
            for readline in self.policyCommandAdd_list[1]:
                print(readline)
                self.groupDC1_D01.setTitle(excelDeviceShort[startPoint + 1])
                self.textDC1_D01.append(readline)
            for readline in self.objectAdd[1]:
                print(readline)
                self.textDC1_D01.append(readline)

            print("############" + excelDeviceShort[startPoint + 5] + "############")
            self.textDC2_D01.setText("")
            for readline in self.policyCommandAdd_list[5]:
                print(readline)
                self.groupDC2_D01.setTitle(excelDeviceShort[startPoint + 5])
                self.textDC2_D01.append(readline)
            for readline in self.objectAdd[5]:
                print(readline)
                self.textDC2_D01.append(readline)

            print("############" + excelDeviceShort[startPoint + 2] + "############")
            self.textDC1_E01.setText("")
            for readline in self.policyCommandAdd_list[2]:
                print(readline)
                self.groupDC1_E01.setTitle(excelDeviceShort[startPoint + 2])
                self.textDC1_E01.append(readline)
            for readline in self.objectAdd[2]:
                print(readline)
                self.textDC1_E01.append(readline)

            print("############" + excelDeviceShort[startPoint + 6] + "############")
            self.textDC2_E01.setText("")
            for readline in self.policyCommandAdd_list[6]:
                print(readline)
                self.groupDC2_E01.setTitle(excelDeviceShort[startPoint + 6])
                self.textDC2_E01.append(readline)
            for readline in self.objectAdd[6]:
                print(readline)
                self.textDC2_E01.append(readline)

            print("############" + excelDeviceShort[startPoint + 3] + "############")
            self.textDC1_F01.setText("")
            for readline in self.policyCommandAdd_list[3]:
                print(readline)
                self.groupDC1_F01.setTitle(excelDeviceShort[startPoint + 3])
                self.textDC1_F01.append(readline)
            for readline in self.objectAdd[3]:
                print(readline)
                self.textDC1_F01.append(readline)

            print("############" + excelDeviceShort[startPoint + 7] + "############")
            for readline in self.policyCommandAdd_list[7]:
                print(readline)
                self.groupDC2_F01.setTitle(excelDeviceShort[startPoint + 7])
                self.textDC2_F01.append(readline)
            for readline in self.objectAdd[7]:
                print(readline)
                self.textDC2_F01.append(readline)
            startPoint=12
            print("############" + excelDeviceShort[startPoint + 0] + "############")
            self.textDC6_C01.setText("")
            # print("policyCommandAdd_list[0]=",self.policyCommandAdd_list[0])
            # print("objectAdd[0]=",self.objectAdd[0])

            for readline in self.policyCommandAdd_list[8]:
                print(readline)
                self.groupDC6_C01.setTitle(excelDeviceShort[startPoint + 0])
                # self.textBrowser1.setText("testPri-C01 ")
                self.textDC6_C01.append(readline)
            for readline in self.objectAdd[8]:
                print(readline)
                # self.textBrowser1.setText("testPri-C01 ")
                # self.textBrowser1.append(','.join(readline))
                self.textDC6_C01.append(readline)

            print("############" + excelDeviceShort[startPoint + 4] + "############")
            self.textDC7_C01.setText("")
            for readline in self.policyCommandAdd_list[12]:
                print(readline)
                self.groupDC7_C01.setTitle(excelDeviceShort[startPoint + 4])
                # self.textBrowser2.append(','.join(readline))
                self.textDC7_C01.append(readline)
            for readline in self.objectAdd[12]:
                print(readline)
                # self.textBrowser2.append(','.join(readline))
                self.textDC7_C01.append(readline)

            print("############" + excelDeviceShort[startPoint + 1] + "############")
            self.textDC6_D01.setText("")
            for readline in self.policyCommandAdd_list[9]:
                print(readline)
                self.groupDC6_D01.setTitle(excelDeviceShort[startPoint + 1])
                self.textDC6_D01.append(readline)
            for readline in self.objectAdd[9]:
                print(readline)
                self.textDC6_D01.append(readline)

            print("############" + excelDeviceShort[startPoint + 5] + "############")
            self.textDC7_D01.setText("")
            for readline in self.policyCommandAdd_list[13]:
                print(readline)
                self.groupDC7_D01.setTitle(excelDeviceShort[startPoint + 5])
                self.textDC7_D01.append(readline)
            for readline in self.objectAdd[13]:
                print(readline)
                self.textDC7_D01.append(readline)
            print("############" + excelDeviceShort[startPoint + 2] + "############")
            self.textDC6_E01.setText("")
            for readline in self.policyCommandAdd_list[10]:
                print(readline)
                self.groupDC6_E01.setTitle(excelDeviceShort[startPoint + 2])
                self.textDC6_E01.append(readline)
            for readline in self.objectAdd[10]:
                print(readline)
                self.textDC6_E01.append(readline)

            print("############" + excelDeviceShort[startPoint + 6] + "############")
            self.textDC7_E01.setText("")
            for readline in self.policyCommandAdd_list[14]:
                print(readline)
                self.groupDC7_E01.setTitle(excelDeviceShort[startPoint + 6])
                self.textDC7_E01.append(readline)
            for readline in self.objectAdd[14]:
                print(readline)
                self.textDC7_E01.append(readline)

            print("############" + excelDeviceShort[startPoint + 3] + "############")
            self.textDC6_F01.setText("")
            for readline in self.policyCommandAdd_list[11]:
                print(readline)
                self.groupDC6_F01.setTitle(excelDeviceShort[startPoint + 3])
                self.textDC6_F01.append(readline)
            for readline in self.objectAdd[11]:
                print(readline)
                self.textDC6_F01.append(readline)

            print("############" + excelDeviceShort[startPoint + 7] + "############")
            for readline in self.policyCommandAdd_list[15]:
                print(readline)
                self.groupDC7_F01.setTitle(excelDeviceShort[startPoint + 7])
                self.textDC7_F01.append(readline)
            for readline in self.objectAdd[15]:
                print(readline)
                self.textDC7_F01.append(readline)
            self.CommandAdd_DC1_C01.extend(self.policyCommandAdd_list[0])
            self.CommandAdd_DC1_D01.extend(self.policyCommandAdd_list[1])
            self.CommandAdd_DC1_E01.extend(self.policyCommandAdd_list[2])
            self.CommandAdd_DC1_F01.extend(self.policyCommandAdd_list[3])
            self.CommandAdd_DC1_C01.extend(self.objectAdd[0])
            self.CommandAdd_DC1_D01.extend(self.objectAdd[1])
            self.CommandAdd_DC1_E01.extend(self.objectAdd[2])
            self.CommandAdd_DC1_F01.extend(self.objectAdd[3])
            self.CommandAdd_DC2_C01.extend(self.policyCommandAdd_list[4])
            self.CommandAdd_DC2_D01.extend(self.policyCommandAdd_list[5])
            self.CommandAdd_DC2_E01.extend(self.policyCommandAdd_list[6])
            self.CommandAdd_DC2_F01.extend(self.policyCommandAdd_list[7])
            self.CommandAdd_DC2_C01.extend(self.objectAdd[4])
            self.CommandAdd_DC2_D01.extend(self.objectAdd[5])
            self.CommandAdd_DC2_E01.extend(self.objectAdd[6])
            self.CommandAdd_DC2_F01.extend(self.objectAdd[7])
            self.CommandAdd_DC6_C01.extend(self.policyCommandAdd_list[8])
            self.CommandAdd_DC6_D01.extend(self.policyCommandAdd_list[9])
            self.CommandAdd_DC6_E01.extend(self.policyCommandAdd_list[10])
            self.CommandAdd_DC6_F01.extend(self.policyCommandAdd_list[11])
            self.CommandAdd_DC6_C01.extend(self.objectAdd[8])
            self.CommandAdd_DC6_D01.extend(self.objectAdd[9])
            self.CommandAdd_DC6_E01.extend(self.objectAdd[10])
            self.CommandAdd_DC6_F01.extend(self.objectAdd[11])
            self.CommandAdd_DC7_C01.extend(self.policyCommandAdd_list[12])
            self.CommandAdd_DC7_D01.extend(self.policyCommandAdd_list[13])
            self.CommandAdd_DC7_E01.extend(self.policyCommandAdd_list[14])
            self.CommandAdd_DC7_F01.extend(self.policyCommandAdd_list[15])
            self.CommandAdd_DC7_C01.extend(self.objectAdd[12])
            self.CommandAdd_DC7_D01.extend(self.objectAdd[13])
            self.CommandAdd_DC7_E01.extend(self.objectAdd[14])
            self.CommandAdd_DC7_F01.extend(self.objectAdd[15])
        except:
            print("Exception")
            traceback.print_exc()
            return 1

    def addTmpConfig(self):

        excel_get_data = []
        excel_get_data = getDataFromExcel.startGetData("Path")

        excelDeviceFull = []

        for rowData in excel_get_data:
            excelDeviceFull.append(rowData[1])

        if self.CommandAdd_DC1_C01:
            setConfig_SRX.startSetConfig(excelDeviceFull[4], self.CommandAdd_DC1_C01, excelDeviceFull)
        if self.CommandAdd_DC1_D01:
            setConfig_SRX.startSetConfig(excelDeviceFull[5], self.CommandAdd_DC1_D01, excelDeviceFull)
        if self.CommandAdd_DC1_E01:
            setConfig_SRX.startSetConfig(excelDeviceFull[6], self.CommandAdd_DC1_E01, excelDeviceFull)
        if self.CommandAdd_DC1_F01:
            setConfig_SRX.startSetConfig(excelDeviceFull[7], self.CommandAdd_DC1_F01, excelDeviceFull)
        if self.CommandAdd_DC2_C01:
            setConfig_SRX.startSetConfig(excelDeviceFull[8], self.CommandAdd_DC2_C01, excelDeviceFull)
        if self.CommandAdd_DC2_D01:
            setConfig_SRX.startSetConfig(excelDeviceFull[9], self.CommandAdd_DC2_D01, excelDeviceFull)
        if self.CommandAdd_DC2_E01:
            setConfig_SRX.startSetConfig(excelDeviceFull[10], self.CommandAdd_DC2_E01, excelDeviceFull)
        if self.CommandAdd_DC2_F01:
            setConfig_SRX.startSetConfig(excelDeviceFull[11], self.CommandAdd_DC2_F01, excelDeviceFull)
        if self.CommandAdd_DC6_C01:
            setConfig_SRX.startSetConfig(excelDeviceFull[12], self.CommandAdd_DC6_C01, excelDeviceFull)
        if self.CommandAdd_DC6_D01:
            setConfig_SRX.startSetConfig(excelDeviceFull[13], self.CommandAdd_DC6_D01, excelDeviceFull)
        if self.CommandAdd_DC6_E01:
            setConfig_SRX.startSetConfig(excelDeviceFull[14], self.CommandAdd_DC6_E01, excelDeviceFull)
        if self.CommandAdd_DC6_F01:
            setConfig_SRX.startSetConfig(excelDeviceFull[15], self.CommandAdd_DC6_F01, excelDeviceFull)
        if self.CommandAdd_DC7_C01:
            setConfig_SRX.startSetConfig(excelDeviceFull[16], self.CommandAdd_DC7_C01, excelDeviceFull)
        if self.CommandAdd_DC7_D01:
            setConfig_SRX.startSetConfig(excelDeviceFull[17], self.CommandAdd_DC7_D01, excelDeviceFull)
        if self.CommandAdd_DC7_E01:
            setConfig_SRX.startSetConfig(excelDeviceFull[18], self.CommandAdd_DC7_E01, excelDeviceFull)
        if self.CommandAdd_DC7_F01:
            setConfig_SRX.startSetConfig(excelDeviceFull[19], self.CommandAdd_DC7_F01, excelDeviceFull)

        self.textDC6_C01.setText("")
        self.textDC6_D01.setText("")
        self.textDC6_E01.setText("")
        self.textDC6_F01.setText("")
        self.textDC7_C01.setText("")
        self.textDC7_D01.setText("")
        self.textDC7_E01.setText("")
        self.textDC7_F01.setText("")

        self.textDC1_C01.setText("")
        self.textDC1_D01.setText("")
        self.textDC1_E01.setText("")
        self.textDC1_F01.setText("")
        self.textDC2_C01.setText("")
        self.textDC2_D01.setText("")
        self.textDC2_E01.setText("")
        self.textDC2_F01.setText("")

        msg = QMessageBox()
        msg.setWindowTitle("Config updated")
        msg.setText("Added to tmp config")
        msg.exec_()
app = QtWidgets.QApplication(sys.argv)
ex = Ui_MainWindow()
w = QtWidgets.QMainWindow()
ex.setupUi(w)
w.show()

ex.pushButtonCheck.clicked.connect(ex.revoke)
ex.pushButtonAddPolicy.clicked.connect(ex.addTmpConfig)
exit(app.exec_())
#developed by Hugo Chan All Right Reserved
