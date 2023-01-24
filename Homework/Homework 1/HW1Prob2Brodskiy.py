"""
 * ===============================================================
 *
 *       Filename:  HW1Prob2Brodskiy.py
 *       Assignment: Homework 1 Problem 2
 *       Title: Palindrome Verification
 *
 *    Description:  Takes in a number and determines whether it is a palindrome
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

num = int(input("Enter a number: "))
length = len(str(num))
revNum = ""
newNum = num

for i in range(length):
    revNum += str(newNum % 10)
    newNum = (newNum // 10) 

revNum = int(revNum)

print(num, "is a palindrome!") if (num == revNum) else print(num, "and", revNum, "are not the same, so", num, "is not a palindrome.")
