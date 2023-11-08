#!/usr/bin/python3

"""Function that creates an Object from a “JSON file”."""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”.

    Args:
        filename: The json filename.
    """
    with open(filename, "r", encoding="utf-8") as jsonFile:
        return json.load(jsonFile)
