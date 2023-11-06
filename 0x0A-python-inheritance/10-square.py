#!/usr/bin/python3

"""
class Square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle.

    Args:
        Rectangle: The parent class.
    """

    def __init__(self, size):
        """
        Public instance method to initialize the instance.

        Args:
            size: Square size
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
