#!/usr/bin/python3
"""
This module provides a function to convert an instance of a class to a JSON-serializable dictionary.

Author: Your Name
"""

def class_to_json(obj):
    """
    Convert an instance of a class to a JSON-serializable dictionary.

    Args:
    obj: An instance of a class.

    Returns:
    dict: Dictionary representation of the class instance.
    """
    json_dict = {}

    # Iterate over the attributes of the class
    for key, value in obj.__dict__.items():
        # Check if the attribute is of a serializable type
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
