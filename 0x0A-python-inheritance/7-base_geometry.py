#!/usr/bin/python3

"""
class BaseGeometry.
"""


class BaseGeometry:
    """
    class BaseGeometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value.

        Args:
            name: Passed key, (Always string).
            value: The passed value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
