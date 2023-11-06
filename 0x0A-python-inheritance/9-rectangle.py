#!/usr/bin/python3

"""
class Rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry.

    Args:
        BaseGeometry: The parent class.
    """

    def __init__(self, width, height):
        """
        Public instance method to create instance.

        Args:
            width: Rectangle width.
            height: Rectangle height.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Public instance method to retrieve rectangle area.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Public instance method to represent class as string.
        """

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
