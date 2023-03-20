"""
 * ===============================================================
 *
 *       Filename:  HW3Prob1Brodskiy.py
 *       Assignment: Homework 3 Problem 1
 *       Title: Pig Latin Converter
 *
 *    Description:  Translates English to pig latin
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

def pigLatinConv(tokens):

    vowels = ['a', 'e', 'i', 'o', 'u']

    print("In pig latin, this is:")
    for i in tokens:
        if i[0] in vowels:
            print(i + "ay",end=" ")
        else:
            print(i[1:] + i[0] + "ay",end=" ")

pigLatinConv(input("Please Enter an English Phrase: ").split())
