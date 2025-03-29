#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 14:59:24 2025

@author: schemburkar
"""


train_data = [[1,10], [2, 20], [3, 30], [10, 110]]
test_data=[[3,4], [9, 100], [5, 55]]
   


def knn1(data, x):
    diff=abs(data[0][0]-x)
    for i in range (1,len(data)):
        if(diff>abs(data[i][0]-x)):
            index=i
        else:
            index=0  
    near_value=data[index][1]  
    print("KNN value by approx",near_value) 
    return(near_value)

#knn1(train_data,1) 
#knn1(train_data,1.3) 
#knn1(train_data,9) 
l=len(test_data)
diff=0
for i in range (l):
      predictedValue=knn1(train_data,test_data[i][0])
      print("Predicted value :",predictedValue)
      diff=predictedValue-test_data[i][1]
      mean_sqr=diff*diff
mean_sqr_err=pow(mean_sqr,1/2)/l
print("Mean Square value ",mean_sqr_err)

abs_err=abs(diff)/l
print("Absolute error",abs_err )   
