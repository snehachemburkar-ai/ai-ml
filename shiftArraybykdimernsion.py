#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 21:52:59 2025

@author: schemburkar
"""

# Rotate an array by kth position

def rotateArray(arr,k):
    result=arr[k:]
    for e in arr[:k]:
        result.append(e)
    return result
    

def rotateArrayShift(arr,k):
    result=arr[k:]
    result=result+arr[:k]
    return result    

arr=[1,2,3,4,5,6,7]
print(rotateArray(arr,3))
print(rotateArrayShift(arr,3))

def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def rotateArrayReverse(arr,k):
    reverse(arr,0,k-1)
    reverse(arr,k,len(arr)-1)
    reverse(arr,0,len(arr)-1)
    
def rotateArrayXor(arr,k):
     temp=arr[k-1]
     for j in range(k):
         for i in range(len(arr)-1):   
                arr[i+1]=arr[i]^arr[i+1]     
                arr[i]=arr[i+1]^arr[i]
                arr[i+1]=arr[i+1]^ arr[i]
     arr[len(arr)-1]=temp
     return arr
 
arrRotate=rotateArrayXor([1,2,3,4,5,6,7],3)
print(arrRotate)