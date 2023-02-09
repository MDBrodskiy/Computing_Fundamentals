"""
 * ===============================================================
 *
 *       Filename:  HW2Prob1Brodskiy.py
 *       Assignment: Homework 2 Problem 1
 *       Title: Temperature Converter
 *
 *    Description:  Uses function c_to_f to print a table of Celsius and Fahrenheit values from -10C to 100C 
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

def c_to_f(fahrenheit):
    return ( 9.0 / 5.0 ) * float(fahrenheit) + 32

print("Celsius\tFahrenheit")
for i in range(-10, 101):
    print(f"{i:.2f}\t{c_to_f(i):.2f}")

