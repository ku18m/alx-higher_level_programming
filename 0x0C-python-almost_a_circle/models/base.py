#!/usr/bin/python3

"""Class Base"""


import json


class Base:
    """
    Class Base:
        This class will be the “base” of all other classes in this project;
        The goal of it is to manage id attribute in all your future classes,
        and to avoid duplicating the same code (by extension, same bugs).
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.

        Args:
            id = Instances counter.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Class static method that returns json string res of list dicts."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON str res of list_objs to a file.

        Args:
            list_objs: A list of instances.
        """
        dicts = []
        filename = f"{cls.__name__}.json"

        if list_objs is not None:
            for instance in list_objs:
                dicts.append(instance.to_dictionary())

        dicts_json = cls.to_json_string(dicts)
        print(dicts_json, type(dicts_json))

        with open(filename, "w") as file:
            file.write(dicts_json)
