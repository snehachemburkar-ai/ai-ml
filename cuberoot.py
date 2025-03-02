#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 20:29:57 2025

@author: schemburkar
"""


def findCubeRoot(x):
    cuberoot=x**(1/3)
    print("Maths Cuberoot of ",x,"is ",cuberoot)


def findcbrt(left,right,num):
     #print(f"value of {left}  {right}")
     cb=(left+right)/2
     diff=abs(cb*cb*cb-num)
     #print(f"Value of {diff}")
     if(diff<=0.0000001):
       print(f"Cuberoot of {num} :", cb)
     else:  
        if((cb*cb*cb)>num):
          right=cb
        else:
          left=cb
        findcbrt(left,right,num)       
     

num=55
findCubeRoot(num)
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
findcbrt(left,right,num)     
