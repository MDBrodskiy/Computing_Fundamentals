"""
 * ===============================================================
 *
 *       Filename:  HW4Prob6Brodskiy.py
 *       Assignment: Homework 4 Problem 6
 *       Title: Sphere Class
 *
 *    Description:  Defines a Sphere Class, based on Point
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

class Sphere:

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

    @property
    def _vol(self):
        return (4.0 / 3.0) * np.pi * self._radius ** 3

    def __str__(self):
        return f"The volume of the sphere centered at {self.center} with a radius of {self._radius} is equal to {self._vol:.2f}."

class centeredSphere:

    def __init__(self, radius):
        self.center = Point(0,0,0)
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, rad):
        if (rad < 0): raise ValueError("Negative numbers are not permitted for radius values")
        else: self._radius = rad

    @property
    def _vol(self):
        return (4.0 / 3.0) * np.pi * self._radius ** 3

    def __str__(self):
        return f"The volume of the sphere centered at the origin with a radius of {self._radius} is equal to {self._vol:.2f}."

notOrigin = [Sphere(Point(np.random.randint(0,6),np.random.randint(0,6),np.random.randint(0,6)), np.random.randint(1,6)), Sphere(Point(np.random.randint(0,6),np.random.randint(0,6),np.random.randint(0,6)), np.random.randint(1,6)), Sphere(Point(np.random.randint(0,6),np.random.randint(0,6),np.random.randint(0,6)), np.random.randint(1,6)), Sphere(Point(np.random.randint(0,6),np.random.randint(0,6),np.random.randint(0,6)), np.random.randint(1,6))]

Origin = [centeredSphere(np.random.randint(5,11)), centeredSphere(np.random.randint(5,11))]

allSphere = notOrigin + Origin
for i in allSphere:
    print(i)

