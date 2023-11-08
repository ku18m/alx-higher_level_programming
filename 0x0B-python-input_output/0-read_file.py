#!/usr/bin/python3

"""Function that reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: The name of the file to open and print.
    """
    with open(filename, "r", encoding="utf-8") as myFile:
        content = myFile.read()
        print(content, end="")
