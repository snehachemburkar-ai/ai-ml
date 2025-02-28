#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:15:31 2025

@author: schemburkar
"""

#Print base 13 digits
def base13code(num):
    if(num==10):
       code='A'
    elif(num==11):
        code='B'
    elif(num==12):
        code='C'
    else:
      code=str(num)
    return code

def convert(x):
    number='' 
    while(x>0):
       num=x%13
       #print("num:",num)
       number=base13code(num)+number
       x=x//13    
    return number

def convertDecimaltobase13(x):
    if(x<13):
      code=base13code(x)
    else:
      code=convert(x)
    return code
      
num=0 
for x in range(50):
   print(convertDecimaltobase13(x))
  