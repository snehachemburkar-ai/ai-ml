#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 20:29:17 2025

@author: schemburkar
"""

#Solve sudoko

def find_first_blank_position(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col
    return None

def find_numbers_to_fill(sudoku, i, j):
    row_vals = set(sudoku[i])
    col_vals = set(sudoku[x][j] for x in range(9))
    box_row, box_col = 3 * (i // 3), 3 * (j // 3)
    box_vals = set(
        sudoku[r][c]
        for r in range(box_row, box_row + 3)
        for c in range(box_col, box_col + 3)
    )
    return set(range(1, 10)) - row_vals - col_vals - box_vals

def solve(sudoku):
    pos = find_first_blank_position(sudoku)
    if pos is None:
        print(sudoku)
        return True
    i, j = pos
    candidates = find_numbers_to_fill(sudoku, i, j)
    for candidate in candidates:
        sudoku[i][j] = candidate
        if solve(sudoku):
            return True
        sudoku[i][j] = 0
    return False