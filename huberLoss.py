#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 17:51:56 2025

@author: schemburkar
"""

#calculate huber loss

huberLoss=[]
def compute_huber_loss(y_true, y_pred, delta):
  arr= zip(y_true,y_pred)
  for (a,p)in enumerate(arr):
    print(p[0],  p[1])
    error= p[0]-p[1]
    if(abs(error)>delta):
        loss= 0.5*error**2
    else:
        loss=delta * abs(error) - 0.5 * delta**2    
    huberLoss.append(loss)
  avghuberLoss=sum(huberLoss)/len(huberLoss)
  return avghuberLoss



y_true=[3,7,1,8]
y_pred=[2,4,3,9]
delta=1.5 
print("Huberloss :",compute_huber_loss(y_true, y_pred, delta) )  