#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 15:06:49 2025

@author: schemburkar
"""
import math
def findHypotehneus(adjs,opps):
    hypotheneus= math.sqrt(math.pow(adjs,2)+math.pow(opps,2))
    print("Hypotheneus :",hypotheneus)
  
    
def findHypotehneuswithoutSqrt(adjs,opps):
      hypotheneusSq=(math.pow(adjs,2)+math.pow(opps,2))
      hypotheneus=hypotheneusSq**0.5
      print("Hypotheneus :",hypotheneus)
    
findHypotehneus(2,3)
findHypotehneus(28,33)
findHypotehneuswithoutSqrt(2,3)
findHypotehneuswithoutSqrt(28,33)