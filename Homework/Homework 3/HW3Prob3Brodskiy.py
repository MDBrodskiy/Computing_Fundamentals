"""
 * ===============================================================
 *
 *       Filename:  HW3Prob3Brodskiy.py
 *       Assignment: Homework 3 Problem 3
 *       Title: String Calculator
 *
 *    Description:  Performs single-digit arithmetic from strings
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

    tokens = phrase.lower().split()
    numbers = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    num1 = numbers[tokens[0]]
    num2 = numbers[tokens[-1]]

    if len(tokens) == 3:
        if tokens[1] == "plus":
            return num1 + num2
        elif tokens[1] == "times":
            return num1 * num2
        elif tokens[1] == "minus":
            return num1 - num2
    elif len(tokens == 4):
        if tokens[1] + " " + tokens[2] == "divided by":
            return num1 / num2
        elif tokens[1] + " " + tokens[2] == "raised to":
            return num1 ** num2

print(stringCalc(input("Enter calculator phrase: ")))
