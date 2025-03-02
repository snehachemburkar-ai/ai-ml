#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 20:57:02 2025

@author: schemburkar
"""

   
    
arr=[0,1,2,3,4]
temp=arr[0]
for i in range(len(arr)-1):
     arr[i]=arr[i+1]
arr[len(arr)-1]=temp
print(arr)