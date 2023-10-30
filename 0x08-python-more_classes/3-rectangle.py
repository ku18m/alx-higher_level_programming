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
        return self.__width

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
            self.__width = value

    @property
    def height(self):
        """Property to retrieve the height"""
        return self.__height

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
            self.__height = value

    def area(self):
        """Instance public method to retrieve rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Instance public method to retrieve rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """Instance public method to retrieve rectangle str"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (self.__height * (("#" * self.__width) + "\n"))[:-1]
