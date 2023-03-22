"""
 * ===============================================================
 *
 *       Filename:  HW3Prob5Brodskiy.py
 *       Assignment: Homework 3 Problem 5
 *       Title: Array Manipulations
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

A = np.arange(2.0, 19.0, 2).reshape(3, 3)
B = np.arange(9.0, 0.0, -1).reshape(3, 3)

# Part A
print("Element-wise Multiplication:", (A ** 2) * B, sep="\n")
print("Matrix-wise Multiplication:", np.matmul((A ** 2), B), sep="\n")

# Part B
A[B % 3 == 0] = np.sqrt(A[B % 3 == 0])
B[A % 4 == 0] = -B[A % 4 == 0]
print("Element-wise Multiplication:", np.linalg.inv(A) * np.linalg.inv(B), sep="\n")
print("Matrix-wise Multiplication:", np.matmul(np.linalg.inv(A), np.linalg.inv(B)), sep="\n")
