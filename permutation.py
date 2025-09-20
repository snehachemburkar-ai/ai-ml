#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 21:12:58 2025

@author: schemburkar
"""

#permutation

def permute(s):
    if len(s) == 1:
        return [s]
    first_letter = s[0]
    remaining = s[1:]
    previous = permute(remaining)
    result = []
    for p in previous:
        for i in range(len(p) + 1):
            new_word = p[:i] + first_letter + p[i:]
            result.append(new_word)
    return result


import math

def permutation(str,result):
      l=len(str)
      if(l==1):
       return(str)
      else:
        while(len(result)<math.factorial(l)): 
          for i in range (l):
           
            for j in range (l):
                if(i==j):
                   break
                start = str[j]
                new=start+str[:j]+str[j+1:]  
                result.append(new)
                str=new  
        #print(result)
      return(result)      

#rel1=permute('abcd') 
#print("Result by 1st Algo:", rel1)
result=[]
rel2=permutation("abcd",result) 
print("Result by 2nd Algo:", rel2)
#if(rel1==rel2):
#    print("Both algo are correct")