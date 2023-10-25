#!/usr/bin/python3
"""class Square"""


class Square:
    """class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize instance.
        Args:
            size: size of the square.
            _position: Square positioning.
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
        if (type(position) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position[0]) is not int) or (type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = position

    def area(self):
        """Instance public method to return area.
        Return: Square Area.
        """
        return self._Square__size ** 2

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

    @property
    def position(self):
        """Property to retrieve position"""
        return self._position

    @position.setter
    def position(self, value):
        """Property Setter.
        Args:
            value: The new position to assign.
        Raises:
            TypeError: If not a tuple and has 2 positive ints.
        """
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    def my_print(self):
        """Instance public method to print a Square of size"""
        if self._Square__size != 0:
            for k in range(self._position[1]):
                print()
                k += 1
            for i in range(self._Square__size):
                print(" " * self._position[0], end="")
                print("#" * self._Square__size)
                i += 1
        else:
            print()
