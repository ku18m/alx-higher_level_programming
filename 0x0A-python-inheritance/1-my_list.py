#!/usr/bin/python3

"""Class MyList that inherits from Class list."""


class MyList(list):
    """
    Class MyList that inherits from Class list.

    Args:
        obj: Parent class.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list,
        but sorted (ascending sort).
        """
        print(sorted(self))
