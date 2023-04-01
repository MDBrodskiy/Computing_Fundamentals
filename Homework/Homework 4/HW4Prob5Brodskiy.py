"""
 * ===============================================================
 *
 *       Filename:  HW4Prob5Brodskiy.py
 *       Assignment: Homework 4 Problem 5
 *       Title: Circle Class
 *
 *    Description:  Defines a Circle Class, based on Point
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

import matplotlib.pyplot as plt
import numpy as np

class Point:

    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z

    @property
    def _r(self):
        return np.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def __str__(self):
        return str((self.x, self.y, self.z))

    def __eq__(self, other):
        return (self._r == other._r)

    def __lt__(self, other):
        return (self._r < other._r)

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def asdict(self):
        return {'x':self.x, 'y':self.y, 'z':self.z}


class Circle():

    def __init__(self, center, radius):
        self.center = center
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, rad):
        if (rad < 0): raise ValueError("Negative numbers are not permitted for radius values")
        else: self._radius = rad

    def draw(self):
        t = np.linspace(-np.pi, np.pi, 1000)
        y = (self._radius * np.sin(t)) + self.center.x
        x = (self._radius * np.cos(t)) + self.center.y

        plt.figure()
        plt.plot(y, x)
        plt.grid(axis='both', color='grey', linewidth=0.5, ls='dotted', alpha=0.7)
        plt.title(f"Circle of radius {self._radius} centered at ({self.center.x}, {self.center.y})")
        plt.xlabel("$x$-axis")
        plt.ylabel("$y$-axis")
        plt.legend(['$(x-$' + str(self.center.x) + '$)^2+(y-$' + str(self.center.y) + '$)^2=$' + str(self._radius ** 2)])
        plt.text(self.center.x, self.center.y, '$(x-$' + str(self.center.x) + '$)^2+(y-$' + str(self.center.y) + '$)^2=$' + str(self._radius ** 2), horizontalalignment='center', verticalalignment='center')
        plt.show()

c = Circle(Point(1,4), 2)
c.draw()
