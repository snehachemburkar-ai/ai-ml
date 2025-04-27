#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 16:11:59 2025

@author: schemburkar
"""

def findAbsError(x,y,m,c):
    l=len(y)
    for i in range (l):
       y1=m * x[i]-c
       #print("Actual and Calculated",y[i], y1)
       err=y1-y[i]
    sqr_err=pow(err,2)
    print("Squre Error ",sqr_err )
    return sqr_err

x=[10,40,80]
y=[8,12,18]   
delta=0.01
m=1
c=2
error=0.1

def findOptimalModel(error,m,c):
  sqr_err=findAbsError(x,y,m,c)

  while(sqr_err>0.2):
     if(sqr_err > error):
        m=m-delta
        c=-+delta
     else:
        m=m+delta
        c=c+delta
        error=sqr_err
     sqr_err=findAbsError(x,y,m,c)
     print("Previous error and Current error",error, sqr_err)

  return [sqr_err,m,c] 
    


val=findOptimalModel(error,m,c )
print("Lowest mean square error",val[0])
print("Optimal m and c : ",val[1],val[2])