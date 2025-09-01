#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 16:57:45 2025

@author: schemburkar
"""

#compute Standard deviation

import math
#Root mean square value
val=[]
def compute_rmse(actual,predicted):
    l=len(actual)
    avg=0
    for i in range (0,l):
        val=actual[i]-predicted[i]
        #print(i, val)
        avg=avg+val**2   
    mean=(avg/l)  
    rsme=math.sqrt(mean)       
    return rsme

actual=[3,1,7,9]
predicted=[5,2,9,7]

print("Root mean square value=",compute_rmse(actual,predicted))