#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 14:51:12 2025

@author: schemburkar
"""

#find content of file using xor operation


def backup(f1,f2):
    bac=""
    f3=[]
    for (a,b) in  zip (f1,f2):
        f3=bin(ord(a)^ord(b))
        bac=bac+f3
        #print(bac)
    return bac

        
f1="I am learning python"
f2="AI/ML is intresting"
backupFile=backup(f1,f2)
print("Backup file content : ",backupFile)
