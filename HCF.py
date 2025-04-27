#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 18:46:27 2025

@author: schemburkar
"""
import math


def factors(n):
     fac=[]
     while((n>=1):
        for i in range (2,int(math.sqrt(n))+1):
            if(n % i==0):
               print(n,i)
               fac.append(i)
               break
               n=n//i
     fac.append(n)   
     return fac




def hcf(x,y):
    #h=1
    fac1=factors(x)
    print("Factors:", fac1)
    fac2=factors(y)
    print("Factors:", fac2)
   
hcf(8,9)