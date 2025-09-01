#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 21:01:05 2025

@author: schemburkar
"""

def is_palindrome(arr, start, end):
    #print(f" arr : {arr}, {start}, {end}")
    if start >= end:
        return True
    if arr[start] == arr[end]:
        return is_palindrome(arr, start+1, end-1)
    return False

print(is_palindrome("mihir",0,4))