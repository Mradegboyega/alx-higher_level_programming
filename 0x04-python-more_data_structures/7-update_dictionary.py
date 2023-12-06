#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Update or add the key-value pair in the dictionary
    a_dictionary[key] = value
    return a_dictionary

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        print("The dictionary is None.")
        return

    # Sort the keys in alphabetic order
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate through the sorted keys and print the key-value pairs
    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
