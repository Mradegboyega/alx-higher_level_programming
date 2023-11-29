#!/usr/bin/python3

def uppercase(s):
    # Check if the input is a string
    if not isinstance(s, str):
        # If not a string, print a new line and return
        print()
        return

    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the character to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            # Keep non-lowercase characters unchanged
            uppercase_char = char

        # Use the first print function with string format
        print("{}".format(uppercase_char), end="")

    # Use the second print function to add a new line
    print()

