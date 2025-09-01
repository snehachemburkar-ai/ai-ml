#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 09:06:59 2025

@author: schemburkar
"""

#: Find the smallest value of an expression such as y = 10*x^2 - 35x + 2
# Further, write code to solve any such expression.

x=0
delta=0.1
prevY=0  
def smallValExpression(x,prevY):
    y=(10*x**2)-(35*x)+2
    print("previous exprsssion value ",prevY,"New value", y)  
    if(y<0):
       print("End recursion")
       return x,y
    elif(y>prevY):
       x=x-delta
    else:
        x=x+delta
    prevY=y
    print("Call recursion")   
    x=smallValExpression(x,prevY)
    return x,y
    
smallVal=smallValExpression(x,prevY)
print("Smallest value of expression",smallVal[1], "for value of x",smallVal[0])