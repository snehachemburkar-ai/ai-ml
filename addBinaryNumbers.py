#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:40:49 2025

@author: schemburkar
"""

carry=0
result=""

def add(x,y):
    global carry
    if(x.isnumeric() and y.isnumeric()):
        z=int(x)+int(y)
    else:
        z=findnum(x)+findnum(y)
        print("Sum=",z)
        if(z>9 and z<13):
            z=base13code(z)
        else:    
            z=z%10
            carry=z//10
    return z



def addition(x,y):
    global carry
    res=0
    i=1
    while(i<len(x) or i<len(y)):
           res=add(x[i],y[i])
           result[i]=result[i]+res+carry
           i=i+1
    print("Additon of ",x,y,"is ",result)

    
def findnum(num):
     if(num=='A'):
        num=10
     elif(num=='B'):
         num=11
     elif(num=='C'):
         num=12
     return int(num)
       
       
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
    

addition('20','34')
#addition('2B','3C')