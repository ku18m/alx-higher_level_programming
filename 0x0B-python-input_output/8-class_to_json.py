#!/usr/bin/python3

"""Function that returns the dictionary description,
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object."""
import json


def class_to_json(obj):
    """
    Function that returns the dictionary description,
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object.

    Args:
        obj: An instance of a class.
    """
    obj_dict = {}

    if "__dict__" in dir(obj):
        obj_dict = obj.__dict__.copy()

    return obj_dict
