#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 14:59:24 2025

@author: schemburkar
"""


train_data = [[1,10], [2, 20], [3, 30], [10, 110]]

def knn(data, x):
    for i in range (len(data)-1):
        if(abs(data[i][0]-x)<=0.99):
             return(data[i][1])
         
nearest_value=knn(train_data,3)
print("KNN value ",nearest_value )    


def knn1(data, x):
    for i in range (len(data)-1):
        diff1=abs(data[i][0]-x)
        diff2=abs(data[i+1][0]-x)
    if(diff1<diff2):
         return(data[i][1])
    else:
         return(data[i+1][1])     
         
near_value=knn1(train_data,8)
print("KNN value ",near_value )   