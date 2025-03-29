#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 20:18:09 2025

@author: schemburkar
"""


arr1=[4,2,3]
arr2=[3,2,4]

def mean_squared_error(actual, predicted):
     diff=0
     n=len(actual)
     for a,b in zip(actual,predicted):
         diff+=(a-b)*(a-b)
     mean_sqr_err=pow(diff,1/2)/n
     print("Mean Square value ",mean_sqr_err)
mean_squared_error(arr1,arr2)     

def mean_absolute_error(actual, predicted):
    abs_err=0
    for a,b in zip(actual,predicted):
        diff=a-b
        if(diff<0):
           diff=-diff
        abs_err+=diff   
    print("Absolute error",abs_err )   
mean_absolute_error(arr1,arr2)
