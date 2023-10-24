#!/usr/bin/python3
"""class Square"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """Initialize instance
        Args:
            size: size of the square
        Raises:
            TypeError: If size is not int.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        """Class public method to return area.
        Return: Square Area.
        """
        return self._Square__size ** 2
