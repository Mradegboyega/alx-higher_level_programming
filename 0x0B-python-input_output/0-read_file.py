#!/usr/bin/python3
"""
This module provides a function to read a text file and print its contents to stdout.

Author: Your Name
"""

def read_file(filename=""):
    """
    Read a text file and print its contents to stdout.

    Args:
    filename (str): The name of the file to be read. Default is an empty string.

    Returns:
    None
    """
    file = open(filename, 'r', encoding='utf-8')
    content = file.read()
    print(content)
    file.close()
