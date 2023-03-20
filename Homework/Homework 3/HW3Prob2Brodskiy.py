"""
 * ===============================================================
 *
 *       Filename:  HW3Prob2Brodskiy.py
 *       Assignment: Homework 3 Problem 2
 *       Title: 5-to-3 Letter Converter
 *
 *    Description:  Converts a 5 Letter Word to each 3 Letter Subcomponent
 *
 *        Version:  1.0
 *        Created:  03/19/2023
 *       Revision:  N/A
 *         Python:  Python 3.9.2
 *
 *         Author:  M.Brodskiy
 *
 * ===============================================================
""" 
import itertools

def fiveToThree(word):
    allCombos = []
    for i in itertools.combinations(word, 3):
        if (i[0] + i[1] + i[2]) not in allCombos:
            allCombos.append(i[0] + i[1] + i[2])
    return allCombos
