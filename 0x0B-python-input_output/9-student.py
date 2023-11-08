#!/usr/bin/python3

"""Class Student module"""


class Student:
    """Class Student that defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Instantiation.

        Args:
            first_name: Student's first name.
            last_name: Student's last name.
            age: Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Public instance method:
        that retrieves a dictionary representation of instance.
        """
        return self.__dict__.copy()
