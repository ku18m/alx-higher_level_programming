#!/usr/bin/python3

"""
Function that returns True,
If the object is exactly an instance of the specified class;
otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Function that returns True,
    If the object is exactly an instance of the specified class;
    otherwise False.

    Args:
        obj: The instance to check.
        a_class: The class to check if the instance created from it.
    """

    return True if type(obj) == a_class else False
