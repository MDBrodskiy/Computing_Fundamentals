"""
 * ===============================================================
 *
 *       Filename:  HW2Prob4Brodskiy.py
 *       Assignment: Homework 2 Problem 4
 *       Title: Tortoise and the Hare
 *
 *    Description:  Simulates the Tortoise and Hare race using functions tortoise_prob and hare_prob 
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
import random

def tortoise_prob():
    rand = random.randint(1,21)
    if rand <= 8:
        return 3
    elif rand <= 10:
        return -6
    else:
        return 1

def hare_prob():
    rand = random.randint(1, 11)
    if rand <= 1:
        return 0
    elif rand <= 4:
        return 9
    elif rand <= 5:
        return -12
    elif rand <= 7:
        return 1
    else:
        return -2

def simulate():

    print("BANG! AND THEY'RE OFF!!!!!")

    posHare = 1
    posTortoise = 1

    for i in range(95):
        print("-",end="")
    print("")

    while posTortoise < 95 and posHare < 95:

        posHare += hare_prob()
        posTortoise += tortoise_prob()

        if posHare <= 0:
            posHare = 1
        if posTortoise <= 0:
            posTortoise = 1

        if posHare >= 95 or posTortoise >= 95:
            break

        for i in range(95):
            if  i == posTortoise == posHare:
                print("OUCH!!!",end="")
            elif i == posHare:
                print("H",end="")
            elif i == posTortoise:
                print("T",end="")
            else:
                print("-",end="")

        print("")

    print("")

    if posHare >= 95 and posTortoise >= 95:
        return 0
    else:
        return 1 if posHare >= 95 else 2

TWins = 0
HWins = 0

for i in range(50):
    result = simulate()
    if result == 1:
        HWins += 1
    elif result == 2:
        TWins += 1

print(f"The tortoise won {TWins} times, the hare won {HWins} times, and they tied {50 - HWins - TWins} times")
