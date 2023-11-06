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
