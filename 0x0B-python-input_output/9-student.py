#!/usr/bin/python3
"""
This module provides a class Student that defines a student and a method to retrieve a dictionary representation.

Author: Your Name
"""

class Student:
    """
    Student class with public instance attributes: first_name, last_name, and age.
    Provides a method to retrieve a dictionary representation.
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

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance.

        Returns:
        dict: Dictionary representation of the Student instance.
        """
        json_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return json_dict

