import os
from pathlib import Path
from Revoke.revokeop import excum
from Revoke.revokeip import policyvoke
from initial.initial import initial
from connectDatabase.getGroupFromDB import getGroupInfoFromExcel
from connectDatabase.getZoneFromDB import getZoneInfoFromExcel
from connectDatabase.getApplicationFromDB import getAppInfoFromExcel
from connectSRX.getConfig_SRX import getConfig_SRX
from connectSRX.getRuleFromConfig import getRuleFromConfig
from connectSRX.getConfig_Forti import getConfig_Forti
from processResults.processResults import processResults


class Revoke(object):
    def startRevoke(self):
        self.printTime("(Program Start Revoke)Current Time =")
        try:
            initial.reset(self)

            startCheck = 0
            startPoint = 4
                  
            #print("phase=", phase)
            print("startCheck=", startCheck)

            inputSource = []
            inputSource = ' '.join(self.textEditSource.toPlainText().split('\n')).split()
                      
            inputDestination = []
            inputDestination = ' '.join(self.textEditDestination.toPlainText().split('\n')).split()
            
            inputApplication = []
            inputApplication = ' '.join(self.textEditApplication.toPlainText().split('\n')).split()
            
            if inputDestination == [] and inputApplication == []:
                print("single source")
                policyvoke.startpolicyvoke(self)
                print("completed single source revoke check")
                return 1

            strTCP = "_TCP"  #default TCP
            for idx, item in enumerate(inputApplication):
                #print(inputApplication[idx])
                if inputApplication[idx].isdigit(): # is digit + default TCP
                    #print(inputApplication[idx])
                    inputApplication[idx] = inputApplication[idx] + strTCP
                elif "_UDP" in inputApplication[idx] or "_TCP" in inputApplication[idx]:
                    pass
                elif "any" in inputApplication[idx] or "Any" in inputApplication[idx]:
                    pass
                elif "WIN_Join_Domain" in inputApplication[idx]:
                    pass        
                elif not "junos-" in inputApplication[idx]:
                    inputApplication[idx] = "junos-" + inputApplication[idx]   
                    #print(inputApplication[idx])
            
            inputDescription = []
            inputDescription = ' '.join(self.textEditDescription.toPlainText().split('\n')).split()
            inputDescription=' '.join(inputDescription)
            # sort by name
            inputSource.sort()
            inputDestination.sort()
            inputApplication.sort()

            print("inputSource=",inputSource)
            print("inputDestination=",inputDestination)
            print("inputApplication=",inputApplication)
            print("inputDescription=",inputDescription)

            #find zone, group and fullname info
            InputSourceZoneInfo = []
            InputSourceGroupInfo = []
            InputDestinationZoneInfo = []
            InputDestinationGroupInfo = []
            InputAppInfo = []

            tempGroupInfo = []
            i = 0
            for source in inputSource:
            #input is ip
                tempGroupInfo = []
                tempGroupInfo = getGroupInfoFromExcel.startGetGroupInfo(source, self.fw_group_get_data)
                if "." in source and "_" not in source and "-" not in source:
                    InputSourceZoneInfo.append(getZoneInfoFromExcel.startGetZoneInfo(source, self.fw_zone_get_data))
                    InputSourceGroupInfo.append(tempGroupInfo) ## whole row data from excel
                    for groupInfo in tempGroupInfo:
                        if groupInfo[3] == inputSource[i]:
                            inputSource[i] = groupInfo[2]
                      
                else:                       
                    #print("SourcetempGroupInfo=", tempGroupInfo)
                    InputSourceZoneInfo.append(getZoneInfoFromExcel.startGetZoneInfo(tempGroupInfo[0][3], self.fw_zone_get_data))
                    InputSourceGroupInfo.append(tempGroupInfo) ## whole row data from excel                    
                i += 1

            i = 0
            for dest in inputDestination:
                tempGroupInfo = []
                tempGroupInfo = getGroupInfoFromExcel.startGetGroupInfo(dest, self.fw_group_get_data)
                if "." in dest and "_" not in dest and "-" not in dest:
                    InputDestinationZoneInfo.append(getZoneInfoFromExcel.startGetZoneInfo(dest, self.fw_zone_get_data))
                    InputDestinationGroupInfo.append(tempGroupInfo) ## whole row data from excel
                    for groupInfo in tempGroupInfo:
                        if groupInfo[3] == inputDestination[i]:
                            inputDestination[i] = groupInfo[2]
                      
                else:                    
                    #print("DesttempGroupInfo=", tempGroupInfo)
                    InputDestinationZoneInfo.append(getZoneInfoFromExcel.startGetZoneInfo(tempGroupInfo[0][3], self.fw_zone_get_data))
                    InputDestinationGroupInfo.append(tempGroupInfo) ## whole row data from excel
                i += 1
                
            #print("1. InputDestinationZoneInfo=", InputDestinationZoneInfo)
            #print("2. tempGroupInfoDest=", tempGroupInfo)
            appListSRX = []
            appListForti = []
            for app in inputApplication:
                tempInputAppInfo = getAppInfoFromExcel.startGetAppInfo(app, self.fw_app_get_data)             
                InputAppInfo.append(tempInputAppInfo)



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
            

            config_list = [[] for i in range(18)]                
            for startCount in range(0,16):                    
                config_list[startCount] = getConfig_SRX.startGetConfig(self.excelDeviceFull[startPoint + startCount], self.excelDeviceFull)                        
  
            config_list[16] = getConfig_Forti.startGetConfig(self.excelDeviceFull[startPoint + 18], self.excelDeviceFull)
            config_list[17] = getConfig_Forti.startGetConfig(self.excelDeviceFull[startPoint + 19], self.excelDeviceFull)

            print("Get config completed")
            
            #########get policy rule to Key########
            config_dict_list = [[] for i in range(18)] 
            
            self.printTime("(Start get dict from config)Current Time =")     
            for startCount in range(0,16):
                config_dict_list[startCount] = getRuleFromConfig.getConfig(config_list[startCount])
            config_dict_list[16] = getRuleFromConfig.getConfig(config_list[16])
            config_dict_list[17] = getRuleFromConfig.getConfig(config_list[17]) 

            self.printTime("(End get dict from config)Current Time =") 


            self.policyCommandAdd_list = [[] for i in range(18)]
            self.objectAdd = [[] for i in range(18)]

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
            self.policyCommandAdd_list[16] = ""
            self.policyCommandAdd_list[17] = ""

            cp1 = []
            cp2 = []
            cp3 = []
            policy = []
            for i in range(0, 18):
                dicmic={}
                cc=[]
                for key in config_dict_list[i].keys():
                    for policyy in config_dict_list[i][key]:
                        policy = policyy.split()
                        for jj in cp:
                            if jj[0] in policy and policy[10] == 'source-address' :
                                cp1.append(policy[8])
                            if jj[1] in policy and policy[10] == 'destination-address':
                                cp2.append(policy[8])
                            if jj[2] in policy :
                                cp3.append(policy[8])
                set1 = set(cp1).intersection(set(cp2))
                jc = set1.intersection(set(cp3))
                if jc:
                    for ij in jc :
                        ea=(excum(self,ij,config_dict_list[i],cp,inputSource,inputDestination,inputApplication,dicmic,inputDescription))
                        cc.extend(ea)
                self.policyCommandAdd_list[i]=cc
                jc = ''
                cp1 = []
                cp2 = []
                cp3 = []
                policy = []

            print("finished")

            print("############" + self.excelDeviceShort[startPoint + 0] + "############")
            self.textPRI_HCP_C01.setText("")
            for readline in self.policyCommandAdd_list[0]:
                print(readline)
                self.textPRI_HCP_C01.append(readline)
            for readline in self.objectAdd[0]:
                print(readline)

                self.textPRI_HCP_C01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 4] + "############")
            self.textSEC_HCP_C01.setText("")
            for readline in self.policyCommandAdd_list[4]:
                print(readline)
                self.textSEC_HCP_C01.append(readline)
            for readline in self.objectAdd[4]:
                print(readline)
                self.textSEC_HCP_C01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 1] + "############")
            self.textPRI_HCP_D01.setText("")
            for readline in self.policyCommandAdd_list[1]:
                print(readline)
                self.textPRI_HCP_D01.append(readline)
            for readline in self.objectAdd[1]:
                print(readline)
                self.textPRI_HCP_D01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 5] + "############")
            self.textSEC_HCP_D01.setText("")
            for readline in self.policyCommandAdd_list[5]:
                print(readline)
                self.textSEC_HCP_D01.append(readline)
            for readline in self.objectAdd[5]:
                print(readline)
                self.textSEC_HCP_D01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 2] + "############")
            self.textPRI_HCP_E01.setText("")
            for readline in self.policyCommandAdd_list[2]:
                print(readline)
                self.textPRI_HCP_E01.append(readline)
            for readline in self.objectAdd[2]:
                print(readline)
                self.textPRI_HCP_E01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 6] + "############")
            self.textSEC_HCP_E01.setText("")
            for readline in self.policyCommandAdd_list[6]:
                print(readline)
                self.textSEC_HCP_E01.append(readline)
            for readline in self.objectAdd[6]:
                print(readline)
                self.textSEC_HCP_E01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 3] + "############")
            self.textPRI_HCP_F01.setText("")
            for readline in self.policyCommandAdd_list[3]:
                print(readline)
                self.textPRI_HCP_F01.append(readline)
            for readline in self.objectAdd[3]:
                print(readline)
                self.textPRI_HCP_F01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 7] + "############")
            for readline in self.policyCommandAdd_list[7]:
                print(readline)
                self.textSEC_HCP_F01.append(readline)
            for readline in self.objectAdd[7]:
                print(readline)
                self.textSEC_HCP_F01.append(readline)

            startPoint=12
            print("############" + self.excelDeviceShort[startPoint + 0] + "############")
            self.textPRI_PUB_C01.setText("")
            for readline in self.policyCommandAdd_list[8]:
                print(readline)
                self.textPRI_PUB_C01.append(readline)
            for readline in self.objectAdd[8]:
                print(readline)
                # self.textBrowser1.setText("testPri-C01 ")
                # self.textBrowser1.append(','.join(readline))
                self.textPRI_PUB_C01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 4] + "############")
            self.textSEC_PUB_C01.setText("")
            for readline in self.policyCommandAdd_list[12]:
                print(readline)
                self.textSEC_PUB_C01.append(readline)
            for readline in self.objectAdd[12]:
                print(readline)
                # self.textBrowser2.append(','.join(readline))
                self.textSEC_PUB_C01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 1] + "############")
            self.textPRI_PUB_D01.setText("")
            for readline in self.policyCommandAdd_list[9]:
                print(readline)
                self.textPRI_PUB_D01.append(readline)
            for readline in self.objectAdd[9]:
                print(readline)
                self.textPRI_PUB_D01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 5] + "############")
            self.textSEC_PUB_D01.setText("")
            for readline in self.policyCommandAdd_list[13]:
                print(readline)
                self.textSEC_PUB_D01.append(readline)
            for readline in self.objectAdd[13]:
                print(readline)
                self.textSEC_PUB_D01.append(readline)
            print("############" + self.excelDeviceShort[startPoint + 2] + "############")
            self.textPRI_PUB_E01.setText("")
            for readline in self.policyCommandAdd_list[10]:
                print(readline)
                self.textPRI_PUB_E01.append(readline)
            for readline in self.objectAdd[10]:
                print(readline)
                self.textPRI_PUB_E01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 6] + "############")
            self.textSEC_PUB_E01.setText("")
            for readline in self.policyCommandAdd_list[14]:
                print(readline)
                self.textSEC_PUB_E01.append(readline)
            for readline in self.objectAdd[14]:
                print(readline)
                self.textSEC_PUB_E01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 3] + "############")
            self.textPRI_PUB_F01.setText("")
            for readline in self.policyCommandAdd_list[11]:
                print(readline)
                self.textPRI_PUB_F01.append(readline)
            for readline in self.objectAdd[11]:
                print(readline)
                self.textPRI_PUB_F01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 7] + "############")
            for readline in self.policyCommandAdd_list[15]:
                print(readline)
                self.textSEC_PUB_F01.append(readline)
            for readline in self.objectAdd[15]:
                print(readline)
                self.textSEC_PUB_F01.append(readline)

            print("############" + self.excelDeviceShort[startPoint + 10] + "############")
            for readline in self.policyCommandAdd_list[16]:
                print(readline)
                self.textPRI_PUB_B01.append(readline)
            for readline in self.objectAdd[16]:
                print(readline)
                self.textPRI_PUB_B01.append(readline)
                
            print("############" + self.excelDeviceShort[startPoint + 11] + "############")
            for readline in self.policyCommandAdd_list[17]:
                print(readline)
                self.textSEC_PUB_B01.append(readline)
            for readline in self.objectAdd[17]:
                print(readline)
                self.textSEC_PUB_B01.append(readline)        

            self.CommandAdd_PRI_HCP_C01.extend(self.policyCommandAdd_list[0])
            self.CommandAdd_PRI_HCP_D01.extend(self.policyCommandAdd_list[1])
            self.CommandAdd_PRI_HCP_E01.extend(self.policyCommandAdd_list[2])
            self.CommandAdd_PRI_HCP_F01.extend(self.policyCommandAdd_list[3])
            self.CommandAdd_PRI_HCP_C01.extend(self.objectAdd[0])
            self.CommandAdd_PRI_HCP_D01.extend(self.objectAdd[1])
            self.CommandAdd_PRI_HCP_E01.extend(self.objectAdd[2])
            self.CommandAdd_PRI_HCP_F01.extend(self.objectAdd[3])
            self.CommandAdd_SEC_HCP_C01.extend(self.policyCommandAdd_list[4])
            self.CommandAdd_SEC_HCP_D01.extend(self.policyCommandAdd_list[5])
            self.CommandAdd_SEC_HCP_E01.extend(self.policyCommandAdd_list[6])
            self.CommandAdd_SEC_HCP_F01.extend(self.policyCommandAdd_list[7])
            self.CommandAdd_SEC_HCP_C01.extend(self.objectAdd[4])
            self.CommandAdd_SEC_HCP_D01.extend(self.objectAdd[5])
            self.CommandAdd_SEC_HCP_E01.extend(self.objectAdd[6])
            self.CommandAdd_SEC_HCP_F01.extend(self.objectAdd[7])
            self.CommandAdd_PRI_PUB_C01.extend(self.policyCommandAdd_list[8])
            self.CommandAdd_PRI_PUB_D01.extend(self.policyCommandAdd_list[9])
            self.CommandAdd_PRI_PUB_E01.extend(self.policyCommandAdd_list[10])
            self.CommandAdd_PRI_PUB_F01.extend(self.policyCommandAdd_list[11])
            self.CommandAdd_PRI_PUB_C01.extend(self.objectAdd[8])
            self.CommandAdd_PRI_PUB_D01.extend(self.objectAdd[9])
            self.CommandAdd_PRI_PUB_E01.extend(self.objectAdd[10])
            self.CommandAdd_PRI_PUB_F01.extend(self.objectAdd[11])
            self.CommandAdd_SEC_PUB_C01.extend(self.policyCommandAdd_list[12])
            self.CommandAdd_SEC_PUB_D01.extend(self.policyCommandAdd_list[13])
            self.CommandAdd_SEC_PUB_E01.extend(self.policyCommandAdd_list[14])
            self.CommandAdd_SEC_PUB_F01.extend(self.policyCommandAdd_list[15])
            self.CommandAdd_SEC_PUB_C01.extend(self.objectAdd[12])
            self.CommandAdd_SEC_PUB_D01.extend(self.objectAdd[13])
            self.CommandAdd_SEC_PUB_E01.extend(self.objectAdd[14])
            self.CommandAdd_SEC_PUB_F01.extend(self.objectAdd[15])

            self.CommandAdd_PRI_PUB_B01.extend(self.policyCommandAdd_list[16])
            self.CommandAdd_PRI_PUB_B01.extend(self.objectAdd[16])
            self.CommandAdd_SEC_PUB_B01.extend(self.policyCommandAdd_list[17])
            self.CommandAdd_SEC_PUB_B01.extend(self.objectAdd[17])
            #processResults.printResults(self,0, 12)
            #processResults.printResults(self,1, 4)

        except Exception as e:
            print("Exception",e)
            raise
        else:
            pass
        finally:
            pass 
