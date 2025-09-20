#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 20:08:32 2025

@author: schemburkar
"""

#Binary search

def binarySearch(arr,x,left,right):
    mid=(left+right)//2
    #print("left:",left)
    #print("Mid:",mid)
    #print("Right:",right)
    #print("Array value :",arr[mid])
    if(arr[mid]==x):
        print("Found x",x,"in location", mid)
        return mid
    elif(left>=right):
        print("Value not found")
        return -1 
    else:
        if(arr[mid]<x):
            left=mid+1
        else:
            right=mid-1
        return (binarySearch(arr,x,left,right))

    
arr=[-1,0.9,2.9,3.5,5.1,7.7,8.5,9.9,10.3]
print("Binary search:",binarySearch(arr,7.7,0,len(arr)))      
         
    