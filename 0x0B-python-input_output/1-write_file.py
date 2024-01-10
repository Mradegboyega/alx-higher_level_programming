#!/usr/bin/python3
"""
This module provides a function to write a string to a text file and return the number of characters written.

Author: Your Name
"""

def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written.

    Args:
    filename (str): The name of the file to be written. Default is an empty string.
    text (str): The string to be written to the file. Default is an empty string.

    Returns:
    int: The number of characters written to the file.
    """
    # Open file in write mode, creating it if it doesn't exist
    with open(filename, 'w', encoding='utf-8') as file:
        # Write the text to the file and get the number of characters written
        count = file.write(text)

    return count
