#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize instance
        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to retrieve the width"""
        return self._width

    @width.setter
    def width(self, value):
        """Property setter.
        Args:
            value: The new width to assign.
        Raises:
            TypeError: If value is not int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """Property to retrieve the height"""
        return self._height

    @height.setter
    def height(self, value):
        """Property setter.
        Args:
            value: The new height to assign.
        Raises:
            TypeError: If value is not int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
