import json
import os
from Revoke.comb import cume
from pathlib import Path

def excum(MainGUI,name,list,cjp,sour,dest,app,dicmas,inputDescription):
    cp1=[]
    cp2 = []
    cp3 = []
    ccp=[]
    i=0
    policy=[]
    command=[]
    print(name)
    for key in list.keys():
        for policyy in list[key]:
                policy = policyy.split()
                if name in policy:
                    if 'source-address' in policy:
                        cp1.append(policy[11])
                    if 'destination-address' in policy:
                        cp2.append(policy[11])
                    if 'application' in policy:
                        cp3.append(policy[11])

    while i < len(cp1):
        j = 0
        while j < len(cp2):
            k = 0
            while k < len(cp3):
                jp = []
                jp.append(cp1[i])
                jp.append(cp2[j])
                jp.append(cp3[k])
                ccp.append(jp)
                k += 1
            j += 1
        i += 1
    print("before delete",ccp)
    for jj in cjp:
      for ch in ccp:
        if jj == ch:
            ccp.remove(ch)
    print("after delete", ccp)
    star = ''
    en = ''
    des = ''
    if ccp ==[]:
        command.append("#Policy " + str(MainGUI.spinBoxRuleNo.value()) + " ############# delete Policy ##############")
        for key in list.keys():
            for policyy in list[key]:
                policy = policyy.split()
                if name in policy:
                    policy[0]='delete'
                    hc=' '.join(policy)
                    command.append(hc)
    else :
        command.append("#Policy " + str(MainGUI.spinBoxRuleNo.value()) + " ############# delete Policy ##############")
        for key in list.keys():
            for policyy in list[key]:
                policy = policyy.split()
                if name in policy:
                    star = policy[4]
                    en = policy[6]


        command.extend(cume(name,list,ccp,star,en,sour,dest,app,dicmas,inputDescription))
        print(dicmas)

    return command

#developed by Hugo Chan All Right Reserved



