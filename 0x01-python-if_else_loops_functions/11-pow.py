#!/usr/bin/python3

def pow(a, b):
    # Check if both inputs are numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Invalid input: both inputs must be numbers")
        return

    # Calculate the result of a to the power of b
    result = a ** b

    # Return the result
    return result
