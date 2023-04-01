"""
 * ===============================================================
 *
 *       Filename:  HW4Prob2Brodskiy.py
 *       Assignment: Homework 4 Problem 2
 *       Title: Plot Generator
 *
 *    Description:  Generates two types of plots for given functions
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

x = np.linspace(-1.5,1.5,1000)
y = np.linspace(-1,1,1000)

def onePlot():
    plt.figure()
    plt.plot(y, np.sin(np.exp(2*x)), y, np.cos(np.exp(-2*x)), '-r')
    plt.grid(axis='both', color='grey', linewidth=0.5, ls='dotted', alpha=0.7)
    plt.title("Two Sinusoidal Functions on One Graph")
    plt.xlabel("$x$-axis from -1.5 to 1.5")
    plt.ylabel("$y$-axis from -1 to 1")
    plt.legend(["$y_1=\sin(e^{2x})$", "$y_2=\cos(e^{-2x})$"])
    plt.text(.1, 1.05,'$\sin(e^{2x})$', horizontalalignment='center', verticalalignment='center')
    plt.text(-.6, 1.05,'$\cos(e^{-2x})$', horizontalalignment='center', verticalalignment='center')

def twoPlot():
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(y, np.sin(np.exp(2*x)), '-b')
    plt.title("Two Sinusoidal Functions on Two Graphs")
    plt.ylabel("$\sin(e^{2x})$")
    plt.grid(axis='both', color='grey', linewidth=0.5, ls='dotted', alpha=0.7)
    plt.text(-.1, .9,'$\sin(e^{2x})$', horizontalalignment='center', verticalalignment='center')
    plt.legend(["$y_1=\sin(e^{2x})$"])
    plt.subplot(2, 1, 2)
    plt.plot(y, np.cos(np.exp(-2*x)), '-r')
    plt.xlabel("$x$-axis")
    plt.ylabel("$\cos(e^{-2x})$")
    plt.legend(["$y_2=\cos(e^{-2x})$"])
    plt.text(-.1, .75,'$\cos(e^{-2x})$', horizontalalignment='center', verticalalignment='center')
    plt.grid(axis='both', color='grey', linewidth=0.5, ls='dotted', alpha=0.7)

onePlot()
twoPlot()
plt.show()
