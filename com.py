#developed by HugoC .All Right reserved
import os
from pathlib import Path
gp=['DC1_eHR_FW_C01','DC1_eHR_FW_D01','DC1_eHR_FW_E01','DC1_eHR_FW_F01','DC2_eHR_FW_C01','DC2_eHR_FW_D01','DC2_eHR_FW_E01'\
,'DC2_eHR_FW_F01','DC6_PUB_FW_B01','DC6_PUB_FW_C01','DC6_PUB_FW_D01','DC6_PUB_FW_E01','DC6_PUB_FW_F01','DC7_PUB_FW_B01','DC7_PUB_FW_C01','DC7_PUB_FW_D01',\
'DC7_PUB_FW_E01','DC7_PUB_FW_F01']
fil=input("TSR folder name:")
num=input("how many TSR:")
fil='Y:\\HCP_Facing\\Upload\\'+fil
Path(fil+'\\combineTSR').mkdir(parents=True,exist_ok=True)
for g in gp:
    lk = open(fil+'\\combineTSR\\'+ g,'w')
for i in range(1,int(num)+1):
    for root, dir, files in os.walk(fil):
        for c in dir:
         if str(i).zfill(2)+'_RID' in c:
          print("involved folder: "+c)
          for g in gp:
              lk=open(fil+'\\'+c+'\\'+g)
              lj=lk.read()
              ck=open(fil+'\\combineTSR\\'+ g,'a')
              ck.write(c+"\n")
              ck.write(lj)
              ck.write('\n\n--------------------------------------------------------------------------------------------\n')

#developed by HugoC .All Right reserved