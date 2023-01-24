"""
 * ===============================================================
 *
 *       Filename:  HW1Prob5Brodskiy.py
 *       Assignment: Homework 1 Problem 5
 *       Title: Approximating Pi
 *
 *    Description:  Approximates pi using a Maclaurin series up to ten terms
 *
 *        Version:  1.0
 *        Created:  01/24/2023
 *       Revision:  N/A
 *         Python:  Python 3.9.2
 *
 *         Author:  M.Brodskiy
 *
 * ===============================================================
""" 

sum = 1
cur_term = 1

for i in range(1, 11):
    print(f"{i}-Term: {4 * sum:.6f}")
    cur_term *= -((2 * i - 1) / (2 * i + 1))
    sum += cur_term
