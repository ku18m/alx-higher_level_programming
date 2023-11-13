#!/usr/bin/python3

"""Class Base"""


import json
import csv


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

        with open(filename, "w") as file:
            file.write(dicts_json)

    @staticmethod
    def from_json_string(json_string):
        """Class static method that returns a list of json str res.

        Args:
            json_string: The json string.
        """
        normal_list = []

        if json_string is not None:
            normal_list = json.loads(json_string)

        return normal_list

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with giving attributes.

        Args:
            dictionary: The attributes dictionary.
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)

        instance.update(**dictionary)

        return instance

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances."""
        filename = f"{cls.__name__}.json"
        instances_list = []

        try:
            with open(filename, "r") as file:
                dicts_json = cls.from_json_string(file.read())
                for dict in dicts_json:
                    instance = cls.create(**dict)
                    instances_list.append(instance)
        except FileNotFoundError:
            pass

        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Class method that writes the JSON str res of list_objs to a file.

        Args:
            list_objs: A list of instances.
        """
        filename = f"{cls.__name__}.csv"

        with open(filename, "w", newline="") as file:
            if list_objs is not None:
                if cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                else:
                    keys = ["id", "size", "x", "y"]

                file_csv = csv.DictWriter(file, fieldnames=keys)

                for instance in list_objs:
                    file_csv.writerow(instance.to_dictionary())
            else:
                file.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """Class method that returns a list of instances."""
        filename = f"{cls.__name__}.csv"
        instances_list = []

        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                else:
                    keys = ["id", "size", "x", "y"]
                dicts = csv.DictReader(file, fieldnames=keys)
                dicts = [
                    dict([k, int(v)] for k, v in d.items()) for d in dicts
                ]
                instances_list = [cls.create(**d) for d in dicts]
        except FileNotFoundError:
            pass

        return instances_list
