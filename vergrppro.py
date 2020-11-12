from getexcel import getdate
from datetime import datetime
from pathlib import Path
import sys

while(True):
    inputgrp=input("groupname:")
    num=input("num:")
    inputip=[]
    if num.isnumeric()==False:
       ip=num.split('/', 3)
       ip[0]=ip[0].replace('-','')
       ip[0]=ip[0].replace('- ','')
       ip[1]=ip[1].replace(' ','')
       inputip.append(ip[0]+'-'+ip[1])
    else:
     for i in range(int(num)):
      ip=input().split('/', 3)
      ip[0]=ip[0].replace('-','')
      ip[0]=ip[0].replace('- ','')
      ip[1]=ip[1].replace(' ','')
      inputip.append(ip[0]+'-'+ip[1])

    gp=['DC1_eHR_FW_C01','DC1_eHR_FW_D01','DC1_eHR_FW_E01','DC1_eHR_FW_F01','DC2_eHR_FW_C01','DC2_eHR_FW_D01','DC2_eHR_FW_E01'\
        ,'DC2_eHR_FW_F01','DC6_PUB_FW_C01','DC6_PUB_FW_D01','DC6_PUB_FW_E01','DC6_PUB_FW_F01','DC7_PUB_FW_C01','DC7_PUB_FW_D01',\
        'DC7_PUB_FW_E01','DC7_PUB_FW_F01']
    for g in gp:
     deviceFullPathName = "Z:\\Network_Security\\Firewall_Policy_Program\\PythonFirewall\\PRDv3\\tmpConfigFile\\"+g
     devv = open(deviceFullPathName, "r")
     contents = devv.readlines()
     for curReadStr in contents:
         if "#" in curReadStr:
             continue
         if "address-book" in curReadStr and "address-set" in curReadStr and inputgrp in curReadStr:
             curReadStr = curReadStr.split()
             for ij in inputip:
                 if ij == curReadStr[9]:
                     print(g, curReadStr[9])
     print("------")