#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_integers = set()

    # Iterate through each element in the list
    for item in my_list:
        # Add the element to the set (sets automatically discard duplicates)
        unique_integers.add(item)

    # Sum up all unique integers
    result_sum = sum(unique_integers)

    return result_sum
