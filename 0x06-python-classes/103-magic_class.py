#!/usr/bin/python3
"""Class MagicClass"""

import math


class MagicClass:
    """Creates a circle"""

    def __init__(self, radius=0):
        """Initialize instance.
        Arg:
            radius: The radius of the new circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Retrieve the area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Retrieve the circumference"""
        return (2 * math.pi * self.__radius)
