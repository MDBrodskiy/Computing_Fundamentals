"""
 * ===============================================================
 *
 *       Filename:  HW3Prob6Brodskiy.py
 *       Assignment: Homework 3 Problem 6
 *       Title: Array Diagonal Printer
 *
 *    Description:  Performs various array arithmetic
 *
 *        Version:  1.0
 *        Created:  03/21/2023
 *       Revision:  N/A
 *         Python:  Python 3.9.2
 *
 *         Author:  M.Brodskiy
 *
 * ===============================================================
""" 

import numpy as np

def getDiagonals(mat):
    diagonals = [reversed(mat).diagonal(i) for i in range(-mat.shape[0]+1,mat.shape[1], -1)]
    diagonals.extend(mat.diagonal(i) for i in range(mat.shape[1]-1,-mat.shape[0],-1))
    return diagonals

m = np.random.randint(1, 9)
n = np.random.randint(1, 9)

mat = np.linspace(1, 100, m * n, dtype=int).reshape(m, n)

print("Original Matrix:\n", mat)
print("Diagonals:\n")
diag = getDiagonals(mat)
for i in diag:
    for j in i:
        print(j, end=' ')
    print('\n')
