#!/usr/bin/python3

"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to a file,
    after each line containing a specific string.

    Args:
        filename: The filename.
        search_string: The specific string.
        new_string: The new string to insert.
    """
    content = []

    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            content += [line]
            if line.find(search_string) != -1:
                content += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(content))
