"""
 * ===============================================================
 *
 *       Filename:  HW2Prob3Brodskiy.py
 *       Assignment: Homework 2 Problem 3
 *       Title: Palindrome Detector
 *
 *    Description:  Uses function is_palindrome to detect palindromes
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

def is_palindrome(word):
    return word.lower().replace(" ","") == word.lower().replace(" ","")[::-1]

print(is_palindrome("race car"))
print(is_palindrome("test"))
print(is_palindrome("Aya"))
print(is_palindrome("Papaya"))
