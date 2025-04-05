#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 16:28:13 2025

@author: schemburkar
"""

from matplotlib import pyplot as plt
img = [
    [255, 120],
    [40, 0]
]

plt.imshow(img, cmap='gray')
img = [
    [[255,255,255], [255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 0, 255],[0,0,0]]
]

plt.imshow(img)