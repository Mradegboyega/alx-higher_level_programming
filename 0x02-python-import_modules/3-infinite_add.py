#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Extract arguments starting from the first (index 1)
    arguments = argv[1:]

    # Convert arguments to integers and sum them
    result = sum(int(arg) for arg in arguments)

    print(result)
