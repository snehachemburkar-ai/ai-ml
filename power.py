#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 22:24:46 2025

@author: schemburkar
"""

import math

def powerofNum(a,n):
    po=1
    if(n!=0):
      for i in range(n):
          po=po*a
    print(f"Power of {a} : {po}")
    

powerofNum(3,4)
print(math.pow(3,4))