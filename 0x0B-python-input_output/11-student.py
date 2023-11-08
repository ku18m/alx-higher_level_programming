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

    def to_json(self, attrs=None):
        """
        Public instance method:
        that retrieves a dictionary representation of instance.

        Args:
            attrs: A list of strings,
                only attribute names contained in this list must be retrieved.
        """
        if (type(attrs) is list and all(type(key) is str for key in attrs)):
            key_list = {}
            for key in attrs:
                if hasattr(self, key):
                    key_list[key] = getattr(self, key)
        else:
            key_list = self.__dict__.copy()

        return key_list

    def reload_from_json(self, json):
        """Public method:
        that replaces all attributes of the Student instance.

        Args:
            json: A dict that holds the data.
        """
        for key in json:
            self.__dict__[key] = json[key]
