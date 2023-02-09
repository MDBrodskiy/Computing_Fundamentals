"""
 * ===============================================================
 *
 *       Filename:  HW2Prob2Brodskiy.py
 *       Assignment: Homework 2 Problem 2
 *       Title: Sum_Product
 *
 *    Description:  Uses function Sum_Product to either sum or multiply all elements in a list
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

def sum_product(in_list, in_mode = 0):
    sum_or_product = 1
    if in_mode == 0:
        for i in in_list:
            sum_or_product += i
        return (min(in_list), sum_or_product - 1)
    else:
        for i in in_list:
            sum_or_product *= i
        return (max(in_list), sum_or_product)
