from tkinter import *
#from tkinter.ttk import *
from functools import partial
from MainGUI import Ui_MainWindow
#from firewallRule import Ui_FirewallRule
from PyQt5 import QtWidgets


import tkinter as tk
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    
    ex.pushButtonCheck.clicked.connect(ex.policyCheck)
    #ex.pushButtonConfigFileBackup.clicked.connect(ex.ConfigBackupPage)
    #ex.pushButtonCopyConfigHCP.clicked.connect(ex.copyConfigFileHCP)
    #ex.pushButtonCopyConfigPUB.clicked.connect(ex.copyConfigFilePUB)
    #ex.pushButtonCopyConfigHCP.clicked.connect(ex.ConfigBackupPage)
    
    
    ex.pushButtonAddPolicy.clicked.connect(ex.addTmpConfig)
    #ex.pushButtonClearTmpTSR.clicked.connect(ex.clearTmpConfig)   
    ex.pushButtonArchiveTSR.clicked.connect(ex.ArchiveTSR)
    ex.pushButtonConfigBackup.clicked.connect(ex.ConfigBackup)
    exit(app.exec_())
    

