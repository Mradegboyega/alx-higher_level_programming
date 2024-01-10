#!/usr/bin/python3
"""
This module provides a function to create an object from a JSON file.

Author: Your Name
"""

def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
    filename (str): The name of the JSON file to read.

    Returns:
    object: The Python object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the content of the file
        json_string = file.read()

        # Convert the JSON string to a Python object using eval
        my_obj = eval(json_string)

    return my_obj
