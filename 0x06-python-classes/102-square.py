#!/usr/bin/python3
"""class Square"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """Initialize instance.
        Args:
            size: size of the square.
        """
        self._Square__size = size

    @property
    def size(self):
        """Property to retrieve the size"""
        return self._Square__size

    @size.setter
    def size(self, value):
        """Property setter.
        Args:
            value: The new size to assign
        Raises:
            TypeError: If size is not int.
            ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    def area(self):
        """Instance public method to return area.
        Return: Square Area.
        """
        return (self._Square__size * self._Square__size)

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
