# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
print("Math log ", math.log10(528))


num=528
right=float(len(str(num))) 
left=right-1

#findlog recursive function

def findlog(left,right):
  print("Left of number:",left)
  print("right of number:",right)
  mid=(left+right)/2
  print("Mid ", mid)
  result=10**mid
  print("result ", result)
  if(result>num):
      right=mid
  else:
    left=mid
  print("Left of number:",left)
  print("right of number:",right)
  diff=abs(result-num)
  if(diff>=0.0001):
      print("Recusion")
      findlog(left,right)
  else:
    print("Log of number:" ,mid)
    
findlog(left,right)

