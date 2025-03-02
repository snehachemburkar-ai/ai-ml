#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 22:03:49 2025

@author: schemburkar
Recursive function for Squareroot
"""



def findSqrt(left,right,num):
     mid=(left+right)/2
     diff=abs(mid*mid-num)
     if(diff<=0.00001):
       print(f"Squareroot of {num} :", mid)
     else:  
        if((mid*mid)>num):
          right=mid
        else:
          left=mid
        findSqrt(left,right,num)       
     

num=55
if(num>0):
   right=num
   left=0
else:
    left=num
    right=0
findSqrt(left,right,num)
