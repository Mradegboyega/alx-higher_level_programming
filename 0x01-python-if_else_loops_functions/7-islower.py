#!/usr/bin/python3

def islower(c):
    # Check if the input is a single character
    if isinstance(c, str) and len(c) == 1:
        # Check if the ASCII value of the character is within the range of lowercase letters
        return ord('a') <= ord(c) <= ord('z')
    else:
        # Return False for non-single character inputs
        return False

# Test cases
print(islower("a"))  # True
print(islower("H"))  # False
print(islower("4"))  # False
print(islower("!"))  # False
print(islower(4))    # False
