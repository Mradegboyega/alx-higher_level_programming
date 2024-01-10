#!/usr/bin/python3
"""
This module provides a class Student that defines a student and methods for serialization and deserialization.

Author: Your Name
"""

class Student:
    """
    Student class with public instance attributes: first_name, last_name, and age.
    Provides methods for serialization and deserialization.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.

        Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance with optional attribute filtering.

        Args:
        attrs (list): A list of attribute names to include in the dictionary.

        Returns:
        dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        else:
            attrs = filter(lambda attr: hasattr(self, attr), attrs)

        json_dict = {attr: getattr(self, attr) for attr in attrs}
        return json_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance based on a dictionary representation.

        Args:
        json (dict): Dictionary representation of the Student instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
