#!/usr/bin/python3
"""

Prints 2 new lines after ".?:" characters.

"""


def text_indentation(text):
    """
    Prints 2 new lines after ".?:" characters.

    Args:
        text: The string to print.

    Returns:
        No return.

    Raises:
        TypeError: If text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    cloned = text[:]

    for k in ".?:":
        list_text = cloned.split(k)
        cloned = ""
        for i in list_text:
            i = i.strip(" ")
            if cloned == "":
                cloned = i + k
            else:
                cloned += "\n\n" + i + k

    print(cloned[:-3], end="")
