#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 20:45:13 2025

@author: schemburkar
"""

#Flatenning of List

def flatenl(l):
    flatlist=[]
    if(len(l)==0):
        return l
    for i in l:
        print("i=",i)
        if(type(i)==list):
            #print("i=",i)
            flatlist.extend(flatenl(i))
        else:
            flatlist.append(i)
        print("FlatList :" ,flatlist)    
    return flatlist    
        
f=flatenl([1,[2,3],4,[5,6,[7,8,9]]]) 
print(f)          