#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 21:13:35 2025

@author: schemburkar
"""




def findAbsError(x,y,m,c):
    l=len(y)
    for i in range (l):
       y1=m * x[i]-c
       #print("Actual and Calculated",y[i], y1)
       err=y1-y[i]
       err+=abs(err)
    abs_err=err/len(y)
    print("Absolute error",abs_err )
    return abs_err

x=[10,40,80]
y=[8,12,18]   
delta=0.01
m=1
c=2
error=0.01

def findOptimalModel(error,m,c):
  abs_err=findAbsError(x,y,m,c)

  while(abs_err>0.1):
     if(abs_err > error):
        m=m-delta
        c=c-delta
     else:
        m=m+delta
        c=c+delta
        error=abs_err
     abs_err=findAbsError(x,y,m,c)
     print("Previous error and Current error",error, abs_err)

  return [abs_err,m,c] 
    


val=findOptimalModel(error,m,c )
print("Lowest absolute error",val[0])
print("Optimal m and c : ",val[1],val[2])
   
    