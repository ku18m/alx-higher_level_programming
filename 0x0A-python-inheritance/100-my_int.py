#!/usr/bin/python3

"""Class MyInt that inherits from Class int."""


class MyInt(int):
    """
    Class MyInt that inherits from Class int.

    Args:
        int: Parent class.
    """

    def __eq__(self, value):
        """Override parent method to make it inverted."""
        return False if super().__eq__(value) else True

    def __ne__(self, value):
        """Override parent method to make it inverted."""
        return False if super().__ne__(value) else True
