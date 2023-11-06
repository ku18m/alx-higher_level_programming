#!/usr/bin/python3

"""A function that adds a new attribute to an object if it's possible."""


def add_attribute(obj, key, value):
    """
    A function that adds a new attribute to an object if it's possible.

    Args:
        obj: The object to insert the new attribute in it.
        key: The attribute key.
        value: The attribute value.

    Raises:
        TypeError: If the object can't have new attribute.
    """

    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
