#!/usr/bin/python3
"""
This module provides a function to append a string at the end of a text file and return the number of characters added.

Author: Your Name
"""

def append_write(filename="", text=""):
    """
    Append a string to the end of a text file and return the number of characters added.

    Args:
    filename (str): The name of the file to be appended. Default is an empty string.
    text (str): The string to be appended to the file. Default is an empty string.

    Returns:
    int: The number of characters added to the file.
    """
    # Open file in append mode, creating it if it doesn't exist
    with open(filename, 'a', encoding='utf-8') as file:
        # Append the text to the file and get the number of characters added
        count = file.write(text)

    return count
