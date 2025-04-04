#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 14:06:12 2025

@author: schemburkar
"""

#Write a function to compute mean of a list of numbers

import math


def findmean(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum/len(arr)

def standardDeviation(arr):
    sd=0
    for i in arr:
        sd+=math.pow((i-mean),2)
    mu=sd/len(arr)   
    return math.pow(mu,0.5)


def findzscore(arr,mean,deviation):
    for i in range (len(arr)-1):
        zscore.insert(i,(arr[i]-mean)/deviation)
        print("Zscore",  arr[i],    zscore[i])
    return zscore


def findOutliers(zscore,arr):
    for i in range (0,len(arr)-1): 
        if(zscore[i]>=2 or zscore[i]<=-2):
           outliers.insert(i,arr[i])
    return outliers


arr=[-10,30,5,36,20,200,22,25,-180,35]

mean =findmean(arr)
print("Mean =", mean)
deviation=standardDeviation(arr)
print("Standard deviation  ",deviation )
zscore=[]
zscore=findzscore(arr,mean,deviation)

outliers=[]
outliers=findOutliers(zscore,arr)
print("Outliers in datapoint are ",outliers)