#!/usr/bin/python3

"""
A function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class;
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class;
    otherwise False.

    Args:
        obj: The instance to check.
        a_class: The class to check if the instance created from it.
    """

    return isinstance(obj, a_class)
