#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 17:25:49 2025

@author: schemburkar
"""

arr=[2,5,8,6,4,7]
res=[]
def findMinMaxscaling(arr):
    mini=min(arr)
    maxi=max(arr)
    for i in range (0,len(arr)-1):
        val=(arr[i]-mini)/(maxi-mini)
        res.insert(i, val)
    print("Mix max scaling values" , res)
    
findMinMaxscaling(arr)
