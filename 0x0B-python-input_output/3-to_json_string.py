#!/usr/bin/python3

"""Function that returns the JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be returned as json str representation.
    """
    return json.dumps(my_obj)
