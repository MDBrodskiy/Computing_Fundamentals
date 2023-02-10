"""
 * ===============================================================
 *
 *       Filename:  HW2Prob5Brodskiy.py
 *       Assignment: Homework 2 Problem 5
 *       Title: The Sieve of Eratosthenes
 *
 *    Description:  Finds prime numbers through the use of a boolean list
 *
 *        Version:  1.0
 *        Created:  02/10/2023
 *       Revision:  N/A
 *         Python:  Python 3.9.2
 *
 *         Author:  M.Brodskiy
 *
 * ===============================================================
""" 

def Sieve_of_Eratosthenes(K):
    list_of_primes = [True for i in range(K + 1)]
    list_of_primes[0], list_of_primes[1] = False, False

    index = 2
    while index ** 2 <= K:
        if list_of_primes[index]:
            for j in range(index ** 2, K + 1, index):
                list_of_primes[j] = False
        index += 1

    return list_of_primes

