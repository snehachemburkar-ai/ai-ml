#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 22:35:55 2025

@author: schemburkar
"""
import math

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

base=2
def convertBinarytoDecimal(b):
    result=0
    i=1
    for i in range (len(b)):
        result=result+(int(b[i])*(math.pow(2,i)))
    print("Decimal equivalent :",result)    
    
convertBinarytoDecimal("1001")
print(0b1001)


def addBinanryNumbers(x,y):
    result=""
    res=0
    carry=0
    while(x>0 or y>0 or carry>0):
         carry=0
         if(x>0 and y>0):
            res=x%2+y%2+res
            x=x//10
            y=y//10
         elif(x>0 and y==0):
             res=x%2+res
             x=x//10
         elif(y>0 and x==0):
             res=y%2+res
             y=y//10
         if(res>=2):
              carry=1
              res=res%2    
         print("res",res) 
         result=str(res)+result
         res=carry
         print("x=",x)
         print("y=",y)
        
    print("Addition of two binary numbers:",result)
    
addBinanryNumbers(111,11)
print("binary addition",bin(0b111+0b11))