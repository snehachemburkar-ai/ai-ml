#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 20:10:56 2025

@author: schemburkar
"""

#division without divide
def divide(divident,divisor,quo):
    print(divident,divisor)
    if(divident<divisor):
        return 0,divident,quo
    elif(divident==divisor):
        quo+=1
        return 1,0,quo
    else:
        quo+=1
        return divide(divident-divisor,divisor,quo)
 
quotient=0    
val,reminder,quotient=divide(104,5,0)
print("Quotient", quotient, "  Reminder", reminder)