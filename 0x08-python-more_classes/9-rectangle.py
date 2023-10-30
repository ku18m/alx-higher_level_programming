#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new Rectangle instance"""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Class static method that returns the biggest rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_2.area() > rect_1.area():
                return rect_2
            return rect_1

    def __init__(self, width=0, height=0):
        """Initialize instance
        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        Rectangle.number_of_instances += 1
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
        return (self.__height *
                ((str(self.print_symbol) * self.__width) + "\n"))[:-1]

    def __repr__(self):
        """Instance public method to retrieve string representation"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Instance public method to print deletion message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
