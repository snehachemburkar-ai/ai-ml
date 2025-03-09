#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 14:51:12 2025

@author: schemburkar
"""

#find content of file using xor operation


def xorArray(a1,a2,a3):
    fArr=[]
    for (a,b,c) in  zip (a1,a2,a3):
       res=a^b^c
    fArr.append(res)
    return fArr

a1=[5,3,7]
a2=[2,9,0]
a3=[1,4,3]  
result=xorArray(a1,a2,a3)
print("Xor of array : ",result)
xorResult=[xorArray(a1,a2,a3),xorArray(a2,a1,a3),xorArray(a3,a2,a1)]   
print("Array of Xor array : ",xorResult)


