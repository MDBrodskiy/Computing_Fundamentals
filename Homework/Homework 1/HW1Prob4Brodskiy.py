"""
 * ===============================================================
 *
 *       Filename:  HW1Prob4Brodskiy.py
 *       Assignment: Homework 1 Problem 4
 *       Title: Guessing Game
 *
 *    Description:  Randomly generates a number from 0-1000, having the player try to guess it with hints
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

import random

num = int(1000 * random.random())
playAgain = -1

guess = int(input("Guess my number between 1 and 1000 with the fewest possible guesses: "))

while playAgain != 0:
    if guess > num:
        guess = int(input("Too high! Try again: "))
    elif guess < num:
        guess = int(input("Too low! Try again: "))
    else:
        print("Congratulations. You guessed the number!")
        num = int(1000 * random.random())
        playAgain = int(input("Play Again? Yes (1)/No (0):" ))
        if playAgain == 1:
            guess = int(input("Guess my number between 1 and 1000 with the fewest possible guesses: "))
