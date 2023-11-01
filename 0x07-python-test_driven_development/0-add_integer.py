#!/usr/bin/python3
"""
Adds two integers

"""


def add_integer(a, b=98):
    """
    Returns (int a + int b).

    Args:
        a: first number.
        b: second number.

    Returns:
        The addition of the two given numbers.

    Raises:
        TypeError: If a or b aren't integer or float numbers.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
