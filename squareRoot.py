#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 22:03:49 2025

@author: schemburkar
Recursive function for Squareroot
"""

#import math

def findSqrt(left,right,num):
     mid=(left+right)/2
     diff=abs(mid*mid- num)
     if(diff<=0.000001):
       print(f"Squareroot of {num} :", mid)
     else:  
        if((mid*mid)>num):
          right=mid
        else:
          left=mid
        findSqrt(left,right,num)       
     

num=4
#print("Squareroot by math lib:",math.sqrt(num))
if(num<=0):
    num=abs(num)
    right=abs(num)
    left=0
elif(num<=1):
   right=1
   left=num
else:
    left=0
    right=num
findSqrt(left,right,num)
