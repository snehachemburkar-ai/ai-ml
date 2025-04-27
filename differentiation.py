#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 22:56:17 2025

@author: schemburkar
"""
from math import * 
#Differentiation Derivatives

def differentiation(f,x):
    x1=x
    y1=f(x1)
    delta=1e-8
    x2=x+delta
    y2=f(x2)
    derivative=(y2-y1)/(x2-x1)
    return derivative

def sqr(x):
    return pow(x,2)


    

print(differentiation(sqr,25))
print(differentiation(sin,25)) 

def partialDerivative(f,args,index):
    y1=f(args)
    delta=1e-8
    args[index]=args[index]+delta
    y2=f(args)
    derivative=(y2-y1)/delta
    return derivative

def sqr(arr):
    for i in arr:
     return pow(i,2)

print(partialDerivative(sqr,[2.3],0))