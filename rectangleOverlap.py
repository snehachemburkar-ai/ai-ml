#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:37:10 2025

@author: schemburkar
"""
import math
#A rectangle is represented by two opposite corners. Each corner is represented a two number (x, y). 
#Given two rectangles, return True if they are touching or overlapping otherwise return false.
#Let the coordinates of 1st rectangle A(x1, y1), B(x2, y2), 
#coordinated of 2nf rectangle C(x3, y3) and D(x4, y4)


def find_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    base = x2 - x1
    p = y2 - y1
    return math.sqrt(base*base + p * p)

find_distance(rect1,rec2)



def is_overlapping_rect(rect1, rect2):
    p11, p12 = rect1
    p21, p22 = rect2
    return True


print(is_overlapping_rect(((1,2), (3,4)), ((3,4), (5,6))))
print(is_overlapping_rect(((1,-1), (-3,-4)), ((3,4), (5,6))))
