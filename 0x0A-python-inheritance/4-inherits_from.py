#!/usr/bin/python3

"""
A function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    A function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
        obj: The instance to check.
        a_class: The class to check if the instance inherited from it.
    """

    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
