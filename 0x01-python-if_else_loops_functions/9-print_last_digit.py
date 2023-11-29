#!/usr/bin/python3

def print_last_digit(number):
    # Check if the input is an integer
    if not isinstance(number, int):
        print("Invalid input: not an integer")
        return

    # Calculate the last digit
    last_digit = abs(number) % 10

    # Use the print function with string format to print the last digit
    print("{}".format(last_digit))

    # Return the last digit
    return last_digit
