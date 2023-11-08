#!/usr/bin/python3

"""Function that appends a string at the end of a text file (UTF8),
and returns the number of characters added."""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8),
    and returns the number of characters added.

    Args:
        filename: The name of the file to open and print.
        text: The text to be written.
    """
    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)
