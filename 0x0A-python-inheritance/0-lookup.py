#!/usr/bin/python3

"""Function that returns the list of available attributes and methods."""


def lookup(obj):
    """
    Function that returns the list of available attributes and methods.

    Args:
        obj: The object to return it's attributes and methods.
    """

    return dir(obj)
