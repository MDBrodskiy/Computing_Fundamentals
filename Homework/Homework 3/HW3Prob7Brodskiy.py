"""
 * ===============================================================
 *
 *       Filename:  HW3Prob7Brodskiy.py
 *       Assignment: Homework 3 Problem 7
 *       Title: Median and Mode Finder
 *
 *    Description:  Uses numpy to find median and mode on an array
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

def findMode(mat):

    freq_list = {}
    mostFreq = 0

    for i in mat:
        for j in i:
            if j not in freq_list:
                freq_list[j] = 1
            else:
                freq_list[j] += 1

    for i in freq_list:
        if freq_list[i] > mostFreq:
            mostFreq = freq_list[i]

    for i in freq_list.keys():
        if freq_list[i] == mostFreq:
            return i

def findMed(mat, axis = 0):
    
    medians = []
    count = 0

    if axis == 0:
        for i in mat:
            i.sort()
            width = len(i)
            if width % 2 == 0:
                medians.append((i[(width // 2) - 1] + i[(width // 2)]) / 2)
                count += 1
            else:
                medians.append(i[width // 2])
                count += 1
    else:
        mat = mat.T
        for i in mat:
            i.sort()
            width = len(i)
            if width % 2 == 0:
                medians.append((i[(width // 2) - 1]  + i[(width // 2)]) / 2)
                count += 1
            else:
                medians.append(i[width // 2])
                count += 1

    return medians

arr1 = np.array([[3, 4, 2, 2], [7, 2, 3, 5], [6, 6, 6, 2]])
arr2 = np.array([[4, 5, 2], [3, 9, 9], [6, 8, 6], [0, 1, 1], [9, 2, 9]])
arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 1, 1]])

print(arr1)
print("Median (rows):", findMed(arr1, 0))
print("Median (cols):", findMed(arr1, 1))
print("Mode:", findMode(arr1))
print(arr2)
print("Median (rows):", findMed(arr2, 0))
print("Median (cols):", findMed(arr2, 1))
print("Mode:", findMode(arr2))
print(arr3)
print("Median (rows):", findMed(arr3, 0))
print("Median (cols):", findMed(arr3, 1))
print("Mode:", findMode(arr3))
