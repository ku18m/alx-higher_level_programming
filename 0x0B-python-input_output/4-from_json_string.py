#!/usr/bin/python3

"""Function that returns an object represented by a JSON string."""
import json


def from_json_string(my_str):
    """
    Function that returns an object represented by a JSON string.

    Args:
        my_str: The json str to be returned as object.
    """
    return json.loads(my_str)
