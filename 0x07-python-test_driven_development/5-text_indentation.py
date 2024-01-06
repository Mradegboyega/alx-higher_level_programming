#!/usr/bin/python3

"""
Module: 5-text_indentation
This module provides a function for printing text with 2 new lines after '.', '?', and ':'.

Functions:
- text_indentation(text): Prints text with 2 new lines after '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', and ':'.

    Args:
    - text: The input text.

    Raises:
    - TypeError: If 'text' is not a string.

    Returns:
    - None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    for char in text:
        print(char, end='')
        if char in punctuations:
            print('\n\n', end='')
