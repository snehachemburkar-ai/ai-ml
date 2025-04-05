#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 22:23:00 2025

@author: schemburkar
"""


#Write a function to print all possible numbers of length n where each digit could go from 0 to m-1

#import math 
def generateCombination1(n,m):
     res=list(range(0,m))
     print(res) 
     #per=math.factorial(n)
     for i in range (n):
         for j in range (m):
             temp=res[i]
             res[i]=res[j]
             res[j]=temp
             print(res)
     

generateCombination1(4,5)