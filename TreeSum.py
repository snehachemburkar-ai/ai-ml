#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 21:05:45 2025

@author: schemburkar
"""

#Sum of tree
# Compute the sum of a tree
#sum_tree([1,2,3]) # 6
#sum_tree([1, [2,3]]) # 6
#sum_tree([1, [2, [3, [4, 5]]]]) # 15


def treeSum(l,sum):
    for i in l:
        print("i=",i)
        if(type(i)==list):
            print("sum=",sum)
            sum=treeSum(i,sum) 
        else :   
            sum=sum+i
    print("Final sum=",sum)   
    return sum    

sum=0
sum=treeSum(([1,[2,3]]),sum)
print(sum)
