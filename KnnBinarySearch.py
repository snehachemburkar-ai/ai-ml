#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 13:42:16 2025

@author: schemburkar
"""

train_data = [[1,10], [2, 20], [3, 30],[6, 50],[8, 80] ,[10, 110]]


test_data=[[3,4], [9, 100], [5, 55]]
   

def binarySearch(data,low,high,x):
    index=0
    mid=low+high//2
    print(low,  mid,  high)
    diff=abs(data[low][0]-x)
    val=abs(data[mid][0]-x)
    print("diff val ",diff, val)
    while(mid!=high or mid!=low):
      if(diff > val):
        diff=data[mid]
        index=mid
      if(data[mid]<data[low]):
        low=mid
      else:
        high=mid 
      mid=low+high//2
      print(low,  mid,  high)
    return index  
    
diff=[]
def knn1(data, x):
    index= binarySearch(train_data,0,len(data),x)
    print("Index",index)
    near_value=data[index][1]  
    print("KNN value by approx",near_value) 
    return(near_value)

    
#knn1(train_data,1) 
#knn1(train_data,1.3) 
#knn1(train_data,9) 
l=len(test_data)
err=0
for i in range (l):
      predictedValue=knn1(train_data,test_data[i][0])
      print("Predicted value for ",test_data[i][0],  predictedValue)
      err=predictedValue-test_data[i][1]
      mean_sqr=err*err
mean_sqr_err=pow(mean_sqr,1/2)/l
print("Mean Square value ",mean_sqr_err)

abs_err=abs(err)/l
print("Absolute error",abs_err )   