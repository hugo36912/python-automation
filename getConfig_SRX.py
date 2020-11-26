import os
from pathlib import Path
from connectDatabase.getDataFromExcel import getDataFromExcel

class getConfig_SRX(object):
    def startGetConfig(deviceName, excelDeviceFull):
       
        DeviceConfig = []
                       
        DestPath = excelDeviceFull[0] + "\\" + excelDeviceFull[2] + "\\" + deviceName
        
        deviceFullPathName = DestPath
               
        FileTmp=open(deviceFullPathName, "r")        
        if FileTmp.mode == 'r':           
            contents = FileTmp.readlines()
            for curReadStr in contents:
            #print(contents)
                if "#" in curReadStr:
                    continue
                if "delete" in curReadStr and "schedulers" not in curReadStr :
                    hj=curReadStr
                    hj=hj.replace("delete","set")
                    if hj in DeviceConfig:
                     DeviceConfig.remove(hj)
                     continue
                if "from-zone" in curReadStr and "to-zone" in curReadStr:
                    DeviceConfig.append(curReadStr)
                if "address-book" in curReadStr and "address-set" in curReadStr:
                    DeviceConfig.append(curReadStr)
                if "address-book" in curReadStr and "address-set" not in curReadStr:   
                    DeviceConfig.append(curReadStr)
                if "set applications application" in curReadStr:
                    DeviceConfig.append(curReadStr) 
        #print(DeviceConfig[-1])
        return DeviceConfig   
        #print(DeviceConfig)

#getDeviceConfig.startGetConfig()
