#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Create a new set to store elements present in only one set
    diff_set = set()

    # Iterate through each element in the first set
    for element in set_1:
        # If the element is not present in the second set, add it to the diff set
        if element not in set_2:
            diff_set.add(element)

    # Iterate through each element in the second set
    for element in set_2:
        # If the element is not present in the first set, add it to the diff set
        if element not in set_1:
            diff_set.add(element)

    return diff_set
