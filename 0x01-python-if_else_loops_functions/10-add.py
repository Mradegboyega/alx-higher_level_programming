#!/usr/bin/python3

def add(a, b):
    # Check if both inputs are integers
    if not isinstance(a, int) or not isinstance(b, int):
        print("Invalid input: both inputs must be integers")
        return None

    # Add the two integers and return the result
    result = a + b
    return result
