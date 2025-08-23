#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 16:11:00 2025

@author: schemburkar
"""

#Tower of Hanoi problem
def towerOfHanoi(disk):
    diskno=len(disk)
    print("Number of disk",diskno)
    if(diskno<=3):
       move(diskno,disk[0],disk[1],disk[2])
    else:
       for i in range (diskno-1):
            move(diskno,disk[i],disk[i+1],disk[i+2])


def move(diskno,src,bet,des):
    print("Move ",src, "to", bet)
    print("Move ",src, "to",des)
    print("Move ",bet ,"to", des)
    

disk=['a','b','c','d']
#towerOfHanoi(3,'a','b','c')
towerOfHanoi(disk)