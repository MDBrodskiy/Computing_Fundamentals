"""
 * ===============================================================
 *
 *       Filename:  HW1Prob1Brodskiy.py
 *       Assignment: Homework 1 Problem 1
 *       Title: MPG Tracker
 *
 *    Description:  Takes in miles driven and gallons used until a negative number is entered, then outputs an mpg value
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

galUsed = 0
milDriven = 0
sumMiles = 0
sumGal = 0

while 1 != 2:
    galUsed = float(input("Enter the number of gallons used (any negative number to end): "))

    if galUsed < 0: 
        break

    milDriven = float(input("Enter the number of miles driven: "))
    print(f"The miles/gallon for this tank was {milDriven / galUsed:.6f}.")
    sumMiles += milDriven
    sumGal += galUsed

print(f"The overall average miles/gallon for the above tankfuls was {sumMiles / sumGal:6f}.")
