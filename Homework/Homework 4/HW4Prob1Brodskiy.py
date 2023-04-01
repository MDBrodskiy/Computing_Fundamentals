"""
 * ===============================================================
 *
 *       Filename:  HW4Prob1Brodskiy.py
 *       Assignment: Homework 4 Problem 1
 *       Title: Matrix Common Term Finder
 *
 *    Description:  Takes in a matrix and returns terms common to
 *                  all rows of the matrix
 *
 *        Version:  1.0
 *        Created:  04/01/2023
 *       Revision:  N/A
 *         Python:  Python 3.9.2
 *
 *         Author:  M.Brodskiy
 *
 * ===============================================================
""" 

import numpy as np

def comMatTerms(A):

    uniqMatTerms = np.unique(A)
    comTerms = []

    for uniqVal in uniqMatTerms:

        B = [A == uniqVal]
        addTerm = True

        for row in B:
            for j in row:
                if (True not in j):
                    addTerm = False

        if addTerm:
            comTerms.append(uniqVal)

    return np.array(comTerms)
