import json
import os
from comb import cume
from pathlib import Path
from connectDatabase.getDataFromExcel import getDataFromExcel
#developed by Hugo Chan All Right Reserved
def excum(name,list,cjp,sour,dest,app,dicmas):
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
                            if '.' in policy[11]:
                                s = policy[11].split('-')
                                cp1.append(s[0])
                        if 'destination-address' in policy:
                            if '.' in policy[11]:
                                d = policy[11].split('-')
                                cp2.append(d[0])
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
        if ccp ==[]:
            for key in list.keys():
                for policyy in list[key]:
                    policy = policyy.split()
                    if name in policy:
                        policy[0]='delete'
                        hc=' '.join(policy)
                        command.append(hc)
        else :
            star=''
            en=''
            des=''
            for key in list.keys():
                for policyy in list[key]:
                    policy = policyy.split()
                    if name in policy:
                        star=policy[4]
                        en=policy[6]
                        if 'source-address'  in policy or 'destination-address'  in policy or 'application' in policy:
                          policy[0] = 'delete'
                          hc = ' '.join(policy)
                          command.append(hc)

            command.extend(cume(name,list,ccp,star,en,sour,dest,app,dicmas))
            print(dicmas)

        return command

#developed by Hugo Chan All Right Reserved



