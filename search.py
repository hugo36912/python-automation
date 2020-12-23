import os
import sys
import chardet
import datetime
from datetime import timedelta
from shutil import copyfile
from pathlib import Path
import zipfile
gp=['DC1_eHR_FW_C01_ds','DC1_eHR_FW_D01_ds','DC1_eHR_FW_E01_ds','DC1_eHR_FW_F01_ds','DC2_eHR_FW_C01_ds','DC2_eHR_FW_D01_ds','DC2_eHR_FW_E01_ds'\
,'DC2_eHR_FW_F01_ds','DC6_PUB_FW_B01','DC6_PUB_FW_C01_ds','DC6_PUB_FW_D01_ds','DC6_PUB_FW_E01_ds','DC6_PUB_FW_F01_ds','DC7_PUB_FW_B01','DC7_PUB_FW_C01_ds','DC7_PUB_FW_D01_ds',\
'DC7_PUB_FW_E01_ds','DC7_PUB_FW_F01_ds']



x = datetime.datetime.now()
day=x.day
year=str(x.year)
month=str(x.month)
today=year+'-'+month.zfill(2)+'-'+str(day).zfill(2)
Path('Z:\\Network_Security\\Firewall_Policy_Program\\PythonFirewall\\PRDv3\\OriginalConfigFile\\archive\\'+today).mkdir(parents=True,exist_ok=True)
Path('Z:\\Network_Security\\Firewall_Policy_Program\\PythonFirewall\\PRDv3\\tmpConfigFile\\archive\\'+today).mkdir(parents=True,exist_ok=True)
for g in gp:
    copyfile(
        'Z:\\Network_Security\\Firewall_Policy_Program\\PythonFirewall\\PRDv3\\OriginalConfigFile\\' + g.replace('_ds',''), \
        'Z:\\Network_Security\\Firewall_Policy_Program\\PythonFirewall\\PRDv3\\OriginalConfigFile\\archive\\'+today+"\\"+g.replace('_ds',''))
    copyfile(
        'Z:\\Network_Security\\Firewall_Policy_Program\\PythonFirewall\\PRDv3\\tmpConfigFile\\' + g.replace('_ds',
                                                                                                               ''), \
        'Z:\\Network_Security\\Firewall_Policy_Program\\PythonFirewall\\PRDv3\\tmpConfigFile\\archive\\' + today + "\\" + g.replace(
            '_ds', ''))
print('backup success')
offset = x.weekday() - 2
dat= x - timedelta(days=offset)



search_path="config_"+str(dat.year)+str(dat.month).zfill(2)+str(dat.day).zfill(2)
search_path='Y:\\HCP_Facing\\Download\\'+search_path
search=Path(search_path)
if search.is_dir():
    pass
else:
    if Path(search_path+'.zip').is_file():
     with zipfile.ZipFile(search_path+".zip","r") as zip_ref:
      print('zipping')
      zip_ref.extractall(search_path)
     print('upzip success')
    else:
     search_path=input("input:")
     search_path='Y:\\HCP_Facing\\Download\\'+search_path
for g in gp:
    for root, dir, files in os.walk(search_path):
       for f in files:
         if g in f:
             sourpa=os.path.join(root, f)
             print("file copied",sourpa)
             if g=='DC6_PUB_FW_B01' or g== 'DC7_PUB_FW_B01':
                 copyfile(sourpa,'Z:\\Network_Security\\Firewall_Policy_Program\\PythonFirewall\\PRDv3\\OriginalConfigFile\\' + g.replace('_ds',''))
                 copyfile(sourpa,'Z:\\Network_Security\\Firewall_Policy_Program\\PythonFirewall\\PRDv3\\tmpConfigFile\\' + g.replace( '_ds', ''))
             else:
              with open(sourpa,'r',encoding='utf-16') as sour:
                 contents=sour.read()
              with open('Z:\\Network_Security\\Firewall_Policy_Program\\PythonFirewall\\PRDv3\\OriginalConfigFile\\' + g.replace( '_ds', ''), 'w', encoding='utf-8') as dest:
                   dest.write(contents)
              with open('Z:\\Network_Security\\Firewall_Policy_Program\\PythonFirewall\\PRDv3\\tmpConfigFile\\' + g.replace( '_ds', ''), 'w', encoding='utf-8') as destt:
                   destt.write(contents)
print('finished')