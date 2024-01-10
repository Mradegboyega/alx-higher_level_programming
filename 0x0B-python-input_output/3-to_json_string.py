#!/usr/bin/python3
"""
This module provides a function to return the JSON representation of an object (string).

Author: Your Name
"""

def to_json_string(my_obj):
    """
    Return the JSON representation of an object.

    Args:
    my_obj: The object to be serialized to JSON.

    Returns:
    str: The JSON representation of the object.
    """
    try:
        # Importing is not allowed, so manually implement JSON serialization
        json_string = str(my_obj).replace("'", '"')
        return json_string
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
