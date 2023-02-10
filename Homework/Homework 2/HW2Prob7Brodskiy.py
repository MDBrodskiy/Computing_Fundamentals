"""
 * ===============================================================
 *
 *       Filename:  HW2Prob7Brodskiy.py
 *       Assignment: Homework 2 Problem 7
 *       Title: Tuple Manipulations
 *
 *    Description:  Performs various manipulations of tuple lists containing hardware items
 *
 *        Version:  1.0
 *        Created:  02/09/2023
 *       Revision:  N/A
 *         Python:  Python 3.9.2
 *
 *         Author:  M.Brodskiy
 *
 * ===============================================================
""" 

import operator

# Define tuple list
items = [("38", "Electric sander", 11, 24.09), ("42", "Power saw", 18, 89.82), ("77", "Sledge hammer", 7, 57.98), ("7", "Hammer", 76, 11.99)]

# Part a
items_sorted = sorted(items, key=operator.itemgetter(1))
print(items_sorted)

# Part b
desc_and_quant = []
for i in items:
    desc_and_quant.append((i[1], i[2]))

desc_and_quant = sorted(desc_and_quant, key=operator.itemgetter(1))
print(desc_and_quant)

# Part c
desc_and_val = []
for i in items:
    desc_and_val.append((i[1], i[2] * i[3]))

desc_and_val = sorted(desc_and_val, key=operator.itemgetter(1))[::-1]
print(desc_and_val)

# Part d
for i in desc_and_val:
    if i[1] > 1000 or i[1] < 200:
        desc_and_val.pop(desc_and_val.index(i))
print(desc_and_val)

# Part e
sum = 0
for i in desc_and_val:
    sum += i[1]
