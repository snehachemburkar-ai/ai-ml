#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 20:29:57 2025

@author: schemburkar
"""
import math

def findCubeRoot(x):
    cuberoot=x**(1/3)
    print("Cuberoot of ",x,"is ",cuberoot)
    print("Cuberoot using Math",math.cbrt(x))
    
findCubeRoot(8)
findCubeRoot(27)
findCubeRoot(333)
findCubeRoot(225)