#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 17:45:54 2025

@author: schemburkar
"""



#absolute mean square error
val=[]
def compute_mae(actual,predicted):
    l=len(actual)
    avg=0
    for i in range (l):
        val=actual[i]-predicted[i]
        #print(i, val)
        avg=avg+abs(val)
    absmean=abs(avg/l )   
    return absmean

actual=[3,1,7,9]
predicted=[5,2,9,7]

print("Absolute mean square value=",compute_mae(actual,predicted))