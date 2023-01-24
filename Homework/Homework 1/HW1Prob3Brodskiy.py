"""
 * ===============================================================
 *
 *       Filename:  HW1Prob3Brodskiy.py
 *       Assignment: Homework 1 Problem 3
 *       Title: Pythagorean Triple Finder
 *
 *    Description:  Prints all Pythagorean triples with side lengths less than 1000
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

for i in range(1, 1000):
    for j in range(i, 1000):
        for k in range(j, 1000):
            if (i ** 2 + j ** 2 == k ** 2):
                print(f"({i}, {j}, {k})")
