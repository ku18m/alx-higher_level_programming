#!/usr/bin/python3

"""Function that writes a string to a text file (UTF8),
and returns the number of characters written."""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8),
    and returns the number of characters written.

    Args:
        filename: The name of the file to open and print.
        text: The text to be written.
    """
    with open(filename, "w", encoding="utf-8") as myFile:
        return myFile.write(text)
