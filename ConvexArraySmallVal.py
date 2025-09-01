#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 08:38:28 2025

@author: schemburkar
"""

#Find the smallest value of a convex arra which first decreases and then increases:
  #arr = [10, 9, 8, 6.5, 4.1, 3.2, 2, 4, 4.5, 6] Ans: 2
  
  
arr = [10, 9, 8, 6.5, 4.1, 3.2,0,-4.5,2,4,5, 6,10]

def binarySearch(low,mid,high):
    mid=(low+high)//2
    print("Mid ",mid)
    smallVal=arr[mid]
    while(low<high):
       if(arr[mid]<arr[mid-1] and arr[mid]<arr[mid+1]):
          smallVal=arr[mid]
       if(arr[mid]>arr[mid+1]):
         high=mid
       else:
         low=mid+1
       print(low,mid,high)
   
    print("Smallest value",smallVal)
    return smallVal

 
    
    

def findSmallestValue(arr):
    low=0
    high=len(arr)-1
    mid=low+high//2
    val=binarySearch(low,mid,high)
    print("Smallest value",val)
    
findSmallestValue(arr)    
