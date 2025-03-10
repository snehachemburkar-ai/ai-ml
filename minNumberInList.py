#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 22:36:19 2025

@author: schemburkar
"""


def minArr(a):
    temp=a[0]
    for i in range (len(a)-1):
        if(a[i]<temp):
            temp=a[i]
    return temp    



def findMin(a):
    a.sort()
    return(a[0])


arr=[77,-25,9,30,14,10,-2]  
print("Minimum elment in array ",minArr(arr) ) 
print("Minimum elment in array by sort ",findMin(arr) ) 