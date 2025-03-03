#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 22:35:55 2025

@author: schemburkar
"""

def convertDecimaltoBinary(n):
    result=""
    while(n>=1):
      b=n%2
      n=n//2
      result=result+str(b)
    result=result[::-1]
    print("Binary number ",result)
    

convertDecimaltoBinary(8)
print("Maths binary",bin(8))