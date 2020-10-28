from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QWidget, QListWidgetItem, QLineEdit, QApplication
from getexcel import getdate
from datetime import datetime
import csv
import sys
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
        MainWindow.setWindowTitle(_translate("MainWindow", "b01 verify"))
        self.labelSource.setText(_translate("MainWindow", "Source IP"))
        self.labelDestination.setText(_translate("MainWindow", "Destinaion IP"))
        self.labelApplication.setText(_translate("MainWindow", "Application"))
        self.labelInputDescription.setText(_translate("MainWindow", "Description"))
        self.pushButtonCheck.setWhatsThis(_translate("MainWindow","<html><head/><body><p><span style=\" font-weight:600;\">Check</span></p></body></html>"))
        self.pushButtonCheck.setText(_translate("MainWindow", "verify"))
    def verif(self, MainWindow):

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("(policy Check)Current Time =", current_time)

        involve = []
        inputSplitSubnet = []
        destsplitsubnet = []
        inputSource = []
        inputSource = ' '.join(self.textEditSource.toPlainText().split('\n')).split()
        inputDestination = []
        inputDestination = ' '.join(self.textEditDestination.toPlainText().split('\n')).split()
        inputApplication = []
        inputApplication = ' '.join(self.textEditApplication.toPlainText().split('\n')).split()
        strTCP = "_TCP"  # default TCP
        for idx, item in enumerate(inputApplication):
            if inputApplication[idx].isdigit() :
                inputApplication[idx] =  'TCP_' + inputApplication[idx]
            if  strTCP in inputApplication[idx]:
                inputApplication[idx] =  inputApplication[idx].replace(strTCP,'')
                inputApplication[idx] = 'TCP_' + inputApplication[idx]

        print('inputSource:', inputSource)
        print('inputDestination:', inputDestination)
        print('inputApplication:', inputApplication)
        with open('C:\\b01\\DC1B.csv', newline='') as csvfile:
            rows = csv.reader(csvfile)

            cp1=[]
            cp2=[]
            cp3=[]
            for cc in rows:
                for inp in inputSource:
                    if inp =='any':
                       inp='Any'
                    if inp in cc[3]:
                        cp1.append(cc[2])
                for ind in inputDestination:
                    if ind == 'any':
                        ind = 'Any'
                    if ind in cc[4]:
                        cp2.append(cc[2])
                for inap in inputApplication:
                    if inap == '443_TCP' or inap =='TCP_443':
                        inap = 'https'
                    if inap == '22_TCP'or inap =='TCP_22':
                        inap = 'ssh'
                    if inap == '80_TCP'or inap =='TCP_80':
                        inap = 'http'
                    if inap == '53_UDP' or inap =='TCP_53':
                        inap = 'domain-udp'
                    if inap == '25_TCP'or inap =='TCP_25':
                        inap = 'smtp'
                    if inap == 'ping':
                        inap = 'icmp-proto'
                    if inap == 'tr':
                        inap = 'traceroute'
                    if inap in cc[6]:
                        cp3.append(cc[2])
            set1 = set(cp1).intersection(set(cp2))
            jc = set1.intersection(set(cp3))
        print("DC1-B01:",jc)
        with open('C:\\b01\\DC2B.csv', newline='') as csvfile:
            rows = csv.reader(csvfile)

            cp1=[]
            cp2=[]
            cp3=[]
            for cc in rows:
                for inp in inputSource:
                    if inp =='any':
                       inp='Any'
                    if inp in cc[3]:
                        cp1.append(cc[2])
                for ind in inputDestination:
                    if ind == 'any':
                        ind = 'Any'
                    if ind in cc[4]:
                        cp2.append(cc[2])
                for inap in inputApplication:
                    if inap == '443_TCP' or inap == 'TCP_443':
                        inap = 'https'
                    if inap == '22_TCP' or inap == 'TCP_22':
                        inap = 'ssh'
                    if inap == '80_TCP' or inap == 'TCP_80':
                        inap = 'http'
                    if inap == '53_UDP' or inap == 'TCP_53':
                        inap = 'domain-udp'
                    if inap == '25_TCP' or inap == 'TCP_25':
                        inap = 'smtp'
                    if inap == 'ping':
                        inap = 'icmp-proto'
                    if inap == 'tr':
                        inap = 'traceroute'
                    if inap in cc[6]:
                        cp3.append(cc[2])
            set1 = set(cp1).intersection(set(cp2))
            jc = set1.intersection(set(cp3))
        print("DC2-B01:", jc)
app = QtWidgets.QApplication(sys.argv)
ex = Ui_MainWindow()
w = QtWidgets.QMainWindow()
ex.setupUi(w)
w.show()

ex.pushButtonCheck.clicked.connect(ex.verif)
exit(app.exec_())