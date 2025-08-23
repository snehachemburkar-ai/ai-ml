#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 15:23:44 2025

@author: schemburkar
"""

def multiplication(y,x):
    if(y==1):
       return x
    else:
       x=x+3
       print("x= ",x)
    return multiplication(y-1,x)

print(multiplication(5,3))

def division(divident,divisor,quotient):
    if(divident<=divisor):
       return quotient
    else:
       divident=divident-divisor
       print("quotient= ",quotient)
    return division(divident,divisor,quotient+1)

print(division(15,3,1))