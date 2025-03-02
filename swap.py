#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 20:08:20 2025

@author: schemburkar
"""

def swap(x,y):
    print("Before swap x:",x,"y:",y)
    temp=x
    x=y
    y=temp
    print("After Swap using temporary variable x:",x,"y:",y)
    
swap(-10, 20)

def swapwithoutThirdvariable(x,y):
    print("Before swap x:",x,"y:",y)
    y=x+y
    x=y-x
    y=y-x
    print("After Swap using mathematicla logic x:",x,"y:",y)

swapwithoutThirdvariable(20,-5)

def pythonSwap(x,y):
    print("Before swap x:",x,"y:",y)
    x,y=y,x
    print(x,y)
    print("After Swap using python inbuild function x:",x,"y:",y)
    
pythonSwap(-90,80)

def stringSwap(x,y):
    print("Before swap x:",x,"y:",y)
    x=x+"_"+y
    y,x=x.split("_")
    print("After Swapusing string  x:",x,"y:",y)
    
stringSwap("35","-25")


def swapZor(x,y):
        print("Before swap x:",x,"y:",y)
        y=x^y
        x=y^x
        y=y^x
        print("After Swap  using Zor x:",x,"y:",y)
swapZor(35,-25)