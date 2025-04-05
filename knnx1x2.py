#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 16:32:02 2025

@author: schemburkar
"""

data = [[1, 1, 10], [1,2, 20], [2, 1, 30], [2, 2, 40]]
test_data=[[1, 1],[1.1, 1.9],[2, 2.3],[3, 1.5]]



    
def knn(data,test_data):
        diff=abs(data[0][0]-test_data[0])
        #print("diff",diff)
        diff1=abs(data[0][1]-test_data[1])
        #print("diff1",diff1)
        index1=0
        for i in range (1,len(data)):
            if(diff>(data[i][0]-test_data[0]) and diff1>(data[i][1]-test_data[1])):
                      index1=i
        near_value=data[index1][2]
        print("KNN value by approx",near_value) 
        return(near_value)

for i in range (len(test_data)-1):
    print("Test data",test_data[i])
    knn(data,test_data[i]) 
