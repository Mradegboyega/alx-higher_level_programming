#!/usr/bin/python3
"""
This module provides a function to write an object to a text file using a JSON representation.

Author: Your Name
"""

def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
    my_obj: The object to be serialized to JSON.
    filename (str): The name of the file to be written.

    Returns:
    None
    """
    try:
        # Convert the object to a JSON string representation
        json_string = str(my_obj).replace("'", '"')

        # Open file in write mode using with statement to ensure proper closure
        with open(filename, 'w', encoding='utf-8') as file:
            # Write the JSON string to the file
            file.write(json_string)
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")
