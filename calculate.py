#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 20:27:52 2025

@author: schemburkar
"""

def mycalc(parameter):
    print(parameter)
    print(type(parameter))
    if type(parameter) is not list:
        return parameter
      
    exp = parameter[0]
    print(exp)
    
    if exp =='+':
        sum = 0
        for a in parameter[1:]:
            print(sum)
            if (type(a) is not list):
                sum = sum+a
            else: 
                sum = sum + mycalc(a)
        return sum
    if exp =='*':
        mult = 1
        for a in parameter[1:]:
            print(mult)
            if (type(a) is not list):
                mult = mult*a
            else: 
                mult = mult*mycalc(a)
        return mult
    if exp == '-':
        sub=0
        for a in parameter[1:]:
            print(sub)
            if(type(a) is not list):
                sub=a-sub
            else:
                sub=mycalc(a)-sub           
        return -sub
    if exp == '/':
        div=1
        mul=1
        for a in parameter[1:]:
            print(div)
            if(type(a) is not list):
                div=div*(a**mul)
                mul=mul*-1
            else:
                div=div/mycalc(a)
                mul=mul*-1
        return div
    if exp=='^':
        if type(parameter[1])!=list:
            powe=parameter[1]
        else :
            powe = mycalc(parameter[1])
        if type(parameter[2])!=list:
            raise_1=parameter[2]
        else :
            raise_1 = mycalc(parameter[2])
        
        return powe**raise_1
    if exp=='log':
        import math
        print(type(parameter[1]),parameter[1])
        if (type(parameter[1]) is list):
            print("calling")
            return math.log10(mycalc(parameter[1]))
        else:
            loge=math.log10(parameter[1])
            return loge