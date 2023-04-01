"""
 * ===============================================================
 *
 *       Filename:  HW4Prob3Brodskiy.py
 *       Assignment: Homework 4 Problem 3
 *       Title: Plot Generator 2.0
 *
 *    Description:  Generates a plot from parametric function
 *
 *        Version:  1.0
 *        Created:  04/01/2023
 *       Revision:  N/A
 *         Python:  Python 3.9.2
 *
 *         Author:  M.Brodskiy
 *
 * ===============================================================
""" 

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
x = np.cos(t) + 2 * np.cos(t / 4)
y = np.sin(t) - 2 * np.sin(t / 4)

def parametrize():
    plt.figure()
    plt.plot(y, x)
    plt.grid(axis='both', color='grey', linewidth=0.5, ls='dotted', alpha=0.7)
    plt.title("$\sin(t)-2\sin\left(\dfrac{t}{4}\\right)$ vs. $\cos(t)+2\cos\left(\dfrac{t}{4}\\right)$")
    plt.xlabel("$\cos(t)+2\cos\left(\dfrac{t}{4}\\right)$")
    plt.ylabel("$\sin(t)-2\sin\left(\dfrac{t}{4}\\right)$")
    plt.text(0, 0, "$y=\sin(t)-2\sin\left(\dfrac{t}{4}\\right)$\n$x=\cos(t)+2\cos\left(\dfrac{t}{4}\\right)$", horizontalalignment='center', verticalalignment='center')

parametrize()
plt.show()
