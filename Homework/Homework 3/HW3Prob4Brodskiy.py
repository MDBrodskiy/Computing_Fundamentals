"""
 * ===============================================================
 *
 *       Filename:  HW3Prob4Brodskiy.py
 *       Assignment: Homework 3 Problem 4
 *       Title: String metric to imperial converter
 *
 *    Description:  Performs metric to imperial conversion
                    from string phrases
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

def stringCalc(phrase):

    units = [["meter", "gram", "liter", "foot", "pounds", "gallon"], [3.28, .0022, .22, .3048, 453.59, 4.546]]
    tokens = phrase.lower().split()
    (initialUnit, finalUnit) = ("", "")
    initialQuant = 0

    for i in tokens:
        if i in units[0] and finalUnit == "":
            finalUnit = i
        elif i in units[0]:
            initialUnit = i

    initialQuant = tokens[tokens.index(initialUnit) - 1]

    return initialQuant * units[1][units[0].index(finalUnit)]

print(stringCalc(input("Enter conversion phrase: ")))
