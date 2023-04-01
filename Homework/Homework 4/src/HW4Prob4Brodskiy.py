"""
 * ===============================================================
 *
 *       Filename:  HW4Prob4Brodskiy.py
 *       Assignment: Homework 4 Problem 4
 *       Title: Point Class Creator
 *
 *    Description:  Defines a Point Class
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

# cur_point = Point(1, 2, 3)
# print(cur_point._r)
# cur_point._r = 5 # Read-only attribute modification causes error
# print(cur_point._r)
