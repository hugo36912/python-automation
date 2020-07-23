import os
from pathlib import Path
from connectDatabase.getDataFromExcel import getDataFromExcel

class getConfig_SRX(object):
    def startGetConfig(deviceName, excelDeviceFull):
       
        DeviceConfig = []
        #excel_get_data = []
        #excel_get_data = getDataFromExcel.startGetData("Path")       
        #inputData = []    
        #for rowData in excel_get_data:
        #    inputData.append(rowData[1])
            
            
        DestPath = excelDeviceFull[0] + "\\" + excelDeviceFull[2] + "\\" + deviceName
        tmpDestPath = excelDeviceFull[0] + "\\" + excelDeviceFull[3] + "\\"  + deviceName
        
        deviceFullPathName = DestPath
        deviceTmpFullPathName = tmpDestPath
               
        #deviceFullPathName = "D:\\PythonFirewall_PUB\\PUBv1\\tmpFirewallConfig\\tmpConfig\\" + deviceName
        #deviceTmpFullPathName = "D:\\PythonFirewall_PUB\\PUBv1\\tmpFirewallConfig\\tmpConfig\\tmp" + deviceName

        File=open(deviceTmpFullPathName, "r")        
        if File.mode == 'r':           
            contents = File.readlines()
            for curReadStr in contents:
            #print(contents)
                if "from-zone" in curReadStr and "to-zone" in curReadStr:
                    DeviceConfig.append(curReadStr)
                if "address-book" in curReadStr and "address-set" in curReadStr:
                    DeviceConfig.append(curReadStr)
                if "address-book" in curReadStr and "address" in curReadStr:   
                    DeviceConfig.append(curReadStr)
                if "set applications application" in curReadStr:
                    DeviceConfig.append(curReadStr)
                    #pass
                    
        FileTmp=open(deviceFullPathName, "r")        
        if FileTmp.mode == 'r':           
            contents = FileTmp.readlines()
            for curReadStr in contents:
            #print(contents)
                if "from-zone" in curReadStr and "to-zone" in curReadStr:
                    DeviceConfig.append(curReadStr)
                if "address-book" in curReadStr and "address-set" in curReadStr:
                    DeviceConfig.append(curReadStr)
                if "address-book" in curReadStr and "address" in curReadStr:   
                    DeviceConfig.append(curReadStr)
                if "set applications application" in curReadStr:
                    DeviceConfig.append(curReadStr) 

         
        return DeviceConfig   
        #print(DeviceConfig)

#getDeviceConfig.startGetConfig()
