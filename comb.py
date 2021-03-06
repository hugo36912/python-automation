import json
import os
from pathlib import Path


#developed by Hugo Chan All Right Reserved
come = []

def tran(value,time,rule):

    print("value", value)
    print("time", time)
    print("rule", rule)

    newval=int(value)+time
    newval=str(newval).zfill(4)
    newval=rule[0]+'-'+rule[1]+'-'+newval
    return newval

def cume(name,list,ne,start,end,sourc,desti,appl,mas,inputDescription):
    cp1=[]
    cp2=[]
    cp3=[]
    cp=[]
    sp1 = []
    sp2 = []
    sp3 = []
    sp = []
    des=''
    namej = name.split("-")
    maxn = namej[0] + namej[1]
    comm=[]
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
                if 'description' in policy:
                    des=str(policy[10])+' '+inputDescription
    for key in list.keys():
        for policyy in list[key]:
            policy = policyy.split()
            cj=policy[8].split('-')
            if cj[0] ==namej[0] and cj[1]==namej[1]:
                if cj[2].isnumeric():
                     cp.append(cj[2])
    matchSource = []
    matchSource = set(cp1) & set(sourc)
    matchDest = []
    matchDest = set(cp2) & set(desti)
    matchApp = []
    matchApp = set(cp3) & set(appl)
    if maxn in mas:
        pay=int(mas[maxn])
    else:
        pay=max(cp)
        mas[maxn]=pay



    result1 = []
    result2 = []
    result3 = []

    if not matchSource == [] and not matchDest == [] and not matchApp == []:
        if len(cp3) > len(matchApp):
            result1.append(cp1)
            result1.append(cp2)
            result1.append(set(cp3) - set(matchApp))
        if len(cp1) > len(matchSource):
            result2.append(set(cp1) - set(matchSource))
            result2.append(cp2)
            result2.append(matchApp)
        if len(cp2) > len(matchDest):
            result3.append(matchSource)
            result3.append(set(cp2) - set(matchDest))
            result3.append(matchApp)

        if not result1 == []:
            print("result1=", result1)
        if not result2 == []:
            print("result2=", result2)
        if not result1 == []:
            print("result3=", result3)

        last = tran(pay, 0, namej)
        nema = tran(pay, 1, namej)
        nema2 = tran(pay, 2, namej)

    if result1 != []:
        if set(cp1) != set(result1[0]):
         result1[0] = set(cp1) - set(result1[0])
         for so in result1[0]:
            comm.append(
                "delete security policies from-zone " + start + " to-zone " + end + " policy " + str(name) +
                " match source-address " + str(so))
        if set(cp2) != set(result1[1]):
         result1[1] = set(cp2) - set(result1[1])
         for de in result1[1]:
            comm.append(
                "delete security policies from-zone " + start + " to-zone " + end + " policy " + str(name) +
                " match destination-address " + str(de))
        if set(cp3) != set(result1[2]):
         result1[2]=set(cp3)-set(result1[2])
         for ap in result1[2]:
            comm.append("delete security policies from-zone " + start + " to-zone " + end + " policy " + str(name) +
                    " match application " + str(ap))

        if result2 != [] and result3 != []:
            comm.append(
                            "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                            " description " + des)
            for so in result2[0]:
                comm.append(
                            "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                            " match source-address " + str(so))
            for de in result2[1]:
                comm.append(
                            "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                            " match destination-address " + str(de))
            for ap in result2[2]:
                comm.append("set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                            " match application " + str(ap))
            comm.append("set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                        " then permit")
            comm.append("set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                        " then log session-close")
            comm.append(
                "insert security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) + " after "
                + last)
            comm.append(
                            "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema2) +
                            " description " + des)
            for so in result3[0]:
                comm.append(
                            "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema2) +
                            " match source-address " + str(so))
            for de in result3[1]:
                comm.append(
                            "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema2) +
                            " match destination-address " + str(de))
            for ap in result3[2]:
                comm.append("set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema2) +
                            " match application " + str(ap))
            comm.append("set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema2) +
                        " then permit")
            comm.append("set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema2) +
                        " then log session-close")
            comm.append(
                "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema2) + " after "
                + nema)
            pay = int(pay)
            pay += 2
            mas[maxn] = pay
        if result2 != [] and result3 == []:
            comm.append(
                            "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                            " description " + des)
            for so in result2[0]:
                        comm.append(
                            "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                            " match source-address " + str(so))
            for de in result2[1]:
                    comm.append(
                        "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                        " match destination-address " + str(de))
            for ap in result2[2]:
                comm.append("set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                            " match application " + str(ap))
            comm.append("set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                        " then permit")
            comm.append("set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                        " then log session-close")
            comm.append(
                "insert security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) + " after "
                + last)
            pay = int(pay)
            pay += 1
            mas[maxn] = pay
        if result3 != [] and result2 == []:
            comm.append(
                            "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                            " description " + des)
            for so in result3[0]:
                comm.append(
                    "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                    " match source-address " + str(so))
            for de in result3[1]:
                comm.append(
                    "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                    " match destination-address " + str(de))
            for ap in result3[2]:
                comm.append(
                    "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                    " match application " + str(ap))
            comm.append(
                "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                " then permit")
            comm.append(
                "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                " then log session-close")
            comm.append(
                "insert security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) + " after "
                + last)

            pay = int(pay)
            pay += 1
            mas[maxn] = pay
    if result1 == [] and result2 != []:
        if set(cp1) != set(result2[0]):
            result2[0] = set(cp1) - set(result2[0])
            for so in result2[0]:
                comm.append(
                    "delete security policies from-zone " + start + " to-zone " + end + " policy " + str(name) +
                    " match source-address " + str(so))
        if set(cp2) != set(result2[1]):
            result2[1] = set(cp2) - set(result2[1])
            for de in result2[1]:
                comm.append(
                    "delete security policies from-zone " + start + " to-zone " + end + " policy " + str(name) +
                    " match destination-address " + str(de))
        if set(cp3) != set(result2[2]):
            result2[2] = set(cp3) - set(result2[2])
            for ap in result1[2]:
                comm.append("delete security policies from-zone " + start + " to-zone " + end + " policy " + str(name) +
                        " match application " + str(ap))
        if result3 != []:
            comm.append(
                            "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                            " description " + des)
            for so in result3[0]:
                comm.append(
                            "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                            " match source-address " + str(so))
            for de in result3[1]:
                comm.append(
                            "set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                            " match destination-address " + str(de))
            for ap in result3[2]:
                comm.append("set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                            " match application " + str(ap))
            comm.append("set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                        " then permit")
            comm.append("set security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) +
                        " then log session-close")
            comm.append(
                "insert security policies from-zone " + start + " to-zone " + end + " policy " + str(nema) + " after "
                + last)
            pay = int(pay)
            pay += 1
            mas[maxn] = pay
    if result1 == [] and result2 == [] and result3 != []:
        if set(cp1) != set(result3[0]):
            result3[0] = set(cp1) - set(result3[0])
            for so in result3[0]:
                comm.append(
                    "delete security policies from-zone " + start + " to-zone " + end + " policy " + str(name) +
                    " match source-address " + str(so))
        if set(cp2) != set(result3[1]):
            result3[1] = set(cp2) - set(result3[1])
            for de in result3[1]:
                comm.append(
                    "delete security policies from-zone " + start + " to-zone " + end + " policy " + str(name) +
                    " match destination-address " + str(de))
        if set(cp3) != set(result3[2]):
            result3[2] = set(cp3) - set(result3[2])
            for ap in result3[2]:
                comm.append("delete security policies from-zone " + start + " to-zone " + end + " policy " + str(name) +
                            " match application " + str(ap))

    cocc=[]
    cocc=comm+come
    return cocc

















